from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    banner = r"""

HELLO from multistage Dockerfile!

                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
-------------{_}^-'{_}----------


    """
    return f"<pre>{banner}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
