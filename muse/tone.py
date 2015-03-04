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

TONE_NAMES = ["A", "B♭", "B", "C", "C♯", "D", "E♭", "E", "F", "F♯", "G", "G♯"]

SEMITONE = 100
WHOLETONE = SEMITONE * 2



class Tone(object):

    def __init__(self, value):
        """
        `value` is defined as the number of cents above (positive) or below
        (negitive) ISO16 (A440) - A above middle C. Semitones align with
        100 Cents. There are 12 Semitones in octive, making 1200 cents an octive
        above the root value.
        """
        self.value = value

        # Firstly, let's store if we're exactly tuned, or off.
        self._modulo = self.value % 100  # Fractions of a semitone (cents)
        self._semitones = self.value // 100
        self._octave = self.value // 1200
        name = TONE_NAMES[self._semitones % 12]
        # We start on A4, so octive adds to 4.
        octave_offset = 4 + self._octave
        full_name = "{}{}".format(name, octave_offset)

        if self._modulo == 0:
            self._tone_name = full_name
        else:
            self._tone_name = "{} cents above {}".format(self._modulo, full_name)

    def relative_tone(self, increment):
        """
        Create a new Tone `increment` cents above or below this Tone.
        """
        return Tone(self.value + increment)

    def __str__(self):
        return "<Tone: {}>".format(self._tone_name)

    def __repr__(self):
        return "<Tone: {}>".format(self._tone_name)


    def to_midi(self):
        if self._modulo != 0:
            """
            XXX: We should be able to use the pitch bend stuff in MIDI to
                 express this. Not quite sure how, yet. Anyway, someone
                 smarter than me should do that.
            """
            raise ValueError("Error: Can't convert sub-semitones to MIDI.")
        A4 = 69
        return A4 + self._semitones
