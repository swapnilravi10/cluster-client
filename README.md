# Reliable Cluster API Client

## Introduction

This project implements a reliable client module for interacting with an unstable API in a cluster environment. The client ensures that group records are created and deleted across all nodes in the cluster, handling retries and rollbacks as needed.

## Assumptions and Interpretation

- The cluster consists of multiple nodes, each with the same RESTful API.
- The API is used to create and delete group records across all nodes in the cluster.
- The API is unstable and can return connection timeouts or 500 errors. In such cases, changes must be rolled back.
- The client module should ensure reliability in creating and deleting groups across all nodes, handling retries and rollbacks as needed.
- The `httpx` library is used for making HTTP requests.
- The code includes unit tests to ensure functionality.
- A Docker image is provided to run the client module.
- Basic Kubernetes manifests are included for deploying the client in a cluster.

## Prerequisites

- Python 3.8 or higher
- `httpx` library
- Docker
- Kubernetes (optional for deployment)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/swapnilravi10/cluster-client.git
    cd cluster-client
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To create a group across all nodes in the cluster:
```bash
python client.py create <groupId>
```

To delete a group across all nodes in the cluster:
```bash
python client.py delete <groupId>
```