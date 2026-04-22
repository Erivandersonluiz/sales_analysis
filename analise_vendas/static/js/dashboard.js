const productCtx = document.getElementById('salesChart').getContext('2d');
const monthlyCtx = document.getElementById('monthlyChart').getContext('2d');

new Chart(productCtx, {
    type: 'bar',
    data: {
        labels: labelsProdutoData,
        datasets: [{
            label: 'Receita por produto',
            data: valuesProdutoData,
            backgroundColor: ['#7c3aed', '#22c55e', '#f59e0b', '#ef4444'],
            borderRadius: 12,
            borderSkipped: false,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Receita por produto' }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: { color: 'rgba(148, 163, 184, 0.2)' },
            },
            x: {
                grid: { display: false }
            }
        }
    }
});

new Chart(monthlyCtx, {
    type: 'line',
    data: {
        labels: labelsMensaisData,
        datasets: [{
            label: 'Receita mensal',
            data: valuesMensaisData,
            fill: true,
            backgroundColor: 'rgba(124, 58, 237, 0.16)',
            borderColor: '#c084fc',
            tension: 0.35,
            pointBackgroundColor: '#c084fc',
            pointBorderColor: '#fff',
            pointRadius: 5,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Vendas por mês' }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: { color: 'rgba(148, 163, 184, 0.2)' }
            },
            x: {
                grid: { display: false }
            }
        }
    }
});
