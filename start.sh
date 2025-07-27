#!/bin/bash

# Script de inicialização do Sistema de Gestão de Clientes
echo "🚀 Iniciando Sistema de Gestão de Clientes..."

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências Python
echo "📥 Instalando dependências Python..."
pip install -r requirements.txt

# Verificar se o MySQL está rodando
echo "🗄️ Verificando conexão com MySQL..."
if ! mysql -u root -e "SELECT 1;" > /dev/null 2>&1; then
    echo "❌ Erro: MySQL não está rodando ou as credenciais estão incorretas"
    echo "💡 Certifique-se de que o MySQL está instalado e rodando"
    echo "💡 Execute: brew services start mysql"
    exit 1
fi

# Criar pasta uploads se não existir
mkdir -p uploads

# Iniciar backend em background
echo "🔧 Iniciando backend Flask..."
python app.py &
BACKEND_PID=$!

# Aguardar backend inicializar
sleep 3

# Verificar se o backend está rodando
if ! curl -s http://localhost:5001/api/estatisticas > /dev/null; then
    echo "❌ Erro: Backend não iniciou corretamente"
    exit 1
fi

echo "✅ Backend iniciado com sucesso em http://localhost:5001"

# Verificar se o frontend existe
if [ ! -d "frontend" ]; then
    echo "❌ Erro: Pasta frontend não encontrada"
    echo "💡 Execute: npx create-react-app frontend"
    exit 1
fi

# Instalar dependências do frontend
echo "📥 Instalando dependências do frontend..."
cd frontend
npm install

# Iniciar frontend
echo "🔧 Iniciando frontend React..."
npm start &
FRONTEND_PID=$!

cd ..

echo ""
echo "🎉 Sistema iniciado com sucesso!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend: http://localhost:5001"
echo ""
echo "📖 Para parar o sistema, pressione Ctrl+C"
echo ""

# Função para limpar processos ao sair
cleanup() {
    echo ""
    echo "🛑 Parando sistema..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Capturar Ctrl+C
trap cleanup SIGINT

# Manter script rodando
wait 