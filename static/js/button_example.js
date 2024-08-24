function sumNumbers() {
    // Read values from textboxes
    var num1 = document.getElementById("number1").value;
    var num2 = document.getElementById("number2").value;

    // Send values to server
    fetch(`/sum/${num1}/${num2}`)
        .then(response => response.text())
        .then(result => {
            // Display the result in the div
            document.getElementById("result").textContent = result;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
//Allow access from the page
window.sumNumbers = sumNumbers;