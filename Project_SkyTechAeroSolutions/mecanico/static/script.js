document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tableMecanicos tbody');

    // funcao para atualziar a tabela visual do frontend
    function atualizarTabela() {
        fetch('/listar_mecanico')
            .then(response => response.json())
            .then(mecanico => {
                tabelaBody.innerHTML = '';

                mecanico.forEach(mecanico => {
                    const row = tabelaBody.insertRow();
                    row.insertCell(0).textContent = mecanico[0]; // insere no campo do ID mecanico
                    row.insertCell(1).textContent = mecanico[1]; // insere no campo de nome do mecanico
                    row.insertCell(2).textContent = mecanico[2]; // insere no campo de cpf do mecanico
                });
            })
            .catch(error => console.error('Erro ao carregar mecanicos:', error));
    }

    atualizarTabela();

    // função que escuta o click do botao cadastrar para enviar para o banco
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/cadastrar_mecanico', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                form.reset(); // limpa o formulario
                atualizarTabela(); // atualiza a tabela para exibir os dados que acabaram de ser inseridos
            })
            .catch(error => console.error('Erro:', error));
    });
});
