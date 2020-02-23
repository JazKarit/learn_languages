from flask import Flask,render_template,request
# from form import WordForm

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/',methods=['POST','GET'])
def index():
    return("hello world")
    # return render_template('index.html')

# @app.route('/response',methods = ['POST', 'GET'])
# def response():
#     if request.method == 'POST':
#       words = request.form
#       response = words['word1']

#       return render_template("index.html",return_str = response)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')