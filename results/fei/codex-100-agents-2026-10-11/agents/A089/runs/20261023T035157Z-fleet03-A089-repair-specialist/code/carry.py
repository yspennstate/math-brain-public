"""Check second-core continuation against actual already allocated source credits."""
from joint import *
def main():
    start=time.perf_counter();src=json.loads((ROOT/'out/A072_FINANCIAL_SOURCE.json').read_text(encoding='utf-8'));db={}
    for p in (ROOT/'out').glob('PAIR_*_STATES.json'):
        for r in json.loads(p.read_text(encoding='utf-8')):db[(tuple(r['pair']),tuple(map(tuple,r['types'])))]=r
    records=[]
    for policy_index,pol in enumerate(src['financial_policies']):
        j=pol['core']
        for kind,rr in [('row',pol['rows']),('terminal',pol['terminals'])]:
            for row_index,r in enumerate(rr):
                assign=dict(r['path']);t=tuple(G[x] for x in range(64) if all((x>>i&1)==b for i,b in assign.items()));typ=canonical(t)
                for k in range(2,6):
                    if k==j:continue
                    pair=tuple(sorted((j,k)));types=(typ,('L',6)) if j==pair[0] else (('L',6),typ)
                    node=db[(pair,types)];a=r['credit'];margin=sub(a,node['hull'])
                    records.append({'source_policy':policy_index,'source_kind':kind,'source_index':row_index,'core':j,'next_core':k,'path':r['path'],'reach':r['reach'],'source_credit':a,'joint_required_enclosure':node['hull'],'margin':margin,'zero_new_flow_certified':margin[0]>=0,'definite_shortfall':margin[1]<0})
    ans={'source':'A072 actual six saved financial policies, every row and terminal','cases':len(records),'pass':sum(r['zero_new_flow_certified'] for r in records),'fail':sum(r['definite_shortfall'] for r in records),'unresolved':sum(not r['zero_new_flow_certified'] and not r['definite_shortfall'] for r in records),'runtime_seconds':time.perf_counter()-start,'cases_detail':records}
    (ROOT/'out/INHERITED_CARRY.json').write_text(json.dumps(ans,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in ans.items() if k!='cases_detail'}))
if __name__=='__main__':main()
