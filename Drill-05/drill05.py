from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global x, y
    global boy_x, boy_y, boy_x_new, boy_y_new
    global point, n
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            boy_x_new, boy_y_new = x, y
            point = [(boy_x, boy_y), (boy_x_new, boy_y_new)]
            draw_line(point[n - 1], point[n])
            boy_x_new, boy_y_new = boy_x, boy_y
    pass


def draw_line(p1, p2):
    for i in range(0, 100 + 1, 2):
        t = i / 100
        boy_x = (1 - t) * p1[0] + t * p2[0]
        boy_y = (1 - t) * p1[1] + t * p2[1]
        character(0, 100, 100, 100, boy_x, boy_y)

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

n = 1
point = [(0, 0), (0, 0)]
boy_x, boy_y = 500, 500
boy_x_new, boy_y_new = 0, 0
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 100, 100, x, y)
    character.clip_draw(0, 100, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
