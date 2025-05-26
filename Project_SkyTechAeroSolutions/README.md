Sistema Vida+ Saúde - Arquitetura de Microserviços
Descrição
Este projeto visa transformar o sistema monolítico da rede de clínicas Vida+ Saúde em uma arquitetura de microserviços. O objetivo é melhorar a escalabilidade e manutenibilidade, com a implementação de serviços independentes para Paciente, Consulta, Prontuário e Faturamento. Cada serviço é desenvolvido com Python e Flask, containerizado com Docker e orquestrado com Docker Compose.

Objetivos
Compreender e implementar uma arquitetura de microserviços.

Desenvolver APIs RESTful com Flask.

Containerizar os serviços com Docker.

Integrar horizontalmente os microserviços via chamadas HTTP.

Simular integração vertical com um sistema de plano de saúde.

Tecnologias
Python e Flask para o desenvolvimento dos microserviços.

Docker e Docker Compose para containerização e orquestração.

Requests para comunicação HTTP entre serviços.

JSON para troca de dados.

Estrutura do Projeto
paciente-service: Cadastro e busca de pacientes.

consulta-service: Agendamento e listagem de consultas.

prontuario-service: Armazenamento e acesso a prontuários médicos.

faturamento-service: Cálculo de valores e geração de faturas.

sistema-plano-saude: Sistema mockado de plano de saúde para validação de cobertura.

Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/vida-mais-saude.git
cd vida-mais-saude
Inicie os containers:

bash
Copiar
Editar
docker-compose up --build
Acesse os microserviços nas seguintes portas:

Paciente: http://localhost:5001

Consulta: http://localhost:5002

Prontuário: http://localhost:5003

Faturamento: http://localhost:5004

Plano de Saúde (mock): http://localhost:5005