
from rfctl.client import LambdaClient

client = LambdaClient("default")

rsp = client.invoke_function("demo-gin", {}, get_log=True)

print(rsp)
