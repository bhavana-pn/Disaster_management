from flask import Flask, url_for , render_template
import http_request
import model
import mail

app = Flask(__name__)

@app.route("/")
def home():
    prediction = model.get_prediction()
    

    prediction = "high"
    if(prediction=="nil"):
        
        return render_template("index.html",content = "Nil Chances of fire")

    elif(prediction=="Mild"):
        return render_template("index.html",content = "Low Chances of fire")

    elif(prediction=="Good"):
        mail.send_mail()
        return render_template("index.html",content = "Good chances of fire") 

    else:
        mail.send_mail()
        return render_template("index.html",content = "High chances of fire") 

if __name__ == "__main__":
    app.run()

