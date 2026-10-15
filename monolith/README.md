# OfficeRooms (monolith)

One Python program serves the web page, applies the booking rules, and stores
data in a local SQLite file.

## Run

```bash
cd monolith
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- App: <http://127.0.0.1:8000>
- API docs: <http://127.0.0.1:8000/docs>
- Stop with Ctrl+C. Reset data by deleting `data/officerooms.db`.

## Where things live

| Part | Files |
|---|---|
| Browser interface | `app/static/index.html`, `style.css`, `app.js` |
| API and booking rule | `app/main.py` |
| Database | `app/database.py`, `data/officerooms.db` |

The conflict rule is checked in `main.py` before saving. A
`UNIQUE(room_id, date, time_slot)` constraint in the database is the safety net.

## Test the five acceptance criteria

1. **See rooms and slots:** open the page and pick a date. Or run
   `curl "http://127.0.0.1:8000/api/availability?date=2030-01-01"`.
2. **Create a booking:** submit name, room, time. An empty name is rejected.
3. **Conflict rejected:** book the same room, date, and time again. Expect HTTP
   409 and "This slot is already booked, please pick another."
4. **Refresh keeps bookings:** book, refresh the browser (and optionally restart
   the server). The booking is still listed.
5. **Confirmation shown:** after a successful booking the page shows
   "Booked: Room, date, time, for Name".

Use fake names only. There is no sign-in.
