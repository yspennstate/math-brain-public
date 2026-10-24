import json, math
import numpy as np

H4=np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],dtype=float)
J4=np.diag([1,1,-1,-1])

def check(n,c=1.0):
    assert n%8==0 and n>=16
    U=np.tile(H4,(n//4,1))/math.sqrt(n)
    A=c*U@J4@U.T
    target=np.array([-c,-c*math.sqrt(1-4/n),c*math.sqrt(1-4/n),c])
    deletion_error=0.0
    for i in range(n):
        B=np.delete(np.delete(A,i,0),i,1)
        vals=np.linalg.eigvalsh(B)
        vals=vals[np.abs(vals)>1e-8]
        deletion_error=max(deletion_error,float(np.max(np.abs(vals-target))))
    I=[]; J=[]
    half=(n//4)//2
    for typ in range(4):
        ids=list(range(typ,n,4))
        I+=ids[:half]; J+=ids[half:]
    UI=U[I,:]; UJ=U[J,:]
    M=c*UI@J4@UJ.T
    s=np.linalg.svd(M,compute_uv=False)
    return {
      "n":n,
      "orth_error":float(np.linalg.norm(U.T@U-np.eye(4),ord=2)),
      "deletion_spectrum_max_error":deletion_error,
      "gram_I_error":float(np.linalg.norm(UI.T@UI-0.5*np.eye(4),ord=2)),
      "gram_J_error":float(np.linalg.norm(UJ.T@UJ-0.5*np.eye(4),ord=2)),
      "top_cross_singular_values":[float(x) for x in s[:4]],
      "fifth_cross_singular_value":float(s[4]),
      "row_leverage":8/n,
    }

out={
 "checks":[check(n) for n in (16,24,32,64)],
 "partner_constant":9*math.e*math.sqrt(3)/(2**(1/6)),
}
print(json.dumps(out,indent=2))
