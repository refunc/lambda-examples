# lambda-examples

Create your refunc lambda func with [refunc-cli](https://github.com/refunc/refunc-cli).

```
export AWS_DEFAULT_ENDPOINT=http://aws-api-gw-endpoint
export AWS_ACCESS_KEY_ID=<your-key-id>
export AWS_SECRET_ACCESS_KEY=<your-access-key>
```

### Create func

```
mkdir demo-func && cd demo-func
rfctl init
rfctl create
```

### Test func

```
python test.py
```

### Update Code

```
rfctl update-code
```

### Invoke func with http

```
rfctl create-url
curl http://refunc-http-endpoint/<namespace>/demo-func
```