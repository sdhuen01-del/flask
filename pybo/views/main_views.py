from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Pybo index!'

@bp.route('/hello')
def hello_world():
    return 'Hello pybo!'

@bp.route('/login')
def login():
    return '로그인 페이지 입니다.'

@bp.route('/logout')
def logout():
    return '로그아웃 페이지 입니다.'