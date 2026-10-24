import itertools, math
import numpy as np

Q=23/12
CSTAR=48*math.sqrt(math.e)*(24/23)**0.25
print('Cstar',repr(CSTAR))
print('Cstar*S0',repr(CSTAR*48**0.125))
print('rank2*S0',repr(8*48**0.125))

def e2_minors(B):
    m,n=B.shape
    return sum(np.linalg.det(B[np.ix_(I,J)])**2
               for I in itertools.combinations(range(m),2)
               for J in itertools.combinations(range(n),2))

def calibrate_gamma(B,target=2.0):
    s=np.linalg.svd(B,compute_uv=False)
    s=s[s>1e-12]
    assert len(s)>=3
    lo=1e-14; hi=max(s)*1e6+1
    for _ in range(300):
        g=(lo*hi)**0.5
        theta=np.sum(s*s/(g*g+s*s))
        if theta>target: lo=g
        else: hi=g
    return (lo*hi)**0.5

def ridge(B,g):
    m,n=B.shape
    KL=B@np.linalg.inv(g*g*np.eye(n)+B.T@B)@B.T
    KR=B.T@np.linalg.inv(g*g*np.eye(m)+B@B.T)@B
    return KL,KR

def anchored(B,i,j):
    m,n=B.shape
    M=0.0
    for k in range(m):
        if k==i: continue
        for l in range(n):
            if l==j: continue
            M += np.linalg.det(B[np.ix_([i,k],[j,l])])**2
    b=B[i,j]
    r=np.delete(B[i,:],j)
    c=np.delete(B[:,j],i)
    C=np.delete(np.delete(B,i,axis=0),j,axis=1)
    exact=np.linalg.norm(b*C-np.outer(c,r),'fro')**2
    return M,exact,b*b*np.linalg.norm(C,'fro')**2,np.dot(r,r)*np.dot(c,c)

rng=np.random.default_rng(1703)
B=rng.normal(size=(5,4))
E=e2_minors(B)
s=np.linalg.svd(B,compute_uv=False)
Esv=sum((s[a]*s[b])**2 for a,b in itertools.combinations(range(len(s)),2))
g=calibrate_gamma(B)
KL,KR=ridge(B,g)
D=np.linalg.det(np.eye(B.shape[0])+B@B.T/g**2)
k=s*s/(g*g+s*s)
p2=g**-4*E/D
p2_direct=0.0
for a,b in itertools.combinations(range(len(k)),2):
    z=k[a]*k[b]
    for c in range(len(k)):
        if c not in (a,b): z*=1-k[c]
    p2_direct+=z
print('random E2 minor/sv diff',abs(E-Esv))
print('theta',np.trace(KL))
print('p2 identity diff',abs(p2-p2_direct))
i=int(np.argmax(np.diag(KL))); j=int(np.argmax(np.diag(KR)))
M,exact,Aterm,Sterm=anchored(B,i,j)
print('anchor identity diff',abs(M-exact))
print('edge-star upper check',M<=2*(Aterm+Sterm)+1e-10)

Bh=np.diag([100.,1.,.1])
Eh=e2_minors(Bh)
gh=calibrate_gamma(Bh)
KLh,KRh=ridge(Bh,gh)
Dh=np.linalg.det(np.eye(3)+Bh@Bh.T/gh**2)
p2h=gh**-4*Eh/Dh
Mh,_,_,_=anchored(Bh,0,0)
print('heavy gamma',gh)
print('heavy diag KL',np.diag(KLh))
print('heavy p2',p2h)
print('heavy anchored ratio',Mh/Eh)
