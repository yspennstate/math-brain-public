"""Rescaled, directed radial-cell certificate for the positive simplex kernel.
Uses the original frozen table builder/checkpoint and exact exponential identities.
"""
from pathlib import Path
import hashlib,json,math,sys
import certify_positive_cells as old
np,base,pos=old.np,old.base,old.pos
ROOT=old.ROOT
original_tables=old.tables

def tables(args):
    a,q,e,c=original_tables(args)
    low,high=a.ranges['TPLUS'].mins[0],a.ranges['TPLUS'].maxs[0]
    ul=np.empty_like(low);uh=np.empty_like(high)
    for i in range(a.bins):
        el,eh=base.bounds((-base.ball(float(a.edges[i]),float(a.edges[i+1]))).exp())
        ul[i]=base.mul_pos_lo(low[i],el);uh[i]=base.mul_pos_hi(high[i],eh)
    u=base.UniformTable(a.edges,{'UPLUS':base.SparseRange.build(ul,uh)})
    r=math.nextafter(args.table_rho_max,math.inf)
    d=base.sub_lo(1.,base.mul_pos_hi(r,r));x2=base.mul_pos_hi(args.cutoff,args.cutoff)
    maximum=base.div_pos_hi(base.add_hi(base.mul_pos_hi(2.,x2),base.mul_pos_hi(base.mul_pos_hi(4.,r),x2)),base.mul_pos_lo(2.,d))
    zmax=float(math.ceil(base.add_hi(maximum,1.)))
    exponent=base.build_exp_table(zmax,max(65536,args.exp_bins),2.)
    old.dump(Path('logs')/('scaled_auxiliary_'+args.label+'.json'),{'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'frozen_builder_sha256':hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest(),'U_lower_sha256':hashlib.sha256(ul.tobytes()).hexdigest(),'U_upper_sha256':hashlib.sha256(uh.tobytes()).hexdigest(),'exp_domain_upper':zmax,'exp_bins':max(65536,args.exp_bins),'exp_lower_sha256':hashlib.sha256(exponent.ranges['E'].mins[0].tobytes()).hexdigest(),'exp_upper_sha256':hashlib.sha256(exponent.ranges['E'].maxs[0].tobytes()).hexdigest(),'identity':'U(a)=exp(-a)T_+(a), bounded on each certified a bin before querying multiple bins.'})
    print('Scaled angular and enlarged exponential tables complete',flush=True)
    return u,q,exponent,c

def majorant(lo,hi,args,tabs):
    u_table,q_table,e,constants=tabs
    n=args.x_panels
    if 32*n*n+180_000_000>900_000_000:raise MemoryError('Sized computation exceeds 900 MB')
    edges=np.linspace(0.,args.cutoff,n+1,dtype=np.float64);edges[0]=0.;edges[-1]=args.cutoff
    xl,xh=edges[:-1],edges[1:];widths=base.sub_hi(xh,xl)
    rlo=math.nextafter(lo,-math.inf);rhi=math.nextafter(hi,math.inf)
    rlo2=base.mul_pos_lo(rlo,rlo);rhi2=base.mul_pos_hi(rhi,rhi)
    dlo=base.sub_lo(1.,rhi2);dhi=base.sub_hi(1.,rlo2)
    il=base.div_pos_lo(1.,dhi);ih=base.div_pos_hi(1.,dlo)
    kl=base.mul_pos_lo(rlo2,il);kh=base.mul_pos_hi(rhi2,ih)
    al=base.div_pos_lo(rlo,base.sqrt_pos_hi(dhi));ah=base.div_pos_hi(rhi,base.sqrt_pos_lo(dlo))
    bl=base.mul_pos_lo(base.mul_pos_lo(2.,rlo),il);bh=base.mul_pos_hi(base.mul_pos_hi(2.,rhi),ih)
    ql=base.mul_pos_lo(al,xl);qh=base.mul_pos_hi(ah,xh)
    hl,hh=q_table.query('HPLUS',ql,qh);sl,sh=q_table.query('S',ql,qh)
    jl=base.mul_pos_lo(al,base.add_lo(hl,base.mul_pos_lo(base.div_pos_lo(constants.j1_lo,2.),sl)))
    jl=np.maximum(jl,base.mul_pos_lo(constants.cw_lo,al));assert np.all(jl>0)
    cl,ch=pos.center_interval(rlo,rhi,xl,xh)
    B=np.empty((n,n),dtype=np.float64);yl,yh=xl[None,:],xh[None,:]
    two_dlo=base.mul_pos_lo(2.,dlo);two_dhi=base.mul_pos_hi(2.,dhi)
    cc_lo=base.sub_lo(1.,base.mul_pos_hi(2.,rhi));cc_hi=base.sub_hi(1.,base.mul_pos_lo(2.,rlo));assert cc_lo>0
    lam_lo=base.sub_lo(1.,kh);lam_hi=base.sub_hi(1.,kl);assert lam_lo>0
    for start in range(0,n,args.chunk):
        stop=min(start+args.chunk,n);xlo,xhi=xl[start:stop,None],xh[start:stop,None]
        xylo=base.mul_pos_lo(xlo,yl);xyhi=base.mul_pos_hi(xhi,yh)
        aa=base.mul_pos_lo(bl,xylo);ab=base.mul_pos_hi(bh,xyhi)
        ulo,uhi=u_table.query('UPLUS',aa,ab)
        difflo=base.sub_lo(xlo,yh);diffhi=base.sub_hi(xhi,yl)
        mindiff=np.where(difflo>0,difflo,np.where(diffhi<0,-diffhi,0.))
        maxdiff=np.maximum(np.abs(difflo),np.abs(diffhi))
        numlo=base.add_lo(base.mul_pos_lo(mindiff,mindiff),base.mul_pos_lo(base.mul_pos_lo(2.,cc_lo),xylo))
        numhi=base.add_hi(base.mul_pos_hi(maxdiff,maxdiff),base.mul_pos_hi(base.mul_pos_hi(2.,cc_hi),xyhi))
        q0lo=base.div_pos_lo(max(0.,0.)+np.maximum(numlo,0.),two_dhi);q0hi=base.div_pos_hi(numhi,two_dlo)
        e0lo,e0hi=e.query('E',q0lo,q0hi)
        positive_lo=base.mul_pos_lo(base.mul_pos_lo(2.,il),base.mul_pos_lo(e0lo,ulo))
        positive_hi=base.mul_pos_hi(base.mul_pos_hi(2.,ih),base.mul_pos_hi(e0hi,uhi))
        sslo=base.add_lo(base.mul_pos_lo(xlo,xlo),base.mul_pos_lo(yl,yl))
        sshi=base.add_hi(base.mul_pos_hi(xhi,xhi),base.mul_pos_hi(yh,yh))
        pluslo=base.add_lo(sslo,base.mul_pos_lo(base.mul_pos_lo(4.,rlo),xylo))
        plushi=base.add_hi(sshi,base.mul_pos_hi(base.mul_pos_hi(4.,rhi),xyhi))
        qplo=base.div_pos_lo(np.maximum(pluslo,0.),two_dhi);qphi=base.div_pos_hi(plushi,two_dlo)
        eplo,ephi=e.query('E',qplo,qphi)
        neglo=base.mul_pos_lo(base.mul_pos_lo(base.mul_pos_lo(4.,constants.j1_lo),il),base.mul_pos_lo(aa,eplo))
        neghi=base.mul_pos_hi(base.mul_pos_hi(base.mul_pos_hi(4.,constants.j1_hi),ih),base.mul_pos_hi(ab,ephi))
        qclo=base.mul_pos_lo(.5,base.mul_pos_lo(lam_lo,np.maximum(sslo,0.)));qchi=base.mul_pos_hi(.5,base.mul_pos_hi(lam_hi,sshi))
        eclo,echi=e.query('E',qclo,qchi)
        cpl=base.add_lo(cl[start:stop,None],cl[None,:]);cph=base.add_hi(ch[start:stop,None],ch[None,:])
        centerlo,centerhi=base.mul_interval(base.mul_pos_lo(2.,eclo),base.mul_pos_hi(2.,echi),cpl,cph)
        rl=base.sub_lo(base.sub_lo(positive_lo,neghi),centerhi);rh=base.sub_hi(base.sub_hi(positive_hi,neglo),centerlo)
        rr=base.abs_square_upper(rl,rh);den=base.mul_pos_lo(jl[start:stop,None],jl[None,:])
        area=base.mul_pos_hi(widths[start:stop,None],widths[None,:])
        B[start:stop]=old.sqrt_array_hi(base.mul_pos_hi(area,base.div_pos_hi(rr,den)))
    B=np.maximum(B,B.T);assert np.isfinite(B).all() and np.all(B>=0)
    tail,kt,at=pos.analytic_tail(rlo,rhi,dhi,ih,kh,al,args.cutoff,constants)
    return B,tail,{'kernel_squared_tail':kt,'additive_squared_tail':at,'minimum_jbar_lower':float(jl.min()),'radial_edges_sha256':hashlib.sha256(edges.tobytes()).hexdigest(),'implementation':'exponentially rescaled radial-cell kernel'}

old.tables=tables
old.majorant=majorant
if __name__=='__main__':raise SystemExit(old.main())
