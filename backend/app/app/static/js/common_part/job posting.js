// Функционал фильтрации вакансий
document.querySelector('.filters__form').addEventListener('input', (e) => {
    // Здесь можно добавить логику фильтрации
    console.log('Применение фильтров:', e.target.value);
});

// Обработка откликов на вакансии
document.querySelectorAll('.job-card .button').forEach(button => {
    button.addEventListener('click', () => {
        alert('Спасибо за отклик! Мы свяжемся с вами в ближайшее время.');
    });
});