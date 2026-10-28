from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
OLD=ROOT.parent/'20261022T205915Z-account03-A028-stopping-tree-payment'
BASE=Path('~/brain_workers/FEI100_20261011')
PROTOCOL=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):write(p,json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=read(ROOT/'out/check_full.json');pilot=read(ROOT/'out/check_pilot.json');ind=read(ROOT/'out/independent.json');fix=read(ROOT/'out/fixture.json')
assert all(v['status']=='PASS' for v in (main,pilot,ind,fix))
assert (main['roots'],main['queries'],main['assertions'])==(6628,17116,1666968)
assert (pilot['roots'],ind['nodes'],ind['leaves'])==(480,166,84)
assert sha(ROOT/'code/check.py')==main['script_sha256']==pilot['script_sha256']
assert sha(ROOT/'code/exact_helper.py')==sha(OLD/'code/exact_helper.py')
assert fix['I_f']=='45/16' and fix['original_U']=='45/4' and fix['old_debit']=='1/8'
assert [p['leaves'] for p in fix['policies']]==[16,8]
assert any(q['Ef'] or q['Of'] for p in fix['policies'] for q in p['queries'])
prior=read(OLD/'CLAIMS.json')[0];claimid=prior['claim_id']
review_path=BASE/'agents/A029/runs/20261022T221752Z-account03-A029-child-deficit-transport/REVIEW_A028.md'
review_claim=read(review_path.parent/'CLAIMS.json')[0]
assert review_claim['statement_sha256']==prior['statement_sha256']
sources=[PROTOCOL,BASE/'BOARD.md',BASE/'claude/B06/STREAM_NOTES.md',OLD/'REPORT.md',OLD/'DERIVATION.md',OLD/'CLAIMS.json',review_path,review_path.parent/'CLAIMS.json',AGENT/'STATUS.md',AGENT/'LEARNED.md']
receipts=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sources]
dump(ROOT/'out/context_receipts.json',dict(read_scope='Current board/lead/status and prior candidate/source review; archived protocol/campaign/paper baseline inherited from preceding completed stage and reopened only for exact new dependencies',sources=receipts))
statement=('Version7 retains the version6 signed entropy sector and mixed JS telescope at its original scope and adds prescribed-profile reference transport. For every independent Boolean controller a and fully shared Boolean sources G,H on finite uniform cubes, with c=(1-a)/2, p=Ec, f=(1-c)G+cH, supply normalized source spectral references Rg,Rh positive on their true supports. At every physical history inherit each source reference through its own actual-phase pair-erasure/outcome channel for DATA queries and keep it fixed for CONTROL queries. Put q=(1-p)Pg+pPh, r=(1-p)Rg+pRh and prescribe Rf(U,t)=r(t)Pf(U,t)/q(t) on positive q rows, assigning all off-target row mass to U=empty. Write Df=D(q||r), W=(1-p)D(Pg||Rg)+pD(Ph||Rh), Z=W-Df>=0, A_v=W_v-E W_child>=0, sigma_v=E Df_child-Df_v. For EVERY finite adaptive mixed physical stopping tree, sum reach*sigma+sum reach*A+E Z_leaf=Z_root. The complete nonnegative entropy-decrement path cost plus both full terminal cross-entropies is H(f_root)+E Df_leaf <= H(f_root)+W_root = weighted original source CE+J_root+L_root. The erasure path cost is smaller. If Rg=Rh at root then Z_root=J_root exactly; all-control revelation attains sum reach*sigma=J_root, with no renewal even though inherited source references may differ. Relative to actual inherited output references, raw reset kappa_v=sigma_v+E_fv+O_fv, so only net reset after those actual erasure/outcome refunds is charged to Z. Old debit b requires original earmark U-b to cover the displayed full root allowance. Conditional on source CE rates Lg,Lh and the stated v5 surcharge premise Pi<=M*gamma*I(a)+(V/2)I(GH), the full payment is <=max(M,Lg+2p,Lh+2(1-p))*I(f). No payment for independently prescribed canonical targets or universal source certificate is asserted.')
claim=dict(claim_id=claimid,version=7,exact_statement=statement,
    hypotheses=['Finite uniform product cube; independent physical controller and data blocks; sources may share all data','Normalized source references positive on true support; preserve all off-target mass and actual branch normalizers','Source-specific physical reference inheritance, prescribed true conditional controller profile and specified zero-row completion','Both full child/terminal KL and CE terms retained; signed net reset transactions and actual output erasure/outcome refunds; no positive-part replacement','Any influence consequence additionally requires genuine source CE suppliers and scoped v5 surcharge premise; old debits deducted from original earmark'],
    statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A028','A026 (v6 balanced DATA precursor)','A029 (independent scoped v6 verification; no v7 repair or acceptance)'],
    proof_source=['out/DERIVATION.md','out/check_full.json','out/independent.json','out/fixture.json'],
    proof_dependencies=[{'claim':claimid+'@6','scope':'entropy sector identity and definitions; independently accepted at stated scope by A029; new KL identities proved from log-sum and chain rule'},{'claim':claimid+'@5','scope':'conditional influence corollary ONLY, surcharge premise retained; earlier bundled structural/reference clauses not accepted by the v6 review'}],
    review_records=[dict(reviewer='A029/account03',reviewed_version=6,verdict='HOLDS_SCOPED_V6_SECTOR_MIXED_JS_TELESCOPE_AND_QUANTITATIVE_JS_PRICE',scope='Version6 only; excludes earlier structural/reference bundles and all new version7 claims',source=str(review_path),source_sha256=sha(review_path))],
    status='V7_AUTHOR_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING; V6_SCOPED_REVIEW_HOLDS',
    supersedes=[dict(claim_id=claimid,version=6,reason='Narrow prescribed-profile KL reconstruction extension; prior scoped results retained, no universal terminal-target assertion')],refutes=[],
    first_unproved_line='Pay conversion from the prescribed conditional-profile targets to externally required terminal references from the SAME original allowance, and supply dimension-independent influence-priced source/controller certificates for every Boolean input.',
    next_consumers=['A029','A056','A087','A091','A094','A096','A097'])
