import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 626
SCREEN_HEIGHT = 434
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

# Load assets
bg_main_menu = pygame.image.load(os.path.join('final.jpeg'))
bg_airpollution = pygame.image.load(os.path.join('airpollution.jpeg'))
bg_waterpollution = pygame.image.load(os.path.join('waterpollution.jpeg'))
bg_radioactive = pygame.image.load(os.path.join('radio-active.jpeg'))
bg_deforestation = pygame.image.load(os.path.join('deforstation.jpeg'))

player_sprites = [
    pygame.image.load(os.path.join('boyr1.png')),
    pygame.image.load(os.path.join('boyr2.png')),
    pygame.image.load(os.path.join('boyr3.png')),
    pygame.image.load(os.path.join('boyr4.png'))
]

boss_sprite_stage1 = pygame.image.load(os.path.join('lugia2.png'))
boss_sprite_stage2 = pygame.image.load(os.path.join('articuno2.png'))
boss_sprite_stage3 = pygame.image.load(os.path.join('skarmory2.png'))
boss_sprite_stage4 = pygame.image.load(os.path.join('rayquaza2.png'))

pygame.mixer.music.load(os.path.join('music.mp3'))
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Environmental Boss Fight")

font = pygame.font.Font(pygame.font.get_default_font(), 16)  # Decreased font size

class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                    self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

questions_stage1 = [
    Question("What is the largest source of air pollution in urban areas?", 
             ["Industrial emissions", "Transportation", "Residential heating", "Natural sources"], 1),
    Question("Which health issue is commonly associated with air pollution?", 
             ["Asthma", "Diabetes", "Osteoporosis", "Skin cancer"], 0),
    Question("The Clean Air Act is a law aimed at:", 
             ["Reducing water pollution", "Protecting biodiversity", "Regulating air quality", "Controlling waste management"], 2),
    Question("What does a high AQI indicate?", 
             ["Good air quality", "Moderate air quality", "Unhealthy air quality", "Very low pollution levels"], 2),
    Question("What is a potential impact of air pollution on wildlife?", 
             ["Habitat loss", "Reduced reproduction", "Increased disease susceptibility", "All of the above"], 3)
]

questions_stage2 = [
    Question("Which of the following is a primary source of water pollution?", 
             ["Agricultural runoff", "Industrial discharges", "Wastewater from households", "All of the above"], 3),
    Question("Which heavy metal is most commonly associated with water pollution?", 
             ["Sodium", "Lead", "Calcium", "Potassium"], 1),
    Question("Which practice can help reduce water pollution?", 
             ["Over-fertilizing crops", "Proper waste disposal", "Using single-use plastics", "Ignoring industrial waste regulations"], 1),
    Question("What is the primary cause of ocean acidification?", 
             ["Increased CO2 levels", "Oil spills", "Plastic pollution", "Heavy metal runoff"], 0),
    Question("Which of the following is a non-point source of water pollution?", 
             ["Factory discharge", "Sewage plant", "Agricultural runoff", "Landfill leachate"], 2)
]

questions_stage3 = [
    Question("What is the primary source of radioactive pollution?", 
             ["Industrial waste", "Nuclear power plants", "Agricultural chemicals", "Urban runoff"], 1),
    Question("Which isotope is commonly associated with radioactive waste?", 
             ["Carbon-14", "Uranium-238", "Oxygen-16", "Hydrogen-1"], 1),
    Question("What is the process of radioactive decay?", 
             ["Fusion", "Fission", "Radioactive decay", "Transmutation"], 2),
    Question("What is a major health risk associated with radioactive materials?", 
             ["Skin irritation", "Radiation sickness", "Allergic reactions", "Gastrointestinal issues"], 1),
    Question("Which event is most linked to radioactive pollution?", 
             ["Chernobyl disaster", "Bhopal tragedy", "Love Canal incident", "Exxon Valdez spill"], 0)
]

questions_stage4 = [
    Question("What is the primary cause of deforestation globally?", 
             ["Urbanization", "Agriculture", "Mining", "All of the above"], 3),
    Question("Which ecosystem is most affected by deforestation?", 
             ["Tundra", "Grassland", "Rainforest", "Desert"], 2),
    Question("Which is a direct consequence of deforestation?", 
             ["Increase in biodiversity", "Soil erosion", "Improved air quality", "Enhanced carbon sequestration"], 1),
    Question("What role do forests play in regulating the Earth's climate?", 
             ["Absorb CO2", "Increase surface temperatures", "Emit greenhouse gases", "Decrease precipitation"], 0),
    Question("Which practice can help combat deforestation?", 
             ["Slash-and-burn", "Reforestation", "Urban sprawl", "Monoculture farming"], 1)
]

