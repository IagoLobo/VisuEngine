assets = {
  # General
  "BUTTON_CLICK_SFX": "button_click.ogg",
  "BUTTON_BACK_SFX": "button_back.ogg",
  "BODY_FONT": "Swansea.ttf",
  "SPEAKER_FONT": "Swansea.ttf",
  "FONT_SIZE_SMALL": 20,
  "FONT_SIZE_MEDIUM": 40,
  "FONT_SIZE_LARGE": 60,
  "BACK_BUTTON": "button_back_1920x1080.png",
  "BACK_BUTTON_ORIGIN": (1500, 925),
  "LOG_LIMIT": 30,
  "BLANK_BG": "black_background_1920x1080.png",
  "HEADING_ORIGIN": (750, 75),
  "DEFAULT_BGM_VOLUME": 3,
  "DEFAULT_SFX_VOLUME": 8,
  # Title screen
  "TITLE_ENGINE_IMAGE": "visu_engine_logo_text.png",
  "TITLE_ENGINE_IMAGE_ORIGIN": (100, 200),
  "TITLE_BG": "cinema_1920x1080.png",
  "TITLE_BGM": "Moar-BGM.ogg",
  "TITLE_START_BUTTON":"button_start_1920x1080.png",
  "TITLE_LOAD_BUTTON": "button_load_1920x1080.png",
  "TITLE_SETTINGS_BUTTON": "button_config_1920x1080.png",
  "TITLE_QUIT_BUTTON": "button_exit_1920x1080.png",
  "TITLE_START_BUTTON_ORIGIN": (1500, 300),
  "TITLE_LOAD_BUTTON_ORIGIN": (1500, 450),
  "TITLE_SETTINGS_BUTTON_ORIGIN": (1500, 600),
  "TITLE_QUIT_BUTTON_ORIGIN": (1500, 750),
  # Settings screen
  "SETTINGS_BG": "cinema_1920x1080.png",
  "SETTINGS_HEADING_TEXT": "CONFIGURATIONS",
  "SETTINGS_BGM_TEXT": "BGM Volume",
  "SETTINGS_SFX_TEXT": "SFX Volume",
  "SETTINGS_BGM_TEXT_ORIGIN": (475, 490),
  "SETTINGS_SFX_TEXT_ORIGIN": (475, 290),
  "SETTINGS_BGM_PLUS_BUTTON": "button_plus_1920x1080.png",
  "SETTINGS_BGM_MINUS_BUTTON": "button_minus_1920x1080.png",
  "SETTINGS_SFX_PLUS_BUTTON": "button_plus_1920x1080.png",
  "SETTINGS_SFX_MINUS_BUTTON": "button_minus_1920x1080.png",
  "SETTINGS_BGM_PLUS_BUTTON_ORIGIN": (1150, 450),
  "SETTINGS_BGM_MINUS_BUTTON_ORIGIN": (850, 450),
  "SETTINGS_SFX_PLUS_BUTTON_ORIGIN": (1150, 250),
  "SETTINGS_SFX_MINUS_BUTTON_ORIGIN": (850, 250),
  # Save and load screen
  "SAVE_HEADING_TEXT": "SAVE GAME",
  "LOAD_HEADING_TEXT": "LOAD GAME",
  "SAVE_LOAD_BG": "cinema_1920x1080.png",
  "SAVE_LOAD_PANEL": "save_panel_1920x1080.png",
  "SAVE_BUTTON": "button_save_1920x1080.png",
  "LOAD_BUTTON": "button_load_1920x1080.png",
  "SAVE_LOAD_PANEL_1_ORIGIN": (150, 150),
  "SAVE_BUTTON_1_ORIGIN": (1300, 200),
  "LOAD_BUTTON_1_ORIGIN": (1300, 200),
  "SAVE_LOAD_PANEL_2_ORIGIN": (150, 400),
  "SAVE_BUTTON_2_ORIGIN": (1300, 450),
  "LOAD_BUTTON_2_ORIGIN": (1300, 450),
  "SAVE_LOAD_PANEL_3_ORIGIN": (150, 650),
  "SAVE_BUTTON_3_ORIGIN": (1300, 700),
  "LOAD_BUTTON_3_ORIGIN": (1300, 700),
  # Game screen
  "TEXT_BOX": "text_box_1920x1080.png",
  "TEXT_BOX_ORIGIN": (0, 740),
  "SPEAKER_BOX_ORIGIN": (50, 750),
  "TEXT_BODY_ORIGIN": (50, 850),
  "TEXT_BODY_LINE_SPACING": 35,
  "TEXT_BODY_BOUNDS": 1300,
  "GAME_SAVE_BUTTON": "button_gameplay_save_1920x1080.png",
  "GAME_LOAD_BUTTON": "button_gameplay_load_1920x1080.png",
  "GAME_LOG_BUTTON": "button_gameplay_log_1920x1080.png",
  "GAME_QUIT_BUTTON": "button_gameplay_exit_1920x1080.png",
  "GAME_SAVE_BUTTON_ORIGIN": (1700, 775),
  "GAME_LOAD_BUTTON_ORIGIN": (1700, 850),
  "GAME_LOG_BUTTON_ORIGIN": (1700, 925),
  "GAME_QUIT_BUTTON_ORIGIN": (1700, 1000),
  "LOG_BOX": "log_box_1920x1080.png",
  "LOG_LINE_SPACING": 40,
  # Confirmation (Yes or no) box
  "CONFIRMATION_BOX": "confirmation_box_1920x1080.png",
  "CONFIRMATION_BOX_BUTTON_YES": "button_yes_1920x1080.png",
  "CONFIRMATION_BOX_BUTTON_NO": "button_no_1920x1080.png",
  "CONFIRMATION_BOX_TEXT": "Are you sure?",
  "CONFIRMATION_BOX_ORIGIN": (450, 400),
  "CONFIRMATION_BOX_BUTTON_YES_ORIGIN": (550, 550),
  "CONFIRMATION_BOX_BUTTON_NO_ORIGIN": (950, 550),
  # Character models
  "MODEL_FEMALE_HAPPY": "fm01_happy.png",
  "MODEL_FEMALE_TIRED": "fm01_tired.png",
  "MODEL_FEMALE_UPSET": "fm01_upset.png",
  "MODEL_MALE_HAPPY": "m01_happy.png",
  "MODEL_MALE_EMBARRASSED": "m01_embarrassed.png",
  "MODEL_MALE_WORRIED": "m01_worried.png",
  # Credits, needs one image at least
  "CREDITS_GALLERY": ["credits_1920x1080.png"],
  "CREDITS_BGM": "Again.ogg"
}

