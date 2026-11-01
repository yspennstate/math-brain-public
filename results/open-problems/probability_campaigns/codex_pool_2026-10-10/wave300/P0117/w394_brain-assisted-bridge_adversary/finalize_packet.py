"""Validate local artifacts, stage the explicitly authorized draft, and save receipts."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import sqlite3

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w394')
PUBLIC='https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf'
def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def append(path,obj):
    with path.open('a',encoding='utf-8') as f:f.write(json.dumps(obj,ensure_ascii=False)+'\n')

bundle=json.loads((ROOT/'drafts/bundle_001.json').read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys={e['key'] for e in bundle['entries']}
assert len(keys)==len(bundle['entries'])<=200
for e in bundle['entries']:
    assert required<=e.keys() and e['kind']=='concept' and e['proof_text'] is None
    assert 'DRAFT' in e['statement'] and e['source']['license'].startswith('owner-own-work')
for r in bundle['relations']:
    assert r['from_key'] in keys and r['kind'] in allowed
    assert ('to_key' in r)!=('to_existing_logical' in r)
    if 'to_key' in r:assert r['to_key'] in keys
    assert r['rationale'].strip()
assert not any(r['kind']=='depends_on' for r in bundle['relations']) # hence no dependency cycle

db=Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True,timeout=2) as con:
    con.execute('PRAGMA query_only=ON')
    target=con.execute("SELECT id,title,body,metadata_json FROM nodes WHERE id=?",('claim_00e83dbdd81c6433d9909a1b375c4e0a688bea718951c1d68fe8ffcd72b1bcf1',)).fetchone()
    assert target and json.loads(target[3])['logical_id']=='math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp'
    live_existing=sum(con.execute('SELECT count(*) FROM nodes WHERE metadata_json LIKE ?',('%'+e['logical_name']+'%',)).fetchone()[0]>0 for e in bundle['entries'])

by_key={e['key']:e for e in bundle['entries']}
edge_rows=ROOT/'EDGE_ROWS.jsonl'
with edge_rows.open('w',encoding='utf-8') as out:
    for i,r in enumerate(bundle['relations'],1):
        a=by_key[r['from_key']]
        b=by_key[r['to_key']] if 'to_key' in r else dict(key=r['to_existing_logical'],statement=target[2])
        out.write(json.dumps(dict(row_id=f'w394.P0117.edge.{i:02}',kind=r['kind'],from_key=a['key'],to_key=b['key'],
          from_quote=a['statement'],to_quote=b['statement'],rationale=r['rationale'],status='draft',independent_reviewer='w395 (pending)'),ensure_ascii=False)+'\n')

partition=[]
for k in [2,4,8,16,32,64,128]:
    fixed_log=8*math.log1p(-1/k)
    growing_log=2*k*k*math.log1p(-1/k)
    partition.append(dict(k=k,fixed_N=4,fixed_retention=math.exp(fixed_log),growing_N=k*k,
                          growing_retention=math.exp(growing_log),growing_log_retention=growing_log))
save(ROOT/'verification/partition_counterexample.json',dict(statement='Independent uniform labels: retention=(1-1/k)^(2N); fixed N works, N=k^2 fails.',
     method='Exact probability formula derived in PARTITION_CHECK.md; table is a finite numerical illustration, not a limit proof.',rows=partition))

claims_path=ROOT/'CLAIMS.jsonl'
existing_ids={json.loads(line)['claim_id'] for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()}
for c in [
 dict(claim_id='w394.P0117.C05',exact_statement='Two finite strictly positive completions of the same B_1 weights have different globally minimizing S_1-through-origin events; the box-minimizer event is unchanged.',assumptions=['Nearest-neighbor Z^2','Inside B_1 edge weights 1','First completion constant 1; second S_2 perimeter/connectors 1/20, remaining weights 1'],source={'type':'owner-own-work','path':'verification/filtration_counterexample.json'},proof_or_counterexample='Every S_1 pair has an outside bypass costing <=1/2 in the second completion, while every simple through-origin path costs >=2. Integer-weight Dijkstra checked all 28 pairs: global hit counts 16 versus 0; box counts 16 versus 16.',independent_reviewer='w395 (pending)',remaining_gap='Independent mathematical check pending; no iid-FPP counterexample is claimed.',status='sketch'),
 dict(claim_id='w394.P0117.C06',exact_statement='For each fixed M and finite partition-independent neighborhood, distinct marked labels give eventual retention under vanishing bin diameter and hence probability convergence. Partition-dependent neighborhoods need not give it.',assumptions=['Measurable mark indicators and labels','For fixed M a deterministic finite neighborhood independent of partition index','Distinct labels on marked pairs almost surely','Deterministic partitions with maximal bin diameter tending to zero'],source={'type':'owner-own-work','path':'PARTITION_CHECK.md'},proof_or_counterexample='Finitely many distinct neighbors are eventually in different bins; take the maximum separating index and apply bounded convergence. For iid uniform labels, a k-bin partition retains probability (1-1/k)^(2N); N=k^2 makes it tend to zero despite pairwise distinct labels.',independent_reviewer='w395 (pending)',remaining_gap='The cited preprint explicitly states the fixed-neighborhood premise; its upstream uniform-comparison and distinct-label theorems remain outside this local audit.',status='sketch')
]:
    if c['claim_id'] not in existing_ids:append(claims_path,c)

append(ROOT/'AUDIT_VERDICTS.jsonl',dict(row_id='w394.P0117.audit.partition_limit',subject=PUBLIC+' section 7.4, equations (81)-(82)',
    verdict='PASS_CONDITIONAL_LIMIT_ORDER',why='For fixed M the stated S(M) is finite and independent of partition index. Pairwise distinct marked labels give pointwise eventual retention; bounded convergence and then large M have the correct order.',
    scope='Local limit argument only; conditional on Theorems 5.1, 5.2, 7.6 and the uniform positive mark density.',auditor='w394',remaining_gap='Full upstream theorem chain is w395 referee lane; no full proof certification.'))

source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source.update(current_openness='UNKNOWN',primary_full_hypotheses_status='Exact working moment class recovered; broader moment-free question not certified solved.',
    exact_working_statement='For every atomless Borel probability law G on [0,infinity) with E[min(X1,X2,X3,X4)^2]<infinity, assign iid weights to undirected nearest-neighbor edges of Z^2. Is P_G(exists an injective doubly infinite nearest-neighbor path, every finite segment of which minimizes T between its endpoints)=0?',
    source_question_quote='Question 31. Do geodesic lines exist?',source_question_url='https://arxiv.org/pdf/1511.03262',
    source_question_locator='Current arXiv PDF p.98 (zero-based page 97), section 4.5; page number differs in other survey editions.',
    formulation_scope='The moment condition is an explicit working restriction. The ledger positive-speed phrase and source question alone do not specify it. A proof in this class is not silently promoted to a moment-free theorem.',
    new_primary_claim=dict(url=PUBLIC,date_on_document='2026-09-24',theorem='1.1',
        statement='Claims simultaneous absence of all bigeodesics for the exact working moment class, without shape regularity.',
        content_checked='Introduction and Theorem 1.1 in named referee public-source read copy; public GitHub file existence independently browsed.',
        proof_assessment='Mathematical validity unverified; one conditional section-7.4 limit-order check passed. No full solution or novelty claimed.'),
    theorem_comparison_sources=['https://arxiv.org/html/1609.02447','https://arxiv.org/html/2204.02332v5','https://arxiv.org/html/1512.00804v2'],
    full_preprint_referee='w395; independent checker of referee-originated results w398',review_state='own claims pending w395')
save(ROOT/'SOURCE_STATUS.json',source)

measure=json.loads((ROOT/'verification/retrieval_before_after.json').read_text(encoding='utf-8'))
append(ROOT/'RESULT_ROWS.jsonl',dict(row_id='w394.P0117.retrieval.001',kind='measured_retrieval_repair',before=measure['before']['warning_bearing_hits_at_5'],
     after_local_overlay=measure['after_local_in_memory_overlay']['warning_bearing_hits_at_5'],k=5,query=measure['query'],command=measure['command'],
     evidence='verification/retrieval_before_after.json',scope='One author-chosen query; same lexical/graph engine with semantic off; local overlay only.',review_state='draft'))
append(ROOT/'RESULT_ROWS.jsonl',dict(row_id='w394.P0117.source.002',kind='source_status_correction',source=PUBLIC,
     corrected_statement='A 2026-09-24 primary preprint claims the moment-qualified simultaneous theorem; dated attempted_unsolved is not current openness evidence.',
     source_locator='Theorem 1.1 and introduction',current_openness='UNKNOWN',mathematical_validity='unverified',review_state='source-checked, not mathematically certified'))

now=datetime.now(timezone.utc).isoformat()
INBOX.mkdir(parents=True,exist_ok=True) # explicitly named output exception in the task
dest=INBOX/'bundle_001.json'
text=(ROOT/'drafts/bundle_001.json').read_text(encoding='utf-8')
if dest.exists():
    assert dest.read_text(encoding='utf-8')==text, 'Do not overwrite another artifact'
else:
    part=INBOX/'bundle_001.part'
    assert not part.exists(), 'Do not overwrite a partial artifact'
    part.write_text(text,encoding='utf-8');part.rename(dest)
receipt=dict(prepared=True,submitted=dict(state=True,path=str(dest),at=now),
             reviewed=dict(state='pending',reviewer='w395; validating coordinator claude-4a88bc43'),
             ingested=dict(state='not performed by w394',live_entries_observed_before_staging=live_existing),
             retrievable=dict(local_overlay=True,live='not demonstrated'),
             entries=6,relations=5,all_entries_kind='concept',all_proof_texts=None,
             live_store_modified_by_worker=False,integrator_executed=False)
save(ROOT/'BUNDLE_RECEIPT.json',receipt)
save(ROOT/'verification/validation.json',dict(passed=True,checked='Required fields, concept-only status, license tags, exact edge ends, existing cross-link identity, no dependency edges/cycles.',
     mathematical_independent_review='pending; structural validation is not proof',command='python -X utf8 finalize_packet.py',at=now))

event=dict(event='w394 P0117: audited L1-L3/C1; adaptive-union warning hits 0/5 to 2/5 in local overlay; six concept drafts staged, full-problem validity unverified.',
           agent='w394',row='S1.P0117.w394',evidence='~/brain_workers/w394/REPORT.md',
           state='queued for reviewer; worker folder restriction permits only the named draft inbox, so no progress-page write was performed')
save(ROOT/'coordination/PROGRESS_EVENT.json',event)
report='''P0117 now has a September 24 primary preprint claiming the full moment-qualified result. I recovered the exact atomless iid minimum-of-four second-moment working statement. The broader moment-free scope and the new proof's full validity remain unverified; I claim no solution or novelty.

I saved an independent anchored-boundary reduction and adaptive-endpoint obstruction before reading w393. Direct audits keep w393 L1-L3/C1 at their stated scopes. The missing premise in that route is divergent accumulated conditional killing bounds. The cheap-ring bounds are summable. A separate narrow audit passes the new preprint's partition-limit step conditionally: its neighborhood is frozen for each M before refinement; upstream comparison and label-separation theorems remain w395's lane.

The bounded brain repair is six concept cards with exact supporting relations, keeping failed routes and assumptions visible. With python -X utf8 build_and_measure.py, the same diagnostic query over 10,650 math nodes and 15,712 edges returned zero explicit adaptive-union warnings among five hits before, and two after a local in-memory overlay. Four P0117 draft cards entered the latter top five. This is one author-chosen query, not broad effectiveness evidence. Semantic retrieval was off for both arms; the 71.329s versus 20.243s timings include cache effects and are not a speed claim. Separate guarded memory recall returned no useful P0117 top-three warning in 18.614s and reported incomplete attachments.

The exact 25-vertex integer-weight diagnostic checked all 28 boundary pairs. Changing only the outside completion changed global origin-hit pair counts from 16 to 0, while inside-box counts stayed 16. The analytic outside bypass extends this counterexample to the full lattice. This demonstrates the filtration scope error, not an iid FPP counterexample. Validation of the draft shape and exact edge ends passed with python -X utf8 finalize_packet.py; it is not mathematical proof.

The six concept cards are staged in ~/math-brain-inbox/w394/bundle_001.json. Submitted, reviewed, ingested, and retrievable states are separate in BUNDLE_RECEIPT.json. Own claims C01-C06 await w395. No integrator or live-store mutation was run. The proposed hook and progress event are staged locally because the worker's write restriction excludes those shared paths. Reviewers can post coordination/PROGRESS_EVENT.json after review. The patch headers retain the required a/live and b/live paths: apply each only to an empty destination. For the approved hook, from ~ prepare the named empty proposal file, then run git apply --check brain_workers/w394/patches/02_selector_hook.diff and git apply brain_workers/w394/patches/02_selector_hook.diff. Refuse a nonempty destination. Patch 01 reconstructs the draft using the same procedure only if its already-staged inbox copy is missing. Both patch payloads are checked by applying in the worker's scratch folder and comparing exact output text.

Risks: warnings could overfire, this query was chosen by its author, and the newly claimed theorem may retire part of the target after full independent validation. Draft concepts carry pending status and must never be promoted into verified theorems. Reproduce measurement in a fresh copy with build_and_measure.py (it deliberately refuses to overwrite a completed draft; use the saved draft for referee replay or a new worker-local output directory).

NEXT: w395 independently checks C02, C04-C06 and the cited preprint premises; the validating coordinator decides concept ingestion and audits the staged selector hook.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
print(json.dumps(dict(validation='passed',staged=str(dest),warning_hits_before=0,warning_hits_after=2,live_entries_before_staging=live_existing,review='pending'),ensure_ascii=False))
