from flask import Blueprint, url_for, redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

# 컨트롤 + 스페이스바 임포트 추가 후 자동으로 불러 와서 추후 추가문 작성
@bp.route('/')
def index():
    return redirect(url_for('question._list'))
