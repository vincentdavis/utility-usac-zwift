#!/bin/sh

docker build -t utility:prd -f Dockerfile .
if [ `echo $?` == 0 ]; then
	docker rm -f utility
	docker run -dt --restart=always -p 8009:8009 --name utility utility:prd
fi