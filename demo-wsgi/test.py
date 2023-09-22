
from rfctl.client import LambdaClient

client = LambdaClient("default")

rsp = client.invoke_function("demo-wsgi", {}, get_log=True)

print(rsp)
