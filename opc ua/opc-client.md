UA Client
1. Monitors tags for changes.

2. Monitoring tags will be found in config DB.

3. On data change post the tag and value to a message queue.

4. This is an Independent process that runs under a GUI application.

5. It subscribes to the message queue for any tag scan request. and post the response data in the message queue.