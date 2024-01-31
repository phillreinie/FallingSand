import pygame
import random


pygame.init()


width, height = 500, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Sand Simulaton")
cell_size = 5
sand_color = (194, 178, 128)

#setting grid dimensions
cols, rows = width // cell_size, height // cell_size

# Initialize the clock for frame rate control
clock = pygame.time.Clock()

# setting up default 0 for gridcell
def create_2D_array(cols, rows):
    return [[0 for _ in range(rows)] for _ in range(cols)]

def update_grid(grid):
    cols, rows = len(grid), len(grid[0])
    new_grid = create_2D_array(cols, rows)
    
    for x in range(cols):
        for y in range(rows -1 , -1, -1):
            if grid[x][y] == 1:
                move_made = False
                if y < rows -1 and grid[x][y+1] == 0:
                    new_grid[x][y+1] = 1 #move the sand one down
                    move_made = True
                else:
                    # cant move down but maybe to L/R
                    directions = [-1,1]
                    random.shuffle(directions)
                    
                    for dir in directions:
                        new_x = x + dir
                        new_y = y +1
                        # is new set position valid(in grid and value 0)
                        if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_x][new_y] == 0:
                            new_grid[new_x][new_y] = 1
                            move_made = True
                            break
                # pile sand up if no other option           
                if not move_made:
                    new_grid[x][y] = 1
    return new_grid

grid = create_2D_array(cols, rows)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            gridX, gridY = mouseX // cell_size, mouseY // cell_size
            print(f"Adding sand at ({gridX}, {gridY})")
            matrix = 5
            extent = matrix // 2
            for i in range(-extent, extent +1):
                for j in range(-extent, extent +1):
                    if random.random() <0.75:
                        if 0 <= gridX + i < cols and 0 <= gridY +j < rows:
                            grid[gridX +i][gridY +j] =1
    
    grid = update_grid(grid)
                
    screen.fill((0, 0, 0))  # Clear screen
    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, sand_color, (i * cell_size, j * cell_size, cell_size, cell_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
