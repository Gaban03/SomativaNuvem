document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formFaturamento');
    const tabelaBody = document.querySelector('#tabelaConsultas tbody');
    const resultado = document.getElementById('resultado');
    const mensagem = document.getElementById('mensagem');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        mensagem.textContent = '';
        tabelaBody.innerHTML = '';
        resultado.style.display = 'none';

        const cpf = document.getElementById('cpfInput').value.trim();

        if (!cpf) {
            mensagem.textContent = 'Por favor, informe um CPF válido.';
            return;
        }

        try {
            const response = await fetch('http://localhost:5004/consultas-paciente', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ cpf })
            });

            if (!response.ok) {
                const error = await response.json();
                mensagem.textContent = error.message || 'Erro desconhecido.';
                return;
            }

            const data = await response.json();

            if (data.consultas.length === 0) {
                mensagem.textContent = 'Nenhuma consulta encontrada para esse CPF.';
                return;
            }

            data.consultas.forEach(consulta => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${consulta.id_consulta}</td>
                    <td>${consulta.medico}</td>
                    <td>${consulta.tipo_de_consulta}</td>
                    <td>R$ ${consulta.preco.toFixed(2)}</td>
                    <td>${new Date(consulta.data_consulta).toLocaleString('pt-BR')}</td>
                `;
                tabelaBody.appendChild(tr);
            });

            resultado.style.display = 'block';

        } catch (error) {
            mensagem.textContent = 'Erro ao buscar consultas: ' + error.message;
        }
    });
});
