const exibirButton = document.getElementById('send-message-button');
exibirButton.addEventListener('click', function() {
// Fazendo uma requisição HTTP do tipo GET para o endpoint "/get-messages"
// Recuperando as mensagens do banco de dados
fetch('http://localhost:3000/get-messages')
.then(response => response.json())
.then(data => {
  // Aqui você pode manipular os dados recuperados e exibi-los na página
  const messagesContainer = document.getElementById('messages');
  // Recuperando a última mensagem
  const lastMessage = data[data.length - 1];
  const messageElement = document.createElement('p');
  
  
  messageElement.innerText = lastMessage.content;
  messagesContainer.appendChild(messageElement);
 
  
     
})



.then(response => {
if (response.ok) {
console.log("Success: Mensagem chegando com sucesso");
}

else {
  console.log("Error:", response.status);
  }
  })
  
  .catch(error => {
  console.error(error);
  });
  });
  
  function adicionarTexto() {
  const textoAdicional = document.getElementById('texto-adicional');
  textoAdicional.innerHTML = 'Texto adicional aqui';
  }