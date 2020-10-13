import yadupload as ya
admins = {'Admin': 526752662}
users = {}  # 12345678:1


def log(message):
    logs = open('logs.txt', 'a', encoding='utf-8')
    #logs.write("<!------!> ")
    from datetime import datetime
    logs.write(str(datetime.now()))
    logs.write("Message from {0} {1} (id = {2}) \n {3}\n".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id), message.text))
    logs.close()
    ya.upload_to_disk()


def zapoln_db():
    f = open('users_db.txt', 'r')
    for line in f:
        if line != '':
            line = line[0:len(line) - 1]
            buf = line.split(':')
            users[int(buf[0])] = int(buf[1])
    f.close()
    #print(users)


def chech_user(user_id, group=1):
    zapoln_db()
    # for id in users.keys():
    #     if user_id == id:
    #         break
    # else:
    #     f = open('users_db.txt', 'a')
    #
    #     users[user_id] = group
    #     f.write(str(user_id))
    #     f.write(':')
    #     f.write('{}\n'.format(group))
    #     f.close()
    #print(users)
    for id in users.keys():
        if user_id == id:
            break
    else:
        users[user_id] = 1
        f = open('users_db.txt', 'a', encoding='utf8', errors='ignore')
        f.write(str(user_id))
        f.write(':')
        f.write('{}\n'.format(1))
        f.close()


    #print(users)

def zapoln_file(user_id):
    f = open('users_db.txt', 'w', encoding='utf8', errors='ignore')
    for id in users.keys():
        f.write(str(id))
        f.write(':')
        if users[id] == None:
            f.write('{}\n'.format(1))
        else:
            f.write('{}\n'.format(users[id]))
    f.close()
