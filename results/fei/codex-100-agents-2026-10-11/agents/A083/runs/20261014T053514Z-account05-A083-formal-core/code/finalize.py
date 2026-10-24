from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
cid='A083-REFERENCE-ONLY-MATCHING-AND-PAID-CONDITIONAL-BILL'
statement=('For any finite source law p_e(t,z), dominating normalized reference q_e(t,z) and the same normalized branch channel on both, including fixed fallback on source-zero rows, inherited and actual child conditional Z laws agree on every source-occupied (b,t) row if and only if L=p_e/q_e (allowing zero) is constant on every component of the branch-support graph formed on the FULL reference support. The source conditional KL splits exactly into conditional branch KL and physical mean inherited-child conditional KL; reference-only mass is conserved. Lean-kernel-checked rational core: g*k0+g*k1=g when k0+k1=1; both transported masses zero imply g=0; u/(u+g)=1 iff g=0 when u+g!=0. For the actual uniform four-bit sign F(x,a,b,y)=(-1)^a if x=0, else 2y-1 if b=1, else +1, query b with spectator y and the complete canonical nonempty occupancy reference (empty atom 1/16, nonempty mass15/16, marginal vector r=(8/15,8/15,4/15,4/15)). Its unique positive normalizer satisfies 1-c=(1-8c/15)^2(1-4c/15)^2 with 3/4<c<13/16. With fair source-zero fallback the COMPLETE mean inherited-child conditional KL is C_child=-(1/2)log2(1-4c/15), and 1/8<C_child<3/16. Root H=3,I=3/2, queried influence1/4; actual child entropies are2,2 and influences1,3/2, so certified mean S4=mean(4I-H)=3. An explicitly unused mean-child S4 account pays C_child once using less than1/16 and leaves more than15/16, retaining both terminal entropies. This is a mean allocation, not an individual-child fraction bound. The retained quotient KL, source erasure/outcome costs, further reference conversion and universal eligibility/payment remain unpaid. Graph/KL/Fourier/canonical interpretation is analytic and exactly certified, not a Lean entropy theorem; no FEI counterexample or universal constant improvement is asserted.')
hyp=['Finite normalized laws; source dominated by reference; retain all reference-positive rows and apply the same declared normalized branch channel',
     'Conditional matching required on source-occupied child rows, including absence of extra reference-positive spectator atoms there',
     'Actual application on independent uniform Boolean physical bits; fresh private b query after the specified essential data-exposure provenance; Shannon/KL bits',
     'Canonical reference matches empty atom and maximum-entropy nonempty conditional marginals; fair fallback on source-zero erased rows',
     'The mean-child S4=3 account is certified from the two actual terminal laws and is explicitly unused before this one conditional transaction; no other bank is simultaneously spent',
     'Only local rational identities are Lean checked; universal finite matching and actual canonical partial-payment proof is analytic with independent exact certificates']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A083'],
       'proof_source':{'run_id':R.name,'files':['PROOF.md','code/ReferenceOnlyRows.lean','code/reference_rows.py','out/RESULT.json','out/CANONICAL_FIXTURE.json','out/AND_PARITY.json','out/LEAN_CHECK.txt','out/LEAN_RESULT.json']},
       'proof_dependencies':[],'review_records':[],'status':'LOCAL_RATIONAL_CORE_KERNEL_CHECKED_ANALYTIC_CRITERION_PROVED_EXACT_CONDITIONAL_PAYMENT_PENDING_REVIEW',
       'supersedes':[],'refutes':['Free omission of source-zero/reference-positive erased rows in normalized same-kernel reference transport','Identifying fallback-dependent separate outcome/child KL bills across different fallbacks without their signed adjustment'],
       'first_unproved_line':None,'next_consumers':['A038','A039','A047','A050','A087','A092','B17','B20']}
dump(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083',
          'gap_id':'C024-PHYSICAL-REFERENCE-OWNED-RESERVE-COMPATIBILITY','attempt_id':'A083-stage5-reference-only-rows',
          'method':'Support-complete finite Bayes matching proof; three small Lean Rat identities; exact Boolean census and canonical occupancy partial-payment certificate',
          'mathematical_delta':'Reference-only support boundary closed; actual canonical b-query inherited conditional bill paid from <1/16 certified mean child surplus with both terminals; remaining quotient and continuation unpaid',
          'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'NARROW_SUPPORT_AND_CONDITIONAL_PAYMENT_CLOSED_UNIVERSAL_FEI_OPEN',
          'claim_versions_used':[{'claim_id':'A050-COMMON-CONDITIONAL-KERNEL-REPAIR','version':1,'use':'A092 independently accepted scope boundary consumed as context; needed algebra reconstructed locally'}],
          'claims_created_or_changed':[{'claim_id':cid,'version':1}],
          'source_artifacts':['REPORT.md','PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/FROZEN_LEAN_SPEC.json','out/RESULT.json','out/CANONICAL_FIXTURE.json','out/LEAN_RESULT.json'],
          'next_consumers':claim['next_consumers'],
          'next_action':'Carry SAME inherited canonical reference through essential y query in b=1 child, retaining other terminal and booked conditional spend; pay remaining quotient/conversion from SAME unused mean-child owner; A047/A092 review',
          'stagnant_substantive_attempts':0,'blockers':['Universal eligible remaining-quotient/reference and terminal-continuation payment is unsupported','New claim independent review and supervisor/mirror adoption unverified'],
          'packet_ids':['A083']}
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
base=Path(r'~\brain_workers\FEI100_20261011')
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),base/'BOARD.md',base/'claude/B17/STREAM_NOTES.md']
for agent,run,files in [
 ('A047','20261014T044331Z-account05-A047-boundary-search',['REPORT.md','PROOF.md']),
 ('A092','20261014T045641Z-account05-A092-counterexample-referee',['REPORT.md','PROOF.md','CLAIMS.json']),
 ('A038','20261014T022516Z-account05-A038-occupancy-term-audit',['REPORT.md']),
 ('A038','20261014T051947Z-account05-A038-occupancy-term-audit',['REPORT.md']),
 ('A039','20261014T025407Z-account05-A039-projection-under-restrictions',['REPORT.md','CLAIMS.json'])]:
    sources.extend(base/'agents'/agent/'runs'/run/f for f in files)
