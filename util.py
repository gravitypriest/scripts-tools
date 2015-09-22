def bdTimestampToSeconds(timestamp):
    # takes BD-formatted timestamp, returns total seconds
    timeParts = timestamp.split(':')
    h = float(timeParts[0])*60*60
    m = float(timeParts[1])*60
    s = float(timeParts[2])
    return h + m + s

def secondsToBdTimestamp(seconds):
    # takes seconds, returns BD-formatted timestamp
    h = str(int(seconds / 60 / 60)).zfill(2)
    m = str(int(seconds / 60 % 60)).zfill(2)
    s = str(int(seconds % 60)).zfill(2)
    ms = str(seconds).split('.')[1].zfill(3)
    return ':'.join((h,m,s))+'.'+ms