all: build squash

squash:
	docker build -f Dockerfile.dd --squash -t demo_dd:squashed .

build:
	docker build -f Dockerfile.dd -t demo_dd .
