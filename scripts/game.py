import story as s
import config as c
import pygame
import math
import ast
from datetime import datetime
import os.path
from os import path
import re
from pygame import mixer
from enum import Enum

pygame.init()
clock = pygame.time.Clock()

story = s.getStory()

screen = pygame.display.set_mode((c.getGameResolutionX(), c.getGameResolutionY()))

pygame.display.set_caption("Visu Engine")
ICON = pygame.image.load(c.SPRITE_PATH + "program_icon_visu_engine.png")
pygame.display.set_icon(ICON)

# Determine game states
class State:
  TITLE = 0
  LOAD = 1
  SAVE = 2
  LOG = 3
  GAME = 4
  SETTINGS = 5
  CREDITS = 6

#region Set Constants
BACK_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["BACK_BUTTON"]).convert_alpha()
BACK_BUTTON_ORIGIN = c.assets["BACK_BUTTON_ORIGIN"]

BODY_FONT_SMALL = pygame.font.Font(c.getFontFileArg(), c.getFontSmall())
BODY_FONT_MEDIUM = pygame.font.Font(c.getFontFileArg(), c.getFontMedium())
BODY_FONT_LARGE = pygame.font.Font(c.getFontFileArg(), c.getFontLarge())

SPEAKER_FONT = pygame.font.Font(c.FONT_PATH + c.assets["SPEAKER_FONT"], c.assets["FONT_SIZE_MEDIUM"])
LOG_LIMIT = c.assets["LOG_LIMIT"]
BLANK_BG_FILE = c.assets["BLANK_BG"]
HEADING_ORIGIN = c.assets["HEADING_ORIGIN"]

DEFAULT_BGM_VOLUME = c.assets["DEFAULT_BGM_VOLUME"]
DEFAULT_SFX_VOLUME = c.assets["DEFAULT_SFX_VOLUME"]

TITLE_BACKGROUND = pygame.image.load(c.BACKGROUND_PATH + c.assets["TITLE_BG"])
TITLE_ENGINE_IMAGE = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_ENGINE_IMAGE"])
TITLE_START_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_START_BUTTON"]).convert_alpha()
TITLE_LOAD_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_LOAD_BUTTON"]).convert_alpha()
TITLE_SETTINGS_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_SETTINGS_BUTTON"]).convert_alpha()
TITLE_QUIT_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_QUIT_BUTTON"]).convert_alpha()
TITLE_BGM = c.MUSIC_PATH + c.assets["TITLE_BGM"]
TITLE_ENGINE_IMAGE_ORIGIN = c.assets["TITLE_ENGINE_IMAGE_ORIGIN"]
TITLE_START_BUTTON_ORIGIN = c.assets["TITLE_START_BUTTON_ORIGIN"]
TITLE_LOAD_BUTTON_ORIGIN = c.assets["TITLE_LOAD_BUTTON_ORIGIN"]
TITLE_SETTINGS_BUTTON_ORIGIN = c.assets["TITLE_SETTINGS_BUTTON_ORIGIN"]
TITLE_QUIT_BUTTON_ORIGIN = c.assets["TITLE_QUIT_BUTTON_ORIGIN"]

TEXT_BOX = pygame.image.load(c.SPRITE_PATH + c.assets["TEXT_BOX"]).convert_alpha()
TEXT_BOX_ORIGIN = c.assets["TEXT_BOX_ORIGIN"]
TEXT_BODY_ORIGIN = c.assets["TEXT_BODY_ORIGIN"]
TEXT_BODY_BOUNDS = c.assets["TEXT_BODY_BOUNDS"]
TEXT_BODY_LINE_SPACING = c.assets["TEXT_BODY_LINE_SPACING"]

SPEAKER_BOX_ORIGIN = c.assets["SPEAKER_BOX_ORIGIN"]

GAME_SAVE_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_SAVE_BUTTON"]).convert_alpha()
GAME_LOAD_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_LOAD_BUTTON"]).convert_alpha()
GAME_LOG_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_LOG_BUTTON"]).convert_alpha()
GAME_QUIT_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_QUIT_BUTTON"]).convert_alpha()
GAME_SAVE_BUTTON_ORIGIN = c.assets["GAME_SAVE_BUTTON_ORIGIN"]
GAME_LOAD_BUTTON_ORIGIN = c.assets["GAME_LOAD_BUTTON_ORIGIN"]
GAME_LOG_BUTTON_ORIGIN = c.assets["GAME_LOG_BUTTON_ORIGIN"]
GAME_QUIT_BUTTON_ORIGIN = c.assets["GAME_QUIT_BUTTON_ORIGIN"]