dump(ROOT/'CLAIMS.json',[claim])
next_action='Starting from a paid profile reference, prescribe ONE changed nonempty conditional controller profile at an intermediate DATA child and bound its actual KL increase using the SAME unused Z/source contraction account with old debit and both terminal CE bills retained; A056/A029/A094 review.'
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B06',packet_id='A028',gap_id='C019',attempt_id='A028-v7-prescribed-profile-reference-payment',
    method='Conditional-label KL slack plus physical source erasure/outcome contraction; exact signed reference reconstruction telescope',
    mathematical_delta='Pays all mixed-history prescribed profile reconstructions from original source KL slack; common root reference makes that slack EXACTLY the already identified JS bank; full source/structural/reference terminal costs and old debit retained. Sharp all-controls stopping case. Canonical externally imposed reset/source universality remain open.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_AUTHOR_PROOF_EXACT_CHECKED; V7_INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
    claim_versions_used=[claimid+'@6 (A029 scoped independent acceptance)',claimid+'@5 (conditional surcharge premise ONLY)'],claims_created_or_changed=[claimid+'@7'],
    source_artifacts=['out/DERIVATION.md','out/FROZEN_SPEC.json','out/FROZEN_FIXTURE.json','out/context_receipts.json','out/check_pilot.json','out/check_full.json','out/independent.json','out/fixture.json'],
    next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
    blockers=['No universal influence-priced source CE suppliers','Conversion to externally prescribed terminal references is not included','New version7 independent acceptance pending; conditional v5 surcharge not covered by A029 scoped v6 acceptance','No Lean entropy formalization or remote mirror verification claimed'],packet_ids=['A028'])
