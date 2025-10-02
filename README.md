Section 1: Core Concepts
__Q1.1 – Free Answer Points__
What is a Docker container and how is it different from a virtual machine?

Docker containers are a basic unit of software used for packiging application code and its libraries and dependencies, making it easy to run it in any environment. Containers abstractize at the OS level, and they share the same kernel with their host, unlike virtual machines which have individual operationg systems.
Given the previous statement, containers are more lightweight, start faster, and are less resource-intensive than virtual machines.

Both containers and virtual machines can be powerful tools when used in the correct context. If you need to run a heavy workload, legacy application or are desire strong isolation - virtual machines are the answear. If you need to deploy microservices in a CI/CD environment and want portability and scalability - containers are the way to go.

__Q1.2 – Multiple Choice Points__
Match the Docker command to its function:

```docker build``` ---> build image for Dockerfile


```docker ps```    ---> show running containers


```docker run```   ---> run a container


__Q1.3 – Free Answer Points__
Name three reasons why Docker is useful in modern DevOps pipelines.

1. Docker ensures that the same code can be used and adapted for multiple enviroments. The same containers can be run and deployed in the same way in development, testing and production environments, improving collaboration and reducing environment-related issues. Therefore, the same CI/CD pipelines can be used for all environments, the isolation between resources being assured by the containers.
   
2. Docker facilitates the CI/CD process - images can be built and tested during the CI, and then deployed during the CD.
   
3. Docker speeds up the pipeline run time by using caching of the image levels; if nothing changes in the image layer then those layeres are cached, thus reducing build and deployment times.

4. Docker allows isolation of the containers, and this integrates well with the microservices achitecture, making the deployment process separate for each microservice.

__Q1.4 – Multiple Choice Points__
Identify whether the following statements are True or False:
1. Docker images are mutable. ---> __**FALSE**_
Docker images are not mutable, once they are created they are **immutable**, they can't be modified after creation. If there is any code change at the image level, it needs to be recreated.

2. Containers can communicate over user-defined networks. __**TRUE**__
Yes, Docker containers use the bridge network for communicating, but the option of them communicating over user-defined networks still exists - this is the case for Docker Compose.

3. The CMD instruction in Dockerfile overrides ENTRYPOINT. __**FALSE**__

CMD does *NOT* ovveride ENTRYPOINT; if provides default arguments to ENTRYPOINT.

__Q1.5 – Free Answer Points__
What is the difference between a bind mount and a named volume in Docker?
Docker containers are stateless by default, but we use the following storage options to make them persisstent after restart:
- bind mounds: used mainly during the development process for maping a local path on the docker container.
- named volumes: used in production grade environments, this is a Docker native solution that uses external storage that can be shared across multiple containers.

__**Section 2: Dockerfile and Image Building**__
__Q2.1 – Coding Points__
Given a Python app with app.py and requirements.txt, write a basic Dockerfile to build and run it.

