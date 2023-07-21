""" Importing a library for working with Flask and running subprocesses """

import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ This function starts and is responsible for the process
    of returning the result index.html """
    return render_template('index.html')

@app.route("/run_allure")
def run_allure():
    """ This function starts and is responsible for generating the report allure. """

    cmd = ["./scriptsh/run_allure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_add_basket")
def run_test_add_basket():
    """ This function starts and is responsible for page tests test_add_basket """
    cmd = ["./scriptsh/run_test_add_basket.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_header")
def run_test_header():
    """ This function starts and is responsible for page tests test_header """
    cmd = ["./scriptsh/run_test_header.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_leave_comment")
def run_test_leave_comment():
    """ This function starts and is responsible for page tests test_leave_comment """
    cmd = ["./scriptsh/run_test_leave_comment.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_login")
def run_test_login():
    """ This function starts and is responsible for page tests test_login """
    cmd = ["./scriptsh/run_test_login.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_sing_up")
def run_test_sing_up():
    """ This function starts and is responsible for page tests test_sing_up """

    cmd = ["./scriptsh/run_test_sing_up.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_all_tests")
def run_all_tests():
    """ This function starts and is responsible for page tests test_all """

    cmd = ["./scriptsh/run_all_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route("/run_test_api")
def run_test_api():
    """ This function starts and is responsible for page tests test_api """

    cmd = ["./scriptsh/run_api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

if __name__ == "__main__":
    app.run(debug=True)
