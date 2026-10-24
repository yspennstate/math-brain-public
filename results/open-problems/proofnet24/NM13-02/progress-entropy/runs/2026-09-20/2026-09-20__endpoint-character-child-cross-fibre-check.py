"""Sanity checks for NM13-02 endpoint character-child theorem.
Not a proof substitute: theorem in the paired markdown report is analytic.
"""
import json
import numpy as np
from mpmath import mp
mp.dps = 500


def fwht(vals):
    a=np.array(vals,dtype=float); N=a.size; h=1
    while h<N:
        for i in range(0,N,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a/N


def phi(coeff,m):
    if m==0: return 0.0
    s=2.0-1.0/m
    return m*(float(np.sum(np.abs(coeff)**s))-1.0)


def local_data(coeff,m,neg_count):
    n=m+1
    mu=neg_count/(1<<m)
    if mu>0.5:
        mu=1-mu
        coeff=-coeff
    s=2.0-1.0/n
    Mparent=(1-mu)**s+mu**s+(2.0**(1-s))*float(np.sum(np.abs(coeff[1:])**s))
    A=n*(Mparent-1.0)-0.5*phi(coeff,m)
    var=float(np.sum(coeff[1:]**2))
    psi=lambda d,t: d*(abs(t)**(2.0-1.0/d)-t*t)
    T=psi(n,1-mu)+psi(n,mu)-0.5*psi(m,1.0)-0.5*psi(m,1-2*mu)
    U=sum(2*psi(n,abs(t)/2)-0.5*psi(m,abs(t)) for t in coeff[1:])
    return mu,A,var,T,U

cases=0; max_violation=-1e100; max_decomp_err=0.0
max_ratio=-1e100; max_case=None; max_T_varhalf=-1e100; max_U_halfsq=-1e100
for m in range(1,5):
    N=1<<m
    for mask in range(1<<N):
        vals=np.ones(N)
        for x in range(N):
            if (mask>>x)&1: vals[x]=-1.0
        coeff=fwht(vals)
        mu,A,var,T,U=local_data(coeff,m,mask.bit_count())
        rhs=4*mu*(1-mu)
        max_violation=max(max_violation,A-rhs)
        max_decomp_err=max(max_decomp_err,abs(A-(T+U)))
        max_T_varhalf=max(max_T_varhalf,T-var/2)
        max_U_halfsq=max(max_U_halfsq,U-var/2)
        if mu>0:
            rr=A/mu
            if rr>max_ratio:
                max_ratio=rr; max_case=(m,mask,mu,A,rr)
        if A-rhs>2e-10 or abs(A-(T+U))>2e-10 or T-var/2>2e-10 or U-var/2>2e-10:
            raise AssertionError((m,mask,mu,A,rhs,T,U,var))
        cases+=1

max_b_over_t2=mp.mpf('-inf'); max_b_arg=None
for n in range(2,201):
    m=n-1; s=mp.mpf(2)-mp.mpf(1)/n; r=mp.mpf(2)-mp.mpf(1)/m
    for a in range(m):
        t=mp.power(2,-a)
        b=n*mp.power(2,1-s)*t**s-(mp.mpf(m)/2)*t**r
        rr=b/(t*t)
        if rr>max_b_over_t2:
            max_b_over_t2=rr; max_b_arg=(n,a,rr)
        if b>t*t+mp.mpf('1e-100'):
            raise AssertionError(('lattice fibre',n,a,b,t*t))


def Cn(n,mu):
    m=n-1; s=mp.mpf(2)-mp.mpf(1)/n; r=mp.mpf(2)-mp.mpf(1)/m
    return n*((1-mu)**s+mu**s-1)-(mp.mpf(m)/2)*((1-2*mu)**r-1)

max_C=mp.mpf('-inf'); max_C_arg=None
for n in range(2,15):
    N=1<<(n-1)
    for k in range(N//2+1):
        mu=mp.mpf(k)/N
        C=Cn(n,mu)
        if C>max_C: max_C=C; max_C_arg=(n,k,mu,C)
        if C>mp.mpf('1e-100'): raise AssertionError(('C dyadic',n,k,C))
for n in [3,4,5,8,16,32,64,128]:
    for k in range(1001):
        mu=mp.mpf(k)/2000
        C=Cn(n,mu)
        if C>mp.mpf('1e-80'): raise AssertionError(('C grid',n,k,C))


def one_point(n):
    m=n-1; delta=mp.power(2,-m)
    psi=lambda d,t: d*(abs(t)**(mp.mpf(2)-mp.mpf(1)/d)-t*t)
    T=psi(n,1-delta)+psi(n,delta)-mp.mpf('0.5')*psi(m,1)-mp.mpf('0.5')*psi(m,1-2*delta)
    U=2*psi(n,delta)-mp.mpf('0.5')*psi(m,2*delta)
    A=T+(1/delta-1)*U
    return delta,T,U,A

one_rows=[]; max_whole=mp.mpf('-inf'); max_whole_n=None
for n in range(2,301):
    d,T,U,A=one_point(n)
    rr=A/d
    if rr>max_whole: max_whole=rr; max_whole_n=n
    if n in [4,8,16,32,64,128,256,300]:
        one_rows.append({
            'n':n,
            'T_over_delta2':mp.nstr(T/(d*d),30),
            'U_over_delta2':mp.nstr(U/(d*d),30),
            'A_over_influence':mp.nstr(rr,30),
        })

out={
  'status':'PASS',
  'exhaustive_boolean_opposite_children_m_1_to_4':cases,
  'max_A_minus_4j1j':repr(max_violation),
  'max_fibre_decomposition_error':repr(max_decomp_err),
  'max_T_minus_variance_over_2':repr(max_T_varhalf),
  'max_sumU_minus_variance_over_2':repr(max_U_halfsq),
  'max_A_over_j_exhaustive':repr(max_ratio),
  'max_A_over_j_case_m_mask_j_A_ratio':max_case,
  'max_lattice_b_over_t2_n_le_200':mp.nstr(max_b_over_t2,40),
  'max_lattice_b_arg_n_a_ratio':[max_b_arg[0],max_b_arg[1],mp.nstr(max_b_arg[2],40)],
  'max_Cn_dyadic_n_le_14':mp.nstr(max_C,40),
  'max_Cn_arg':[max_C_arg[0],max_C_arg[1],mp.nstr(max_C_arg[2],20),mp.nstr(max_C_arg[3],30)],
  'one_point_max_A_over_influence_n_le_300':mp.nstr(max_whole,40),
  'one_point_max_n':max_whole_n,
  'one_point_selected_rows':one_rows,
}
print(json.dumps(out,indent=2))
