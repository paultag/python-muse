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

from muse.scales.chromatic import ChromaticScale
from muse.tone import Tone

def take(it, count):
    for _ in range(count):
        yield next(it)


def test_scale_acending_iteratation():
    cs = ChromaticScale(Tone(0))  # A4
    series = list(take(cs.acending(), 13))
    assert [x._tone_name for x in series] == [
        'A4', 'B♭4', 'B4', 'C4', 'C♯4', 'D4', 'E♭4',
        'E4', 'F4', 'F♯4', 'G4', 'G♯4', 'A5']


def test_scale_decending_iteratation():
    cs = ChromaticScale(Tone(0))  # A4
    series = list(take(cs.decending(), 13))
    assert [x._tone_name for x in series] == [
        'A4', 'G♯3', 'G3', 'F♯3', 'F3', 'E3', 'E♭3',
        'D3', 'C♯3', 'C3', 'B3', 'B♭3', 'A3']


def test_scale_acending_iteratation_range():
    cs = ChromaticScale(Tone(0))  # A4
    series = list(cs.acending())
    assert [x._tone_name for x in series] == [
        'A4', 'B♭4', 'B4', 'C4', 'C♯4', 'D4', 'E♭4',
        'E4', 'F4', 'F♯4', 'G4', 'G♯4', 'A5']


def test_scale_acending_iteratation_range():
    cs = ChromaticScale(Tone(0))  # A4
    series = list(take(cs.forever_acending(), 25))
    assert [x._tone_name for x in series] == [
        'A4', 'B♭4', 'B4', 'C4', 'C♯4', 'D4', 'E♭4',
        'E4', 'F4', 'F♯4', 'G4', 'G♯4', 'A5',
        'B♭5', 'B5', 'C5', 'C♯5', 'D5', 'E♭5',
        'E5', 'F5', 'F♯5', 'G5', 'G♯5', 'A6']
