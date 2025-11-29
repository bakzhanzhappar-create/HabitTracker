async function fetchHabits() {
    const tbody = document.getElementById("habits-body");
    const emptyMsg = document.getElementById("list-empty");
    tbody.innerHTML = "";

    try {
        const res = await fetch("/habits");
        if (!res.ok) {
            throw new Error("Failed to load habits");
        }
        const habits = await res.json();
        if (!habits.length) {
            emptyMsg.style.display = "block";
            return;
        }
        emptyMsg.style.display = "none";

        for (const habit of habits) {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${habit.id}</td>
                <td>${habit.name}</td>
                <td>${habit.minutes}</td>
                <td>${habit.weight}</td>
                <td>${habit.date}</td>
                <td><button data-id="${habit.id}" class="delete-btn">Delete</button></td>
            `;
            tbody.appendChild(tr);
        }
    } catch (e) {
        emptyMsg.textContent = "Error loading habits";
        emptyMsg.style.display = "block";
    }
}

async function createHabit(event) {
    event.preventDefault();
    const nameInput = document.getElementById("name");
    const minutesInput = document.getElementById("minutes");
    const weightInput = document.getElementById("weight");
    const errorEl = document.getElementById("form-error");

    const name = nameInput.value.trim();
    const minutes = Number(minutesInput.value);
    const weight = Number(weightInput.value);

    if (!name) {
        errorEl.textContent = "Name is required.";
        return;
    }
    if (!(minutes > 0 && minutes <= 50)) {
        errorEl.textContent = "Minutes must be between 1 and 50.";
        return;
    }
    if (!(weight >= 1 && weight <= 10)) {
        errorEl.textContent = "Importance must be between 1 and 10.";
        return;
    }

    try {
        const res = await fetch("/habits", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name, minutes, weight}),
        });
        if (!res.ok) {
            const data = await res.json().catch(() => ({}));
            errorEl.textContent = data.detail || "Failed to save habit.";
            return;
        }

        errorEl.textContent = "";
        nameInput.value = "";
        minutesInput.value = "";
        weightInput.value = "";
        await fetchHabits();
    } catch (e) {
        errorEl.textContent = "Network error.";
    }
}

async function deleteHabit(id) {
    try {
        const res = await fetch(`/habits/${id}`, {
            method: "DELETE",
        });
        if (!res.ok && res.status !== 404) {
            // if 404, just refresh list
            throw new Error("Failed to delete habit");
        }
        await fetchHabits();
    } catch (e) {
        console.error(e);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("habit-form");
    form.addEventListener("submit", createHabit);

    const tbody = document.getElementById("habits-body");
    tbody.addEventListener("click", (event) => {
        const target = event.target;
        if (target.matches(".delete-btn")) {
            const id = target.getAttribute("data-id");
            if (id) {
                deleteHabit(Number(id));
            }
        }
    });

    fetchHabits();
});


