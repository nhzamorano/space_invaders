import pygame 
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf 

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        )
    pygame.display.set_caption("Alien Invasion")
    #Make the play button
    play_button = Button(ai_settings,screen,'Paly')
    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #bg_color = (250,240,210)
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    #alien = Alien(ai_settings, screen)
    
    gf.create_fleet(ai_settings,screen,stats,ship,aliens,bullets)

    # Start the main loop for the game.
    while True:
        #Ojo aqui con aliens
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens, bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, stats,sb, ship, aliens, bullets,play_button)
        
#310 - display the level

run_game()