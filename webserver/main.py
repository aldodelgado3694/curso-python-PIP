import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contacto", response_class=HTMLResponse)
def get_items():
    return """
    <h1>Hola soy una pagina en H1</h1>
    <p>Soy un parrafo</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()


