#!/bin/sh
Xvfb :99 -screen 0 1024x768x16 &
cd $WEBOTS_HOME/resources/web/server
./server.sh start
while true; do sleep 1000; done
