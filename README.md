# Sistema de Gestão de Clientes

Sistema web completo para gestão de clientes com geração automática de documentos Word (custeio e investimento).

## 🚀 Funcionalidades

- **Gestão Completa de Clientes**: Cadastro, edição e visualização detalhada
- **Sistema de Custeios**: Controle de solicitações com valores, prazos e taxas
- **Gestão de Investimentos**: Acompanhamento com tipos, prazos e rentabilidade
- **Geração Automática de Documentos**: Criação de documentos Word baseados nos dados cadastrados
- **Upload e Organização de Documentos**: Sistema para anexar documentos por cliente
- **Interface Moderna e Responsiva**: Design Material-UI para qualquer dispositivo

## 🛠️ Tecnologias Utilizadas

### Backend
- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **MySQL**: Banco de dados
- **python-docx**: Geração de documentos Word
- **PyPDF2**: Análise de documentos PDF

### Frontend
- **React**: Biblioteca JavaScript para interface
- **Material-UI**: Componentes de interface moderna
- **Axios**: Cliente HTTP para API
- **React Router**: Navegação entre páginas

## 📋 Pré-requisitos

- Python 3.8+
- Node.js 14+
- MySQL 8.0+
- npm ou yarn

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd sistema-clientes
```

### 2. Configure o banco de dados MySQL

Execute o script SQL para criar o banco de dados:
```bash
mysql -u root -p < setup_database.sql
```

### 3. Configure o ambiente Python

```bash
# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:
```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=mysql://root:sua_senha@localhost/cliente_system
SECRET_KEY=sua_chave_secreta_aqui
```

### 5. Configure o Frontend

```bash
cd frontend

# Instale as dependências
npm install

# Configure a URL da API (se necessário)
# Edite src/services/api.js e ajuste a API_BASE_URL
```

## 🚀 Executando o Sistema

### 1. Inicie o Backend

```bash
# Na raiz do projeto (com venv ativado)
python app.py
```

O backend estará disponível em: `http://localhost:5001`

### 2. Inicie o Frontend

```bash
cd frontend
npm start
```

O frontend estará disponível em: `http://localhost:3000`

## 📖 Como Usar

### 1. Cadastro de Clientes
- Acesse a seção "Clientes"
- Clique em "Novo Cliente"
- Preencha as informações necessárias
- Salve o cliente

### 2. Gestão de Custeios
- Acesse os detalhes de um cliente
- Vá para a aba "Custeios"
- Clique em "Novo Custeio"
- Preencha as informações do custeio

### 3. Gestão de Investimentos
- Acesse os detalhes de um cliente
- Vá para a aba "Investimentos"
- Clique em "Novo Investimento"
- Preencha as informações do investimento

### 4. Geração de Documentos
- Acesse a seção "Documentos"
- Selecione um cliente
- Clique em "Gerar Custeio" ou "Gerar Investimento"
- O documento Word será baixado automaticamente

### 5. Upload de Documentos
- Acesse a seção "Documentos"
- Selecione um cliente
- Escolha um arquivo para upload
- Defina o tipo de documento
- Adicione observações (opcional)
- Clique em "Enviar Documento"

## 🗄️ Estrutura do Banco de Dados

### Tabelas Principais

- **clientes**: Informações dos clientes
- **custeios**: Dados de custeio por cliente
- **investimentos**: Dados de investimento por cliente
- **documentos**: Documentos anexados por cliente

### Campos Identificados nos Documentos

#### Documentos de Custeio:
- Nome do cliente
- CPF/CNPJ
- Valor
- Data
- Endereço
- Telefone
- Finalidade
- Taxa de juros
- Garantia

#### Documentos de Investimento:
- Nome do cliente
- Valor do investimento
- Tipo de investimento
- Endereço
- Telefone
- Objetivo

## 🔧 Configurações Avançadas

### Personalizando a Geração de Documentos

Os templates de documentos podem ser personalizados editando a função `gerar_documento` no arquivo `app.py`.

### Adicionando Novos Campos

Para adicionar novos campos aos documentos:

1. Atualize os modelos no backend (`app.py`)
2. Execute as migrações do banco de dados
3. Atualize as interfaces no frontend
4. Modifique a função de geração de documentos

### Configurando o MySQL

Se você precisar usar credenciais diferentes:

1. Edite a string de conexão em `app.py`
2. Atualize o arquivo `.env`
3. Execute as migrações: `flask db upgrade`

## 🐛 Solução de Problemas

### Erro de Conexão com MySQL
- Verifique se o MySQL está rodando
- Confirme as credenciais no arquivo `app.py`
- Teste a conexão: `mysql -u root -p`

### Erro de CORS
- Verifique se o Flask-CORS está instalado
- Confirme se o backend está rodando na porta 5000

### Erro de Geração de Documentos
- Verifique se a biblioteca `python-docx` está instalada
- Confirme se a pasta `uploads` existe

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos canais disponíveis.

---

**Desenvolvido com ❤️ para otimizar a gestão de clientes e documentos** 