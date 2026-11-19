from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def logs():
    with open("/app/logs/visits.log", "a") as f:
        f.write(f"New visit registered. {datetime.datetime.now()}\n")
    return "Visit logged successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)