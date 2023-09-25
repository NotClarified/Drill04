from pico2d import *

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('2d-fantasy-elf.jpg')

frame = 0
max_X, min_X = TUK_X - 100, 50
max_Y, min_Y = TUK_Y - 115, 70

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
    ground.draw(TUK_X // 2, TUK_Y // 2)
    character.clip_draw(frame * 215 + 350, 560, 100, 115, x, y)
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    x += dir_X * 5
    y += dir_Y * 5
    if x > max_X or x < min_X:
        dir_X = 0
    elif y > max_Y or y < min_Y:
        dir_Y = 0
    delay(0.05)
