# Copyright (c) Paul R. Tagliamonte <tag@pault.ag>, 2015
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from .tone import Tone
from .scale import SEMITONE

MAJOR = [0, SEMITONE * 4, SEMITONE * 7]
MINOR = [0, SEMITONE * 3, SEMITONE * 7]

MAJOR_7TH = [0, SEMITONE * 4, SEMITONE * 7, SEMITONE * 11]
MAJOR_7TH_DIM = [0, SEMITONE * 3, SEMITONE * 6, SEMITONE * 11]

MINOR_7TH = [0, SEMITONE * 3, SEMITONE * 7, SEMITONE * 10]
DIM_7TH = [0, SEMITONE * 3, SEMITONE * 6, SEMITONE * 9]



def chord(tone, pattern):
    return [tone.relative_tone(x) for x in pattern]
