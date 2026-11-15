"""Integer SOS replay: no solver, numerical arrays or floating eigenvalues."""
import json
from pathlib import Path
from sympy.polys.domains import QQ
from rank3_target55 import target
from inherited20.inherited19.inherited18.inherited17.memory_guard import install

def full(G):return [[G[max(i,j)][min(i,j)]for j in range(len(G))]for i in range(len(G))]
def main():
    install(300_000_000);cert=json.loads(Path('rank3_sos55.json').read_text())
    assert cert['schema']==1 and cert['margin']=='1/5' and cert['gamma']==4
    rr,M,gs=target();D=cert['gram_denominator'];Df=cert['factor_denominator']
    assert isinstance(D,int)and D>0 and isinstance(Df,int)and Df>0 and Df*Df%D==0
    assert [b['key']for b in cert['blocks']]==['free0',*gs]
    actual=[[rr.zero for j in range(4)]for i in range(4)];records=[]
    for block in cert['blocks']:
        n=block['n'];dim=block['dim'];mons=block['mons'];G=full(block['G']);L=block['chol'];scale=Df*Df//D
        assert n in (1,4) and dim==n*len(mons)
        assert all(len(m)==6 and all(isinstance(e,int)and e>=0 for e in m)and sum(m)<=2 for m in mons)
        assert all(len(row)==i+1 for i,row in enumerate(block['G']))
        assert len(L)==dim and all(len(row)==i+1 for i,row in enumerate(L))
        assert all(isinstance(a,int)for row in G+L for a in row)
        caps=[0]*dim;diag=[0]*dim
        for i in range(dim):
            for j in range(i+1):
                val=scale*G[i][j]-sum(L[i][k]*L[j][k]for k in range(j+1))
                if i==j:diag[i]=val
                else:caps[i]+=abs(val);caps[j]+=abs(val)
        assert all(a>b for a,b in zip(diag,caps)),block['key']
        records.append(dict(key=block['key'],dim=dim,minimum_integer_diagonal_dominance_gap=str(min(a-b for a,b in zip(diag,caps)))))
        g=rr.one if block['key']=='free0'else gs[block['key']]
        for v in range(dim):
            for u in range(v+1):
                power=tuple(a+b for a,b in zip(mons[u//n],mons[v//n]));i,j=sorted((u%n,v%n));fac=2 if i==j and u!=v else 1
                pol=rr.from_dict({power:QQ(fac*G[u][v],D)})*g
                if n==4:actual[i][j]+=pol
                else:
                    for a in range(4):actual[a][a]+=pol
    for i in range(4):
        for j in range(i,4):assert actual[i][j]==M[i][j],(i,j)
    Path('rank3_certificate55_checks.json').write_text(json.dumps(dict(label='PROVED (rank3_certificate55.py)',single_carrier_Tstar_margin_at_k5='1/5',target_gamma=4,blocks=records,all_polynomial_coefficients_equal=True),indent=2)+'\n')
    print('PROVED (rank3_certificate55.py): rank-three zero-edge single carrier with tied edge has Tstar>=1/5 at k=5; 16 integer PSD witnesses and full rational polynomial identity.')
if __name__=='__main__':main()
