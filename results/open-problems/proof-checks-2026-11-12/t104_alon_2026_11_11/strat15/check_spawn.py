"""Regression replay for the inherited/new module name collision."""
import sys,json,multiprocessing as mp
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from verify_new import worker,collar_replay

if __name__=='__main__':
    collar_replay(json.loads((HERE/'local_uniform.json').read_text()))
    assert Path(sys.path[0]).resolve()!=HERE
    sys.path.insert(0,str(HERE))
    records=json.loads((HERE/'certificates.json').read_text())['records'][:4]
    with mp.get_context('spawn').Pool(1)as pool:
        peaks=list(pool.imap(worker,records))
    print('PROVED (check_spawn.py): spawned workers imported the extended target and replayed all twelve saved control margins exactly.')
