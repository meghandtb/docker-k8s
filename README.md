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
