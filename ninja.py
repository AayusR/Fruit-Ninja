import pygame
import random
import math
import time

pygame.init()
pygame.mixer.init()
# constants
from ninja.constants import *
from ninja.Button import Button



# pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("FRUIT NINJA")
start_btn = Button(start_img, 400, 300, False, screen)

pygame.mixer.music.play(-1)

# game variables
score = 0
lives = 5
level = 1
paused = True
new_level = True
current_score = 0
game_over = False
label_no = 0

letter_objects = []
input_letter = ""
text_font = pygame.font.Font("./AldotheApache.ttf", 50)
high_score_file = open(file_loc, "r")
read = high_score_file.readlines()
highscore = int(read[0])
high_score_file.close()


def drawText(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    screen.blit(img, (x, y))


def draw_screen():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, "white", [0, 0, WIDTH, HEIGHT], 5)
    drawText(f"Score: {score}", text_font, "black", 30, HEIGHT - 700)
    drawText(f"LIVE {lives}", text_font, "black", WIDTH // 2 - 160, HEIGHT - 700)
    drawText(f"BEST {highscore}", text_font, "black", WIDTH // 2 + 100, HEIGHT - 700)
    pause_btn = Button(pause_img, WIDTH - 100, HEIGHT - 720, False, screen)
    pause_btn.draw()
    return pause_btn.clicked

def draw_pause():
    surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(
        surf, (0, 0, 0, 100), [(WIDTH - 600) / 2, (HEIGHT - 300) / 2, 600, 300], 0, 5
    )
    pygame.draw.rect(
        surf, (0, 0, 0, 200), [(WIDTH - 600) / 2, (HEIGHT - 300) / 2, 600, 300], 5, 5
    )
    # define btns
    resume_btn = Button(
        play_img, (WIDTH - 600) / 2 + 50, (HEIGHT - 300) / 2 + 50, False, surf
    )
    resume_btn.draw()
    quit_btn = Button(
        quit_img, (WIDTH - 600) / 2 + 350, (HEIGHT - 300) / 2 + 50, False, surf
    )
    quit_btn.draw()
    surf.blit(
        text_font.render("Play", True, "white"),
        ((WIDTH - 600) / 2 + 180, (HEIGHT - 300) / 2 + 75),
    )

    surf.blit(
        text_font.render("Quit", True, "white"),
        ((WIDTH - 600) / 2 + 480, (HEIGHT - 300) / 2 + 75),
    )
    surf.blit(
        text_font.render(f"Score: {current_score}", True, "white"),
        ((WIDTH - 600) / 2 + 20, (HEIGHT - 300) / 2 + 200),
    )
    surf.blit(
        text_font.render(f"HighScore: {highscore}", True, "white"),
        ((WIDTH - 600) / 2 + 250, (HEIGHT - 300) / 2 + 200),
    )

    screen.blit(surf, (0, 0))
    return resume_btn.clicked, quit_btn.clicked


def check_highscore():
    global highscore, score
    if score > highscore:
        highscore = score
        file = open(file_loc, "w")
        file.write(str(int(highscore)))
        file.close()


class Letter:
    def __init__(self, letter, speed, x_pos, y_pos, fruit, isBomb):
        self.x_pos = x_pos
        self.speed = speed
        self.letter = letter
        self.y_pos = y_pos
        self.wid = x_pos
        self.angle = 80 * 3.14 / 180
        self.time = 0
        self.gravity = 0.03999
        self.isBomb = isBomb
        self.fruit_img_full = fruit[0]
        self.fruit_img_cut = fruit[1]
        self.surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.pressed = False
        self.scored = False
        if self.y_pos >= HEIGHT + 150:
            self.angle = 90 * 3.14 / 180

    def draw(self):
        if self.pressed:
            self.remove()
        else:
            screen.blit(self.fruit_img_full, (self.x_pos - 60, self.y_pos - 60))
            screen.blit(
                text_font.render(self.letter, True, "white"), (self.x_pos, self.y_pos)
            )

    def remove(self):
        
        screen.blit(self.fruit_img_cut, (self.x_pos - 60, self.y_pos - 60))
        screen.blit(
            text_font.render(self.letter, True, "green"),
            (self.x_pos, self.y_pos),
        )

    def update(self):
        # Calculate the new x and y positions
        if self.wid > WIDTH / 2:
            self.x_pos = self.x_pos - self.speed * math.cos(self.angle) * self.time
        else:
            self.x_pos = self.x_pos + self.speed * math.cos(self.angle) * self.time

        self.y_pos = self.y_pos - (
            self.speed * math.sin(self.angle) * self.time
            - 0.5 * self.gravity * self.time**2
        )
        # Increase the time
        self.time += 1


def generate_levels():
    global input_letter
    input_letter = ''
    letter_objs = []
    letter_copy = letters.copy()
    horizontal_spacing = (WIDTH - 150) // level

    for i in range(level):
        speed_tup = random.choice(speed_arr)
        x_pos = random.randint(
            10 + (i * horizontal_spacing), (i + 1) * horizontal_spacing
        )
        speed = speed_tup[0]
        y_pos = speed_tup[1]
        letter = random.choice(letter_copy)
        letter_copy.remove(letter)

        fruit = random.choice(fruits)
        if fruit[0] == fruit[1]:
            isBomb = True
        else:
            isBomb = False
        new_letter = Letter(letter, speed, x_pos, y_pos, fruit, isBomb)
        letter_objs.append(new_letter)
    return letter_objs


def main():
    global new_level, paused, lives, level, input_letter, letter_objects, score, current_score, game_over, label_no

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill("white")
        screen.blit(background, (0, 0))
        pausebtn_status = draw_screen()
        if paused and game_over:
            game_over = False
        if paused:
            resume_btt, quit_butt = draw_pause()
            if resume_btt:
                ui_sound.play()
                paused = False
            if quit_butt:
                ui_sound.play()
                check_highscore()
                running = False
        if new_level and not paused:
            letter_objects = generate_levels()
            new_level = False
        else:
            for l in letter_objects:
                l.draw()
                if not paused:
                    l.update()
                if l.y_pos >= HEIGHT + 200:
                    if not l.pressed and not l.isBomb:
                        score -= 1
                        label_no += 1
                        if score <=0:
                            score = 0
                    
                    letter_objects.remove(l)

                    

        if len(letter_objects) <= 0 and not paused:
            input_letter = ""
            if label_no == 0:
                level += 1
            label_no = 0
            if level >= 4:
                level = 4
            new_level = True

        for l in letter_objects:
            if l.letter == input_letter and not l.scored:
                input_letter = ""
                if not l.isBomb:
                    score += level
                    fruit_sound1.play()
                else:
                    bomb_sound.play()
                    lives -= 1
                l.pressed = True
                l.scored = True
                # /1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check_highscore()
                running = False

            if event.type == pygame.KEYDOWN:
                if not paused:
                    if event.unicode.lower() in letters:
                        input_letter = event.unicode.lower()

                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if paused:
                        paused = False
                        ui_sound.play()
                    else:
                        paused = True
                        ui_sound.play()
        if pausebtn_status:
            paused = True
        if lives <= 0:
            game_over = True
            paused = True
            input_letter = ""
            lives = 5
            level = 1
            letter_objects = []
            new_level = True
            check_highscore()
            current_score = score
            score = 0
        if paused:
            draw_pause()
        clock.tick(60)
        pygame.display.update()
    pygame.quit()


main()
