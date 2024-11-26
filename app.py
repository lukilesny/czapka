from flask import Flask, redirect, render_template_string, url_for, request, render_template
from checks import *

app = Flask(__name__)

@app.route('/start')
def start_page():
   return render_template('input.html')

@app.route('/input', methods=['POST', 'GET'])
def input_page():
    if request.method == 'POST':
        input_data = request.form['chars']
        return redirect(url_for('result_page', letters=input_data))
    else:
        input_data = request.args.get('chars')
        return redirect(url_for('result_page', letters=input_data))

# @app.route('/example')
# def example_result_page():
#    return render_template('example_result.html')

@app.route('/result/<letters>')
def result_page(letters):
    checked, left = check(letters)
    return render_template_string(generate_results_html(letters, checked, left))

if __name__ == '__main__':
    app.run()