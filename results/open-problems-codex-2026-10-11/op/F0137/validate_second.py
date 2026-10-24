import pathlib,json,hashlib
from fractions import Fraction as F
R=pathlib.Path(__file__).resolve().parent
old=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
new=[json.loads(x) for x in (R/'SECOND_CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
byclaim={x['claim']:x for x in old}
for x in new: byclaim[x['claim']]=x
(R/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in byclaim.values()),encoding='utf8')
results=json.loads((R/'auxiliary_results.json').read_text())
strong=results['stronger_example']
assert F(strong['A'])>1 and F(strong['kappa'])>1 and F(strong['delta'])>0
assert F(strong['origin_numerator_two_term_bound'])==F(-211939,2153627)<0
assert F(strong['exit_displacement_two_term_bound'])==F(-5887889,437186281)<0
assert F(strong['B'])<0 and F(strong['C'])+F(strong['B'])<0
assert all(x['likelihood_ratio']==x['formula_ratio'] for x in results['reversal_checks'])
assert len(results['saturated_reversal_paths'])==4
source=(R/'AuxiliaryAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in source and 'native_decide' not in source
summary={'total_claims':len(byclaim),'new_claims':len(new),'stronger_example_checked':True,
 'arbitrary_reversal_paths':4,'saturated_reversal_paths':4,
 'lean_input_sha256':hashlib.sha256((R/'AuxiliaryAlgebra.lean').read_bytes()).hexdigest(),
 'full_conjecture_solved':False}
(R/'second_validation.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps(summary,indent=2))
