import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        
run_game()
