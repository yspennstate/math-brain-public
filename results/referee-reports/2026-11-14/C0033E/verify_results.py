"""Independent precision audits, outward interval point certificates, resources."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,math,time,resource,random,sys
sys.set_int_max_str_digits(0)
from pathlib import Path
from fractions import Fraction
import mpmath as mp
import interval_core as ic
from mp_core import *
from mixed_limit import q_weak,limiting
from optimize_collar import build


def closed_cyclic(L):
    k=mp.exp(L);D=36*(-L*L+(6*k*k+6*k-4)/(k*(3*k+1))*L+3*(k-1)**2/k)
    f22=9*(k-1)**2*(k+3)/(k*(3*k+1))
    return D/(9*L*(f22+6*L)+D)

def point_cert(q,dps,label):
    # Round high precision entries to exact rationals. The certificate is for
    # this rounded point, whose exact coordinates are saved, not its generator.
    digits=dps-30
    nums=[int(mp.nint(x*mp.mpf(10)**digits)) for x in coordinates(q)]
    den=10**digits
    def significant_bounds(z,digits=42):
        lo=ic.endpoint(z._mpi_[0]);hi=ic.endpoint(z._mpi_[1]);mx=max(abs(lo),abs(hi))
        if not mx:return ['0','0']
        ex=math.floor(math.log10(mx.numerator)-math.log10(mx.denominator))
        power=ex-digits+1;unit=Fraction(10)**power
        l=lo/unit;h=hi/unit
        il=l.numerator//l.denominator;ih=-((-h.numerator)//h.denominator)
        return [str(il)+'e'+str(power),str(ih)+'e'+str(power)]
    ic.bounds=significant_bounds
    attempts=[]
    while True:
        ic.iv.dps=dps
        xx=[ic.iv.mpf(n)/ic.iv.mpf(den) for n in nums]
        qiv=ic.matrix(xx);strict_minors=[]
        try:
            for mat in (qiv,[[ic.iv.mpc(int(i==j))-qiv[i][j] for j in range(3)] for i in range(3)]):
                minors=[mat[0][0].real,(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]).real,ic.det3(mat).real]
                assert all(map(ic.pos,minors));strict_minors.append([significant_bounds(x) for x in minors])
            cert=ic.full_certificate(xx)
            break
        except ArithmeticError as exc:
            attempts.append(dict(precision=dps,error=str(exc)))
            print('interval retry',label,dps,str(exc),flush=True)
            dps*=2
            if dps>32000:raise
    cert.update(label=label,precision=dps,retries=attempts,strict_minors=strict_minors,coordinate_numerators=list(map(str,nums)),coordinate_denominator='10^'+str(digits))
    return cert

def main():
    start=time.monotonic();out={'cyclic':[],'precision_audits':[],'point_certificates':[],'normalized_obstruction':[]}
    def checkpoint():
        out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        p=Path('data/verification.json');t=p.with_suffix('.tmp');t.write_text(json.dumps(out,indent=2)+'\n');t.replace(p)
    for L in (1,4,10,50,150,400,1000):
        mp.mp.dps=100+int(3*L/math.log(10));q=cyclic(L);ev=evaluate(q,True);m=closed_cyclic(mp.mpf(L))
        ratio=mp.det(ev['negative_hessian'])/mp.det(ev['J'])
        out['cyclic'].append(strings(dict(L=L,precision=mp.mp.dps,margin=ev['margin'],closed_formula_error=abs(m-ev['margin']),full_determinant_error=abs(ratio-ev['margin']),explicit_remainder_bound=mp.mpf(10)/3*L*mp.exp(-L) if L>=4 else None)))
    records=[]
    search=json.load(open('data/search_mp.json'))
    rng=random.Random(33505);dense={}
    for LL in (20,60,150,400,1000):
        for j in range(120):
            coeff=[str(rng.gauss(0,1)) for _ in range(9)]
            factor=str(rng.uniform(.01,.9));dense[LL,j]=(coeff,factor)
    def reconstruct(row):
        p=row['parameters'];L=p['L']
        if row['group'].startswith('mixed'):return mixed(mp.exp(-L),*[mp.mpf(str(p[k])) for k in ('alpha','beta','eta','ratio','phase')])
        if row['group'].startswith('spectral_graph'):return spectral(p['params'],L)
        if row['group'].startswith('cyclic'):return cyclic(L)
        if row['group'].startswith('ambient'):
            q=cyclic(L);gap=mp.mpf('.5')-mp.sqrt(3)*abs(q[0,1])
            if 'direction' in p:
                i=p['direction'];return q+B[i]*(p['sign']*gap*mp.mpf(p['radius'])/mp.sqrt(tr(B[i]*B[i])))
            coeff,factor=dense[L,p['dense_index']]
            t=sum((mp.mpf(coeff[i])*B[i] for i in range(9)),mp.zeros(3));t/=mp.sqrt(mp.re(tr(t*t)))
            return q+gap*mp.mpf(factor)*t
        raise ValueError(row['group'])
    for group,g in search['groups'].items():
        for which in ('minimum','minimum_scaled'):
            row=g[which]
            if row is None:continue
            dps=max(row['precision'],160)
            mp.mp.dps=dps;q=reconstruct(row);v1=evaluate(q)
            mp.mp.dps=dps*2;q=reconstruct(row);v2=evaluate(q)
            error=abs(v1['margin']-v2['margin']);assert error<mp.mpf('1e-55'),(group,which,'precision',mp.nstr(error))
            assert abs(v2['margin']-mp.mpf(row['margin']))<mp.mpf('1e-55'),(group,which,'saved generator',mp.nstr(v2['margin']-mp.mpf(row['margin'])))
            out['precision_audits'].append(strings(dict(group=group,which=which,precision1=dps,precision2=2*dps,margin=v2['margin'],difference=error)))
            records.append((v2['margin'],v2['scaled'],row));checkpoint()
    # A fixed real subfamily approaches the universal coefficient obstruction.
    for L in (10,20,60,150,400,1000):
        mp.mp.dps=140+int(16*L/math.log(10));h=mp.exp(-L);q=q_weak(mp.mpf('.5'),h,h**6);ev=evaluate(q)
        nu=h*(1-h)/4;K=2*mp.log((mp.mpf('.5')-h*(1-h))/(h*(1-h)))
        e2=h**12;limit=limiting(mp.mpf('.5'),h)
        assert e2<=nu**8/(mp.mpf('8e13')*(K+1)) or L<14
        out['normalized_obstruction'].append(strings(dict(L=L,precision=mp.mp.dps,margin=ev['margin'],logscale=ev['logscale'],product=ev['margin']*ev['logscale'],scaled=ev['scaled'],limit=limit,error=abs(ev['margin']-limit),uniform_remainder=mp.mpf('4e13')*e2/nu**8,proved_collar=bool(e2<=nu**8/(mp.mpf('8e13')*(K+1))))))
    # Extremal sweep point and both objective extrema at the last collar.
    selected=[('sweep_min',min(records,key=lambda v:v[0])[2]),('sweep_scaled_min',min(records,key=lambda v:v[1])[2])]
    for label,row in selected:
        dps=max(250,2*row['precision']);mp.mp.dps=dps+50;q=reconstruct(row)
        cert=point_cert(q,dps,label);out['point_certificates'].append(cert);checkpoint()
        print('certified',label,cert['margin'],flush=True)
    for filename,label in [('collar_optimization.json','optimized_collar_400'),('scaled_optimization.json','optimized_scaled_400')]:
        dat=json.load(open('data/'+filename));run=dat['runs'][-1];row=run['best'];L=run['L'];dps=250+int(14*L/math.log(10));mp.mp.dps=dps+50
        q=build(row['x'],L);v1=evaluate(q)
        mp.mp.dps*=2;v2=evaluate(build(row['x'],L));assert abs(v1['margin']-v2['margin'])<mp.mpf('1e-55')
        mp.mp.dps=dps+50;q=build(row['x'],L);cert=point_cert(q,dps,label);out['point_certificates'].append(cert);checkpoint()
        print('certified',label,cert['margin'],flush=True)
    dps=5200;mp.mp.dps=dps+50;t=mp.exp(-1000)
    q=mixed(t,2,2,mp.mpf(21)/10)
    cert=point_cert(q,dps,'special_mixed_min_L1000');out['point_certificates'].append(cert);checkpoint()
    print('certified special minimum',cert['margin'],flush=True)
    # A strictly feasible all-nine-direction certificate in the proved mixed
    # subcollar, with log p_min roughly 100 rather than merely a limit formula.
    dps=1800;mp.mp.dps=dps+50;h=mp.exp(-100);q=q_weak(mp.mpf('.5'),h,h**6)
    cert=point_cert(q,dps,'proved_mixed_collar_L100');out['point_certificates'].append(cert)
    out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
    Path('data/verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print('done',out['seconds'],out['peak_rss_mib'],flush=True)
if __name__=='__main__':main()
