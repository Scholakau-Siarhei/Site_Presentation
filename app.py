""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ Эта функция запускает и отвечает за процесс возврата результата index.html. """

    return render_template('index.html')

# @app.route("/error")
# def error():
#     """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
#     return render_template('test_error.html')

@app.route("/run_allure")
def run_allure():
    """ Эта функция запускает и отвечает за генерацию отчета allure. """

    cmd = ["X:/Learn_QA/PYTHON/my_work/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_sing_up")
def run_test_sing_up():
    """ Эта функция запускает и отвечает за тесты страницы """

    cmd = ["/scripts/run_test_sing_up.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

if __name__ == "__main__":
    app.run(debug=True)