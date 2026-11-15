"""Exact convolution for all f_t=(-1)^t sign(r-t-1/2), at fixed n.
Polynomial packing is carry-free: Q coefficients <=2^(n+k), L<=2^n.
GMP multiplies the packed integers, then Python unpacks exact coefficients.
"""
import ctypes,math,time,json,argparse
import stable_logs as sl
from pathlib import Path
lib=ctypes.CDLL(str(Path('polyconv.dylib').resolve()))
lib.multiply_bytes.argtypes=[ctypes.c_char_p,ctypes.c_size_t,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_void_p]
lib.multiply_bytes.restype=ctypes.c_size_t

def convolution(a,b,width,count):
    assert max(a).bit_length()<=width*8 and max(b).bit_length()<=width*8
    aa=b''.join(x.to_bytes(width,'little') for x in a)
    bb=b''.join(x.to_bytes(width,'little') for x in b)
    buf=ctypes.create_string_buffer((len(a)+len(b))*width)
    size=lib.multiply_bytes(aa,len(aa),bb,len(bb),buf)
    assert size<=len(buf)
    raw=buf.raw
    return [int.from_bytes(raw[j*width:(j+1)*width],'little') for j in range(count)]

def all_parity_thresholds(n):
    choose=[math.comb(n,k) for k in range(n+1)]
    base=[math.comb(n-1,r) for r in range(n)]
    total=1<<n
    den=[total*n*(total-2*x) for x in base]
    A=[None]*n;B=[None]*n;G=[None]*n
    frow=[((-1)**j)*x for j,x in enumerate(base)]
    for k in range(n+1):
        if k==0:
            L=[total]*n;Q=[total]*n
        else:
            ck=[math.comb(k,s) for s in range(k+1)]
            v=[-1<<k];cum=0
            for a in range(1,n+1):
                if a-1<=k:cum+=ck[a-1]
                v.append(2*cum-(1<<k))
            c=[math.comb(n-k,t) for t in range(n-k+1)]
            L=convolution([abs(x) for x in v],c,(n+2+7)//8,n+1)[1:]
            Q=convolution([x*x for x in v],c,(n+k+2+7)//8,n+1)[1:]
            # t>r has a=r-t<0 and contributes the constant tail.
            tail=sum(c)
            for r in range(n):
                if r<len(c):tail-=c[r]
                # Here the threshold is r+1, so remove c[r+1] too.
                beyond=tail-(c[r+1] if r+1<len(c) else 0)
                L[r]+=(1<<k)*beyond
                Q[r]+=(1<<(2*k))*beyond
        if k<n:Frow=[2*x for x in frow]
        else:
            Frow=[];cum=0
            for j in range(n):cum+=choose[j];Frow.append(2*cum-total)
        for j,F in enumerate(Frow):
            if not F:continue
            # Keep the complete dynamic range. Exact differences protect near-one ratios.
            logw=math.log2(choose[k])+2*math.log2(abs(F))-math.log2(den[j])
            la=sl.log_neg_log_dyadic(Q[j],n+k)
            R=Q[j]*(1<<(n-k))
            lb=sl.log_log_ratio(R-F*F,F*F)
            lg=sl.log_log_ratio(L[j]-abs(F),abs(F))
            if la is not None:A[j]=sl.add(A[j],logw+la)
            if lb is not None:B[j]=sl.add(B[j],logw+lb)
            if lg is not None:G[j]=sl.add(G[j],logw+lg)
        if k<n-1:
            nxt=[0]*n
            for j in range(n):nxt[j]=frow[j]+(frow[j-1] if j else 0)+(nxt[j-1] if j else 0)
            frow=nxt
    logs={'A/I':A,'B/I':B,'Gamma/I':G}
    linear={key:[(2.**x if x>-1074 else None) if x is not None else 0. for x in values] for key,values in logs.items()}
    return linear,logs

def main():
    p=argparse.ArgumentParser();p.add_argument('--dimensions',nargs='+',type=int,default=[25,32,64,128,256,512,1000,1024,2000]);args=p.parse_args()
    for n in args.dimensions:
        path=Path(f'parity_thresholds_v3_{n:04d}.json')
        if path.exists():continue
        t=time.monotonic();vals,logs=all_parity_thresholds(n)
        row={'n':n,'family':'parity times threshold, all r=1,...,n','ratios':vals,'log2_ratios':logs,'underflow_note':'null in ratios means a positive value below binary64 range; use log2_ratios','wall_seconds':time.monotonic()-t,'maxima':{}}
        for name,v in vals.items():
            j=max(range(n),key=lambda j: logs[name][j] if logs[name][j] is not None else float("-inf"));row['maxima'][name]={'value':v[j],'threshold':j+1}
        path.write_text(json.dumps(row,indent=2)+'\n')
        print(n,row['wall_seconds'],row['maxima'],flush=True)
if __name__=='__main__':main()
