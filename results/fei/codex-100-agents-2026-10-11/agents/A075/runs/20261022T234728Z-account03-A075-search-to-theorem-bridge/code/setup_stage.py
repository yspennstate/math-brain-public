from pathlib import Path
import json, hashlib, shutil
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261021T173628Z-account03-A075-search-to-theorem-bridge'
(ROOT/'out').mkdir(exist_ok=True)
helpers={}
for name in ['arithmetic.py','block_reveal.py','asymptotic.py','bridge.py']:
    source=OLD/'code'/name
    helpers[name]=hashlib.sha256(source.read_bytes()).hexdigest()
    shutil.copyfile(source,ROOT/'code'/name)
spec={
 'revision':'A075-diagonal-v1','helper_versions':helpers,
 'family':'F_n=J(g_n^6), g_n negative on {0,1,2}; J=-h(x xor1), h negative {0,1,2,4,8,16,32,6,17,40}; disjoint uniform blocks',
 'domain':{'pilot':[8],'whole_zero_chain':[8,12,24],'endpoints_only':[16,32,48],'remaining_dimensions':[4,5]},
 'case_count':'29 retained states for n=8,12,24 (j=0..n-6), plus 6 endpoints for n=16,32,48; six fixed initial prefix profiles per n; two analytic fixed remaining dimensions. No symmetry reduction.',
 'policy':'Original coordinates 2=0 then 0=0; carry original proportional D_b; subsequently query padding 3,4,... and assign all outgoing debit to zero child, zero to constant+ selected-core sibling. Full functions and stopped siblings retained.',
 'arithmetic':'rational Walsh/product-moment identities and rational log forms; 192-bit directed intervals, 80-term atanh with proved tail; exact polynomial entropy expansion',
 'memory_estimate_mb':150,'pilot_max_seconds':55,'maximum_runtime_seconds':180,
 'automatic_escalation':False,'finite_claim_scope':'Only declared states. Infinite claims require separate analytic proof.'}
(ROOT/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(ROOT.parent.parent/'STATUS.md').write_text('STATE: A075 stage7 active: checking fixed-depth versus growing-depth inherited-debit obstruction, and exact unused-sibling repair; FEI OPEN.\nNEXT: certify the diagonal remaining-capacity law, preserve full history, and hand analytic quantifiers to A074/A092.\n',encoding='utf-8')
print(json.dumps({'spec_frozen':str(ROOT/'out/FROZEN_SPEC.json'),'helpers':helpers}))
