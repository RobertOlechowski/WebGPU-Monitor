docker rm -vf $(docker ps -aq)
docker image prune -a -f