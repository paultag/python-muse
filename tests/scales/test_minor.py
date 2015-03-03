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

from muse.scales.minor import NaturalMinorScale, HarmonicMinorScale
from muse.tone import Tone

def take(it, count):
    for _ in range(count):
        yield next(it)


NATURAL_MINOR_SCALE = ['B♭4', 'C4', 'C♯4', 'E♭4', 'F4', 'F♯4', 'G♯4', 'B♭5']
# http://en.wikipedia.org/wiki/File:MinorScale.svg


def test_scale_acending_iteratation():
    cs = NaturalMinorScale(Tone(100))  # Bb4
    series = list(take(cs.acending(), 8))
    assert [x._tone_name() for x in series] == NATURAL_MINOR_SCALE


def test_scale_acending_iteratation():
    cs = NaturalMinorScale(Tone(1300))  # Bb5
    series = list(take(cs.decending(), 8))
    assert ([x._tone_name() for x in series] == list(
        reversed(NATURAL_MINOR_SCALE)))


HARMONIC_MINOR_SCALE = ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G♯4', 'A5']


def test_scale_acending_iteratation():
    cs = HarmonicMinorScale(Tone(100))  # A4
    series = list(take(cs.acending(), 8))
    assert [x._tone_name() for x in series] == HARMONIC_MINOR_SCALE


def test_scale_acending_iteratation():
    cs = HarmonicMinorScale(Tone(1200))  # A5
    series = list(take(cs.decending(), 8))
    assert ([x._tone_name() for x in series] == list(
        reversed(HARMONIC_MINOR_SCALE)))
