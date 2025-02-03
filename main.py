import pygame, sys, os, random
from button import Button

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sing Till the End")

BG = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

red_x = pygame.image.load("assets/red_x.png")
red_x = pygame.transform.scale(red_x, (red_x.get_width()/8, red_x.get_height()/8))

TITLE_FONT = 70
LYRIC_FONT = 50

songs = {0 : "This is Amazing Grace",
         1 : "Goodness of God",
         2 : "Found in You",
         3 : "Trust in God",
         4 : "What a Beautiful Name",
         5 : "Holy Forever"}

completed = {0 : False,
             1 : False,
             2 : False,
             3 : False,
             4 : False,
             5 : False}


row_height = LYRIC_FONT + 5  # Space between rows
num_rows = HEIGHT // row_height
num_cols = WIDTH // 150  # Approximate width of text space per column

occupied_rects = []

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def get_font_song(size):
    return pygame.font.SysFont("Arial", size)


def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("black")

        play_text = get_font(45).render("Choose a song", True, "White")
        play_rect = play_text.get_rect(center=(WIDTH / 2, 60))
        SCREEN.blit(play_text, play_rect)

        song1 = Button(image=None, pos=(WIDTH / 2, 160),
                       text_input="This is Amazing Grace", font=get_font(55), base_color="White",
                       hovering_color="Green")

        song2 = Button(image=None, pos=(WIDTH / 2, 260),
                       text_input="Goodness of God", font=get_font(55), base_color="White", hovering_color="Green")

        song3 = Button(image=None, pos=(WIDTH / 2, 360),
                       text_input="Found in You", font=get_font(55), base_color="White", hovering_color="Green")

        song4 = Button(image=None, pos=(WIDTH / 2, 460),
                       text_input="Trust in God", font=get_font(55), base_color="White", hovering_color="Green")

        song5 = Button(image=None, pos=(WIDTH / 2, 560),
                       text_input="What a Beautiful Name", font=get_font(55), base_color="White",
                       hovering_color="Green")

        song6 = Button(image=None, pos=(WIDTH / 2, 660),
                       text_input="Holy Forever", font=get_font(55), base_color="White",
                       hovering_color="Green")

        play_back = Button(image=None, pos=(WIDTH / 2, 760),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        song1.change_color(play_mouse_pos)
        song1.update(SCREEN)
        song2.change_color(play_mouse_pos)
        song2.update(SCREEN)
        song3.change_color(play_mouse_pos)
        song3.update(SCREEN)
        song4.change_color(play_mouse_pos)
        song4.update(SCREEN)
        song5.change_color(play_mouse_pos)
        song5.update(SCREEN)
        song6.change_color(play_mouse_pos)
        song6.update(SCREEN)
        play_back.change_color(play_mouse_pos)
        play_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.check_for_input(play_mouse_pos):
                    main_menu()
                elif song1.check_for_input(play_mouse_pos):
                    song_screen(0)
                elif song2.check_for_input(play_mouse_pos):
                    song_screen(1)
                elif song3.check_for_input(play_mouse_pos):
                    song_screen(2)
                elif song4.check_for_input(play_mouse_pos):
                    song_screen(3)
                elif song5.check_for_input(play_mouse_pos):
                    song_screen(4)
                elif song6.check_for_input(play_mouse_pos):
                    song_screen(5)

        pygame.display.update()


def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("white")

        options_text = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        options_rect = options_text.get_rect(center=(WIDTH / 2, 260))
        SCREEN.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(WIDTH / 2, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        options_back.change_color(options_mouse_pos)
        options_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.check_for_input(options_mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("SING IT!", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(WIDTH / 2, 200))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH / 2, 350),
                             text_input="SONG", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(WIDTH / 2, 500),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(WIDTH / 2, 650),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if options_button.check_for_input(menu_mouse_pos):
                    options()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def song_screen(key):
    song_name = songs.get(key)

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("black")

        play_text = get_font(TITLE_FONT).render(song_name, True, "White")
        play_rect = play_text.get_rect(center=(WIDTH / 2, 260))
        SCREEN.blit(play_text, play_rect)

        if completed.get(key):
            base_color = "Dim Gray"
            hovering_color = "Dark Green"
        else:
            base_color = "White"
            hovering_color = "Green"

        play_start = Button(image=None, pos=(WIDTH / 2, 430),
                            text_input="START", font=get_font(75), base_color=base_color, hovering_color=hovering_color)

        play_back = Button(image=None, pos=(WIDTH / 2, 530),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        play_start.change_color(play_mouse_pos)
        play_start.update(SCREEN)
        play_back.change_color(play_mouse_pos)
        play_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.check_for_input(play_mouse_pos):
                    play()
                elif play_start.check_for_input(play_mouse_pos):
                    if not completed.get(key):
                        lyric_screen(key, song_name)

        pygame.display.update()


def lyric_screen(key, song_name):
    fail = False
    SCREEN.fill("black")
    correct = 0

    with open("lyrics/" + song_name + ".txt", "r") as file:
        lines = file.read().splitlines()
    file.close()

    render_text(lines)
    pygame.display.flip()

    pygame.mixer.music.load("mr/" + song_name + ".mp3")
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    correct += 1
                if event.key == pygame.K_LEFT:
                    song_screen(key)
                if event.key == pygame.K_UP:
                    completed[key] = True
                    pygame.mixer.music.fadeout(4000)
                if event.key == pygame.K_DOWN:
                    fail = True

        sing_it(lines, correct)

        if fail:
            SCREEN.blit(red_x, (20, 20))

        pygame.display.update()


def get_non_overlapping_position(text_surface):
    """Finds a valid random position where text does not overlap."""
    max_attempts = 100
    text_width, text_height = text_surface.get_size()

    for _ in range(max_attempts):
        x = random.randint(0, WIDTH - text_width)
        y = random.randint(0, HEIGHT - text_height)
        text_rect = pygame.Rect(x, y, text_width, text_height)

        # Check if it collides with any previously placed text
        if not any(text_rect.colliderect(rect) for rect in occupied_rects):
            occupied_rects.append(text_rect)  # Store the occupied space
            return x, y

    return None  # No valid space found (unlikely)


def render_text(lines):
    """Render text using available positions without overlap."""
    occupied_rects.clear()  # Reset on each frame

    for line in lines:
        text_surface = get_font_song(LYRIC_FONT).render(line.rstrip(), True, "White")
        position = get_non_overlapping_position(text_surface)
        if position:
            SCREEN.blit(text_surface, position)


def sing_it(lines, correct):
    SCREEN.fill("black")

    for i in range(len(lines)):
        if i+correct < len(lines):
            text_surface = get_font_song(LYRIC_FONT).render(lines[i+correct].rstrip(), True, "White")
            position = occupied_rects[i+correct]
            SCREEN.blit(text_surface, position)


if __name__ == '__main__':
    main_menu()