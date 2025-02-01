
const ctx = document.getElementById('revenueChart').getContext('2d');
new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Revenue',
            data: [18000, 22000, 19000, 24000, 21000, 24567],
            borderColor: '#2196F3',
            tension: 0.4,
            fill: false
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: 'Monthly Revenue'
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    callback: value => '$' + value.toLocaleString()
                }
            }
        }
    }
});

// Add interactivity
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', e => {
        document.querySelector('.nav-item.active').classList.remove('active');
        item.classList.add('active');
    });
});

// Search functionality
document.querySelector('.search').addEventListener('input', e => {
    console.log('Searching for:', e.target.value);
    // Implement search functionality here
});
