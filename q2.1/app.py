from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    banner = r"""
    /\_/\           ___
   = o_o =_______    \ \  - HELLO from Dockerfile!-
    __^      __(  \.__) )
(@)<_____>__(_____)____/
 
    """
    return f"<pre>{banner}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