SAVE_LOAD_BG = pygame.image.load(c.BACKGROUND_PATH + c.assets["SAVE_LOAD_BG"])

SAVE_HEADING_TEXT = c.assets["SAVE_HEADING_TEXT"]
LOAD_HEADING_TEXT = c.assets["LOAD_HEADING_TEXT"]

SAVE_LOAD_PANEL = pygame.image.load(c.SPRITE_PATH + c.assets["SAVE_LOAD_PANEL"]).convert_alpha()
SAVE_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["SAVE_BUTTON"]).convert_alpha()
LOAD_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["LOAD_BUTTON"]).convert_alpha()

SAVE_LOAD_PANEL_1_ORIGIN = c.assets["SAVE_LOAD_PANEL_1_ORIGIN"]
SAVE_BUTTON_1_ORIGIN = c.assets["SAVE_BUTTON_1_ORIGIN"]
LOAD_BUTTON_1_ORIGIN = c.assets["LOAD_BUTTON_1_ORIGIN"]

SAVE_LOAD_PANEL_2_ORIGIN = c.assets["SAVE_LOAD_PANEL_2_ORIGIN"]
SAVE_BUTTON_2_ORIGIN = c.assets["SAVE_BUTTON_2_ORIGIN"]
LOAD_BUTTON_2_ORIGIN = c.assets["LOAD_BUTTON_2_ORIGIN"]

SAVE_LOAD_PANEL_3_ORIGIN = c.assets["SAVE_LOAD_PANEL_3_ORIGIN"]
SAVE_BUTTON_3_ORIGIN = c.assets["SAVE_BUTTON_3_ORIGIN"]
LOAD_BUTTON_3_ORIGIN = c.assets["LOAD_BUTTON_3_ORIGIN"]

LOG_BOX = pygame.image.load(c.SPRITE_PATH + c.assets["LOG_BOX"])
LOG_LINE_SPACING = c.assets["LOG_LINE_SPACING"]

CREDITS_GALLERY = c.assets["CREDITS_GALLERY"]
CREDITS_BGM = c.assets["CREDITS_BGM"]

CONFIRMATION_BOX = pygame.image.load(c.SPRITE_PATH + c.assets["CONFIRMATION_BOX"]).convert_alpha()
CONFIRMATION_BOX_BUTTON_YES = pygame.image.load(c.SPRITE_PATH + c.assets["CONFIRMATION_BOX_BUTTON_YES"]).convert_alpha()
CONFIRMATION_BOX_BUTTON_NO = pygame.image.load(c.SPRITE_PATH + c.assets["CONFIRMATION_BOX_BUTTON_NO"]).convert_alpha()
CONFIRMATION_BOX_TEXT = c.assets["CONFIRMATION_BOX_TEXT"]
CONFIRMATION_BOX_ORIGIN = c.assets["CONFIRMATION_BOX_ORIGIN"]
CONFIRMATION_BOX_BUTTON_YES_ORIGIN = c.assets["CONFIRMATION_BOX_BUTTON_YES_ORIGIN"]
CONFIRMATION_BOX_BUTTON_NO_ORIGIN = c.assets["CONFIRMATION_BOX_BUTTON_NO_ORIGIN"]

SETTINGS_BG = pygame.image.load(c.BACKGROUND_PATH + c.assets["SETTINGS_BG"])
SETTINGS_BGM_PLUS_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_PLUS_BUTTON"]).convert_alpha()
SETTINGS_BGM_MINUS_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_MINUS_BUTTON"]).convert_alpha()
SETTINGS_SFX_PLUS_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_PLUS_BUTTON"]).convert_alpha()
SETTINGS_SFX_MINUS_BUTTON = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_MINUS_BUTTON"]).convert_alpha()
SETTINGS_BGM_PLUS_BUTTON_ORIGIN = c.assets["SETTINGS_BGM_PLUS_BUTTON_ORIGIN"]
SETTINGS_BGM_MINUS_BUTTON_ORIGIN = c.assets["SETTINGS_BGM_MINUS_BUTTON_ORIGIN"]
SETTINGS_SFX_PLUS_BUTTON_ORIGIN = c.assets["SETTINGS_SFX_PLUS_BUTTON_ORIGIN"]
SETTINGS_SFX_MINUS_BUTTON_ORIGIN = c.assets["SETTINGS_SFX_MINUS_BUTTON_ORIGIN"]

SETTINGS_HEADING_TEXT = c.assets["SETTINGS_HEADING_TEXT"]
SETTINGS_BGM_TEXT = c.assets["SETTINGS_BGM_TEXT"]
SETTINGS_SFX_TEXT = c.assets["SETTINGS_SFX_TEXT"]
SETTINGS_BGM_TEXT_ORIGIN = c.assets["SETTINGS_BGM_TEXT_ORIGIN"]
SETTINGS_SFX_TEXT_ORIGIN = c.assets["SETTINGS_SFX_TEXT_ORIGIN"]

