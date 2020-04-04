from app.main import bp
from flask import render_template

@bp.route('/', methods=['GET'])
def index():
	return render_template('index.html', title='Home')

@bp.route('/test', methods=['GET'])
def test():
	return render_template('index.html', title='Test')