## Knowledge Base  
1. Topic levels are spearated with a froward slash `/`  
2. Example: factory/floor1/machine23/frequency  
    Hierarchical topic organisation. 

3. Topics can be subscribe using wildcards. There are two wildcards.  

    #### a. Single Level Selection `+` :  
    Let's assume we have a client that subscribes to frequency of all machines of a floor. In that case Subscribing topic will be `/factory/floor1/*/frequency`

    Nice thing about this is, newly added device will automatically send data to interested destinations. 

    #### b. Multi Level Selection `#` :  
    Wildcard # should be the ending chracter of a topic string following a forward slash `/`.  

    Example: `factory/floor1/#`  

    A client that subscribes to above topic, it will receive messages from all topics that start with *factory/floor1/*.   

    When a client subscribes to a topic with a multi-level wildcard, it receives all messages of a topic that begins with the pattern before the wildcard character, no matter how long or deep the topic is. 