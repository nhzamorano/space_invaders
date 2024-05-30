class Settings():
    """
    A class to store all setting for Alien Invasion
    """
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600 
        self.bg_color = (250,240,210)
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
    