class Ajustes:
    """Una clase que guarda todos los ajustes para invasión alien"""

    def __init__(self):
        """Inicializa los ajustes del juego"""
        # ajustes de pantalla
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)
        # velocidad de la nave
        self.nave_velocidad = 3.5