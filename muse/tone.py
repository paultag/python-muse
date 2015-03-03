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

# Base parts here; core Semitone / Wholetone

TONE_NAMES = ["A", "B♭", "B", "C", "C♯", "D", "E♭", "E", "F", "F♯", "G", "G♯"]


class Tone(object):

    def __init__(self, value):
        """
        `value` is defined as the number of cents above (positive) or below
        (negitive) ISO16 (A440) - A above middle C. Semitones align with
        100 Cents. There are 12 Semitones in octive, making 1200 cents an octive
        above the root value.
        """
        self.value = value

    def relative_tone(self, increment):
        """
        Create a new Tone `increment` cents above or below this Tone.
        """
        return Tone(self.value + increment)

    def _tone_name(self):
        """
        Return the name in either:

          > N cents above NOTE
          > NOTE

        Where NOTE is something like C♯4
        """
        # Firstly, let's store if we're exactly tuned, or off.
        modulo = self.value % 100  # Fractions of a semitone (cents)
        semitones = self.value // 100
        octave = self.value // 1200
        name = TONE_NAMES[semitones % 12]
        # We start on A4, so octive adds to 4.
        octave_offset = 4 + octave
        full_name = "{}{}".format(name, octave_offset)

        if modulo == 0:
            return full_name
        return "{} cents above {}".format(modulo, full_name)

    def __str__(self):
        return "<Tone: {}>".format(self._tone_name())

    def __repr__(self):
        return "<Tone: {}>".format(self._tone_name())
