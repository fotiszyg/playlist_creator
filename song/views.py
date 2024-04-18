from flask import Blueprint

from common import upload_csv_file

bp = Blueprint("upload", __name__)


@bp.route("/upload")
def post():
    return upload_csv_file()
