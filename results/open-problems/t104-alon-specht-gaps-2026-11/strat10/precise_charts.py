"""PROVED: improve inherited square-root enclosure by exact column rescaling.
Independent positive rescaling of U,W leaves every normalized frame datum and
chart unchanged. It keeps the inherited absolute root tolerance meaningful
for large integer witnesses. All resulting coordinates remain rational intervals.
"""
from fractions import Fraction as F
from face_intervals import source_chart as inherited_chart

def source_chart(source,permutation=None):
    scaled=dict(source)
    for key in ('U','W'):
        norm=max(abs(v)for v in source[key]);assert norm>0
        scaled[key]=[F(v,norm)for v in source[key]]
    return inherited_chart(scaled,permutation)
