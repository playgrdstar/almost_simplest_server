from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
  return render_template('base.html', 
                        title='This is the title', 
                        bodytext='This is the body text')

@app.route("/extended")
def extended():
  return render_template('extension.html', 
                        title_extended='This is the title of another page', 
                        bodytext_extended='This is the body text of another page ')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)