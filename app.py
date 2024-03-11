# pip3 install flask diceware

# from flask import Flask, render_template, request
# from diceware import get_passphrase

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         words = int(request.form.get('words', 6))
#         delimiter = request.form.get('delimiter', ' ')
#         capitalization = request.form.get('capitalization') == 'on'
#         options = {
#             'randomsource': 'system',
#             'caps': capitalization,
#             'num': words,
#             'sep': delimiter
#         }
#         print(options)
#         password = get_passphrase(options)
#         return f'Your new password is: {password}'
#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from diceware import get_passphrase, pkg_resources

wordlist_file = pkg_resources.resource_filename('diceware', 'wordlists/wordlist_en.txt')

class Options:
    def __init__(self, num, caps, sep):
        self.num = num
        self.caps = caps
        self.delimiter = sep
        self.specials = 0
        self.randomsource = "system"
        self.wordlist = "en_securedrop"
        self.infile = wordlist_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        words = int(request.form.get('words', 6))
        delimiter = request.form.get('delimiter', '')
        capitalization = request.form.get('capitalization') == 'on'
        options = Options(words, capitalization, delimiter)
        password = get_passphrase(options)
        return f'Your new password is: {password}'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)