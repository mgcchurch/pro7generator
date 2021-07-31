#! /usr/bin/env python

# See README.txt for information and build instructions.

import presentation_pb2
import cue_pb2
import sys
import argparse
import configparser
import os
import pyodbc
import uuid


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
        # RGB and alpha of groups
        self.group_color = {
            "Title": [1, 1, 0, 1],
            "Verse": [0, 0.466666669, 0.8, 1],
            "Verse 1": [0, 0.466666669, 0.8, 1],
            "Verse 2": [0, 0.349019617, 0.6, 1],
            "Verse 3": [0, 0.235294119, 0.4, 1],
            "Verse 4": [1, 0.498039216, 0, 1],
            "Verse 5": [0, 0.290196091, 0.501960814, 1],
            "Verse 6": [0, 0.176470593, 0.301960796, 1],
            "Chorus": [0.8, 0, 0.305882365, 1],
            "Chorus 1": [0.8, 0, 0.305882365, 1],
            "Chorus 2": [0.6, 0, 0.23137255, 1],
            "Chorus 3": [0.4, 0, 0.152941182, 1],
            "Chorus 4": [0.701960802, 0, 0.266666681, 1],
            "Bridge": [0.4627451, 0, 0.8, 1],
            "Bridge 1": [0.4627451, 0, 0.8, 1],
            "Bridge 2": [0.349019617, 0, 0.6, 1],
            "Bridge 3": [1, 0.498039216, 0, 1],
            "PreChorus": [1, 0.498039216, 0, 1],
            "Tag": [0.8, 0.160784319, 0.160784319, 1],
            "Intro": [0.701960802, 0.654902, 0.141176477, 1],
            "Ending": [0, 1, 1, 1],
            "Outro": [0.494117647, 0.4627451, 0.0980392173, 1],
            "Interlude": [0.141176477, 0.701960802, 0.298039228, 1],
            "Vamp": [0.141176477, 0.701960802, 0.298039228, 1],
            "Turnaround": [0.141176477, 0.701960802, 0.298039228, 1],
            "Blank": [0, 0, 0, 1]
        }


class pro7generator:
    def __init__(self):
        pass

    def generate_lyrics(self, config_parser):
        """
        Use the lyrics template to generate lyrics files in the output folder
        """

        # import the lyrics template file which is defined in the config.ini
        try:
            with open(config_parser['LYRICS']['template_path'], "rb") as f:
                presentation = presentation_pb2.Presentation()
                presentation.ParseFromString(f.read())
        except IOError:
            print("Lyrics template file not found.")
            return

        # import MS Access database file
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=./src/proto/Input/Lyrics_Database.mdb;')
        conn = pyodbc.connect(conn_str)

        cursor = conn.cursor()
        cursor.execute('select * from Lyrics')
        # fetch the data of each row from lyrics database file and save it to lyrics instance, a row includes title, singer, etc
        for row in cursor.fetchall():
            lyrics = Lyrics()
            # loop all elements in the song
            # for index in range(lyrics.database_length):
            lyrics.singer = row[lyrics.database_dictionary["singer"]]
            lyrics.youtube = row[lyrics.database_dictionary["youtube"]]
            lyrics.traditional["[Title]"].append(
                row[lyrics.database_dictionary["title_traditional"]])
            # split lyrics text into each line
            traditional_elements = row[lyrics.database_dictionary["lyrics_traditional"]].splitlines(
            )
            current_label = None
            for element in traditional_elements:
                # if the element in the line is label, record the current label
                if element in lyrics.traditional.keys():
                    current_label = element
                else:
                    if current_label is not None and element != "":
                        lyrics.traditional[current_label].append(element)

            # use first cues as template
            cues_template = cue_pb2.Cue()
            cues_template.CopyFrom(presentation.cues[0])

            # loop and fetch each label from the song
            for label, lines in lyrics.traditional.items():
                # if lines is blank, move to the next label
                if lines == []:
                    continue
                # cue_groups[0] is used to storage 'title'
                if label == '[Title]':
                    cue_groups = presentation.cue_groups[0]
                else:
                    cue_groups = presentation.cue_groups.add()
                    # renew the group uuid
                    cue_groups.group.uuid.string = str(uuid.uuid4())

                # set the group name
                cue_groups.group.name = label[1:-1]
                # set the color of the cue_groups
                cue_groups.group.color.red = lyrics.group_color[cue_groups.group.name][0]
                cue_groups.group.color.green = lyrics.group_color[cue_groups.group.name][1]
                cue_groups.group.color.blue = lyrics.group_color[cue_groups.group.name][2]
                cue_groups.group.color.alpha = lyrics.group_color[cue_groups.group.name][3]

                # loop each line in the label group
                for i in range(len(lines)):
                    if i == 0 and label == '[Title]':
                        # cue_group of 'Title' use the current cue_identifiers
                        cue_identifiers = cue_groups.cue_identifiers[0]
                        # use the cues[0] to set title
                        new_cue = presentation.cues[0]
                    else:
                        # add new cue_identifiers
                        cue_identifiers = cue_groups.cue_identifiers.add()
                        # renew the string with new uuid
                        cue_identifiers.string = str(uuid.uuid4())
                        # add new cue (slide) for the new line
                        new_cue = presentation.cues.add()
                        new_cue.CopyFrom(cues_template)
                        # update cue UUID
                        new_cue.uuid.string = cue_identifiers.string
                        # update actions UUID
                        new_cue.actions[0].uuid.string = str(uuid.uuid4())

                    # loop and update each element in the cue (slide)
                    for element in new_cue.actions[0].slide.presentation.base_slide.elements:
                        # update element UUID
                        element.element.uuid.string = str(uuid.uuid4())
                        if (element.element.name == "Traditional"):
                            rtf_data_bytes = element.element.text.rtf_data
                            rtf_data_str = str(
                                rtf_data_bytes, encoding="utf-8")
                            rtf_data_str = rtf_data_str.replace(
                                "Traditional", lines[i])
                            element.element.text.rtf_data = bytes(
                                rtf_data_str, encoding="utf8")
                        elif (element.element.name == "Simple"):
                            rtf_data_bytes = element.element.text.rtf_data
                            rtf_data_str = str(
                                rtf_data_bytes, encoding="utf-8")
                            rtf_data_str = rtf_data_str.replace("Simple", "")
                            element.element.text.rtf_data = bytes(
                                rtf_data_str, encoding="utf8")
                        elif (element.element.name == "English"):
                            if len(lyrics.english[label]) >= i + 1:
                                rtf_data_bytes = element.element.text.rtf_data
                                rtf_data_str = str(
                                    rtf_data_bytes, encoding="utf-8")
                                rtf_data_str = rtf_data_str.replace(
                                    "English", lyrics.english[label][i])
                                element.element.text.rtf_data = bytes(
                                    rtf_data_str, encoding="utf8")
                        elif (element.element.name == "Pinyin"):
                            rtf_data_bytes = element.element.text.rtf_data
                            rtf_data_str = str(
                                rtf_data_bytes, encoding="utf-8")
                            rtf_data_str = rtf_data_str.replace("Pinyin", "")
                            element.element.text.rtf_data = bytes(
                                rtf_data_str, encoding="utf8")

            # output lyrics pro file in the output folder
            with open(config_parser['LYRICS']['output_path'] + lyrics.traditional["[Title]"][0]+".pro", "wb") as output_file:
                output_file.write(presentation.SerializeToString())
                output_file.close()

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
