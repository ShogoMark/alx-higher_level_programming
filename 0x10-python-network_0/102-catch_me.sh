#!/bin/bash
#A script that makes a request, responds with a string
curl -X GET 0.0.0.0:5000/catch_me -d "You got me!"
