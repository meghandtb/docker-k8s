Section 1: Core Concepts
__Q1.1 – Free Answer Points__
What is a Docker container and how is it different from a virtual machine?

Docker containers are a basic unit of software used for packiging application code and its dependencies, making it easy to run it in any environment. Containers abstractize at the OS level, and they share the same kernel with their host, unlike virtual machines which have individual operationg systems.
Containerele are more lightweight which implies a faster start and less used resources while compared to virtual machines.

__Q1.2 – Multiple Choice Points__
Match the Docker command to its function:

docker build ---> build image for Dockerfile
docker ps    ---> show running containers
docker run   ---> run a container

__Q1.3 – Free Answer Points__
Name three reasons why Docker is useful in modern DevOps pipelines.
1. Docker improves collaboration between teams and ensures consistency accross multiple environments. The same containers can be run and deployed in the same way accross multiple environments (prod and non-prod).
2. Docker facilitates the CI/CD process by allowing the build of the images to be integrated in the CI process and the download and run of the images in the CD pipelines.
3. Docker speeds up the pipeline run time by using caching of the image levels; if nothing changes in the image layer then those layeres are cached, making for a faster time.
4. Docker allows isolation of the containers, and this integrates well with the microservices achitecture, making the deployment process separate for each microservice.

__Q1.4 – Multiple Choice Points__
Identify whether the following statements are True or False:
1. Docker images are mutable. ---> __**FALSE**_
Docker images are not mutable, once they are created they are **immutable**, they can't be modified after creation. If there is any code change at the image level, it needs to be recreated.

2. Containers can communicate over user-defined networks. __**TRUE**__
Yes, generally speaking, Docker containers use the bridge networkn for communicating, but the option of them communicating over user-defined networks still exists. in fact this is the case for Docker Compose.

3. The CMD instruction in Dockerfile overrides ENTRYPOINT. __**FALSE**__


__Q1.5 – Free Answer Points__
What is the difference between a bind mount and a named volume in Docker?
Docker containers are stateless by default, but we use the following storage options to make them persisstent after restart:
- bind mounds: used mainly during the development process for maping a local path on the docker container.
- named volumes: this is a Docker native solution that uses external storage that can be shared across multiple containers.

__**Section 2: Dockerfile and Image Building**__
__Q2.1 – Coding Points__
Given a Python app with app.py and requirements.txt, write a basic Dockerfile to build and run it.

