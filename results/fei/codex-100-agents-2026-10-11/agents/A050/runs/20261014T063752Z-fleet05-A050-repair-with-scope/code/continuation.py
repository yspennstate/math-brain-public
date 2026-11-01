from pathlib import Path
path=Path(__file__).resolve();root=path.parents[1]
src=(path.parent/'check.py').read_text(encoding='utf-8').split('CENSUS=0')[0]
exec(compile(src,str(path.parent/'check.py'),'exec'),globals())
specification={'helper_version':'A050-envelope-continuation-v1','family':'same actual canonical priority gate, b=1 child, next y query, spectator S_a and retained S_x; same inherited reference; fair source-zero fallback','domain':'c=3/4,25/32,13/16 normalized occupancy-family samples; analytic identities for all 3/4<c<13/16, true canonical normalizer certificate retained','case_count':3,'symmetry':'none','arithmetic':'Fraction full same-channel transport, exact Walsh and physical edges, integer/log identities and exact strict integer signs','memory_estimate_MB':100,'max_runtime_seconds':60}
(root/'out/CONTINUATION_SPEC.json').write_text(json.dumps(specification,indent=2),encoding='utf-8')
LIMIT=60
t=tuple(1-2*((x>>1)&1) if not(x&1) else 2*((x>>3)&1)-1 if ((x>>2)&1) else 1 for x in range(16))
p,inf=spec(t,(0,1,2,3));pe=marginal(p,11)
b1=restrict(t,2,1);p1,i1=spec(b1,(0,1,3));p0,i0=spec(restrict(t,2,0),(0,1,3))
checks=[]
for c in (F(3,4),F(25,32),F(13,16)):
 theta=(F(8,15)*c,F(8,15)*c,F(4,15)*c,F(4,15)*c)
 raw={s:__import__('functools').reduce(lambda a,b:a*b,(theta[j] if s>>j&1 else 1-theta[j] for j in range(4)),F(1)) for s in range(16)}
 norm=1-raw[0];q={s:F(1,16) if not s else F(15,16)*w/norm for s,w in raw.items()};qe=marginal(q,11)
 pred={s:w*(p1.get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,w in qe.items()}
 q1={s:w/sum(pred.values()) for s,w in pred.items() if w}
 ck(sum(q1.values())==1)
 # Relabel ambient y=3 to local y=2, fixed independent of data/history.
 qlocal={(s&3)|((s>>3)<<2):w for s,w in q1.items()}
 res=check_query(b1,2,2,qlocal,2,f'continuation_c_{c.numerator}_{c.denominator}')
 thetaA=theta[1];eta=1/(2-thetaA);V=(2-thetaA)**2/(4*(1-thetaA))
 qlast=marginal(qlocal,3)
 for s,w in qlast.items():ck(w==(theta[0] if s&1 else 1-theta[0])*(eta if s&2 else 1-eta))
 C=scale(logvec(V),F(1,2));B=logvec(V)
 ck(res['C_child']==serial(C));ck(res['envelope']==serial(B))
 ck(res['query_influence']==str(F(1,2)));ck(res['terminal_H']=={str(2):str(F(2))});ck(res['terminal_I']==str(F(1)))
 # Incoming likelihood conditional y debt is NOT refunded or reused.
 earlier=scale(logvec(1/(1-F(4,15)*c)),F(1,2));combined=add(earlier,scale(B,F(1,2)))
 ck(bounds(combined)[1]<F(1,4));ck(V<=F(2209,2040))
 checks.append({'c':str(c),'eta':str(eta),'V':str(V),'new_conditional_KL':serial(C),'new_envelope':serial(B),'reach':'1/2','earlier_booked_envelope':serial(earlier),'conservative_total_envelope':serial(combined),'final_mean_H':'2','final_mean_I':'1','final_S4_owner':'2','owner_remaining':'>7/4','query_edge_reserve':'1 (distinct from final S4 owner)'})
ck(2209**8<2*2040**8)
ck(ent(p0.values())=={2:F(2)} and sum(i0.values())==1)
ck(sum(i1.values())==F(3,2))
# Original mean child owner splits exactly: 3=4*(1/2)*(1/2)+2.
ck((4*(sum(i0.values())+sum(i1.values()))/2-2)==3)
ck(F(3)==4*F(1,2)*F(1,2)+2)
result={'status':'PASS','cases':CASES,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'strict_integer_sign':'2209^8 < 2*2040^8','canonical_y_conditional_bill':'1/2 log2 V <1/16','canonical_y_envelope':'log2 V <1/8','combined_booked_envelope':'B_b+(1/2) B_y <1/4','owner':'old mean child S4=3 partitioned into query edge reserve1 and final S4=2; take total conditional envelope from final2 only','cases_detail':checks}
(root/'out/CONTINUATION_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='cases_detail'}))
