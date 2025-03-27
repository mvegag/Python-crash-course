import sys
import pygame

from ajustes import Ajustes
from nave import Nave

class AlienInvasion:
    """
    Clase para manejar los assets y el comportamiento
    """

    def __init__(self):
        """Inicializa el juego y crea los recursos"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.ajustes = Ajustes()

        self.screen = pygame.display.set_mode(
            (self.ajustes.screen_width, self.ajustes.screen_height)
        )
        pygame.display.set_caption("Invasión juanc")

        self.nave = Nave(self)

    def run_game(self):
        """Empieza el ciclo principal del juego"""
        while True:
            # observa los movimientos del mouse y teclado
            self._check_events() # helper method
            self.nave.update()
            # redibuja la pantalla con cada paso por el loop
            self._update_screen()
            # reloj
            self.clock.tick(60) # pygame trata de correr el loop 60 veces por segundo

    def _check_events(self):
        """Responde a movimientos del teclado y del mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a presiones del teclado"""
        if event.key == pygame.K_RIGHT:
            # Mover la nave a la derecha e izquierda
            self.nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = True
        # salir del juego presionando q
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a dejar de presionar la tecla"""
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = False

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a una nueva pantalla"""
        self.screen.fill(self.ajustes.bg_color)
        self.nave.blitme()
        # hace la pantalla disponible
        pygame.display.flip()

if __name__ == "__main__":
    # crear una instancia del juego y correrlo
    ai = AlienInvasion()
    ai.run_game()

# controla la tasa de fotogramas
## queremos la misma velocidad de fotogramas en todos los sistemas
## creamos un reloj, el reloj cambia una vez cada paso por el loop principal
## si el loop se procesa más rapido que lo que definimos, pygame calcula el tiempo correcto para pausar y que corra
## a ritmo consistente

# Color de fondo



