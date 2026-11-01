from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
S=R.parents[2]/'A075'/'runs'/'20261023T043917Z-fleet03-A075-search-to-theorem-bridge'
# All destinations are within the current A071 run; source tree is read only.
pins={}
for name in ['arithmetic.py','profile_engine.py']:
    data=(S/'code'/name).read_bytes();(R/'code'/name).write_bytes(data)
    pins[str(S/'code'/name)]=hashlib.sha256(data).hexdigest()
for name in ['REPORT.md','PROOF.md','CLAIMS.json','out/BANK_AUDIT.json']:
    pins[str(S/name)]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(R/'out'/'SOURCE_PINS.json').write_text(json.dumps(pins,indent=2)+'\n',encoding='utf-8')
spec={'helper_version':'A071 fourth-v1; copied A084/A075 prime-log utilities, new direct Walsh subset spectrum and named-profile Bellman/admission engine; hashes in SOURCE_PINS',
'actual_Boolean_family':'Fplus=J(-1,+1,g,g,g,g), six-bit g negative {0,1,2}; h negative {0,1,2,4,8,16,32,6,17,40}; J=-h(x xor1)',
'parameter_domain':'Every restriction of all four fixed six-bit cores; twelve dummy-deleted profiles/core; every adaptive physical query, stop, and sequential admission of distinct cores using exact hull allocator of admitted set',
'case_count':'12^4=20736 labelled full profiles; 6084 block-symmetry orbits. All 15 nonempty admitted masks; at most 28560 labelled hull states; 144+1728+6912=8784 admission cuts',
'symmetry':'Literal block swaps axes0<->2 and1<->3, each checked on all16 outer inputs; admitted masks transformed with profiles; credit histories remain labelled and are never averaged',
'arithmetic':'Fraction prime-log forms; exact cancellation before directed192-bit log sign; atanh80 remainder; no floating verdict',
'pilot':'one two-core mask,144 labelled states, independent spectra compared with pinned centered engine; <=55s',
'memory_estimate_mb':240,'memory_stop_private_mb':280,'maximum_runtime_seconds':1500,
'search_scope':'Fixed dimension24 only; no automatic dimension increase. Both outcomes retained; original stopped donor and old owner labels unchanged. Actual carried credit, never reset at admission.',
'source_review':'Compare all3456 A075 triple state instances and source phase cuts using independently rebuilt spectra and Bellman/credit recursion',
'output_limits':'Chunk at most128 profile certificates/file; files below20MB; no detached job'}
(R/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'frozen':True,'source':str(S),'run':str(R)}))
