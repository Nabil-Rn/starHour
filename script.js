document.getElementById('volunteerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const dataString = document.getElementById('volunteerData').value;
    createPieChart(dataString);
});

function createPieChart(dataString) {
    // Parse the input string into an array of objects with labels and values
    // I choose to split with comma for each category and get the hours after the :colon
    const dataArr = dataString.split(',').map(item => {
        const [label, hours] = item.trim().split(':');
        return {
            label: label,
            value: parseFloat(hours),
        };
    });

    // Calculate the total hours and determine the appropriate limit
    const totalHours = dataArr.reduce((sum, d) => sum + d.value, 0);
    const pieLimit = totalHours <= 60 ? 60 : 120;

    const hoursNeeded = pieLimit - totalHours;

    //const colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange'];
    const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'];// better colors

    const pieData = {
        labels: dataArr.map(d => `${d.label} ${d.value} hours`), // Display both label and hours
        datasets: [{
            data: dataArr.map(d => d.value),
            backgroundColor: colors.slice(0, dataArr.length),
        }]
    };

    // If the total hours are less than 60 or 120, add a slice for "hours left to do"
    if (totalHours < pieLimit) {
        const description = "Hours left to do";
        pieData.labels.push(`${hoursNeeded} ${description}`);
        pieData.datasets[0].data.push(hoursNeeded);
        pieData.datasets[0].backgroundColor.push('#FFFFFF');
    }

    const ctx = document.getElementById('volunteerPieChart').getContext('2d');

    if (window.myPieChart) {
        window.myPieChart.destroy();
    }

    window.myPieChart = new Chart(ctx, {
        type: 'pie',
        data: pieData,
        options: {
            responsive: true,
            title: {
                display: true,
                text: `Volunteer Hours (out of ${pieLimit} hours)`
            }
        },
    });

    // Update the summary text
    let summaryText = `Total hours volunteered: ${totalHours}. You need ${hoursNeeded} more hours to reach ${pieLimit} hours.`;

    if (totalHours >= 120) {
        summaryText += '\n\nCongratulations! You have earned two stars for your volunteer work!';
    } else if (totalHours >= 60) {
        summaryText += '\n\nYou have earned one star for your volunteer work!!! Keep going for two stars!';
    } else {
        summaryText += '\n\nYou need more hours to earn your first star. Keep volunteering!';
    }

    document.getElementById('volunteerSummary').innerText = summaryText;
}
