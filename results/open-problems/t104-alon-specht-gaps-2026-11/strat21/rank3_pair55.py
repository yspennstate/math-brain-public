"""Exact transfer for the last zero-edge/zero-edge endpoint pair."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20/inherited19/inherited18/inherited17'))
from lower_formula import x3
from memory_guard import install

def main():
    install(300_000_000);p,q,d,e,b,c,sq1,sq2,y1,y2=s.symbols('p q d e b c sq1 sq2 y1 y2');R=s.Rational
    F1=2*(4-p-sq1)+R(14,5)*b-y1+x3(s.Integer(5),(5-p)/2,R(13,10)-d)
    F2=2*(4-q-sq2)+R(14,5)*c-y2+x3(s.Integer(5),(5-q)/2,R(13,10)-e)
    new=2*(8-p-q-sq1-sq2)+R(5,2)*(b+c)-y1-y2+x3(s.Integer(8),(8-p-q)/2,R(8,5)-d-e)
    f=s.factor(x3(s.Integer(8),(8-p-q)/2,R(8,5)-d-e)-x3(s.Integer(5),(5-p)/2,R(13,10)-d)-x3(s.Integer(5),(5-q)/2,R(13,10)-e)-R(3,10)*(d+e))
    assert s.cancel(new-F1-F2-f-R(3,10)*(d+e-b-c))==0
    assert s.diff(f,d)==(-495*p+625*q-1590)/4000
    assert s.diff(f,e)==(625*p-495*q-1590)/4000
    # Both derivatives <=-17/200 for p,q in [0,2].
    assert s.diff(f,d).subs({p:0,q:2})==-R(17,200)
    assert s.diff(f,e).subs({p:2,q:0})==-R(17,200)
    worst=f.subs({d:R(3,10),e:R(3,10)})
    decomposition=(300*(p-q)**2+200*(p+q)+400*(p*(1-q/2)+q*(1-p/2)))/4000
    assert s.expand(worst+R(9,50)-decomposition)==0
    assert 2*R(1,5)-R(9,50)==R(11,50)
    Path('rank3_pair55_checks.json').write_text(json.dumps(dict(label='PROVED (rank3_pair55.py; rank3_certificate55.py)',comparison=str(f),moment_box='0<=p,q<=2, 0<=B_i<=d_i<=3/10',comparison_lower_bound='-9/50',nonnegative_decomposition=str(decomposition),Tstar_at_k8_margin='11/50'),indent=2)+'\n')
    print('PROVED (rank3_pair55.py; rank3_certificate55.py): zero-edge/zero-edge pair Tstar>=11/50 at k=8; all carrier trace-square and Y terms cancel exactly.')
if __name__=='__main__':main()
