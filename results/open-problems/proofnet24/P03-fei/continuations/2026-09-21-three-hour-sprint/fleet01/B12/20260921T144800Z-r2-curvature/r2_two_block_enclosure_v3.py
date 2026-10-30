"""B12 region-2 x in [1,2] two-block enclosure, v3: curvature tightening.

This module strengthens v2 only on y-cells where the exact scalar residual
J(x_hi,y) has a certified curvature sign.

With p*=2^-x_hi, v=2^-y and G(y)=G_num(y), the v2 residual is

 J(y)=G(y)/(1-v)+Psit(v)/v + const
      -8(1-p*)(1-v)ell(v)/ln2.

On one candidate segment G is affine with slope s.  Direct differentiation gives

 J''(y)
 = -2 ln2 s v/(1-v)^2
   +(ln2)^2 v G(y)(1+v)/(1-v)^3
   + C''(y)
   +8 ln2 (1-p*) [1/(1-v)-ell(v)],

where C(y)=Psit(v)/v and, writing m=1-2v,

 C''(y)= 2 ln2 / [v(1-v)^3] *
         {2v^3-2v+(-4v^2+3v-1) ln(m)}.

The formula is used only for cells with y_lo>1 (so m>0); the first cell falls
back to v2.

Two rigorous consequences:
* J'' <= 0 on a cell => J is concave there, hence its minimum is at an endpoint.
* J'' >= k>0 => for center yc,
      J(y) >= J(yc)+J'(yc)(y-yc)+(k/2)(y-yc)^2.
  If D encloses |J'(yc)|, minimizing the quadratic on all R gives the safe
      min J >= lower(J(yc)) - D^2/(2k).
The final lower bound is max(v2, these curvature bounds), so v3 is fail-safe.
"""
import importlib.util
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
V2_PATH = os.path.normpath(os.path.join(
    HERE, "..", "20260921T131812Z-r2-twoblock", "r2_two_block_enclosure_v2.py"))
_spec = importlib.util.spec_from_file_location("b12_r2_twoblock_v2", V2_PATH)
if _spec is None or _spec.loader is None:
    raise ImportError("cannot load B12 two-block v2")
V2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(V2)

Iv=V2.Iv; UP=V2.T.UP; LN2=V2.LN2
exp2neg=V2.exp2neg; ell_iv=V2.ell_iv
R2=V2.R2; _adaptive=V2._adaptive
from fei_cert import L_iv


def _j_second_range(cert, X, Y):
    """Rigorous enclosure of d^2/dy^2 J(x_hi,y) on one y-node segment.

    For any component touching y=1, return [-inf,+inf] so callers fall back
    to the already-rigorous v2 bounds.
    """
    lo=np.full_like(Y.lo, -np.inf, dtype=float)
    hi=np.full_like(Y.hi,  np.inf, dtype=float)
    # Build v,m first because outward rounding can leave m.lo==0 even when a
    # floating endpoint is only infinitesimally above 1.  Such components
    # deliberately fall back to v2 rather than evaluate log(m) at the boundary.
    vall=exp2neg(Y)
    mall=1-2*vall
    safe=(Y.lo > 1.0) & (mall.lo > 0)
    if not np.any(safe):
        return Iv(lo,hi)

    Ys=Iv(Y.lo[safe],Y.hi[safe])
    Xhi=Iv(X.hi[safe])
    p=exp2neg(Xhi)
    v=Iv(vall.lo[safe],vall.hi[safe])
    m=Iv(mall.lo[safe],mall.hi[safe])
    # L_iv(m)=log2(1/m), hence ln m=-ln2*L_iv(m).
    lnm=-LN2*L_iv(m)

    iy0,iy1=R2._seg_pair(cert,Ys.lo,Ys.hi)
    if np.any(iy0 != iy1):
        raise ValueError("J'' cell crosses a candidate node")
    s=Iv(cert.slopes[iy0])
    G=cert.Gnum_range(Ys)
    om=1-v

    Bpp=(-2*LN2*s*v/om.sq()
         + (LN2*LN2)*v*G*(1+v)/(om.sq()*om))

    N=2*v.sq()*v - 2*v + (-4*v.sq()+3*v-1)*lnm
    Cpp=2*LN2*N/(v*om.sq()*om)

    Dpp=8*LN2*(1-p)*(1/om-ell_iv(v))
    r=Bpp+Cpp+Dpp
    lo[safe]=r.lo
    hi[safe]=r.hi
    return Iv(lo,hi)


