from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('2d-fantasy-elf.jpg')

frame = 0

def handle_events():
    pass

while True:
    character.clip_draw(frame * 215 + 350, 560, 100, 115, 200, 200)
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    delay(0.05)

close_canvas()