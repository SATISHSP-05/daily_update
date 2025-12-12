
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
        <h3>GET Example</h3>
        <a href="/get-info?name="username"">Click to Send GET Request</a>

        <h3>POST Example</h3>
        <form action="/post-info" method="POST">
            <input type="text" name="username" placeholder="Enter username">
            <button type="submit">Submit</button>
        </form>
    """)


@app.route("/get-info", methods=["GET"])
def get_info():
    name = request.args.get("name", "No Name Given")
    return render_template_string(f"""
        <h2>GET Method Output</h2>
        <p>You sent: <b>{name}</b></p>
        <a href="/">Back</a>
    """)

@app.route("/post-info", methods=["POST"])
def post_info():
    username = request.form.get("username")
    return render_template_string(f"""
        <h2>POST Method Output</h2>
        <p>You submitted: <b>{username}</b></p>
        <a href="/">Back</a>
        <a href="/get-info?name="username"">Click to Send GET Request</a>

    """)



if __name__ == "__main__":
    app.run(debug=True)
