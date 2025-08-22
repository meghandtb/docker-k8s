1. Docker container versus Virtual Machine:

Containerele docker sunt utilizate pentru impachetarea aplicatiilor cu dependindetele de care are nevoie pentru a rula aplicatia pe orice environment.
Containerele fac abstractizare la nivel de OS, impart acelasi kernel cu hostul pe care se afla, spre deosebire de masinile virtuale care au fiecare un sistem de operare individual.
Containele sunt mai usoare, mai lightweight ceea ce inseamna ca pornesc mai repede decat masinile vrtuale si utilizeaza mai putine resurse.

2.
docker build -> build image from Dockerfile
docker ps -> show running containers
docker run -> run a container

Docker images are mutable -> Imaginile de Docker nu sunt mutable, sunt imutable odata ce sunt create. Nu mai pot fi modificate dupa creare, daca e ceva de adaugat trebuie recreata imaginea.
Containers can communicate over user-defined networks -> da in general in Docker se foloseste bridge networkul dar exista si optiunea ca containerele de Dokcer sa comunice prin user-defined networks asta e cazul util pentru docker compose.
The CMS instructions in Dockerfile overrides ENTRYPOINT.

Diferenta dintre un bind mount and a named volume in Docker:

containerel de docker sunt stateless by default, daca vrem sa fie persistente la restart trebuie sa persistam storage-ul in 2 feluri:
bind mounds: folosit pentru development, mapeaza o cale de pe masina locala pe containerul de docker.
named volumes sunt oferite de docker, sunt externe containerului.

