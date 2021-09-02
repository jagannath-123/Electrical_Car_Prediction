from flask import Flask, request, render_template

from Cars import Cars

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    req = request.form
    f=0
    ans=""
    if request.method == "POST" and request.form.get("click"):
        size = request.form.get("size")
        road = request.form.get("road")
        battery = request.form.get("battery")
        time = request.form.get("time")
        pred = Cars()
        tem = pred.new_data([size,road,battery,time])
        f=1
    if f: ans = "The Best Electric car for you is: "+tem
    return render_template("index.html",ans=ans)


if __name__ == "__main__": 
    app.run(debug=False)
