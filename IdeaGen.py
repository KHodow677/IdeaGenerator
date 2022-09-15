import RandomWordGen
import pygame
import os

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lightRed = (200, 0, 0)
gold = (255, 215, 0)
lightOrange = (255, 165, 0)
orange = (252, 113, 7)

window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Random Game Idea Generator")
fps = 60
clock = pygame.time.Clock()

small_font = pygame.font.SysFont("Calibri", 18)
button_font = pygame.font.SysFont("Calibri", 24)
medium_font = pygame.font.SysFont("Calibri", 50)
large_font = pygame.font.SysFont("Calibri", 60, bold=True)

def text_objects(msg, color, size="small"):
    text_surface = button_font.render(msg, True, color)
    if size == "medium":
        text_surface = medium_font.render(msg, True, color)
    elif size == "large":
        text_surface = large_font.render(msg, True, color)

    return text_surface, text_surface.get_rect()

def text(msg, color, b_x, b_y, b_length, b_height, size = "small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (b_x), (b_y)
    window.blit(text_surf, text_rect)

def button(msg, b_color, b_color_active, b_x, b_y, b_length, b_height, action="None", color_text=white):
    cursor_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if cursor_pos[0] in range(b_x, b_x + b_length) and cursor_pos[1] in range(b_y, b_y + b_height):
        pygame.draw.rect(window, b_color_active, (b_x, b_y, b_length, b_height))
        if mouse_click[0] == 1 and action != "None":
            randomGen = RandomWordGen.RandomWordGen()
            if action == "Generate":
                randomGen.Reset()
                main(randomGen.idea)
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(window, b_color, (b_x, b_y, b_length, b_height))
    text(msg, color_text, (b_x + b_length/2), (b_y + b_height/2), b_length, b_height)

def main(idea = ""):
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(gold)
        text("Idea Generator", black, 200, 50, 120, 50, "medium")

        button("Generate", orange, lightOrange, 60, 200, 120, 50, "Generate")
        button("Quit", lightRed, red, 210, 200, 120, 50, "Quit")

        text(idea, black, 200, 130, 120, 50)

        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

