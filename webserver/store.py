import requests
def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    categorias = r.json()
    for category in categorias:
        print(category['name'])