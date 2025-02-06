from flask import Flask, redirect, render_template_string, url_for, request, render_template
from unidecode import unidecode
from checks import generate_alfabet, check, generate_results_html

app = Flask(__name__)

@app.route('/')
@app.route('/start')
def start_page():
   return render_template('input.html')

@app.route('/input', methods=['POST']) # TO DO: remember previous values
def input_page():
    if request.method == 'POST':
        input_data = request.form['chars']
        selected = request.form.getlist('zestaw')
        rmed = request.form.getlist('replace')[0] #replace_from
        added = request.form.getlist('replace')[1] #replace_to
        rmed += request.form['lost']
    # else: # GET
        # input_data = request.args.get('chars')
    input_data = unidecode(input_data.upper())
    rmed = unidecode(rmed.upper())
    added = unidecode(added.upper())
    alfabet = generate_alfabet(selected, added, rmed)
    print("DEBUG: input", selected, "+", added, "-", rmed, "=", alfabet)
    return redirect(url_for('result_page', letters=input_data, alfabet=alfabet))

# @app.route('/example')
# def example_result_page():
#    return render_template('example_result.html')

@app.route('/result/<letters>::<alfabet>')
def result_page(letters, alfabet):
    checked, left = check(letters, alfabet)
    return render_template_string(generate_results_html(letters, checked, left))

if __name__ == '__main__':
    app.run()