from pathlib import Path
import json,hashlib,datetime
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
RUN=ROOT.name
read=lambda name:json.loads((ROOT/'out'/name).read_text(encoding='utf-8'))
primary=read('SIGNED_PAYMENT_TESTS.json');follow=read('selector_followup.json');ind=read('independent_tribes_selector.json')
records=[json.loads(line) for line in (ROOT/'out'/'payment_records.jsonl').read_text(encoding='utf-8').splitlines()]
for r in list(records):
 if r['family']=='point_defect':
  for copies in range(2,17):
   records.append(dict(family='point_defect_tensor',base_point_defect_n=r['n'],copies=copies,n=r['n']*copies,certificate='H,Hinf,gap,I each multiply by copies; ratios identical',ratios_H_Hinf_gap=r['ratios_H_Hinf_gap'],gap_le_4I=r['gap_le_4I'],Hinf_le_2I=r['Hinf_le_2I']))
assert len(records)==primary['case_count']==797
for r in records:
 if r['family']!='point_defect_tensor' and not r['Hinf_le_2I']:
  assert Q(r['Hinf'][0])>2*Q(r['I'])
for r in follow['records']:
 for t in range(1,17):assert t*Q(r['H'][1])<=4*(t*Q(r['I'])+2)
(ROOT/'out'/'complete_payment_records.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
def claim(cid,statement,proof,refutes):
 return dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=['Uniform independent cube inputs; Boolean outputs +-1, except explicitly labelled normalized non-Boolean controls; logarithms base two.'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A035'],proof_source=proof,proof_dependencies=['Elementary Fourier factorization, Parseval and physical boundary identities; threshold_paper_38pp §8.4 Proposition 8.9 as contextual exact identity, explicitly rederived.'],review_records=[],status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=refutes,first_unproved_line=None,next_consumers=['B07 lead','A031','A033','A088','A094','B20'])
claims=[claim('A035-MINENTROPY-CONSTANT-DIAGNOSTICS',
 'For the explicitly specified 797 Boolean cases, H-Hinf<=4I is certified by rational log intervals; Hinf<=2I fails in three tribes cases. In particular h_{2,3} has I=27/16 and Hinf=10-4log2(3)>2I. The actual 514-bit Boolean F=(1+z)/2+(1-z)y product(j=1..32)h_{2,8}(x_j)/2 has I=2315/128, Hinf=2 and H-Hinf-4I>1.631488620635. These refute only helper constants 2 and 4, not universal finiteness or FEI. The largest certified Hinf/I in the specified primary family is (512/1029)(22-2log2(353))>2.524150672274, at h_{3,4}.',
 ['CANCELLATION_FAILURE.tex','out/complete_payment_records.json','out/SIGNED_PAYMENT_TESTS.json','out/independent_tribes_selector.json','code/payment_test.py','code/independent_tribes_selector.py'],
 ['Proposed Hinf<=2I on all Boolean functions','Proposed H-Hinf<=4I on all Boolean functions']),
 claim('A035-SIGNED-AND-GAP-SCOPE-AUDIT',
 'For every even n quadratic bent sign, every nonzero signed Fourier autocorrelation is zero and every unsigned autocorrelation is one; its total unsigned cost is 2^n-1, and I=n/2, so total unsigned cost cannot be universally paid by KI. Separately, sup_boolean (H-Hinf)/I = sup_boolean H/I (extended real values): for arbitrary Boolean h and integer t>=1 the balanced-core selector F built from y*h^tensor(t) satisfies H(F)-Hinf(F)=tH(h)/2 and I(F)=1+tI(h)/2. Normalized dyadic non-Boolean phi_t=3/4+(1/(4*2^t))sum(i=1..7*4^t)x_i has gap/I=2t+log2(9) and violates the singleton signed Booleanity identity; flat psi_n has Hinf/I=log2(n) but gap zero.',
 ['CANCELLATION_FAILURE.tex','out/SIGNED_PAYMENT_TESTS.json','out/selector_followup.json'],
 ['Unsigned total Fourier autocorrelation<=KI universally for Boolean functions','An estimate for H-Hinf is an easier universal conjecture than full FEI'])]
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2),encoding='utf-8')
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN,stream='B07',packet_id='A035',gap_id='G-BOOLEANITY',attempt_id='A035-signed-payment-1',method='Frozen exact Boolean Walsh/edge search, rational log intervals, independent factored spectrum certificate, selector/tensor scope audit',mathematical_delta='Refuted helper constants Hinf<=2I and H-Hinf<=4I by actual Boolean witnesses; proved min-gap universal constant equals FEI constant; isolated unsigned sign-loss exponential obstruction. No dimension-independent payment proved.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_REFUTATIONS_AND_SCOPE_REDUCTION; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',claim_versions_used=['threshold_paper_38pp §8.4 Proposition 8.9, local SHA in out/source_manifest.json; rederived, not imported as unreviewed campaign claim','B07 STREAM_NOTES.md v1, 2026-10-11 22:40 UTC, instructions only'],claims_created_or_changed=[c['claim_id']+' v1' for c in claims],source_artifacts=['REPORT.md','CLAIMS.json','CANCELLATION_FAILURE.tex','FROZEN_SPEC.json','FOLLOWUP_SPEC.json','TRIBES_SELECTOR_SPEC.json','out/SIGNED_PAYMENT_TESTS.json','out/independent_tribes_selector.json','out/selector_followup.json','out/source_manifest.json'],next_consumers=['B07 lead','A031','A033','A088','A094','B20'],next_action='A088/A094 reconstruct the exact witnesses and selector scope; test a source-complete F^4=1 coordinate erasure payment from A031, retaining signed convolution and full remaining entropy, instead of enlarging the min-gap finite census.',stagnant_substantive_attempts=0,blockers=['No universal signed influence payment supplied; review and supervisor mirroring pending.','31-formula followup exceeded frozen 60-second estimate: measured 164.55 seconds, below campaign 30-minute job limit; retained as execution deviation.'],packet_ids=['A035'])
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
fields=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
expected_progress=[x.split(' (')[0] for x in fields['progress_fields']]
assert set(progress)==set(expected_progress)
assert all(set(c)==set(fields['claim_fields']) for c in claims)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'primary_cases':len(records),'primary_checks':primary['exact_checks'],'formula_seeds':follow['seed_count'],'formula_selectors':follow['selector_count'],'schema_exact':True,'new_claims':len(claims)}))
