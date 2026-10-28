from pathlib import Path
import json, hashlib, datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s): Path(p).write_text(s,encoding='utf-8',newline='')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o): write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name in ('check.py.log','independent.py.log'):
    s=read(R/'out'/name)
    assert '"status": "PASS"' in s and 'Traceback' not in s, name
p=R/'PROOF.md'
s=read(p).replace('Author derivation, exact checks pending; external review pending. Bits throughout.',
    'Author proof with exact checks passed; external mathematical review pending. Bits throughout.')
s=s.replace('For the family above, (4)--(6) imply',
    'After querying the marked bit y, descend to V of the remaining controller; before that query retain the mark in both control children. Thus the marked y increment is zero. For the family above, (4)--(6) imply')
s=s.replace('Exact scalar checks verify the central-binomial recurrence and both squared\nbounds on a frozen finite range;',
    'The FWHT checker passed 37 assertions on n3,5,7 (12.6894 seconds). The\nseparate direct-character checker passed 790 assertions, including m1..256\nexact central-binomial recurrence and squared bounds (1.4606 seconds);')
write(p,s)
source=Path('agents/A022/runs/20261023T120109Z-account03-A022-one-point-surgery')
statement=(
 'Let V(f)=sum_{S nonempty} fhat(S)^2 log2(sum_{T containing S} fhat(T)^2/fhat(S)^2), '
 'and GV(f) its sum of parent-minus-mean-child increments over physical coordinates. '
 'Let b(x)=g(x0,x1,x2)g(x3,x4,x5), with g=-1 only at000, delta=1/64, '
 'a_n balanced majority on n=2m+1 controls, m>=1, and F_n=b*a_n at data points0,e0, b elsewhere. '
 'For h_n(y,z)=(-1)^y a_n(z), GV(F_n)-2delta GV(h_n)>=delta log2(m+1)-37, '
 'whereas I_DATA(F_n)<=6. Therefore no finite constant K>=0 makes '
 'GV(F_n)<=2delta GV(h_n)+K I_DATA(F_n) hold for all m. '
 'The root marked-singleton term J_y(h_n) is zero, so a fixed root J credit cannot fix this. '
 'In contrast -37<=GV(F_n)-2delta GV(a_n)<=49 and I_DATA(F_n)>=21/16; '
 'the original-controller transfer holds with K=256 for this same family. '
 'An explicit failure of the unmarked-selector K=256 transfer is m=2^100736. '
 'These statements concern a proposed potential-transfer inequality, not unbounded Fourier H/I.')
gap='A021-ADJACENT-DEPENDENT-CONTROLLERS-MARKED-SECTOR-PAYMENT'
first=('For two arbitrary dependent controllers, pay the complete signed marked singleton/sector '
        'cocycle after both physical outcomes from one compatible original owner at a stable rate. '
        'Universal original-owner eligibility and the universal GV criterion remain unproved.')
