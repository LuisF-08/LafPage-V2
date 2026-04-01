from fastapi import FastAPI
from app.routes import autenticacao
from app.middleware.middleware import  setup_middleware
from fastapi.responses import HTMLResponse

app = FastAPI()

setup_middleware(app)

app.include_router(autenticacao.router)

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


@app.get("/", response_class=HTMLResponse)
def inicio():
    return """
    <html>
        <head>
            <title>Minha API - Servidor Ativo</title>
            <style>
                body {
                    margin: 0;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    text-align: center;
                }
                .container {
                    padding: 2rem;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 16px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                    max-width: 600px;
                }
                h1 {
                    margin-bottom: 1rem;
                    font-size: 3rem;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                }
                .rocket {
                    font-size: 4rem;
                    margin: 1rem 0;
                }
                p {
                    font-size: 1.2rem;
                    margin-bottom: 1.5rem;
                }
                .status {
                    background: rgba(0, 255, 0, 0.2);
                    padding: 0.5rem 1rem;
                    border-radius: 8px;
                    display: inline-block;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="rocket">🚀</div>
                <h1>Servidor Ativo!</h1>
                <p>Sua API FastAPI está rodando com sucesso.</p>
                <div class="status">Status: Online</div>
            </div>
        </body>
    </html>
    """