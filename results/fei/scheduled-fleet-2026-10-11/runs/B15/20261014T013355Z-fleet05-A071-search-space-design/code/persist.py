import hashlib,json,sys
from datetime import datetime,timezone
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(100000)
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
v=json.loads((RUN/'out/verification.json').read_text(encoding='utf-8'))
assert v['all64_fail_monotone_E'] and v['all64_fail_separator_K_but_core_passes']
assert v['one_flip_rescues_A080_K'] and v['one_flip_escapes_rare_band']
one=next(r for r in v['orbits'] if r['mask']==1)
assert Q(one['E_bounds'][0])>max(Q(r['E_bounds'][1]) for r in v['orbits'] if r['mask']!=1)
assert Q(334828508,100000000)<Q(one['E_bounds'][0])
assert Q(one['E_bounds'][1])<Q(334828510,100000000)
assert sum(r['orbit_size'] for r in v['orbits'])==64
assert len(v['orbits'])==10 and v['A080_core_states_independently_matched']==4
claim_id='A071-F6-INDEPENDENT-SIGN-ADMISSION-OBSTRUCTION'
statement=('Let h be the Boolean sign negative on {0,1,2,4,8,16,32,6,17,40}, and define '
 'g0=h,g1=h(g0^6),g2=h((-g1)^6),g3=h(g2^6), with independent disjoint copies. '
 'For E(f)=min relevant_i H(S_i|S_without_i)/Inf_i(f) in bits, E(g3)>33483/10000. '
 'Over all64 independent output-sign choices e in {0,1}^6, every actual7776-bit '
 'F_e=h((-1)^e_0*g3,...,(-1)^e_5*g3) has E(F_e)<33483/10000. '
 'The unique maximizing orbit under the actual48 gate automorphisms complements exactly one block, '
 'and its minimum E lies strictly between334828508/100000000 and334828510/100000000, hence above669/200. '
 'For any core of minority probability0<p<=1/16, complementing exactly one of six identical minority-oriented '
 'blocks yields minority sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6, with3p<sigma(p)<4p<=1/4. '
 'This gives finite-step bias escape but no monotone-erasure or terminal-entropy payment theorem and no FEI resolution.')
claim={'claim_id':claim_id,'version':1,'exact_statement':statement,
 'hypotheses':['Uniform independent physical bits; all copies disjoint; Boolean signs and entropy bits',
  'Gate fixed as stated; search permits independent output signs only, not changing gates or core truth tables',
  'Core recursion exactly the stated three steps; transitive physical coordinates of each core retained',
  'Finite erasure assertion uses actual g3; analytic minority-map assertion permits arbitrary core dimension',
  'Exact rational enclosures and proved group action; external independent acceptance pending'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A071; A080 supplied the explicit high-erasure rare-core target'],
 'proof_source':str(RUN/'PROOF.md'),
 'proof_dependencies':['Elementary Walsh/biased composition, physical pivotal identity and pair-entropy homogeneity reconstructed in PROOF.md',
  'A080 g3 circuit specification consumed; four core states independently reconstructed and matched, not assumed universal theorem',
  'Exact spectrum/coordinate certificates in out/big/results.json, out/verification.json and out/bias_map.json'],
 'review_records':[],'status':'LOCAL_EXACT_CERTIFICATE_AND_SCOPED_PROOF_REVIEW_PENDING',
 'supersedes':[],'refutes':['Proposed extension: for every actual high-E core g some independent six-block sign vector preserves E(g)',
  'Proposed extension: independent signs always preserve every threshold K already exceeded by g; explicit failure K=33483/10000'],
 'first_unproved_line':None,'next_consumers':['A075','A080','A084','A089','A074','A092','B15','B20']}
write(RUN/'CLAIMS.json',[claim])
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',
 BASE/'agents/A075/runs/20261014T005346Z-fleet05-A075-search-to-theorem-bridge/REPORT.md',
 BASE/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard/REPORT.md',
 BASE/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard/code/check.py',
 BASE/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard/out/VALIDATION.json',
 BASE/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard/out/CERTIFICATE_SUMMARY.json',
 BASE/'agents/A089/runs/20261014T000812Z-fleet05-A089-repair-specialist/REPORT.md',
 AGENT/'runs/20261013T215901Z-fleet05-A071-search-space-design/REPORT.md']
