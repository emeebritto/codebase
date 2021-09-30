*não esquecer o uso do ; no final dos comamandos no mysql.

// instalar como dependencia de desenvolvimento:

    npm install --save-dev [nomeDoPackage]

// instalar mysql2:

    npm install mysql2

// intalar sequelize sequelize-cli path:

    npm instal sequelize sequelize-cli path

// criar arquivos iniciais com o sequelize:

    npx sequelize-cli init

// criando models:

    npx sequelize-cli model: create --name Peassoas --attributes nome:string,ativo:boolean,email:string,role:string

// criando migrate:

    npx sequelize-cli db:migrate

// Acessa o MySql:

    sudo mysql -u root -p

        // p = password

// Mostrar databases do mysql:

    show databases;

// Criar database:

    create database [nome_do_projeto];


*No config.json fica as configuração de conexão com a dataBase


// acessa dataBase:
    use [nome_dataBase];

// Mostrar tabelas na dataBase:
    show tables;

// exibir mais detalhes da tabala:
    describe [nome_tabela];

// inserir dados no banco:
    insert into [nomeTabela] (nome, ativo, email, role, createdAt, updatedAt) //campos exemplar, isso pode mudar
    values ("Carla Gomes", 1, "carla@carla.com", "estudante", NOW(), NOW());

// Selecinar todos os dados de um dataBase:
    select * from Pessoas;

// Para criar uma seed:
    npx sequelize-cli seed:generate --name demo-pessoas

// Para conectar com banco e enviar as seeds:

    npx sequelize-cli db:seed:all