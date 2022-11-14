from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Acesse a página de teste: http://127.0.0.1:5000/test"

@app.route("/test")
def test():
    return {"test": ["01 Project", "02 Python", "03 React"]}

if __name__ == "__main__":
    app.run(debug=True)