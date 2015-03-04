from muse.scales.minor import NaturalMinorScale
from muse.chords import chord, HALF_DIMINISHED_SEVENTH
from muse.tone import Tone


def take(it, n):
    for _ in range(n):
        yield next(it)


# 7 notes in A4 Natural Minor
for note in take(NaturalMinorScale(Tone(0)).acending(), 7):
    print(chord(note, HALF_DIMINISHED_SEVENTH))
