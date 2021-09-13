# ping_monitoring
Trace ICMP packets to the host and use it with your monitoring service.

# Get Started
## Host Based

After cloning the project, use command below to install dependencies.
> pipenv install

Then use the shell subcommand to activate virtualenv.
> pipenv shell

In order to run the code use:
> python3 pinging.py --host {hostname} --duration {duration}

you can use more command line options defined in section [CommandLine](#commandline)

## Container Based
After cloning the project, use docker-compose to build and run the project
> docker-compose build
> docker-compose up -d

to test the functionality of the project you can curl one of endpoints

### health endpoint
> curl -XGET {FLASK_HOST}:{FLASK_PORT}/health

### ping endpoint
> curl -XPOST {FLASK_HOST}:{FLASK_PORT}/ping -H "Content-Type: application/json" -d '{"host": "1.1.1.1", "duration": "10s"}'

duration could be one of
* h (hour) -> `1h`
* m (minute) -> `10m`
* s (second) -> `30s`

## CommandLine

**--host**

define the hostname or ip you want to ping from.

**-d / --duration**

the duration of pinging the host.

**--real-time**

disabled by default. use it if you want the plotter to plot in realtime.

**--save-file**

disabled by default. save the output of file in a name you define or the script's default name "Pinging {host}.txt"

**-o / --output**

use this option if you enabled "--save-file" and you want a custom name for the output file.

TODO
---
- [x] dependency management
- define interface to work with monitoring tools
- write unit tests
- [x] add Dockerfile
- add ci pipelines
- add flake8 pipeline
