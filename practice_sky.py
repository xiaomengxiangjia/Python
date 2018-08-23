import pygame

class Sky():
    
    def __init__(self, screen):
        """初始化熊猫并设置其初始位置"""
        self.screen = screen
        
        # 加载熊猫图像并获取其外接矩形
        self.image = pygame.image.load('images/panda.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每只新熊猫放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """在指定位置绘制熊猫"""
        self.screen.blit(self.image, self.rect)
