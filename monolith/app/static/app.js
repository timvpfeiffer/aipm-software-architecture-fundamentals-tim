const dateInput = document.getElementById("date");
const roomSelect = document.getElementById("room");
const timeSelect = document.getElementById("time");
const messageBox = document.getElementById("message");

function showMessage(text, kind) {
  messageBox.textContent = text;
  messageBox.className = kind;
}

async function loadOptions() {
  const [rooms, slots] = await Promise.all([
    fetch("/api/rooms").then(r => r.json()),
    fetch("/api/slots").then(r => r.json()),
  ]);
  roomSelect.innerHTML = rooms.map(r => `<option value="${r.id}">${r.name}</option>`).join("");
  timeSelect.innerHTML = slots.map(s => `<option>${s}</option>`).join("");
}

async function refresh() {
  const date = dateInput.value;
  const [availability, bookings] = await Promise.all([
    fetch(`/api/availability?date=${date}`).then(r => r.json()),
    fetch(`/api/bookings?date=${date}`).then(r => r.json()),
  ]);

  document.getElementById("availability").innerHTML = availability.map(room => `
    <div class="room"><strong>${room.room}</strong>
      <div class="slots">${room.slots.map(s =>
        `<span class="slot ${s.available ? "free" : "taken"}">${s.time_slot}</span>`).join("")}</div>
    </div>`).join("");

  const list = document.getElementById("bookings");
  list.innerHTML = bookings.length
    ? bookings.map(b => `<li>${b.time_slot} - ${b.room} - ${b.person_name}</li>`).join("")
    : "<li>No bookings yet.</li>";
}

document.getElementById("booking-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const res = await fetch("/api/bookings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      room_id: Number(roomSelect.value),
      date: dateInput.value,
      time_slot: timeSelect.value,
      person_name: document.getElementById("name").value,
    }),
  });
  const data = await res.json();
  if (res.ok) {
    showMessage(data.message, "success");
  } else {
    const detail = Array.isArray(data.detail) ? data.detail.map(d => d.msg).join(" ") : data.detail;
    showMessage(detail, "error");
  }
  refresh();
});

dateInput.addEventListener("change", refresh);

(async () => {
  dateInput.value = new Date().toISOString().slice(0, 10);
  await loadOptions();
  refresh();
})();
