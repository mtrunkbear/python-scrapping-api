from requests_html import HTMLSession

# Inicializar una sesión de requests-html
session = HTMLSession()

# Navegar a la página web que contiene elementos con lazy loading
url = "https://www.example.com"
response = session.get(url)

# Desplazarse hacia abajo en la página web para cargar los elementos con lazy loading
response.html.render(sleep=1, keep_page=True)

# Obtener el contenido HTML actualizado de la página web
html = response.html.html

# Crear un objeto BeautifulSoup a partir del contenido HTML actualizado
soup = BeautifulSoup(html, 'html.parser')

# Buscar los elementos que necesitas utilizando las funciones de BeautifulSoup