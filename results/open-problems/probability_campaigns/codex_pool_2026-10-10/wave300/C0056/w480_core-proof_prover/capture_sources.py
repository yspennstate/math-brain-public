"""Capture only the named C0056 records, cited public sources and exact store cards."""
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'sources'
SOURCE.mkdir(exist_ok=True)
INTAKE = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
receipts = []
records = {}
for filename, field, wanted in [('problems.jsonl','problem_id','C0056'), ('attempts.jsonl','problem_id','C0056'), ('sources.jsonl','source_id','bourgade_band_icm_2018')]:
    matches = []
    with (INTAKE / filename).open(encoding='utf-8') as handle:
        for number, line in enumerate(handle, 1):
            if wanted not in line:
                continue
            row = json.loads(line)
            if row.get(field) == wanted:
                matches.append({'line':number,'record':row,'raw_line_sha256':hashlib.sha256(line.encode('utf-8')).hexdigest()})
    records[filename] = matches
    receipts.append({'path':str(INTAKE / filename),'matching_records':len(matches),'hash_scope':'matching raw line only; provenance receipt, not a proof'})
(SOURCE / 'intake_c0056_records.json').write_text(json.dumps(records, indent=2)+'\n', encoding='utf-8')

urls = [
    ('bourgade_1807.03031.pdf', 'https://arxiv.org/pdf/1807.03031'),
    ('recent_claim_01-introduction.tex', 'https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex'),
]
for filename, url in urls:
    dest = SOURCE / filename
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read(3000000)
            assert not response.read(1), 'Public-source size gate exceeded'
            final_url = response.url
        dest.write_bytes(data)
        receipts.append({'url':url,'final_url':final_url,'path':str(dest),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':'fetched','mathematical_proof_checked':False})
    except Exception as error:
        receipts.append({'url':url,'status':'unavailable','error':str(error),'mathematical_proof_checked':False})

export = Path('~/math-brain-build/export/population/nodes.jsonl')
cards = []
with export.open(encoding='utf-8') as handle:
    for number, line in enumerate(handle, 1):
        if 'c0056' not in line.lower():
            continue
        row = json.loads(line)
        meta = json.loads(row.get('metadata_json','{}'))
        logical = meta.get('logical_id','')
        if 'c0056' in logical:
            cards.append({'line':number,'id':row['id'],'logical_id':logical,'body':row['body'],'digest_as_recorded':row.get('digest'),'truth_status':meta.get('truth_status'),'claim_kind':meta.get('claim_kind')})
(SOURCE / 'store_c0056_cards.json').write_text(json.dumps(cards, indent=2)+'\n', encoding='utf-8')
(SOURCE / 'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts, indent=2)+'\n', encoding='utf-8')

status = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status.update({
    'exact_original_statement': records['problems.jsonl'][0]['record']['statement'],
    'primary_source': {
        'author':'Paul Bourgade','title':'Random band matrices','url':'https://arxiv.org/pdf/1807.03031','locator':'Section 2.1, printed page 7; page index 6',
        'model':'H=Delta+alpha*V; iid centered potentials of variance 1; discrete hopping spectrum [-2d,2d].',
        'finite_volume':'Periodic boundary conditions on the N-side box; microscopic energy scale N^d. Source does not fully formalize a fixed-energy GOE theorem.',
        'short_quote':'there is no clear understanding about how extended states imply GOE spectral statistics',
        'source_status_date':'2018 (historical status only)',
    },
    'working_statement': 'Uniform-law spectral subtarget: H_lambda=-A+lambda*U on l2(Z^3), iid U uniform[-1,1], fixed lambda>0 before eta->0. Seek nonzero purely absolutely continuous spectral restriction to a deterministic open interval for all fixed sufficiently small lambda.',
    'normalization_bridge': 'The source variance-one uniform law is V=sqrt(3)*U; alpha=lambda/sqrt(3). Hopping sign is reversed by the bipartite gauge on Z^3; a Laplacian diagonal constant translates energies.',
    'full_target_components': {'spectral_component':'conditional reduction prepared; LG unproved', 'GOE_component':'not solved or reduced by this lane'},
    'recent_primary_claim': {'date':'2026-09-23','url':urls[1][1],'law':'iid uniform[-1,1]','scope':'Claims nonzero pure a.c. spectrum on a fixed interval for each fixed d>=3 at sufficiently small fixed coupling; no GOE conclusion in the main theorem.','independent_proof_audit':'not performed'},
    'current_openness':'UNKNOWN',
    'prior_attempts':[r['record']['attempt_id'] for r in records['attempts.jsonl']],
    'owner_solved_retired_check':'Exact C0056 intake and export cards were inspected; both retain unverified/attempted-unsolved status. No exhaustive owner-archive certification or current solved-status certification is claimed.',
    'canonical_store_check':'Exact export cards checked; canonical live math-research-brain store has not yet been queried.',
    'receipts_path':str(SOURCE / 'SOURCE_RECEIPTS.json'),
    'review_state':'packet_preparing; independent verdict pending',
    'bundle_state':{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False},
    'formal_check_receipt':None,
    'integration_not_run':'The current task prohibits unreviewed live-store changes; a concept-only draft is prepared for the validating coordinator.',
})
(ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(status, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'exact_records':{k:len(v) for k,v in records.items()},'public_receipts':receipts[-2:],'exact_store_cards':len(cards)}))
