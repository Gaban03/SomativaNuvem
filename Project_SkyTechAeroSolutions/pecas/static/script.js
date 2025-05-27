document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tabelaPecas tbody');

    function atualizarTabela() {
        fetch('/listar-pecas')
            .then(response => response.json())
            .then(pecas => {
                tabelaBody.innerHTML = '';

                pecas.forEach(peca => {
                    const row = tabelaBody.insertRow();
                    row.insertCell(0).textContent = peca[0];
                    row.insertCell(1).textContent = peca[1];
                    row.insertCell(2).textContent = peca[2];
                    row.insertCell(3).textContent = peca[3];
                });
            })
            .catch(error => console.error('Erro ao carregar peças:', error));
    }

    atualizarTabela();

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/cadastrar-peca', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                if (data.message === "Cadastro realizado com sucesso!") {
                    form.reset();
                    atualizarTabela();
                }
            })
            .catch(error => console.error('Erro:', error));
    });
});
