import pygame
import random

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
WINDOW_MAX_FPS = 60

BACK_COLOUR = (3, 5, 54)

# Initial position of the object
object_x = 10
object_y = WINDOW_HEIGHT - 50
object_dy = 0  # Vertical velocity of the object
gravity = 1    # Acceleration due to gravity

# Obstacle settings
obstacles = []
obstacle_width = 30
obstacle_height = 40
obstacle_speed = 1

# Jump settings
jump_power = -20  # The initial upward velocity when jumping
jumping = False   # Flag to track if the object is currently jumping

def handle_events():
    global done, jumping, object_dy
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                object_dy = jump_power
                jumping = True

def update_obstacles():
    global obstacles
    
    if random.randint(0, 100) < 5:  # Adjust the probability for obstacle appearance
        obstacles.append([WINDOW_WIDTH, WINDOW_HEIGHT - obstacle_height])
    
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
    
    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -obstacle_width]

def check_collisions():
    global done
    
    for obstacle in obstacles:
        if object_x + 50 > obstacle[0] and object_x < obstacle[0] + obstacle_width \
                and object_y + 50 > obstacle[1] and object_y < obstacle[1] + obstacle_height:
            done = True  # Collision occurred, end the game

def update_object_position():
    global object_dy, object_y, jumping
    
    object_dy += gravity
    object_y += object_dy
    
    if object_y >= WINDOW_HEIGHT - 50:
        object_y = WINDOW_HEIGHT - 50
        object_dy = 0
        jumping = False

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("Hopper")

clock = pygame.time.Clock()
done = False
while not done:
    handle_events()
    update_obstacles()
    check_collisions()
    update_object_position()

    window.fill(BACK_COLOUR)
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(window, (255, 105, 180), (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
    
    pygame.draw.rect(window, (255, 0, 0), (object_x, object_y, 50, 50))  # Draw the object
    pygame.display.flip()

    clock.tick(WINDOW_MAX_FPS)

pygame.quit()
