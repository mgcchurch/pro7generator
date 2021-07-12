#! /usr/bin/env python

# See README.txt for information and build instructions.

import presentation_pb2
import sys
import argparse
import configparser
import os
import pyodbc


class Lyrics:
    def __init__(self):
        self.database_dictionary = {"title_traditional": 1,
                                    "singer": 2,
                                    "youtube": 3,
                                    "lyrics_traditional": 4,
                                    "title_simple": 5,
                                    "lyrics_simple": 6,
                                    "title_english": 7,
                                    "lyrics_english": 8,
                                    "arrangement1": 9,
                                    "arrangement2": 10,
                                    "arrangement3": 11,
                                    "arrangement4": 12,
                                    "arrangement5": 13
                                    }
        self.database_length = 13
        self.singer = ""
        self.youtube = ""
        self.traditional = {"[Title]": [], "[Intro]": [],
                            "[Verse]": [], "[Verse 1]": [], "[Verse 2]": [], "[Verse 3]": [], "[Verse 4]": [], "[Verse 5]": [], "[Verse 6]": [],
                            "[Verse 7]": [], "[Verse 8]": [], "[Verse 9]": [], "[PreChorus]": [], "[PreChorus 1]": [], "[PreChorus 2]": [],
                            "[Chorus]": [], "[Chorus 1]": [], "[Chorus 2]": [], "[Chorus 3]": [], "[Chorus 4]": [], "[Chorus 5]": [], "[Chorus 6]": [],
                            "[Bridge]": [], "[Bridge 1]": [], "[Bridge 2]": [], "[Bridge 3]": [], "[Ending]": []
                            }
        self.simple = {"[Title]": [], "[Intro]": [],
                       "[Verse]": [], "[Verse 1]": [], "[Verse 2]": [], "[Verse 3]": [], "[Verse 4]": [], "[Verse 5]": [], "[Verse 6]": [],
                       "[Verse 7]": [], "[Verse 8]": [], "[Verse 9]": [], "[PreChorus]": [], "[PreChorus 1]": [], "[PreChorus 2]": [],
                       "[Chorus]": [], "[Chorus 1]": [], "[Chorus 2]": [], "[Chorus 3]": [], "[Chorus 4]": [], "[Chorus 5]": [], "[Chorus 6]": [],
                       "[Bridge]": [], "[Bridge 1]": [], "[Bridge 2]": [], "[Bridge 3]": [], "[Ending]": []
                       }
        self.pinyin = {"[Title]": [], "[Intro]": [],
                       "[Verse]": [], "[Verse 1]": [], "[Verse 2]": [], "[Verse 3]": [], "[Verse 4]": [], "[Verse 5]": [], "[Verse 6]": [],
                       "[Verse 7]": [], "[Verse 8]": [], "[Verse 9]": [], "[PreChorus]": [], "[PreChorus 1]": [], "[PreChorus 2]": [],
                       "[Chorus]": [], "[Chorus 1]": [], "[Chorus 2]": [], "[Chorus 3]": [], "[Chorus 4]": [], "[Chorus 5]": [], "[Chorus 6]": [],
                       "[Bridge]": [], "[Bridge 1]": [], "[Bridge 2]": [], "[Bridge 3]": [], "[Ending]": []
                       }
        self.english = {"[Title]": [], "[Intro]": [],
                        "[Verse]": [], "[Verse 1]": [], "[Verse 2]": [], "[Verse 3]": [], "[Verse 4]": [], "[Verse 5]": [], "[Verse 6]": [],
                        "[Verse 7]": [], "[Verse 8]": [], "[Verse 9]": [], "[PreChorus]": [], "[PreChorus 1]": [], "[PreChorus 2]": [],
                        "[Chorus]": [], "[Chorus 1]": [], "[Chorus 2]": [], "[Chorus 3]": [], "[Chorus 4]": [], "[Chorus 5]": [], "[Chorus 6]": [],
                        "[Bridge]": [], "[Bridge 1]": [], "[Bridge 2]": [], "[Bridge 3]": [], "[Ending]": []
                        }
        self.arrangements = ["", "", "", "", ""]


class pro7generator:
    def __init__(self):
        pass

    def generate_lyrics(self, config_parser):
        """
        Use the lyrics template to generate lyrics files in the output folder
        """

        # import the lyrics template
        # try:
        #   with open(config_parser['LYRICS']['template_path'], "rb") as f:
        #     presentation = presentation_pb2.Presentation()
        #     presentation.ParseFromString(f.read())
        # except IOError:
        #   print("Lyrics template file not found.")

        lyrics = Lyrics()
        # import MS Access database file
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=./src/proto/Input/Lyrics_Database.mdb;')
        conn = pyodbc.connect(conn_str)

        cursor = conn.cursor()
        cursor.execute('select * from Lyrics')
        for row in cursor.fetchall():
            print(row)
        # pick up one lyrics
            for index in range(lyrics.database_length):
                lyrics.singer = row[lyrics.database_dictionary["singer"]]
                lyrics.youtube = row[lyrics.database_dictionary["youtube"]]
                lyrics.traditional["[Title]"].append(
                    row[lyrics.database_dictionary["title_traditional"]])
                traditional_elements = row[lyrics.database_dictionary["lyrics_traditional"]].splitlines(
                )
                current_label = None
                for element in traditional_elements:
                    if element in lyrics.traditional.keys():
                        current_label = element
                    else:
                        if current_label is not None:
                            lyrics.traditional[current_label].append(element)

        # pick up sentence in the lyrics
        # create slide in the lyrics pro file
        # new_cue = presentation.cues.add()
        # new_cue.CopyFrom(presentation.cues[1])

        # output lyrics pro file in the output folder

        # Read the existing address book.
        # pass
        # with open(config_parser['LYRICS']['template_path'], "wb") as f:
        #   f.write(presentation.SerializeToString())

        # f.close()

    def generate_playlist(self, config_parser):
        """
        Use the playlist template to generate playlist file in the output folder
        """
        pass


if __name__ == "__main__":
    # Parse argument from user's input
    parser = argparse.ArgumentParser(description='Pro7 Generator')
    parser.add_argument('command', help="Type command in the format 'Pro7Generator [option] [command]', "
                                        "command must be lyrics or playlist", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    config_parser = configparser.RawConfigParser()
    config_parser.read('./src/proto/config.ini')

    if args.command[0] == 'lyrics':
        if os.path.isfile("./src/proto/Template/lyrics.pro") is None:
            print("Lyrics template file does not exit!")
            sys.exit(-1)

        pro7generator_instance = pro7generator()
        pro7generator_instance.generate_lyrics(config_parser)

    elif args.command[0] == 'playlist':
        if os.path.isfile("./template/serviceplan.pro") is None:
            print("Plan template file does not exit!")
            sys.exit(-1)

        pro7generator_instance = pro7generator()
        pro7generator_instance.generate_playlist(config_parser)
