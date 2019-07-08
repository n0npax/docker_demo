all:
	$(MAKE) fine
	$(MAKE) ugly
	echo "chop chop time"
	$(MAKE) evil

evil:
	docker inspect ugly_secret | grep LowerDir

ugly:
	docker build -f Dockerfile.ugly -t ugly_secret .

fine:
	DOCKER_BUILDKIT=1 docker build --no-cache --secret id=mysecret,src=mysecret.txt -f Dockerfile.fine -t fine_secret .
