# GetSqurd

Python web site to help people square up on bills after shared trips.

## Running with Docker

To build and run
```
git clone https://github.com/brabidou/GetSqurd
cd GetSqurd
docker build . --tag getsqurd
docker run -d -p 5000:5000 getsqurd
```

To stop the docker container
```
docker ps -a 
docker stop <container name>
```

To start the docker container
```
docker ps -a
docker start <container name>
```

To remove the container
```
docker ps -a 
docker stop <container name>
docker rm <container name>
```

To List all docker iamges
```
docker images
```

To Remove Docker images
```
docker images -a
docker rmi <image id>
```


## Running with VirtualEnv

Create the virtual env (Assuming venv is installed)
```
python -m virtualenv venv
source venv/bin/activate
pip install  -r requirements.txt
```

Activate the virtual
```
source venv/bin/activate
```

Deactivate
```
deactivate
```