"""Independent exact partition checks and re-evaluation of accepted leaves."""
import json,time,math,resource
from pathlib import Path
from fractions import Fraction as F
from bnb import enclosure
from interval_core import iv

def volume(cell):return math.prod(F(h)-F(l) for l,h in cell)

def path_to(root,cell):
    cur=[[F(l),F(h)] for l,h in root];target=[[F(l),F(h)] for l,h in cell]
    widths=[h-l for l,h in cur];path=[]
    assert all(cur[i][0]<=target[i][0]<target[i][1]<=cur[i][1] for i in range(7))
    while cur!=target:
        i=max(range(7),key=lambda j:(cur[j][1]-cur[j][0])/widths[j])
        mid=sum(cur[i])/2
        if target[i][1]<=mid:cur[i][1]=mid;path.append(0)
        elif target[i][0]>=mid:cur[i][0]=mid;path.append(1)
        else:raise AssertionError('cell not a leaf of the prescribed bisection tree')
    return path

def main():
    iv.dps=45;start=time.monotonic();out=[]
    for name in ('bnb_small','bnb_local_improved','bnb_interior','bnb_interior_full'):
        p=json.loads(Path('data/'+name+'.json').read_text());root=p['root'];tree={}
        cells=[('certified',r['box']) for r in p['certified']]
        cells += [('infeasible',c) for c in p['infeasible']]+[('pending',c) for c in p['pending']]
        for kind,cell in cells:
            path=path_to(root,cell);node=tree
            for bit in path:
                assert 'leaf' not in node
                node=node.setdefault(bit,{})
            assert not node;node['leaf']=kind
        def complete(node):
            if 'leaf' in node:return
            assert set(node)=={0,1}
            complete(node[0]);complete(node[1])
        complete(tree)
        assert sum(volume(c) for _,c in cells)==volume(root)
        for row in p['certified']:
            status,certificate=enclosure(row['box'],p.get('interior_delta'),row.get('method')=='full_hessian')
            assert status=='certified'
        # Recheck each discarded cell as well: no infeasible status is trusted.
        for cell in p['infeasible']:
            status,_=enclosure(cell,p.get('interior_delta'))
            assert status=='infeasible'
        out.append(dict(file=name+'.json',leaf_count=len(cells),partition='exact complete binary partition',
                        accepted_leaves_rechecked=len(p['certified']),discarded_leaves_rechecked=len(p['infeasible']),
                        pending=len(p['pending'])))
        print(out[-1],flush=True)
    result=dict(runs=out,seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/cover_audit.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
