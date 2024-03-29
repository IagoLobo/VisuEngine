import config as configurations

def getStory():

  def color(color):
    color_string = "({},{},{})".format(color[0], color[1], color[2])
    return color_string

  story = [
    ["CHAPTER", {"title": "Prologue", "file": "chapter_prologue_1920x1080.png"}],
    ["BG_IMG", {"file": "cinema_nomovie_lowlight_1920x1080.png"}],
    ["MUSIC", {"file": "Otome90.ogg"}],
    ["SPRITE", 
      {"reference": "johndoe", "file": configurations.assets["MODEL_MALE_HAPPY"], "x": 200, "y": 25}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """Hello there! Welcome to Visu Engine, a basic engine for Visual Novel games in Python.""",
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "janedoe", "file": configurations.assets["MODEL_FEMALE_TIRED"], "x": 1100, "y": 25}
    ],
    ["TEXT", {
      "speaker": "Jane Doe", 
      "body": """*PANT* *PANT* *PANT*""", 
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "janedoe", "file": configurations.assets["MODEL_FEMALE_HAPPY"], "x": 1100, "y": 25}
    ],
    ["TEXT", {
      "speaker": "Jane Doe", 
      "body": """Hey, John! Sorry to keep you wanting!""", 
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """No worries, Jane! I was introducing the engine to our players.""", 
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane Doe", 
      "body": """What? What are you talking about, dude? Did you hit your head?""", 
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane Doe", 
      "body": """Or is this a reference to the movie we are gonna watch now?""", 
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """Yeah, yeah, it's totally a reference to the movie... *cough* *cough*""", 
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """Anyway, let's get a seat, it's about to start!""", 
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane",
      "body": """Sure thing!""",
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """Oh, and by the way, you can {} change {} the colors {} of words if you want to.""".format(
        color(configurations.RED),
        color(configurations.GREEN),
        color(configurations.WHITE)
      ), 
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["TEXT_BOX_HIDE", {}],
    # Inserted this so the engine recognizes it's a pause in the scene
    ["TEXT", {
      "speaker": "", 
      "body": "", 
      "speaker_color": configurations.WHITE,
      "body_color": configurations.WHITE}
    ],
    ["TEXT_BOX_SHOW", {}],
    ["SPRITE",
      {"reference": "janedoe", "file": configurations.assets["MODEL_FEMALE_UPSET"], "x": 1100, "y": 25}
    ],
    ["TEXT", {
      "speaker": "Jane Doe",
      "body": """WHAT THE HELL HAPPENED JUST NOW?!""",
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "johndoe", "file": configurations.assets["MODEL_MALE_EMBARRASSED"], "x": 200, "y": 25}
    ],
    ["TEXT", {
      "speaker": "John Doe", 
      "body": """NOTHING!""", 
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE_REMOVE", {"reference": "johndoe"}],
    ["SPRITE_REMOVE", {"reference": "janedoe"}],
    ["CHAPTER", {"title": "Epilogue", "file": "chapter_epilogue_1920x1080.png"}],
    ["BG_IMG", {"file": "cinema_movie_nolight_1920x1080.png"}],
    ["SPRITE",
      {"reference": "janedoe", "file": configurations.assets["MODEL_FEMALE_HAPPY"], "x": 1100, "y": 25}
    ],
    ["TEXT", {
      "speaker": "Jane Doe",
      "body": """Wow, this movie is really cool! I'm loving it so far!""",
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "johndoe", "file": configurations.assets["MODEL_MALE_HAPPY"], "x": 200, "y": 25}
    ],
    ["TEXT", {
      "speaker": "John Doe",
      "body": """I'm loving it too! Especially this second chapter... Very interesting, right?""",
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "janedoe", "file": configurations.assets["MODEL_FEMALE_UPSET"], "x": 1100, "y": 25}
    ],
    ["TEXT", {
      "speaker": "Jane Doe",
      "body": """Eh? There's no chapters in this movie, what are you talking about?""",
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["SPRITE",
      {"reference": "johndoe", "file": configurations.assets["MODEL_MALE_EMBARRASSED"], "x": 200, "y": 25}
    ],
    ["TEXT", {
      "speaker": "John Doe",
      "body": """Well, look at the time! Until we meet again, everyone!""",
      "speaker_color": configurations.GREEN,
      "body_color": configurations.WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane Doe",
      "body": """Wait, everyone?""",
      "speaker_color": configurations.RED,
      "body_color": configurations.WHITE}
    ],
    ["MUSIC", {"file": "Again.ogg"}],
    ["BG_IMG", {"file": "black_background_1920x1080.png"}],
    ["SPRITE_REMOVE", {"reference": "johndoe"}],
    ["SPRITE_REMOVE", {"reference": "janedoe"}],
    ["CREDITS", {}]
  ]

  for i in story:
    i.insert(0, 0)

  return story
