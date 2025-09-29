# 📦 Verificador de Etiquetas - Mercado Livre

## 📋 Sobre o Projeto
API para verificação automática de etiquetas de envio do Mercado Livre através de arquivos PDF.

## 🚀 Funcionalidades
- ✅ **Verificação automática** de etiquetas do Mercado Livre
- 📄 **Suporte a arquivos PDF**
- 🔍 **Análise inteligente** de padrões e identificação de erros
- ⚡ **Processamento rápido** e eficiente
- 🌐 **API RESTful** simples e documentada

## 🛠️ Tecnologias Utilizadas
- **Backend**: FastAPI, Python 3.8+
- **Processamento de PDF**: PyMuPDF (fitz)
- **Análise de texto**: Expressões Regulares (Regex)
- **Documentação**: Swagger UI automática

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes)

### 1. Clone o repositório
```bash
git clone <url>
cd PortalPDF
```

### 2. Instale as dependências
```bash
pip install fastapi uvicorn python-multipart PyMuPDF
```

### 3. Executar a API
```bash
python main.py
```

### 4. Veja a documentação da api
Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc

### 5. Frontend
Abra o arquivo index.html para executar e testar o backend