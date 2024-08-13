from flask import Flask, render_template, request
import speech2text
import action

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_val = ""
    bot_val = None

    if request.method == "POST":
        if "ask" in request.form:
            user_val = speech2text.speech2text()
            bot_val = action.Action(user_val)
        elif "send" in request.form:
            user_val = request.form["user_input"]
            bot_val = action.Action(user_val)
        elif "delete" in request.form:
            user_val = ""
            bot_val = None

        # If the bot requests to shut down
        if bot_val == "Ok, shutting down!":
            return render_template("shutdown.html")

    return render_template("index.html", user_val=user_val, bot_val=bot_val)

if __name__ == "__main__":
    app.run(debug=True)
