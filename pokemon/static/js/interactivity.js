document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("table tbody tr");
    rows.forEach((row) => {
        row.addEventListener("click", () => {
            rows.forEach((r) => r.classList.remove("selected-row"));
            row.classList.add("selected-row");
        });
    });
});

