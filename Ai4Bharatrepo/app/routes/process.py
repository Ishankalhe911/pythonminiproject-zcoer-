from flask import Blueprint, request, Response

bp = Blueprint('process', __name__, url_prefix='/process')

@bp.route('/status', methods=['POST'])
def call_status():
    status = request.values.get('CallStatus')
    print(f"📡 Callback Call Status: {status}")

    return Response("", status=200)
