import numpy as np

rng=np.random.default_rng(2026092407)
max_det_rel=0.0
max_lev_excess=0.0
min_s2_ratio=float('inf')
funnel_viol=0
accepted=0
for _ in range(5000):
    mR=int(rng.integers(8,25)); mC=int(rng.integers(8,25))
    UR,_=np.linalg.qr(rng.normal(size=(mR,2)))
    VC,_=np.linalg.qr(rng.normal(size=(mC,2)))
    lr=np.sum(UR**2,axis=1); lc=np.sum(VC**2,axis=1)
    LR=np.where(lr<=2/7)[0]; LC=np.where(lc<=2/7)[0]
    GR=UR[LR].T@UR[LR]; GC=VC[LC].T@VC[LC]
    if np.min(np.linalg.eigvalsh(GR))<4/7 or np.min(np.linalg.eigvalsh(GC))<4/7:
        continue
    accepted += 1
    wr,Vr=np.linalg.eigh(GR); wc,Vc=np.linalg.eigh(GC)
    GRh=(Vr*np.sqrt(wr))@Vr.T; GCh=(Vc*np.sqrt(wc))@Vc.T
    GRmh=(Vr*(1/np.sqrt(wr)))@Vr.T; GCmh=(Vc*(1/np.sqrt(wc)))@Vc.T
    Ut=UR[LR]@GRmh; Vt=VC[LC]@GCmh
    max_lev_excess=max(max_lev_excess,float(np.max(np.sum(Ut**2,axis=1))-0.5),float(np.max(np.sum(Vt**2,axis=1))-0.5))
    s2=1/64+rng.random()*0.05; s1=s2+rng.random()*0.5; Sig=np.diag([s1,s2])
    C=GRh@Sig@GCh
    min_s2_ratio=min(min_s2_ratio,float(np.linalg.svd(C,compute_uv=False)[1]/((4/7)*s2)))
    BR=rng.normal(size=(2,2)); BR=(BR+BR.T)/2
    BC=rng.normal(size=(2,2)); BC=(BC+BC.T)/2
    H=np.block([[BR,Sig],[Sig,BC]])
    S=np.block([[GRh,np.zeros((2,2))],[np.zeros((2,2)),GCh]])
    HL=S@H@S
    rhs=np.linalg.det(GR)*np.linalg.det(GC)*np.linalg.det(H)
    resid=np.linalg.det(HL)-rhs
    scale=max(1.0,abs(np.linalg.det(HL)),abs(rhs))
    max_det_rel=max(max_det_rel,float(abs(resid)/scale))
    sv=np.linalg.svd(HL,compute_uv=False); sc=np.linalg.svd(C,compute_uv=False)[1]
    if abs(np.linalg.det(HL))+1e-10 < (sc**2)*(sv[-1]**2):
        funnel_viol+=1
print('accepted',accepted)
print('max_normalized_determinant_residual',max_det_rel)
print('max_leverage_excess_over_half',max_lev_excess)
print('min_cross_s2_ratio',min_s2_ratio)
print('determinant_collapse_violations',funnel_viol)
print('QFORM_B19_R52_FOURLATENT_CHECK_PASS' if funnel_viol==0 and max_lev_excess<=1e-12 else 'FAIL')