BACK_BUTTON_RECT = BACK_BUTTON.get_rect(topleft=c.assets["BACK_BUTTON_ORIGIN"])
CONFIRMATION_BOX_BUTTON_YES_RECT = CONFIRMATION_BOX_BUTTON_YES.get_rect(topleft=c.assets["CONFIRMATION_BOX_BUTTON_YES_ORIGIN"])
CONFIRMATION_BOX_BUTTON_NO_RECT = CONFIRMATION_BOX_BUTTON_NO.get_rect(topleft=c.assets["CONFIRMATION_BOX_BUTTON_NO_ORIGIN"])

TITLE_START_BUTTON_RECT = TITLE_START_BUTTON.get_rect(topleft=TITLE_START_BUTTON_ORIGIN)
TITLE_LOAD_BUTTON_RECT = TITLE_LOAD_BUTTON.get_rect(topleft=TITLE_LOAD_BUTTON_ORIGIN)
TITLE_SETTINGS_BUTTON_RECT = TITLE_SETTINGS_BUTTON.get_rect(topleft=TITLE_SETTINGS_BUTTON_ORIGIN)
TITLE_QUIT_BUTTON_RECT = TITLE_QUIT_BUTTON.get_rect(topleft=TITLE_QUIT_BUTTON_ORIGIN)

GAME_SAVE_BUTTON_RECT = GAME_SAVE_BUTTON.get_rect(topleft=GAME_SAVE_BUTTON_ORIGIN)
GAME_LOAD_BUTTON_RECT = GAME_LOAD_BUTTON.get_rect(topleft=GAME_LOAD_BUTTON_ORIGIN)
GAME_LOG_BUTTON_RECT = GAME_LOG_BUTTON.get_rect(topleft=GAME_LOG_BUTTON_ORIGIN)
GAME_QUIT_BUTTON_RECT = GAME_QUIT_BUTTON.get_rect(topleft=GAME_QUIT_BUTTON_ORIGIN)

SETTINGS_BGM_PLUS_BUTTON_RECT = SETTINGS_BGM_PLUS_BUTTON.get_rect(topleft=SETTINGS_BGM_PLUS_BUTTON_ORIGIN)
SETTINGS_BGM_MINUS_BUTTON_RECT = SETTINGS_BGM_MINUS_BUTTON.get_rect(topleft=SETTINGS_BGM_MINUS_BUTTON_ORIGIN)
SETTINGS_SFX_PLUS_BUTTON_RECT = SETTINGS_SFX_PLUS_BUTTON.get_rect(topleft=SETTINGS_SFX_PLUS_BUTTON_ORIGIN)
SETTINGS_SFX_MINUS_BUTTON_RECT = SETTINGS_SFX_MINUS_BUTTON.get_rect(topleft=SETTINGS_SFX_MINUS_BUTTON_ORIGIN)

SAVE_BUTTON_1_RECT = SAVE_BUTTON.get_rect(topleft=SAVE_BUTTON_1_ORIGIN)
SAVE_BUTTON_2_RECT = SAVE_BUTTON.get_rect(topleft=SAVE_BUTTON_2_ORIGIN)
SAVE_BUTTON_3_RECT = SAVE_BUTTON.get_rect(topleft=SAVE_BUTTON_3_ORIGIN)
LOAD_BUTTON_1_RECT = LOAD_BUTTON.get_rect(topleft=LOAD_BUTTON_1_ORIGIN)
LOAD_BUTTON_2_RECT = LOAD_BUTTON.get_rect(topleft=LOAD_BUTTON_2_ORIGIN)
LOAD_BUTTON_3_RECT = LOAD_BUTTON.get_rect(topleft=LOAD_BUTTON_3_ORIGIN)
#endregion

#region Rendering Functions

# Render text of any size with a given screen coordinate
def renderBodyText(text, font_size, origin, aa, fg, bg = None):
  match font_size:
    case "small":
      output = BODY_FONT_SMALL.render("{}".format(text), aa, fg, bg)
    case "medium":
      output = BODY_FONT_MEDIUM.render("{}".format(text), aa, fg, bg)
    case "large":
      output = BODY_FONT_LARGE.render("{}".format(text), aa, fg, bg)
    case _:
      output = BODY_FONT_LARGE.render("{}".format(text), aa, fg, bg)
  
  screen.blit(output, origin)

