#!/usr/bin/python

import MySQLdb

# # Open database connection
# dbapi = MySQLdb.connect("jarvis.c16cpzmyddrq.us-east-1.rds.amazonaws.com","jarvis","MySQLSocialBase","locust-api" )
# dbapp = MySQLdb.connect("jarvis.c16cpzmyddrq.us-east-1.rds.amazonaws.com","jarvis","MySQLSocialBase","locust-app" )


dbapi = MySQLdb.connect( "mysql-producao-v3.ckxzlgg1orrm.sa-east-1.rds.amazonaws.com", "ansible", "!@#9df5b407U", "sb-tnotifications")
dbapp = MySQLdb.connect( "mysql-producao-v3.ckxzlgg1orrm.sa-east-1.rds.amazonaws.com", "ansible", "!@#9df5b407U", "sb-app-v3")


def insert_user(code):

   cursor = dbapi.cursor()

   sql = "INSERT INTO engine4_users (email, username, displayname, photo_id, status, status_date, search, show_profileviewers, level_id, invites_used, extra_invites, enabled, approved, creation_date, creation_ip, modified_date, lastlogin_date, lastlogin_ip, update_date, member_count, view_count, perfilcompleto, is_owner, is_external, auth_type, picture_id) VALUES ('usersb"+str(code)+"@socialbase.com.br', 'usersb"+str(code)+"@socialbase.com.br', 'User SB "+str(code)+"', NULL, NULL, NULL, 0, 1, 1, 0, 0, 1, 1, '2014-10-20 18:18:55', X'EFBFBDEFBFBD2E65', '2014-10-20 18:18:55', '2014-10-20 18:18:55', NULL, NULL, 0, 0, 0, 1, 0, 'LOCAL', 2)"
   cursor.execute(sql);
   dbapi.commit()

   cursor = dbapp.cursor()
   sql = "INSERT INTO users (username, last_login, create_at, last_update, password_hash, password_salt) VALUES ('usersb"+str(code)+"@socialbase.com.br', NULL, '2015-11-23 11:48:54', NULL, 'f457c4bc22d54f5c22523a422bdd2b6e', '2538948')"
   cursor.execute(sql);
   last_id = cursor.lastrowid

   cursor.execute("INSERT INTO users_networks (user_id, network_id) VALUES ("+str(last_id)+", 317)")
   dbapp.commit()

for i in range(1, 100):
   insert_user(i)