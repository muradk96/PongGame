import socket
from _thread import *
from player import Player
import pickle
import sys
# from ball import Ball
# from collision_manager import CollisionManager

server = "192.168.178.26"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for a connection, Server Started")


def read_pos(str):
    str = str.split(",")
    if len(str) == 2:
        return int(str[0]), int(str[1])
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5])

def make_pos(tup):
    input = ""
    for t in tup:
        input = input + str(t) + ","
    return input[:-1]

pos = [(30, 200), (960, 200)]
ball_pos = [500, 250, 3, 3]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = (data[0], data[1])

            if not data:
                print("Disconnected")
                break
            else:

                if player == 1:
                    reply = (pos[0][0], pos[0][1], ball_pos[0], ball_pos[1], ball_pos[2], ball_pos[3])

                else:
                    ball_pos[0] = data[2]
                    ball_pos[1] = data[3]
                    ball_pos[2] = data[4]
                    ball_pos[3] = data[5]
                    reply = (pos[1][0], pos[1][1], ball_pos[0], ball_pos[1], ball_pos[2], ball_pos[3])



                print("Received: ", data)
                print("Sending : ", reply)

                conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
