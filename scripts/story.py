import config as configurations
import os.path
from os import path
import ast

def getStory():
  
  # Load story bit in string
  def loadStoryBit(file_path):
    result = []

    # First, get the whole file as a string
    if path.exists(file_path):
      with open(file_path, "r") as pure_file:
        string_file = pure_file.read().replace('\n', '')
    else:
      return 0
    
    # Separate story parts by []
    string_file = string_file.replace("],", "]\n")

    # print(string_file)
    result = string_file.splitlines()

    return result

  story = loadStoryBit(configurations.CHAPTER_1), loadStoryBit(configurations.CHAPTER_2)

  print(*story)

  for i in story:
    i.insert(0, 0)

  return story
