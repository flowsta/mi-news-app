import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

csv_path = './static/espanaenllamas.csv'
csv_obj = csv.DictReader(open(csv_path, 'r'))
csv_list = list(csv_obj)

@app.route("/")
def index():
    return render_template('index.html',
        object_list=csv_list,
    )

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )
    
    

