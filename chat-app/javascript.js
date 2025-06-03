function userInput () {
    var message = document.getElementById('message').value;
    var result = document.getElementById('result');
    result.textContent = message;
}
  
sendButton.addEventListener('click', userInput, false);