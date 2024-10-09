from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# List of feminine animal names
animal_names = [
    "Ladybug", "Doe", "Kitten", "Lioness", "Vixen", "Dove", "Hen", "Mermaid", "Swan", "Bunny"
]

# In-memory storage for chat messages
chat_history = []

def generate_animal_name():
    # Randomly assign a name that has not been assigned in the current session
    name = random.choice(animal_names)
    # Ensure the name is unique per session
    while any(chat['name'] == name for chat in chat_history):
        name = random.choice(animal_names)
    return name

@app.route('/')
def index():
    # Assign a unique code name if not already assigned in this session
    if 'code_name' not in session:
        session['code_name'] = generate_animal_name()
    return render_template('chat.html', chat_history=chat_history)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get the message from the form
    message = request.form.get('message')
    if message:
        # Append message with the session-specific code name to the chat history
        chat_history.append({'name': session['code_name'], 'message': message})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
