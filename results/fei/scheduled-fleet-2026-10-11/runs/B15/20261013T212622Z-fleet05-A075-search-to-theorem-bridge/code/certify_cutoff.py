from pathlib import Path
import hashlib, json
engine_path=Path(__file__).with_name('check_matching.py')
engine=engine_path.read_text(encoding='utf-8').split('\nfinite=[];',1)[0]
exec(compile(engine,str(engine_path),'exec'),globals())
seed={2:Q(16,3),3:Q(-21,8),5:Q(95,24),11:Q(-121,24),13:Q(65,24)}
sl,su=enclose(seed); ck(sl>Q(368,125))
prior=json.loads((ROOT/'out'/'FINITE_HEREDITARY.json').read_text(encoding='utf-8'))
equality=[]; prior_rows=0
for row in prior['roots']:
    for v in row['ratios']:
        expr={int(x):Q(c) for x,c in v['ratio_form'].items()}
        if expr==seed:
            ck(row['r']==6 and row['k']==3 and row['l']==0)
            equality.append({'r':row['r'],'k':row['k'],'l':row['l'],'i':v['i']})
        else: ck(Q(v['hi'])<sl)
        prior_rows+=1
rows=[]; orbits=0
for r in [10,11,12]:
    for k in range(r//2+1):
        l=r-2*k; vals=[]
        for typ,present in [('paired',k>0),('isolated',l>0)]:
            if not present: continue
            hist,B,d=compressed(k,l,typ); expr=scale(B,1/d); low,high=enclose(expr)
            ck(high<sl)
            vals.append({'type':typ,'I_i':str(d),'ratio_form':forms(expr),'lo':str(low),'hi':str(high),'margin_below_seed_lower':str(sl-high)})
            orbits+=1
        rows.append({'r':r,'k':k,'l':l,'coordinate_orbits':vals})
ck(len(rows)==19); ck(orbits==33)
for row in json.loads((ROOT/'out'/'POINT_DEFECTS.json').read_text(encoding='utf-8')): ck(Q(row['hi'])<sl)
# log2(e)<3/2 because ln2>2/3; check exact numerical enclosure too.
ck(LN2[0]>Q(2,3))
tail13=2+Q(8,10)+Q(41,8192)*Q(55,2)
ck(tail13<Q(368,125))
point_upper=Q(23,8); ck(point_upper<Q(368,125))
# P(r)=(3r+2)(4r+3)/2: 2P(r)-P(r+1)=6r^2-(7/2)r-23/2>0 for r>=13.
ck(6*13**2-Q(7,2)*13-Q(23,2)>0)
perfect_tail12=2+Q(8,15)+Q(30,4096)*Q(51,2)
ck(perfect_tail12<Q(368,125))
out={'helper_version':'A075-hereditary-cutoff-v1','reused_engine_sha256':hashlib.sha256(engine_path.read_bytes()).hexdigest(),'prior_coordinate_rows_sharpened':prior_rows,'new_compressed_parameter_pairs':len(rows),'new_coordinate_orbits':orbits,'equality_rows':equality,'sharp_all_dimension_constant_form':forms(seed),'sharp_constant_interval':[str(sl),str(su)],'tail_all_r_ge_13_upper_at_cutoff':str(tail13),'point_defect_all_dimension_upper':str(point_upper),'perfect_matching_tail_all_even_r_ge_12_upper_at_cutoff':str(perfect_tail12),'rows':rows,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'SHARP_HEREDITARY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({x:v for x,v in out.items() if x not in ['rows','sharp_constant_interval','equality_rows']},indent=2))
