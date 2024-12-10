document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("loginForm");
    const emailInput = document.getElementById("correo");

    form.addEventListener("submit", function (e) {
        const emailValue = emailInput.value.trim();
        if (!validateEmail(emailValue)) {
            e.preventDefault(); // Evita el envío del formulario
            emailInput.classList.add("is-invalid");
        } else {
            emailInput.classList.remove("is-invalid");
        }
    });

    // Validación del correo electrónico
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
