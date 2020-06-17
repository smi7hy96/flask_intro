from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! \n Open a new tab and enter /welcome/name for URL"


@app.route("/ryan")
def ryan():
    return "Hello Ryan"


@app.route("/welcome/<name>")
def welcome_name(name):
    return "Welcome " + name.title() + "!"


def factors(num):
    list_factors = []
    for x in range(1, num+1):
        if num % x == 0:
            list_factors.append(x)
    return list_factors


@app.route('/home')
def home():
    return '<a href="/factor_raw/100"> click here for an example</a>'


@app.route('/factor_raw/<int:n>')
def factors_display_raw_html(n):
    list_factor = factors(int(n))

    html = "<h1> Factors of "+str(n)+" are</h1>"+"\n"+"<ul>"
    for f in list_factor:
        html += "<li>"+str(f)+"</li>"+"\n"
    html += "</ul> </body>"
    return html


if __name__ == '__main__':
    app.run(debug=True)
