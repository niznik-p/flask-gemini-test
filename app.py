import os
from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash-latest')

form_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Ask Gemini</title>
    <style></style>
  </head>
  <body>
    <h1>Ask Gemini</h1>
    <form action="/ask" method="post">
      <input type="text" name="phrase" placeholder="What...is your NAME?" required>
      <input type="submit" value="Ask">
    </form>
    {% if question and answer %}
    <br><hr>
    <div id="question">
      <h2>{{ question }}</h2>
    </div>
    <div id="answer">
      <h2>Answer:</h2>
      <p>{{ answer }}</p>
    </div>
    {% endif %}
  </body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(form_template)


@app.route('/ask', methods=['POST'])
def ask_gemini():
    user_input = request.form.get('phrase')

    if not user_input:
        return jsonify({"error": "No phrase provided"}), 400

    try:
        response = model.generate_content(user_input)
        print(response)
        return render_template_string(form_template, question=user_input, answer=response.text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/ask', methods=['POST'])
def ask_gemini_api():
    user_input = request.json.get('phrase')

    if not user_input:
        return jsonify({"error": "No phrase provided"}), 400

    try:
        response = model.generate_content(user_input)
        return jsonify({"question": user_input, "answer": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=8008, debug=True)
