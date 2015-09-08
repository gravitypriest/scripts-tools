'''
Checks for timing conflcts in *.ass subtitle file.
Specifically, checks whether the start time of a 
line is earlier than the end time of the previous line.

Usage: subtitle-timing-confilict.py <file.ass>
'''

import sys

def timestamp2Seconds(timestamp):
    timeParts = timestamp.split(':')
    h = float(timeParts[0])*60*60
    m = float(timeParts[1])*60
    s = float(timeParts[2])

    return h + m + s

def main():
    try:
        prevEndTime = None
        with open(sys.argv[1]) as inFile:
            for line in inFile:
                if line.startswith('Dialogue: '):
                    dlgArr = line.split('Dialogue: ')[1].split(',', 9)
                    beginTime = dlgArr[1]
                    endTime = dlgArr[2]
                    # print just timestamps and dialogue
                    printedLine = ','.join([dlgArr[1],dlgArr[2],dlgArr[9]])
                    if prevEndTime:
                        if timestamp2Seconds(beginTime) < timestamp2Seconds(prevEndTime):
                            print ('WARNING: Subtitle start time is earlier than previous end time ---\n'
                                '--> Current line:  ' + printedLine + ''
                                '--> Previous line: ' + prevLine + '\n')
                    prevEndTime = endTime
                    prevLine = printedLine
    except IOError:
        print 'Please enter a valid filename!'
        exit()
    except IndexError:
        print 'Please enter a file!'
        exit()

if __name__ == "__main__":
    main()