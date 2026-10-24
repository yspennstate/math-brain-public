from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];p=R/'code/fixtures.py';s=p.read_text()
(R/'code/fixtures_pilot_v1.py').write_text(s,encoding='utf-8')
(R/'out/EXECUTION_CORRECTIONS.json').write_text(json.dumps({'fixture_pilot':'50-second runtime cutoff, no mathematical assertion failure; now split same frozen domain into8 sequential phase jobs','classification_verifier':'Initial comparison omitted character parity-group swap. Corrected verifier checks all12 raw profiles against8 canonical profiles and their exact mirrored forms. No continuum bound changed.','fixture_pilot_code_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2),encoding='utf-8')
s=s.replace('import arithmetic as ar','import arithmetic as ar\nimport sys\nidx=int(sys.argv[1]);assert 0<=idx<8').replace('for profile in profiles:','for profile in [profiles[idx]]:').replace("RUN/'out/FIXTURE_RESULTS.json'","RUN/f'out/FIXTURE_{idx}.json'")
s=s.replace("res={'status':'PASS'","res={'status':'PASS','profile_index':idx")
p.write_text(s,encoding='utf-8')
spec=json.loads((R/'out/FROZEN_VERIFY.json').read_text());spec['fixture_partition']='Same2048 parents/6144 references; eight sequential phase jobs,256 parents and768 references each; maximum50seconds/job. Cover metadata128 parents,1536 singleton restrictions in aggregate.'
spec['fixture_helper_version']='A013-two-row-fixtures-v2'
(R/'out/FROZEN_VERIFY.json').write_text(json.dumps(spec,indent=2),encoding='utf-8');print('same-domain sequential fixture partition frozen')