# Asset paths
SCRIPTS_PATH = 'scripts/'
SETTINGS_PATH = 'settings/'
SAVES_PATH = 'saves/'
BACKGROUND_PATH = 'backgrounds/'
MUSIC_PATH = 'sounds/music/'
SFX_PATH = 'sounds/sfx/'
SPRITE_PATH = 'sprites/'
FONT_PATH = 'fonts/'

# Resolution configurations
RESOLUTION_HD = (1280, 720)
RESOLUTION_FULLHD = (1920, 1080)
RESOLUTION_4K = (3840, 2160)

# Get resolution set by build
def getGameResolutionX():
    return RESOLUTION_FULLHD[0]

def getGameResolutionY():
    return RESOLUTION_FULLHD[1]

# Get font sizes
def getFontFileArg():
    return FONT_PATH + assets["BODY_FONT"]

def getFontSmall():
    return assets["FONT_SIZE_SMALL"]

def getFontMedium():
    return assets["FONT_SIZE_MEDIUM"]

def getFontLarge():
    return assets["FONT_SIZE_LARGE"]

# Game settings
GAME_SETTINGS = SETTINGS_PATH + "game_settings.txt"

# Save files
SAVE_FILE_1 = SAVES_PATH + "save_file_1.txt"
SAVE_FILE_2 = SAVES_PATH + "save_file_2.txt"
SAVE_FILE_3 = SAVES_PATH + "save_file_3.txt"

# Misc commands
TEXT_BOX_HIDE = "TEXT_BOX_HIDE"
TEXT_BOX_SHOW = "TEXT_BOX_SHOW"
CHAPTER = "CHAPTER"
CREDITS = "CREDITS"
BG_IMG = "BG_IMG"
SPRITE = "SPRITE"
SPRITE_REMOVE = "SPRITE_REMOVE"
MUSIC = "MUSIC"
MUSIC_STOP = "MUSIC_STOP"
SFX = "SFX"
TEXT = "TEXT"
TEXT_COLOR_PATTERN = r"\((\W|\d)+\)"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
