import sys, pygame, math, random

# Starter code for an adventure game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
# Khoa Minh Ngo
# Vu Minh Thu Ha

def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the other.
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap != None

def main():
    """
    Set up all the needed variables and processes to run the game
    """

    # Initialize pygame
    pygame.init()

    map = pygame.image.load("map.png")
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    # Create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    map = map.convert_alpha()
    map_mask = pygame.mask.from_surface(map)

    # Create map 2
    map2 = pygame.image.load("map2.png")
    map2_rect = map2.get_rect()
    map2 = map2.convert_alpha()
    map2.set_colorkey((69,139,0))
    map2_mask = pygame.mask.from_surface(map2)

    # Create map 3
    map3 = pygame.image.load("map3.png")
    map3_rect = map3.get_rect()
    map3 = map3.convert_alpha()
    map3.set_colorkey((91, 59, 11))
    map3_mask = pygame.mask.from_surface(map3)

    # Create the key
    key = pygame.image.load("key.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (40, 40))
    key_rect = key.get_rect()
    key_rect.center = (380, 450)
    key_mask = pygame.mask.from_surface(key)

    # Create the finish button
    finish_button = pygame.image.load("finish_button.png").convert_alpha()
    finish_button = pygame.transform.smoothscale(finish_button, (120, 60))
    finish_button_rect = finish_button.get_rect()
    finish_button_rect.center = (580, 550)
    finish_button_mask = pygame.mask.from_surface(finish_button)

    # Create the level-1 start button
    start_button1 = pygame.image.load("level1.png").convert_alpha()
    start_button1 = pygame.transform.smoothscale(start_button1, (650, 623))
    start_button1_rect = start_button1.get_rect()
    start_button1_rect.center = (325, 311.5)
    start_button1_mask = pygame.mask.from_surface(start_button1)

    # Create the door for level 2
    door = pygame.image.load("door.png").convert_alpha()
    door = pygame.transform.smoothscale(door, (100, 120))
    door_rect = door.get_rect()
    door_rect.center = (510, 250)
    door_mask = pygame.mask.from_surface(door)

    # Create the level-2 key
    key2 = pygame.image.load("key.png").convert_alpha()
    key2 = pygame.transform.smoothscale(key2, (40, 40))
    key2_rect = key2.get_rect()
    key2_rect.center = (325, 320)
    key2_mask = pygame.mask.from_surface(key2)

    # Create the level-2 start button
    start_button2 = pygame.image.load("start_button.png").convert_alpha()
    start_button2 = pygame.transform.smoothscale(start_button2, (100, 100))
    start_button2_rect = start_button2.get_rect()
    start_button2_rect.center = (500, 65)
    start_button2_mask = pygame.mask.from_surface(start_button2)

    # Create the level-2 finish button
    finish_button2 = pygame.image.load("finish_button.png").convert_alpha()
    finish_button2 = pygame.transform.smoothscale(finish_button2, (90, 45))
    finish_button2_rect = finish_button2.get_rect()
    finish_button2_rect.center = (540, 497)
    finish_button2_mask = pygame.mask.from_surface(finish_button2)

    # Create the snake's offspring
    snake_offspring = pygame.image.load("snake.png").convert_alpha()
    snake_offspring = pygame.transform.smoothscale(snake_offspring, (15, 15))
    snake_offspring_rect = snake_offspring.get_rect()
    snake_offspring_rect.center = (300, 200)
    snake_offspring_mask = pygame.mask.from_surface(snake_offspring)

    # Create the player data
    snake_player = pygame.image.load("snake.png").convert_alpha()
    snake_player = pygame.transform.smoothscale(snake_player, (30, 30))
    snake_player_rect = snake_player.get_rect()
    snake_player_mask = pygame.mask.from_surface(snake_player)

    # Create the level-3 food
    apple = pygame.image.load("food.png").convert_alpha()
    apple = pygame.transform.smoothscale(apple, (40, 40))
    apple_rect = apple.get_rect()
    apple_rect.center = (64, 64)
    apple_mask = pygame.mask.from_surface(apple)

    # Create the level-3 start button
    snake_start_button3 = pygame.image.load("snake_start_button.png").convert_alpha()
    snake_start_button3 = pygame.transform.smoothscale(snake_start_button3, (650, 623))
    snake_start_button3_rect = snake_start_button3.get_rect()
    snake_start_button3_rect.center = (325, 311.5)
    snake_start_button3_mask = pygame.mask.from_surface(snake_start_button3)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font - there is some problem on my Mac that makes this pause for 10s of seconds sometimes.
    # I will see if I can find a fix.
    myfont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 35)

    # The started variable records if the start color has been clicked and the level started
    started = False
    # The key_found variable records if the key has been found
    key_found = False
    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True
    # level to decide which maze is displayed
    level = 1
    # create a list containing positions of apples for level-3 game
    apple_list = []
    # record the development of the snake in level-3 game
    development = 0
    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop. In it, we must:
    # - check for events
    # - update the scene
    # - draw the scene
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        if level == 1:
            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            snake_player_rect.center = pos

            if pixel_collision(snake_player_mask, snake_player_rect, start_button1_mask,
                               start_button1_rect) and event.type == pygame.MOUSEBUTTONDOWN:
                started = True

            # Draw the background
            screen.fill((69,139,0))  # This helps check if the image path is transparent
            screen.blit(map, map_rect)

            if started:
                # Draw the finish button
                screen.blit(finish_button, finish_button_rect)

                # Remove key from the map when player take the key
                if not key_found:
                    screen.blit(key, key_rect)

                # See if we touch the maze walls
                if pixel_collision(snake_player_mask, snake_player_rect, map_mask, map_rect):
                    message_screen = pygame.image.load("lose.png").convert_alpha()
                    message_screen = pygame.transform.smoothscale(message_screen, (382.5, 325))
                    message_screen_rect = message_screen.get_rect()
                    message_screen_rect.center = (325, 311.5)
                    screen.blit(message_screen, message_screen_rect)
                    level = -1 # Stop the game

                if not key_found and pixel_collision(snake_player_mask, snake_player_rect, key_mask, key_rect):
                    key_found = True

            if started is False:
                # Draw the start_button
                screen.blit(start_button1, start_button1_rect)

            # Draw the player character
            screen.blit(snake_player, snake_player_rect)

            if key_found and pixel_collision(snake_player_mask, snake_player_rect, finish_button_mask, finish_button_rect):
                level += 1
                started = False
                key_found = False

        if level == 2:
            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            snake_player_rect.center = pos

            if pixel_collision(snake_player_mask, snake_player_rect, start_button2_mask,
                               start_button2_rect) and event.type == pygame.MOUSEBUTTONDOWN:
                started = True

            # Draw the background
            screen.fill((69,139,0))
            screen.blit(map2, map2_rect)

            if started:
                screen.blit(snake_offspring, snake_offspring_rect)
                # Remove key from the map when player take the key
                if not key_found:
                    screen.blit(key2, key2_rect)

                # Draw the finish button
                screen.blit(door, door_rect)

                # See if we touch the maze walls
                if pixel_collision(snake_player_mask, snake_player_rect, map2_mask, map2_rect):
                    message_screen = pygame.image.load("lose.png").convert_alpha()
                    message_screen = pygame.transform.smoothscale(message_screen, (382.5, 325))
                    message_screen_rect = message_screen.get_rect()
                    message_screen_rect.center = (325, 311.5)
                    screen.blit(message_screen, message_screen_rect)
                    level = -1  # Stop the game

                if not key_found and pixel_collision(snake_player_mask, snake_player_rect, key2_mask, key2_rect):
                    key_found = True
                    print("colliding with key")

            if started is False:
                # Draw the start_button for this level
                screen.blit(start_button2, start_button2_rect)

            # Draw the player character
            screen.blit(snake_player, snake_player_rect)

            if key_found and pixel_collision(snake_player_mask, snake_player_rect, door_mask, door_rect):
                level += 1
                started = False
                key_found = False

        if level == 3:
            # Position the snake_player to the mouse location
            pos = pygame.mouse.get_pos()
            snake_player_rect.center = pos

            if development == 100:
                level = -1 # Stop the game when player wins

            if pixel_collision(snake_player_mask, snake_player_rect, snake_start_button3_mask,
                               snake_start_button3_rect) and event.type == pygame.MOUSEBUTTONDOWN:
                started = True

            # Draw the background
            screen.fill((91, 59, 11))
            screen.blit(map3, map3_rect)

            if started:
                development_text = 'Development: ' + str(development) + '%'
                development_stat = myfont.render(development_text, True, (250, 250, 250))
                screen.blit(development_stat, (220, 50))

                # See if we touch the maze walls
                if pixel_collision(snake_player_mask, snake_player_rect, map3_mask, map3_rect):
                    message_screen = pygame.image.load("lose.png").convert_alpha()
                    message_screen = pygame.transform.smoothscale(message_screen, (382.5, 325))
                    message_screen_rect = message_screen.get_rect()
                    message_screen_rect.center = (325, 311.5)
                    screen.blit(message_screen, message_screen_rect)
                    level = -1  # Stop the game

                # Time for each apple is randomly display
                if frame_count % 50 == 0:
                    apple_position = (random.randrange(150, 520), random.randrange(200, 410))
                    apple_list.append(apple_position)

                # Display all apple not yet eaten
                for apple_display in apple_list:
                    screen.blit(apple, apple_rect)
                    apple_position_x = apple_display[0]
                    apple_position_y = apple_display[1]
                    apple_rect.center = (apple_position_x, apple_position_y)

                    # Remove the apple when it is eaten
                    if pixel_collision(snake_player_mask, snake_player_rect, apple_mask, apple_rect):
                        apple_list.remove((apple_position_x, apple_position_y))
                        development += 10

                if development == 100:
                    message_screen = pygame.image.load("win.png").convert_alpha()
                    message_screen = pygame.transform.smoothscale(message_screen, (650, 623))
                    message_screen_rect = message_screen.get_rect()
                    message_screen_rect.center = (325, 325)
                    screen.blit(message_screen, message_screen_rect)

            if started is False:
                # Draw the start_button
                screen.blit(snake_start_button3, snake_start_button3_rect)

            # Draw the player character
            screen.blit(snake_player, snake_player_rect)

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(33)

    pygame.quit()
    sys.exit()


# Start the program
main()