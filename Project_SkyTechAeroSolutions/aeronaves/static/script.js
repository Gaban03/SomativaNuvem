document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const tabelaBody = document.getElementById('tabelaAeronaves');

    function atualizarTabela() {
        fetch('/listar_aeronaves')
            .then(response => response.json())
            .then(aeronaves => {
                tabelaBody.innerHTML = '';

                aeronaves.forEach(aeronave => {
                    const row = tabelaBody.insertRow();
                    row.insertCell(0).textContent = aeronave[0]; // ID (auto_increment)
                    row.insertCell(1).textContent = aeronave[1]; // Modelo
                    row.insertCell(2).textContent = aeronave[2]; // Fabricante
                    row.insertCell(3).textContent = aeronave[3]; // Horas de voo
                });
            })
            .catch(error => console.error('Erro ao carregar aeronaves:', error));
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const modelo = document.getElementById('modelo').value;
        const fabricante = document.getElementById('fabricante').value;
        const horas_voo = document.getElementById('horas_voo').value;

        fetch('/cadastrar_aeronave', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ modelo, fabricante, horas_voo })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            if (data.message === "Cadastro realizado com sucesso") {
                form.reset();
                atualizarTabela();
            }
        })
        .catch(error => console.error('Erro ao cadastrar:', error));
    });

    atualizarTabela(); // carrega os dados ao iniciar
});
