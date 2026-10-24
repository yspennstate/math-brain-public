"""Rationalize and exactly bound the strongest guarded search direction.

The result is negative; this certifies one retained direction, not the entire
36-dimensional Hessian. Candidate selection is fixed by the saved search file.
"""
from pathlib import Path
import json
import sympy as s
from fractions import Fraction as F
from certify import f,logbounds,linlog,enc

OUT=Path(__file__).resolve().parent

def rounded_matrix(real,imag,D):
    n=len(real);M=s.zeros(n)
    def rat(x):return s.Rational(round(float(x)*D),D)
    for i in range(n):
        M[i,i]=rat(real[i][i])
        for j in range(i+1,n):
            M[i,j]=rat(real[i][j])+s.I*rat(imag[i][j]);M[j,i]=s.conjugate(M[i,j])
    return M

def main():
    data=json.loads((OUT/'search_boundary_results.json').read_text())
    row=max(data['rows'],key=lambda x:x['lambda_max'])
    K=rounded_matrix(row['K_real'],row['K_imag'],10**8)
    A=rounded_matrix(row['A_real'],row['A_imag'],10**6)
    n=K.rows;eta=s.Rational(1,1000000)
    # Sylvester's criterion, rational Hermitian determinants.
    minors=[]
    for M in [K-eta*s.eye(n),s.eye(n)-K-eta*s.eye(n)]:
        vals=[f(M[:j,:j].det(method='domain-ge')) for j in range(1,n+1)]
        assert all(x>0 for x in vals)
        minors.append(vals)
    frob=f((A*A).trace());assert frob<4
    # Hence K+tA remains a contraction for every |t|<=eta/2.
    atoms=[]
    for mask in range(2**n):
        bits=[(mask>>i)&1 for i in range(n)]
        M=K-s.diag(*[1-b for b in bits])
        p=f((-1)**(n-sum(bits))*M.det(method='domain-ge'));assert p>0
        T=M.inv(method='DM');R=T*A
        tr=f(s.expand(R.trace()));tr2=f(s.expand((R*R).trace()))
        g=p*tr;h=p*(tr*tr-tr2)
        atoms.append({'mask':mask,'p':p,'g':g,'h':h})
        if mask%16==15:print('rational atoms',mask+1,flush=True)
    assert sum(a['p'] for a in atoms)==1
    assert sum(a['g'] for a in atoms)==0
    assert sum(a['h'] for a in atoms)==0
    fisher=sum(a['g']**2/a['p'] for a in atoms)
    frozen=linlog([-a['h'] for a in atoms],[logbounds(a['p']) for a in atoms])
    curvature=(frozen[0]-fisher,frozen[1]-fisher)
    assert curvature[1]<-F(1,500000)
    result={'status':'strictly_negative_rationalized_direction',
        'source_family':row['family'],'source_variant':row['variant'],
        'source_numeric_hessian_max':row['lambda_max'],
        'kernel_rounding_denominator':10**8,'direction_rounding_denominator':10**6,
        'K':[[str(x) for x in rr] for rr in K.tolist()],
        'A':[[str(x) for x in rr] for rr in A.tolist()],
        'kernel_margin':'1/1000000','feasible_t_interval':['-1/2000000','1/2000000'],
        'shifted_leading_principal_minors':minors,'direction_frobenius_squared':frob,
        'fisher':fisher,'frozen_bounds':frozen,'entropy_curvature_bounds':curvature,
        'entropy_curvature_upper_simple':'-1/500000','atoms':atoms}
    (OUT/'rational_candidate_certificate.json').write_text(json.dumps(enc(result),indent=2)+'\n')
    print('exact curvature interval:',*[float(x) for x in curvature],flush=True)

if __name__=='__main__':main()
