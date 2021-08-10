# Ragnarok Client
Ragnarok is an open source security framework for analysing vulnerability in network servers.

This repository contains the Ragnarok client, as well as an ephemeral form of the Diffie-Hellman key exchange. 
The client folder contains all the components nessecary for building the architecture

# Setup
This repo contains multiple inter-linked packages.
To import them locally, follow the instructions bellow
```
pip install cryptography  
```
After importing the modules, clone the repo
To start the client run:
```
python main.py
```
To define the different arguments you can use:
* ```-d``` or ```-debug``` - for outputting debug messages in the terminal
