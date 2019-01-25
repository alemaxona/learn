from flask import Flask, render_template
from random import randint

# Указание каталога шаблонов
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    report = [randint(0, 20) for _ in range(25)]
    return render_template('report.txt', data=report)

def my_name(value):
    return 'SONY '+ value
app.jinja_env.globals.update(my_name=my_name)  # Глобальная переменная, которую можно импортировать в каждый шаблон.

if __name__ == '__main__':
    app.run()
