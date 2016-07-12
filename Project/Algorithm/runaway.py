#!/usr/bin/python
#-​*- encoding: utf-8 -*​-

import sys
global roomindex

def open(iteration, list):
    for i in roomindex[::iteration]:
        list[i] = 1 - list[i]

cases = input()
for i in range(cases + 1) :
    roomNumber = int(input())
    roomindex = list(range(roomNumber + 1))
    room = [0] * (roomNumber + 1);
    count = 0

    for j in range(1, roomNumber + 1):
        open(j, room);

    for j in range(1, roomNumber + 1):
        if room[j] == 1:
            count = count + 1

    print count
