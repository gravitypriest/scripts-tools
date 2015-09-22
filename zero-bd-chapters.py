'''
Split a multi-episode Blu-ray chapters file,
reset the first timestamp in each resulting
file to zero, adjust the rest accordingly.
'''

import sys, argparse
from util import bdTimestampToSeconds, secondsToBdTimestamp

def main():
    parser = argparse.ArgumentParser(description='Split a multi-episode '
        'Blu-ray chapter timestamps file to multiple chapter files, '
        'adjusted for time.')
    parser.add_argument('-f', '--file', metavar='<path>',
        help='Input file', required=True)
    parser.add_argument('-s', '--start', metavar='<num>', type=int,
        help='Start offset -- e.g. 3 will start at the 3rd timestamp',
        required=False, default=0)    
    parser.add_argument('-e', '--end', metavar='<num>', type=int,
        help='End offset -- e.g. 2 will end at the 2nd to last timestamp',
        required=False, default=0)
    parser.add_argument('-c', '--chaps', metavar='<num>', type=int,
        help='Number of chapters per episode', required=True)
    args = parser.parse_args()

    total_chap = args.chaps
    in_fname = args.file
    chapter_set = []
    all_sets = []
    offset_ctr = 0
    start_offset = args.start
    end_offset = args.end

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
            else:
                if end_offset != 0:
                    if len(chapter_set) > end_offset:
                        chapter_set = chapter_set[0:len(
                            chapter_set) - end_offset]
                    else:
                        overlap = end_offset - len(chapter_set)
                        remove_chaps = overlap % total_chap
                        remove_sets = overlap / total_chap

                        if remove_sets > 0:
                            all_sets = all_sets[0:-remove_sets]
                        if remove_chaps > 0:
                            chapter_set = all_sets[-1][0:-remove_chaps]
                            all_sets = all_sets[0:-1]

        if len(all_sets) == 0 and len(chapter_set) == 0:
            print 'No chapters found. Exiting...'

        if len(all_sets) > 0:
            print '%d set(s) of %d chapter(s) found.' % (len(all_sets),
                total_chap)

        if len(chapter_set) != 0 and len(chapter_set) < total_chap:
            if len(all_sets) == 0:
                print 'Not enough chapters to make a set of %d. Exiting...' % (
                    total_chap)
                exit()
            else:
                print '%d chapter(s) left over.' % (len (chapter_set))

        for chapter_set in all_sets:
            first_chapter = bdTimestampToSeconds(chapter_set[0])
            part = all_sets.index(chapter_set) + 1
            out_fname = in_fname.split('.')[0] + '_out_' + str(part) + '.txt'
            with open(out_fname,'w') as outFile:
                for chapter in chapter_set:
                    chapter_time = bdTimestampToSeconds(chapter)
                    adjusted_time = secondsToBdTimestamp(chapter_time - 
                        first_chapter)
                    outFile.write(adjusted_time+'\n')
            print 'Chapters retimed and written to ' + out_fname
    except IOError:
        print 'Please enter a valid filename!'
        exit()

if __name__ == "__main__":
    main()