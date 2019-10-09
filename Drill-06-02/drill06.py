from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1000

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
cnt = 0
t = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
point = (random.randint(400, 800), random.randint(400, 800), random.randint(400, 800), random.randint(400, 800),
         random.randint(400, 800), random.randint(400, 800), random.randint(400, 800), random.randint(400, 800))

while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if cnt == 0:
        x = (2 * t ** 2 - 3 * t + 1) * point[0] + (-4 * t ** 2 + 4 * t) * point[2] + (2 * t ** 2 - t) * point[4]
        y = (2 * t ** 2 - 3 * t + 1) * point[1] + (-4 * t ** 2 + 4 * t) * point[3] + (2 * t ** 2 - t) * point[5]
        t += 0.02
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif cnt == 1:
        x = ((-t ** 3 + 2 * t ** 2 - t) * point[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[2] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * point[4] + (t ** 3 - t ** 2) * point[6]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * point[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[3] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * point[5] + (t ** 3 - t ** 2) * point[7]) / 2
        t += 0.02
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif cnt == 2:
        x = (2 * t ** 2 - 3 * t + 1) * point[2] + (-4 * t ** 2 + 4 * t) * point[4] + (2 * t ** 2 - t) * point[6]
        y = (2 * t ** 2 - 3 * t + 1) * point[3] + (-4 * t ** 2 + 4 * t) * point[5] + (2 * t ** 2 - t) * point[7]
        t += 0.02
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif cnt == 3:
        x = ((-t ** 3 + 2 * t ** 2 - t) * point[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[6] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * point[0] + (t ** 3 - t ** 2) * point[2]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * point[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[7] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * point[1] + (t ** 3 - t ** 2) * point[3]) / 2
        t += 0.02
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    delay(0.05)
    frame = (frame + 1) % 8

    if cnt == 0:
        if t == 0.5:
            t = 0
            cnt = 1
    elif cnt == 1:
        if t == 0.98:
            t = 0.5
            cnt = 2
    elif cnt == 2:
        if t == 1:
            t = 0
            cnt = 3
    elif cnt == 3:
        if t == 1:
            t = 0
            cnt = 0

close_canvas()
