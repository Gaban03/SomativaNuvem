document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tableMecanicos tbody');

    function atualizarTabela() {
        fetch('/listar_mecanico')
            .then(response => response.json())
            .then(mecanico => {
                tabelaBody.innerHTML = '';

                mecanico.forEach(mecanico => {
                    const row = tabelaBody.insertRow();
                    row.insertCell(0).textContent = mecanico[0];
                    row.insertCell(1).textContent = mecanico[1];
                    row.insertCell(2).textContent = mecanico[2];
                });
            })
            .catch(error => console.error('Erro ao carregar mecanicos:', error));
    }

    atualizarTabela();

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
                if (data.message === "Cadastro realizado com sucesso!") {
                    form.reset();
                }
                atualizarTabela();
            })
            .catch(error => console.error('Erro:', error));
    });
});
