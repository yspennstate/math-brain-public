from pathlib import Path
import json, hashlib, datetime, re

RUN=Path(__file__).resolve().parents[1]
OWN=RUN.parents[1]
BASE=OWN/'runs/20261014T061720Z-account05-A099-candidate-assembly'
ROOT=Path('~/brain_workers/FEI100_20261011')
REPO=Path('~/mop_fei100')
SOURCE=ROOT/'agents/A096/runs/20261014T094929Z-account05-A096-live-gap-ledger'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()

def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

for d in ['code','out']: (RUN/d).mkdir(exist_ok=True)
protocol=json.loads((REPO/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
save(RUN/'out/FROZEN_SPEC.json',{
 'helper_version':'A099-direct-characters-prime-log-v1',
 'family':'All labeled Boolean truth tables n=1,2,3; fixed 3-bit point defect; all 16 two-bit terminals',
 'domain':{'n':[1,2,3],'references':['true spectrum','uniform','increasing full-support rational weights']},
 'case_count':'(4+16+256)*3=828 root/reference pairs, 2412 labeled one-bit queries, 828 adaptive histories; 32 tensor cases',
 'symmetry':'none','arithmetic':'Fraction probabilities; exact prime-log vectors; Gibbs sign analytic',
 'memory_estimate_MB':80,'max_runtime_seconds':55,'pilot':'n=1,2, 60 root/reference pairs; under 60 s',
 'no_automatic_dimension_escalation':True,'saved_at':NOW})
base=(BASE/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8')
addition=(RUN/'STAGE6_ADDITIONS.tex').read_text(encoding='utf-8')
text=base.replace('14 October 2026; assembly version 5','21 October 2026; assembly version 6')
text=text.replace('\\section{Dependencies, review and sources}',addition+'\n\\section{Dependencies, review and sources}')
text=text.replace('Historical C024 is kept separate from the',
 'A paid incoming complete reference now continues through every finite\n'
 'adaptive no-reset history at its original ancestor rate. Prescribed\n'
 'fresh-reference resets remain a separate signed account.\nHistorical C024 is kept separate from the')
(RUN/'CANDIDATE_MANUSCRIPT.tex').write_text(text,encoding='utf-8')

# Source-bound intake. Decode source bytes explicitly; four pdftotext files are cp1252.
paths=[REPO/'reports/fei-2026-10-11'/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=REPO/'research_pushes/2026-10-11-full-fei-100-agents'
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))
paths += list((ROOT/'context').glob('*.txt'))
paths += [ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',OWN/'STATUS.md',BASE/'CANDIDATE_MANUSCRIPT.tex',BASE/'CLAIMS.json',BASE/'out/PROOF_DEPENDENCIES.json',SOURCE/'REPORT.md',SOURCE/'DERIVATION.md',SOURCE/'CLAIMS.json']
for agent in ['A094','A095','A086','A081']:
    available=[r for r in (ROOT/'agents'/agent/'runs').iterdir() if (r/'REPORT.md').exists()]
    r=max(available)
    paths += [r/'REPORT.md',r/'CLAIMS.json']
    paths += [p for p in [r/'AUDIT.md',r/'DERIVATION.md',r/'RECONSTRUCTION.md'] if p.exists()]
receipts=[]
for p in paths:
    raw=p.read_bytes()
    try: data=raw.decode('utf-8');enc='utf-8'
    except UnicodeDecodeError: data=raw.decode('cp1252');enc='cp1252 (explicit source encoding)'
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc})
save(RUN/'out/SOURCE_RECEIPTS.json',receipts)
(RUN/'out/BOARD_SNAPSHOT.md').write_bytes((ROOT/'BOARD.md').read_bytes())

claims=json.loads((BASE/'CLAIMS.json').read_text(encoding='utf-8'))
fresh=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8'))
for c in fresh:
    c['review_records'].append({'reviewer':'A099','verdict':'RECONSTRUCTED_PENDING_EXECUTED_VALIDATION',
     'source':str(RUN/'STAGE6_ADDITIONS.tex'),'scope':'Exact original statement, including priced A097 application and independent terminal; no integrated-chain acceptance',
     'independent_method':'Direct character sums and prime-log identities; analytic conditional KL; full finite-tree cancellation',
     'statement_sha256':c['statement_sha256']})
    claims.append(c)
save(RUN/'CLAIMS.json',claims)
dag=json.loads((BASE/'out/PROOF_DEPENDENCIES.json').read_text(encoding='utf-8'))
for c in fresh:
    dag['nodes'].append({'claim_id':c['claim_id'],'version':c['version'],
      'proof_dependencies':[d['claim_id'] for d in c['proof_dependencies']],
      'statement_sha256':c['statement_sha256'],'tex_label':'sec:conservative',
      'review_scope':'A099 independent reconstruction; validation pending; integrated chain open'})
save(RUN/'out/PROOF_DEPENDENCIES.json',dag)
progress={k:v for k,v in json.loads((BASE/'PROGRESS.json').read_text(encoding='utf-8')).items()}
progress.update(run_id=RUN.name,attempt_id='A099-assembly-v6',method='Single-source conservative continuation and explicit signed reset ledger; independent A096 reconstruction',
 mathematical_delta='Paid complete reference continues through every finite adaptive no-reset history; actual constant-child inherited-cost obstruction retained; signed reset test Z<=U+r explicit. Full FEI OPEN.',
 deliverable_status='SAVED_VALIDATION_PENDING',mathematical_status='SCOPED_RECONSTRUCTION_UNIVERSAL_RESET_OPEN',
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1,'change':'Original statement preserved; independent A099 review added after validation'} for c in fresh],
 source_artifacts=[str(RUN/'CANDIDATE_MANUSCRIPT.tex'),str(RUN/'STAGE6_ADDITIONS.tex'),str(RUN/'out/SOURCE_RECEIPTS.json')],
 next_consumers=['A097','A094','A085','A100','B20'],
 next_action='A097/A094 price prescribed weak non-flat descendant resets, channel and both complete terminals from SAME unused ancestor account; A085/A094 independently audit full source.',
 stagnant_substantive_attempts=0,blockers=['Full FEI universal source/reference payment open','Both independent integrated-chain audits pending','Remote persistence unverified'],packet_ids=['A099'])
