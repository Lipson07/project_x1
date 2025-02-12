const form = document.getElementById('registrationForm');
const firstName = document.getElementById('firstName');
const lastName = document.getElementById('lastName');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;

    // Validate First Name
    if (firstName.value.trim().length < 2) {
        showError('firstName');
        isValid = false;
    } else {
        hideError('firstName');
    }

    // Validate Last Name
    if (lastName.value.trim().length < 2) {
        showError('lastName');
        isValid = false;
    } else {
        hideError('lastName');
    }

    // Validate Email
    if (!isValidEmail(email.value)) {
        showError('email');
        isValid = false;
    } else {
        hideError('email');
    }

    // Validate Password
    if (password.value.length < 8) {
        showError('password');
        isValid = false;
    } else {
        hideError('password');
    }

    // Validate Confirm Password
    if (password.value !== confirmPassword.value) {
        showError('confirmPassword');
        isValid = false;
    } else {
        hideError('confirmPassword');
    }

    if (isValid) {
        // Here you would typically send the data to your server
        console.log('Form submitted successfully');
        alert('Регистрация успешно завершена!');
        form.reset();
    }
});

function isValidEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function showError(fieldId) {
    const field = document.getElementById(fieldId);
    const errorDiv = document.getElementById(fieldId + 'Error');
    field.parentElement.classList.add('error');
    errorDiv.style.display = 'block';
}

function hideError(fieldId) {
    const field = document.getElementById(fieldId);
    const errorDiv = document.getElementById(fieldId + 'Error');
    field.parentElement.classList.remove('error');
    errorDiv.style.display = 'none';
}