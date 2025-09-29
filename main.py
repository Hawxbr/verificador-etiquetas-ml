from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz
import re
import tempfile
import os
from swagger_config import configure_swagger

app = FastAPI()

configure_swagger(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EtiquetaService:
    @staticmethod
    def verificar_etiqueta_pdf(file_path: str) -> str:
        try:
            texto = ""
            doc = fitz.open(file_path)
            for page in doc:
                texto += page.get_text()
            doc.close()
            
            texto = texto.lower()
            
            padroes_erro = [
                r'erro', r'error', r'invoice_pending', r'pendente', 
                r'falha', r'invalid', r'rejeitado', r'rejected'
            ]
            
            for padrao in padroes_erro:
                if re.search(padrao, texto):
                    return "erro"

            padroes_ok = [
                r'etiqueta', r'label', r'envio', r'shipping',
                r'mercado livre', r'mercado envios', r'meli',
                r'\d{10,13}', 
                r'\d{8,12}',
                r'nf[:\-\s]*\d+',
                r'[a-z]{2}\d{9}[a-z]{2}'
            ]
            
            padroes_encontrados = 0
            for padrao in padroes_ok:
                if re.search(padrao, texto):
                    padroes_encontrados += 1

            if padroes_encontrados >= 2:
                return "ok"
            else:
                return "erro"
                
        except Exception:
            return "erro"

@app.post("/verificar")
async def verificar_etiqueta(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são aceitos")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_path = temp_file.name
        
        resultado = EtiquetaService.verificar_etiqueta_pdf(temp_path)
        os.unlink(temp_path)
        
        return {"status": resultado}
        
    except Exception:
        return {"status": "erro"}

@app.get("/")
async def root():
    return {"message": "API Verificador de Etiquetas - Mercado Livre"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)