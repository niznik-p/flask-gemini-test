# flask-gemini-test
Making a really basic Flask app for discussion at PrincetonPy

## Basic Walkthrough

- Get a Google Generative Language API key from the Google Cloud (you should be able to sign up for a demo for free)
  - If you don't want to use Google, you should be able to adapt the code to work with OpenAI or some other free options (?)
- Clone the repo (obviously)
- Create a conda environment with flask installed (`conda create -n flask-demo python=3.12 flask`)
- Activate the environment and run `pip install google-generativeai`
- Make sure to set the environment variable for your API Key (`export GOOGLE_API_KEY=<your key>`)
  - I just do it as a one-off, but you can also set it in your `.bashrc` or `.bash_profile`, etc.
- Run the app with `python app.py`
- Open a browser and navigate to `localhost:8008` to use the website OR run `python api_test.py` to see the API response