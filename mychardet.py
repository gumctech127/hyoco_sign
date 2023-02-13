
from chardet.universaldetector import UniversalDetector
import os

# files = ['test.hsc']

directory_in_str = 'LED_Sign\Monthly_Schedules'
files = os.fsencode(directory_in_str)
    
detector = UniversalDetector()
# 
for file in os.listdir(files):
    filename = os.fsdecode(file)
    if filename.endswith(".hsc"):
        print(filename.ljust(20), end='')
        detector.reset()
        for line in open(os.path.join(directory_in_str, filename), 'rb'):
            detector.feed(line)
            if detector.done: break
        detector.close()
        print(detector.result)


# # gives me as a result:
# 1- January 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.6715158248808822, 'language': 'Greek'}
# 1- January 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8449993687509817, 'language': 'Greek'}
# 1- January 2021_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.56742304549958, 'language': 'Greek'}
# 1- January 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.97694160165174, 'language': 'Turkish'}
# 1- January 2023_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.49193005680241464, 'language': 'Turkish'}
# 10- October 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8044939410130372, 'language': 'Greek'}
# 10- October 2020_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.9205483890863465, 'language': 'Greek'}
# 10- October 2021_playlist.hsc{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# 10- October 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9771296968470448, 'language': 'Turkish'}
# 11- November 2019_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9702556339496634, 'language': 'Turkish'}
# 11- November 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8041123025210954, 'language': 'Greek'}
# 11- November 2021_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8189217376596125, 'language': 'Greek'}
# 11- November 2022_playlist.hsc{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# 12- December 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8117937921674108, 'language': 'Greek'}
# 12- December 2020_playlist.hsc{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# 12- December 2021_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9742418525547094, 'language': 'Turkish'}
# 12- December 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9847077962872692, 'language': 'Turkish'}
# 2- February 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.6782988130109922, 'language': 'Greek'}
# 2- February 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.723953540809809, 'language': 'Greek'}
# 2- February 2021_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.7630861646373661, 'language': 'Greek'}
# 2- February 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9811175050108812, 'language': 'Turkish'}
# 2- February 2023_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9862736421208997, 'language': 'Turkish'}
# 3- March 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.7607946145934101, 'language': 'Greek'}
# 3- March 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8667151499584901, 'language': 'Greek'}
# 3- March 2021_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.9092090472275002, 'language': 'Greek'}
# 3- March 2022.playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.984036309600171, 'language': 'Turkish'}
# 4- April 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8298336542155755, 'language': 'Greek'}
# 4- April 2020_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.5964351631648379, 'language': 'Greek'}
# 4- April 2021playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.7936096112228609, 'language': 'Greek'}
# 4- April 2022playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9859033734755883, 'language': 'Turkish'}
# 5- May 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8902671920769273, 'language': 'Greek'}
# 5- May 2020_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.5835364788403389, 'language': 'Greek'}
# 5- May 2021_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.9411396030527517, 'language': 'Greek'}
# 5- May 2022_playlist.hsc{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# 6- June 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.87500546878418, 'language': 'Greek'}
# 6- June 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.7718572699780256, 'language': 'Greek'}
# 6- June 2021_playlist.hsc{'encoding': 'Windows-1253', 'confidence': 0.8559485021329186, 'language': 'Greek'}
# 6- June 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9808346601481717, 'language': 'Turkish'}
# 7- July 2019_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.6971404467057419, 'language': 'Greek'}
# 7- July 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.937123360080976, 'language': 'Greek'}
# 7- July 2021_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.8875612127697026, 'language': 'Greek'}
# 7- July 2022_playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.9781249551308248, 'language': 'Turkish'}
# 8- August 2019_playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.41959490084985834, 'language': ''}
# 8- August 2020_playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.4128999307479225, 'language': ''}
# 8- August 2021_playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.42984311512415346, 'language': ''}
# 8- August 2022_playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.4005764807360552, 'language': ''}
# 9- September 2019_playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.4100028409090909, 'language': ''}
# 9- September 2020_playlist.hsc{'encoding': 'windows-1253', 'confidence': 0.44611191163415254, 'language': 'Greek'}
# 9- September 2021.playlist.hsc{'encoding': 'MacRoman', 'confidence': 0.3860597692080087, 'language': ''}
# 9- September 2022.playlist.hsc{'encoding': 'Windows-1254', 'confidence': 0.48665846173787786, 'language': 'Turkish'}