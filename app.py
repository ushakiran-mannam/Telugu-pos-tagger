import numpy as np
from flask import Flask, request, jsonify, render_template
from tagger import find_tag,disambiguer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tag',methods=['POST'])
def tag():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [str(x) for x in request.form.values()]
    input = request.form.values()
    for i in input:
        input_string = i
    # print(input_string)
    output_result = []
    input_words = input_string.split()

    for i in input_words:
        output_result.append([i,find_tag(i)])
    
    # print(int_features)
    # print(len(int_features))
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    output =  output_result  # round(prediction[0], 2)

    output_disambi  =  disambiguer(output)

    return render_template('index.html', prediction_text='POS TAGS FOR WORDS ARE {}'.format(output_result), after_disambiguity='AFTER DISAMBIGUATION {}'.format(output_disambi))


# @app.route('/bert',methods=['POST'])
# def bert():
#     return render_template('index.html', prediction_text='Hello world {}'.format("Hello"))
# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)