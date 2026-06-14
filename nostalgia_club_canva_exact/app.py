from flask import Flask, render_template, abort

app = Flask(__name__)

LOOKS = {
    "look-01": {
        "number": "LOOK 01",
        "title": "Polkadot Volume",
        "image": "img/look_01.png",
        "description": "Top blanco con polkadots y volumen suave, combinado con pantalón negro amplio. Una prenda delicada, cómoda y nostálgica."
    },
    "look-02": {
        "number": "LOOK 02",
        "title": "Denim Memory",
        "image": "img/look_02.png",
        "description": "Conjunto denim oscuro con cuello protagonista y pantalón wide leg. Una propuesta estructurada con inspiración en memoria, campo y vestuario cotidiano."
    },
    "look-03": {
        "number": "LOOK 03",
        "title": "Soft Black",
        "image": "img/look_03.png",
        "description": "Look total black con silueta relajada, volumen y detalle translúcido en polkadots. Una pieza sutil, oscura y contemporánea."
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/look/<slug>")
def look_detail(slug):
    look = LOOKS.get(slug)
    if not look:
        abort(404)
    return render_template("look.html", look=look)

if __name__ == "__main__":
    app.run(debug=True)
