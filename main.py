from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('2d-fantasy-elf.jpg')

frame = 0
max_X, min_x = 800, 0
max_Y, min_Y = 600, 0
def handle_events():
    global running, dir_X, dir_Y #실행, 움직임 방향
    events = get_events()
    for event in events: #키 입력 시 입력되는 이벤트
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_X += 1
            elif event.key == SDLK_LEFT:
                dir_X -= 1
            elif event.key == SDLK_UP:
                dir_Y += 1
            elif event.key == SDLK_DOWN:
                dir_Y -= 1
            elif event.key == SDL_QUIT:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_X -= 1
            elif event.key == SDLK_LEFT:
                dir_X += 1
            elif event.key == SDLK_UP:
                dir_Y -= 1
            elif event.key == SDLK_DOWN:
                dir_Y += 1

running = True
dir_X, dir_Y = 0, 0 #x,y 방향
x, y = max_X // 2, max_Y // 2  # x, y축 위치

while running:
    character.clip_draw(frame * 215 + 350, 560, 100, 115, x, y)
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    x += dir_X * 5
    y += dir_Y * 5
    if x > max_X or x < min_x:
        dir_X = 0
    if y > max_Y or y < min_Y:
        dir_Y = 0
    delay(0.05)
