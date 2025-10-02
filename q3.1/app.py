from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    banner = r"""

HELLO from Docker compose!

                  /)-._
                 Y. ' _]
          ,.._   |`--"=
         /    "-/   \
/)     |   |_     `\|___
\:::::::\___/_\__\_______\

    """
    return f"<pre>{banner}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
