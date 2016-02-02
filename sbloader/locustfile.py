# coding: utf-8

import ssl
from locust import HttpLocust, task, events, web
from websocket import create_connection
import time
from sbclient import SbClient, sb_debug, get_ws_server
import random

socket_list = []

class SBUserBehavior(SbClient):
    """
    Classe to simulate socialbase users behaviors, his configuration commming from SbClient heritage,
    so would be nice if you expend minute to see how it works

    """
    sb_debug(False) # set True to active errors output
    user_id = 4

    def on_start(self):
        """
        on_start is called when a Locust start before any task is scheduled,
        as well, every time will be created a new connection with websocket server, provided by tornado
        """
        time.sleep(1)
        token = self.login(self.getCredendials(4)).json()['access_token']
        print("KKKKK", token)
        self.user_token.append(token)
        self.header['Authorization'] = "Bearer %s" % token
        SBUserBehavior.user_id += 1

    def login(self, user):
        """
        called for every user
        """
        return self.sbtask('POST', self.url_login, user, None)

    @task(20)
    def run_teste_tasks(self):
        """
        task to simulate a post user on socialbase plataform
        :weight: 20
        """
        self.group_all()

    @task(20)
    def run_publish_tasks(self):
        """
        task to simulate a post user on socialbase plataform
        :weight: 20
        """
        self.publish()

    @task(25)
    def run_comment_tasks(self):
        """
        task that choose a randon action and leave a comment
        :weight: 25
        """
        self.comment()

    @task(30)
    def run_like_publish_tasks(self):
        """
        task that choose a randon action and give a like point
        :weight: 30
        """

        self.like_publish()

    @task(30)
    def run_like_comment_tasks(self):
        """
        task that choose a randon action and give a like point
        :weight: 30
        """
        self.like_comment()

    @task(10)
    def run_follow_tasks(self):
        """
        this task go to persons page choose someone randomically and give a follow
        :weight: 3
        """
        self.follow()

    @task(10)
    def run_search_tasks(self):
        """
        task that choose some words to simulate the search
        :weight: 2
        """
        self.sb_search()

    @task(1)
    def run_categories_news(self):
        """
        task that ask for categories of news
        :weight: 2
        """
        self.news()

    @task(2)
    def run_group_tasks(self):
        """
        task that do a post group, sending notification to all users:w
        :weight: 1
        """
        self.group()

    @task(10)
    def run_send_ws_message(self):
        """
        task to simulate a chat conversations between sbsuporte and randomic user
        :weight: 4
        """
        self.ws.send(self.send_ws_message())

    @task(10)
    def run_send_invite_group(self):
        """
        task to simulate a chat conversations between sbsuporte and randomic user
        :weight: 4
        """
        self.group_invite()

class WebsiteUser(HttpLocust):
    """
    Represents an HTTP “user” which is to be hatched and attack the system that is to be load tested.
    """
    task_set = SBUserBehavior
    """
    # SBUserBehavior class defining a set of tasks that a Locust user will execute.
    # When a TaskSet starts running, it will pick a task from the tasks attribute,
    # execute it, call it’s wait function which will sleep a random number between min_wait and max_wait milliseconds.
    # It will then schedule another task for execution and so on.
    """

    min_wait = 5000
    """
    # Minimum waiting time between the execution of locust tasks.
    # Can be used to override the min_wait defined in the root Locust class,
    # which will be used if not set on the TaskSet.
    """

    max_wait = 10000
    """
    # Maximum waiting time between the execution of locust tasks.
    # Can be used to override the max_wait defined in the root Locust class,
    # which will be used if not set on the TaskSet.
    """


# """
# We need somewhere to store the stats.
# On  the master node stats will contain the aggregated sum of all content-lengths,
# while one the slave nodes this will be the sum of the content-lengths since the
# last stats report was sent to the master
# """
# stats = {"content-length":0}
#
# def on_request_success(method, path, response_time, response):
#     """
#     Event handler that get triggered on every successful request
#     """
#     stats["content-length"] += int(response.info.getheader("content-length"))
#
# def on_report_to_master(client_id, data):
#     """
#     This event is triggered on the slave instances every time a stats report is
#     to be sent to the locust master. It will allow us to add our extra content-length
#     data to the dict that is being sent, and then we clear the local stats in the slave.
#     """
#     data["content-length"] = stats["content-length"]
#     stats["content-length"] = 0
#
# def on_slave_report(client_id, data):
#     """
#     This event is triggered on the master isntance when a new stats report arrives
#     from a slave. Here we just add the content-length to the master's aggregated
#     stats dict.
#     """
#     stats["content-length"] += stats["content-length"]
#
# # Hook up the event listeners
# events.request_success += on_request_success
# events.report_to_master += on_report_to_master
# events.slave_report += on_slave_report
#
# @web.app.route("/content-length")
# def total_content_length():
#     """
#     Add a route to the Locust web app, where we can see the total content-length
#     """
#     return "Total content-length recieved: %i" % stats["content-length"]