import math
import numpy as np


def main():
    lines=[]

    # Diffuse exact-zero-aggregate Walsh control.
    N=64
    s=np.ones(N)
    s[N//2:]=-1
    P=np.column_stack([np.ones(N),s])/math.sqrt(N)
    C=P.copy()
    B=P@C.T
    A=np.block([[np.zeros((N,N)),B],[B.T,np.zeros((N,N))]])
    sv=np.linalg.svd(B,compute_uv=False)
    ev=np.linalg.eigvalsh(A)
    nz=ev[np.abs(ev)>1e-10]
    lines.append(f"walsh_N={N}")
    lines.append(f"PTP_error={np.linalg.norm(P.T@P-np.eye(2)):.3e}")
    lines.append(f"CTC_error={np.linalg.norm(C.T@C-np.eye(2)):.3e}")
    lines.append("B_top_singulars="+",".join(f"{x:.12f}" for x in sv[:2]))
    lines.append("A_nonzero_eigs="+",".join(f"{x:.12f}" for x in nz))
    lines.append(f"max_cross_entry={np.max(np.abs(B)):.12f}")
    lines.append(f"max_cross_principal_2x2_det={np.max(np.abs(B))**2:.12f}")

    # Seeded exact dual-collapse regression.
    rng=np.random.default_rng(20260923)
    h,m=7,9
    Q,_=np.linalg.qr(rng.normal(size=(h,2)))
    P2=Q[:,:2]
    C2=rng.normal(size=(m,2))
    M=rng.normal(size=(2,2)); M=(M+M.T)/2
    Nmat=rng.normal(size=(2,2)); Nmat=(Nmat+Nmat.T)/2
    lamH=rng.normal(size=h); lamI=rng.normal(size=m)
    B2=P2@C2.T
    A2=np.block([
        [P2@Nmat@P2.T+np.diag(lamH), B2],
        [B2.T, C2@M@C2.T+np.diag(lamI)]
    ])
    U=np.block([[P2,np.zeros((h,2))],[np.zeros((m,2)),C2]])
    K=np.block([[Nmat,np.eye(2)],[np.eye(2),M]])
    D0=np.diag(np.r_[lamH,lamI])
    collapse_err=np.linalg.norm(A2-(D0+U@K@U.T))

    max_rank_I=0; max_s3_I=0.0
    for i in range(m):
        rows=list(range(h))+[h+i]
        cols=[h+j for j in range(m) if j!=i]
        X=A2[np.ix_(rows,cols)]
        ss=np.linalg.svd(X,compute_uv=False)
        max_rank_I=max(max_rank_I,int(np.sum(ss>1e-10)))
        if len(ss)>=3:
            max_s3_I=max(max_s3_I,float(ss[2]))

    max_rank_H=0; max_s3_H=0.0
    for a in range(h):
        rows=[h+j for j in range(m)]+[a]
        cols=[b for b in range(h) if b!=a]
        X=A2[np.ix_(rows,cols)]
        ss=np.linalg.svd(X,compute_uv=False)
        max_rank_H=max(max_rank_H,int(np.sum(ss>1e-10)))
        if len(ss)>=3:
            max_s3_H=max(max_s3_H,float(ss[2]))

    lines.append(f"dual_collapse_error={collapse_err:.3e}")
    lines.append(f"max_augmented_rank_I={max_rank_I}")
    lines.append(f"max_augmented_s3_I={max_s3_I:.3e}")
    lines.append(f"max_augmented_rank_H={max_rank_H}")
    lines.append(f"max_augmented_s3_H={max_s3_H:.3e}")

    # Exact Pluecker disjointness and grouped-hub bound at the report's N=512.
    Nbig=512
    rho=(1-2/Nbig)**2
    bound=2*math.e*(1-2/Nbig)**(-0.5)
    lines.append(f"N512_rho={rho:.15f}")
    lines.append(f"N512_grouped_bound={bound:.15f}")

    # Designated account04/B09 partner endpoint.
    partner=np.block([[np.zeros((3,3)),np.eye(3)],[np.eye(3),np.zeros((3,3))]])
    pe=np.linalg.eigvalsh(partner)
    lines.append("partner_eigs="+",".join(f"{x:.1f}" for x in pe))
    lines.append("partner_bound=3.000000000000000")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
