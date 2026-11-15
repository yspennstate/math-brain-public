"""Uniform, directed certificate for Heilman's actual positive simplex operator.

The finite majorant uses radial cell indicators, not the sphere-valued Laguerre
matrix. Numerical power iteration selects a positive witness only. The check
uses outward-rounded entries and certified row sums. See proofs/CELL_BOUND.md.
"""
from pathlib import Path
import os
for _key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse, ctypes, datetime, hashlib, json, math, platform, sys, time
from ctypes import wintypes

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'cut_bounds'))
import numpy as np
import scipy
import flint
from flint import arb, ctx
import plur_cert as base
import plur_cert_positive as pos

def sqrt_array_hi(values):
    values=np.asarray(values,dtype=np.float64)
    assert np.all(values>=0) and np.all(np.isfinite(values))
    result=base.up(np.sqrt(values))
    # A directed product lower bound verifies every vectorized square root.
    # This makes the check independent of the numerical sqrt implementation.
    mask=base.mul_pos_lo(result,result)<values
    if np.any(mask):
        flat_result=result.ravel();flat_values=values.ravel()
        for i in np.flatnonzero(mask.ravel()):
            flat_result[i]=base.sqrt_pos_hi(float(flat_values[i]))
    return result


def dump(path, data):
    (ROOT/path).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def hardware():
    k=ctypes.WinDLL('kernel32',use_last_error=True)
    k.GetCurrentProcess.restype=wintypes.HANDLE
    k.SetProcessAffinityMask.argtypes=[wintypes.HANDLE,ctypes.c_size_t]
    k.SetProcessAffinityMask.restype=wintypes.BOOL
    assert k.SetProcessAffinityMask(k.GetCurrentProcess(),12),ctypes.get_last_error()
    class Memory(ctypes.Structure):
        _fields_=[('dwLength',wintypes.DWORD),('dwMemoryLoad',wintypes.DWORD)]+[(n,ctypes.c_ulonglong) for n in ('ullTotalPhys','ullAvailPhys','ullTotalPageFile','ullAvailPageFile','ullTotalVirtual','ullAvailVirtual','ullAvailExtendedVirtual')]
    m=Memory();m.dwLength=ctypes.sizeof(m)
    assert k.GlobalMemoryStatusEx(ctypes.byref(m))
    assert m.ullAvailPhys>=2**31,'Need at least 2 GiB free RAM'
    return {'affinity':[2,3],'available_ram':m.ullAvailPhys,'threads':{key:os.environ[key] for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')}}

def tables(args):
    hi=math.nextafter(args.table_rho_max,math.inf)
    hi2=base.mul_pos_hi(hi,hi)
    dlo=base.sub_lo(1.,hi2)
    invd=base.div_pos_hi(1.,dlo)
    alpha=base.div_pos_hi(hi,base.sqrt_pos_lo(dlo))
    beta=base.mul_pos_hi(base.mul_pos_hi(2.,hi),invd)
    x2=base.mul_pos_hi(args.cutoff,args.cutoff)
    qmax=base.mul_pos_hi(alpha,args.cutoff)
    amax=base.mul_pos_hi(beta,x2)
    kappa=base.mul_pos_hi(hi2,invd)
    zmax=base.up(max(x2,base.mul_pos_hi(kappa,base.add_hi(x2,x2))))
    cache=ROOT/'logs'/f'cells_tables_{args.table_rho_max}_{args.cutoff}_{args.q_bins}_{args.a_bins}_{args.exp_bins}_{args.v_panels}_{args.precision}.npz'
    recipe={'parameters':{k:getattr(args,k) for k in ('table_rho_max','cutoff','q_bins','a_bins','exp_bins','v_panels','precision')},'input_hashes':{str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in (Path(__file__).resolve(),ROOT/'cut_bounds/plur_cert.py',ROOT/'cut_bounds/plur_cert_positive.py')}}
    receipt=cache.with_suffix('.json')
    if cache.exists() and receipt.exists():
        saved=json.loads(receipt.read_text(encoding='utf-8'))
        assert saved['recipe']==recipe,'Cache recipe or source changed'
        assert hashlib.sha256(cache.read_bytes()).hexdigest()==saved['sha256'],'Cache bytes changed'
        restored=[]
        with np.load(cache,allow_pickle=False) as data:
            for tag in ('a','q','e'):
                ranges={}
                for name in saved['range_names'][tag]:
                    ranges[name]=base.SparseRange.build(data[tag+'_'+name+'_lo'].copy(),data[tag+'_'+name+'_hi'].copy())
                restored.append(base.UniformTable(data[tag+'_edges'].copy(),ranges))
        print('Verified table checkpoint loaded',flush=True)
        return (*restored,pos.build_constants())
    print('Building directed Arb tables',flush=True)
    q=pos.build_positive_q_table(qmax,args.q_bins,args.v_panels,2.)
    print('q table complete',flush=True)
    a=pos.build_positive_a_table(amax,args.a_bins,args.v_panels,2.)
    print('a table complete',flush=True)
    e=base.build_exp_table(zmax,args.exp_bins,2.)
    arrays={};names={}
    for tag,table in (('a',a),('q',q),('e',e)):
        arrays[tag+'_edges']=table.edges
        names[tag]=list(table.ranges)
        for name,ranges in table.ranges.items():
            arrays[tag+'_'+name+'_lo']=ranges.mins[0]
            arrays[tag+'_'+name+'_hi']=ranges.maxs[0]
    np.savez_compressed(cache,**arrays)
    receipt.write_text(json.dumps({'recipe':recipe,'range_names':names,'sha256':hashlib.sha256(cache.read_bytes()).hexdigest(),'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'builder':'Arb interval tables; all saved arrays are the original leaf enclosures, reconstructed by min/max only.'},indent=2)+'\n',encoding='utf-8')
    print('Directed tables checkpoint saved',flush=True)
    return a,q,e,pos.build_constants()

def majorant(lo,hi,args,tabs):
    a_table,q_table,exp_table,constants=tabs
    n=args.x_panels
    if 32*n*n+180_000_000>900_000_000:
        raise MemoryError('Sized computation exceeds 900 MB')
    edges=np.linspace(0.,args.cutoff,n+1,dtype=np.float64)
    edges[0]=0.;edges[-1]=args.cutoff
    xl,xh=edges[:-1],edges[1:]
    widths=base.sub_hi(xh,xl)
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
    jh=base.mul_pos_hi(ah,base.add_hi(hh,base.mul_pos_hi(base.div_pos_hi(constants.j1_hi,2.),sh)))
    jl=np.maximum(jl,base.mul_pos_lo(constants.cw_lo,al))  # Analytic lower bound (153).
    assert np.all(jl>0)
    cl,ch=pos.center_interval(rlo,rhi,xl,xh)
    wl,wh=exp_table.query('E',base.mul_pos_lo(xl,xl),base.mul_pos_hi(xh,xh))
    B=np.empty((n,n),dtype=np.float64)
    yl,yh=xl[None,:],xh[None,:]
    for start in range(0,n,args.chunk):
        stop=min(start+args.chunk,n)
        xlo,xhi=xl[start:stop,None],xh[start:stop,None]
        pl=base.mul_pos_lo(xlo,yl);ph=base.mul_pos_hi(xhi,yh)
        aa=base.mul_pos_lo(bl,pl);ab=base.mul_pos_hi(bh,ph)
        tl,th=a_table.query('TPLUS',aa,ab);dl,dh=a_table.query('P',aa,ab)
        ssl=base.add_lo(base.mul_pos_lo(xlo,xlo),base.mul_pos_lo(yl,yl))
        ssh=base.add_hi(base.mul_pos_hi(xhi,xhi),base.mul_pos_hi(yh,yh))
        bracketl=base.sub_lo(tl,base.mul_pos_hi(base.mul_pos_hi(2.,constants.j1_hi),dh))
        bracketh=base.sub_hi(th,base.mul_pos_lo(base.mul_pos_lo(2.,constants.j1_lo),dl))
        kbl,kbh=base.mul_interval(il,ih,bracketl,bracketh)
        zl=base.mul_pos_lo(.5,base.mul_pos_lo(kl,ssl));zh=base.mul_pos_hi(.5,base.mul_pos_hi(kh,ssh))
        eml,emh=exp_table.query('E',zl,zh)
        epl=base.div_pos_lo(1.,emh);eph=base.div_pos_hi(1.,eml)
        skl,skh=base.mul_interval(eml,emh,kbl,kbh)
        cpl=base.add_lo(cl[start:stop,None],cl[None,:]);cph=base.add_hi(ch[start:stop,None],ch[None,:])
        scl,sch=base.mul_interval(epl,eph,cpl,cph)
        rl=base.sub_lo(skl,sch);rh=base.sub_hi(skh,scl)
        rr=base.abs_square_upper(rl,rh)
        den=base.mul_pos_lo(jl[start:stop,None],jl[None,:])
        gauss=base.mul_pos_hi(wh[start:stop,None],wh[None,:])
        common=base.div_pos_hi(base.mul_pos_hi(4.,gauss),den)
        area=base.mul_pos_hi(widths[start:stop,None],widths[None,:])
        B[start:stop]=sqrt_array_hi(base.mul_pos_hi(area,base.mul_pos_hi(common,rr)))
    B=np.maximum(B,B.T)
    assert np.all(np.isfinite(B)) and np.all(B>=0)
    tail,kt,at=pos.analytic_tail(rlo,rhi,dhi,ih,kh,al,args.cutoff,constants)
    return B,tail,{'kernel_squared_tail':kt,'additive_squared_tail':at,'minimum_jbar_lower':float(jl.min()),'radial_edges_sha256':hashlib.sha256(edges.tobytes()).hexdigest()}

def certify(lo,hi,args,tabs):
    begin=time.perf_counter()
    B,tail,info=majorant(lo,hi,args,tabs)
    n=len(B)
    v=np.ones(n)
    for _ in range(args.power_steps):
        w=B@v
        assert np.isfinite(w).all() and np.min(w)>0
        v=w/np.max(w)
    # The positive binary64 vector is an exact witness; no eigenvalue accuracy is assumed.
    assert np.min(v)>0
    rows=np.empty(n)
    for i in range(n):
        ratios=base.div_pos_hi(v,float(v[i]))
        products=base.mul_pos_hi(B[i],ratios)
        _,sumhi=base.sum_enclosure(products)
        rows[i]=sumhi
    finite=float(rows.max())
    tailnorm=float(base.sqrt_pos_hi(tail))
    bound=float(base.add_hi(finite,tailnorm))
    key=f'{lo:.10f}_{hi:.10f}_N{n}'
    witness=ROOT/'logs'/f'cell_witness_{key}.json'
    witness.write_text(json.dumps({'v_binary64_hex':[float(x).hex() for x in v],'row_upper_binary64_hex':[float(x).hex() for x in rows]},separators=(',',':'))+'\n',encoding='utf-8')
    row={'rho_lo':lo,'rho_hi':hi,'x_panels':n,'cutoff':args.cutoff,'finite_operator_upper':finite,'outside_hs_squared_upper':tail,'outside_operator_upper':tailnorm,'operator_upper':bound,'pass':bound<2.,'seconds':time.perf_counter()-begin,'matrix_upper_sha256':hashlib.sha256(B.tobytes()).hexdigest(),'witness_file':str(witness.relative_to(ROOT)),'witness_sha256':hashlib.sha256(witness.read_bytes()).hexdigest(),**info}
    del B
    return row

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--rho-min',type=float,default=.4);ap.add_argument('--rho-max',type=float,default=.43)
    ap.add_argument('--table-rho-max',type=float,default=.43)
    ap.add_argument('--rho-panels',type=int,default=30)
    ap.add_argument('--x-panels',type=int,default=1600);ap.add_argument('--cutoff',type=float,default=9.)
    ap.add_argument('--q-bins',type=int,default=4096);ap.add_argument('--a-bins',type=int,default=16384)
    ap.add_argument('--exp-bins',type=int,default=65536);ap.add_argument('--v-panels',type=int,default=64)
    ap.add_argument('--precision',type=int,default=100);ap.add_argument('--chunk',type=int,default=24)
    ap.add_argument('--power-steps',type=int,default=40);ap.add_argument('--max-seconds',type=int,default=540)
    ap.add_argument('--label',default='pilot');ap.add_argument('--pilot',action='store_true')
    args=ap.parse_args();started=time.perf_counter()
    assert 0<args.rho_min<=args.rho_max<=args.table_rho_max<.5
    hw=hardware();ctx.prec=args.precision
    inputs=[Path(__file__).resolve(),ROOT/'cut_bounds/plur_cert.py',ROOT/'cut_bounds/plur_cert_positive.py']
    metadata={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':sys.argv,'parameters':vars(args),'hardware':hw,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'flint':flint.__version__,'random_generator':None,'seed':None,'input_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'reproduction':'Directed upper bounds; floating witness may vary by BLAS, but every witness is checked with outward rounding. Exact bit reproduction expected for the same binary64 environment and dependency versions; theorem uses only the verified upper bound.'}
    dump(Path('logs')/f'cells_{args.label}_metadata.json',metadata)
    tabs=tables(args)
    if args.pilot:
        intervals=[(args.rho_min,args.rho_max)]
    else:
        edges=np.linspace(args.rho_min,args.rho_max,args.rho_panels+1)
        edges[0]=args.rho_min;edges[-1]=args.rho_max
        intervals=list(zip(map(float,edges[:-1]),map(float,edges[1:])))
    results=[]
    out=ROOT/'logs'/f'cells_{args.label}_rows.jsonl'
    for lo,hi in intervals:
        if time.perf_counter()-started>args.max_seconds:
            print('Checkpoint: command time budget reached; remaining slabs not certified.',flush=True)
            break
        row=certify(lo,hi,args,tabs)
        with out.open('a',encoding='utf-8') as f:f.write(json.dumps(row)+'\n')
        results.append(row)
        print(json.dumps({k:row[k] for k in ('rho_lo','rho_hi','x_panels','finite_operator_upper','outside_operator_upper','operator_upper','pass','seconds')}),flush=True)
    done=len(results)==len(intervals)
    summary={'complete':done,'all_pass':done and all(r['pass'] for r in results),'slabs':len(results),'requested_slabs':len(intervals),'worst_upper':max((r['operator_upper'] for r in results),default=None),'elapsed_seconds':time.perf_counter()-started}
    dump(Path('logs')/f'cells_{args.label}_summary.json',summary)
    print(json.dumps(summary),flush=True)
    return 0 if summary['all_pass'] else 2

if __name__=='__main__':raise SystemExit(main())
