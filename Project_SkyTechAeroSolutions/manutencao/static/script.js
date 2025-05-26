// Aguar o carregamento completo da pagina antes de rodar o js
document.addEventListener('DOMContentLoaded', function () {
    // Seleciona o formulario
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tableConsults tbody');

    function atualizarTabela() {
        fetch('/listar')
        .then(response => response.json())
        .then(consultas => {
         // Limpa a tabela
        tabelaBody.innerHTML = '';
        
        consultas.forEach(consulta => {
        const row = tabelaBody.insertRow();
        row.insertCell(0).textContent = consulta[0];
        row.insertCell(1).textContent = consulta[1];
        row.insertCell(2).textContent = consulta[2];
        row.insertCell(3).textContent = consulta[3];
        row.insertCell(4).textContent = consulta[4];
        row.insertCell(5).textContent = consulta[5];
         });
        })
        .catch(error => console.error('Erro ao carregar consultas:', error));
    }
        
    atualizarTabela();

    // Adiciona um listen para o evento submit
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Impede o recarregamento da pagina

        // Obtem dados do formulario
        const formData = new FormData(form);

        // Envia os dados para o endpoint /cadastrar
        fetch('/cadastrar', {
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