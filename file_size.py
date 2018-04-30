"""Herein lies the thing that will de-qualitize
    audio that I will play on the Ice Cube arcade machine...

    RIP Audio Quality"""

import os
import sys
import subprocess
from shutil import copyfile

SIZE_LIMIT = 5 * (10 ** 6) # bytes
ALLOWED_FTYPES = ('ogg', 'mp3')

def patch_audio_quality(sm_path):
    audio_files = [
            f for f in os.listdir(sm_path)
            if f.endswith(ALLOWED_FTYPES) and not f.startswith('.')
            ]

    for af in audio_files:
        stats = os.stat(sm_path +'/' + af)
        size = stats.st_size
        if size >= SIZE_LIMIT:
            print >> sys.stderr, af
            print >> sys.stderr, size > SIZE_LIMIT
            passes_check = call_avconv(sm_path, af)
            if not passes_check:
                call_avconv(sm_path, af, q=1)
        else:
            print 'SKIPPING: {} // {}b'.format(af, size)


def call_avconv(sm_path, af, q=3):
    """
    avconv -i Tike\ Tike\ Kardi.ogg -c:a:0 libvorbis -qscal
e:a 3 smaller.ogg -y

    This should... um... ONLY remove the original one,
    IF! the file size is less than LIMIT at least... ie. BE
    CAREFUL bc I am reducing the quality of these files!!! """
    full_path = sm_path + '/' + af
    temp_file = sm_path + '/' + 'temp.ogg'
    FNULL = open(os.devnull, 'w')
    code = subprocess.check_call([
        'avconv',
        '-i', full_path,
        '-c:a:0', 'libvorbis',
        '-qscale:a', str(q),
        temp_file, '-y'], 
        stdout=FNULL, stderr=FNULL)

    # now that we've put the lower quality version into the 
    # temp file, let's move that into the full path, and then
    # delete the temp file
    copyfile(temp_file, full_path)
    os.remove(temp_file)

    if code != 0:
        print >> sys.stderr, "Something went wrong with avconv..."
        print >> sys.stderr, "On: {}".format(full_path)
    else:
        # check new file size
        size = os.stat(full_path).st_size
        if size >= SIZE_LIMIT:
            print >> sys.stderr, "Needs to be smaller..."
            return False
        return True


