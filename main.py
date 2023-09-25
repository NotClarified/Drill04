from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('2d-fantasy-elf.jpg')

frame = 0

def handle_events():
    global running, dir #실행, 움직임 방향
    events = get_events()
    for event in events: #키 입력 시 입력되는 이벤트
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            pass
        elif event.type == SDL_KEYUP:
            pass

while running:
    character.clip_draw(frame * 215 + 350, 560, 100, 115, 200, 200)
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    delay(0.05)

close_canvas()