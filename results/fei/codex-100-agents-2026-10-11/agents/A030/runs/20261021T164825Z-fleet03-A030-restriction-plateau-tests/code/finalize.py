from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
load=lambda n:json.loads((ROOT/'out'/n).read_text(encoding='utf-8'))
pilot,main,verify,lean=[load(n) for n in ['PILOT.json','VALIDATION.json','CONTINUATION.json','LEAN_RUN.json']]
assert pilot['status']==main['status']==verify['status']=='PASS'
assert (main['roots'],main['faces'],main['checks'])==(5796,17388,98616)
assert (verify['internal_tree_nodes'],verify['checks'])==(1023,6139)
now=datetime.now(timezone.utc).isoformat()
statement=('For any finite uniform physical controller partition (C_0,C_1,C_2) and independent Boolean cores u_j on disjoint private blocks having a common mean m, put q_j=E C_j, V=1-m^2, h_j=1-2C_j, F=u_kappa and phi(s)=-s log2(s), phi(0)=0. With L(q)=phi(q^2)-phi((1-2q)^2)/4+2q(1-q), H(F)=sum_j q_j H(u_j)+(V/4)sum_j H(h_j)+V sum_j L(q_j). For every actual controller coordinate i, R=V sum_j phi(q_j), E_i=D_i(F)-(V/4)sum_j D_i(h_j)-(R-E R_child) obeys E_i<=14 Inf_i(F), uniformly in all controller/core dimensions and m in [-1,1]. If r_j are supplied C-priced own-history controller potentials under ONE common controller policy, the original P=(V/4)sum_j r_j plus R is a (C+14)-priced controller potential retaining both actual child continuations. More exactly D_i(F)-C Inf_i(F)-(P+R)+E(P_child+R_child)=E_i-s_i, with s_i the actual nonnegative unused cut-transaction slack. At the surjective table (0,0,0,0,1,1,1,2), three independent two-bit point-defect cores of mean 1/2, query 2 and subsequent order 0,1 at C=1, s_i=3/16 while E_i-s_i=(27/64)log2(3)-9/16 lies strictly between 1/10 and 7/64. A separate exact ten-bit mixed-tree certificate with both actual initial data children verifies original P+R+sum q_j Q_1(u_j) at price15 on all1023 internal nodes and zero terminal reserves. No arbitrary unequal-mean continuation, shared-core extension, initial cut-reserve admission, universal FEI bound or Lean certificate is asserted. This adds an equal-mean correction and exact non-flat transaction to the existing A030 three-state cut-reserve candidate; the previous version remains preserved at its original scope.')
claim={
 'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':2,
 'exact_statement':statement,
 'hypotheses':['Finite uniform cubes; actual Boolean sign cores; all entropies bits','Three exclusive labels; zero-probability and constant endpoints allowed','Independent disjoint private data blocks; common current core mean for the analytic controller theorem','ONE prescribed own-history controller policy and inherited C-priced cut potentials; C>=0','The finite mixed-tree certificate retains its unequal-mean sibling but does not extend the analytic hypothesis','Existing v1 scope preserved; this version adds the specified diagonal correction only'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A030; harmonic cut reserve and rarity accounts credited to A064/A038 and original A030 v1'],
 'proof_source':['PROOF.md','code/check.py','out/VALIDATION.json','code/verify_continuation.py','out/CONTINUATION.json'],
 'proof_dependencies':[{'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':1,'scope':'Original harmonic cut interface; its three-label weights and physical coupling are explicitly reconstructed here. No imported DATA payment is needed for the new analytic controller theorem or finite certificate.'}],
 'review_records':[],
 'status':'ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW; LEAN_RUNTIME_UNVERIFIED',
 'supersedes':[{'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':1,'scope':'Additional equal-mean correction and finite transaction; old report and old scope preserved'}],
 'refutes':['On the declared non-flat surjective witness, E_i<=s_i (no additional controller price from the original P+R transaction)'],
 'first_unproved_line':None,
 'next_consumers':['A029','A064','A087','A091','A094','B06']}
(ROOT/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
next_action='Price unequal-mean coherent empty-private Fourier rows after one further DATA query from the SAME remaining account, retaining all three cut continuations and both full terminal costs; A087/A094 independently review the equal-mean proof and exact debt.'
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B06','packet_id':'A030',
 'gap_id':'G-R-MISMATCH','attempt_id':'A030-stage6-equal-mean-signed-correction',
 'method':'Fourier-sector cancellation; global scalar Lipschitz bound; actual controller-edge coupling; exact exhaustive surjective census; independent direct-character reconstruction; SAME-bank physical continuation',
 'mathematical_delta':'Arbitrary-dimensional equal-mean three-state correction E<=14Inf; actual unused slack alone fails by (27/64)log2(3)-9/16>1/10; one complete mixed physical tree paid at15 with both children and original cut/core/rarity accounts. No universal FEI implication claimed.',
 'deliverable_status':'COMPLETE_LOCAL; independent review and supervisor copying pending',
 'mathematical_status':'SCOPED_ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES; FULL_FEI_OPEN; LEAN_RUNTIME_UNVERIFIED',
 'claim_versions_used':[{'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':1,'scope':'Original harmonic cut interface, reconstructed for common means'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':2}],
 'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/VERIFY_SPEC.json','out/PILOT.json','out/VALIDATION.json','out/CONTINUATION.json','out/LEAN_RUN.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Universal unequal-mean coherent-row payment and initial inherited cut reserve admission unpaid','Lean compiler attempt returned no exit/output within runtime; no formal target verified','Independent review, registry adoption and remote mirror receipts unobserved'],
 'packet_ids':['A030']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A030 stage6: equal-mean controller correction and an unpaid local surplus

## exact target, quantifiers, hypotheses and units

For every finite uniform controller cube, three exclusive labels, and three independent Boolean cores on disjoint private cubes with common current mean m, bound the actual signed controller correction using the original three cut potentials and rarity bank. There is no bound on dimension or on the shape of any core spectrum. Entropy is in bits; physical influence is uniform flip disagreement. The analytic result is E_i<=14 Inf_i(F). The explicit finite mixed continuation retains its unequal-mean sibling and full core terminal costs. Initial cut-reserve admission and full FEI remain OPEN. This extends the existing A030 candidate, rather than opening another broad universal candidate while review is pending.

## sources actually read, revisions and theorem locators

Read the complete execution protocol revision {protocol['revision']}, current campaign entry/status/registries/packet/actions, campaign plan and supplement; the B06 board block is supervisor snapshot2026-10-21 16:43UTC and STREAM_NOTES is unchangedv2. The original lead plateau-amplification target was completed in earlier stages. Continue the actual saved non-flat three-cut frontier, rather than repeat plateau, tree telescope or bounded-depth statistics results. Read A030 stage5 REPORT/PROOF/CLAIMS (20261014T062839Z), A028 stage5 REPORT (20261014T051435Z), A029 stage5 REPORT (20261014T055200Z), and A087's scoped binary-transfer acceptance (20261014T045317Z). A028/A029 conservation is context, not an entropy payment premise.

Read threshold38pp Section8.2 Proposition8.6 (75)--(79), threshold29pp Proposition7.1 (64)--(67), and the percolation30pp/31pp theorem statements and scope. The percolation comparison supplies no universal restriction payment and is not a dependency. Source bytes, encodings, hashes and target line locators for43 files are in out/SOURCE_RECEIPTS.json; targeted source excerpts are saved separately. Paper text uses explicit cp1252 where UTF-8 decoding fails on the source soft-hyphen byte; no source was changed. The initial default PowerShell display had mojibake; all later analysis uses explicit encodings.

The session wake reported stale owner-model/state-of-mind notes; this was reported before using them and neither note is a mathematical premise. The math-store query found no controller-specific answering card and no recall result is adopted as a theorem. Several later fleet05 directories contain no reports: the last substantive A030 source is October14, not an automatically dated empty stage. No shared source, brain store, board, registry or other agent folder was modified.

## complete derivation or exact first unsupported line

PROOF.md is the complete analytic derivation. Put V=1-m^2, h_j=1-2C_j, q_j=E C_j and phi(s)=-s log2(s). The private-empty Fourier sector is exactly the constant m because all core means agree. All nonempty private sectors are disjoint. Expanding their actual coefficients gives

H(F)=sum q_j H(u_j)+(V/4)sum H(h_j)+V sum L(q_j),

where L(q)=phi(q^2)-phi((1-2q)^2)/4+2q(1-q). This identity is exact for arbitrary core spectra. The derivative extends continuously at0,1/2,1 and has |L'|<=55/8<7: use |x ln x|<=1/e, e>=8/3 and ln2>=2/3. Coupled physical controller endpoints give ||q_child-q||_1<=t, where t is their changed-label probability. The old rarity release is nonnegative and actual influence is d=Vt/2. Hence E<=7Vt=14d, including V=0 and t=0 without division.

With supplied original C-priced cut potentials, P=(V/4)sum r_j, so P+R pays controller queries at C+14. The exact local identity is D_F-Cd-(P+R)+E(P_child+R_child)=E-s, with s the actual unused cut-transaction slack. A complete control-only tree retains sum q_j H(u_j) in its terminals. No new root bank or core FEI certificate appears.

At labels(0,0,0,0,1,1,1,2), three independent two-bit point defects of common mean1/2, query2 then0,1, and C1: d=3/8, E=-3/8+(27/64)log2(3), s=3/16, and E-s=-9/16+(27/64)log2(3) in(1/10,7/64). Thus even the actual positive unused cut slack is insufficient at this genuinely non-flat surjective query. All terminal core entropies2 and influences1 remain. The extra influence rate required at this node is exactly(9/8)log2(3)-3/2>0. This is a scoped failure of the declared no-extra-price local transaction, not an FEI counterexample or failure of every global transfer.

A ten-bit predecessor uses a first core of mean1/4 with point-defect and padded-dictator children; its initial DATA query reaches both means(1/2,1/2,1/2) and(0,1/2,1/2). The SAME original harmonic cut account, rarity account and weighted core reserves pay a full1023-internal-node fixed physical continuation at15, retaining both actual siblings and all1024 constant leaves. The unequal sibling is verified on this finite tree only.

First unsupported universal line: pay the coherent empty-private rows when a DATA query makes the three core means unequal, using the SAME remaining original account, all cut continuations and both full terminals. A separate inherited initial cut-reserve admission is also still unpaid. The core-disjointness and equal-mean hypotheses are both used, and exact shared-core/unequal-mean countercontrols demonstrate that the identity cannot simply omit them. The analytic theorem is an author-checked proof pending independent reconstruction; it is not Lean-checked.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json predates the pilot and full census. Command from A030: python -X utf8 runs/{ROOT.name}/code/check.py --pilot; then the same without --pilot. Pilot18 roots/54 faces/{pilot['checks']} exact assertions PASS in{pilot['elapsed_seconds']:.6f}s. Main all5796 surjective three-bit label maps, no symmetry quotient, common-mean point-defect triple:17388 faces/98616 assertions PASS in{main['elapsed_seconds']:.6f}s. All18 pilot roots and11 selected main roots use complete raw-cube FWHT; the rest use an independently expanded exact Fourier-sector formula. The main finite maximum E/d is (9/8)log2(3)-1, not a claimed universal optimum. Scalar analytic bounds supply the all-dimensional extension.

Arithmetic is integer Walsh, Fraction probabilities, rational coefficients of prime logarithms, exact prime-factor zero decisions, and40-term rational atanh intervals with explicit geometric tail. No floating sign decides a result. Main includes{main['certified_sign_decisions']} certified nonzero sign decisions and{main['exact_zero_decisions']} exact-zero decisions. Boundary means are +/-1,0,1/2; arbitrary endpoints are covered by the analytic proof, not this finite list.

out/VERIFY_SPEC.json predates the independent continuation test. Command: python -X utf8 runs/{ROOT.name}/code/verify_continuation.py. Final PASS:{verify['checks']} assertions,{verify['internal_tree_nodes']} internal physical nodes in{verify['elapsed_seconds']:.6f}s. Selected spectra are independently reconstructed by direct character sums instead of FWHT; all same-account local inequalities retain both siblings. An extra exact sign check for E-s was added after the first6135-assertion pass, preserving the same domain; the final6139-assertion pass is the reported output, not an additional independent full test.

Expected memory180MB for each exact checker, observed peak unmeasured; no job expected to exceed300MB was launched. Pilot/main runtime guards55s/300s; verification55s. No GPU, new worker, detached job, automatic dimension growth or other-agent process action. For the core-only Lean attempt, fresh memok exited0 (physical9.1GB, commit22.7GB free). Command is reproduced by code/run_lean.py; named source/hash and allowed-axiom requirements were supplied, output confined to this run. The wrapper returned RUNTIME_UNVERIFIED after63.532s with no compiler exit code or output; target identity/axioms are unverified. It was not retried. Even a pass would certify only the natural-number price-conversion lemma, not the real logarithmic entropy theorem. No formal certification is claimed.

## proof dependencies and changed downstream conclusions

The new scalar collapse, Lipschitz payment and finite mixed certificate are self-contained; the prior three-state harmonic cut interface is explicitly reconstructed at the equal-mean slice. The old source remains intact. The new version2 adds this scope and keeps earlier claims at their original scope; it does not adopt an unreviewed general mixed-query theorem. A087's prior binary acceptance remains contextual and is not represented as acceptance of this extension.

A029/A064/A087 now have an actual non-flat three-state controller payment in arbitrary controller dimensions while means agree, plus a once-owned unused-slack failure of size>1/10 and an inherited-bank finite mixed continuation. They cannot infer that bank conservation alone pays unequal-mean rows, that terminal reserve value is free surplus, or that a full finite case supplies universal admission. No full-FEI status or constant changes.

## one next mathematical action and independent reviewer

{next_action} Use a perturbation of the equal-mean scalar identity that retains the actual coherent empty-private Fourier rows, rather than optimize the finite constant or repeat plateau tests. A029/A064 should compare the exact remaining debt against their signed child account; saved files are the handoff, with no message or external acceptance claimed.

## actual persistence receipts or precise save blocker

The four protocol artifacts, PROOF.md, both frozen specifications, reproducible code, pilot/main/continuation outputs, source receipts and failed Lean receipt are locally saved. The finalizer verifies exact protocol field sets, identical PROGRESS/PACKET_DELTA, statement hash, output counts, all files<20MB and two-line STATUS. out/PERSISTENCE_RECEIPTS.json contains actual current artifact sizes/hashes. WORKLOG and LEARNED append this stage. No local save blocker. Independent review, supervisor copying, registry adoption and remote mirror verification are pending; local persistence does not imply any of them. The current user deadline23Oct14:49UTC supersedes older static21Oct protocol dates; no schedule is changed.

## Universal bridge

This stage advances C019 stopping-tree payment through C024 history transfer by paying the exact three-cut coherent correction at14 times actual controller influence for arbitrary-dimensional equal-mean independent cores, and by preserving the original cut/core/rarity accounts on one complete mixed physical continuation. The exact positive remainder after actual unused slack, (27/64)log2(3)-9/16>1/10, identifies the source transfer that a universal proof must still fund. Unequal-mean coherent rows and initial inherited cut-reserve admission remain unpaid, so full FEI is OPEN. NEXT perturbs the explicit paid scalar identity at the first unequal-mean DATA exposure while retaining both terminals; that attacks the universal history bridge directly instead of producing another isolated plateau or class estimate.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A030 stage6 saved: all-dimensional equal-mean E<=14Inf;5796 surjective maps/98616 checks and1023-node same-bank mixed tree/6139 checks PASS; unused-cut-slack residual>1/10; review pending; FEI OPEN.\nNEXT: Price unequal-mean coherent rows after next DATA query from SAME remaining account, all3 cut continuations and both terminals; A029/A064/A087/A094 review. Lean runtime unverified.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{now} {ROOT.name}: recovered actual October14 source (later fleet05 run directories empty); derived all-dimensional equal-mean three-cut correction E<=14Inf;5796 surjective maps/98616 exact assertions PASS; positive unused slack3/16 still leaves (27/64)log2(3)-9/16>1/10. Independent character-sum and full same-bank ten-bit continuation6139 checks/1023 internal nodes PASS at15, both siblings retained. Core Lean attempt RUNTIME_UNVERIFIED; no formal certificate or universal FEI claim. Unequal means and initial cut admission remain unpaid; all run artifacts saved for A029/A064/A087/A094.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\nEqual core means m collapse the empty-private Fourier sector to constant m for ANY physical controller dimension and arbitrary disjoint independent core spectra. With V=1-m^2, q_j=E C_j, h_j=1-2C_j and L(q)=phi(q^2)-phi((1-2q)^2)/4+2q(1-q), H(F)=sum qH(u)+(V/4)sum H(h)+Vsum L(q). Continuous derivative obeys |L\'|<=55/8<7; coupling child label distributions gives E_i<=14Inf_i(F) after original rarity release. Original P+R therefore pays controller-only continuation at C+14; core terminals remain explicit.\n\nAt table(0,0,0,0,1,1,1,2), three two-bit point-defect cores m1/2, query2 then0,1,C1: actual unused cut slack3/16 is insufficient; E-s=(27/64)log2(3)-9/16 lies in(1/10,7/64). Full terminal core entropy2 each and weighted Q1 core reserve3/2 cannot be silently spent again. A non-flat predecessor and BOTH data children admit one exact complete1023-node same-bank tree at15; no universal unequal-mean history result follows. The equal-mean identity fails on explicit unequal-mean and correlated/shared-core controls. Core Lean attempt produced no compiler result; formal status unverified.\n')
expectedp={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
assert set(progress)==expectedp
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('This stage advances C019')
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=AGENT/name;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_at':now,'schema_validation':'PASS','local_only':True,'files':receipts},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'COMPLETE_LOCAL','artifact_count':len(receipts),'schema':'PASS','claim':claim['claim_id']+'@2','fei':'OPEN','independent_review':'PENDING','lean':'RUNTIME_UNVERIFIED','root':str(ROOT)},indent=2))
