import flask
import flask.typing
import functions_framework as ff

@ff.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return "Hello wonderful serverless world!"

# gcloud functions deploy my-http-function   \
# --gen2   \
# --region=asia-southeast1   \
# --runtime=python312   \
# --source=.   \
# --entry-point=hello   \
# --trigger-http