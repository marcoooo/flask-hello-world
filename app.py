from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <div class="container">Hello Seqone!</div>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
