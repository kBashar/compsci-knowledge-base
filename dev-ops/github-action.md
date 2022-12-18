Github Actions is a CI/CD platform. Full software development life cycle can be managed using github actions.

To understand this tool let's go through an example implementation. All releated concepts will be described along the way. 

We have a tiny hello world python project. It has a main.py file and a README.md file. The python script takes a name as input and print out `hello <name>` and the  README file has this tutorial. All codes are [here](https://github.com/kBashar/github-action).

Github Actions has following components.
1. Workflow
2. Events
3. Jobs
4. Runner
5. Actions

Workflows    
    -> defines operations to run when an event related to the repository is triggered, also it describes the computing platform to execute those operations.
    -> Workflows are *yml* file residing in *.github/workflows* path of a repository.
  
    -> Example of events, [push, pull]. [All supported events](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).  

Workflow has jobs  
    -> Jobs define steps to run  
    -> Steps are described using *actions* and/or *shell* command  
    -> Jobs run on a *runner*  

A Runner is a virtual computing platform  
    -> github Supports Linux(Ubuntu), MacOs, Windows  
    -> Users can define their own runner  

Actions are predefiend  
    -> its a package that can accomplish a single task   


Project Goal

Write and Implement a workflow that runs in an event of *[push]* in master branch and build an exe and upload as a release. 

* It's a python project

Our workflow should run whenever there is new tags pushed  

**on**  
```yml
on:
  push:
    tags:
      - '*'  
```  

**Job specification**  
Multiple jobs can run in a single workflow. But every job gets a virtual computing platform aka runner.  

```yml
    jobs:
      build-release-exe: 
        runs-on: windows-latest
```  
A job need an unique `job-id` among the workflow jobs and `runs-on` pointing to the runner platform.

**Job steps**  
1. Checkout the repository using a github actions  
```yml
    steps:
      - name: Repo-Checkout
        uses: actions/checkout@v3
```
1. Our project is coded in python, it's time to install Python. We use the official github action of version 4 ( `actions/setup-python@v4` ) to install Python. There is a new key `with` here, this is used to provide Input parameters to the action. In our case there are 3 such input parameters, all of them are optionals and github has ways to resolve the values in case no input is provided. We are writing them to make our build environment predictable and matching with the development enevironment. 
```yml
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        cache: 'pip'
        architecture: 'x64'
```  
1. Project dependencies are to be isntalled. 
```yml
    - name: Install Requirement
      run: pip install -r requirements.txt
```  
1. Now build the exe using PyInstaller. 
```yml
    - name: Build exe
      run: PyInstaller --onefile main.py
```
1. Our exe is ready to release. We create a release in Github and upload the exe as an artifact of the release. Till now we have used `actions` provided by Github. This time we will use a community made actions, [ncipollo/release-action](https://github.com/ncipollo/release-action).
Here build artifact is the exe generated in previous step. This action will add latest pushed tag to the release. 
```yml
    - name: Create Release
      uses: ncipollo/release-action@v1
      with:
        artifacts: 'dist/main.exe'
        artifactContentType: application/zip
        removeArtifacts: true
``` 
