const ctx = document.getElementById('salesChart').getContext('2d');
const salesChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labelsData,   // variáveis globais vindas do template
        datasets: [{
            label: 'Receita por produto',
            data: valuesData,
            backgroundColor: ['#007bff', '#28a745', '#ffc107', '#dc3545']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'top' },
            title: { display: true, text: 'Receita total por produto' }
        }
    }
});
