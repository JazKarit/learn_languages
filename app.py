from flask import Flask,render_template,request
from form import WordForm
from ngram import ngram,generatetext,translations

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/response',methods = ['POST', 'GET'])
def response():
    if request.method == 'POST':
      word_tuples = request.form
      words = [word_tuples['word1'],word_tuples['word2'],word_tuples['word3'],word_tuples['word4'],word_tuples['word5']]
      response_list = generatetext(words)
      translation = translations(words)
      print(response_list)
      return render_template("index.html",response_list = response_list,len = len(response_list),special_words = words,flag='false',translation=translation)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')