progress['claim_versions_used'] += [{'claim_id':c['claim_id'],'version':c['version']} for c in fresh]
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
report='''# A099 candidate assembly version 6

## exact target, quantifiers, hypotheses and units

Assemble the strongest supported uniform-cube chain in one source. Every Boolean sign is finite-dimensional; entropy and complete reference costs use bits, influence is ordinary physical flip probability. Advance C019/C024 only by continuing a supplied paid reference through every finite adaptive no-reset physical tree. Full FEI and arbitrary useful reference resets remain OPEN.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full; current board dated 2026-10-21 15:51 UTC, own prior status, B20 notes v2 and v5 assembly consumed. Required campaign ledgers, plan, supplemental sources and four paper texts are byte-pinned in out/SOURCE_RECEIPTS.json. The four pdftotext files require explicit cp1252 decoding; the failed initial UTF-8 read is not source corruption. Paper results remain context, not universal proof premises. New critical source: A096 run 20261014T094929Z, DERIVATION Sections 1--4 and both original CLAIMS; A094 complete floor/child-price challenge and A086 independent reconstruction consumed. A095 cumulative-admission theorem is intake only, not silently accepted or used. Later run directories containing only .final markers supply no new mathematics and are not substituted for source-complete reports. Earlier v5 complete source and scoped reviews remain unchanged.

## complete derivation or exact first unsupported line

CANDIDATE_MANUSCRIPT.tex contains all prior lemmas and four explicitly open universal conjectures, followed by complete no-reset transport and signed reset accounting proofs. For p_tb and q_tb, m_t=sum_b p_tb and v_t=sum_b q_tb. Actual signed physical children average to m; both carry v. Exactly CE(P,Q)=B_j+mean CE(children,v)+R_j, with R_j conditional occupancy KL >=0. Finite adaptive telescoping retains all reference-only mass and every full terminal H+D. Applying the already paid A097 floor yields unchanged rate 2C0+10 (18 structurally), with arbitrary independent terminal CE additive. This is conservative ancestor payment, not individual child influence payment. The three-bit matching-reference fixture has a constant child at I=0 with inherited CE=log2(8/5)>0.

With ancestor quota A, executed debit d, original stopped cost T, U=A-d-T, subsequent erasures b, conditional refunds r and signed terminal-reference reset Z, the exact final balance is U+r-Z. Thus this specified account admits the reset exactly when Z<=U+r. Channel terms or label costs must be charged separately if required. This algebra exposes rather than solves the first unsupported line: construct useful references/history/reset choices for arbitrary Boolean sources, with an absolute initial influence price and every retained terminal and required debit paid by the SAME account. No finite tests or bookkeeping identity proves that existence. Historical C024 remains distinct from this finite-tree interface.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes the search. The independent checker uses direct character sums, exact Fraction probabilities and prime-log vectors, no author checker. Pilot and full commands: python -X utf8 code/check_transport.py --pilot; python -X utf8 code/check_transport.py. Planned full domain: all 276 labeled signs in dimensions 1--3, three references each, every labeled one-bit query and one outcome-adaptive stopped tree per root/reference, plus the exact constant-child and complete arbitrary two-bit terminal tensor checks. Status at initial checkpoint: validation pending. Finite identities do not establish the all-dimensional KL sign; that sign is proved by log x<=x-1 with zero-fiber support checked where used. No GPU, automatic dimension escalation or heavy search. Memory estimate 80 MB, mathematical job cap 55 seconds. No Mathlib build is authorized by the 1.5GB job limit; a bounded core-Lean bookkeeping check may be used with explicit scope.

## proof dependencies and changed downstream conclusions

The v5 DAG is preserved and extended by the two exact original A096 statements. The no-reset application uses A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 at its already audited scope; its elementary chain rule is rederived completely. Both independent integrated-chain audits remain open. No universal constant improves. A096 source status is not changed in its own tree. The local review adds A099 only after successful independent validation. A094/A086 incoming-child obstruction supports the continuing prohibition on renewing a child bank; it does not refute FEI.

## one next mathematical action and independent reviewer

A097/A094 should specify one weak non-flat active descendant reset relative to its actual incoming reference, retain the complementary full terminal, channel cost and old debit, and prove Z plus the other new costs fits the SAME measured unused account plus actual refunds. A085/A094 independently audit the full assembled dependency chain; no scoped acceptance substitutes for either integrated audit.

## actual persistence receipts or precise save blocker

All four protocol files and the single-source TeX are saved locally in the assigned run, with code, frozen specification and source receipts. Final validation, artifact hashes and rolling-file updates follow in code/finalize.py. No shared campaign source, other agent folder, git state or trading path is modified. Supervisor copy, canonical adoption and remote mirrors remain unverified. Session wake warned that personal context notes were stale, and the user was alerted before reliance. A requested read-only brain recall unexpectedly reported an automatically detached BM25 refresh; no such helper was intentionally launched by A099, and no other process was stopped.

## Universal bridge

C019 stopping payment and the finite-tree C024 transfer interface advance from one paid supplied-source floor to every finite adaptive no-reset history at unchanged rate, with all full terminals retained. The exact reset debit Z and remaining account U+r now state the unpaid admission without a fresh child bank. Improvement to the universal FEI constant is zero: a cheap reference for every Boolean source and complete useful reset/channel payment remain unproved, and both integrated audits are pending. NEXT targets that same-account weak non-flat reset because conservative marginalization is automatic and further root or shallow-history certificates would repeat already paid work.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A099 v6 source/checkpoint saved; all-depth no-reset complete-reference continuation reconstructed; exact reset ledger explicit; validation pending; FEI OPEN.\nNEXT: Validate independent checker; A097/A094 pay prescribed weak non-flat reset plus channel and both full terminals from SAME unused ancestor account; A085/A094 integrated audits.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+NOW+': v6 checkpoint saved; source-complete A096 no-reset chain consumed and independently reconstructed; exact signed reset account added. No-reset inheritance distinguished from unpaid cheap-source/reset existence.\n')
print(json.dumps({'saved':True,'sources':len(receipts),'claims':len(claims),'manuscript_bytes':len(text.encode('utf-8'))}))
