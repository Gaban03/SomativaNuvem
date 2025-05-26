document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.querySelector('#tablePacients tbody');
    const selectPlano = document.getElementById('id_plano_saude');

    // Buscar planos e popular select
    function carregarPlanos() {
        fetch('http://localhost:5005/planos')
            .then(response => response.json())
            .then(planos => {
                planos.forEach(plano => {
                    const option = document.createElement('option');
                    option.value = plano.id;
                    option.textContent = plano.nome;
                    selectPlano.appendChild(option);
                });
            })
            .catch(error => console.error('Erro ao carregar planos:', error));
    }

    function atualizarTabela() {
        fetch('/listar')
            .then(response => response.json())
            .then(pacientes => {
                tabelaBody.innerHTML = '';

                pacientes.forEach(paciente => {
                    const row = tabelaBody.insertRow();
                    row.insertCell(0).textContent = paciente[0];
                    row.insertCell(1).textContent = paciente[1];
                    row.insertCell(2).textContent = paciente[2];
                });
            })
            .catch(error => console.error('Erro ao carregar pacientes:', error));
    }

    carregarPlanos();
    atualizarTabela();

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/cadastrar', {
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
