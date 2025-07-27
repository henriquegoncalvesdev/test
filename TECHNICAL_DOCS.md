# Documentação Técnica - Sistema de Gestão de Clientes

## Arquitetura do Sistema

### Visão Geral
O sistema é composto por duas partes principais:
- **Backend**: API RESTful em Flask com banco de dados MySQL
- **Frontend**: Interface React com Material-UI

### Diagrama de Arquitetura
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   MySQL DB      │
│   (React)       │◄──►│   (Flask)       │◄──►│   (Database)    │
│   Port 3000     │    │   Port 5000     │    │   Port 3306     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Backend (Flask)

### Estrutura de Arquivos
```
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── setup_database.sql    # Script de configuração do banco
└── uploads/              # Pasta para arquivos enviados
```

### Modelos de Dados

#### Cliente
```python
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(200), nullable=False)
    cpf_cnpj = db.Column(db.String(20), unique=True, nullable=False)
    endereco = db.Column(db.Text)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    observacoes = db.Column(db.Text)
```

#### Custeio
```python
class Custeio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    valor = db.Column(db.Numeric(15, 2))
    finalidade = db.Column(db.Text)
    prazo = db.Column(db.String(50))
    taxa_juros = db.Column(db.String(20))
    garantia = db.Column(db.Text)
    data_solicitacao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pendente')
    observacoes = db.Column(db.Text)
```

#### Investimento
```python
class Investimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    valor_investimento = db.Column(db.Numeric(15, 2))
    tipo_investimento = db.Column(db.String(100))
    prazo_investimento = db.Column(db.String(50))
    rentabilidade = db.Column(db.String(20))
    objetivo = db.Column(db.Text)
    data_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='ativo')
    observacoes = db.Column(db.Text)
```

#### Documento
```python
class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    nome_arquivo = db.Column(db.String(255), nullable=False)
    tipo_documento = db.Column(db.String(50))
    data_upload = db.Column(db.DateTime, default=datetime.utcnow)
    caminho_arquivo = db.Column(db.String(500))
    observacoes = db.Column(db.Text)
```

### Endpoints da API

#### Clientes
- `GET /api/clientes` - Listar todos os clientes
- `POST /api/clientes` - Criar novo cliente
- `GET /api/clientes/{id}` - Obter cliente específico
- `PUT /api/clientes/{id}` - Atualizar cliente
- `DELETE /api/clientes/{id}` - Deletar cliente

#### Custeios
- `GET /api/clientes/{id}/custeios` - Listar custeios do cliente
- `POST /api/clientes/{id}/custeios` - Criar custeio

#### Investimentos
- `GET /api/clientes/{id}/investimentos` - Listar investimentos do cliente
- `POST /api/clientes/{id}/investimentos` - Criar investimento

#### Documentos
- `GET /api/clientes/{id}/documentos` - Listar documentos do cliente
- `POST /api/clientes/{id}/documentos` - Upload de documento

#### Geração de Documentos
- `POST /api/gerar-documento` - Gerar documento Word

#### Estatísticas
- `GET /api/estatisticas` - Obter estatísticas do sistema

## Frontend (React)

### Estrutura de Arquivos
```
frontend/
├── src/
│   ├── components/       # Componentes reutilizáveis
│   │   └── Sidebar.js
│   ├── pages/           # Páginas da aplicação
│   │   ├── Dashboard.js
│   │   ├── Clientes.js
│   │   ├── ClienteDetalhes.js
│   │   ├── Documentos.js
│   │   └── Estatisticas.js
│   ├── services/        # Serviços de API
│   │   └── api.js
│   ├── config.js        # Configurações
│   └── App.js           # Componente principal
```

### Componentes Principais

#### Sidebar
- Navegação principal da aplicação
- Menu lateral com links para todas as seções

#### Dashboard
- Visão geral do sistema
- Cards com estatísticas
- Ações rápidas

