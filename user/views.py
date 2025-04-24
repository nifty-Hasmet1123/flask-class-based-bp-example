from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView
import logging

# NOTE FOR EACH CLASS ONLY 1 CRUD(GET, POST, PUT, DELETE) method only other methods will be considered as helper methods only
# GENERAL RULE IF YOU WERE TO USE THE METHODVIEW YOU WILL NEED TO UNDERSTAND THAT IF YOUR INTENTIONS ARE TO ONLY HAVE 1 LOGIC FOR EACH CRUD 
# USE FUNCTION BASE IF YOU PLAN TO HAVE MULTIPLE POST ETC.

user_bp = Blueprint("user_bp", __name__)

class User(MethodView):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def get(self):
        return render_template("index.html")
    
    # for body parameter only if you want you can handle it here if statement but please just use the function LOL
    def post(self):
        json_body = request.get_json(silent=True)
    
        if json_body:
            result = json_body.get("data", None)
            return jsonify({ "success body": f"{result}" }), 200
        return jsonify({ "error": "no data" }), 400
    
    # adding additional routes using function base then attaching to the blueprint
    @staticmethod
    @user_bp.route("/user/query", methods=["POST"])
    def query_param():
        query_parameter = request.args
        
        if query_parameter:
            result = query_parameter.get("q") # provided that q is a params
            return jsonify({ "success query params": f"{result}" }), 200
        return jsonify({ "error": "no query params detected." }), 400

    @staticmethod
    @user_bp.route("/user/<int:user_id>", methods=["POST"])
    def url_param(user_id):
        num = int(user_id)
        
        # logging from the User class
        User.logger.info(f"\n***\nReceived user_id: {user_id}\n***")

        if num:
            return jsonify({ "Success": f"On fetching the number: {user_id}" }), 200
        return jsonify("error"), 400

user_view = User.as_view(name="user_api")
user_bp.add_url_rule("/user", view_func=user_view, methods=["GET"])
user_bp.add_url_rule("/user", view_func=user_view, methods=["POST"])
