from pathlib import Path
import hashlib,json,datetime
run=Path(__file__).resolve().parents[1];agent=run.parents[1];root=agent.parents[1]
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def receipt(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
contract=json.loads(protocol.read_text(encoding='utf-8-sig'))
claimid='A049-MINIMAL-CONTRACTED-CORE-DATA-RESERVE-AUDIT'
statement='For every Boolean seed g with alpha=Pr(g=-1)>0, F=y*(1+a*(1-z)*(g-1)) on independent uniform bits, queried at physical core bit a with identical inactive labels contracted, has d=alpha/2, labelled release kappa=1/2 and the seed-shape-independent exact entropy decrement D(alpha) displayed in REPORT.md. The common parity boosts the release by (1-alpha^2)/2 and shifts the signed residual oppositely while preserving the true entropy ledger. Kappa/d is unbounded on all-essential point seeds. Within this declared effective-dimension family, six variables is minimal both for D-kappa<0 and for kappa>4d. The parameter-free six-bit point-seed witness has I=21/16, mean terminal I=5/4, d=1/16, 9/32<D<5/16, negative residual<-3/16, and complete exact normalized joint-reference KL/terminal certificates, including a once-only finite K4 child-surplus payment. No arbitrary-tree minimality or universal FEI result is asserted.'
hypotheses=['Uniform independent cube, Boolean signs, base-two entropy and KL, actual Fourier-square laws.', 'Construction and minimum restricted to F=y*(1+a*(1-z)*(g-1)), t effective seed bits plus fresh a,z,y, query a then stop.', 'Exclusive root labels choose y/yh; contract identical inactive cores only, retain opposite/distinct cores.', 'Finite reference certificate uses uniform core frequencies times deterministic common-parity law, actual physical Bayes transport and the fresh references specified in REPORT.md; no arbitrary-reference price.']
claim=dict(claim_id=claimid,version=1,exact_statement=statement,hypotheses=hypotheses,
 statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A049'],
 proof_source='REPORT.md; code/check.py; code/reproduce.py; out/WITNESS.json; out/REPRODUCTION.json',proof_dependencies=[],review_records=[],
 status='PROVED_LOCALLY_REVIEW_PENDING',supersedes=[],refutes=['Exploratory shared-core positive labelled-release rate-four payment at a core-data query; no named scoped theorem'],first_unproved_line=None,next_consumers=['A048','A050','A092','A038','A039','B20'])
progress=dict(protocol_revision=contract['revision'],run_id=run.name,stream='B10',packet_id='A049',gap_id='C019-CORE-DATA-SIGNED-RESERVE-PAYMENT',attempt_id='A049-stage4-contracted-core-data-reveal',
 method='Frozen all278 small seeds, scalar seed-spectrum cancellation, six-bit exact circuit and signed integer certificate, independent normalized nonmatching reference transport',
 mathematical_delta='Effective six-bit minimum in declared family; signed residual negative after essential data reveal, labelled release/d=8 and unbounded point-family growth; full seed-independent scalar decrement; source/erasure/outcome/terminal/reset KL retained; finite actual and full-reference K4 surplus owner checked once.',
 deliverable_status='COMPLETE_LOCALLY_SAVED',mathematical_status='SCOPED_EXTRACTION_AND_FINITE_ACCOUNT_CHECKED; REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A048-COMMON-FACTOR-LABEL-RESERVE-OBSTRUCTION@1','A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1'],claims_created_or_changed=[claimid+'@1'],
 source_artifacts=['REPORT.md','out/FROZEN_SPEC.json','out/REFERENCE_SPEC.json','out/FULL_CHECK.json','out/WITNESS.json','out/REPRODUCTION.json','out/truth_table.txt','out/VALIDATION_REPAIR.md','out/SOURCE_RECEIPTS.json'],
 next_consumers=['A048','A050','A092','A038','A039','B20'],
 next_action='At A092 exposed opposite-priority gate, carry actual conditional likelihood and erasure into the prescribed occupancy reference, naming one unused child bank and preserving reference-only rows and both complete terminals.',
 stagnant_substantive_attempts=0,blockers=['Universal prescribed-reference conditional source/child surplus remains unproved; independent review, canonical adoption and remote mirrors pending.'],packet_ids=['A049'])
