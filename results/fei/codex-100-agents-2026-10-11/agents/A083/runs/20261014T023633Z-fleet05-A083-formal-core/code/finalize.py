from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
cid='A083-PHYSICAL-BAYES-OCCUPANCY-CORE'
statement=('For rational binary normalized laws and rational weights summing to one, their reach-weighted mixture is normalized. For rational total, group and atom with group nonzero, (group/total)*(atom/group)=atom/total; nonnegative atom and rest summing to a zero group imply atom zero. These three local statements are Lean-kernel checked. For every m>=1, on the uniform (m+4)-bit cube let Z=AND(z_1,...,z_m), g(u,v)=(-1)^(u+v), h(u,v)=1-2uv, and F_m=g if Z and a, h if Z and not a and b, else +1. The essential tree first queries u, then controllers until failure, then a and b only if a=0,u=1; it stops at nonconstant character cores. Conditional on u=0 and u=1, the physical surviving-v probabilities are p0=2^-m/2 and p1=3*2^-m/4; equal weights on their actual terminal leaves instead give q0=1/(m+2), q1=2/(m+3). The physical reach-weighted Bayes posterior is normalized and composes through every occupied prefix, with zero posterior-reference KL. The alternative marginal reference has conditional KL K_m=(D_Ber(p0||q0)+D_Ber(p1||q1))/2>1/(2(m+3)) bits for all m>=10, while I(F_m)=2^-m*(5m/8+2), so K_m/I(F_m) diverges. The family has H(F_m)<4I(F_m), expected terminal influence 5*2^-m/8 and terminal Fourier entropy zero; the terminal-inclusive signed ledger is retained exactly. The entropy, Fourier and all-m interpretation is analytic, not a Lean entropy theorem; this obstructs free or separately universal-influence-priced replacement of these two specified marginal references, not arbitrary signed reference accounting or FEI.')
hyp=['Uniform finite Boolean cubes with independent physical bits; entropy and KL in bits; ordinary total influence',
     'Fresh singleton prescribed essential tree; terminal characters remain uncomputed and their influence is retained',
     'Correct reference is the conditional physical-reach mixture of actual leaf Fourier-square laws; alternative is equal weight per distinct terminal transcript',
     'Rational normalization and occupied-prefix hypotheses as stated; unreachable zero rows are not divided',
     'Infinite extension is the explicit leaf calculation and analytic binary-KL lower bound in PROOF.md, separately checked on frozen finite domains']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A083'],
       'proof_source':{'run_id':R.name,'files':['PROOF.md','code/BayesOccupancy.lean','code/occupancy_check.py','out/LEAN_RESULT.json','out/LEAN_CHECK.txt','out/RESULT.json']},
       'proof_dependencies':[],'review_records':[],'status':'LOCAL_CORE_KERNEL_CHECKED_ANALYTIC_FAMILY_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':['Free identification of physical-reach and equal-terminal-leaf spectral mixture references after the specified shared-data exposure','An absolute bound K_m<=C I(F_m) for the two specified marginal references'],
       'first_unproved_line':None,'next_consumers':['A038','A039','A050','A087','A091','A092','B17','B20']}
dump(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083',
          'gap_id':'C024-PHYSICAL-REFERENCE-OWNED-RESERVE-COMPATIBILITY','attempt_id':'A083-stage4-physical-bayes-core',
          'method':'Consume A092 shared-control audit; independent exact exposed-data tree and signed ledger; small Lean rational posterior core; analytic all-m KL obstruction',
          'mathematical_delta':'Correct reach-weighted reference normalized and composable; equal-leaf substitution has unbounded KL/I even on H<4I Boolean family; terminal influence retained; universal signed reserve compatibility unpaid',
          'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'NARROW_CORE_CLOSED_UNIVERSAL_BRIDGE_OPEN',
          'claim_versions_used':[{'claim_id':'A083-COHERENT-ROW-CORE-AND-RESET-OBSTRUCTION','version':1,'use':'prior formal-interface context; unchanged independent A092 scope acceptance consumed, no new proof premise'}, {'claim_id':'A050-ACTIVE-LABEL-SCHEDULE-REPAIR','version':1,'use':'A092-reviewed zero-injection context; needed fixed projection independently reconstructed'}],
          'claims_created_or_changed':[{'claim_id':cid,'version':1}],
          'source_artifacts':['PROOF.md','REPORT.md','out/SOURCE_RECEIPTS.json','out/FROZEN_CASE_SPEC.json','out/FROZEN_SPEC.json','out/RESULT.json','out/LEAN_RESULT.json'],
          'next_consumers':claim['next_consumers'],
          'next_action':'Compare one correctly reach-weighted Bayes mixture to A038 owned reserve at a mixed data/controller prefix, retaining signed KL and both unfinished terminal-core bills; A092/A087 review',
          'stagnant_substantive_attempts':0,'blockers':['Universal exclusive-influence payment for the complete signed reference cost is unsupported','Independent review of the new narrow claim and supervisor/mirror adoption unverified'],
          'packet_ids':['A083']}
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
base=Path(r'~\brain_workers\FEI100_20261011')
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),base/'BOARD.md',base/'claude/B17/STREAM_NOTES.md']
for f in ['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/entropy_tools.py']:
    sources.append(base/'agents/A092/runs/20261014T020903Z-fleet05-A092-counterexample-referee'/f)
