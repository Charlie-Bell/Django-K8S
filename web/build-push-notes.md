These commands are for manual rebuild, push, deployment. We would rather automate this with a GitHub Workflow

### Login with API Token
sudo docker login registry.digitalocean.com

### Build container image
sudo docker build -t registry.digitalocean.com/cb-k8s/django-k8s-web:latest -f Dockerfile .

### Push container image
sudo docker push registry.digitalocean.com/cb-k8s/django-k8s-web --all-tags

### Deploy Kubernetes Deployment
kubectl apply -f k8s/apps/django-k8s-web.yaml