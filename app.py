from flask import Flask , render_template , request 

app = Flask(__name__)


import model

@app.route("/",  methods = ['POST','GET'])
def hell():
    if request.method == 'POST':
        print('new prediction')
    return render_template("welcomepage.html")

@app.route("/index.html",  methods = ['POST','GET'])
def hello():
    if request.method == 'POST':
        print('new prediction')
    return render_template("index.html")

@app.route("/sub.html", methods = ['POST','GET'])
def submit():
        if request.method == 'POST':
         description_input = request.form['description']
         output = model.description_predict(description_input)     
        return render_template("sub.html", n= output, m= description_input)

@app.route("/indexcs.html",  methods = ['POST','GET'])
def hellocs():
    return render_template("indexcs.html")


@app.route("/subcs.html",  methods = ['POST','GET'])
def submitcs():
    if request.method == 'POST':
        fname_input = request.form['firstname']
        lname_input = request.form['lastname']
        tech_input = request.form['technology']
        skill_input = request.form['skills']
        loc_input = request.form['location']
    return render_template("subcs.html", a = tech_input, b = skill_input, c = loc_input, d = fname_input, e = lname_input)




if __name__== "__main__":
    app.run(debug=True)