from flask import Flask, redirect, render_template_string, url_for, request, render_template
from unidecode import unidecode
from checks import generate_sets, check, generate_results_html

app = Flask(__name__)

@app.route('/')
@app.route('/start')
def start_page():
   return render_template('input.html')

@app.route('/input', methods=['POST', 'GET']) # moze tylko POST? i bez else
def input_page():
    if request.method == 'POST':
        input_data = request.form['chars']
        selected = request.form.getlist('zestaw')
    else:
        input_data = request.args.get('chars')
    input_data = unidecode(input_data.upper())
    # to do: po minusie mozna dac zgubione literki, np luca di bosqo
    sets = generate_sets(selected)
    print("input_page", selected, sets)
    return redirect(url_for('result_page', letters=input_data, sets=sets))

# @app.route('/example')
# def example_result_page():
#    return render_template('example_result.html')

@app.route('/result/<letters>::<sets>')
def result_page(letters, sets):
    print("result_page", sets)
    checked, left = check(letters, sets)
    return render_template_string(generate_results_html(letters, checked, left))

if __name__ == '__main__':
    app.run()