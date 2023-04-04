#!/bin/bash
# Display all allowed HTTP methods on a given URL server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-