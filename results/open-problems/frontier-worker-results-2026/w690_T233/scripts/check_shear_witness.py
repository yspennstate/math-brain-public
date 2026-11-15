"""Deterministic two-dimensional algebra checks, no random/training sweep."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=65
I=mp.eye(2); k=mp.sqrt(mp.mpf(5)/4)
records=[]
for L in [16,32,128,512,2048]:
    m=L; n=L-2; t=mp.sqrt(m)/n; theta=mp.pi/(2*n)
    w=mp.tan(theta); u=w*w/t; rho=mp.sqrt(1+w*w)
    B=mp.matrix([[1,t],[0,1]]); A=mp.matrix([[1,t],[-u,1]])
    v=mp.matrix([k,0]); z=mp.matrix([0,k])
    a=mp.matrix([k,-u/k]); b=mp.matrix([-u/k,k])
    D0=[B.T*B-v*v.T,B.T*B-B*B.T,z*z.T-B*B.T]
    D1=[A.T*A-a*a.T,A.T*A-A*A.T,b*b.T-A*A.T]
    expected=[mp.diag([u*u,-u*u/(k*k)]),mp.diag([u*u,-u*u]),mp.diag([u*u/(k*k),-u*u])]
    err=max(mp.norm(D1[j]-D0[j]-expected[j]) for j in range(3))
    P=A**n
    Pformula=rho**n*mp.matrix([[0,t/w],[-u/w,0]])
    assert mp.norm(P-Pformula)<mp.mpf('1e-50')
    assert err<mp.mpf('1e-55')
    gram=mp.norm(P*a)**2
    gf=rho**(2*n)*w*w*(1/(k*k)+k*k*n*n/m)
    assert abs(gram-gf)<mp.mpf('1e-50')
    out=mp.sqrt(m)*(b.T*P*a)[0]
    of=n*rho**n*w*(w*w/(k*k)-k*k)
    assert abs(out-of)<mp.mpf('1e-50')
    # Direct products, independently evaluating the exact scalar output kernel.
    prefixes=[a]; suffixes=[b]
    for j in range(n):
        prefixes.append(A*prefixes[-1]); suffixes.append(A.T*suffixes[-1])
    kernel=mp.norm(prefixes[-1])**2+mp.norm(suffixes[-1])**2
    kernel+=sum(mp.norm(prefixes[j])**2*mp.norm(suffixes[n-1-j])**2 for j in range(n))
    assert n*w*w<=4/n
    assert n*n*w**4<=16/(n*n)
    target=-k*k*mp.pi/2
    records.append(dict(L=L,W_drift=float(n*w*w),imbalance_drift=float(n*n*w**4),
                        endpoint_gram=float(gram),output=float(out),loss=float((out-target)**2/2),
                        kernel_over_L=float(kernel/L),algebra_error=float(err)))
assert records[-1]['endpoint_gram']<records[0]['endpoint_gram']
assert abs(records[-1]['kernel_over_L']-25/128)<0.003
result={'pass':True,'scope':'Deterministic 2x2 identities only, not Gaussian or actual-GD experiment.',
        'precision_digits':mp.mp.dps,'kernel_limit':25/128,'records':records}
outpath=Path(__file__).resolve().parents[1]/'logs/shear_witness_check.json'
outpath.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