for f in ['REPORT.md','CLAIMS.json']:
    sources.append(base/'agents/A039/runs/20261013T235428Z-fleet05-A039-projection-under-restrictions'/f)
sources.extend([base/'agents/A038/STATUS.md', A/'runs/20261013T234228Z-fleet05-A083-formal-core/code/CoherentTransport.lean',A/'runs/20261013T234228Z-fleet05-A083-formal-core/code/check_lean.py'])
dump(R/'out/SOURCE_RECEIPTS.json',{'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources],'notes':'mutable source hashes captured at finalization, not asserted identical to start snapshot; no unfinished A038 stage4 theorem used'})
(A/'STATUS.md').write_text('STATE: A083 stage 4 complete: physical Bayes core Lean PASS; essential shared-data tree signed ledger 1787 exact checks PASS; equal-leaf reference KL/I unbounded with H<4I; FEI OPEN.\nNEXT: Compare correct physical reach-weighted Bayes reference with A038 owned reserve at one mixed data/controller prefix, retaining signed KL and both child bills; A092/A087 review.\n',encoding='utf-8')
entry='\n2026-10-14 stage 4 (run '+R.name+'): Consumed A092 independent acceptance of stage3 and shared-control bank obstruction. Proved physical weighted posterior composition and all-m equal-leaf-reference KL/I obstruction after essential u exposure. Lean first timed out with blank diagnostics; unchanged rerun passed (49.145s, 528928768 bytes peak). Both memok gates exited0. Initial v1 pilot had an incorrect strict-inequality assertion on an equal-column corner; corrected, preserved, then omitted irrelevant b-query in v2. Final pilot172 assertions; main1787 assertions in .508s, twelve actual trees and five formula-only KL certificates. Full signed ledger, terminal influence and no zero-row division verified. New local claim awaits review; universal signed reserve payment OPEN.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson='\n2026-10-14 durable fact: On F_m shared AND priority gate after querying u, the essential u=0 and u=1 leaves number m+2 and m+3. Physical surviving-v probabilities are t/2 and 3t/4; equal-leaf references give 1/(m+2),2/(m+3). Conditional KL average exceeds 1/[2(m+3)] bits for m>=10 while I=t(5m/8+2), giving unbounded mismatch/I without violating FEI (H<4I). Correct Bayes column is the PHYSICAL reach-weighted mixture; posterior atom/group and group/total compose, and empty groups have zero atoms. Lean checks exactly that local Rat core, not entropy. Data-first terminals have H=0 but influence5t/8 and cannot be dropped from the ledger. Bank tends3, signed residual tends1.5: preserve cancellation. Avoid irrelevant b query at u=0,a=0 when comparing essential policies.\n'
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)
protocol=json.loads(sources[0].read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert json.loads((R/'out/RESULT.json').read_text())['status']=='PASS'
assert json.loads((R/'out/LEAN_RESULT.json').read_text())['status']=='PASS'
lean=(R/'code/BayesOccupancy.lean').read_text()
assert 'sorry' not in lean and 'axiom ' not in lean
assert len((A/'STATUS.md').read_text().splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
dump(R/'out/ARTIFACT_RECEIPTS.json',{'validation':'PASS','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]})
print(json.dumps({'status':'PASS','claim_sha256':digest,'run_files':len(files),'progress_copies_identical':True,'mirror_verified':False}))
