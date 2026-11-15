import csv,json,math,time
worst={};rows=0
for r in csv.DictReader(open('census_n6.csv')):
 if not float(r['I']):continue
 rows+=1;ds=list(map(float,r['inf'].split('|')));es=list(map(float,r['erasure'].split('|')));ratios=[e/d if d else 0 for e,d in zip(es,ds)]
 ts=list(map(int,r['minterms'].split('|')));cs=list(map(int,r['maxterms'].split('|')));dt=min(t.bit_count() for t in ts);dc=min(c.bit_count() for c in cs);ts=[t for t in ts if t.bit_count()==dt];cs=[c for c in cs if c.bit_count()==dc];tu=0;cu=0
 for t in ts:tu|=t
 for c in cs:cu|=c
 elig=[i for i in range(6) if tu&cu&(1<<i)];mx=max(ds[i] for i in elig)
 rules={'term_clause_adverse_pair':max(min(ratios[i] for i in range(6) if t&c&(1<<i)) for t in ts for c in cs),'term_clause_maxInf':max(ratios[i] for i in elig if ds[i]==mx),'tied_constant_singleton_score':max(ratios)}
 for k,v in rules.items():
  if k not in worst or v>worst[k]['ratio']:worst[k]=dict(ratio=v,truth_hex=r['truth_hex'],minterms=r['minterms'],maxterms=r['maxterms'])
json.dump(dict(rows=rows,worst=worst),open('extra_rules.json','w'),indent=2);print(json.dumps(worst,indent=2))
