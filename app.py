from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Event and Ticket Management System</h1>
    <h2>Welcome!</h2>
    <p>Manage Events and Book Tickets Online.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
