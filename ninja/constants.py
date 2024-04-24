import pygame

WIDTH = 1080
HEIGHT = 720
BTN_WIDTH = 50
BTN_HEIGHT = 30

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# bck image
background = pygame.image.load("./images/bg.jpg")

# startbtnimage
start_img = pygame.image.load("./images/start.png")
pause_img = pygame.image.load("./images/pause.png")
play_img = pygame.image.load("./images/play_btn.png")
quit_img = pygame.image.load("./images/quit_btn.png")
# fruits
apple_full = pygame.image.load("./images/apple_full.png")
apple_cut = pygame.image.load("./images/apple_cut.png")
bananas_full = pygame.image.load("./images/bananas_full.png")
bananas_cut = pygame.image.load("./images/bananas_cut.png")
bomb = pygame.image.load("./images/bomb.png")
orange_full = pygame.image.load("./images/orange_full.png")
orange_cut = pygame.image.load("./images/orange_cut.png")
pomegranate_full = pygame.image.load("./images/pomegranate_full.png")
pomegranate_cut = pygame.image.load("./images/pomegranate_cut.png")
watermelon_full = pygame.image.load("./images/watermelon_full.png")
watermelon_cut = pygame.image.load("./images/watermelon_cut.png")
file_loc = "./high_score.txt"

fruits = [
    [apple_full, apple_cut],
    [bananas_full, bananas_cut],
    [orange_full, orange_cut],
    [pomegranate_full, pomegranate_cut],
    [watermelon_full, watermelon_cut],
    [bomb, bomb],
]

speed_arr = [
    (1, HEIGHT),
    (1.05, HEIGHT + 30),
    (1.1, HEIGHT + 40),
    (1.125, HEIGHT + 50),
    (1.15, HEIGHT + 160),
    (1.2, HEIGHT + 150),
    (1.25, HEIGHT + 170),
]

bomb_sound = pygame.mixer.Sound("./sounds/menu-bomb.wav")
fruit_sound1 = pygame.mixer.Sound("./sounds/Impact-Apple.wav")
fruit_sound2 = pygame.mixer.Sound("./sounds/Visceral-impact-2.wav")
ui_sound = pygame.mixer.Sound("./sounds/ui-button-push.wav")
bomb_sound.set_volume(0.4)
fruit_sound1.set_volume(0.4)
fruit_sound2.set_volume(0.4)
ui_sound.set_volume(0.3)
pygame.mixer.music.load("./sounds/sound_track.mp3")
pygame.mixer.music.set_volume(0.3)
