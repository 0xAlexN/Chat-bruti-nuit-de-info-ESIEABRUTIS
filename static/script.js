$(document).ready(function () {
    function appendMessage(sender, text) {
        let avatar = sender === 'user' ? '🤨' : '🤪';
        let className = sender;

        let html = `
            <div class="message ${className}">
                <div class="avatar">${avatar}</div>
                <div class="text">${text}</div>
            </div>
        `;

        $('#chat-box').append(html);
        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
    }

    function sendMessage() {
        let message = $('#user-input').val().trim();
        if (message === '') return;

        appendMessage('user', message);
        $('#user-input').val('');

        // Petit délai pour simuler la "réflexion" (ou la sieste)
        setTimeout(function () {
            $.ajax({
                url: '/chat',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: message }),
                success: function (response) {
                    appendMessage('bot', response.response);
                },
                error: function () {
                    appendMessage('bot', "Oups, mon cerveau a glissé. (Erreur serveur)");
                }
            });
        }, 500 + Math.random() * 1000);
    }

    $('#send-btn').click(sendMessage);

    $('#user-input').keypress(function (e) {
        if (e.which == 13) {
            sendMessage();
        }
    });
});
