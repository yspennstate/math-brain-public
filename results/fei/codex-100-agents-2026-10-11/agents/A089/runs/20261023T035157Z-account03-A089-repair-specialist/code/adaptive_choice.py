"""Second core may be chosen from observations; at most two cores ever queried."""
from joint import *
import joint as primary
from functools import lru_cache
def main():
    start=time.perf_counter();db={};initial_checks=primary.checks
    for p in (ROOT/'out').glob('PAIR_*_STATES.json'):
        for r in json.loads(p.read_text(encoding='utf-8')):db[(tuple(r['pair']),tuple(map(tuple,r['types'])))]=r
    def get(j,k,t,u):
        pair=tuple(sorted((j,k)));types=(t,u) if j<k else (u,t)
        return db[(pair,types)]
    @lru_cache(None)
    def envelope(j,t):
        s=get(j,next(k for k in range(2,6) if k!=j),t,('L',6))['S4'];stop=negative(s);upp=stop[1];actions=[]
        for coord,a,b in rows(t):
            u=(envelope(j,a)[0]+envelope(j,b)[0]+1)//2
            actions.append({'kind':'first_core','coordinate':coord,'upper':u});upp=max(upp,u)
        for k in range(2,6):
            if k==j:continue
            for coord,a,b in rows(('L',6)):
                u=(get(j,k,t,a)['hull'][1]+get(j,k,t,b)['hull'][1]+1)//2
                actions.append({'kind':'select_second_core','core':k,'coordinate':coord,'upper':u});upp=max(upp,u)
        return upp,actions
    results=[];states=[]
    for j in range(2,6):
        for t in TYPES:
            rho,aa=envelope(j,t);states.append({'first_core':j,'type':t,'upper':rho,'actions':aa})
        s=get(j,next(k for k in range(2,6) if k!=j),('L',6),('L',6))['S4'];A=negative(s)
        aa=envelope(j,('L',6))[1]
        margins=[A[0]-a['upper'] for a in aa]
        test(min(margins)>0)
        results.append({'first_core':j,'root_credit':A,'minimum_root_margin_units':min(margins),'all_root_query_margins_units':margins})
    carry=json.loads((ROOT/'out/INHERITED_CARRY.json').read_text(encoding='utf-8'));saved=json.loads((ROOT/'out/A072_FINANCIAL_SOURCE.json').read_text(encoding='utf-8'))
    unres=[r for r in carry['cases_detail'] if not r['zero_new_flow_certified']]
    for r in unres:
        test(not r['path']);p=saved['financial_policies'][r['source_policy']];test('initial_debit' not in p)
        # Source theorem defines each such policy's initial credit as -S, D=0.
    out={'version':'adaptive-two-core-admission-v1','first_core_choices':4,'pre_second_core_envelope_states':len(states),'pair_states':len(db),'at_most_two_adaptively_selected_cores':True,'minimum_root_margin_units':min(x['minimum_root_margin_units'] for x in results),'root_results':results,'states':states,'carry_strict':carry['pass'],'carry_root_equalities_by_source_definition':len(unres),'carry_fail':carry['fail'],'checks':primary.checks-initial_checks,'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/ADAPTIVE_CHOICE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k not in ['states','root_results']}));print('minimum margin display',float(F(out['minimum_root_margin_units'],Q)))
if __name__=='__main__':main()
