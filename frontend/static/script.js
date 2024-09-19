document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("chat-message").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const messageInput = document.getElementById("chat-message");
    const message = messageInput.value.trim();

    if (message === "") return;

    // Display user message
    displayMessage(message, 'user');

    // Clear input field
    messageInput.value = "";

    // Simulate bot response
    setTimeout(() => {
        const botReply = "This is a bot reply to: " + message;
        displayMessage(botReply, 'bot');
    }, 500);
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");

    const messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message", sender);

    const messageContent = document.createElement("p");
    messageContent.textContent = message;
    messageDiv.appendChild(messageContent);

    chatBox.appendChild(messageDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
