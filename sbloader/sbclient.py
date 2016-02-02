# Metodos de apoio
# coding: utf-8

import json
import sys
from locust import TaskSet
import random
from config import *


class SbClient(Target, TaskSet):

    user_token, publish_id, comment_id, like_id = [], [], [], []

    def publish(self):
        token = random.choice(self.user_token)
        self.header['Authorization'] = "Bearer %s" % token
        self.publish_id.append({"user": token,
                                "self": self.sbtask('POST',
                                                        '/v3/activities',
                                                        random.choice(data),
                                                        None).json()['self']})
        output('BRANCO', ' PUBLISH POST ')

    def comment(self):
        if self.publish_id:
            token = random.choice(self.user_token)
            publish = random.choice(self.publish_id)
            self.header['Authorization'] = "Bearer %s" % token
            self.comment_id.append({"user": token,
                                    "self": self.sbtask('POST',
                                                             publish['self']+'/comments',
                                                             random.choice(data),
                                                             '/v3/activities/[int]/comments').json()['self']})
            output('AZUL', ' COMMENT ')

    def home(self):
        [self.sbtask('GET', ed, None, None) for ed in behavior_home]
        output('VERDE', ' HOME ')

    def news(self):
        token = random.choice(self.user_token)
        self.header['Authorization'] = "Bearer %s" % token
        self.sbtask('GET', '/v3/news?category=1', None, None)
        output('VERMELHO', ' GET NEWS ')

    def follow(self):
        not_following = []
        token = random.choice(self.user_token)
        self.header['Authorization'] = "Bearer %s" % token
        self.sbtask('GET', '/v3/birthdays?currentDate=' + str(datetime.date.today()), None, None)

        def process_user(users):
            if users:
                for i in users:
                    if not i['isFollowing']:
                        not_following.append(i['userId'])

        #TODO try define a dimanic range
        for i in xrange(0, 4):
            users = self.sbtask('GET',
                                '/v3/members?offset=' + str(10 * i) + '&limit=10',
                                None,
                                '/v3/members?offset=[int]&limit=10').json()['items']
            process_user(users)

        if not_following:
            self.sbtask('POST', '/v3/users/me/following', {"userId": random.choice(not_following)}, None)

        [self.sbtask('GET', ed, None, None) for ed in behavior_novidades]
        output('ROXO', ' FOLLOW AND BACK TO NEWS ')

    def like_publish(self):
        if self.publish_id:
            publish = random.choice(self.publish_id)
            token = random.choice(self.user_token)
            self.header['Authorization'] = "Bearer %s" % token
            if not token == publish['user']:
                self.like_id.append({"user": token,
                                     "LikeId": self.sbtask('POST', publish['self']+'/likes', None, '/v3/activities/[int]/likes')})
                output('AZUL', ' LIKE PUBLISH ')

    def like_comment(self):
        if self.comment_id:
            comment = random.choice(self.comment_id)
            token = random.choice(self.user_token)
            self.header['Authorization'] = "Bearer %s" % token
            if not token == comment['user']:
                self.like_id.append({"user": token,
                                     "LikeId": self.sbtask('POST', comment['self'] +
                                                           '/likes', None, '/v3/activities/[int]/comments/[int]/likes')})
                output('VERDE', ' LIKE COMMENT ')

    def sb_search(self):
        keyword = ["futuro", "passado", "pindureta", "entendeuam", "Mainhaaa", "eu", "blablabla"]
        w = random.choice(keyword)
        self.sbtask('GET', '/v3/search?autocomplete=true&query=' + w, None, None)
        output('VERDE', ' SEARCH ')

    def send_ws_message(self):
        room = random.choice(room_list)
        payload = self.room_message(room['room_id'], room['email'])
        output('AMARELO', ' CHAT MESSAGE ')
        return payload

    def group(self):
        [self.sbtask('GET', ed, None, None) for ed in behavior_grupo]
        self.sbtask('POST', '/v3/groups', group_data, None)
        output('VERDE', ' MESSAGE IN GROUP TO ALL PEOPLE ')

    def group_invite(self):
        token = random.choice(self.user_token)
        self.header['Authorization'] = "Bearer %s" % token
        print("HEADER ", self.header)
        for i in xrange(10, 35):
            group_id = self.sbtask('POST', '/v3/groups', create_group(i), None).json()['groupId']
            for j in xrange(1):
                self.sbtask('POST', '/v3/groups/'+str(group_id)+'/invites', {"type": "users", "idList": 5}, None)

    def group_all(self):

        user = {"username": "usersb1@socialbase.com.br1",
                "password": "socialbase",
                "type": "credentials"
                }

        token = self.sbtask('POST', self.url_login, user, None)
        self.header['Authorization'] = token.json()['access_token']
        self.sbtask('POST', '/v3/activities', group_data, None)
        output('VERMELHO', ' MESSAGE IN GROUP TO ALL PEOPLE ')

    def sbtask(self, method, endpoint, data, name):
        if method.upper() == "GET":
            return self.client.get(endpoint, headers=self.header, verify=False, name=name)
        elif method.upper() == "DELETE":
            return self.client.delete(endpoint, headers=self.header, name=name)
        elif method.upper() == "PUT":
            return self.client.put(endpoint, headers=self.header, name=name)
        else:
            return self.client.post(endpoint, headers=self.header, data=json.dumps(data), verify=False, name=name)

    def getCredendials(self, id):
        return {"username": "usersb" + str(id) + "@socialbase.com.br",
                "password": "socialbase",
                "type": "credentials"
                }

    def ws_login(self, token):
        output('AMARELO', ' WS LOGIN ')
        return json.dumps({"type": "authenticate",
                "payload":
                   {"token": token,
                    "issue": "https://l-app.socialbase.com.br/",
                    "audience": "https://l.socialbase.com.br"
                    }
               })

    def ws_message(self, user_name):
        return {"type": "chat",
                         "payload":
                             {"command": "contacts_online",
                              "details":
                                  [{"status": 1, "user_name": user_name}]
                              }
                         }

    def ws_ping(self):
        return {"type": "ping",
                         "payload":
                             {"command": "ping",
                              "details": "ping"
                                  }
                              }

    def open_room(self):
        return json.dumps({"type": "chat",
                           "payload":
                               {"command": "room_create",
                                "details":
                                    #{"new_user":  "usersb"+str(random.randint(1, 100))+"@socialbase.com.br"}
                                    {"new_user":  "sbsuporte@socialbase.com.br"}
                                }
                           })

    def room_message(self, room_id, sender):
        return json.dumps({"type":"chat",
                           "payload":
                               {"command":"room_message",
                                "details":
                                    {"sender": sender,
                                     "destination":room_id,
                                     "message": "Ola eu sou o user"+str(sender)
                                     }
                                }
                           })

    # def loop(self):
    #     while True:
    #         ob = self.ws.recv()
    #         print("return_ws", ob)

def sb_debug(op):
    if not op:
        f = open('/dev/null', 'w')
        sys.stderr = f

def get_ws_server():
    return ws_server

def create_group(id):
    return {"photo": "/images/data/group_picture.png",
            "photo_id": None,
            "search": False,
            "title": "Teste"+str(id),
            "description": "Teste_ de notificações"+str(id),
            "privacy": True,
            "invite": False
            }