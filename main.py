from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('2d-fantasy-elf.jpg')

frame = 0

while True:
    character.clip_draw(frame * 215 + 350, 560, 100, 115, 200, 200)
    # character.clip_draw(left,bottom,width,height,x,y)
    frame = (frame + 1) % 5
    update_canvas()
    delay(0.5)

close_canvas()