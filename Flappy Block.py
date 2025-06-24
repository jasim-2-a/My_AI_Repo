import os, requests, pygame, random, sys

# === Download upgraded assets ===
ASSETS = {
    "bird.png": "https://raw.githubusercontent.com/samuelcust/flappy-bird-assets/master/sprites/yellowbird-midflap.png",
    "pipe.png": "https://raw.githubusercontent.com/samuelcust/flappy-bird-assets/master/sprites/pipe-green.png",
    "bg.png":   "https://raw.githubusercontent.com/samuelcust/flappy-bird-assets/master/sprites/background-day.png",
    "base.png": "https://raw.githubusercontent.com/samuelcust/flappy-bird-assets/master/sprites/base.png",
    "wing.wav": "https://raw.githubusercontent.com/samuelcust/flappy-bird-assets/master/audio/wing.wav"
}
for name, url in ASSETS.items():
    if not os.path.exists(name):
        with requests.get(url) as r:
            open(name, "wb").write(r.content)

# === Pygame setup ===
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Block – Upgraded")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# === Load assets ===
BIRD = pygame.image.load("bird.png").convert_alpha()
PIPE = pygame.image.load("pipe.png").convert_alpha()
BG = pygame.image.load("bg.png").convert()
BASE = pygame.image.load("base.png").convert()
FLAP = pygame.mixer.Sound("wing.wav")

# Scale to fit
BIRD = pygame.transform.scale(BIRD, (34, 24))
PIPE = pygame.transform.scale(PIPE, (52, 320))
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
BASE = pygame.transform.scale(BASE, (WIDTH, 100))

# Constants
GRAVITY = 0.5; FLAP_STRENGTH = -9; GAP = 150
FPS = 60; WHITE = (255, 255, 255); LIGHT_BLUE = (173, 216, 230)

# Button helpers (same as before)...

def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, LIGHT_BLUE, rect, border_radius=10)
    label = font.render(text, True, (0,0,0))
    screen.blit(label, (x + w//2 - label.get_width()//2, y + h//2 - label.get_height()//2))
    return rect

def wait_for_click(buttons):
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
        mouse = pygame.mouse.get_pos(); click = pygame.mouse.get_pressed()[0]
        for name, rect in buttons.items():
            if rect.collidepoint(mouse) and click:
                return name
        pygame.display.update()
        clock.tick(FPS)

# Screens (unchanged)...

def start_screen():
    while True:
        screen.blit(BG, (0, 0))
        title = font.render("Flappy Block", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        start_btn = draw_button("Start", WIDTH//2 - 70, 300, 140, 60)
        screen.blit(BASE, (0, HEIGHT-100))
        if wait_for_click({"start": start_btn})=="start":
            return

def game_over_screen(score):
    while True:
        screen.blit(BG, (0, 0))
        msg = font.render("Game Over", True, WHITE)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 150))
        score_text = font.render(f"Score: {int(score)}", True, WHITE)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 220))
        retry_btn = draw_button("Retry", WIDTH//2 -100, 300, 90, 50)
        quit_btn = draw_button("Quit", WIDTH//2 +10, 300, 90, 50)
        screen.blit(BASE, (0, HEIGHT-100))
        return wait_for_click({"retry": retry_btn, "quit": quit_btn})

# Game logic (unchanged)...

def run_game():
    bx, by = 60, HEIGHT//2; vel = 0; pipes = []; last_pipe = pygame.time.get_ticks(); score = 0
    base_x = 0; base_speed = 2

    while True:
        clock.tick(FPS)
        screen.blit(BG, (0,0))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                vel = FLAP_STRENGTH; FLAP.play()
        vel += GRAVITY; by += vel
        bird_rect = BIRD.get_rect(center=(bx, by))
        screen.blit(BIRD, bird_rect)

        now = pygame.time.get_ticks()
        if now - last_pipe > 1500:
            y = random.randint(100,400)
            top = PIPE.get_rect(midbottom=(WIDTH+50, y-GAP//2))
            bottom = PIPE.get_rect(midtop=(WIDTH+50, y+GAP//2))
            pipes += [top, bottom]; last_pipe = now

        for p in pipes:
            p.centerx -= 3
            img = PIPE if p.bottom>=HEIGHT else pygame.transform.flip(PIPE, False, True)
            screen.blit(img, p)
        pipes = [p for p in pipes if p.right>0]

        for p in pipes:
            if p.centerx==bx: score += 0.5

        if bird_rect.top<=0 or bird_rect.bottom>=HEIGHT-100 or any(bird_rect.colliderect(p) for p in pipes):
            return score

        base_x -= base_speed
        if base_x<=-WIDTH: base_x = 0
        screen.blit(BASE, (base_x, HEIGHT-100))
        screen.blit(BASE, (base_x+WIDTH, HEIGHT-100))

        screen.blit(font.render(str(int(score)), True, WHITE), (WIDTH//2 -10, 10))
        pygame.display.update()

# Main loop
while True:
    start_screen()
    s = run_game()
    choice = game_over_screen(s)
    if choice=="quit":
        pygame.quit(); sys.exit()
