from pathlib import Path
import json
f=[1 if x.bit_count()>=2 else -1 for x in range(16)]
cofactors=[];partitions=[]
def place(x,A):return sum(((x>>j)&1)<<i for j,i in enumerate(A))
for j in range(4):
    for bit in (0,1):
        A=[i for i in range(4) if i!=j];g=[f[place(x,A)|(bit<<j)] for x in range(8)]
        support=[A[k] for k in range(3) if any(g[x]!=g[x^(1<<k)] for x in range(8))]
        assert support==A
        cofactors.append({'query':j,'value':bit,'truth_table':g,'support':support})
for mask in range(1,15,2):
    A=[i for i in range(4) if mask>>i&1];B=[i for i in range(4) if not mask>>i&1]
    witness=None
    for a in range(1<<len(A)):
        for b in range(1<<len(B)):
            # A product g(A)h(B) obeys f(a,b)f(0,0)=f(a,0)f(0,b).
            lhs=f[place(a,A)|place(b,B)]*f[0]
            rhs=f[place(a,A)]*f[place(b,B)]
            if lhs!=rhs:witness={'a':a,'b':b,'lhs':lhs,'rhs':rhs}
    assert witness is not None
    partitions.append({'A':A,'B':B,'nonproduct_minor':witness})
Path(__file__).resolve().parents[1].joinpath('out/NONMEMBER_CERTIFICATE.json').write_text(json.dumps({'status':'PASS','function':f,'cofactors':cofactors,'partitions':partitions,'conclusion':'all nontrivial products impossible; every potential mux root has child support intersection3>2; no constant/literal root; hence outside grammar'},indent=2)+'\n',encoding='utf-8')
