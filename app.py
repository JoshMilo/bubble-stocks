from flask import Flask, render_template, jsonify
from stock_scraper import get_data


app = Flask(__name__)


@app.route('/data')
def data():
    return jsonify(get_data())


if __name__ == '__main__':
    app.run()