dump(run/'CLAIMS.json',[claim]);dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)
base=Path(r'~\brain_workers\FEI100_20261011')
sources=[protocol,base/'BOARD.md',base/'claude'/'B10'/'STREAM_NOTES.md',
 base/'agents'/'A048'/'runs'/'20261014T022727Z-fleet05-A048-tensor-stress'/'PROOF.md',
 base/'agents'/'A048'/'runs'/'20261014T052201Z-fleet05-A048-tensor-stress'/'PROOF.md',
 base/'agents'/'A048'/'runs'/'20261014T052201Z-fleet05-A048-tensor-stress'/'REPORT.md',
 base/'agents'/'A050'/'runs'/'20261014T033613Z-fleet05-A050-repair-with-scope'/'PROOF.md',
 base/'agents'/'A047'/'runs'/'20261014T044331Z-fleet05-A047-boundary-search'/'REPORT.md',
 base/'agents'/'A092'/'runs'/'20261014T045641Z-fleet05-A092-counterexample-referee'/'PROOF.md']
dump(run/'out'/'SOURCE_RECEIPTS.json',[receipt(p) for p in sources])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A049 stage4 complete: six-bit minimum in contracted core-data family; signed residual <-3/16, release/d=8, true rate4 excess retained; 11,566 main/reproduction checks PASS; full reference/terminal owner verified; review pending; FEI OPEN.\nNEXT: A048/A050/A092 review; at exposed opposite-priority gate transfer actual likelihood/erasure to prescribed occupancy reference, name one unused child bank, and retain reference-only rows and both terminal bills.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+stamp+' | '+run.name+' | Read updated board/B10 and A048/A050/A047/A092 scope audits. Minimized A048 common-parity reserve failure through an actual core-data query and duplicate-label contraction: six-bit F=y*(1-2*1_{a=1,z=0,w=000}), d=1/16, kappa=1/2, 9/32<D<5/16. Initial pilot rejected an overly tight D upper bound; correction and exact integer sandwich saved. Final pilot 7/199 PASS0.0312s; full278/11468 PASS0.7471s; separate scalar/character/reference reconstruction98 PASS0.0267s. Seed shape cancels, all t<=2 profiles positive, six minimum; fixed nonmatching normalized reference retained E/O/terminal/reset and checked full finite K4 owner. No broad FEI claim, no external writes/reviews/mirrors.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n'+stamp+' | Core-data common-factor audit: for F=y*(1+a*(1-z)*(g-1)), alpha=Pr(g=-1)>0, contracted inactive duplicate labels give kappa=1/2, d=alpha/2; before parity kappa=alpha^2/2. Actual D is invariant and depends only on alpha: phi((1-alpha/2)^2)+3phi(alpha^2/4)-phi((1-alpha)^2)/2-phi(alpha^2)/2+2alpha(1-alpha). All four nonzero t<=2 minority profiles have D>1/2. Six-bit point seed alpha1/8 has 9/32<D<5/16 by2^600*7^98<15^225<2^604*7^98, residual<-3/16, and true K4 excess>1/32, which cannot be discarded when cancelling inflated labels. Complete full-reference example: uniform32 root, inherited branch predictions4/113,109/113, active Q heavy49/1744 and others113/1744; signed E/O/child/reset sum retains initial KL. Fresh terminal CE mean2, root CE5; mean full-terminal K4 surplus3 pays excess11/4 once, leaves1/4. Entropy-only active-core surplus and full-reference surplus are ALTERNATIVE ledgers, never two jointly spendable banks. Scalar-family effective minimum6 is not arbitrary-tree/global minimality.\n')
expected_progress=[x.split(' (')[0] for x in contract['required_per_run']['progress_fields']]
assert set(progress)==set(expected_progress)
assert set(claim)==set(contract['required_per_run']['claim_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+field in report for field in contract['required_per_run']['report_fields'])
assert report.rsplit('\n\n',1)[-1].startswith('**Universal bridge:**')
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
full=json.loads((run/'out'/'FULL_CHECK.json').read_text());repro=json.loads((run/'out'/'REPRODUCTION.json').read_text())
assert full['cases']==278 and full['assertions']+repro['assertions']==11566
files=[p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']+[agent/p for p in ('STATUS.md','WORKLOG.md','LEARNED.md')]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(run/'out'/'PERSISTENCE.json',dict(saved_at_utc=stamp,files=[receipt(p) for p in files],schema_checks='PASS',delta_equality='PASS',status_lines=2,report_fields='PASS',local_only=True,external_review='pending',mirror_verification='unverified'))
print(json.dumps(dict(saved_files=len(files)+1,protocol_fields='PASS',maximum_file_bytes=max(p.stat().st_size for p in files),main_plus_reproduction_assertions=11566),indent=2))
