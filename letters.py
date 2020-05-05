import pyglet
import subprocess
from random import randrange

window = pyglet.window.Window()

label = pyglet.text.Label(' ',
                          font_name='monaco',
                          font_size=320,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    letter = chr(symbol)
    subprocess.Popen(["say", letter])
    label.text = letter.upper()

    red = (200,0,0,255)
    green = (0,200,0,255)
    blue = (70,0,255,255)
    yellow = (255,255,45,255)
    orange = (255, 130, 0, 255)
    pink = (255, 105, 210, 255)
    purple = (185, 70, 225, 255)

    colors = [red, green, blue, yellow, orange, pink, purple]
    label.color = colors[randrange(7)]


@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
