"""Exact local theorems, algebraic expansions and finite collar partition replay.

All sign decisions use rational arithmetic; no float or numerical LP is imported.
The inherited Bernstein module uses NumPy object arrays of exact integers.
"""
import sys,json,time
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from collar_algebra import BASES,chart,part,local_data,physical_ball_data,connected_expansion
from collar_boxes import point_bank,collar_record
from chart_jets import expansions

HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'STRAT12'))
from exact_bernstein import verify_certificate,volume

def local_proofs():
    sys.path.append(str(HERE/'STRAT12/STRAT11'))
    from corner_algebra import verify_invariant_formula
    assert verify_invariant_formula()
    result={}
    for kind in BASES:
        local=local_data(kind);rr,B,K,gap,den,Qn,weights,num=chart(kind)
        assert part(num,0)==0
        assert all(sum(b[j]for b in B)==0 for j in range(2))
        assert all(sum(Qn[i][j]for j in range(5))==0 for i in range(5))
        assert sum(Qn[i][i]for i in range(5))==2*den
        assert all(sum(Qn[i][k]*Qn[k][j]for k in range(5))==den*Qn[i][j] for i in range(5)for j in range(5))
        assert all(sum(Qn[i][k]*gap[k][j]for k in range(5))==den*gap[i][j] for i in range(5)for j in range(5))
        assert sum(weights.values())==1
        assert sorted(str(part(w,0))for w in weights.values())==(['0']*8+['1/2']*2 if kind=='edges' else ['0']*7+['1/3']*3)
        # Taylor's integral remainder and the 128 signed Farkas identities:
        # T = L + R_T, omega_i = g_i + R_i, omega_i>=0 imply
        # T >= ||h||_1/6 - (MT+sum caps_i MG_i)||h||_1^2/2.
        # local_data checks the Hessian bounds and rho*M <= 1/12 exactly.
        # Audit the same constants by polynomial cancellation, independently
        # of the quotient Hessian estimate and Taylor's integral formula.
        from collar_algebra import tangent
        L,Q2,active,gs,A,l=tangent(kind)
        R=F(local['derivative_cube_radius'])
        def quadratic_envelope(poly):
            assert all(sum(m)>=2 for m in poly)
            return sum((abs(F(str(c)))*R**(sum(m)-2)for m,c in poly.items()),F(0))
        caps=list(map(F,local['multiplier_caps']))
        alternative=quadratic_envelope(num-den*L)/F(local['gram_lower'])
        alternative+=sum(c*quadratic_envelope(weights[ij]-g)for c,ij,g in zip(caps,active,gs))
        assert alternative<=local['remainder_rounded']
        # Independent second derivation from the six-vertex matrix definitions
        # used in zero_face.py, rather than the invariant moment expression.
        from sympy.polys.domains import QQ
        tau=sum(gap[i][i]for i in range(5));lam=(2+tau)/4
        G=[[gap[i][j]+lam/30 if i<5 and j<5 else (lam*QQ(5,6)if i==j else -lam/6)
            for j in range(6)]for i in range(6)]
        Pi=[[den*(int(i==j)-QQ(1,5))-Qn[i][j]for j in range(5)]for i in range(5)]
        tr=sum(G[i][i]for i in range(6));tr2=sum(G[i][j]**2 for i in range(6)for j in range(6))
        direct=2*den*(lam*tr-tr2)+3*sum(Pi[i][j]*G[i][j]**2 for i in range(5)for j in range(5))
        direct+=(1-lam)*(den*tr/2-QQ(3,4)*sum(Pi[i][i]*G[i][i]for i in range(5)))
        direct-=2*sum(w*(2*den-Qn[i][i]-Qn[j][j]+2*Qn[i][j])*(G[i][i]+G[j][j]-2*G[i][j])
                      for (i,j),w in weights.items())
        assert direct==num
        result[kind]=dict(local=local,physical_ball=physical_ball_data(kind),
                          connected_quadratic=connected_expansion(kind))
    return result

