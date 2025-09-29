from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

def configure_swagger(app: FastAPI):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Verificador de Etiquetas",
            version="1.0.0",
            description="API para verificar etiquetas do Mercado Livre",
            routes=app.routes,
        )

        openapi_schema["paths"]["/verificar"]["post"]["summary"] = "Verificar etiqueta"
        openapi_schema["paths"]["/verificar"]["post"]["description"] = "Envie um PDF da etiqueta para verificar se está correta"
        
        openapi_schema["paths"]["/verificar"]["post"]["responses"] = {
            "200": {
                "description": "Sucesso",
                "content": {
                    "application/json": {
                        "examples": {
                            "etiqueta_ok": {
                                "summary": "Etiqueta correta",
                                "value": {"status": "ok"}
                            },
                            "etiqueta_erro": {
                                "summary": "Etiqueta com problema", 
                                "value": {"status": "erro"}
                            }
                        }
                    }
                }
            },
            "400": {
                "description": "Arquivo inválido",
                "content": {
                    "application/json": {
                        "example": {"detail": "Apenas arquivos PDF são aceitos"}
                    }
                }
            }
        }

        openapi_schema["paths"]["/"]["get"]["summary"] = "Status da API"
        openapi_schema["paths"]["/"]["get"]["description"] = "Verifica se a API está funcionando"
        openapi_schema["paths"]["/"]["get"]["responses"] = {
            "200": {
                "description": "Sucesso",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {
                                    "type": "string",
                                    "example": "API Verificador de Etiquetas - Mercado Livre"
                                }
                            }
                        }
                    }
                }
            }
        }

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi