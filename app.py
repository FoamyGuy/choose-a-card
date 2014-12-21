from flask import Flask, request, render_template
from cards import card_dict
# set the project root directory as the static folder, you can set others.

app = Flask(__name__, static_url_path='')
app._static_folder = "static/"

@app.route('/')
def root():
    f = open("card.txt", 'r')
    cur_card = f.read()
    f.close()
    return render_template('index.html', card=card_dict[cur_card])


@app.route('/hi')
def hi():
    return "OH HAI!"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