def _j_block_lower_v3(cert,X,Y):
    old_lo,old_w=V2._j_block_lower(cert,X,Y)

    xstar=Iv(X.hi)
    pstar=exp2neg(xstar)
    jpp=_j_second_range(cert,X,Y)

    jlo=V2._j_point(cert,xstar,pstar,Iv(Y.lo))
    jhi=V2._j_point(cert,xstar,pstar,Iv(Y.hi))

    concave=jpp.hi <= 0
    concave_lo=np.where(concave,np.minimum(jlo.lo,jhi.lo),-np.inf)

    convex=jpp.lo > 0
    yc=(Y.lo+Y.hi)/2
    jc=V2._j_point(cert,xstar,pstar,Iv(yc))
    jp0=V2.T._qprime_range(cert,pstar,Iv(yc))
    dabs=np.maximum(np.abs(jp0.lo),np.abs(jp0.hi))
    # Avoid invalid division on non-convex components; values are discarded there.
    ksafe=np.where(convex,jpp.lo,1.0)
    quad=(jc - Iv(dabs).sq()/(2*Iv(ksafe))).lo
    quad_lo=np.where(convex,quad,-np.inf)

    lo=np.maximum.reduce([old_lo,concave_lo,quad_lo])
    return lo,old_w


def phi2_over_v_lower_twoblock_v3(cert,X,Yp):
    old_lo,old_wx,old_wy=V2.phi2_over_v_lower_twoblock_v2(cert,X,Yp)
    v=exp2neg(Yp); ellv=ell_iv(v); lam=v*ellv/LN2
    af0_lo,af0_w=V2.T._af0_joint_lower(cert,X,lam,ellv)
    j_lo,j_w=_j_block_lower_v3(cert,X,Yp)
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
    if ylo>=yhi:
        raise ValueError("empty y shard")
    yi=np.arange(ylo,yhi)
    I,J=np.meshgrid(xi,yi,indexing="ij"); I,J=I.ravel(),J.ravel()
    return _adaptive(lambda X,Y: phi2_over_v_lower_twoblock_v3(cert,X,Y),
                     xs[I],xs[I+1],xs[J],xs[J+1],max_depth,
                     "region 2 B12 curvature-v3 x[1,2] yidx[%d,%d)"%(ylo,yhi))


if __name__=="__main__":
    if len(sys.argv)<5:
        raise SystemExit("usage: python r2_two_block_enclosure_v3.py CANDIDATE.npz C Y_INDEX_LO Y_INDEX_HI [MAX_DEPTH]")
    src=sys.argv[1]; c=float(sys.argv[2]); j0=int(sys.argv[3]); j1=int(sys.argv[4])
    depth=int(sys.argv[5]) if len(sys.argv)>5 else 30
    if abs(c-0.003)>1e-15:
        raise RuntimeError("this sprint driver is pinned to c=0.003")
    got=R2.verify_candidate_file(src); cert,C0=R2.load_cert(src,c)
    print("candidate git_blob=%s bytes=%d C0=%.7f c=%g C_cert=%.7f"%
          (got,R2.EXPECTED_CANDIDATE_BYTES,C0,c,cert.C_cert()),flush=True)
    ok=verify_fleet01_shard(cert,j0,j1,depth)
    print("B12 CURVATURE-V3 SHARD %s"%("VERIFIED" if ok else "NOT verified"),flush=True)
