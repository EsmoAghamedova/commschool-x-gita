const ROOMS = [
    { number: 101, type: "Single", price: 80, guests: 1, available: true },
    { number: 203, type: "Double", price: 140, guests: 2, available: true },
    { number: 301, type: "Suite", price: 250, guests: 4, available: true },
    { number: 202, type: "Double", price: 130, guests: 2, available: false },
];

function findRoom(roomNumber) {
    return ROOMS.find((r) => r.number === Number(roomNumber)) || null;
}

function renderRooms() {
    const grid = document.getElementById("room-grid");
    grid.innerHTML = "";

    ROOMS.forEach((room) => {
        const card = document.createElement("article");
        card.className = "room-key" + (room.available ? "" : " is-booked");

        card.innerHTML = `
      <div class="key-hole"></div>
      <div class="key-number">${room.number}</div>
      <h3 class="key-type">${room.type}</h3>
      <p class="key-price"><span class="price-amount">${room.price}</span> GEL <span class="price-unit">/ ღამე</span></p>
      <p class="key-guests">მაქს. ${room.guests} სტუმარი</p>
      <span class="key-status ${room.available ? "available" : "booked"}">
        ${room.available ? "თავისუფალია" : "დაკავებულია"}
      </span>
    `;

        if (room.available) {
            card.addEventListener("click", () => {
                window.location.href = `booking.html?room=${room.number}`;
            });
        }

        grid.appendChild(card);
    });
}

function initBookingForm() {
    const roomNumberInput = document.getElementById("room-number");
    const nightsInput = document.getElementById("nights");
    const totalValue = document.getElementById("total-value");
    const form = document.getElementById("booking-form");
    const message = document.getElementById("booking-message");

    const params = new URLSearchParams(window.location.search);
    const prefillRoom = params.get("room");
    if (prefillRoom) {
        roomNumberInput.value = prefillRoom;
    }

    function updateTotal() {
        const room = findRoom(roomNumberInput.value);
        const nights = Number(nightsInput.value) || 0;

        if (room && nights > 0) {
            totalValue.textContent = `${(room.price * nights).toFixed(2)} GEL`;
        } else {
            totalValue.textContent = "— GEL";
        }
    }

    updateTotal();
    roomNumberInput.addEventListener("input", updateTotal);
    nightsInput.addEventListener("input", updateTotal);

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        message.classList.remove("success", "error");

        const name = document.getElementById("guest-name").value.trim();
        const room = findRoom(roomNumberInput.value);
        const nights = Number(nightsInput.value);

        if (!room) {
            message.textContent = `❌ ოთახი #${roomNumberInput.value} ვერ მოიძებნა.`;
            message.classList.add("error");
            return;
        }

        if (!room.available) {
            message.textContent = `❌ ოთახი #${room.number} ამჟამად დაკავებულია.`;
            message.classList.add("error");
            return;
        }

        const total = (room.price * nights).toFixed(2);

        const query = new URLSearchParams({
            name,
            room: room.number,
            type: room.type,
            nights,
            total,
        });

        window.location.href = `status.html?${query.toString()}`;
    });
}

function initStatusPage() {
    const container = document.getElementById("status-summary");
    const params = new URLSearchParams(window.location.search);

    const name = params.get("name");
    const room = params.get("room");
    const type = params.get("type");
    const nights = params.get("nights");
    const total = params.get("total");

    if (!name || !room) {
        container.innerHTML = `
      <div class="status-empty">
        <p>ჯერ არცერთი დაჯავშნა არ არის დადასტურებული.</p>
        <a href="booking.html" class="cta">დაჯავშნის გაკეთება →</a>
      </div>
    `;
        return;
    }

    container.innerHTML = `
    <div class="status-card">
      <span class="key-status available">დადასტურებულია</span>
      <h3>${name}, თქვენი ოთახი მზადაა</h3>
      <dl>
        <div><dt>ოთახი</dt><dd>#${room} (${type})</dd></div>
        <div><dt>ღამეების რაოდენობა</dt><dd>${nights}</dd></div>
        <div><dt>ჯამური ღირებულება</dt><dd>${total} GEL</dd></div>
      </dl>
      <a href="rooms.html" class="cta">სხვა ოთახის დაჯავშნა →</a>
    </div>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("room-grid")) renderRooms();
    if (document.getElementById("booking-form")) initBookingForm();
    if (document.getElementById("status-summary")) initStatusPage();
});