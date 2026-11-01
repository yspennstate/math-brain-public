from pathlib import Path
prefix=Path(__file__).with_name('gu_independent.py').read_text(encoding='utf-8').split('\nstart=time.monotonic()')[0]
exec(compile(prefix,'standalone direct GU primitives','exec'))
@lru_cache(None)
def nonempty(a):
    s=F(sum(a),len(a));return add(upper(a),times(log(s*s),s*s) if s else {})
def gv(a,coords):return add(*(add(nonempty(a),times(add(nonempty(cut(a,i,0)),nonempty(cut(a,i,1))),-F(1,2))) for i in coords))
start=time.monotonic();fixtures=[(0,(-1,1,1,1)),(63,(-1,1,-1,1)),(0,(1,1,1,1)),(63,(-1,-1,-1,1))]
for v,a in fixtures:
    delta=F(1,64);seed=tuple((-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1) for x in range(64));f=tuple(seed[x]*(a[z] if x==v else 1) for z in range(4) for x in range(64))
    P=spectrum(f);m=F(sum(a),len(a));R=add(*(times(log(sum(P[T] for T in range(256) if T&S==S)/p),p) for S,p in enumerate(P[:64]) if S and p),num(delta*3*(1-m*m)))
    same(nonempty(f),add(times(nonempty(a),delta),R));ge(R)
    I=influence(f,range(6));Gd=gv(f,range(6));Gc=gv(f,range(6,8));Ga=gv(a,range(2))
    ge(add(num(243),times(Gd,-1)));ge(add(times(Ga,delta),num(F(21,2)),times(Gc,-1)))
    ge(add(times(Ga,delta),num(256*I),times(add(Gd,Gc),-1)))
    ge(add(times(nonempty(a),delta),num(24*I),times(nonempty(f),-1)))
    assert time.monotonic()-start<120
out={'status':'PASS','cases':4,'assertions':tests,'elapsed_seconds':time.monotonic()-start,'representation':'direct character/direct upward sums; standalone48-term arithmetic shared with independent replay','review':'author reproduction, not independent-person review'}
(ROOT/'out/v_independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
