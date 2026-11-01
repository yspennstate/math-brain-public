import numpy as np

rng=np.random.default_rng(20260923)
max_ortho=0.0
max_det_rel=0.0
checks=0
for n in [6,10,25,80]:
    for r in [3,4,6]:
        if r>=n:
            continue
        for theta in [1/4,1/8,1/16]:
            for _ in range(50):
                Z=rng.normal(size=(n,r))
                R=np.linalg.qr(Z)[0][:,:r]
                p=np.sum(R*R,axis=1)
                H=np.where(p>theta)[0]
                T=np.where(p<=theta)[0]
                S=R[H].T@R[H] if len(H) else np.zeros((r,r))
                eps=np.linalg.eigvalsh(S)[-1]
                if eps<=1-2*theta+1e-12:
                    G=np.eye(r)-S
                    vals,vecs=np.linalg.eigh(G)
                    g=vals[0]
                    Gmh=vecs@np.diag(vals**-0.5)@vecs.T
                    W=R[T]@Gmh
                    max_ortho=max(max_ortho,np.linalg.norm(W.T@W-np.eye(r),ord=2))
                    lev=np.sum(W*W,axis=1)
                    assert lev.max(initial=0)<=theta/g+1e-9
                    assert theta/g<=0.5+1e-9
                    d=(1+rng.random(r)*4)*rng.choice([-1,1],size=r)
                    Gh=vecs@np.diag(vals**0.5)@vecs.T
                    K=Gh@np.diag(d)@Gh
                    lhs=abs(np.linalg.det(K))
                    rhs=np.linalg.det(G)*abs(np.prod(d))
                    max_det_rel=max(max_det_rel,abs(lhs-rhs)/max(1,abs(rhs)))
                else:
                    vals,vecs=np.linalg.eigh(S)
                    u=vecs[:,-1]
                    v=R@u
                    assert np.sum(v[H]**2)>1-2*theta-1e-9
                    assert len(H)*theta<r+1e-9
                checks+=1

assert 6/(1/4)==24
assert 6/(1/8)==48
assert 6/(1/16)==96
assert 6/(1/32)==192
assert int(np.ceil(3/(1/4))-1)==11
assert int(np.ceil(3/(1/8))-1)==23
assert int(np.ceil(3/(1/16))-1)==47
assert int(np.ceil(3/(1/32))-1)==95

print('QFORM_B08_R28_GRAM_PEEL_CHECK_PASS')
print('deterministic_random_instances', checks)
print('max_whitening_orthogonality_error', max_ortho)
print('max_determinant_relative_error', max_det_rel)
