"""Replay rotation curve and its inherited unrotated residual certificate."""
import json,os
from rotation_obstruction import build,HERE,SOURCE,fc

if __name__=='__main__':
    assert json.loads((HERE/'rotation_obstruction.json').read_text())==build()
    previous=os.getcwd()
    try:
        os.chdir(SOURCE)
        assert fc.build()==json.loads((SOURCE/'pressure_family.json').read_text())
    finally:os.chdir(previous)
    print('PROVED: rotated residual curve has T=o(frame distance squared); inherited family filters replayed.')
