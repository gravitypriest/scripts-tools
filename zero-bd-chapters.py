'''
Split a multi-episode Blu-ray chapters file,
reset the first timestamp in each resulting
file to zero, adjust the rest accordingly.
'''

import sys, argparse

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
    return ':'.join((h,m,s)) + '.' + ms

def main():
    parser = argparse.ArgumentParser(description='Split a multi-episode Blu-ray chapter timestamps file to multiple chapter files, adjusted for time.')
    parser.add_argument('--file', metavar='<path>', help='Input file', required=True)
    parser.add_argument('--start', metavar='<num>', type=int, help='Start offset -- e.g. 3 will start at the 3rd timestamp', required=False, default=0)
    parser.add_argument('--chaps', metavar='<num>', type=int, help='Number of chapters per episode', required=True)
    args = parser.parse_args()

    total_chap = args.chaps
    in_fname = args.file
    chapter_set = []
    all_sets = []
    offset_ctr = 0
    start_offset = args.start

    try:
        with open(in_fname) as inFile:
            for line in inFile:
                if offset_ctr < start_offset:
                    offset_ctr += 1
                    continue
                chapter_set.append(line)
                if len(chapter_set) == total_chap:
                    all_sets.append(chapter_set)
                    chapter_set = []                
             
        for chapter_set in all_sets:
            first_chapter = timestamp2Seconds(chapter_set[0])
            part = all_sets.index(chapter_set) + 1
            out_fname = in_fname.split('.')[0] + '_out_' + str(part) + '.txt'
            with open(out_fname,'w') as outFile:
                for chapter in chapter_set:
                    chapter_time = timestamp2Seconds(chapter)
                    adjusted_time = seconds2Timestamp(chapter_time - first_chapter)
                    outFile.write(adjusted_time+'\n')
            print 'Chapters retimed and written to ' + out_fname
    except IOError:
        print 'Please enter a valid filename!'
        exit()

if __name__ == "__main__":
    main()