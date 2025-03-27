import pygame

class Nave:
    """Clase que maneja la nave"""

    def __init__(self, ai_game):
        """Inicializa la nave y coloca la posición inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # python trata los objetos como rectangulos
        self.ajustes = ai_game.ajustes

        # carga la imagen
        self.image = pygame.image.load("img/juanc.bmp")
        self.image= pygame.transform.scale(self.image, (200, 300))
        self.rect = self.image.get_rect()

        # comienza la nave en el centro de abajo
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # guardar un decimal para la posición horizontal de la nave

        # bandera de movimiento, empieza con la nave que no se mueve
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave basado en la bandera de movimiento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ajustes.nave_velocidad
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ajustes.nave_velocidad

        self.rect.x = self.x

    def blitme(self):
        """Dibuja la nave en su posición inicial"""
        self.screen.blit(self.image, self.rect)

