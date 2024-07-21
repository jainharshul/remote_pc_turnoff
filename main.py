from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Remote PC Control</h1>
        <form action="/shutdown" method="post">
            <input type="submit" value="Shut Down PC">
        </form>
    </body>
    </html>
    '''

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system('shutdown /s /t 1')
    return 'Shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)