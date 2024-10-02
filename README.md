## Hands-on Kubernetes: Deploying Python Flask application with Pods, Deployments and Services
The code repository for our follow-along article, catch my sub-stack [article here](http://google.com)! 

### Getting started
- You need to download Docker and Python for this tutorial

#### Docker folder
Contains the files used to build our Docker Image.
- Dockerfile - commands used to build Docker image
- main.py - Our Python Flask application
- requirements.txt - Generated from pip, used by Dockerfile for dependencies installation

#### Kubernetes Deployment folders
- Deployment - Contains the deployment.yaml to deploy our Kubernetes Deployment
- Service - Contains the service.yaml to deploy our Kubernetes Service (NodePort)

Happy deploying! Please raise any issues and I'll attend to it and fix the code!