"""OfficeRooms monolith: serves the web page, applies booking rules, stores data."""
import sqlite3
from datetime import date as date_type
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, field_validator

from . import database

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="OfficeRooms (monolith)")


@app.on_event("startup")
def startup():
    database.init_db()


class BookingRequest(BaseModel):
    room_id: int
    date: str
    time_slot: str
    person_name: str

    @field_validator("person_name")
    @classmethod
    def name_not_empty(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Name is required.")
        return v

    @field_validator("date")
    @classmethod
    def valid_date(cls, v):
        try:
            date_type.fromisoformat(v)
        except ValueError:
            raise ValueError("Date must look like YYYY-MM-DD.")
        return v

    @field_validator("time_slot")
    @classmethod
    def valid_slot(cls, v):
        if v not in database.TIME_SLOTS:
            raise ValueError("Unknown time slot.")
        return v


@app.get("/api/rooms")
def get_rooms():
    return database.list_rooms()


@app.get("/api/slots")
def get_slots():
    return database.TIME_SLOTS


@app.get("/api/availability")
def get_availability(date: str):
    try:
        date_type.fromisoformat(date)
    except ValueError:
        raise HTTPException(status_code=422, detail="Date must look like YYYY-MM-DD.")
    taken = {(b["room_id"], b["time_slot"]) for b in database.list_bookings(date)}
    return [
        {
            "room_id": room["id"],
            "room": room["name"],
            "slots": [
                {"time_slot": s, "available": (room["id"], s) not in taken}
                for s in database.TIME_SLOTS
            ],
        }
        for room in database.list_rooms()
    ]


@app.get("/api/bookings")
def get_bookings(date: str):
    return database.list_bookings(date)


@app.post("/api/bookings", status_code=201)
def create_booking(req: BookingRequest):
    room = next((r for r in database.list_rooms() if r["id"] == req.room_id), None)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found.")
    # Booking rule: a room can only be booked once per date and time slot.
    conflict = HTTPException(
        status_code=409,
        detail="This slot is already booked, please pick another.",
    )
    if database.find_booking(req.room_id, req.date, req.time_slot):
        raise conflict
    try:
        booking_id = database.insert_booking(
            req.room_id, req.date, req.time_slot, req.person_name
        )
    except sqlite3.IntegrityError:
        # Safety net: the database UNIQUE constraint caught a simultaneous booking.
        raise conflict
    return {
        "id": booking_id,
        "room": room["name"],
        "date": req.date,
        "time_slot": req.time_slot,
        "person_name": req.person_name,
        "message": f"Booked: {room['name']}, {req.date}, {req.time_slot}, for {req.person_name}",
    }


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