The Dockerfile used for this section can be found in **q2.1/**.
Steps to reproduce:

- First run the following command in the root of **q2.1/** in order to build the Docker image:
```
docker build -t flask-docker-app .
docker images
```

<img width="567" height="46" alt="image" src="https://github.com/user-attachments/assets/4630e025-6321-42d0-84e9-97ed8e25f708" />

- Then run the Docker container:
```
docker run -p 8090:5000 flask-docker-app
docker ps
```

__Q2.2 – Coding Points__
Modify the above Dockerfile to use a multi-stage build with no pip/build tools in final image.
The Dockerfile used for this section can be found in **q2.1/**.
Steps to reproduce:

- First run the following command in the root of **q2.1/** in order to build the Docker image:
```
docker build -t multi-stage .
docker images
```
<img width="605" height="58" alt="image" src="https://github.com/user-attachments/assets/5d71dfab-2c0c-4108-a3b8-18000c1b42ce" />


- Then run the Docker container:
```
docker run -p 8090:5000 multi-stage
docker ps
```


__Q2.3 – Free Answer Points__
Explain how Docker layer caching works and how it helps with CI/CD pipelines.
for the image creation process Docker uses caching, meaning every command in a dockerfile RUN,CMD, COPY creates a layer in the cache. If a change is detected at the layer level then the layer gets recreated, if nothing changes the already exiting cache is used. Therefore, a best practice is to maintain the same command order between image builds, as to n ot mess with the cache layers.
In the context of CI/CD pipelines the layer caching helps in improving pipeline execution time and in reducing the amount of used resources.

__**Section 3: Docker Networking, Volumes, and Compose**__
__Q3.1 – Coding Points__
Write a docker-compose.yml file for a Python web app and a Redis container.

__Q3.2 – Free Answer Points__
In what scenario would you use Docker Compose instead of running containers manually?

Docker Compose is used when there multiple containers to be run and managed, this can be declared in a singular docker-compose file and deployed togheter. Otherwise, these containers need to be ran manually and handled indicidually. Moreover, Docker Compose adds all of the containers it manages unde a common network which makes it easire for containers to communicate with eachother via name.

__Q3.3 – Multiple Choice Points__
Which of the following are benefits of using volumes in Docker?
A. Data persists after container deletion
B. Can be backed up
C. Consume less memory
D. Can be shared between containers

A. B. D.

__**Section 4: Challenge**__
__Q4.1 – Hands-on Coding + Explanation Points__
You are given a Node.js app that connects to PostgreSQL. Write a docker-compose.yml and explain how to use .env for DB_USER, DB_PASS, and DB_NAME. Add suggestive comments to understand the role of each component used in docker-compose.yml


Kubernetes & EKS Chapter
Total: 100 points
Assignment Type: Practical, free-answer, YAML-based, and conceptual
Initial setup:
Install minikube cluster following the documentation
Install helm
Good to have: AWS account

1. Kubernetes Core Concepts (10 points)
• - Explain what a Pod is in your own words. (3 points)
A pod is the smallest deployable unit in k8s, it is a wrapper over one or multiple containers which share the same network, storage and configuration.

• - What is the role of the kubelet on a worker node? (2 points)
Kubelet is an agent running on every single worker node in a k8s cluster. It facilitates communication with the control plane and ensures that the pods and container state are running accordingly to the configuration file.

• - List 3 main components of the Kubernetes control plane and their purpose. (5 points)
control plane ul este creierul k8s, si are urmatoarele componente:

 The control plane can be refered to as the "brain of the k8s cluster". it encapsulates the following components:
 - The API Server -> it is the gateway to the k8s cluster and facilitates the communication between its components; every service trying to access the cluster goes to the API Server, a relevant example for thos would be using the kubectl command, which goes to the API Server in order to interogate the state of the cluster's resources.
 - controller manager -> it monitors the state of the cluster and ensures that the current state matches the desired state kept by the configuration files, for example it ensures that the desires number of replicas from a deployment are running.
 - scheduler -> it asigns the newly created pods to the worker nodes based on resources, taints&tollerations, affinitty/anti-affinitty rules.
 - etcd -> it is a distributed key-value store that keeps the state of the cluster; it is considered the source of truth of the k8s cluster, and for interacting with it one uses the etcld.
   
3. Working with Pods and Deployments (20 points)
• - Create a Deployment YAML that launches 3 replicas of an NGINX container. Include
ports and labels. (10 points)
• - Apply the Deployment to your local cluster and share the output of `kubectl get
deployments` and `kubectl get pods`. (5 points)

<img width="494" height="45" alt="image" src="https://github.com/user-attachments/assets/eab97a60-2461-455b-b936-f2ce39bffdd6" />


<img width="537" height="73" alt="image" src="https://github.com/user-attachments/assets/54b9f216-8664-4113-976b-8cdb582c0605" />


• - Update the Deployment to use a different NGINX image tag and apply a rolling update.
Show the steps. (5 points)

<img width="879" height="139" alt="image" src="https://github.com/user-attachments/assets/0e857457-cf12-49a7-a1f4-2c0dec40157d" />

<img width="879" height="139" alt="image" src="https://github.com/user-attachments/assets/96f1c620-91db-4f94-bb54-925e60b91eaf" />

<img width="837" height="376" alt="image" src="https://github.com/user-attachments/assets/e241c315-d524-4bd9-842b-488529cfd076" />

<img width="1006" height="342" alt="image" src="https://github.com/user-attachments/assets/9dedcff1-23ef-421b-b571-e97a8b63adae" />

5. Kubernetes Services & Networking (15 points)
• - Write a Service YAML manifest that exposes your NGINX Pods using type ClusterIP. (5
points)

<img width="550" height="59" alt="image" src="https://github.com/user-attachments/assets/bef51853-a47b-435b-92a8-e24079ac9c91" />


• - Explain how kube-proxy helps with service networking. (3 points)
Kube-proxy runs on every worker node in the cluster and makes sure that the services inside of it are accesible. Because of it pods from the same node can be exposed togheter through one single port and ip address. Kube-proxy ensures the communication between services and pods, pods are ephemeral and if a services needs to communicate with a certain pod, if the ip address changes

• - What is the role of DNS in Kubernetes networking? (2 points)
The DNS holds the name of the services to ensure communication between them and pods. A service in the default namespace can be accessed through service-name.default.svc.cluster.local.

• - Bonus: Deploy a second Service using NodePort and share its exposed port and IP. (5
points)
<img width="654" height="100" alt="image" src="https://github.com/user-attachments/assets/d4cd2544-0e89-440e-9741-dbac27a02f9d" />
<img width="715" height="82" alt="image" src="https://github.com/user-attachments/assets/396bcd65-b6c4-4755-8409-0c9b7684aed7" />
<img width="901" height="343" alt="image" src="https://github.com/user-attachments/assets/84c274b3-ceca-4827-bd43-09900b0621d8" />


7. Helm Basics (10 points)
• - Install Helm on your system and add the Bitnami chart repository. (2 points)
```
brew install helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm repo list
```

<img width="557" height="86" alt="image" src="https://github.com/user-attachments/assets/30655a4d-09cd-412d-a136-ab3f8be62a76" />


• - Use Helm to install an application (e.g., Apache or Redis). Share the command and
verify it was deployed. (5 points)
```
helm install my-redis bitnami/redis
```

<img width="815" height="184" alt="image" src="https://github.com/user-attachments/assets/f2acc1de-19d9-47b5-b578-b490f7bac5af" />

```
helm list
```
<img width="953" height="45" alt="image" src="https://github.com/user-attachments/assets/991155bf-a60a-4190-937a-9ee1772d6739" />

```
kubectl get pods
kubectl get svc

```
<img width="628" height="228" alt="image" src="https://github.com/user-attachments/assets/e1c0cb55-0ad6-4074-ab2e-a5236019c18f" />


• - What is the function of values.yaml in Helm? (3 points)
The values.yaml file holds the configuration for a chart, meaning the default settings used by the chart at deployment (such as image tag) resulting in a simpler deployment process. This values can be customized and overwritten to better fit the application needs.

. Horizontal Pod Autoscaler (10 points)
• - Enable the metrics-server in your cluster (minikube or EKS). Provide the command. (2 points)

For minikube run the command:

```
minikube addons enable metrics-server
```

<img width="756" height="57" alt="image" src="https://github.com/user-attachments/assets/f5c9234e-bbfa-4aad-b4df-adf0c96be06e" />

<img width="512" height="215" alt="image" src="https://github.com/user-attachments/assets/e7608845-005e-4a7c-9143-7f686e850378" />


• - Create an HPA object for the NGINX Deployment to scale between 2 and 5 replicas at 50% CPU usage. (5 points)

<img width="717" height="74" alt="image" src="https://github.com/user-attachments/assets/8ef8b70e-09a4-497b-911e-b0e057da1ef5" />

• - How can you simulate load to test if the HPA works? Explain briefly. (3 points) 

6. Monitoring & Debugging (10 points)
• - Use `kubectl describe` and `kubectl logs` to troubleshoot a failing Pod. Share your observations. (5 points)
• - List 3 common reasons why a Pod might be in CrashLoopBackOff and how to fix them. (5 points)

7. EKS and IAM Integration (15 points)
• - Explain the difference between managed node groups and Fargate profiles in EKS. (5 points)
• - Create an IAM role and associate it with a Kubernetes Service Account using IRSA (IAM Roles for Service Accounts). Share the steps. (10 points)

9. Challenge (10 points)
• - Deploy a 2-tier app using Helm charts: backend (Redis) and frontend (web app). Ensure Services connect the two.
• - Include Service YAMLs, any custom values.yaml overrides, and a short explanation of how traffic flows through the system.
