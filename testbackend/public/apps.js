const button = document.getElementById('send-message-button'); // Obtendo o elemento do botão "send-message-button"

button.addEventListener('click', function() { // Adicionando um evento de clique no botão

const input = document.getElementById('message-input'); // Obtendo o valor da caixa de entrada de mensagem com o ID "message-input"
const message = input.value;

// Fazendo uma requisição HTTP do tipo POST para o endpoint "/send-message"
// Enviando a mensagem em formato JSON junto com o cabeçalho "Content-Type: application/json"
fetch('http://localhost:3000/send-message', {
method: 'POST',
body: JSON.stringify({ message }),
headers: { 'Content-Type': 'application/json' }
})
.then(response => {
if (response.ok) {
console.log("Success: Mensagem enviada com sucesso");
} else {
console.log("Error:", response.status);
}
})
.catch(error => {
console.error('Error:', error);
});
});