package main

import (
	"context"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/gin-gonic/gin"
	"github.com/thomasgouveia/aws-lambda-go-api-proxy/httpadapter"
)

var adapter *httpadapter.HandlerAdapterFnURL

func hello(c *gin.Context) {
	c.String(200, "hello")
}

func init() {
	eng := gin.Default()
	gin.SetMode(gin.ReleaseMode)
	apis := eng.Group("/default/demo-gin")
	{
		apis.GET("/hello", hello)
	}
	adapter = httpadapter.NewFunctionURL(eng)
}

func Handler(ctx context.Context, req events.LambdaFunctionURLRequest) (events.LambdaFunctionURLResponse, error) {
	return adapter.ProxyWithContext(ctx, req)
}

func main() {
	lambda.Start(Handler)
}
