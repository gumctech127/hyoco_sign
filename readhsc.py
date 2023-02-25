import pandas as pd
import os
import re


# filename = 'test.hsc'
# oldEnc = 'C:/Users/Admin/Desktop/LED Sign Messges/Weekly Standard/time-temperature.yml'
# newEnc = 'C:/Users/GUM User/LED_Sign/Weekly_Standard/time-temperature.yml'

# # Sample dict
# replacementDict = {'file': {0: filename}, 'old': {0: oldEnc}, 'new': {0: newEnc}}


class Hyoco:
    '''
    Hyoco LED Sign software utilities
    '''
    def __init__(self, directory='..\Monthly_Schedules') -> None:
        self.directory = directory

    def replace_paths(self, df):
        '''
        For Hyoco schedule (*.hsc) files, replaces utf16 little ended path strings, with new path strings.

        @param  df    dataframe of file, old, and new path strings
        '''
        schedules = df['file'].drop_duplicates().to_list()
        df = df.reset_index()  # make sure indexes pair with number of rows
            
        for filename in schedules:
            # Filter by file
            df2 = df.query("file == @filename")
            with open(os.path.join(self.directory, filename), 'rb') as f:
                newhsc = f.read()
                
            for index, row in df2.iterrows():
                oldraw = (row['old'].encode('utf16')[2:])
                if row['new']:
                    newraw = row['new'].replace(os.sep, '/')
                    newraw = (newraw.encode('utf16')[2:])
                    # Prepend the string length as a bytearray
                    oldraw = bytearray([len(oldraw)]) + (b'\x00') + (bytearray(oldraw))
                    newraw = bytearray([len(newraw)]) + (b'\x00') + (bytearray(newraw))
                    newhsc = newhsc.replace(oldraw, newraw)
            
            outname = os.path.join('out', os.path.basename(filename))
            newFile = open(outname, "wb")
            # write to file
            for byte in newhsc:
                newFile.write(byte.to_bytes(1, byteorder='little'))

    def make_list(self):
        '''
        Make a CSV of Hyoco Schedule files, old yml path, new yml path
        
        @return df  Pandas Dataframe of csv content
        '''
        pathlist = []
        newlist = []
        colnames = ['file','old','new']

        df2 = pd.DataFrame(columns=colnames)

        for filename in os.listdir(self.directory):
            file = os.path.join(self.directory, filename)
            df = pd.DataFrame(columns=colnames)
            if os.path.isfile(file) and filename.endswith('.hsc'):
                with open(file, 'rb') as f:
                    hsc = f.read()

                path_pattern = b'C\x00:\x00.*?\x00(?:\x00\x00)'
                pathlist = re.findall(path_pattern, hsc)
                # Remove duplicates
                pathlist = list(set(pathlist))
                pathlist16=[]
                newlist = []
                for path in pathlist:
                    try:
                        pathlist16.append(path.decode('utf16').strip('\x00'))
                        # newlist.append(self.getNewPath(pathlist16[-1]).replace('\\','/'))
                        new = self.getNewPath(pathlist16[-1])
                        # new = new.replace('Sunday Worship Hrs REVISED-1_Mask.yml','Sunday Worship Hrs REVISED-2_Mask.yml')
                        # newsep = new.replace(os.sep, '/')
                        newlist.append(new)
                    except Exception as e:
                        print ('Error during path search.  {}'.format(e))
                df['old'] = pathlist16
                df['file'] = filename
                df['new'] = newlist
                # print(df)
                # Filter out duplicate old paths per schedule
                # df = df.drop_duplicates(subset=['old'])
                df2 = pd.concat([df2, df], ignore_index=True)
                # print(df2)

        # Save to csv file
        df2.to_csv('list.csv', index=False)
        return df2

    def getNewPath(self, inpath:str="") -> str:
        '''
        Search the file system, starting at the parent of the default schedules folder for each old yml filename, returning the new yml path.

        @param inpath   str old_yml_path

        @retval outpath str new_yml_path
        '''
        
        outpath = None
        yml = os.path.basename(inpath)
        # find it first
        for root, dirs, files in os.walk(os.path.join(self.directory,".."), topdown=False):
            for name in files:
                if name == yml:
                    outpath = (os.path.abspath(os.path.join(root, name)))
                    # print(os.path.join(root, name))
                    break
            # for name in dirs:
            #     print(os.path.join(root, name))
                    
        return outpath                


if __name__ == "__main__":
    # Hyoco.replace_paths(filename, replacementDict)
    H = Hyoco(directory='..\Monthly_Schedules')
    # H.make_list()
    # print(H.getNewPath('C:/Users/Admin/Desktop/LED Sign Messges/Weekly Standard/time-temperature.yml'))
    H.replace_paths(H.make_list())