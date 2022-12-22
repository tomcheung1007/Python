import sys   #to exit game when player quits
from time import sleep
import pygame

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''overall class to manage game assets and behaviour'''

    def __init__(self):
        '''initialise the game, and create game resources'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        #create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #make the play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        '''respond to keyboard and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''start a new game when the player clicks play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset the game settings
            self.settings.initalize_dynamic_settings()
            #reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True 
            self.sb._prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            #get rid of any remaining alien and bullets
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_event(self, event):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        '''respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''update position of bullets and get rid of old bullets'''
        #update bullet positions
        self.bullets.update()
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        '''respond to bullet-alien collisions'''
        #remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb._prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()    
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
     
    def _update_aliens(self):
        '''check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.
        '''
        self._check_fleet_edges()
        self.aliens.update()
            #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
        
    def _ship_hit(self):
        '''respond to the ship being hit by an alien'''
        if self.stats.ships_left > 0:
            #decrement ships_left and update scoreboard
            self.stats.ships_left -=1
            self.sb.prep_ships()
            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        '''create the fleet of aliens'''
        #create an alien and find the number of aliens in a row
        #spacing between each alien is equial to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
    #create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien) 

    def _check_fleet_edges(self):
        '''respond appropriately if any aliens have reached an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''drop the entire fleet and change the fleet's direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        '''check if any aliens have reached the bottom of the screen'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        '''update images on the screen and flip to the new screen'''
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
                     
        #make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':                  #this code tells python to run code if __name__ (current module i.e. app.py) is equal to __main__ (i.e. being run directly). So if imported, it will not run
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

