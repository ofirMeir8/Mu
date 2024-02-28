from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/name/')
def name_page():
    return render_template('name.html')

@app.route('/gameone/')
def gameone_page():
    return render_template('gameone.html')

@app.route('/gametwo/')
def gametwo_page():
    return render_template('gametwo.html')

@app.route('/tk/')
def tk_page():
    return render_template('tk.html')

@app.route('/gamethree/')
def gamethree_page():
    return render_template('gamethree.html')

@app.route('/gamefour/')
def gamefour_page():
    return render_template('gamefour.html')

@app.route('/tk_opener_first/')
def tk_opener__first():
    subprocess.Popen(['python', 'riddleOne.py'])
    return render_template('gamethree.html')

@app.route('/tk_opener_second/')
def tk_opener__second():
    subprocess.Popen(['python', 'riddleTwo.py'])
    return render_template('gamefour.html')

@app.route('/end/')
def end():
    return render_template('end.html')

@app.route('/treasure/')
def treasure():
    return render_template('treasure.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)

