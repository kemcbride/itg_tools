## itg_tools

This repo is for ITG (in the groove) related code that I write that I find useful,
and maybe somehow other people will find it useful.

Right now, it only has two things in it which are very specifically named "prep" and 
"file_size".

#### prep
Pretty generic and intended to be run on a USB stick's In The Groove {2,3}/Songs
directory to "prep" the songs to be run on a machine.

Ideally my script would call the famous `itgoggpatch` but for now, I just run it separately.

Otherwise, the only thing prep does for now is call my `file_size` module's shrinker function.

#### file_size
The file_size module just has a few functions that basically check whether the audio files
for a song are too big, and shrinks the .oggs using avconv. 

*Note:* this is not clever.

It just runs avconv and converts them to quality level 3, which I think I arbitrarily chose
as being "small enough."

I'm putting this up here now as a testament to the fact that finally after trying
to use it twice on a cab and having my code just delete the audio and having to play 
charts without audio, I'll fix it - as I hope I have now - and see that it works.
