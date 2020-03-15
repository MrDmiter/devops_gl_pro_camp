# GL DevOps Pro Camp Entry Task

Small python script that can be run in Docker, that shows some metrics of the OS. Depending on the passed arguments it shows different metrics. Only two arguments are allowed: 'mem' - prints RAM metrics and 'cpu' - prints CPU metrics

## How to run?
Project is launched in three steps: clone, build, run. You must have docker and git installed on your computer. 

### Clone

Clone project from github. 
```bash
git clone https://github.com/MrDmiter/devops_gl_pro_camp.git
```
In command line move to the folder with cloned project.
### Build
Perform the following  command in order to create docker image. Instead [image_name] choose any name you want.
```powershell
docker build -t [image_name] .
```
### Run
Run created image performing next command. As [argument] pass 'mem' in case you want to see memory metrics or 'cpu' in case you want to see cpu metrics. 
```powershell
docker run --rm [image_name] [argument]
```
## Author

**Dmitriy Terentyev** - ter.dmi.ol@gmail.com