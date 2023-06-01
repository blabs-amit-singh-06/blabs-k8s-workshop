# blabs-k8s-workshop
# install Dependency
 Docker , GIT
# run
## Build Image
  docker build -t blabs-k8s-workshop .
## Run the Image
    docker run -p 5000:5000 blabs-k8s-workshop 
<p>once the docker image is up and exposed to 5000 port. access the /health and /ping end point on localhost,http://127.0.0.1:5000/health,http://127.0.0.1:5000/ping,</p>

## step 2: optional
   install minikube for the k8s
   minikube start
   minikube dashboard  (to get the ui of dash board)
   minikube stop

## step 2: continued
### load image on minikube 
  minikube image load blabs-health-k8s-workshop
  minikube image load "docker image name


## the kubernates initial setup
### step 1: deployment
      kubectl apply -f deployment.yaml 
      kubectl get deployments
      kubectl get pods
      kubectl describe pod "pod name"      
      kubectl delete -n default deployment k8s-workshop   ** for deleting deployment

###step 2: attach a service to the pods 
####     ClusterIP:-if we use this service then we have to do port forwarding
       kubectl apply -f cluster_service/service.yaml  ** deploy a service
       kubectl get services  or  kubectl get svc
       kubectl port-forward service/k8s-workshop-clusterip 9080:5000

####      NodePort : it is directly exposing the pods to real world( not considered safe)
     kubectl apply -f node/service.yaml  ** deploy a service
     kubectl get services  or  kubectl get svc

####      loadbalancer: it is used to expose the pods to public domain
     kubectl apply -f loadbalancer/service.yaml  ** deploy a service

## ingress:-Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.


###       ADD Ingress to minikube
       minikube addons enable ingress


####       adding a host name for the minikube ip
       minikube ip                  **copy the ip
       sudo  nano /etc/hosts        ** add the minikube ip and then assign a host name example:192.168.49.2    myapp.info


###       create a ingress_eample.yaml
###       define the host that was added to the hosts and define all the services with path and port
       kubectl apply -f ingress/ingress_file.yaml

## kubectl get deployments

## kubectl get pods

## kubectl get services

## kubectl get ingress

## to delete all stuff of kubernates
 kubectl delete daemonsets,replicasets,services,deployments,pods,rc,ingress --all --all-namespaces




