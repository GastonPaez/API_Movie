from flask import Flask, render_template
import ssl
import requests

app = Flask(__name__, template_folder= 'templates')


url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMDcyMDBkMzRlMDQ3YTc0NWM5ODAyYzJjYTgyM2I1NiIsInN1YiI6IjY1ZTdhMTNjYTZjMTA0MDE4N2U4MzNhOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GudR83qtZWM4hoJP2FAcKAU6_Rl5kZLHC03EsPciQ3A"
}

r = requests.get(url, headers=headers)

print("| Funcionando |")

# Resultados de la api que traer peliculas
resultados=r.json()
ultimos=resultados["results"][-10:] # Ultimas 10 peliculas

print(type(resultados))
@app.route('/')
def index():
    ssl._create_default_https_context=ssl._create_default_https_context
    
    return render_template('index.html', data=resultados["results"], bottom=ultimos)


if __name__ == '__main__':
    app.run(debug=True)