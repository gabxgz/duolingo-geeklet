# [sudo] pip install duolingo-api
import duolingo
import math
import shutil
import os


USERNAME = 'xxxxxxx'
PASSWORD = 'xxxxxxx'

dir = os.path.dirname(__file__)
data = duolingo.Duolingo(USERNAME, password=PASSWORD)
languages = data.get_languages(abbreviations=False)

for language in languages:
  details = data.get_language_details(language)
  isLearning = details['current_learning']
  abbr = details['language']

  if isLearning:
    progress = data.get_language_progress(abbr)

    level = progress['level']
    currentXP = progress['points']
    targetXP = currentXP + progress['level_left']
    streak = details['streak']

    print 'L%d %s' % (level, language)
    print 'XP %d/%d' % (currentXP, targetXP)

    percentComplete = progress['level_percent']

    photo = int(math.floor(percentComplete)/10)
    source = 'images/%d.png' % (photo)
    imageSource = os.path.join(dir, source)
    imageDestination = os.path.join(dir, 'progress.png')
    shutil.copyfile(imageSource, imageDestination)
