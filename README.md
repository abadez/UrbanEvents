# UrbanEvents

## Requirements (Linux)
1. Have docker and docker compose installed
- sudo apt install docker
- sudo apt install docker-compose
2. Make sure you don't have any service running on ports 5432 and 8000
- Note: By default potgresql runs on port 5432, if you have any postgresql instance running on your computer stop it: sudo service postgresql stop
3. Have Postman installed to use project API

## Run project (Linux)
1. Open a terminal in project folder in the same location as the "Dockerfile" file.
2. Run docker-compose and wait until postgresql service is listening for connections ("LOG:  database system is ready to accept connections") and then press Ctrl-C to exit: sudo docker-compose up
- Note: This is required because our project does not wait for postgresql to be running and fails to start.
3. Migrate data to postgresql: sudo docker-compose run urban_events python manage.py migrate --noinput
4. (Optional) Run django test to check if service is running ok: sudo docker-compose run urban_events python manage.py test
4. Run again docker-compose (now the database is already populated) to start project service: sudo docker-compose up -d

## Use Postman to test project (Linux)

1. Open Postman GUI and import the postman collection "UrbanEventsPostmanCollection.postman_collection.json".
2. Run the collection to run the several requests to the project API.

## Default users to use in API
1. By default the migration command creates one admin user with credentials "admin:admin" and two users with credentials "user:user" and "user2:user2".
- The admins are allowed to update and delete events
- The users can create and get event details

## API
### Events

Get all events and create new events.

#### Suported methods
Method | Url | Description |
-------|-----|-------------|
GET | /events_api/events/ | Return all events
POST | /events_api/events/ | Create an event

#### Request / Response
##### GET

- Get all events.

###### Request
```json
GET /events_api/events/
```
###### Response
Attribute | Description |
----------| ------------|
id | Event id
description | Event description
lat | Location latitude
lon | Location longitude
author | User id that created the event
creation_date | Event creation date
modify_date | Event modify date
state | Event state
category | Event category

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
[
    {
	"id": 1,
	"description": "Event at Aveiro",
	"lat": 40.64427,
	"lon": -8.64554,
	"author": 3,
	"creation_date": "2020-02-01T18:33:16.432100Z",
	"modify_date": "2020-02-01T18:33:16.432111Z",
	"state": 0,
	"category": 4
    }
]
```
##### POST

- Create an event.

###### Request
Attribute | Type | Description |
----------|------|-------------|
description | String | Event description
lat | Float | Location latitude
lon | Float | Location longitude
category | Integer | Event category

```json
POST /events_api/events/
---------------------------
{
    "description": "Event at Aveiro",
    "lat": 40.6442700,
    "lon": -8.6455400,
    "category": 4
}
```
###### Response
```json
HTTP/1.1 201 Created
Content-Type: application/json;charset=UTF-8
{
    "id": 1,
    "description": "Event at Aveiro",
    "lat": 40.64427,
    "lon": -8.64554,
    "author": 3,
    "creation_date": "2020-02-01T18:33:16.432100Z",
    "modify_date": "2020-02-01T18:33:16.432111Z",
    "state": 0,
    "category": 4
}
```

### Event Detail

Get, update and delete an event.

#### Suported methods
Method | Url | Description |
-------|-----|-------------|
GET | /events_api/events/id/ | Return an event
PUT | /events_api/events/id/ | Update an event
DELETE | /events_api/events/id/ | Delete an event

#### Request / Response
##### GET

- Get an event.

###### Request
```json
GET /events_api/events/1/
```
###### Response
Attribute | Description |
----------| ------------|
id | Event id
description | Event description
lat | Location latitude
lon | Location longitude
author | User id that created the event
creation_date | Event creation date
modify_date | Event modify date
state | Event state
category | Event category

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
    "id": 1,
    "description": "Event at Aveiro",
    "lat": 40.64427,
    "lon": -8.64554,
    "author": 3,
    "creation_date": "2020-02-01T18:33:16.432100Z",
    "modify_date": "2020-02-01T18:33:16.432111Z",
    "state": 0,
    "category": 4
}
```
##### PUT

- Update an event.

###### Request
Attribute | Type | Description |
----------|------|-------------|
state | Integer| Event state

```json
PUT /events_api/events/1/
----------------------------
{
    "state": 1
}
```
###### Response
```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
    "id": 1,
    "description": "Event at Aveiro",
    "lat": 40.64427,
    "lon": -8.64554,
    "author": 3,
    "creation_date": "2020-02-01T18:33:16.432100Z",
    "modify_date": "2020-02-01T18:33:16.432111Z",
    "state": 1,
    "category": 4
}
```
##### DELETE

- Delete an event.

###### Request
```json
DELETE /events_api/events/1/
```
###### Response
```json
HTTP/1.1 204 No Content
```
