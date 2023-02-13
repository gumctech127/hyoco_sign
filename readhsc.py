import pandas as pd
import os
import re


filename = 'test.hsc'
oldEnc = 'C:/Users/Admin/Desktop/LED Sign Messges/Weekly Standard/time-temperature.yml'
newEnc = 'C:/Users/GUM User/LED_Sign/Weekly_Standard/time-temperature.yml'

# Sample dict
replacementDict = {'file': {0: filename}, 'old': {0: oldEnc}, 'new': {0: newEnc}}


class Hyoco:
    '''
    Hyoco LED Sign software utilities
    '''
    def __init__(self) -> None:
        pass

    def replace_paths(filename:str, df):
        '''
        For Hyoco schedule (*.hsc) files, replaces utf16 little ended path strings, with new path strings.

        @param  str filename    *.hsc file path
        @param  df    dataframe of file, old, and new path strings
        '''
        df = df.reset_index()  # make sure indexes pair with number of rows
        # Filter by file
        df = df.query("file == @filename")
        for index, row in df.iterrows():
            oldraw = (row['old'].encode('utf16')[2:])
            newraw = (row['new'].encode('utf16')[2:])
            # Prepend the string length as a bytearray
            oldraw = bytearray([len(oldraw)]) + (b'\x00') + (bytearray(oldraw))
            newraw = bytearray([len(newraw)]) + (b'\x00') + (bytearray(newraw))
            
            with open(filename, 'rb') as f:
                hsc = f.read()
       
            # print(oldraw)
            # p = hsc.find(oldraw)
            # print(p)
            # print(hsc[67:94])

            newhsc = hsc.replace(oldraw, newraw)
            outname = os.path.join('out', os.path.basename(filename))
            newFile = open(outname, "wb")
            # write to file
            for byte in newhsc:
                newFile.write(byte.to_bytes(1, byteorder='little'))

    def make_list():
        # df = pd.read_csv('list.csv')
        # print (df)
        # print()
        # dd = df.to_dict()
        # print(dd)

        directory_in_str = 'LED_Sign\Monthly_Schedules'
        files = os.fsencode(directory_in_str)

        datalist = []
        colnames = ['file','old','new']
        df = pd.DataFrame(columns=colnames)
            
        for file in os.listdir(files):
            filename = os.fsdecode(file)
            if filename.endswith(".hsc"):
                
                with open(filename, 'rb') as f:
                    hsc = f.read()

                b'C/x00:/x00'
                # print(oldraw)
                # p = hsc.find(oldraw)
                # print(p)
                # print(hsc[67:94])

                # datalist.append([filename, ,])
                print(filename)
                

if __name__ == "__main__":
    # Hyoco.replace_paths(filename, replacementDict)
    Hyoco.make_list()