# Get color for character's text
def getColor(word):
  if re.search(c.TEXT_COLOR_PATTERN, word):
    match = re.search(c.TEXT_COLOR_PATTERN, word).string
    match = match.replace('(', '')
    match = match.replace(')', '')
    return tuple(map(int, match.split(',')))
  else:
    return 0

# Shows confirmation box and text
def drawConfirmation(text, x, y, fg_color):
  counter = 0
  cur_x = x
  color = fg_color
  split_text = text.split()

  for word in split_text:

    if getColor(word):
      color = getColor(word)
      continue

    # confirmation text is small by default
    word_to_draw = BODY_FONT_SMALL.render("{} ".format(word), True, color)
    word_width = word_to_draw.get_width()

    # If the word overlaps the boundary, skips line
    if cur_x + word_width > TEXT_BODY_BOUNDS:
      cur_x = x
      counter += 1

    screen.blit(word_to_draw, (cur_x, y + (counter * TEXT_BODY_LINE_SPACING)))
    cur_x += word_width

def drawSpeaker(name, x, y, fg_color, bg_color = None):
  speaker_box = SPEAKER_FONT.render("{}".format(name), True, fg_color, bg_color)
  screen.blit(speaker_box, (x, y))

def loadUserSettings():
  # File exists, load and return it
  if path.exists(c.GAME_SETTINGS):
    settings = []

    with open(c.GAME_SETTINGS, "rt") as in_file:
      for cnt, line in enumerate(in_file):
        settings.append(int(line.strip()))

    return settings

  # File doesn't exist, create and return it
  else:
    saveUserSettings(DEFAULT_BGM_VOLUME, DEFAULT_SFX_VOLUME)
    return [DEFAULT_BGM_VOLUME, DEFAULT_SFX_VOLUME]

def saveUserSettings(bgm, sfx):  
  with open(c.GAME_SETTINGS, "wt") as out_file:
    out_file.write("{}\n{}".format(bgm, sfx))

def setVolume(bgm, sfx):
  mixer.music.set_volume(bgm / 10)
  sound_btn_click.set_volume(sfx / 10)
  sound_btn_back.set_volume(sfx / 10)

def saveToFile(file, payload):
  with open(file, "wt") as out_file:
    write_string = ""

    for elem in payload:
      write_string += "{}\n".format(elem)

    out_file.write("{}".format(write_string))

def commonSaveLoadGUI():
  screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_1_ORIGIN)
  screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_2_ORIGIN)
  screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_3_ORIGIN)

# Get save data and return it as a list
def loadSaveFileData(save_file):
  result = []

  if path.exists(save_file):
    with open(save_file, "rt") as in_file:
      for ctn, line in enumerate(in_file):
        if ctn in [1, 2, 3, 4]:
          result.append(ast.literal_eval(line.strip()))
        elif ctn in [7, 8]:
          result.append(int(line.strip()))
        else:
          result.append(line.strip())

    return result
  else:
    return 0

# Get current chapter and date info for all save files
def saveFileChapterDate():
  save_files = [c.SAVE_FILE_1, c.SAVE_FILE_2, c.SAVE_FILE_3]
  output = []

  for save in save_files:
    if loadSaveFileData(save):
      data = loadSaveFileData(save)
      output.append([data[0], data[1]])
    else:
      output.append(False)

  return output

# Show all save files date and time to all slots
def drawSaveFileChapterDate():
  save_details_start_y = 200
  save_details_y = save_details_start_y
  save_details_y_increment = 250

  for elem in save_details:
    save_chapter = "NO FILE"
    save_datetime = ""

    if elem:
      save_chapter = "Chapter {}: {}".format(elem[1]["number"], elem[1]["title"])
      save_datetime = elem[0]

    renderBodyText(save_chapter, "medium", (200, save_details_y), True, c.WHITE)
    renderBodyText(save_datetime, "medium", (200, save_details_y + 50), True, c.WHITE)

    save_details_y += save_details_y_increment

# Show confirmation (yes or no) box
def displayConfirmationBox():
  screen.blit(CONFIRMATION_BOX, CONFIRMATION_BOX_ORIGIN)
  text_to_draw = BODY_FONT_MEDIUM.render(CONFIRMATION_BOX_TEXT, True, c.WHITE)
  text_width = text_to_draw.get_width()
  text_x = int(math.floor(CONFIRMATION_BOX.get_width() - text_width) / 2) + CONFIRMATION_BOX_ORIGIN[0]
  text_y = int(math.floor(c.getGameResolutionY() - CONFIRMATION_BOX.get_height()) / 2) + 50
  screen.blit(text_to_draw, (text_x, text_y))
  screen.blit(CONFIRMATION_BOX_BUTTON_YES, CONFIRMATION_BOX_BUTTON_YES_ORIGIN)
  screen.blit(CONFIRMATION_BOX_BUTTON_NO, CONFIRMATION_BOX_BUTTON_NO_ORIGIN)

