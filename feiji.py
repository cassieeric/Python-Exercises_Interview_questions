# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time

# 子弹夹
list = []

# 程序的入口
def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 接受图片背景信息
    background = pygame.image.load('./feiji/background.png')

    # 飞机图片的接收
    plane = pygame.image.load('./feiji/hero1.png')

    # 设置飞机位置
    x = 480/2 - 100/2
    y = 600

    # 设置飞机速度
    speed = 10

    while True:
        # 把背景图片剪切到游戏窗口上
        screen.blit(background, (0, 0))
        # 把飞机图片剪切到游戏窗口上
        screen.blit(plane, (x, y))

        # 事件监测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()  # 这种方式是能够检测连续按下的，比之前的版本要新

        if key_pressed[K_w] or key_pressed[K_UP]:
            print('up')
            y -= speed

        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print('down')
            y += speed

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print('left')
            x -= speed

        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print('right')
            x += speed

        if key_pressed[K_SPACE]:
            print('发射子弹')
            bullet = pygame.image.load('./feiji/bullet.png')
            # 子弹的详细信息
            my_bullet = {
                '子弹': bullet,
                'x': x + 40,
                'y': y - 20
            }
            # 把子弹添加到弹夹里
            list.append(my_bullet)

        for i in list:
            screen.blit(i['子弹'], (i['x'], i['y']))
            i['y'] -= 25



        # 更新数据
        pygame.display.update()

        # 减少CPU的使用量
        time.sleep(0.01)

main()