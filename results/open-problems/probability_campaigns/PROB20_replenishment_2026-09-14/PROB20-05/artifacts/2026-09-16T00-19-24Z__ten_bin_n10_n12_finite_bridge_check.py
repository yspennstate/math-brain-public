"""PROB20-05 exact/self-check artifact: ten-bin finite bridge at n=10,11,12.

This reproduces the checkpoint's two finite certificates:
  (i) the exact two-sample endpoint certificate, exhaustively over S_10;
  (ii) the exact integer cellwise diagonal-residual certificate on symmetry representatives
       not certified by (i).

The helper C++ generator is compiled at runtime only to make the 10! enumeration fast.
SciPy's Hungarian routine is used only to FIND a balanced cell assignment; the returned
branch counts and objective W are recomputed as exact Python integers. Thus successful
cell certificates do not rely on floating-point optimality.

Expected residuals are precisely the structured targets already covered analytically:
identity; one adjacent transposition; and, at n=10, positive reversal and its end-adjacent
perturbation. The report explains their analytic closure.
"""

from __future__ import annotations
import ast
import subprocess
import tempfile
from pathlib import Path
import numpy as np
from scipy.optimize import linear_sum_assignment

CPP = r'''
#include <array>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

long long psi12(int s){
    int a=abs(s);
    if(a==0) return 8;
    if(a==1) return 13;
    return 12LL*a;
}

long long localpair(const array<int,10>&p){
    long long s=0;
    for(int j=0;j<10;j++) for(int l=0;l<10;l++){
        int d=j-l, e=p[j]-p[l];
        s += llabs(d-e)*psi12(d+e);
    }
    return s;
}

vector<int> invp(const vector<int>&p){
    int n=p.size(); vector<int> q(n);
    for(int i=0;i<n;i++) q[p[i]]=i;
    return q;
}
vector<int> rc(const vector<int>&p){
    int n=p.size(); vector<int> q(n);
    for(int i=0;i<n;i++) q[i]=n-1-p[n-1-i];
    return q;
}
vector<int> canon4(const vector<int>&p){
    auto a=p, b=invp(p), c=rc(p), d=invp(c);
    return min(min(a,b),min(c,d));
}

int main(int argc,char**argv){
    if(argc!=3){ cerr << "usage: gen n k\n"; return 2; }
    int n=atoi(argv[1]), k=atoi(argv[2]);
    if(n<10 || k<0 || k+10>n) return 3;

    array<array<long long,10>,10> U{};
    for(int j=0;j<10;j++) for(int x=0;x<10;x++){
        long long s=0;
        for(int i=0;i<n;i++) if(i<k || i>=k+10)
            s += 2LL*llabs(j-x)*psi12(2*(k-i)+j+x);
        U[j][x]=s;
    }

    array<int,10> p; iota(p.begin(),p.end(),0);
    set<vector<int>> reps;
    long long failures=0;
    const long long threshold=8LL*n*n*n*n;
    do{
        long long S=localpair(p);
        for(int j=0;j<10;j++) S += U[j][p[j]];
        // J=S/(12 n^4), and J>=2/15 is equivalent to 5S>=8n^4.
        if(5*S < threshold){
            ++failures;
            vector<int> q(n); iota(q.begin(),q.end(),0);
            for(int j=0;j<10;j++) q[k+j]=k+p[j];
            reps.insert(canon4(q));
        }
    }while(next_permutation(p.begin(),p.end()));

    cerr << failures << " " << reps.size() << "\n";
    for(const auto&q:reps){
        cout << '[';
        for(int i=0;i<n;i++){ if(i) cout << ','; cout << q[i]; }
        cout << "]\n";
    }
}
'''

def compile_generator(tmp: Path) -> Path:
    src=tmp/'gen.cpp'; exe=tmp/'gen'
    src.write_text(CPP,encoding='utf-8')
    subprocess.run(['g++','-O3','-std=c++17',str(src),'-o',str(exe)],check=True)
    return exe

def endpoint_reps(exe: Path,n:int,k:int):
    cp=subprocess.run([str(exe),str(n),str(k)],check=True,text=True,
                      stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    failures,reps_count=map(int,cp.stderr.strip().split())
    reps=[tuple(ast.literal_eval(line)) for line in cp.stdout.splitlines() if line.strip()]
    assert len(reps)==reps_count
    return failures,reps

def cell_margin(p: tuple[int,...]) -> int:
    n=len(p)
    a=np.arange(1-n,n,2,dtype=np.int64)
    labels=np.repeat(np.arange(n),n)
    rr=np.repeat(np.arange(n),n)
    ss=np.tile(np.arange(n),n)
    lx=a[labels]
    ly=a[np.array([p[i] for i in labels],dtype=np.int64)]
    M=a[rr,None]*lx[None,:]+a[ss,None]*ly[None,:]
    rows,cols=linear_sum_assignment(-M)

    counts=np.bincount(labels[cols],minlength=n)
    assert np.array_equal(counts,np.full(n,n,dtype=counts.dtype))
    # exact integer recomputation of the found assignment
    W=sum(int(M[r,c]) for r,c in zip(rows,cols))
    return 15*W-7*n*n*(n*n-1)

def check_case(exe,n,k,expected_fail,expected_reps,expected_negative):
    failures,reps=endpoint_reps(exe,n,k)
    assert failures==expected_fail, (n,k,failures)
    assert len(reps)==expected_reps, (n,k,len(reps))
    neg=set()
    for idx,p in enumerate(reps,1):
        m=cell_margin(p)
        if m<0: neg.add(p)
        if idx%25000==0:
            print(f'n={n} k={k}: cell checked {idx}/{len(reps)}')
    assert neg==set(expected_negative), (n,k,neg)
    print(f'n={n} k={k}: endpoint_fail={failures}, symmetry_reps={len(reps)}, cell_negative={len(neg)}')

with tempfile.TemporaryDirectory() as td:
    exe=compile_generator(Path(td))

    check_case(
        exe,10,0,59040,15606,
        [
            tuple(range(10)),
            (0,1,2,3,4,5,6,7,9,8),
            (8,9,7,6,5,4,3,2,1,0),
            (9,8,7,6,5,4,3,2,1,0),
        ],
    )

    # k=1 is the 180-degree image of k=0.
    check_case(exe,11,0,116855,46405,[tuple(range(11))])

    # k=2 is the 180-degree image of k=0; k=1 is centrally fixed.
    check_case(
        exe,12,0,291410,139837,
        [tuple(range(12)),(0,1,2,3,4,5,6,7,8,9,11,10)],
    )
    check_case(exe,12,1,366923,93227,[tuple(range(12))])

print('EXACT TEN-BIN n=10,11,12 FINITE-BRIDGE CHECKS PASSED')