sources.extend([A/'runs/20261014T023633Z-account05-A083-formal-core/code/occupancy_check.py',A/'runs/20261014T023633Z-account05-A083-formal-core/code/check_lean.py'])
dump(R/'out/SOURCE_RECEIPTS.json',{'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources],'scope':'A039 excerpts; all other listed proof/report mathematical locators as REPORT; mutable captures at finalization'})
dump(R/'out/MEMORY_GATES.json',{'observed_memok_exit_codes':[0,0,0],'observed_free_GB':[['33.6','47.4'],['29.1','42.3'],['31.5','46.4']],'column_order':['physical','commit'],'command':r'python -X utf8 ~\brain_workers\FEI100_20261011\tools\memok.py','receipt_basis':'observed tool outputs before respective Lean launches'})
(A/'STATUS.md').write_text('STATE: A083 stage 5 complete: reference-only support criterion closed; Lean Rat core PASS; 270432 exact checks; canonical b-query conditional KL paid from <1/16 certified mean child surplus; FEI OPEN.\nNEXT: Carry SAME inherited canonical reference through b=1 child y query; preserve booked conditional spend and other terminal; pay quotient/conversion from remaining SAME owner; A047/A092 review.\n',encoding='utf-8')
entry='\n2026-10-14 stage5 '+R.name+': Consumed A047/A092 support boundary and A038 certified-child direction. Extended matching graph to full reference support allowing zero likelihood. Actual exposed private b query has full conditional child KL=-(1/2)log2(1-4c/15) in (1/8,3/16); paid from <1/16 of independently certified mean S4=3, terminals H2/I1 and H2/I3/2 retained. Pilot96/2258 checks; final main7008 census+9 rational+1 canonical cases,270432 checks in41.1484s. Two blank Lean60s timeouts, preserved; unchanged source bounded120s passed93.1585s peak525996032bytes; all three memok gates exit0. No failed mathematical checker. Remaining quotient/reference/continuation and universal eligible owner payment OPEN; independent review pending.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson='\n2026-10-14 durable stage5: Under domination rather than equal erased support, inherited conditional matching iff p_e/q_e (including0) is constant on branch-support graph components formed on FULL q_e support. Reference-only ghosts cannot vanish under a normalized fallback and may connect otherwise disjoint real branch cliques. A047 common-support scope remains valid. On reached F=(-1)^a if x=0, else2y-1 ifb=1, else+1, private b query with canonical occupancy reference has C_child=-(1/2)log2(1-4c/15), c in(3/4,13/16), so1/8<C_child<3/16. Both terminal H=2, I=1 and3/2; meanS4=3 explicitly unused pays conditional cost once with <1/16 fraction. It is a MEAN allocation; individual child fraction need not hold. Quotient KL, source erasure/outcome and fresh projection still need payment. AND2 times parity with uniform reference: fair ghost fallback yields childKL1/outcome0, allghosts-to-zero yields childKL(log2 3)/2/outcome1-(log2 3)/2; total owned debt conserved. Formal Rat core only; entropy/graph theorem analytic.\n'
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)
protocol=json.loads(sources[0].read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
result=json.loads((R/'out/RESULT.json').read_text());assert result['status']=='PASS' and result['assertions']==270432
assert json.loads((R/'out/LEAN_RESULT.json').read_text())['status']=='PASS'
lean=(R/'code/ReferenceOnlyRows.lean').read_text();assert 'sorry' not in lean and 'axiom ' not in lean
assert len((A/'STATUS.md').read_text().splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'];assert all(p.stat().st_size<20_000_000 for p in files)
dump(R/'out/ARTIFACT_RECEIPTS.json',{'validation':'PASS','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]})
print(json.dumps({'status':'PASS','claim_sha256':digest,'run_files':len(files),'progress_copies_identical':True,'mirror_verified':False}))
