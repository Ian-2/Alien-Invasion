class Settings:
    #class to store gamesettings

    def __init__(self):
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (176, 224, 230)

        #ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #bullet Settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 20

        #scoring Settings
        self.alien_points = 50
        #speed increase rate
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale