#!/usr/bin/env python

import pyglet
from pyglet import shapes
from pyglet.window import key, mouse

from board import *


N = 15

config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(width=750, height=750, caption='Gomoku', config=config)

field_size = window.height // N
board_size = field_size * N

board = Board(N)
player = Color.BLACK


@window.event
def on_draw():
    window.clear()
    shapes.Rectangle(x=0, y=0, width=board_size, height=board_size, color=(30, 100, 160)).draw()

    for i in range(N):
        p = (i+0.5) * field_size
        shapes.Line(x=p, y=0, x2=p, y2=board_size).draw()
        shapes.Line(x=0, y=p, x2=board_size, y2=p).draw()

    for i, row in enumerate(board.fields):
        for j, color in enumerate(row):
            if color != Color.NONE:
                v = 200 if color == Color.WHITE else 30
                x, y = (i+0.5)*field_size, (j+0.5)*field_size
                shapes.Circle(x=x, y=y, radius=field_size/2-2, color=(v, v, v)).draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT and board.winner == Color.NONE:
        i = x // field_size
        j = y // field_size

        if board.is_empty(i, j):
            board.put(i, j, player)

            if board.winner == Color.NONE:
                board.ai(player.opponent)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.R:
        global board, player
        board = Board(N)
        player = player.opponent
        if player == Color.WHITE:
            r = range(N//2 - 3, N//2 + 4)
            board.put(*random.choice([(i, j) for i in r for j in r]), player.opponent)


if __name__ == '__main__':
    pyglet.app.run()
