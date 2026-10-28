from pathlib import Path
helper=Path(__file__).resolve().parents[2]/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(helper.read_text(encoding='utf-8').split("rows=[];candidates=0;sets=0;wins=")[0],str(helper),'exec'))
from profile import reference,core_characters
old=R.parent/'20261023T105418Z-account03-A014-overlap-beyond-worst-case-read/code/independent.py'
namespace={'__file__':str(Path(__file__).resolve())}
exec(compile(old.read_text(encoding='utf-8').split("src=read(R/'out/check.json')")[0],str(old),'exec'),namespace)
direct_mass=namespace['direct_mass'];mass_cases=0;clique_cases=0;fourier_cases=0
for a in (1,2):
    b=3*a;n=a+b;universe=list(itertools.combinations(range(a),2))
    for mask in range(1<<len(universe)):
        H=tuple(e for j,e in enumerate(universe) if mask>>j&1);table,Z,q=reference(a,b,H)
        edges=list(H)+[(u,v) for u in range(n) for v in range(max(a,u+1),n)]
        # Direct unmatched-set/perfect-matching enumeration on EVERY labelled set.
        total=F(0)
        for S in range(1,1<<n):
            actual=direct_mass(n,edges,S);key=(S&((1<<a)-1),(S>>a).bit_count())
            ck(actual==table[key]);total+=actual;mass_cases+=1
        ck(total==Z)
for a in (1,2,3):
    H=tuple(itertools.combinations(range(a),2))
    for b in (3*a,3*a+1):
        n=a+b;lam=F(1,n-1);table,Z,q=reference(a,b,H)
        for (S,l),actual in table.items():
            k=S.bit_count()+l;r=k//2
            base=F(math.factorial(2*r),2**r*math.factorial(r))*(lam/48)**r
            expected=base if k%2==0 else base*(2*r+1)*lam*F(3*n-2*r-3,96)
            ck(actual==expected);clique_cases+=1
for b in (9,10):
    a=3;n=a+b;A=(1<<a)-1
    for truth in range(256):
        g=[(truth>>x)&1 for x in range(8)];N=sum(g);t=core_characters(g)
        values=[1-2*int((g[x&A] if x>>a==0 else 0)+(int(x&A==0 and (x>>a).bit_count()==1))) for x in range(1<<n)]
        fh=walsh(values)
        for S,coefficient in enumerate(fh):
            expected=(1<<n)-2*(N+b) if S==0 else -2*(t[S&A]+b-2*(S>>a).bit_count())
            ck(coefficient==expected);fourier_cases+=1
out={'direct_nonempty_masses':mass_cases,'closed_clique_profiles':clique_cases,'full_table_Fourier_coefficients':fourier_cases,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'peer_review':'PENDING; same-author independent implementation'}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
