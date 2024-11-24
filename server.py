from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # templates 폴더에서 index.html을 렌더링
    return render_template("index.html")
@app.route('/trigger-buzzer',methods=['POST'])
def trigger_buzzer():
    data = request.get_json()
    if data.get("motion"):
        print("buzzer") #buzzer sign chage
        return {"statu":"success"}, 200
    return {"status":"error"},400
if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=8080)

