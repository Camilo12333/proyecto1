from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello_world():
    return"<p>Hello, World Open Source<p>"

@app.route("/datos",methods=["GET", "POST"])
def formulario():
    if request.method=="POST":
        A = request.form['A']
        B = request.form['B']
        C = request.form['C']
        print(int(A)+ int(B)+ int(C))
        x1 = (-B + (B**2 + 4*A*C)**(1/2)) / (2*A)
        x2 = (-B - (B*B + 4*A*C)**(1/2)) / (2*A)
        print(f"El resultado de la función cuadrática es",x1, x2,)
        
        return render_template("formulario.html",C=C,A=A,B=B)
    
    return render_template("formulario.html")

if __name__=="__main__":
    app.run()