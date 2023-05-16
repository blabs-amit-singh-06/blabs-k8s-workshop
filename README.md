# blabs-k8s-workshop
# install Dependency
 Docker , GIT
# run
Build Image
  docker build -t blabs-k8s-workshop .
Run the Image
    docker run -p 5000:5000 blabs-k8s-workshop
** once the docker image is up and exposed to 5000 port. access the /health and /ping end point on localhost,http://127.0.0.1:5000/health,http://127.0.0.1:5000/ping,