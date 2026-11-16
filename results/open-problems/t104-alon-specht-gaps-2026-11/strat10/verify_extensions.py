"""PROVED: all new rational moment cells, split-scale links, and padding."""
import json
from fractions import Fraction as F
from moment_polytope import vertices
import cells,cubic_cells
from padding import check_allN

def replay():
    vs=vertices(True);assert len(vs)==33;counts={}
    for filename,module,alln in [('fine_cells.json',cells,False),('cubic_cells.json',cubic_cells,False),('stacked_cells.json',cubic_cells,False),('cubic_allN_cells.json',cubic_cells,True)]:
        records=json.load(open(filename))
        for c in records:
            assert module.check(c,vs)==F(c['margin'])
            assert F(c['rhi'])-F(c['rlo'])<=F(1,50)
            if 'base_cover'in c:
                parent=json.load(open(c['base_cover']['file']))[c['base_cover']['index']]
                assert F(parent['rlo'])<=F(c['rlo'])<=F(c['rhi'])<=F(parent['rhi'])
                assert F(c['alo'])<=F(parent['ahi'])<=F(c['ahi'])
            else:assert F(c['alo'])<=(F(64,125)if alln else F(14,25))
            if alln or 'all_N_margins'in c:
                ms=(cubic_cells.check_allN if module is cubic_cells else check_allN)(c,vs)
                assert list(map(F,c['all_N_margins']))==ms
        counts[filename]=len(records);print('PROVED:',filename,len(records),'rational cells replayed;',('all N>=6'if alln else 'N=6'),flush=True)
    return counts
if __name__=='__main__':replay()
