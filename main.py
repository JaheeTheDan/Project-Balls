import keyboard
from just_playback import Playback

file = 'balls.wav' # This the audio file (you can choose any audio at your will as long as it works the just_playback library and the name is the same as audio file name)
playback = Playback()
playback.load_file(file)

keyword = 'balls # the keyword can anything you choose
keyboard.add_word_listener(keyword, playback.play, ['space', 'enter']) # The space and enter is used to trigger a check if the keyword is match with what is type
print('program ready')
while True:
    keyboard.wait() # This ensures that the code doesn't stop running
