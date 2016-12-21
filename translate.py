import sys
from pprint import pprint
import re

def translate_program():
    language_count = 0;
    language = [];
    
    translate_dict_en = {}
    translate_dict_thai = {}

    def count_language():
        first_line = open("translation.txt").readline();
        for i in first_line.split(';'):
            language.append(i.strip())

    def clean_string(s):
        return s.strip().capitalize().replace("  "," ") 
    
    def start_translate():
        for line in open("translation.txt"):
            line = line.strip()
            key, english, thai = line.split(";")
            key = clean_string(key)
            english = clean_string(english)
            thai = clean_string(thai)
            
            #check if name already voted
            translate_dict_en[key] = english
            translate_dict_thai[key] = thai
        write_to_file("thai.txt")
    def write_to_file(language_name):
        f = open(language_name, "w")
        for key in translate_dict_thai:
            xml_string = '<string name="key">value</string>'
            xml_string = xml_string.replace("key",key)
            xml_string = xml_string.replace("value",translate_dict_thai[key])
            re.sub('\+', '', xml_string)
            f.write(xml_string+"\n")
        f.close()
    
    
    # start_translate()
    count_language()

    
if __name__ == '__main__':
    translate_program()