dump(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report=f'''# A028: original JS slack pays prescribed profile reconstruction

## exact target, quantifiers, hypotheses and units

For every finite Boolean mux f=(1-c)G+cH with arbitrary biased/nonpoint controller c on independent physical controls and fully shared data sources, pay one prescribed family of terminal-reference conversions through EVERY adaptive mixed restriction tree. Entropy, cross-entropy and KL are in bits; influence uses physical Boolean flips. This stage closes the prescribed-profile transport lemma, not universal C019 or FEI. The full expected nonnegative entropy path plus terminal CE is bounded by weighted original source CE+J+L. Source CE suppliers and a root surcharge estimate give the explicit conditional influence rate in the derivation. Independently required terminal targets remain outside the theorem.

## sources actually read, revisions and theorem locators

Execution protocol v2 was read in full, with current user dates governing the campaign clock. Current BOARD, B06 STREAM_NOTES v2 and own rolling status were read at stage intake; B06 lead's arbitrary-controller request was completed in v5/v6 and is not restarted. The prior v6 REPORT/DERIVATION/helper and previous proof chain supply the accepted finite source baseline, including campaign registries, supplemental notes and four local paper texts. Those older sources were not newly re-audited wholesale this stage. Current A029 REVIEW_A028.md and CLAIMS.json independently accept exactly the v6 sector/JS telescope and quantitative JS price; they explicitly exclude earlier structural/reference bundles. Current A021/A056 durable notes were consulted as context for retaining real child KL terms and prescribed-target scope, not as proof premises. Source pins are in out/context_receipts.json. No external literature search, brain write, publication or message was used.

## complete derivation or exact first unsupported line

The complete all-dimensional proof is in out/DERIVATION.md. Let Pg,Ph be source spectra and Rg,Rh their normalized references, positive on true support. At each history set q=(1-p)Pg+pPh, r=(1-p)Rg+pRh. The output spectrum Pf(U,t) has data marginal q. Prescribe Rf(U,t)=r(t)Pf(U,t)/q(t), assigning all q=0 row mass to U=empty. This preserves every off-target reference atom. Then Df=D(Pf||Rf)=D(q||r), W=(1-p)D(Pg||Rg)+pD(Ph||Rh), and Z=W-Df is a nonnegative conditional source-label KL.

Source references inherit through their own actual-phase physical pair channels. At DATA nodes the exact source debt drop A=W-EWchild is the weighted sum of source erasure KL and D(fair||reference branch masses); at CONTROL nodes it is zero by affinity in p. Both child references are normalized by their actual reference branch masses. Thus A>=0. If sigma=E Df_child-Df, then sigma=Z-EZchild-A, and finite actual reaches give sum reach*sigma+sum reach*A+E Z_leaf=Z_root.

For actual output-reference propagation, kappa=average(D_target_child-D_inherited_child)=sigma+E_f+O_f. The physical erasure and outcome refunds E_f,O_f are displayed and retained. No assertion bounds raw positive resets by Z. The complete payment is sum reach*DeltaH+E CE_leaf=Hroot+E Df_leaf<=Hroot+Wroot=weighted source CE+Jroot+Lroot. DeltaH=B_i+JS_i>=B_i>=0, so the erasure path is also paid. At a common root source reference Rg=Rh, Zroot=Jroot EXACTLY; later source references may differ and the inherited Z replaces any renewed JS bank. Revealing all controls and stopping is sharp: A=0, Zleaf=0, net reset=Jroot. This combined ledger uses J once; it does not add two separately renewed entropy/reset payments.

If an old debit b exists, admission requires U-b>=Hroot+Wroot; Z is slack within this original allowance. Conditional on supplied CE source rates Lg,Lh and Pi<=M gamma I(a)+(V/2)I(GH), the full rate is max(M,Lg+2p,Lh+2(1-p)); in v5 M=K+3log2(e). No unreviewed v5 structural premise is promoted to accepted status here. The exact first unsupported universal line is payment for a conversion to externally imposed terminal references and dimension-independent source/controller CE suppliers for arbitrary Boolean inputs. Allowing the target reference to use the actual structural conditional spectrum does not prove either requirement.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded computation. Main enumerates all controller tables in dimensions0..1 and every ordered equal-dimension shared-source pair in dimensions0..2, with four ordered reference choices (uniform or half-true-plus-half-uniform). There is no symmetry reduction or automatic dimension growth. Pilot: {pilot['roots']} cases/{pilot['queries']} physical queries/{pilot['assertions']} assertions in {pilot['seconds']:.3f}s. Main: 6,624 enumerated cases plus four references on the predeclared seven-variable nonconstant fixture, total {main['roots']} roots/{main['queries']} physical queries/{main['assertions']} assertions in {main['seconds']:.3f}s. All PASS. Spectra/references/kernels are exact Fractions; entropy equality is prime-log vector equality; signs use outward rational 24-term atanh enclosures, not floating point.

Independent code imports neither main checker nor helper. Direct character sums and separately expanded conditional-label KL verify two mixed policies on a six-variable fixture: {ind['nodes']} nodes/{ind['leaves']} leaves/{ind['assertions']} assertions in {ind['seconds']:.3f}s. One policy is complete, the other adaptive and stopped; both full terminal KL terms remain. The independent frozen fixture was described broadly in the initial spec; its exact three-data-bit functions and adaptive stopping rule are fixed in code/independent.py before execution. These checks support implementations; the finite entropy-chain/telescope proof supplies the infinite-dimensional quantifiers.

The seven-variable fixture has I(f)=45/16. Original U=4I(f)=45/4 carries old debit1/8. Root admission reserve has exact prime-log vector 3/8+(765/512)log2(3)+(75/128)log2(5)+(121/512)log2(11)>0. The D0,C0,D1,C1 prefix retains16 complete terminals, and the three-control-only tree retains8; both are paid from that original allowance. Root Z=J=15/4-(15/32)log2(5)-(17/32)log2(17)>0. The latter policy attains the JS payment exactly. out/fixture.json stores every query normalizer, actual refunds and all terminal H/D/Z values. This finite influence receipt is a witness for the general ledger, not a new universal class bound.

Commands from this run: python -X utf8 code/check.py pilot; python -X utf8 code/check.py full; python -X utf8 code/independent.py; python -X utf8 code/fixture.py. Helper bytes are pinned to v6. Estimates160MB/100MB; peak memory was not measured, and no job expected above300MB was started. Pilot1.8s, main59.5s, independent0.6s, fixture0.2s; all within caps. Compute snapshot showed high shared CPU and only1701MB free, so verification stayed small and sequential; no work was stopped or throttled. No Lean proof or compiler run was performed or claimed.

## proof dependencies and changed downstream conclusions

Version7 extends the same pending A028 candidate, avoiding a new broad candidate. The KL transport itself uses Parseval, log-sum and KL chain rule, all reconstructed explicitly. V6 gives J+L notation; A029's acceptance is scoped to that earlier version. V5 surcharge enters only the conditional influence corollary. The new step is original conditional-label KL slack funding all prescribed mixed-history reconstructions, with Zroot=the SAME original J for common root references. Both full source bills, structural conditional entropy, old debits and actual output refunds survive. A056's more constrained compatible-reference work does not license arbitrary fresh targets here. Full FEI and externally prescribed-reference conversion remain OPEN.

## one next mathematical action and independent reviewer

{next_action} A029 should independently reconstruct common-reference sharpness and nonrenewal; A056 should compare the actual physical inherited output reference with the prescribed profile target; A094 should challenge the full original earmark with old debit and both terminals. These are saved consumer requests for supervisor routing, not sent messages.

## actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, exact/independent code and outputs are saved only in A028. PACKET_DELTA is byte-identical to PROGRESS; schema and statement hash are checked against protocol. Rolling STATUS has two lines; WORKLOG and LEARNED are appended. out/persistence.json will record file hashes and sizes; code/verify.py independently reads the package back, including nonempty counts and an actual refund-dropping rejection guard. Files are under20MB. Independent v7 review, supervisor copying and remote mirror acceptance remain unobserved. Brain self-care wake was degraded by stale owner-model and state-of-mind notes; those owner-context sources were not used for mathematical premises and remain unverified.

## Universal bridge

This stage moves C019 and C024 by paying an explicit all-history terminal-profile conversion, rather than only carrying the old entropy JS telescope: inherited source KL slack Z pays signed reconstruction after actual physical erasure/outcome refunds, and a common original source reference gives Zroot=Jroot sharply. Complete entropy/erasure path and terminal CE are retained at the same original supplied source-plus-J+L allowance, including prior debits; the conditional influence constant does not grow with depth or dimension. The remaining universal bridge is payment for externally required conditional-profile changes and genuine influence-priced source/controller suppliers. NEXT changes precisely that unpaid profile on an already paid history, so it attacks the missing universal transaction instead of another isolated class.
'''
write(ROOT/'REPORT.md',report)
write(AGENT/'STATUS.md','STATE: A028 v7 saved ALL mixed-history prescribed-profile reference payment from SAME original KL slack; common reference slack=original J sharply; exact checks PASS; v7 review pending; FEI OPEN.\nNEXT: A056/A029/A094 review; change one nonempty conditional profile after paid DATA history using SAME unused Z/source account, old debit and BOTH terminal CE retained.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{stamp} — {ROOT.name}: v7 prescribed profile-reference transport proved by conditional-label KL Z=W-Df and physical source E/O contraction. Common root reference Z=J, sharp all-controls tree; complete path+terminal CE<=weighted original source CE+J+L. Main6628 roots/1666968 assertions; direct-character independent166 nodes/4355 checks; old-debit nonconstant fixture3976 checks PASS. Externally prescribed profiles and universal source admission OPEN; v7 independent review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n## Stage7: original source KL slack pays prescribed profile reconstruction\n\nFor independent arbitrary controller and shared Boolean G,H, prescribe output reference Rf(U,t)=r(t)Pf(U,t)/q(t), q=(1-p)Pg+pPh, r=(1-p)Rg+pRh, completing zero true rows at empty control set without deleting off-target mass. Df=D(q||r), W=weighted source KL, Z=W-Df>=0 is conditional label KL. Inherit each source through its OWN actual-phase physical pair kernel (and actual reference branch normalizers). Source debt W is supermartingale: A=W-EWchild>=0, and A=0 on controls. Then sigma=E Dfchild-Df=Z-EZchild-A; EVERY mixed finite stopping tree has sum reach*sigma+sum reach*A+E Zleaf=Zroot. If original Rg=Rh, Zroot=Jroot exactly, with equality after all controls; descendant source refs need not coincide and cannot renew J. Raw actual reset kappa=sigma+E_f+O_f; the actual output erasure/outcome refunds must be retained. Full nonnegative entropy path+terminal profile CE<=Hroot+Wroot=weighted source CE+Jroot+Lroot. Z is inside this allowance, not extra money. Old debit b needs U-b to cover it. Externally prescribed target conversion and universal influence-priced source suppliers remain open. Scoped v6 acceptance by A029 includes JS price, excludes older structural/reference bundles; no v7 acceptance claimed.\n')
protocol=read(PROTOCOL)
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
keys=set(protocol['required_per_run']['progress_fields']);keys.remove('packet_ids (one primary ID, for compatibility)');keys.add('packet_ids')
assert set(progress)==keys
assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ('persistence.json','verify.json')]
assert all(p.stat().st_size<20_000_000 for p in files)
dump(ROOT/'out/persistence.json',dict(status='LOCAL_SAVED_HASHED',created_utc=stamp,files=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)) for p in files],mirror='UNVERIFIED',v7_independent_review='PENDING'))
print(json.dumps(dict(status='LOCAL_PACKAGE_WRITTEN',files=len(files),claim_version=7,full_FEI='OPEN')))
