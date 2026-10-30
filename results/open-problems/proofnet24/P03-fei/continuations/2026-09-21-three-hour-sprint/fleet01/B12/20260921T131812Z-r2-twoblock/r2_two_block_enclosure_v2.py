"""B12 region-2 x in [1,2] two-block enclosure, v2.

This strengthens r2_two_block_enclosure.py by keeping the *entire* residual
x-dependent block together.  After extracting

    K0(t)=G_num(t)+Psi(2^-t),

region 2 has the exact identity

    Phi/v = [K0(x)-K0(x+lambda)]/v + J(x,y),

where p=2^-x, v=2^-y, lambda=-log2(1-v), and

    J(x,y) = G_num(y)/(1-v) + Psi(1-v)/v
             + c(1-p) - 8[1+p(x-1)]
             - 8(1-p)(1-v)ell(v)/ln2.

For fixed y and x in [1,2], J is strictly decreasing in x.  Indeed, with
 a(v)=8(1-v)ell(v)/ln2 > 0,

 dJ/dx = p { c ln2 - 8[1-ln2(x-1)] - a(v) ln2 } < 0

for the pinned c=.003, since 1-ln2(x-1) >= 1-ln2 > 0 on [1,2].
Therefore the exact cell minimum in the x direction is attained at x_hi,
not by separately minimizing the positive c(1-p) term at x_lo.  With
x*=x_hi fixed, J(x*,y) is a one-variable smooth function on each y-node
segment.  Its y derivative is exactly the Q' derivative already proved in
v1, so endpoint-sign and centred mean-value enclosures apply unchanged.

The final bound is max(v1, v2), hence fail-safe.
"""
import importlib.util
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
V1_PATH = os.path.join(HERE, "r2_two_block_enclosure.py")
_spec = importlib.util.spec_from_file_location("b12_r2_twoblock_v1", V1_PATH)
if _spec is None or _spec.loader is None:
    raise ImportError("cannot load B12 two-block v1")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)

Iv=T.Iv; UP=T.UP; LN2=T.LN2; exp2neg=T.exp2neg; ell_iv=T.ell_iv
psit_over_z_iv=T.psit_over_z_iv; _adaptive=T._adaptive
R2=T.R2


def _j_point(cert, xstar, pstar, y):
    v=exp2neg(y)
    xpart=(Iv(cert.c)*(1-pstar)
           - 8*(1 + pstar*(xstar-1))
           - 8*(1-pstar)*(1-v)*ell_iv(v)/LN2)
    return cert.Gnum_range(y)/(1-v) + psit_over_z_iv(v) + xpart


def _j_block_lower(cert, X, Y):
    # Exact x minimizer by the strict derivative lemma: x*=x_hi.
    xstar=Iv(X.hi)
    pstar=exp2neg(xstar)
    v=exp2neg(Y)
    direct=(cert.Gnum_range(Y)/(1-v) + psit_over_z_iv(v)
            + Iv(cert.c)*(1-pstar)
            - 8*(1 + pstar*(xstar-1))
            - 8*(1-pstar)*(1-v)*ell_iv(v)/LN2)

    # J_y equals the Q_y derivative from v1 because the added CE+margin terms
    # are constants after x is frozen at x_hi.
    jp=T._qprime_range(cert,pstar,Y)
    jlo=_j_point(cert,xstar,pstar,Iv(Y.lo))
    jhi=_j_point(cert,xstar,pstar,Iv(Y.hi))
    sign_pos=jp.lo >= 0
    sign_neg=jp.hi <= 0
    endpoint_lo=np.where(sign_pos,jlo.lo,np.where(sign_neg,jhi.lo,-np.inf))

    yc=(Y.lo+Y.hi)/2
    ry=UP(np.maximum(Y.hi-yc,yc-Y.lo))
    jc=_j_point(cert,xstar,pstar,Iv(yc))
    ajp=np.maximum(np.abs(jp.lo),np.abs(jp.hi))
    mv_lo=(jc-Iv(ry)*Iv(ajp)).lo
    lo=np.maximum.reduce([direct.lo,endpoint_lo,mv_lo])
    width_hint=np.minimum(direct.width(),2*ry*ajp)
    return lo,width_hint


def phi2_over_v_lower_twoblock_v2(cert,X,Yp):
    old_lo,old_wx,old_wy=T.phi2_over_v_lower_twoblock(cert,X,Yp)
    v=exp2neg(Yp); ellv=ell_iv(v); lam=v*ellv/LN2
    af0_lo,af0_w=T._af0_joint_lower(cert,X,lam,ellv)
    j_lo,j_w=_j_block_lower(cert,X,Yp)
    new_lo=af0_lo+j_lo
    lo=np.maximum(old_lo,new_lo)
    use_new=new_lo >= old_lo
    wx_new=0.5*af0_w
    wy_new=0.5*af0_w+j_w
    return lo,np.where(use_new,wx_new,old_wx),np.where(use_new,wy_new,old_wy)


def verify_fleet01_shard(cert,y_index_lo,y_index_hi,max_depth=30):
    xs=cert.xs
    xi=np.where((xs[:-1]>=1.0)&(xs[1:]<=2.0+8*np.finfo(float).eps))[0]
    ylo=max(0,int(y_index_lo)); yhi=min(len(xs)-1,int(y_index_hi))
    if ylo>=yhi: raise ValueError("empty y shard")
    yi=np.arange(ylo,yhi)
    I,J=np.meshgrid(xi,yi,indexing="ij"); I,J=I.ravel(),J.ravel()
    return _adaptive(lambda X,Y: phi2_over_v_lower_twoblock_v2(cert,X,Y),
                     xs[I],xs[I+1],xs[J],xs[J+1],max_depth,
                     "region 2 B12 two-block-v2 x[1,2] yidx[%d,%d)"%(ylo,yhi))

if __name__=="__main__":
    if len(sys.argv)<5:
        raise SystemExit("usage: python r2_two_block_enclosure_v2.py CANDIDATE.npz C Y_INDEX_LO Y_INDEX_HI [MAX_DEPTH]")
    src=sys.argv[1]; c=float(sys.argv[2]); j0=int(sys.argv[3]); j1=int(sys.argv[4]); depth=int(sys.argv[5]) if len(sys.argv)>5 else 30
    if abs(c-0.003)>1e-15: raise RuntimeError("this sprint driver is pinned to c=0.003")
    got=R2.verify_candidate_file(src); cert,C0=R2.load_cert(src,c)
    print("candidate git_blob=%s bytes=%d C0=%.7f c=%g C_cert=%.7f"%(got,R2.EXPECTED_CANDIDATE_BYTES,C0,c,cert.C_cert()),flush=True)
    ok=verify_fleet01_shard(cert,j0,j1,depth)
    print("B12 TWO-BLOCK-V2 SHARD %s"%("VERIFIED" if ok else "NOT verified"),flush=True)
