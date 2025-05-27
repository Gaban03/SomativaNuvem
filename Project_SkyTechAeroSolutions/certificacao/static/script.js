// Aguar o carregamento completo da pagina antes de rodar o js
document.addEventListener('DOMContentLoaded', function () {
    // Seleciona o formulario
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tableCertificacoes tbody');

    function atualizarTabela() {
        fetch('/listar_certificacoes')
        .then(response => response.json())
        .then(certificacoes => {
         // Limpa a tabela
        tabelaBody.innerHTML = '';
        
        certificacoes.forEach(certificacoes => {
        const row = tabelaBody.insertRow();
        row.insertCell(0).textContent = certificacoes[0]; // insere no campo de ID certificação
        row.insertCell(1).textContent = certificacoes[1];// insere no campo de ID mecanico
        row.insertCell(2).textContent = certificacoes[2]== 1 ? 'Sim' : 'Não'; // insere no campo de apto 
         });
        })
        .catch(error => console.error('Erro ao carregar certificações:', error));
    }
        
    atualizarTabela();

    // Adiciona um listen para o evento submit
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Impede o recarregamento da pagina

        // Obtem dados do formulario
        const formData = new FormData(form);

        // Envia os dados para o endpoint /cadastrar
        fetch('/cadastrar_certificacoes', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Exibe a mensagem de erro ou sucesso
            form.reset(); // Limpas os campos do formulario
            atualizarTabela(); // atualiza a tabela para exibir os dados que acabaram de ser inseridos
            })
            .catch(error => {
                console.error('Erro:', error);
        });
    });
}) ;