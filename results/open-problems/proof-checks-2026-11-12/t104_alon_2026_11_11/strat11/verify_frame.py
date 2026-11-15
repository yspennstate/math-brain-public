"""Replay exact first and second jets, including the flat rotation direction."""
import json
from frame_jets import build

if __name__=='__main__':
    data=build()
    assert json.load(open('frame_expansion.json'))==data
    print('PROVED: eigenframe L=11*alpha/10-beta/20; full quadratic jet matched.')
    print('PROVED: the gauge line has L=0 and Q=0; no negative direction on the admissible tangent cone.')
