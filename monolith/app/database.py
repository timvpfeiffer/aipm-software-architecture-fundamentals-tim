"""SQLite storage for rooms and bookings."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "officerooms.db"

ROOMS = ["Aurora", "Birch", "Cedar"]
TIME_SLOTS = [f"{hour:02d}:00" for hour in range(9, 17)]


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS rooms ("
            "id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)"
        )
        conn.execute(
            "CREATE TABLE IF NOT EXISTS bookings ("
            "id INTEGER PRIMARY KEY, "
            "room_id INTEGER NOT NULL REFERENCES rooms(id), "
            "date TEXT NOT NULL, "
            "time_slot TEXT NOT NULL, "
            "person_name TEXT NOT NULL, "
            "created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, "
            "UNIQUE(room_id, date, time_slot))"
        )
        for name in ROOMS:
            conn.execute("INSERT OR IGNORE INTO rooms (name) VALUES (?)", (name,))


def list_rooms():
    with connect() as conn:
        return [dict(r) for r in conn.execute("SELECT id, name FROM rooms ORDER BY id")]


def list_bookings(date):
    with connect() as conn:
        rows = conn.execute(
            "SELECT b.id, b.room_id, r.name AS room, b.date, b.time_slot, b.person_name "
            "FROM bookings b JOIN rooms r ON r.id = b.room_id "
            "WHERE b.date = ? ORDER BY b.time_slot, r.id",
            (date,),
        )
        return [dict(r) for r in rows]


def find_booking(room_id, date, time_slot):
    with connect() as conn:
        row = conn.execute(
            "SELECT id FROM bookings WHERE room_id = ? AND date = ? AND time_slot = ?",
            (room_id, date, time_slot),
        ).fetchone()
        return row is not None


def insert_booking(room_id, date, time_slot, person_name):
    """Insert a booking. Raises sqlite3.IntegrityError on a duplicate slot."""
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO bookings (room_id, date, time_slot, person_name) "
            "VALUES (?, ?, ?, ?)",
            (room_id, date, time_slot, person_name),
        )
        return cur.lastrowid