claim={
 'claim_id':'A021-ADJACENT-MUX-OWNER-VACUUM-OBSTRUCTION','version':1,
 'exact_statement':statement,
 'hypotheses':['Independent uniform DATA/control cubes; Boolean majority n=2m+1, m>=1.',
 'All logarithms base2; zero spectral terms omitted; DATA influence counts all six physical DATA bits.',
 'The tested combined-selector extension is UNPROVED, not a theorem asserted by A022@9.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A021'],
 'proof_source':{'path':'PROOF.md','sha256':sha(p),'sections':'1--5; analytic all-m induction and uniform curvature estimate'},
 'proof_dependencies':[{'claim_id':'A022-ODDFACE-SURGERY-GAP-LEDGER','version':9,
 'statement_sha256':'873c5aeda6a49b7224df3a50364eb592977fea0fe916b4abb4f97c9353bdb450',
 'use':'GU_PROOF.md Section7 adjacent-selector interface and notation; independently rederived for the same-controller family; no general adjacent bound assumed.',
 'acceptance':'Source author proof; external acceptance not assumed.'}],
 'review_records':[{'reviewer':'A021 author, alternative implementation',
 'scope':'FWHT n3,5,7 all physical queries:37 assertions; direct characters n3 plus scalar m1..256:790 assertions.',
 'result':'PASS; computational reconstruction is separate, but not independent external human/agent review.'}],
 'status':'AUTHOR_PROVED_SCOPED_OBSTRUCTION_AND_REPAIR_EXTERNAL_REVIEW_PENDING',
 'supersedes':[],
 'refutes':[{'statement':'Unasserted extension (N) in PROOF.md: GV(F)<=2delta GV(h)+K I_DATA for all adjacent shared-controller edits and one fixed K.',
 'scope':'No proved A022@9 assertion is refuted; no FEI counterexample claimed.'}],
 'first_unproved_line':first,
 'next_consumers':['A022','A025','A028','A029','A087','A094','B05','B20']}
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A021',
 'gap_id':gap,'attempt_id':'shared-majority-selector-vacuum-cocycle-1',
 'method':'Actual Boolean shared-majority counterfamily; exact nonempty upper-set split; central-binomial induction; uniform second-derivative bounds; independent rational-log checks.',
 'mathematical_delta':'Unmarked combined-selector ownership loses an unbounded logarithmic restriction cocycle despite root singleton zero; retaining the original marked controller repairs this family at the same256 rate.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_EXTERNAL_REVIEW_PENDING',
 'mathematical_status':'SCOPED_POTENTIAL_TRANSFER_OBSTRUCTION_AND_SAME_FAMILY_REPAIR; FULL_FEI_OPEN',
 'claim_versions_used':['A022-ODDFACE-SURGERY-GAP-LEDGER@9, GU_PROOF Section7 only, family interface rederived'],
 'claims_created_or_changed':['A021-ADJACENT-MUX-OWNER-VACUUM-OBSTRUCTION@1'],
 'source_artifacts':[str(source/'GU_PROOF.md'),str(source/'CLAIMS.json'),str(source/'PROOF.md'),
 'BOARD.md header2026-10-23T13:48Z','claude/B05/STREAM_NOTES.md v2',
 'A029 20261023T125429Z REPORT.md (context only)',
 'A021 stage20 arithmetic.py and direct-character arithmetic prefix (own prior code)'],
 'next_consumers':claim['next_consumers'],'next_action':first,
 'stagnant_substantive_attempts':0,
 'blockers':['External mathematical review outstanding.',
 'Arbitrary dependent-controller marked-sector payment and universal owner eligibility open.',
 'Remote publication/mirror verification not performed by this run; supervisor collection pending.',
 'Brain self-care degraded/unverified: stale model/state/dream affects personalization and continuity, not a mathematical acceptance claim.'],
 'packet_ids':['A021']}
