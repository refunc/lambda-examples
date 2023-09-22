from apig_wsgi import make_lambda_handler
from main import app

# Configure this as your entry point in AWS Lambda
lambda_handler = make_lambda_handler(app)
