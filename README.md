<h1 align="center">Dockerized Product REST API</h1>

<div align="center">

![Python version](https://img.shields.io/badge/python-3.8+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

A small simple REST API for products management. 

## Table of contents

1. [Introduction](#introduction)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Next](#next)


## Introduction

This REST API is an experimental project for products management.

The REST API provides the below functionalities:
1) Registration of a product
2) Retrieval of product details
3) Listing all available products
4) Listing all sold out products
5) Registering quantity update

At the moment tests run before starting the Flask application.

## Installation

1. Install Docker Desktop
2. Clone the repository

## Usage

After downloading the repository open a terminal and run the following command:

```bash
docker-compose up --build
```

If any code changes occur then rebuild Docker images using the below command:

```bash
docker-compose up --force-recreate --build flask-app
```

## Next
- adding more tests
- generating interactive documentation (with Swagger UI) 