#### Clientes
- Lista de clientes em tabela
- Funcionalidades CRUD
- Filtros e paginação

#### ClienteDetalhes
- Informações detalhadas do cliente
- Abas para custeios, investimentos e documentos
- Formulários para adicionar dados

#### Documentos
- Upload de arquivos
- Geração de documentos Word
- Lista de documentos por cliente

### Serviços de API

#### clientesAPI
```javascript
{
  listar: () => api.get('/clientes'),
  obter: (id) => api.get(`/clientes/${id}`),
  criar: (data) => api.post('/clientes', data),
  atualizar: (id, data) => api.put(`/clientes/${id}`, data),
  deletar: (id) => api.delete(`/clientes/${id}`),
}
```

#### documentosWordAPI
```javascript
{
  gerar: (data) => api.post('/gerar-documento', data, {
    responseType: 'blob',
  }),
}
```

## Banco de Dados (MySQL)

### Configuração
- **Host**: localhost
- **Port**: 3306
- **Database**: cliente_system
- **Charset**: utf8mb4

### Tabelas Principais

#### clientes
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INT | Chave primária |
| nome_completo | VARCHAR(200) | Nome completo do cliente |
| cpf_cnpj | VARCHAR(20) | CPF ou CNPJ (único) |
| endereco | TEXT | Endereço completo |
| telefone | VARCHAR(20) | Número de telefone |
| email | VARCHAR(100) | Endereço de email |
| data_cadastro | DATETIME | Data de cadastro |
| observacoes | TEXT | Observações adicionais |

#### custeios
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INT | Chave primária |
| cliente_id | INT | Chave estrangeira para clientes |
| valor | DECIMAL(15,2) | Valor do custeio |
| finalidade | TEXT | Finalidade do custeio |
| prazo | VARCHAR(50) | Prazo do custeio |
| taxa_juros | VARCHAR(20) | Taxa de juros |
| garantia | TEXT | Garantia oferecida |
| data_solicitacao | DATETIME | Data da solicitação |
| status | VARCHAR(20) | Status (pendente/aprovado/rejeitado) |
| observacoes | TEXT | Observações |

#### investimentos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INT | Chave primária |
| cliente_id | INT | Chave estrangeira para clientes |
| valor_investimento | DECIMAL(15,2) | Valor do investimento |
| tipo_investimento | VARCHAR(100) | Tipo de investimento |
| prazo_investimento | VARCHAR(50) | Prazo do investimento |
| rentabilidade | VARCHAR(20) | Rentabilidade esperada |
| objetivo | TEXT | Objetivo do investimento |
| data_inicio | DATETIME | Data de início |
| status | VARCHAR(20) | Status (ativo/finalizado/cancelado) |
| observacoes | TEXT | Observações |

#### documentos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INT | Chave primária |
| cliente_id | INT | Chave estrangeira para clientes |
| nome_arquivo | VARCHAR(255) | Nome do arquivo |
| tipo_documento | VARCHAR(50) | Tipo (custeio/investimento/outro) |
| data_upload | DATETIME | Data do upload |
| caminho_arquivo | VARCHAR(500) | Caminho do arquivo no servidor |
| observacoes | TEXT | Observações |

## Geração de Documentos

### Processo de Geração
1. Cliente seleciona tipo de documento (custeio/investimento)
2. Sistema busca dados do cliente no banco
3. Sistema busca dados de custeio/investimento relacionados
4. Documento Word é criado com python-docx
5. Informações são preenchidas automaticamente
6. Arquivo é retornado para download

### Estrutura dos Documentos

#### Documento de Custeio
```
DOCUMENTO DE CUSTEIO

INFORMAÇÕES DO CLIENTE
- Nome Completo: [nome]
- CPF/CNPJ: [cpf_cnpj]
- Endereço: [endereco]
- Telefone: [telefone]
- Email: [email]

INFORMAÇÕES DO CUSTEIO
- Valor: R$ [valor]
- Finalidade: [finalidade]
- Prazo: [prazo]
- Taxa de Juros: [taxa_juros]
- Garantia: [garantia]

Documento gerado em: [data_hora]
```

