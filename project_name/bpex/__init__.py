'''
example of a hierarchical structure using blueprints
'''

from flask import Blueprint

bp = Blueprint('bpex', __name__, url_prefix='/bpex')

@bp.route('sample')
def sample():
    return 'hello from a path down'
