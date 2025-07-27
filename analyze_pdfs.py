import PyPDF2
import re
import json

def extract_text_from_pdf(pdf_path):
    """Extrai texto de um arquivo PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Erro ao ler PDF {pdf_path}: {e}")
        return ""

def analyze_custeio_document(text):
    """Analisa o documento de custeio e extrai informações relevantes"""
    info = {
        "tipo": "custeio",
        "campos_identificados": []
    }
    
    # Padrões comuns em documentos de custeio
    patterns = {
        "nome_cliente": r"(?:Nome|Cliente|Solicitante)[:\s]*([A-Za-zÀ-ÿ\s]+)",
        "cpf_cnpj": r"(?:CPF|CNPJ)[:\s]*(\d{3}[.\-]?\d{3}[.\-]?\d{3}[.\-]?\d{2}|\d{2}[.\-]?\d{3}[.\-]?\d{3}[.\-]?\d{4}[.\-]?\d{2})",
        "valor": r"(?:Valor|Montante|Total)[:\s]*R?\$?\s*([\d.,]+)",
        "data": r"(?:Data|Data de)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
        "endereco": r"(?:Endereço|Endereco)[:\s]*([A-Za-zÀ-ÿ\s,\d\-]+)",
        "telefone": r"(?:Telefone|Tel|Fone)[:\s]*([\d\s\-\(\)]+)",
        "email": r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",
        "finalidade": r"(?:Finalidade|Objetivo|Propósito)[:\s]*([A-Za-zÀ-ÿ\s]+)",
        "prazo": r"(?:Prazo|Vencimento)[:\s]*(\d+\s*(?:dias|meses|anos))",
        "taxa_juros": r"(?:Taxa|Juros)[:\s]*([\d.,]+%?)",
        "garantia": r"(?:Garantia|Colateral)[:\s]*([A-Za-zÀ-ÿ\s]+)"
    }
    
    for field_name, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            info["campos_identificados"].append({
                "campo": field_name,
                "padrao": pattern,
                "exemplos": matches[:3]  # Primeiros 3 exemplos
            })
    
    return info

def analyze_investimento_document(text):
    """Analisa o documento de investimento e extrai informações relevantes"""
    info = {
        "tipo": "investimento",
        "campos_identificados": []
    }
    
    # Padrões específicos para investimento
    patterns = {
        "nome_cliente": r"(?:Nome|Cliente|Investidor)[:\s]*([A-Za-zÀ-ÿ\s]+)",
        "cpf_cnpj": r"(?:CPF|CNPJ)[:\s]*(\d{3}[.\-]?\d{3}[.\-]?\d{3}[.\-]?\d{2}|\d{2}[.\-]?\d{3}[.\-]?\d{3}[.\-]?\d{4}[.\-]?\d{2})",
        "valor_investimento": r"(?:Valor|Investimento|Capital)[:\s]*R?\$?\s*([\d.,]+)",
        "tipo_investimento": r"(?:Tipo|Categoria|Modalidade)[:\s]*([A-Za-zÀ-ÿ\s]+)",
        "data_inicio": r"(?:Data de Início|Início)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
        "prazo_investimento": r"(?:Prazo|Duração|Período)[:\s]*(\d+\s*(?:dias|meses|anos))",
        "rentabilidade": r"(?:Rentabilidade|Retorno|Taxa)[:\s]*([\d.,]+%?)",
        "endereco": r"(?:Endereço|Endereco)[:\s]*([A-Za-zÀ-ÿ\s,\d\-]+)",
        "telefone": r"(?:Telefone|Tel|Fone)[:\s]*([\d\s\-\(\)]+)",
        "email": r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",
        "objetivo": r"(?:Objetivo|Finalidade|Propósito)[:\s]*([A-Za-zÀ-ÿ\s]+)"
    }
    
    for field_name, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            info["campos_identificados"].append({
                "campo": field_name,
                "padrao": pattern,
                "exemplos": matches[:3]
            })
    
    return info

def main():
    """Função principal para analisar os documentos"""
    
    # Analisar documento de custeio
    print("=== ANALISANDO DOCUMENTO DE CUSTEIO ===")
    custeio_text = extract_text_from_pdf("Custeio Claudinei Couto  05 07 24.pdf")
    if custeio_text:
        custeio_info = analyze_custeio_document(custeio_text)
        print(f"Tipo: {custeio_info['tipo']}")
        print(f"Campos identificados: {len(custeio_info['campos_identificados'])}")
        for campo in custeio_info['campos_identificados']:
            print(f"- {campo['campo']}: {campo['exemplos']}")
    
    print("\n" + "="*50 + "\n")
    
    # Analisar documento de investimento
    print("=== ANALISANDO DOCUMENTO DE INVESTIMENTO ===")
    investimento_text = extract_text_from_pdf("Investimento Pecuário de Renato Renor Caldeira.pdf")
    if investimento_text:
        investimento_info = analyze_investimento_document(investimento_text)
        print(f"Tipo: {investimento_info['tipo']}")
        print(f"Campos identificados: {len(investimento_info['campos_identificados'])}")
        for campo in investimento_info['campos_identificados']:
            print(f"- {campo['campo']}: {campo['exemplos']}")
    
    # Salvar análise em JSON para referência
    analysis = {
        "custeio": custeio_info if 'custeio_info' in locals() else {},
        "investimento": investimento_info if 'investimento_info' in locals() else {}
    }
    
    with open("document_analysis.json", "w", encoding="utf-8") as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)
    
    print("\nAnálise salva em 'document_analysis.json'")

if __name__ == "__main__":
    main() 