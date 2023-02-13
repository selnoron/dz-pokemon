# Python
from typing import Any

# Other
import requests
from requests.models import Response

# Flask
from flask import (
    Flask, 
    render_template,
)
from flask.app import Flask as FlaskApp

# Local
from models.pokemon import (
    Pokemon,
    Name,
    Base
)

app: FlaskApp = Flask(__name__)
pokemons: list[Pokemon] = []
ppok: list[dict] = []

@app.route("/home")
def home_page() -> str:
    return "Welcome to my first page!"

@app.route("/")
def main_page() -> str:
    return render_template(
        'index.html',
        ctx_lst=pokemons,
        pok=ppok
    )

@app.route("/num")
def get_nubmers() -> str:
    result: str = ""
    for i in range(1, 2001):
        result += f"<h2>{i}</h2>"

    return result

if __name__ == '__main__':
    URL: str = (
        'https://raw.githubusercontent.'
        'com/fanzeyi/pokemon.json/'
        'master/pokedex.json'
    )
    response: Response =\
        requests.get(URL)
    data: list[dict] = response.json()

    pokemon: dict[str, Any]
    for pokemon in data:
        base = Base(
            *list(pokemon.get('base').values())
        )
        name = Name(
            *list(pokemon.get('name').values())
        )
        pkm = Pokemon(
            id=pokemon.get('id'),
            name=name,
            type=pokemon.get('type'),
            base=base
        )
        pokemons.append(pkm)

    pok_input: str = input()
    for pokemon in data:
        if pok_input == pokemon.get('name').get('english'):
            ppok.append(pokemon)
            print(pokemon)

    app.run(
        port=8080,
        debug=True
    )