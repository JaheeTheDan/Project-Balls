import os
import sys
import keyboard
from just_playback import Playback

application_path = os.path.dirname(sys.executable)
print(application_path)
# application_path = os.path.dirname(sys.prefix)
# print(application_path)


# audio_file\balls2.wav
file = application_path + '\\audio_file\\balls.wav'
playback = Playback()
playback.load_file(file)

keyboard.add_word_listener('balls', playback.play, ['space', 'enter'])
print('program ready')
while True:
    # recorded = keyboard.record(until='enter')
    # words = list(keyboard.get_typed_strings(recorded))
    # for i in words:
    #     if 'balls' in i: 
    #         playback.play()
    keyboard.wait()
