"""Exact comparison of the two inherited targets and new constraint data."""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def replay():
    old5 = load('face5', HERE/'STRAT8/zero_face.py')
    oldN = load('faceN', HERE/'STRAT13/STRAT12/STRAT10/zero_face.py')
    a = old5.construct(); b = oldN.construct()
    p5 = {m: F(str(c)) for m,c in a[-1].items()}
    pN5 = {m[:6]: F(str(c)) for m,c in b[-1].subs(b[0].gens[-1],-1).items()}
    assert pN5 == {m: 2*c for m,c in p5.items()}
    assert max(m[-1] for m in b[-1]) == 2
    from exact_bernstein import data
    target, gs = data()
    assert {m: F(c*80) for m,c in target.items()} == p5
    rr,t,V,R,M,delta,Q,tau,D,edges,Pi,num = a
    expected = dict(orientation=t*t-1-rr.gens[5]**2,
                    order12=V[1][0]-V[0][0],order23=V[2][0]-V[1][0],
                    x3bound=V[2][0]+1,
                    spectral00=5*t-M[0][0],spectral11=5*t-M[1][1],
                    connected=25*t*t-5*t*tau+delta,rank=delta,
                    ratio=784*delta-75*tau*tau,
                    scale_guard=103*D-200*tau,
                    scale14=40000*(tau*tau-4*delta)-(103*D-200*tau)**2)
    expected.update({'row'+str(i):4*t-R[i][i] for i in range(5)})
    expected.update({'g'+str(i)+str(j):g for (i,j),g in edges.items() if (i,j)!=(3,4)})
    assert gs == {k:{m:int(c) for m,c in p.items()} for k,p in expected.items()}
    # Recover chart coordinates uniquely from the physical matrix S and lambda
    # when z>0, as at all nine equality centers.
    assert 10*R[3][3]==10*t*t
    assert all(10*R[i][3]==10*t*V[i][0] for i in range(5))
    assert R[4][4]==1+rr.gens[5]**2
    assert all(R[i][4]+V[i][0]==V[i][1]*rr.gens[5] for i in range(5))
    # Re-derive the physical T5 numerator directly from its trace definition.
    # S=2R/D, lambda=10t/D, Q_S=Q/delta, Pi=Pi/(5delta).
    direct = delta*(1800*t*tau-360*sum(R[i][j]**2 for i in range(5) for j in range(5)))
    direct += 120*sum(Pi[i][j]*R[i][j]**2 for i in range(5) for j in range(5))
    direct += (D-10*t)*(60*tau*delta-20*sum(Pi[i][i]*R[i][i] for i in range(5)))
    direct -= 360*sum(g*(2*delta-Q[i][i]-Q[j][j]+2*Q[i][j])*(R[i][i]+R[j][j]-2*R[i][j]) for (i,j),g in edges.items())
    assert direct == num
    tr2=sum(R[i][j]**2 for i in range(5) for j in range(5))
    Mn=sum(Q[i][i]*R[i][i] for i in range(5))
    U=sum(Q[i][i]*sum(R[i][j]**2 for j in range(5)) for i in range(5))
    R1=sum(Q[i][j]*R[i][j]**2 for i in range(5) for j in range(5))
    R2=sum(Q[i][i]*R[i][j]*R[j][j] for i in range(5) for j in range(5))
    invariant=(14*D+4*tau)*(10*Mn-2*tau*delta)+240*delta*tr2
    invariant-=120*delta*sum(R[i][i]**2 for i in range(5))
    invariant+=-720*U+120*R1+360*R2
    assert invariant==num
    result = dict(label='PROVED (verify_targets.py)',
                  identity='C_N(q=-1)=2*Cface; C_N=10(N-2)^2 D^2 Delta T_N',
                  T5='Cface/(45 D^2 Delta)',T6='C_N(q=0)/(160 D^2 Delta)',
                  target_terms=len(p5),target_divisor=80,
                  ratio='r>3/25',scale='a>103/200',
                  scale_guard='103D-200tau>=0 on whole box',
                  scale_constraint='40000(tau^2-4Delta)-(103D-200tau)^2>=0')
    (HERE/'target_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['label']+': '+result['identity'],flush=True)
    return result

if __name__ == '__main__':
    replay()
