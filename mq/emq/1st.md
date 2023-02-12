Reasons to choose EMQ  
1. Native MQTT
2. Corporate Support if needed
3. MQTT full support
4. Cloud Integration 
5. Integration with other MQTT brokers


Docker install:
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx:latest

default login:  
    username: admin  
    password: public  

another user:
    username: user1
    password: Akashpata1

A great problem of starting EMQX from docker commandline is that, configuration and data don't persist between sessions. To solve this we need to use volumes for persisting data. Docmentation is here. [link](https://github.com/emqx/emqx-docker#persistence)
