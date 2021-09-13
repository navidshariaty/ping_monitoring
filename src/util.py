import datetime
import argparse
import os

from ping3 import ping


def parse_args():
    parser = argparse.ArgumentParser(__name__)
    parser.add_argument("--flask-host", default=os.getenv("FLASK_HOST"), type=str, dest="flask_host", help="hostname for flask to run")
    parser.add_argument("--flask-port", default=os.getenv("FLASK_PORT"), type=int, dest="flask_port", help="port for flask to run")
    return parser.parse_args()


def parse_duration(duration):
    if len(duration) == 0:
        return None, "duration is empty"
    times = {
        "h": 60 * 60,
        "m": 60,
        "s": 1
    }
    if duration[-1] not in times.keys():
        return None, "unknown time acronym. use one of \"{}\"".format(", ".join(times.keys()))
    elif not duration[:-1].isdigit():
        return None, "wrong time format"
    return int(duration[:-1]) * times[duration[-1]], None


def log_error(message):
    print(message)


class PingMonitoring:
    """
    duration:
        could be one of:
        1) hour
            - 10h
        2) minute
            - 10m
        3) second
            - 10s
    """
    def __init__(self, host_name, duration):
        self.error_happened = False
        self.host_name = host_name
        self.duration_seconds, error = parse_duration(duration)
        if error:
            log_error(error)
            self.error_happened = True
        self.report_time, self.result = list(), list()

    def ping_action(self):
        return {
            "host": self.host_name,
            "@timestamp": datetime.datetime.now().isoformat(),
            "ping": ping(self.host_name)
        }
