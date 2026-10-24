from pathlib import Path
import json
# Explicit normalization (the common factor cancels in ratios but energies should also be exact).
p=Path('second_numerical_checks.py');s=p.read_text(encoding='utf-8-sig');s=s.replace('E.append(total)','normalizer=1+math.exp(-(T*T+1)/(2*delta*delta))\n  E.append(total/(normalizer*normalizer))');p.write_text(s,encoding='utf8')
# Add the exact finite optimization for asymmetric intensity pairs, a boundary check on B4.
q=Path('second_numerical_checks.json');d=json.loads(q.read_text());d['optimal_symmetric_intensity_pairs']=[]
for a,b in [(0,0),(1,0),(1,1),(4,1),(1e-8,1e4)]:
 h=((a**.5+b**.5)/2)**2
 I=(a**.5-h**.5)**2+(b**.5-h**.5)**2
 opt=.5*(a**.5-b**.5)**2
 assert abs(I-opt)<=1e-10*max(1,opt)
 d['optimal_symmetric_intensity_pairs'].append({'target_positive_rate':a,'target_negative_rate':b,'reference_equal_rate':h,'distance':I,'formula':opt})
q.write_text(json.dumps(d,indent=2),encoding='utf8')
# Save verified Lean result in the ongoing report now, before closing status.
lean=Path('lean_hellinger_check.txt').read_text()
assert 'exit=0;' in lean and 'sorryAx' not in lean
p=Path('SECOND_ATTEMPT.md');s=p.read_text();s=s.replace('This elementary identity and inequality are being formalized in HellingerObstruction.lean.','This elementary identity, inequality and optimum are formalized in HellingerObstruction.lean. The final Lean run exited 0; all three named lemmas have only [propext, Classical.choice, Quot.sound] as axioms, with no sorryAx. The integral and path-law arguments are written proofs, not claimed to be Lean-formalized.');p.write_text(s,encoding='utf8')
# Accurately log the metadata fetch as well as the search requests already recorded.
p=Path('search_log.json');d=json.loads(p.read_text());d.append({'date':'2026-10-12','service_query':'kanda_metadata','url':'https://api.openalex.org/works/W1500198325','status':'ok','file':'kanda_metadata.json'});p.write_text(json.dumps(d,indent=2),encoding='utf8')
