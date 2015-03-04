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

from .tone import Tone, WHOLETONE, SEMITONE
from itertools import cycle



class ScaleIterator(object):
    def __init__(self, tonic, series):
        self.tonic = tonic
        self._series = series
        self.series = iter(cycle(series))
        self._cur_tone = None

    def interval_count(self):
        return len(self._series)

    def __next__(self):
        if self._cur_tone is None:
            self._cur_tone = self.tonic
            return self._cur_tone
        self._cur_tone = self._cur_tone.relative_tone(next(self.series))
        return self._cur_tone
    next = __next__  # Sigh.


class Scale(object):
    ASCENDING = None
    DECENDING = None

    def __init__(self, tonic):
        self.tonic = tonic

    def acending(self):
        return ScaleIterator(self.tonic, self.ASCENDING)

    def decending(self):
        return ScaleIterator(self.tonic, self.DECENDING)


class SymmetricScale(Scale):
    SCALE = None

    def __init__(self, tonic):
        super(SymmetricScale, self).__init__(tonic=tonic)
        self.ASCENDING = self.SCALE
        self.DECENDING = [-x for x in reversed(self.SCALE)]
