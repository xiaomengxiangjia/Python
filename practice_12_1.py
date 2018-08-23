import sys

import pygame
from practice_sky import Sky

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Blue Sky")
    
    # 创建一艘飞船
    panda_new = Sky(screen)
    
    # 设置背景色
    bg_color = (190, 238, 225)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 让最近绘制的屏幕可见
        screen.fill(bg_color)
        panda_new.blitme()
                
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        
run_game()
