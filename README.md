# taiphuong_applied_position_technical_assessment
Tai Phuong's Technical Assessment

### 1. Choice of Framework & Library:
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. (https://fastapi.tiangolo.com/)
#### a. What are the benefits & drawbacks associated with that choice?
<b>Benefits</b>: 
- I've chosen that because it quite fast and easy to implementing.
- with external  libraries for serializering objects, migration database, ORM, we can work that independently, very flexible, capitable for switch relation database with no-relation database if necessary.
- Use asynchronous programming for optimizing the bunch of work.
- Generate well documentation for any sides.

<b>Drawbacks</b>: something not perfect like Django Rest Framework, not easy to get related data when we use many to many relation. I need more time for building that.


#### b. What are the assumptions underlying that choice?

FastAPI will adapt to scalable any project from small, we can start with anything small, and scale it by adding multiple services under microservices architecture

### 2. Potential Improvement

- I will take time for working with serializing and deserializing with multiple objects as many to many. You can see it with `working_hours`. I did my code as manually for achieving result
- Authorization and authentication
- Structure code for adding new layer for business logic

### 3. Production consideration:
- Working perfect with migration using alembic, fix anny issues we have, very dangerous if we can not handle of changes of data and structures
- FastAPI quite good for production, help we reduce more steps for production.

### 4. Assumptions

- I assumed that system have a lot of doctors working with specific working hours, address, and consultation fee.
- I design an API create a doctor with their working hours, if have time I will design a filter can choose a day like(Monday), and choose the time like (8:00 -> 17:00)


------------
### 5. Installation:

#### 1. Docker
Requisition:
- Docker
- Docker compose


At a current folder, place a docker_compose.yml

Run a command for building a container:

```
$ docker-compose build

```
Run a container
```
$ docker-compose up -d
```
> When you run `docker-compose up -d` (run a server), database will create and migrate. 

When we have any changes in models, run a command follow below.
```
$ docker-compose exec api alembic revision --autogenerate "Alter a column" #create versions file for mark a changing

$ docker-compose exec api alembic upgrade head  # Execute the changes.
```
To check the logs, run:
```
docker-compose logs
```
Navigate to http://localhost:9000/docs for viewing API documents


#### 3. Without docker
Requisition:
- Any virtual environment (conda, python venv) (https://docs.python.org/3/library/venv.html)
- Pip installation (https://pip.pypa.io/en/stable/installation/)

Creating a virtual environment

```
python3 -m venv /path/to/venv
```

Activate your virtual environment
```
source [/path/to/venv]/bin/activate
```
Install libraries from requirements.txt
> please make sure pip3 installed, come back to Requisition.
```
(venv) $ pip3 install -r requirements.txt
```
Migrate database with alembic

```
python3 backend_pre_start.py
alembic upgrade head
```

Run a server
```
uvicorn main:app --host 0.0.0.0 --port 9000
```
Navigate to http://localhost:9000/docs for viewing API documents


![This is an image](./apidocs.png)

