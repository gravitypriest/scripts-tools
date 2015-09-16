'''
Zero out the first chapter in a Blu-ray
chapters file, adjust the rest accordingly.

Usage: zero-bd-chapters.py <file.txt>
'''

import sys

def timestamp2Seconds(timestamp):
    timeParts = timestamp.split(':')
    h = float(timeParts[0])*60*60
    m = float(timeParts[1])*60
    s = float(timeParts[2])
    return h + m + s

def seconds2Timestamp(seconds):
    h = str(int(seconds / 60 / 60)).zfill(2)
    m = str(int(seconds / 60 % 60)).zfill(2)
    s = str(int(seconds % 60)).zfill(2)
    ms = str(seconds).split('.')[1].zfill(3)
    return ':'.join((h,m,s))+'.'+ms

def main():
    try:
        firstLine = True
        firstChapter = 0
        in_fname = sys.argv[1]
        out_fname = sys.argv[1].split('.')[0]+'_out.txt'
        with open(in_fname) as inFile, open(out_fname,'w') as outFile:
            for line in inFile:
                if firstLine:
                    firstChapter = timestamp2Seconds(line)
                    firstLine = False
                adjustedTime = seconds2Timestamp(
                    timestamp2Seconds(line)-firstChapter)
                outFile.write(adjustedTime+'\n')
        print 'Chapters retimed and written to ' + out_fname
    except IOError:
        print 'Please enter a valid filename!'
        exit()
    except IndexError:
        print 'Please enter a file!'
        exit()

if __name__ == "__main__":
    main()