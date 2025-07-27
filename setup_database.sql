-- Script para configurar o banco de dados MySQL
-- Execute este script no MySQL para criar o banco de dados

-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS cliente_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usar o banco de dados
USE cliente_system;

-- Criar usuário (opcional - ajuste conforme necessário)
-- CREATE USER 'cliente_user'@'localhost' IDENTIFIED BY 'sua_senha_aqui';
-- GRANT ALL PRIVILEGES ON cliente_system.* TO 'cliente_user'@'localhost';
-- FLUSH PRIVILEGES;

-- As tabelas serão criadas automaticamente pelo Flask-SQLAlchemy
-- quando você executar o aplicativo pela primeira vez

-- Verificar se o banco foi criado
SELECT 'Banco de dados cliente_system criado com sucesso!' AS Status; 