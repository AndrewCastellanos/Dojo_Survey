from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key= "Keep it safe"






@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_result():
    session["name"]= request.form['name']
    session["Dojo_Location"]= request.form['Dojo_Location']
    session["Favorite_Language"]= request.form['Favorite_Language']


    
    return redirect('/result')

@app.route('/result') 
def show_result():
    return render_template("result.html")



if __name__ == '__main__':
    app.run(debug = True)




