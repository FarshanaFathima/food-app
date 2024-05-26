<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--     <title>FastAPI and Kafka Dockerized Project</title> -->
</head>
<body>

<h1>FastAPI and Kafka Dockerized Project</h1>

<h2>Introduction</h2>
<p>This project is a demonstration of using FastAPI for building APIs, Kafka for messaging, and Docker for containerization. It aims to showcase my learning journey in integrating these technologies to build a simple yet effective application.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
</ul>

<h2 id="project-overview">Project Overview</h2>
<p>The main goal of this project is to create a basic application that leverages the power of FastAPI for handling HTTP requests, Kafka for message brokering, and Docker for containerization. This setup is particularly useful for building scalable and maintainable microservices.</p>

<h2 id="technologies-used">Technologies Used</h2>
<ul>
    <li><strong>FastAPI</strong>: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.</li>
    <li><strong>Apache Kafka</strong>: A distributed event streaming platform capable of handling trillions of events a day.</li>
    <li><strong>Docker</strong>: A set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.</li>
</ul>


<h2 id="project-structure">Project Structure</h2>
<pre><code>fastapi-kafka-docker/
├── api
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yaml
├── email-backend
│   ├── Dockerfile
│   ├── email-backend.py
│   └── requirements.txt
├── kafka-food-delivery
│   ├── kafka-docker-compose.yaml
│   ├── kafka_server_jaas.conf
│   ├── login.properties
│   └── run_workaround.sh
├── mongo_container
│   ├── docker-compose.yaml
│   └── mongo-dat
├── order_backend
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
└── transaction
    ├── Dockerfile
    ├── requirements.txt
    └── transaction.py
<ul>
    <li><code>app/main.py</code>: The main entry point of the FastAPI application.</li>
    <li><code>app/models.py</code>: Contains the database models.</li>
    <li><code>app/schemas.py</code>: Defines the request and response schemas.</li>
    <li><code>app/kafka_producer.py</code>: Handles Kafka message production.</li>
</ul>


<h2 id="acknowledgements">Acknowledgements</h2>
<p>Thanks to the FastAPI and Kafka communities for their excellent documentation and support.</p>

</body>
</html>