write(RUN/'out/source_manifest.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B15','packet_id':'A071',
 'gap_id':'B15-ARBITRARY-CORE-BIASED-ADMISSION','attempt_id':'A071-stage4-independent-block-signs',
 'method':'Freeze all64 independent signs on actual1296-bit g3; exact48-automorphism quotient to10 orbits; all6 block types per orbit; exact rational biased transform,96-bit proved logs and independent uniform-Walsh reexpansion.',
 'mathematical_delta':'All64 signs fail monotone E admission and K=33483/10000; one-flip maximizing orbit rescues prior669/200 threshold and exits rare band. Exact universal one-flip minority map has3p<sigma(p)<4p for0<p<=1/16. Terminal C_e retained; no universal payment.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; independent review/supervisor copying pending',
 'mathematical_status':'BOUNDED_HIGH_E_INDEPENDENT_SIGN_ADMISSION_REFUTED; BIAS_ESCAPE_PROVED; OWNED_PAYMENT_AND_FEI_OPEN',
 'claim_versions_used':['A071-F6-BIASED-ADMISSION-OBSTRUCTION@1 and own recentered interface',
  'A080 stage3 explicit g3 specification; locally independently reconstructed, source external review pending',
  'A075-RARE-CORE-LOCALIZATION@1 consumed for gap/dispatch context only, not a mathematical premise',
  'A089 stage3 signed-reserve criterion and terminal identity consumed for context, split reconstructed'],
 'claims_created_or_changed':[claim_id+'@1'],
 'source_artifacts':[str(p) for p in sources]+[str(RUN/'out/verification.json'),str(RUN/'out/bias_map.json'),str(RUN/'out/big_manifest.json')],
 'next_consumers':['A075','A080','A084','A089','A074','A092','B15','B20'],
 'next_action':'Price one-flipped-block rare-bias escape using exact signed reserves, all physical block types and complete terminal C_e in one exclusive influence ledger; A074/A092 independently reconstruct group coverage and decisive coordinate certificates.',
 'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A071']}
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A071 stage4 complete locally: all64 independent g3 block signs fail K=3.3483; best one-flip E=3.34828509 rescues K=3.345 and escapes rare bias; exact10 orbits; review pending; FEI OPEN.\nNEXT: A075/A089 price one-flip escape signed reserves plus full terminal C_e in one physical ledger; A074/A092 audit48-automorphism coverage and15 decisive certificates; no more raw sign/depth search.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Stage20261014T013355Z: consumed A075 rare localization and A080 high-E rare obstruction, then froze ALL64 independent block signs on g3. Verified48 gate automorphisms,10 orbits and60 representative block types; internal independent uniform-Walsh reconstruction plus15 decisive reserve checks passed. Best one-flip E=3.348285089821851 belowK3.3483 whilecoreE3.3483872565 exceedsK; oldK3.345 rescued. One-flip minority0.0843323290 exitsrare; exact sigma=4p-10p^2+18p^3-19p^4+10p^5-2p^6 lies between3p,4p on0<p<=1/16. Full terminal H,C_e retained. Pilot0.2179s,full computation375.827s,verifier69.555s. Two33MB packet files moved intoout/big with hashes/regeneration. No FEI or all-depth paid admission claim. Run '+str(RUN)+'.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Mixed signs matter: on actualg3=h(h((-h(h^6))^6)^6) as defined explicitly in stage4 PROOF, all64 independent signs are exactly10 orbits under48 matched-pair automorphisms. Best orbit flips oneblock and hasE3.348285089821851<coreE3.3483872565, so monotone/E-threshold3.3483 admission fails. It still rescues669/200 and increases minority from0.02227493483 to0.08433232901. Keep all6 block minima: foroneflip the fourunmatched blocks setE; the complemented block and its mate have larger ratios. Foranyminorityp<=1/16, oneflip sigma=4p-10p²+18p³-19p⁴+10p⁵-2p⁶ satisfies3p<sigma<4p and eventually exitsrare. This is bias escape, not erasure/entropy payment. Mixed terminal identity H=QHcore+C_e,I=QIcore,Q=sumq_j; no corebank reset. Rawcommon-sign absorption remains true at its ownscope.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected and set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '\n## '+field+'\n' in report
assert report.rsplit('\n## ',1)[-1].startswith('Universal bridge\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
big=json.loads((RUN/'out/big_manifest.json').read_text())
for r in big:
 p=RUN/r['path'];assert p.stat().st_size==r['bytes'] and digest(p)==r['sha256']
write(RUN/'out/schema_validation.json',{'protocol_fields_exact':True,'report_fields_present':True,'packet_delta_identical':True,
 'statement_hash_valid':hashlib.sha256(statement.encode()).hexdigest()==claim['statement_sha256'],
 'winner_orbit_strictly_separated':True,'K33483_over10000_verified':True,
 'all64_patterns_covered':True,'large_files_only_in_out_big_with_hashes_and_commands':True,'full_FEI':'OPEN'})
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='receipts.json':
  assert p.stat().st_size<20_000_000 or p.is_relative_to(RUN/'out/big')
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)})
write(RUN/'out/receipts.json',{'saved_at_utc':now,'files':receipts,'independent_review':'PENDING',
 'supervisor_copy':'PENDING','mirror_verification':'PENDING','downstream_use':'PENDING'})
print(json.dumps({'run':str(RUN),'schema':'PASS','files':len(receipts)+1,'claims':1,
 'all64_fail_K3_3483':True,'oneflip_rescues_K3_345':True,'full_FEI':'OPEN'}))
