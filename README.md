# Docker presentation


## Tell me a secret
https://docs.docker.com/develop/develop-images/build_enhancements/

Secret was stored just in one layer. Lets check `/var/lib/docker/overlayfs2`

## Why size matters ^^
### Same app different Dockerfiles
* demo_small latest 101MB
* demo_multistage latest 62MB
* demo_basic latest 936MB
### Squashed dummy image
* demo_dd squashed 4.41MB
* demo_dd latest 88.3MB
