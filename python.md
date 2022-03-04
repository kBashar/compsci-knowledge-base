# Python

## __pipenv vs pip__
### __pipenv__
* Manages both the virtual environment and packages
* Has provision for installing separate packages for development and production.
* Creates Pipfile, Pipfile.lock to list the installed packages and related dependence list. Great thing about this is it's interoperable with requirements.txt format.
* <code>pipenv graph</code> command prints out the dependency graph. 
#### 

## logging 

* logging module is available at __logging__
* logging has 5 severity level.  
    | Level       | Value       |
    | ----------- | ----------- |
    | Debug       | 10          |
    | Info        | 20          |
    | Warning     | 30(Default) | 
    | Error       | 40          |
    | Crtical     | 50          |
* logging has a basicconfig() method that helps to configure the logger for basic usage. A logging config initiated in any module will have effect on all other modules linked with it. So if in a project the main file intiates the logging using <code>logging.basicconfig()</code>, the same logger can be accessed in all other modules/file through out the project.
* basicconfig() takes several arguments, follwoing are the important ones.
  * filename, where the logs are to be written. 
  * format, this is % style string that provides provision for formating the log message. supported attributes [here](https://docs.python.org/3/library/logging.html#logrecord-attributes)

    ```python
    import logging

    logging.basicConfig
    (
        filename="example.log",     
        encoding="utf-8", 
        datefmt='%d/%m/%Y %I:%M:%S %p',
        format='%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s', 
        level=logging.DEBUG
    )
    ```