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

from .tone import Tone, SEMITONE
from .intervals import (
    PERFECT_UNISON,
    MAJOR_THIRD, MINOR_THIRD,
    DIMINISHED_FIFTH, PERFECT_FIFTH, AUGMENTED_FIFTH,
    DIMINISHED_SEVENTH, MINOR_SEVENTH, MAJOR_SEVENTH,
)

from .intervals import MAJOR_SEVENTH as INT_MAJOR_SEVENTH


# Triad chords
MAJOR = [PERFECT_UNISON, MAJOR_THIRD, PERFECT_FIFTH]
MINOR = [PERFECT_UNISON, MINOR_THIRD, PERFECT_FIFTH]
AUGMENTED = [PERFECT_UNISON, MAJOR_THIRD, AUGMENTED_FIFTH]
DIMINISHED = [PERFECT_UNISON, MINOR_THIRD, DIMINISHED_FIFTH]

# Seventh chords
DIMINISHED_SEVENTH = [PERFECT_UNISON, MINOR_THIRD,
                      DIMINISHED_FIFTH, DIMINISHED_SEVENTH]

HALF_DIMINISHED_SEVENTH = [PERFECT_UNISON, MINOR_THIRD,
                           DIMINISHED_FIFTH, MINOR_SEVENTH]

MINOR_MAJOR_SEVENTH = [PERFECT_UNISON, MINOR_THIRD,
                       PERFECT_FIFTH, INT_MAJOR_SEVENTH]

DOMINANT_SEVENTH = [PERFECT_UNISON, MAJOR_THIRD,
                    PERFECT_FIFTH, MINOR_SEVENTH]

MAJOR_SEVENTH = [PERFECT_UNISON, MAJOR_THIRD,
                 PERFECT_FIFTH, INT_MAJOR_SEVENTH]

AUGMENTED_SEVENTH = [PERFECT_UNISON, MAJOR_THIRD,
                     AUGMENTED_FIFTH, MINOR_SEVENTH]

AUGMENTED_MAJOR_SEVENTH = [PERFECT_UNISON, MAJOR_THIRD,
                           AUGMENTED_FIFTH, INT_MAJOR_SEVENTH]


def chord(tone, pattern):
    return [tone.relative_tone(x) for x in pattern]
