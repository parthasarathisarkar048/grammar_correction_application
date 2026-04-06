function correctText() {
    let text = document.getElementById("text").value;
    document.getElementById("result").innerText = "Correcting...";

    fetch('/correct', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'text=' + encodeURIComponent(text)
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("result").innerText = data;
    });
}