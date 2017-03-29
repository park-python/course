package main

import (
	"fmt"
	"log"
	"time"

	"github.com/valyala/fasthttp"
)

func requestHandler(ctx *fasthttp.RequestCtx) {
	started := time.Now()
	defer func() {
		log.Printf("Request %s", time.Now().Sub(started))
	}()
	time.Sleep(100 * time.Millisecond)
	fmt.Fprintf(ctx, "Hello, world!\n\n")
	fmt.Fprintf(ctx, "Request method is %q\n", ctx.Method())
	fmt.Fprintf(ctx, "RequestURI is %q\n", ctx.RequestURI())
	fmt.Fprintf(ctx, "Requested path is %q\n", ctx.Path())
	fmt.Fprintf(ctx, "Host is %q\n", ctx.Host())
	fmt.Fprintf(ctx, "Query string is %q\n", ctx.QueryArgs())
	fmt.Fprintf(ctx, "User-Agent is %q\n", ctx.UserAgent())
	fmt.Fprintf(ctx, "Connection has been established at %s\n", ctx.ConnTime())
	fmt.Fprintf(ctx, "Request has been started at %s\n", ctx.Time())
	fmt.Fprintf(ctx, "Serial request number for the current connection is %d\n", ctx.ConnRequestNum())
	fmt.Fprintf(ctx, "Your ip is %q\n\n", ctx.RemoteIP())
	ctx.SetContentType("text/plain; charset=utf8")
}

func main() {
	addr := "127.0.0.1:8000"
	log.Printf("Starting server on %s", addr)
	if err := fasthttp.ListenAndServe(addr, requestHandler); err != nil {
		log.Fatalf("Error in ListenAndServe: %s", err)
	}
}
