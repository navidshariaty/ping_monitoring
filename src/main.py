"""
    laus deo
    pining program and monitor it realtime
    Eng: P.Zahedi
    E-mail: p.zahedi@live.com
    Github: pouyazhd
"""
import util

from flask import Flask, jsonify, make_response, request


if __name__ == "__main__":
    args = util.parse_args()
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health_check():
        return make_response(
            jsonify(
                {"status": "OK"}
            ),
            200
        )

    @app.route('/ping', methods=["POST"])
    def ping_handler():
        request_data = request.get_json(force=True)
        host = request_data.get("host")
        duration = request_data.get("duration", "30s")
        if not host:
            return make_response(
                "host not provided", 400
            )
        pm_object = util.PingMonitoring(host, duration)
        if pm_object.error_happened:
            return make_response(
                "bad duration parameter", 400
            )
        return make_response(
            jsonify(pm_object.ping_action()), 200
        )

    app.run(host=args.flask_host, port=args.flask_port, debug=False)
