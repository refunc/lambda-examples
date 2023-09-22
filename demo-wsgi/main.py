from madara.app import Madara
from madara.wrappers import Request
from madara.blueprints import Blueprint

app = Madara(config={
    "debug": False,
    "middlewares": []
})

bp_lambda = Blueprint("lambda")


@bp_lambda.route("/", methods=["GET"])
def index(request: Request):
    return "index"


@bp_lambda.route("/hello", methods=["GET"])
def hello(request: Request):
    return "hello"


app.register_blueprint(bp_lambda, url_prefix="/default/demo-wsgi")

if __name__ == "__main__":
    app.run()
