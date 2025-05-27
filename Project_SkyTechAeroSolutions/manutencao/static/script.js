// Aguar o carregamento completo da pagina antes de rodar o js
document.addEventListener('DOMContentLoaded', function () {
    // Seleciona o formulario
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tableManutencao tbody');

    function atualizarTabela() {
        fetch('/listar-manutencao')
        .then(response => response.json())
        .then(manutencoes => {
         // Limpa a tabela
        tabelaBody.innerHTML = '';
        
        manutencoes.forEach(manutencao => {
        const row = tabelaBody.insertRow();
        row.insertCell(0).textContent = manutencao[0];
        row.insertCell(1).textContent = manutencao[1];
        row.insertCell(2).textContent = manutencao[2];
        row.insertCell(3).textContent = manutencao[3];
        row.insertCell(4).textContent = manutencao[4];
        row.insertCell(5).textContent = manutencao[5];
        row.insertCell(6).textContent = manutencao[6];
         });
        })
        .catch(error => console.error('Erro ao carregar manutenções:', error));
    }
        
    atualizarTabela();

    // Adiciona um listen para o evento submit
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Impede o recarregamento da pagina

        // Obtem dados do formulario
        const formData = new FormData(form);

        // Envia os dados para o endpoint /cadastrar
        fetch('/cadastrar-manutencao', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Exibe a mensagem de erro ou sucesso
            if (data.message === "Cadastro realizado com sucesso!"){
                form.reset(); // Limpas os campos do formulario
                atualizarTabela();
            }
            })
            .catch(error => {
                console.error('Erro:', error);
        });
    });
}) ;