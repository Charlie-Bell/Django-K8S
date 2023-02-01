# charliebell.de
This project hosts the portfolio website 'charliebell.de'. It is part web development, part dev ops, reason being to create a scalable static website which can be reliably updated. The tech stack can be split as such:
<br><br>
Front-end: Bootstrap 5, HTML5, Django (Python).
<br><br>
Back-end: Docker, Kubernetes, GitHub Actions, Digital Ocean.
<br><br>
The use of Docker and Kubernetes for a static site is to allow for future scalability, builds, and online rollouts which are automated by GitHub Actions. Normally this would be overkill, but it demonstrates a solid foundation for a scalable high-traffic website. For example, a load balancer is used here for only one node, but this allows for the nodes to be scaled out as necessary to accomodate further traffic. If this were an e-commerce website, web traffic could be plenty and demand would then be high, hence this needs for easy node creation. Pods allow the website to stay functional during a rollout by sequentially updating allowing for maximum availability.
<br><br>