from flask import Blueprint

from list.service import decade_playlist

bp = Blueprint("list", __name__)


@bp.route("/list/<int:decade>")
def get(decade):
    return decade_playlist(decade)