dump(R/'PROGRESS.json',progress)
write(R/'PACKET_DELTA.json',read(R/'PROGRESS.json'))
report=f'''# A021: shared-selector singleton debt

## exact target, quantifiers, hypotheses and units

Test one original-owner transfer for two adjacent edits on the SAME control cube, using precisely A022@9's nonempty upper-set V and its total physical restriction increment GV. This stage proves that the natural but UNPROVED replacement of the original marked controller by an unmarked shared selector cannot hold with any dimension-independent DATA payment. The actual Boolean majority family, all-m bounds, and the same-family repair are in [PROOF.md](PROOF.md). Bits, uniform measure, n=2m+1 with m>=1, t=2, k=6, delta=1/64. DATA influence includes every one of the six DATA coordinates. Full FEI remains OPEN; no H/I divergence is asserted.

## sources actually read, revisions and theorem locators

Read BOARD.md at its 2026-10-23 13:48 UTC header, B05 STREAM_NOTES v2, and own stage20 STATUS. The lead notes are older than the current exact obstruction; previous R/G sign corrections remain in force. Read A022 run20261023T120109Z PROOF.md, CLAIMS.json and GU_PROOF.md completely; the relevant current target is GU_PROOF Section7's adjacent shared selector and unpaid singleton term, not the auxiliary entropy handoff already closed there. A022-ODDFACE-SURGERY-GAP-LEDGER@9 statement hash is recorded in CLAIMS.json. Read A029 run20261023T125429Z REPORT.md for context. The execution protocol was reread in full; its old campaign end is superseded by the owner's explicit 2026-10-23 14:49 UTC deadline. Earlier required sources were read in the recovered stages; no new claim from an unread paper is used here. Source bytes used for the current proof are hashed in out/PERSISTENCE.json.

## complete derivation or exact first unsupported line

The complete analytic argument is PROOF.md Sections1--4. For h=y*a with balanced a, GV(a)-GV(h)=sum_j phi(ahat(j)^2), although root V(a)=V(h) and the root marked singleton is zero. For majority this debt is n phi(d_m^2), d_m=binom(2m,m)/4^m. An exact output decomposition gives V(F)=2delta V(a)+T(mean(a)). On |s|<=1/2, -13<T''(s)<1; the total DATA drift Dstar is independent of majority width and lies in[-36,42]. Thus GV(F)-2delta GV(h)>=delta log2(m+1)-37, while I_DATA<=6. This defeats every fixed K; m=2^100736 is an explicit analytic K=256 witness. No astronomical truth table is enumerated. Keeping the original marked a gives residual in[-37,49] and I_DATA>=21/16, hence repairs the SAME family with constant256. The exact first unsupported universal line is: {first}

## executed validation with domain, arithmetic, commands and outputs

Frozen SEARCH_SPEC.json and REPLAY_SPEC.json record family, helper hashes, cases, symmetry, arithmetic, memory estimate180MB and runtime ceiling120seconds; wrapper timeout130seconds. Pilot n3 passed13 assertions in0.4201seconds. Main command: `python -X utf8 {R.name}/code/run_checks.py`, run from the runs directory (equivalently the absolute script path). FWHT checker n3,5,7, total bits9,11,13, checks EVERY physical F and h query and exact upper-set identities:37 assertions PASS in12.6894seconds. Separate direct-character/direct-upper-set implementation n3 and scalar m1..256:790 assertions PASS in1.4606seconds. All spectra are integer/exact rational; logarithms use separate40/48-term rational enclosures and exact prime-log identity comparison. Logs and certificates are in out/. The independent implementation shares the mathematical target and author; it is computational reproduction, not independent external mathematical acceptance. Finite checks do not supply the all-m bridge; induction and curvature estimates do. These bounded jobs were below the300MB preflight threshold; no heavy search or dimension escalation was started.

## proof dependencies and changed downstream conclusions

This is a narrowly scoped obstruction/repair for an UNPROVED extension of A022@9's Section7, using its actual V/GV quantities. It does not refute the proved one-point stable256 transfer, the auxiliary handoff, or earlier unequal-depth cut-payment certificates. Root singleton credit is inadequate: its value is zero in this family while its restriction cocycle grows. Consumers must retain the marked sector and BOTH child liabilities when transferring one compatible owner. A022@9's general adjacent-controller line was already open and remains open. A025/A028/A029 source transport and A087/A094 original-owner eligibility are not proved by the new identity. Statement, proof and dependency hashes are in CLAIMS.json and out/PERSISTENCE.json. No new broad universal candidate is opened.

## one next mathematical action and independent reviewer

Ask A022/B05 to reconstruct the marked-sector cocycle for TWO arbitrary dependent controllers and prove its payment from the same original owner at a stable constant, retaining both physical outcomes. A029 or A094 can independently check the all-m vacuum-migration obstruction and owner convention; these are requested downstream consumers, not reviewers already assigned or contacted. This targets the known unpaid universal line rather than another width enumeration.

## actual persistence receipts or precise save blocker

All four required protocol files, proof, frozen specifications, code, certificates and rolling updates are saved under the authorized A021 folder. out/PERSISTENCE.json records byte counts and SHA256 values; out/FINAL_VALIDATION.json checks exact protocol field sets, compatibility-copy equality, statement/proof hashes and required outputs. External review, supervisor copy, remote publication and mirror verification remain outstanding; no receipt is represented as mathematical downstream use. No messages were sent and no other agent's folder was modified. Brain self-care is degraded/unverified because its required model/state/dream sources are stale; personalization and continuity remain affected. This does not certify or invalidate mathematics. Current computations have completed; no research job is left running.

**Universal bridge:** This stage moves C024 history transfer and C019 stopping-tree payment by identifying an unavoidable signed singleton-sector debt in adjacent-controller ownership and proving that deleting it causes an unbounded logarithmic loss, while retaining it restores the same256 rate on this family. The unpaid step is stable original-owner payment of that full signed sector cocycle for arbitrary dependent controllers, together with owner eligibility; no universal GV inequality or FEI theorem is claimed. The shortest next route is the marked-sector payment at that already exposed universal interface, because further rare-core width checks cannot settle source compatibility or history transfer.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A021 13:51 stage complete locally: shared-selector singleton debt is logarithmically unbounded; retaining original marked owner repairs SAME majority family at256; exact checks PASS; external review pending; FEI OPEN.\nNEXT: A022/B05 pay signed marked singleton/sector cocycle for TWO arbitrary dependent controllers from ONE original compatible owner, both outcomes retained; A029/A094 independently review obstruction.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | Stage {R.name}: consumed A022@9 GU_PROOF Section7. Proved actual Boolean shared-majority obstruction to UNPROVED unmarked-selector GV transfer (root J=0, child debt grows logarithmically), plus SAME-family original-owner256 repair. Pilot13/main37/separate790 assertions PASS. Analytic all-m bridge supplied. Not an FEI counterexample; external review and arbitrary-controller payment open. Full receipts in stage out/.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-23 13:51 stage: For balanced a, GV(a)-GV(y*a)=sum_j phi(ahat(j)^2), although V(a)=V(y*a) and root marked singleton J_y(y*a)=0. A new character moves vacuum child liability into a marked singleton; root equality does not preserve signed restriction increments. On the two-adjacent-point t2 tensor seed with shared odd-majority controller, GV(F)-2delta GV(y*a)>=delta log2(m+1)-37, delta1/64, I_DATA<=6. The original marked controller gives residual[-37,49] and I_DATA>=21/16, hence SAME256 repair. This obstructs only an unproved combined-selector ownership extension, not A022@9 or FEI. Keep the mark through both outcomes; root-only J credits cannot pay its history cocycle. See stage20261023T135142Z PROOF.md for all-m proof and exact witness.\n')
manifest={'generated_at':now,'local_only':True,'files':{str(p.relative_to(R)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name not in ('PERSISTENCE.json','FINAL_VALIDATION.json')},
 'sources':{str(source/n):sha(source/n) for n in ('GU_PROOF.md','CLAIMS.json','PROOF.md')},
 'rolling':{str(A/n):sha(A/n) for n in ('STATUS.md','WORKLOG.md','LEARNED.md')}}
dump(R/'out/PERSISTENCE.json',manifest)
protocol=json.loads(read('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
expected=set(protocol['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert claim['proof_source']['sha256']==sha(R/'PROOF.md')
assert all(h in report for h in protocol['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
dump(R/'out/FINAL_VALIDATION.json',{'status':'PASS','at':now,'exact_protocol_fields':True,'compatibility_copy_identical':True,'statement_and_proof_hashes':True,'report_fields_and_final_bridge':True,'rolling_status_two_lines':True,'all_files_under20MB':True,'full_fei':'OPEN','external_review':'PENDING','research_jobs_left_running':False})
print(json.dumps({'status':'PASS','run':str(R),'manifest_files':len(manifest['files']),'claim':claim['claim_id'],'external_review':'PENDING','full_fei':'OPEN'}))
