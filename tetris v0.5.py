from time import sleep
from blockRom import *
from pynput import keyboard
import random
from copy import copy
import os
def canMoveX(num):
    canMove = True
    currentLine = 0
    for line in activeBoard:
        for row in line:
            pos = row + num
            if pos > 9 or pos < 0 or pos in passiveBoard[currentLine]:
                canMove = False
        currentLine += 1
    return canMove

def moveX(num):
    if canMoveX(num):
        line = 0
        for lines in activeBoard:
            row = 0
            for rows in lines:
                activeBoard[line][row] += num
                row += 1
            line += 1
    draw()
    
def canMoveY():
    canMove = True
    nextLine = 1
    for line in activeBoard:
        for row in line:
            if nextLine > 19 or row in passiveBoard[nextLine]:
                canMove = False
                break
        nextLine += 1
    return canMove

def moveY():
    activeBoard.pop()
    activeBoard.insert(0,[])
    draw()

def on_press(key):
    try:
        if key.char == 'a':
            moveX(-1)
        elif key.char == 'd':
            moveX(1)
        if key.char == 's' and not activeBoard[19]:
            if canMoveY():
                moveY()
    except:
        if key == key.left:
            moveX(-1)
        elif key == key.right:
            moveX(1)
        elif key == key.down and not activeBoard[19]:
            if canMoveY():
                moveY()
        elif key == key.esc:
            thing

def coordToBoard(x,y):
    x -= 1
    y -= 1
    if not x in activeBoard[y]:
        activeBoard[y].append(x)
def clear():
    print('\033c', end='')
def draw():
    renderBoard = f'''Score: {score}    Next Piece: Square
                        '''
    currentLine = 0
    for line in activeBoard:
        renderLine = ''
        for num in range(10):
            if num in line or num in passiveBoard[currentLine]:
                renderLine += '[]'
            else:
                renderLine += ' .'
        renderBoard += '<!' + renderLine + '''!>
                        '''
        currentLine += 1
    renderBoard += '<!********************!>'
    print('\033c', end='')
    os.system('cls')
    print(renderBoard)

def store():
    currentLine = 0
    for line in activeBoard:
        for row in line:
            if row not in passiveBoard[currentLine]:
                passiveBoard[currentLine].append(row)
        currentLine += 1

activeBoard = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
passiveBoard = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
coordToBoard(5,1)
coordToBoard(5,2)
coordToBoard(5,3)
coordToBoard(6,3)
time = 0.5
score = 0
draw()
listener = keyboard.Listener(on_press=on_press)
listener.start()
sleep(time)
while True:
    while canMoveY():
        moveY()
        sleep(time)
    store()
    score += 100
    if score%1000 == 0:
        time *= 0.9
    activeBoard = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    coordToBoard(5,1)
    coordToBoard(6,1)
    coordToBoard(5,2)
    coordToBoard(6,2)
    draw()
    sleep(time)