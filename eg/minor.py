from muse.scales.minor import NaturalMinorScale
from muse.chords import chord, MINOR_7TH
from muse.tone import Tone


def take(it, n):
    for _ in range(n):
        yield next(it)


# 7 notes in A4 Natural Minor
for note in take(NaturalMinorScale(Tone(0)).acending(), 7):
    print(chord(note, MINOR_7TH))
