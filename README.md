# charliebell.de
This project hosts the portfolio website 'charliebell.de'. It uses a CI/CD pipeline, with the goal being to create a scalable website which can be reliably updated with high availability. The tech stack can be split as such:
<br><br>
Front-end: Bootstrap 5, HTML5, Django (Python).
<br><br>
Back-end: Docker, Kubernetes, GitHub Actions, Digital Ocean.
<br><br>
The CI/CD pipeline runs in GitHub Actions as follows:
1. The user pushes changes to the main branch via git.
2. Testing is performed on the changes in GitHub Actions.
3. A new build is constructed using new Docker container image is built.
4. The Docker image is pushed to a DigitalOcean repository.
5. Kubernetes is provisioned and pulls the Docker image.
6. The Kubernetes deployment image is updated from the Docker image in rollout.

The use of Docker and Kubernetes for the site is to allow for future scalability, builds, and online rollouts which are automated by GitHub Actions.
The advantage of using Kubernetes is that rollouts of new deployments can be implemented with zero downtime due to the multiple pods. The pipeline also demonstrates a solid foundation for a scalable high-traffic website. For example, although the load balancer used here has only one node, it allows for the nodes to be scaled out as necessary to accomodate further traffic. If this were an e-commerce website, web traffic could be plenty and nodes can easily be created to accomodate the high traffic.
<br><br>