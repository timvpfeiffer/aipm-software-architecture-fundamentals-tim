# Prototype Brief

## Product

- **Product name:** OfficeRooms (a small shared-office room-booking tool)
- **Target user:** An employee in a shared office who needs a meeting room for a specific time slot.
- **Problem to solve:** Rooms get double-booked or people don't know which rooms are free. Booking by chat or spreadsheet is slow and error-prone.
- **Success moment:** The user picks a free room and time, clicks book, and immediately sees a confirmation. If the slot is taken, they see a clear message instead.

## Core User Journey

Describe the smallest end-to-end journey both prototypes must support.

1. The user opens the app and sees the rooms with their available time slots for a chosen date.
2. The user picks a room, date, and time, enters their name, and submits the booking. If the slot is already taken, they see a clear conflict message and can choose another slot.
3. On success, the user sees a confirmation. After a browser refresh, the booking is still there.

## Required Capabilities

- A browser-based interface.
- A backend API.
- Persistent storage for bookings.
- A visible confirmation or notification after a successful booking.

## Acceptance Criteria

- A participant can see available rooms and time slots.
- A participant can create a booking with a name, room, date, and time.
- A conflicting booking is rejected with a clear message.
- Refreshing the browser does not lose a confirmed booking.
- The application shows a confirmation after a successful booking.

## Constraints

- Build only the core user journey. Do not add sign-in, payments, calendars,
  email delivery, or production deployment.
- Use local development data only. Do not enter personal or sensitive data.
- The agent must explain how to run and test the prototype.
- The agent must not commit, push, install unrelated tooling, or connect external
  services without approval.

## Architecture Variant

- **Variant:** Monolith
- **Why this variant is being tested:** It's the simplest baseline. One application holds the interface, booking logic, and storage, so it is the quickest way to get the shared user journey working and to see how a single deployable unit behaves.
- **Expected trade-off:** Fast to build and easy to run and debug locally, but all logic is coupled in one place. A change or failure in one area can affect everything, and it scales and splits across teams less easily.

## Evidence From Testing

- **What worked:**
- **What failed or was unclear:**
- **What changed between variants:**