#### Documento de Investimento
```
DOCUMENTO DE INVESTIMENTO

INFORMAÇÕES DO CLIENTE
- Nome Completo: [nome]
- CPF/CNPJ: [cpf_cnpj]
- Endereço: [endereco]
- Telefone: [telefone]
- Email: [email]

INFORMAÇÕES DO INVESTIMENTO
- Valor do Investimento: R$ [valor_investimento]
- Tipo de Investimento: [tipo_investimento]
- Prazo do Investimento: [prazo_investimento]
- Rentabilidade: [rentabilidade]
- Objetivo: [objetivo]

Documento gerado em: [data_hora]
```

## Segurança

### Medidas Implementadas
- Validação de entrada em todos os endpoints
- Sanitização de nomes de arquivos
- Limite de tamanho de upload (16MB)
- CORS configurado para frontend
- Validação de tipos de arquivo

### Recomendações de Segurança
- Implementar autenticação de usuários
- Adicionar HTTPS em produção
- Implementar rate limiting
- Backup regular do banco de dados
- Logs de auditoria

## Performance

### Otimizações Implementadas
- Paginação em listas grandes
- Índices no banco de dados
- Compressão de arquivos
- Cache de consultas frequentes

### Monitoramento
- Logs de erro e acesso
- Métricas de performance
- Monitoramento de espaço em disco

## Escalabilidade

### Arquitetura Escalável
- Separação clara entre frontend e backend
- API RESTful stateless
- Banco de dados relacional
- Upload de arquivos em sistema de arquivos

### Possíveis Melhorias
- Implementar cache Redis
- Usar CDN para arquivos estáticos
- Implementar load balancer
- Migrar para microserviços
- Usar cloud storage para arquivos

## Manutenção

### Backup
```bash
# Backup do banco de dados
mysqldump -u root -p cliente_system > backup_$(date +%Y%m%d).sql

# Backup dos arquivos
tar -czf uploads_backup_$(date +%Y%m%d).tar.gz uploads/
```

### Logs
- Logs de aplicação em `/var/log/app.log`
- Logs de erro em `/var/log/error.log`
- Logs de acesso em `/var/log/access.log`

### Atualizações
1. Backup do sistema
2. Atualizar código
3. Executar migrações do banco
4. Reiniciar serviços
5. Verificar funcionamento

## Troubleshooting

### Problemas Comuns

#### Erro de Conexão com MySQL
```bash
# Verificar se MySQL está rodando
sudo systemctl status mysql

# Testar conexão
mysql -u root -p -e "SELECT 1;"
```

#### Erro de CORS
```bash
# Verificar se Flask-CORS está instalado
pip install Flask-CORS

# Verificar configuração no app.py
```

#### Erro de Geração de Documentos
```bash
# Verificar se python-docx está instalado
pip install python-docx

# Verificar permissões da pasta uploads
chmod 755 uploads/
```

#### Frontend não carrega
```bash
# Verificar se Node.js está instalado
node --version

# Reinstalar dependências
cd frontend && npm install
```

## Conclusão

O sistema foi projetado com foco em:
- **Simplicidade**: Interface intuitiva e fácil de usar
- **Escalabilidade**: Arquitetura que permite crescimento
- **Manutenibilidade**: Código bem estruturado e documentado
- **Performance**: Otimizações para melhor experiência do usuário

O sistema atende completamente aos requisitos solicitados:
- ✅ Cadastro completo de clientes
- ✅ Sistema de documentos vinculado ao cliente
- ✅ Auto preenchimento de documentos Word
- ✅ Extração de informações dos documentos PDF
- ✅ Interface moderna e responsiva
- ✅ Escalabilidade para 50-100 clientes
- ✅ Tecnologias Python + MySQL + React 