def replay_partition():
    inputs=json.loads((HERE/'STRAT12/remaining_open_boxes.json').read_text())['boxes']
    bank=json.loads((HERE/'collar_cover.json').read_text())
    byid={r['node']:r for r in bank['records']}
    assert len(byid)==len(bank['records'])==9
    assert set(byid)=={b['node']for b in inputs}==set(point_bank())
    # Check that the input is precisely the OPEN frontier of STRAT12's bank,
    # independently of the separately supplied remaining_open_boxes.json.
    inherited=json.loads((HERE/'STRAT12/certificates.json').read_text())
    actual=[]
    def collect(tree,node):
        if tree['kind']=='split':
            for c in tree['children']:collect(c,node)
        elif tree['kind']=='open':actual.append(dict(node=node,**tree))
    for r in inherited['records']:collect(r['tree'],r['node'])
    assert sorted(actual,key=lambda x:x['node'])==sorted(inputs,key=lambda x:x['node'])
    totals=Counter();volumes=Counter();splits=0;maxdepth=0;rows=[]
    for source in inputs:
        node=source['node'];record=byid[node];counts=Counter();depthmax=0
        assert record['box']==source['box']
        def visit(tree,box,depth,path):
            nonlocal splits,maxdepth,depthmax
            if tree['kind']=='split':
                splits+=1;axis=tree['axis']
                assert axis==max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
                assert len(tree['children'])==2
                a,b=box[axis];mid=(a+b)/2;left=box.copy();right=box.copy()
                left[axis]=(a,mid);right[axis]=(mid,b)
                return visit(tree['children'][0],left,depth+1,path+'0')+visit(tree['children'][1],right,depth+1,path+'1')
            assert tree['box']==[[str(a),str(b)]for a,b in box]
            assert tree['depth']==depth and tree['path']==path
            kind=tree['kind'];assert kind in ('positivity','exclusion','collar')
            if kind=='collar':
                cert=collar_record(box,node);assert cert is not None
                assert {k:tree[k]for k in cert}==cert
            else:
                lo,method=verify_certificate(tree)
                assert lo==F(tree['lower']) and method==tree['verification']
            counts[kind]+=1;totals[kind]+=1
            vol=volume(box);volumes[kind]+=vol
            maxdepth=max(maxdepth,depth);depthmax=max(depthmax,depth)
            return vol
        assert visit(record['tree'],[tuple(map(F,x))for x in source['box']],0,'')==volume(source['box'])
        rows.append(dict(node=node,type=point_bank()[node]['kind'],counts=dict(counts),max_additional_depth=depthmax))
    assert sum(volumes.values())==F(189,134217728)
    assert sum(totals.values())==splits+9
    return dict(label='PROVED (verify_collars.py): all nine retained boxes closed on their feasible connected parts',
                counts=dict(totals),volumes={k:str(v)for k,v in volumes.items()},
                split_nodes=splits,max_additional_depth=maxdepth,rows=rows,open_leaves=0)

def main():
    start=time.monotonic()
    # The completed theorem is strict. Audit that none of the older accepted
    # inequalities used to discard a scale strip has only a zero margin.
    # Their actual validity is independently replayed by replay_all.py.
    for name in ('moment_cells.json','fine_cells.json'):
        cells=json.loads((HERE/'STRAT12/STRAT10'/name).read_text())
        assert all(F(c['margin'])>0 for c in cells)
    for path in ('STRAT12/STRAT10/global_cover.json','STRAT12/STRAT11/corner_cover.json'):
        nodes=json.loads((HERE/path).read_text())['nodes']
        assert all(F(n['lower'])>0 for n in nodes if n['kind']=='positive')
    expected=json.loads((HERE/'local_certificates.json').read_text())
    assert expected['physical_charts']==local_proofs()
    assert expected['algebraic_chart_expansions']==expansions()
    print('PROVED (verify_collars.py): both physical local theorems, 256 signed Farkas identities, exact remainders, matrix balls, and all nine algebraic chart expansions.',flush=True)
    result=replay_partition()
    result['elapsed_seconds_NUMERICAL']=time.monotonic()-start
    (HERE/'collar_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'remaining_open_boxes.json').write_text(json.dumps(dict(label='PROVED (verify_collars.py): zero OPEN leaves',boxes=[]),indent=2)+'\n')
    with (HERE/'LOG.md').open('a')as f:f.write('\nPROVED (verify_collars.py): all nine collar partitions replayed; zero OPEN leaves. NUMERICAL elapsed '+str(result['elapsed_seconds_NUMERICAL'])+' seconds.\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
