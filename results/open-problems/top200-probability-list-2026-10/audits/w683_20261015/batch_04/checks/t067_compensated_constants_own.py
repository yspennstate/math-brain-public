"""Independent Fraction error ledger at both proposed degree cutoffs."""
from fractions import Fraction as F
from pathlib import Path
import json

def constants(L,values):
    g,c2,c3,c31,c4=map(F,values)
    b4=F(25,288)+F(49,100)*L/(1-L)
    b3=F(1,6)+F(49,20)*L*b4
    b1=F(5,24)+F(49,20)*L*b3
    pieces_u=[g*(F(1,6)+F(49,20)*L*b4), c2/2*(F(1,24)+b3*(1/(1-L)+1+L/2)+F(1,6)),c31/2*b1/(1-L)**2,c3/6,c4/(24*(1-L)**4)]
    pieces_m=[c2/12,F(5,24)*c31,F(5,72)*c3*L*L,c4*(2+4*L*L+L**4)/24]
    return sum(pieces_u),sum(pieces_m),pieces_u,pieces_m

def cutoff(D,L):
    fU,fM,fu,fm=constants(L,[F(1,8),F(1,5),F(2,5),F(1,2),F(3,5)])
    qU,qM,qu,qm=constants(L,[8,20,38,38,99])
    beta=F(49,4); hU=qU+9*beta*fU; hM=qM+9*beta*fM
    alpha=(D-qU)/fU; B=81*((1-qU/D)*fM/fU+qM/D)
    assert D*L*L>=1 and D-hU>0 and qM-qU*fM/fU>0
    return {'degree':D,'L':str(L),'fU':str(fU),'fM':str(fM),'qU':str(qU),'qM':str(qM),'HU':str(hU),'HM':str(hM),'alpha':str(alpha),'B':str(B),'curvature':str(32*alpha+2*B+3600),'positive_denominator':str(D-hU),'monotonicity_margin':str(qM-qU*fM/fU),'fU_pieces':list(map(str,fu)),'fM_pieces':list(map(str,fm)),'qU_pieces':list(map(str,qu)),'qM_pieces':list(map(str,qm))}

if __name__=='__main__':
    rows=[cutoff(100,F(1,10)),cutoff(91,F(209657,2000000))]
    first=rows[0]
    for k,v in {'fU':F(57480763247,209952000000),'fM':F(619609,3600000),'qU':F(584087821,21870000),'qM':F(12978097,720000)}.items():assert F(first[k])==v,(k,first[k],v)
    assert F(first['HU'])<57 and F(first['HM'])<38
    assert F(27,2)*20+F(135,4)*38+F(81,4)*99==F(14229,4)<3600
    Path('checks/t067_compensated_constants_own.json').write_text(json.dumps({'complete':True,'rows':rows},indent=2)+'\n',encoding='utf8')
    print(json.dumps([{'degree':r['degree'],'positive_denominator':r['positive_denominator'],'monotonicity_margin':r['monotonicity_margin']} for r in rows]))
