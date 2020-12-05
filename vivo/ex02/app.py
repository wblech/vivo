from flask import Flask
from flask import request

from vivo.config import settings
from vivo.ex01.get_an import get_an


app = Flask(__name__)


@app.route('/')
def get_list():
    args = request.args
    new_list = list(args.values())
    int_list = [int(num) for pos in new_list for num in pos if num != ',']
    list_parse = get_an(int_list)
    response = app.response_class(
        response=list_parse, status=200, mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, port=5000)