The Dockerfile used for this section can be found in **q2.1/**, but also bellow:

```
FROM python:3.12

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

```

Steps to reproduce:

- First run the following command in the root of **q2.1/** in order to build the Docker image:
```
docker build -t flask-docker-app .
docker images
```

<img width="567" height="46" alt="image" src="https://github.com/user-attachments/assets/4630e025-6321-42d0-84e9-97ed8e25f708" />

- Then run the Docker container:
```
docker run -p 8090:5000 --name flask-container-q21 flask-docker-app
docker ps
```

<img width="855" height="168" alt="image" src="https://github.com/user-attachments/assets/1c4d31f4-a326-4dfd-a214-194eac37f7a9" />

<img width="1074" height="54" alt="image" src="https://github.com/user-attachments/assets/441f0f68-e679-4eea-8726-e3c8444de513" />

Now the application is running on port 5000 on the container, and port 8090 on localhost, so we can access it like so:

<img width="543" height="192" alt="image" src="https://github.com/user-attachments/assets/b3cbdac1-4368-4a70-96e4-88f1da267c9d" />



__Q2.2 – Coding Points__
Modify the above Dockerfile to use a multi-stage build with no pip/build tools in final image.
The Dockerfile used for this section can be found in **q2.2/** or bellow:

```
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]


```

Steps to reproduce:

- First run the following command in the root of **q2.2/** in order to build the Docker image:
```
docker build -t multi-stage .
docker images
```

<img width="517" height="58" alt="image" src="https://github.com/user-attachments/assets/604b5e48-9870-4a6e-8eec-15cfd2fcf88c" />

- Then run the Docker container:
```
docker run -p 8090:5000 multi-stage
docker ps
```
<img width="859" height="157" alt="image" src="https://github.com/user-attachments/assets/e1eab827-e161-4024-8bfa-c84f04530a39" />


<img width="1021" height="52" alt="image" src="https://github.com/user-attachments/assets/46e34834-592d-444a-92eb-25148c59c99f" />


<img width="460" height="207" alt="image" src="https://github.com/user-attachments/assets/285bedf1-6e83-4eca-9e16-b65e6b982185" />


__Q2.3 – Free Answer Points__
Explain how Docker layer caching works and how it helps with CI/CD pipelines.

In Docker, every instruction in a Dockerfile (such as ```FROM```, ```RUN```, ```COPY```, ```CMD```) creates a new image layer. Docker caches these layers locally, so if a change is detected at the layer level then the layer and all its subsequent onds get recreated, if nothing changes the already existing cache is used. Therefore, a best practice is to maintain the same command order between image builds, as to avoid interfering with the cache layers.

In the context of CI/CD pipelines, the caching mechanism is especially useful in improving pipeline execution time and in reducing the amount of used resources. For example, dependencies installed early in the Dockerfile (e.g., ```pip install``` or ```apt-get install```) can be cached across builds if source code changes occur later in the file.

__**Section 3: Docker Networking, Volumes, and Compose**__
__Q3.1 – Coding Points__
Write a docker-compose.yml file for a Python web app and a Redis container.

```
version: "3.9"

services:
  web:
    build: .
    container_name: flask-app
    ports:
      - "8090:5000"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    restart: always

  redis:
    image: redis:7-alpine
    container_name: redis-server
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: always

volumes:
  redis_data:
```
The code for this module can be found in the root of **q3.1/* or above.

Steps to recreate:

```
docker compose up
```
<img width="1184" height="691" alt="image" src="https://github.com/user-attachments/assets/9edaf573-86f5-4351-af22-78bf18ab2b13" />


<img width="375" height="203" alt="image" src="https://github.com/user-attachments/assets/b3411e67-0865-440c-b8bb-420abe54714c" />


__Q3.2 – Free Answer Points__
In what scenario would you use Docker Compose instead of running containers manually?

Docker Compose is useful when an application requires multiple containers that must run and work together, such as an application with a database. Instead of starting each container manually with multiple ```docker run``` commands, you can write a singular *docker-compose* file to include all of the application's containers and deploy them togheter. Moreover, Docker Compose adds all of the containers it manages under a common network which makes it easier for containers to communicate with eachother via service name.

__Q3.3 – Multiple Choice Points__
Which of the following are benefits of using volumes in Docker?
A. Data persists after container deletion
B. Can be backed up
C. Consume less memory
D. Can be shared between containers

A. B. D.

The only statement that does not match is *C*, since using container does not affect memory usage but storage persistence.

__**Section 4: Challenge**__
__Q4.1 – Hands-on Coding + Explanation Points__
You are given a Node.js app that connects to PostgreSQL. Write a docker-compose.yml and explain how to use .env for DB_USER, DB_PASS, and DB_NAME. Add suggestive comments to understand the role of each component used in docker-compose.yml

The docker compose file can be found in the root of *q4.1* of here:

```
version: "3.9"                     # Docker Compose file format version

services:
  app:                             # Service definition for the Node.js app
    build: .                       # Build image from Dockerfile in current directory
    container_name: node-app        # Name for the running container
    ports:
      - "3000:3000"                # Map host port 3000 → container port 3000 (http://localhost:3000)
    environment:                   # Environment variables passed into the container
      - DB_USER=${DB_USER}         # Database username (from .env file)
      - DB_PASS=${DB_PASS}         # Database password (from .env file)
      - DB_NAME=${DB_NAME}         # Database name (from .env file)
      - DB_HOST=db                 # Service name "db" acts as hostname inside the Compose network
      - DB_PORT=5432               # Default PostgreSQL port inside the container
    depends_on:                    # Ensure DB starts before app tries to connect
      - db
    restart: always                # Restart container if it crashes/stops unexpectedly

  db:                              # Service definition for PostgreSQL database
    image: postgres:16-alpine      # Lightweight official PostgreSQL image
    container_name: postgres-db     # Name for the running container
    environment:                   # Pass DB initialization values
      - POSTGRES_USER=${DB_USER}   # Create DB user (from .env file)
      - POSTGRES_PASSWORD=${DB_PASS} # Set user password
      - POSTGRES_DB=${DB_NAME}     # Create database with given name
    ports:
      - "5432:5432"                # Expose DB to host (optional, useful for pgAdmin/psql tools)
    volumes:                       # Persistent storage for DB data
      - pg_data:/var/lib/postgresql/data
    restart: always                # Restart DB container if it stops

volumes:
  pg_data:                         # Named volume to persist database data (lives outside container lifecycle)

```

Run the following command:

```
docker compose up
```

<img width="1221" height="259" alt="image" src="https://github.com/user-attachments/assets/39f7dda0-1d07-4901-b385-96f97eab9077" />

Access it at http://localhost:3000/ like so:

<img width="629" height="245" alt="image" src="https://github.com/user-attachments/assets/cc672def-a1ff-4c39-8955-9cb153c97636" />

Kubernetes & EKS Chapter
Total: 100 points
Assignment Type: Practical, free-answer, YAML-based, and conceptual
Initial setup:
Install minikube cluster following the documentation
Install helm
Good to have: AWS account

1. Kubernetes Core Concepts (10 points)


- Explain what a Pod is in your own words. (3 points)


A pod is the smallest deployable unit in k8s, it is a wrapper over one or multiple containers which share the same network, storage and configuration. Pods are ephemeral by nature and are usally managed by Deployments.

- What is the role of the kubelet on a worker node? (2 points)
Kubelet is an agent running on every single worker node in a k8s cluster. It facilitates communication with the control plane (mainly the API Server) and ensures that containers described in PodSpecs are running and healthy. The kubelet interacts with the container runtime (such as containerd, Docker) to start, stop and monitor containers to match the desired state.

- List 3 main components of the Kubernetes control plane and their purpose. (5 points)
  
 The control plane can be refered to as the "brain of the k8s cluster". It encapsulates the following components:
 - The API Server -> it is the gateway to the k8s cluster and facilitates the communication between its components; every service trying to access the cluster goes to the API Server. A relevant example for this would be using the ```kubectl``` command, which communicates with the API Server in order to get the state of the cluster's resources.
 - controller manager -> it monitors the state of the cluster and ensures that the current state matches the desired state kept by the configuration files, for example it ensures that the desired number of replicas from a deployment are running.
 - scheduler -> it assigns the newly created pods to the worker nodes based on available resources, taints and tollerations, affinitty/anti-affinitty rules.
 - etcd -> it is a distributed key-value store that keeps the state of the cluster; it is considered the source of truth of the k8s cluster. For interacting with it ```etcdl``` command is used.
   
3. Working with Pods and Deployments (20 points)

- Create a Deployment YAML that launches 3 replicas of an NGINX container. Include ports and labels. (10 points)

The manifest for the deployment can be found in the root of the *k8s_section2* or here:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80

```

Run ``` kubectl apply -f deployment.yaml``` in order to create it.
  
- Apply the Deployment to your local cluster and share the output of `kubectl get
deployments` and `kubectl get pods`. (5 points)

<img width="494" height="45" alt="image" src="https://github.com/user-attachments/assets/eab97a60-2461-455b-b936-f2ce39bffdd6" />


<img width="537" height="73" alt="image" src="https://github.com/user-attachments/assets/54b9f216-8664-4113-976b-8cdb582c0605" />


- Update the Deployment to use a different NGINX image tag and apply a rolling update.
Show the steps. (5 points)

<img width="879" height="139" alt="image" src="https://github.com/user-attachments/assets/0e857457-cf12-49a7-a1f4-2c0dec40157d" />

<img width="879" height="139" alt="image" src="https://github.com/user-attachments/assets/96f1c620-91db-4f94-bb54-925e60b91eaf" />

<img width="837" height="376" alt="image" src="https://github.com/user-attachments/assets/e241c315-d524-4bd9-842b-488529cfd076" />

<img width="1006" height="342" alt="image" src="https://github.com/user-attachments/assets/9dedcff1-23ef-421b-b571-e97a8b63adae" />

By changing the image of the deployment, a rolling update strategy will be triggered. The deployment will create a new replica set by creating new pods with the desired image and deleting the old ones, one by one, in order to ensure there is no downtime. This is the default deployment strategy in k8s.

5. Kubernetes Services & Networking (15 points)
- Write a Service YAML manifest that exposes your NGINX Pods using type ClusterIP. (5 points)

<img width="550" height="59" alt="image" src="https://github.com/user-attachments/assets/bef51853-a47b-435b-92a8-e24079ac9c91" />


- Explain how kube-proxy helps with service networking. (3 points)

  
Kube-proxy runs on every worker node in the cluster and makes sure that the services inside of it are accesible. Because of it, pods from the same node can be exposed togheter through one single port and ip address. Kube-proxy ensures the communication between services and pods, pods are ephemeral and if a service needs to communicate with a certain pod, if the ip address changes

- What is the role of DNS in Kubernetes networking? (2 points)
The DNS holds the name of the services to ensure communication between them and pods. A service in the default namespace can be accessed through service-name.default.svc.cluster.local.

- Bonus: Deploy a second Service using NodePort and share its exposed port and IP. (5 points)
<img width="654" height="100" alt="image" src="https://github.com/user-attachments/assets/d4cd2544-0e89-440e-9741-dbac27a02f9d" />
<img width="715" height="82" alt="image" src="https://github.com/user-attachments/assets/396bcd65-b6c4-4755-8409-0c9b7684aed7" />
<img width="901" height="343" alt="image" src="https://github.com/user-attachments/assets/84c274b3-ceca-4827-bd43-09900b0621d8" />


7. Helm Basics (10 points)
- Install Helm on your system and add the Bitnami chart repository. (2 points)
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

```
kubectl run -i --tty load-generator --image=busybox /bin/sh
# inside pod:
while true; do wget -q -O- http://nginx-service; done
```

<img width="671" height="598" alt="image" src="https://github.com/user-attachments/assets/72f38b7f-ee75-45d3-8b06-6072b466d618" />

<img width="731" height="103" alt="image" src="https://github.com/user-attachments/assets/eb3848e3-2e42-4772-bc9b-b9ffc81b0715" />

<img width="747" height="114" alt="image" src="https://github.com/user-attachments/assets/fd5aac60-5eca-438c-890e-c5021b4a034d" />


6. Monitoring & Debugging (10 points)
• - Use `kubectl describe` and `kubectl logs` to troubleshoot a failing Pod. Share your observations. (5 points)
For this use case I will create a pod with a faulty container image, in order to better observe and conduct the examination.

```
kubectl run faulty-pod --image busybox:777
```
<img width="701" height="183" alt="image" src="https://github.com/user-attachments/assets/1f5ecc3f-8710-49f5-82ee-fd134e8c5ac1" />

The pod is in state ImagePullBackOff so let's investigate:

```
kubectl get pods
kubectl describe pod faulty-pod
```
<img width="974" height="183" alt="image" src="https://github.com/user-attachments/assets/39b84bea-f676-4ccc-a6b8-7d5f89753392" />

```
kubectl logs faulty-pod
```

<img width="924" height="31" alt="image" src="https://github.com/user-attachments/assets/f82b874c-08b1-455f-b9e2-9f1710583962" />

Image pull issues (ImagePullBackOff) occur when the image name or tag is wrong; fix by correcting the image in the Deployment.

Use

```
kubectl edit pod faulty-pod

```
to fix the name of the image.

• - List 3 common reasons why a Pod might be in CrashLoopBackOff and how to fix them. (5 points)

- if the pod uses too many resources and exceeds the CPU/memory limit it gets killed by the kubelet agent
- application crashes at startup due to an error in the container's main process, scrip/command/entrypoint error
- environment variables are configured incorrectly


8. EKS and IAM Integration (15 points)
• - Explain the difference between managed node groups and Fargate profiles in EKS. (5 points)
• - Create an IAM role and associate it with a Kubernetes Service Account using IRSA (IAM Roles for Service Accounts). Share the steps. (10 points)

9. Challenge (10 points)
• - Deploy a 2-tier app using Helm charts: backend (Redis) and frontend (web app). Ensure Services connect the two.
• - Include Service YAMLs, any custom values.yaml overrides, and a short explanation of how traffic flows through the system.
