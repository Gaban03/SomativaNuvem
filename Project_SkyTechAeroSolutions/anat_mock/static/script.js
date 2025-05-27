// Aguar o carregamento completo da pagina antes de rodar o js
document.addEventListener('DOMContentLoaded', function () {
    const tabelaBody = document.querySelector('#tableMecanicosCertificacoes tbody');

    function atualizarTabela() {
        fetch('/anat_mock')
        .then(response => response.json())
        .then(mecanicos_certificacao => {
         // Limpa a tabela
        tabelaBody.innerHTML = '';
        
        mecanicos_certificacao.forEach(mecanicos_certificacao => {
        const row = tabelaBody.insertRow();
        row.insertCell(0).textContent = mecanicos_certificacao[0]; // insere no campo de ID mecanico
        row.insertCell(1).textContent = mecanicos_certificacao[1]; // insere no campo nome do mecanico
        row.insertCell(2).textContent = mecanicos_certificacao[2]; // insere no campo cpf do mecanico
        row.insertCell(3).textContent = mecanicos_certificacao[3] === 1 ? 'Sim' : (mecanicos_certificacao[3] === 0 ? 'Não' : 'Sem certificação'); // insere no campo apto
         });
        })
        .catch(error => console.error('Erro ao carregar certificações:', error));
    }
        
    atualizarTabela();
}) ;