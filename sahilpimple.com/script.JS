function analyzeLog() {
    const logFileInput = document.getElementById('logFile');
    const formData = new FormData();
    formData.append('logFile', logFileInput.files[0]);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => displayResults(data))
    .catch(error => console.error('Error:', error));
}

function displayResults(data) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '<h2>Error Analysis:</h2>';
    
    for (const error in data) {
        const count = data[error];
        resultsContainer.innerHTML += `<p>${error}: ${count} occurrences</p>`;
    }
}
