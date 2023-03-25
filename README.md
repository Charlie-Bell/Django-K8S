# charliebell.de
This repository hosts my portfolio website 'charliebell.de'. It uses a CI/CD pipeline, with the goal being to create a scalable website which can be reliably updated with high availability. The tech stack can be split as such:
<br><br>
Front-end: Bootstrap 5, HTML5, Django.
<br><br>
Back-end: Docker, Kubernetes, GitHub Actions, Digital Ocean.
<br><br>
The CI/CD pipeline runs in GitHub Actions as follows:
1. The developer pushes changes to the main branch via git.
2. Integrations tests are automatically performed in GitHub Actions.
3. A new Docker container image is built.
4. The Docker image is pushed to a DigitalOcean repository.
5. Kubernetes is provisioned and pulls the Docker image.
6. The Kubernetes deployment image is updated from the Docker image in rollout.

The website demonstrates a CD/CD pipeline ready for production, this is thanks to the backend stack.
Each technology was selected for a reason:
 - Django - This allows for easy front and backend setup using a unified coding language Python.
 - Bootstrap 5 - Nice learning curve and felxibility with great resources.
 - HTML5 - Essential for any web application.
 - Docker - Quick containerization providing high portability to the web.
 - Kubernetes - High availability and scalability due to the cluster and pod configurations.
 - GitHub Actions - Automated integration tests and CI/CD pipeline with all the technologies.
 - Digital Ocean - Cheap web hosting and simple to use Kubernetes management interface, native Docker contianer registry, and AWS S3 Bucket.

The use of Docker and Kubernetes allows easy future scalability, quick builds, and online rollouts which are automated by GitHub Actions. The advantage of using Kubernetes is that rollouts of new deployments can be implemented with zero downtime due to the multiple pods. The pipeline also demonstrates a solid foundation for a scalable high-traffic website. For example, although the load balancer used here has only one node, it allows for the nodes to be scaled out as necessary to accomodate further traffic. If this were an e-commerce website, web traffic could be plenty and nodes can easily be created to accomodate the high traffic.
<br><br>
<b>Overall this CI/CD pipeline can easily be reused for any kind of site requiring high scalability and availability under the flow of large internet traffic.</b>
