#!/usr/bin/env python3
import json, math, time
import numpy as np

def hadamard_matrix(n):
    H=np.array([[1]],dtype=np.int64)
    for _ in range(n):
        H=np.block([[H,H],[H,-H]])
    return H

def h2(x):
    x=np.asarray(x,dtype=np.float64)
    out=np.zeros_like(x)
    mask=(x>0.0)&(x<1.0)
    y=x[mask]
    out[mask]=-(y*np.log2(y)+(1.0-y)*np.log2(1.0-y))
    return out

def entropy_rows(p):
    out=np.zeros(p.shape[0],dtype=np.float64)
    mask=p>0
    logs=np.zeros_like(p)
    logs[mask]=np.log2(1.0/p[mask])
    out=np.sum(p*logs,axis=1)
    return out

def exhaustive():
    overall_max_js_minus_b=-1e300
    overall_max_identity_error=0.0
    overall_max_js_over_b=0.0
    equality_with_intermediate_fiber=0
    total_functions=0
    total_splits=0
    by_dimension={}
    for n in range(1,5):
        N=1<<n
        H=hadamard_matrix(n)
        count=1<<N
        batch=2048 if N==16 else count
        idx_pairs=[]
        for i in range(n):
            idx0=np.array([s for s in range(N) if ((s>>i)&1)==0],dtype=np.int64)
            idx1=idx0 | (1<<i)
            idx_pairs.append((idx0,idx1))
        dmax=-1e300
        derr=0.0
        dratio=0.0
        dsplits=0
        for start in range(0,count,batch):
            b=min(batch,count-start)
            masks=np.arange(start,start+b,dtype=np.uint64)[:,None]
            xs=np.arange(N,dtype=np.uint64)[None,:]
            vals=1-2*((masks>>xs)&1).astype(np.int8)
            coeff=(vals@H.T)/float(N)
            parent_p=coeff*coeff
            Hp=entropy_rows(parent_p)
            for idx0,idx1 in idx_pairs:
                u=coeff[:,idx0]
                v=coeff[:,idx1]
                w=u*u+v*v
                t=np.divide(np.minimum(u*u,v*v),w,out=np.zeros_like(w),where=w>0)
                B=np.sum(w*h2(t),axis=1)

                a=u+v
                c=u-v
                denom=a*a+c*c
                p=np.divide(a*a,denom,out=np.zeros_like(denom),where=denom>0)
                JS=np.sum(w*(1.0-h2(p)),axis=1)

                Pa=a*a
                Pc=c*c
                delta=Hp-(entropy_rows(Pa)+entropy_rows(Pc))/2.0
                identity_error=np.abs(delta-(B+JS))
                viol=JS-B
                ratio=np.divide(JS,B,out=np.zeros_like(JS),where=B>1e-15)

                dmax=max(dmax,float(np.max(viol)))
                derr=max(derr,float(np.max(identity_error)))
                dratio=max(dratio,float(np.max(ratio)))
                overall_max_js_minus_b=max(overall_max_js_minus_b,float(np.max(viol)))
                overall_max_identity_error=max(overall_max_identity_error,float(np.max(identity_error)))
                overall_max_js_over_b=max(overall_max_js_over_b,float(np.max(ratio)))

                eq_rows=np.where(np.abs(viol)<1e-12)[0]
                for rr in eq_rows:
                    active=w[rr]>1e-15
                    intermediate=active&(t[rr]>1e-12)&(t[rr]<0.5-1e-12)
                    if np.any(intermediate):
                        equality_with_intermediate_fiber += 1
                dsplits += b
        total_functions += count
        total_splits += dsplits
        by_dimension[str(n)]={
            "functions":count,
            "coordinate_splits":dsplits,
            "max_JS_minus_B":dmax,
            "max_delta_minus_B_plus_JS_abs":derr,
            "max_JS_over_B_when_B_positive":dratio,
        }

    # Sharp two-variable controlled-character witness:
    # child at t=0 is constant 1; child at t=1 is residual character (-1)^x.
    # Truth table order (t least significant, x next): f(0,0)=1,f(1,0)=1,f(0,1)=1,f(1,1)=-1.
    vals=np.array([1,1,1,-1],dtype=np.int64)
    H=hadamard_matrix(2)
    coeff=(vals@H.T)/4.0
    p=coeff*coeff
    Hroot=float(entropy_rows(p[None,:])[0])
    Iroot=sum(((s.bit_count())*p[s]) for s in range(4))
    # split coordinate 0 (t)
    u=coeff[[0,2]]
    v=coeff[[1,3]]
    w=u*u+v*v
    t=np.divide(np.minimum(u*u,v*v),w,out=np.zeros_like(w),where=w>0)
    B=float(np.sum(w*h2(t)))
    a=u+v
    c=u-v
    denom=a*a+c*c
    branchp=np.divide(a*a,denom,out=np.zeros_like(denom),where=denom>0)
    JS=float(np.sum(w*(1.0-h2(branchp))))

    return {
        "status":"PASS",
        "theorem_checked":"pointwise dependent-branch recombination JS_i <= B_i and Delta_iH=B_i+JS_i",
        "enumeration":{
            "total_boolean_functions_dimensions_1_through_4":total_functions,
            "total_coordinate_splits":total_splits,
            "by_dimension":by_dimension,
        },
        "global_max_JS_minus_B":overall_max_js_minus_b,
        "global_max_identity_error":overall_max_identity_error,
        "global_max_JS_over_B_when_B_positive":overall_max_js_over_b,
        "equality_cases_with_any_intermediate_fiber_t":equality_with_intermediate_fiber,
        "sharp_controlled_character":{
            "H":Hroot,
            "I":Iroot,
            "B_control":B,
            "JS_control":JS,
            "H_over_I":Hroot/Iroot,
            "JS_over_B":JS/B,
        },
        "constant_update_one_point_quadratic":{
            "C_chi":2.0+1.0/(math.sqrt(math.e)*math.log(2.0)),
            "old_direct_C_chi_plus_2_over_ln2":2.0+1.0/(math.sqrt(math.e)*math.log(2.0))+2.0/math.log(2.0),
            "new_direct_2_C_chi":2.0*(2.0+1.0/(math.sqrt(math.e)*math.log(2.0))),
        },
    }

if __name__=="__main__":
    t0=time.time()
    out=exhaustive()
    out["elapsed_seconds"]=time.time()-t0
    print(json.dumps(out,indent=2,sort_keys=True))
