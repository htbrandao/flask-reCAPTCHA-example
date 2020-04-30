import json
from requests import post
from flask import Flask, render_template, request


# helpers ============================================================ #

class ReCaptha():
    # self generated
    SECRET_KEY = 'verylongstringhasgwhatever' 
    RECAPTCHA_USE_SSL= False
    RECAPTCHA_PUBLIC_KEY = 'googleGeneratedPubKey' # google generated
    RECAPTCHA_PRIVATE_KEY = 'googleGeneratedPrivateKey' # google generated
    RECAPTCHA_DATA_ATTRS = {'theme': 'light'}


def is_human(captcha_response):
    payload = {'response': captcha_response, 'secret': private_key}
    response = post("https://www.google.com/recaptcha/api/siteverify", data=payload)
    response_text = json.loads(response.text)
    return response_text['success']


# main =============================================================== #

app = Flask(__name__)
app.config.from_object(ReCaptha)

pub_key = ReCaptha.RECAPTCHA_PUBLIC_KEY
private_key = ReCaptha.RECAPTCHA_PRIVATE_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        success()
    return render_template('home.html', pub_key=pub_key)


@app.route('/success', methods=['GET', 'POST'])
def success():
    captcha_response = request.form['g-recaptcha-response']
    print(captcha_response)
    if is_human(captcha_response):
        return render_template('success.html')
    else:
        return render_template('fail.html')
    return render_template('success.html')


@app.route('/fail', methods=['GET', 'POST'])
def fail():
    return render_template('fail.html')


# start ============================================================== #

if __name__ == "__main__":
    app.run()
