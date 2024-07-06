# Store API: Uma API RESTful de Produtos Construída com FastAPI e TDD
✨ Uma API robusta, escalável e bem-testada para gerenciamento de produtos ✨

## Visão Geral
A Store API é uma API RESTful projetada para facilitar o gerenciamento de produtos em seu e-commerce ou sistema de estoque.<br>
Desenvolvida com o poderoso framework FastAPI, ela oferece alta performance, documentação automática com Swagger UI e, principalmente, confiabilidade através de Test Driven Development (TDD).

## Principais Características

CRUD Completo: Crie, leia, atualize e exclua produtos com facilidade.<br>
Validação de Dados: Garanta a integridade dos seus dados com a validação automática fornecida pelo Pydantic.<br>
Documentação Interativa: Explore e teste os endpoints da API diretamente no seu navegador com o Swagger UI.<br>
Alta Performance: FastAPI e Uvicorn garantem que sua API seja rápida e responsiva.<br>
Testes Abrangentes: Mais de 90% de cobertura de testes garante a qualidade e a estabilidade da API.<br>
Fácil Implantação: Utilize Docker para implantar sua API rapidamente em qualquer ambiente.<br>

## Endpoints Principais

<table>
    <thead>
        <tr>
            <th>Método</th>
            <th>Endpoint</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>POST</td>
            <td>/products/</td>
            <td>Cria um novo produto</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/products/{id}</td>
            <td>Obtém os detalhes de um produto</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/products/</td>
            <td>Lista todos os produtos</td>
        </tr>
        <tr>
            <td>PATCH</td>
            <td>/products/{id}</td>
            <td>Atualiza um produto existente</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/products/{id}</td>
            <td>Exclui um produto</td>
        </tr>
    </tbody>
</table>

## Tecnologias Utilizadas

FastAPI: Framework web de alta performance.
Pydantic: Validação de dados e modelagem de objetos.
Motor: Driver assíncrono para MongoDB.
Pytest: Framework de testes.
Docker: Conteinerização para fácil implantação.
Como Executar

## Clone o Repositório:<br>
Bash<br>
git clone https://github.com/seu-usuario/store-api.git

## Instale as Dependências:<br>
Bash<br>
poetry install

## Inicie o MongoDB:<br>
Bash<br>
docker-compose up -d db 

## Execute a API:<br>
Bash<br>
make run

## Documentação da API
Após executar a API, acesse a documentação interativa do Swagger UI em:<br> http://localhost:8000/docs.

## Testes
Execute os testes com o seguinte comando:<br>
Bash<br>
make test

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests!

## Licença

MIT License

## Contato

Lucasgyn94 - needslucas944@gmail.com
