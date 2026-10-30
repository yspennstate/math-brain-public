"""Independent exact continuous gate for D91 from frozen refined raw sums."""
import hashlib,json,math
from pathlib import Path
from fractions import Fraction as R
ROOT=Path(__file__).resolve().parent

def upper(q):
    m,e=q['upper'];return R(m*2**e) if e>=0 else R(m,2**(-e))

def constants(L,values):
    g,h,t,m,k=values
    # Independently collect the five error categories before summing.
    b4=R(25,288)+R(49,100)*L/(1-L)
    b3=R(1,6)+R(49,20)*L*b4
    b1=R(5,24)+R(49,20)*L*b3
    U=[g*(R(1,6)+R(49,20)*L*b4),
       h/2*(R(1,24)+b3*(1/(1-L)+1+L/2)+R(1,6)),
       m*b1/(2*(1-L)**2),t/6,k/(24*(1-L)**4)]
    M=[h/12,5*m/24,5*t*L*L/72,k*(2+4*L*L+L**4)/24]
    return sum(U),sum(M)

def main():
    d=91;L=R(209657,2000000);beta=R(49,4)
    assert d*L*L>=1 and L<=R(39,250)<1
    fU,fM=constants(L,(R(1,8),R(1,5),R(2,5),R(1,2),R(3,5)))
    qU,qM=constants(L,tuple(map(R,(8,20,38,38,99))))
    alpha=(d-qU)/fU;B=81*((1-qU/d)*fM/fU+qM/d);curvature=32*alpha+2*B+3600
    assert d>qU+9*beta*fU and qM-qU*fM/fU>0
    folder=ROOT/'gaussian_fourth_gate_refined_v1'
    report=json.loads((folder/'report.json').read_text(encoding='utf-8'))
    replay=json.loads((ROOT/'gaussian_fourth_refined_replay.json').read_text(encoding='utf-8'))
    assert replay['status']=='EXACT_ALL_INTERVALS_AND_DIRECT_QUADRATURE_PASS'
    assert replay['producer_report_sha256']==hashlib.sha256((folder/'report.json').read_bytes()).hexdigest()
    cfg=json.loads((folder/'config.json').read_text(encoding='utf-8'));assert cfg['bin_width']=='1/16' and cfg['radius']=='6'
    bins=json.loads((folder/'bins.json').read_text(encoding='utf-8'));assert len(bins['bins'])==96
    P,D,tail=map(upper,(bins['P'],bins['D'],bins['tail']))
    point=[];pin={}
    for i in range(86):
        path=folder/f'endpoint_{i:03d}.json';pin[str(path.relative_to(ROOT.parent))]=hashlib.sha256(path.read_bytes()).hexdigest()
        r=json.loads(path.read_text(encoding='utf-8'));s=R(10,100-i)
        assert r['s']==str(s) and r['source_sha256']==cfg['source_sha256']
        assert pin[str(path.relative_to(ROOT.parent))]==report['endpoints'][i]['sha256']
        g_upper=upper(r['F_quadrature'])+R(9,10)*s*P*D+tail-R(1,3)
        u_upper=upper(r['Q_quadrature'])+90*s*P*D+36*tail
        point.append((s,alpha*(s-g_upper)-B*s*s-u_upper))
    def gate(points,poison=R(0)):
        assert len(points)==86 and [x for x,_ in points]==[R(10,100-i) for i in range(86)]
        return [min(e,f)-curvature*(b-a)**2/8-poison for (a,e),(b,f) in zip(points,points[1:])]
    margins=gate(point);assert len(margins)==85 and min(margins)>R(3,200)
    assert min(gate(point,R(1)))<0,'Inflated U_G must defeat this actual certificate'
    try:gate(point[:-1])
    except AssertionError:pass
    else:raise AssertionError('Missing endpoint accepted')
    output={'status':'EXACT_D91_CONTINUOUS_GATE_PASS','D':d,'lambda_upper':str(L),
        'F_constants':[str(fU),str(fM)],'Q_constants':[str(qU),str(qM)],
        'alpha':str(alpha),'B':str(B),'curvature_upper':str(curvature),
        'positive_replacement_denominator':str(d-qU-9*beta*fU),'positive_d_monotonicity_coefficient':str(qM-qU*fM/fU),
        'interval_margins':list(map(str,margins)),'minimum_exact_margin':str(min(margins)),
        'uniform_margin_floor':'3/200','endpoints':86,'intervals':85,'inflated_U_control_rejected':True,'missing_endpoint_control_rejected':True,
        'endpoint_hashes':pin,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'compensated91_gate.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:output[k] for k in ('status','D','lambda_upper','uniform_margin_floor','endpoints','intervals')}))

if __name__=='__main__':main()