def draw_health(health, x, y):
    for i in range(health):
        pygame.draw.rect(screen, RED, (x + i * 20, y, 15, 15))

def main_menu():
    play_button = Button(200, 150, 100, 50, "Play", WHITE)
    quit_button = Button(350, 150, 100, 50, "Quit", WHITE)

    menu_running = True
    while menu_running:
        screen.fill(WHITE)
        screen.blit(bg_main_menu, (0, 0))
        
        play_button.draw(screen)
        quit_button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(event.pos):
                    game_loop(1)
                if quit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

def game_over():
    game_over_running = True
    while game_over_running:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to restart the game
                    game_loop(1)  # Restart from stage 1
        
        pygame.time.wait(200)

def display_congrats():
    congrats_running = True
    while congrats_running:
        screen.fill(WHITE)
        congrats_text = font.render("Congratulations! You've completed all stages!", True, BLACK)
        menu_text = font.render("Press Enter to return to the main menu.", True, BLACK)
        
        screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to go back to main menu
                    main_menu()
                    congrats_running = False
        
        pygame.time.wait(200)

def game_loop(stage):
    clock = pygame.time.Clock()
    
    player_x = 50
    player_y = 300  # Player position at y = 300
    player_index = 0
    player_health = 3
    boss_health = 5

    question_index = 0
    current_question = None

    if stage == 1:
        questions = questions_stage1
        boss_sprite = boss_sprite_stage1
        background_image = bg_airpollution
    elif stage == 2:
        questions = questions_stage2
        boss_sprite = boss_sprite_stage2
        background_image = bg_waterpollution
    elif stage == 3:
        questions = questions_stage3
        boss_sprite = boss_sprite_stage3
        background_image = bg_radioactive
    elif stage == 4:
        questions = questions_stage4
        boss_sprite = boss_sprite_stage4
        background_image = bg_deforestation

    current_question = questions[question_index]

    stage_running = True
    while stage_running:
        clock.tick(FPS)
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))  # Draw background for the current stage

        # Animate player sprite
        player_index = (player_index + 1) % len(player_sprites)

        # Check if the player health or boss health has dropped to zero
        if player_health <= 0:
            game_over()
            stage_running = False

        if boss_health <= 0:
            question_index += 1  # Move to the next question
            if question_index < len(questions):
                current_question = questions[question_index]
                boss_health = 5  # Reset boss health for the next question
            else:
                # All stages completed; show congrats message
                display_congrats()
                stage_running = False
                continue  # Skip the rest of the loop to avoid drawing

        # Draw player and boss
        player_sprite = player_sprites[player_index]
        screen.blit(player_sprite, (player_x, player_y))
        screen.blit(boss_sprite, (SCREEN_WIDTH - 200, 300))  # Boss y position at 300

        # Draw health bars under sprites
        draw_health(player_health, player_x, 400)  # Health bar y position at 400
        draw_health(boss_health, SCREEN_WIDTH - 200, 400)  # Boss health bar y position at 400

        question_text = font.render(current_question.question, True, BLACK)
        screen.blit(question_text, (50, 20))

        option_buttons = []
        for i, option in enumerate(current_question.options):
            button = Button(50, 70 + i * 50, 500, 40, option, WHITE)
            button.draw(screen)
            option_buttons.append(button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, option_button in enumerate(option_buttons):
                    if option_button.is_clicked(event.pos):
                        if i == current_question.correct_answer:
                            boss_health -= 1
                            question_index += 1
                            if question_index < len(questions):
                                current_question = questions[question_index]
                            else:
                                # Proceed to the next stage immediately
                                stage += 1
                                if stage <= 4:
                                    game_loop(stage)  # Start the next stage
                                else:
                                    # Game completed; show congrats message
                                    display_congrats()
                                    stage_running = False
                        else:
                            # Wrong answer, decrease health and redisplay the question
                            player_health -= 1
                            current_question = current_question  # Keep the same question

        pygame.display.update()

main_menu()
