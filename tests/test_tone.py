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

from muse.tone import Tone, note_to_cents, str_to_cents, str_to_tone


def test_tone_name_Bb():
    tone = Tone(100)
    x = tone._tone_name
    assert x == "B♭4"
    assert note_to_cents("B♭", 4) == 100


def test_tone_name_Eb4():
    tone = Tone(600)
    x = tone._tone_name
    assert x == "E♭4"
    assert note_to_cents("E♭", 4) == 600


def test_tone_name_Eb5():
    tone = Tone(1200 + 600)
    x = tone._tone_name
    assert x == "E♭5"
    assert note_to_cents("E♭", 5) == 1200 + 600


def test_tone_name_Eb5_plus():
    tone = Tone(605)
    x = tone._tone_name
    assert x == "5 cents above E♭4"


def test_tone_str_Eb5_plus_str():
    tone = Tone(605)
    assert str(tone) == "<Tone: 5 cents above E♭4>"


def test_tone_str():
    assert str_to_cents("E♭4") == 600
    assert str_to_cents("A4") == 0
    assert str_to_cents("C102") == 117900
    assert str_to_cents("C♯2") == -2000


def test_tone_tone():
    assert str_to_tone("E♭4").value == 600
    assert str_to_tone("A4").value == 0
    assert str_to_tone("C102").value == 117900
    assert str_to_tone("C♯2").value == -2000
