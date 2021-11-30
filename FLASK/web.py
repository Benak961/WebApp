from flask import Flask,render_template,url_for
app=Flask(__name__)

posts=[
    {
        'author':'Narayan murthy',
        'title':'Infosys',
        'content':'Tech',
        'date_posted':'Nov 30 21'

    },
     {
        'author':'Jhon',
        'title':'BMS',
        'content':'Edu',
        'date_posted':'Nov 29 21'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",m='About')

if __name__=="__main__":
    app.run(debug=True)