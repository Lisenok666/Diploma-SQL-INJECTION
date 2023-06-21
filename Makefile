IMAGE:=aaa-frontend

help:
	@echo "help - show this help"
	@echo "run - start application"
	@echo "dev - start application in dev mode with live reload"
	@echo "build - build docker image"


build:
	@docker build -t ${IMAGE} .

dev:
	@docker run -v $(PWD):/app \
		-p 0.0.0.0:8000:8000 \
		-p 0.0.0.0:8001:8001 \
		-it ${IMAGE} \
		adev runserver --livereload --host 0.0.0.0 --port 8000 run.py

run:
	@docker run -it -p 0.0.0.0:8000:8000 ${IMAGE}