#endregion

# region Set Variables 
current_state = State.TITLE
current_background = TITLE_BACKGROUND
current_bg_file = BLANK_BG_FILE
current_bgm = ""
current_story_index = 0
current_sprites = {}
current_chapter = {"number": 0, "title": "", "file": ""}
current_text = {
  "speaker": "",
  "body": "",
  "speaker_color": c.WHITE,
  "body_color": c.WHITE
}
scrollback_log = []
scrollback_pos = 0
state_before_load = State.TITLE
save_details = saveFileChapterDate()
ready_to_save = False
ready_to_load = False
quit_confirmation = False
save_file = ""
confirmation_ok = False
running = True
title_bgm_playing = False
display_text_box = 1
display_game_ui = True
slide_index = 0
#endregion

# Load music and sfx configuration and apply
volume = loadUserSettings()
volume_bgm = volume[0]
volume_sfx = volume[1]
sound_btn_click = mixer.Sound(c.SFX_PATH + c.assets["BUTTON_CLICK_SFX"])
sound_btn_back = mixer.Sound(c.SFX_PATH + c.assets["BUTTON_BACK_SFX"])
setVolume(volume_bgm, volume_sfx)

# region Main game loop
while running:
  screen.fill(c.BLACK)
  screen.blit(current_background, (0, 0))

  match current_state:
    case State.TITLE:
      slide_index = 0

      if current_background != TITLE_BACKGROUND:
        current_background = TITLE_BACKGROUND

      # Reset music
      if not(title_bgm_playing):
        title_bgm_playing = True
        current_bgm = c.assets["TITLE_BGM"]
        mixer.music.load(c.MUSIC_PATH + current_bgm)
        mixer.music.play(-1)

      screen.blit(TITLE_ENGINE_IMAGE, TITLE_ENGINE_IMAGE_ORIGIN)
      screen.blit(TITLE_START_BUTTON, TITLE_START_BUTTON_ORIGIN)
      screen.blit(TITLE_LOAD_BUTTON, TITLE_LOAD_BUTTON_ORIGIN)
      screen.blit(TITLE_SETTINGS_BUTTON, TITLE_SETTINGS_BUTTON_ORIGIN)
      screen.blit(TITLE_QUIT_BUTTON, TITLE_QUIT_BUTTON_ORIGIN)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
          mouse_x, mouse_y = event.pos

          if TITLE_START_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            current_bg_file = BLANK_BG_FILE
            current_text["speaker"] = ""
            current_text["speaker_color"] = c.WHITE
            current_text["body"] = ""
            current_text["body_color"] = c.WHITE
            current_sprites = {}
            current_story_index = 0
            current_chapter = {"number": 0, "title": "", "file": ""}
            scrollback_log = []
            scrollback_pos = 0
            mixer.music.stop()
            title_bgm_playing = False
            current_state = State.GAME

          if TITLE_LOAD_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            current_background = SAVE_LOAD_BG
            state_before_load = State.TITLE
            current_state = State.LOAD

          if TITLE_SETTINGS_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            current_background = SETTINGS_BG
            current_state = State.SETTINGS

          if TITLE_QUIT_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            running = False

    case State.LOAD:
      renderBodyText(LOAD_HEADING_TEXT, "large", HEADING_ORIGIN, True, c.WHITE)
      commonSaveLoadGUI()
      screen.blit(LOAD_BUTTON, LOAD_BUTTON_1_ORIGIN)
      screen.blit(LOAD_BUTTON, LOAD_BUTTON_2_ORIGIN)
      screen.blit(LOAD_BUTTON, LOAD_BUTTON_3_ORIGIN)
      drawSaveFileChapterDate()
      screen.blit(BACK_BUTTON, BACK_BUTTON_ORIGIN)

      if ready_to_load:
        displayConfirmationBox()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            if ready_to_load and not(confirmation_ok):
              # Cancel confirmation box if it's open
              ready_to_load = False
            else:
              if state_before_load == State.TITLE:
                current_state = State.TITLE
              else:
                # Change to the right background when changing states
                current_background = pygame.image.load(c.BACKGROUND_PATH + current_bg_file)
                current_state = State.GAME

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
          mouse_x, mouse_y = event.pos

          if not(ready_to_load) and not(confirmation_ok):
            if BACK_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              if state_before_load == State.TITLE:
                current_state = State.TITLE
              else:
                # Change to the right background when changing states
                current_background = pygame.image.load(c.BACKGROUND_PATH + current_bg_file)
                current_state = State.GAME

            if LOAD_BUTTON_1_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_1
              ready_to_load = True

            if LOAD_BUTTON_2_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_2
              ready_to_load = True

            if LOAD_BUTTON_3_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_3
              ready_to_load = True

          elif ready_to_load and not(confirmation_ok):
            if CONFIRMATION_BOX_BUTTON_YES_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              confirmation_ok = True

            if CONFIRMATION_BOX_BUTTON_NO_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              ready_to_load = False

      # Once you know which file to load and confirmed your selection, load the state
      if ready_to_load and confirmation_ok:
        if loadSaveFileData(save_file):
          save_data = loadSaveFileData(save_file)
          current_chapter = save_data[1]
          current_sprites = save_data[2]
          current_text = save_data[3]
          scrollback_log = save_data[4]
          current_bgm = save_data[5]
          current_bg_file = save_data[6]
          current_story_index = save_data[7]
          display_text_box = save_data[8]
          
          for i in story:
            i[0] = 0

          cnt = 1
          for i in story:
            i[0] = 1
            cnt += 1

            if cnt >= current_story_index:
              break

          current_background = pygame.image.load(c.BACKGROUND_PATH + current_bg_file)
          if current_bgm != "":
            mixer.music.load(c.MUSIC_PATH + current_bgm)
            mixer.music.play(-1)

          confirmation_ok = False
          ready_to_load = False
          current_state = State.GAME

    case State.SAVE:
      renderBodyText(SAVE_HEADING_TEXT, "large", HEADING_ORIGIN, True, c.WHITE)
      commonSaveLoadGUI()
      screen.blit(SAVE_BUTTON, SAVE_BUTTON_1_ORIGIN)
      screen.blit(SAVE_BUTTON, SAVE_BUTTON_2_ORIGIN)
      screen.blit(SAVE_BUTTON, SAVE_BUTTON_3_ORIGIN)
      drawSaveFileChapterDate()
      screen.blit(BACK_BUTTON, BACK_BUTTON_ORIGIN)
      
      if ready_to_save:
        displayConfirmationBox()

      if ready_to_save and confirmation_ok:
        now = datetime.now()
        dt = now.strftime("%Y %b %d - %H:%M:%S")

        saveToFile(
          save_file,
          [
              dt,
              current_chapter,
              current_sprites,
              current_text,
              scrollback_log,
              current_bgm,
              current_bg_file,
              current_story_index,
              display_text_box
          ]
        )

        # Update stored save file chapter and date display
        save_details = saveFileChapterDate()
        confirmation_ok = False
        ready_to_save = False

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            if ready_to_save and not(confirmation_ok):
              # Cancel confirmation box if it's open
              ready_to_save = False
            else:
              current_background = pygame.image.load(c.BACKGROUND_PATH + current_bg_file)
              current_state = State.GAME

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
          mouse_x, mouse_y = event.pos
          
          # Save didn't happen yet, only showing save screen options
          if not(ready_to_save) and not(confirmation_ok):
            if BACK_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              current_background = pygame.image.load(c.BACKGROUND_PATH + current_bg_file)
              current_state = State.GAME

            if SAVE_BUTTON_1_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_1
              ready_to_save = True
            
            if SAVE_BUTTON_2_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_2
              ready_to_save = True

            if SAVE_BUTTON_3_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              save_file = c.SAVE_FILE_3
              ready_to_save = True

          # One of the save slot was selected, confirm decision
          elif ready_to_save and not(confirmation_ok):
            if CONFIRMATION_BOX_BUTTON_YES_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              confirmation_ok = True

            if CONFIRMATION_BOX_BUTTON_NO_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              ready_to_save = False

    case State.LOG:
      if len(current_sprites) > 0:
        for spr in current_sprites.values():
          sprite_to_draw = pygame.image.load(c.SPRITE_PATH + spr["file"]).convert_alpha()
          screen.blit(sprite_to_draw, (spr["x"], spr["y"]))

      screen.blit(LOG_BOX, (0, 0))
      start_x = 80
      current_y = 20

      for i in range(len(scrollback_log)):
        pos = i + scrollback_pos
        current_x = start_x
        if current_y + LOG_LINE_SPACING > c.getGameResolutionY():
          break

        try:
          scrollback_speaker = BODY_FONT_SMALL.render("{}".format(scrollback_log[pos]["speaker"]), True, scrollback_log[pos]["speaker_color"])
          screen.blit(scrollback_speaker, (50, current_y))
          current_y += LOG_LINE_SPACING

        except:
          pass

        try:
          current_line = scrollback_log[pos]["body"].split()
          color = scrollback_log[pos]["body_color"]

          for j in range(len(current_line)):
            if getColor(current_line[j]):
              color = getColor(current_line[j])
              continue

            word_to_draw = BODY_FONT_SMALL.render("{} ".format(current_line[j]), True, color)
            word_width = word_to_draw.get_width()

            if current_x + word_width > TEXT_BODY_BOUNDS:
              current_x = start_x
              current_y += LOG_LINE_SPACING

            screen.blit(word_to_draw, (current_x, current_y))

            current_x += word_width

          current_y += LOG_LINE_SPACING

        except:
          pass

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        # You can scroll the log with up and down keys and exit with escape key
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            sound_btn_back.play()
            current_state = State.GAME

          if event.key == pygame.K_DOWN:
            if not(scrollback_pos >= len(scrollback_log)-1):
              scrollback_pos += 1

          if event.key == pygame.K_UP:
            if not(scrollback_pos <= 0):
              scrollback_pos -= 1

        # You can scroll the log with the mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 4:
            if not(scrollback_pos <= 0):
              scrollback_pos -= 1

          if event.button == 5:
            if not(scrollback_pos >= len(scrollback_log)-1):
              scrollback_pos += 1

    case State.GAME:
      if display_game_ui:
        if len(current_sprites) > 0:
          for spr in current_sprites.values():
            sprite_to_draw = pygame.image.load(c.SPRITE_PATH + spr["file"]).convert_alpha()
            screen.blit(sprite_to_draw, (spr["x"], spr["y"]))

        if display_text_box != 0:
          screen.blit(TEXT_BOX, TEXT_BOX_ORIGIN)

        screen.blit(GAME_SAVE_BUTTON, GAME_SAVE_BUTTON_ORIGIN)
        screen.blit(GAME_LOAD_BUTTON, GAME_LOAD_BUTTON_ORIGIN)
        screen.blit(GAME_LOG_BUTTON, GAME_LOG_BUTTON_ORIGIN)
        screen.blit(GAME_QUIT_BUTTON, GAME_QUIT_BUTTON_ORIGIN)
        
        if current_text["body"] != "":
          drawConfirmation(current_text["body"], c.assets["TEXT_BODY_ORIGIN"][0], c.assets["TEXT_BODY_ORIGIN"][1], current_text["body_color"])

        if current_text["speaker"] != "":
          drawSpeaker(" " + current_text["speaker"] + " ", SPEAKER_BOX_ORIGIN[0], SPEAKER_BOX_ORIGIN[1], current_text["speaker_color"])

      if quit_confirmation:
        displayConfirmationBox()

      # Game loop, passing through dialogue
      if story[current_story_index][0] == 0:
        story[current_story_index][0] = 1
        command = story[current_story_index][1]
        obj = story[current_story_index][-1]

        match command:
          case c.BG_IMG:
            current_background = pygame.image.load(c.BACKGROUND_PATH + obj["file"])
            current_bg_file = obj["file"]
          
          case c.SPRITE:
            current_sprites[obj["reference"]] = dict(file=obj["file"], x=obj["x"], y=obj["y"])

          case c.SPRITE_REMOVE:
            current_sprites.pop(obj["reference"])

          case c.CHAPTER:
            current_chapter["number"] = current_chapter["number"] + 1
            current_chapter["title"] = obj["title"]
            current_chapter["file"] = obj["file"]
            current_background = pygame.image.load(c.BACKGROUND_PATH + obj["file"])
            display_game_ui = False

          case c.TEXT:
            current_text = dict(
              speaker=obj["speaker"],
              body=obj["body"], 
              speaker_color=obj["speaker_color"],
              body_color=obj["body_color"])
            scrollback_log.insert(0, current_text)

            if len(scrollback_log) > LOG_LIMIT:
              scrollback_log.pop(-1)
          
          case c.CREDITS:
            current_story_index = 0
            for i in story:
              i[0] = 0
            current_state = State.CREDITS
          
          case c.MUSIC:
            mixer.music.load(c.MUSIC_PATH + obj["file"])
            mixer.music.play(-1)
            current_bgm = obj["file"]
          
          case c.SFX:
            sound = mixer.Sound(c.SFX_PATH + obj["file"])
            sound.play()
          
          case c.MUSIC_STOP:
            mixer.music.stop()
            current_bgm = ""

          case c.TEXT_BOX_SHOW:
            display_text_box = 1
          
          case c.TEXT_BOX_HIDE:
            display_text_box = 0

        if (not(story[current_story_index][1] is c.TEXT) and not(story[current_story_index][1] is c.CHAPTER)):
          if current_story_index + 1 < len(story):
            current_story_index += 1

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if not(quit_confirmation):
          if event.type == pygame.KEYDOWN:
            # Advance story bit by pressing space
            if (event.key == pygame.K_SPACE and (story[current_story_index][1] is c.TEXT or story[current_story_index][1] is c.CHAPTER)):
              display_game_ui = True

              if current_story_index + 1 < len(story):
                current_story_index += 1

            if event.key == pygame.K_ESCAPE:
              quit_confirmation = True

          if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            mouse_x, mouse_y = event.pos

            if GAME_SAVE_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              current_background = SAVE_LOAD_BG
              current_state = State.SAVE

            if GAME_LOAD_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              current_background = SAVE_LOAD_BG
              state_before_load = State.GAME
              current_state = State.LOAD

            if GAME_LOG_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              current_state = State.LOG

            if GAME_QUIT_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              quit_confirmation = True

        else:
          if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            mouse_x, mouse_y = event.pos

            if CONFIRMATION_BOX_BUTTON_YES_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_click.play()
              current_story_index = 0

              for i in story:
                i[0] = 0

              quit_confirmation = False
              title_bgm_playing = False
              current_state = State.TITLE

            if CONFIRMATION_BOX_BUTTON_NO_RECT.collidepoint(mouse_x, mouse_y):
              sound_btn_back.play()
              quit_confirmation = False

    case State.SETTINGS:
      renderBodyText(SETTINGS_HEADING_TEXT, "large", HEADING_ORIGIN, True, c.WHITE)
      renderBodyText(SETTINGS_BGM_TEXT, "large", SETTINGS_BGM_TEXT_ORIGIN, True, c.WHITE)
      renderBodyText(SETTINGS_SFX_TEXT, "large", SETTINGS_SFX_TEXT_ORIGIN, True, c.WHITE)
      screen.blit(SETTINGS_BGM_PLUS_BUTTON, SETTINGS_BGM_PLUS_BUTTON_ORIGIN)
      screen.blit(SETTINGS_BGM_MINUS_BUTTON, SETTINGS_BGM_MINUS_BUTTON_ORIGIN)

      screen.blit(SETTINGS_SFX_PLUS_BUTTON, SETTINGS_SFX_PLUS_BUTTON_ORIGIN)
      screen.blit(SETTINGS_SFX_MINUS_BUTTON, SETTINGS_SFX_MINUS_BUTTON_ORIGIN)

      renderBodyText(volume_bgm, "large", (1050, 490), True, c.WHITE)
      renderBodyText(volume_sfx, "large", (1050, 290), True, c.WHITE)
      screen.blit(BACK_BUTTON, BACK_BUTTON_ORIGIN)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
          mouse_x, mouse_y = event.pos

          if BACK_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_back.play()
            current_state = State.TITLE

          if SETTINGS_BGM_PLUS_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            volume_bgm = volume_bgm + 1 if volume_bgm < 10 else 10
            setVolume(volume_bgm, volume_sfx)
            saveUserSettings(volume_bgm, volume_sfx)

          if SETTINGS_BGM_MINUS_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            volume_bgm = volume_bgm - 1 if volume_bgm > 0 else 0
            setVolume(volume_bgm, volume_sfx)
            saveUserSettings(volume_bgm, volume_sfx)

          if SETTINGS_SFX_PLUS_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            volume_sfx = volume_sfx + 1 if volume_sfx < 10 else 10
            setVolume(volume_bgm, volume_sfx)
            saveUserSettings(volume_bgm, volume_sfx)

          if SETTINGS_SFX_MINUS_BUTTON_RECT.collidepoint(mouse_x, mouse_y):
            sound_btn_click.play()
            volume_sfx = volume_sfx - 1 if volume_sfx > 0 else 0
            setVolume(volume_bgm, volume_sfx)
            saveUserSettings(volume_bgm, volume_sfx)

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            current_state = State.TITLE

    case State.CREDITS:
      current_slide = pygame.image.load(c.BACKGROUND_PATH + CREDITS_GALLERY[slide_index])
      screen.blit(current_slide, (0, 0))

      # Reset music
      if CREDITS_BGM != current_bgm:
        title_bgm_playing = False
        current_bgm = c.assets["CREDITS_BGM"]
        mixer.music.load(c.MUSIC_PATH + current_bgm)
        mixer.music.play(-1)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            current_state = State.TITLE

          if event.key == pygame.K_SPACE:
            if slide_index + 1 >= len(CREDITS_GALLERY):
              current_state = State.TITLE
            else:
              slide_index += 1

  # Screen update
  pygame.display.update()
  clock.tick(60)

  #endregion