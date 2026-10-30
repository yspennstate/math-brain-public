from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
read=lambda p: json.loads(p.read_text(encoding='utf-8'))
write=lambda p,x: p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
V=read(R/'out/VALIDATION.json'); assert V['status']=='PASS'
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
req=protocol['required_per_run']
statement='For the GMP26 Proposition 5.1 family F_k with selector children OR of k disjoint AND3 blocks and its specified one-minimal-positive-point deletion, the explicit complete selector-first computing tree described in DERIVATION.md has signed Cov(T)<=16 I(F_k)/3 for k>=2; WWW14 therefore gives H(F_k)<26 I(F_k) for every k>=1. This is a narrow primary-source application, not a universal paid-tree theorem or an improved constant over the prior 23-rate repair.'
hyp=['Uniform physical cube and sign-valued Boolean functions','Bits for spectral entropy','The precise minimal-positive-point edit and complete leaf refinement in DERIVATION.md','Source protocol is WWW14 arXiv:1312.3003v1 Lemma1.5/Section2.3; all leaves constant']
claim=dict(claim_id='A093-WWW14-GMP-COMPLETE-TREE-AUDIT',version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 contributors=['A093 (source-audit application)','Wan--Wright--Wu (prior protocol)','Gonzalez--MacManus--Pereyra (prior Boolean family)'],
 proof_source=['DERIVATION.md','code/audit_www.py','out/VALIDATION.json','https://arxiv.org/pdf/1312.3003v1'],
 proof_dependencies=['WWW14 Lemma1.5 and Section2.3 protocol; independent payment reconstruction in DERIVATION.md','Elementary covariance perturbation and complete physical-tree telescopes'],
 review_records=[],status='ANALYTIC_SOURCE_APPLICATION_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],
 first_unproved_line='No gap asserted for the displayed family calculation; independent review and formal check remain separate. A universal finite paid-tree/covariance-selection bound and retained terminal/reference transfer are unproved.',
 next_consumers=['B19 lead','A090','A085','A028','A061','A064','A095','A096','A097','A099','A100'])
assert set(claim)==set(req['claim_fields']); write(R/'CLAIMS.json',[claim])
formal='Not Lean-certified. See out/FORMAL_STATUS.json for any admission or execution receipt.'
P=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B19',packet_id='A093',gap_id='G-R-MISMATCH',attempt_id='A093-WWW14-primary-whole-tree-audit-v1',
 method='Read primary theorem versions; independently reconstruct signed variance/covariance tree payment; exact rational physical-tree and Walsh checks on the actual GMP family',
 mathematical_delta='Explicit complete selector-first GMP tree covariance <=16I/3 and source-code FEI rate<26; this pays the forced locally bad query. Source read-count/depth/terminal hypotheses preserved; prior23 rate is stronger and unchanged.',
 deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY',mathematical_status='NARROW_SOURCE_APPLICATION_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 claim_versions_used=['WWW14 arXiv:1312.3003v1 Lemma1.5, Lemma2.5, Section2.3','Shalev arXiv:1806.03646v2 Theorem9 and Theorem31 (scope/overlap only)','GMP26 arXiv:2606.00246v2 Proposition5.1 family; prior A093 source audit'],
 claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['REPORT.md','DERIVATION.md','CLAIMS.json','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json','code/audit_www.py','code/finalize.py'],
 next_consumers=claim['next_consumers'],next_action='A090/A085 independently reconstruct the edited-tree perturbation and actual protocol occupancy. Then compare its signed complete-tree payment with one inherited mixed query at the original reference, both full terminals and old debits retained.',
 stagnant_substantive_attempts=0,blockers=['Full FEI remains open','No independent acceptance, shared-index adoption, mirror verification or downstream use inferred','Earlier source-correction candidates remain pending; no third broad universal candidate opened',formal],packet_ids=['A093'])
expected={x.split(' (')[0] for x in req['progress_fields']}; assert set(P)==expected
write(R/'PROGRESS.json',P); write(R/'PACKET_DELTA.json',P)
report=f'''# A093 B19: primary whole-tree funding audit

## exact target, quantifiers, hypotheses and units

Determine whether the primary decision-tree literature supplies a complete account for GMP26's actual Boolean family whose prescribed selector decrement/influence ratio diverges. Every k>=1 is included analytically. The cube is uniform, outputs are signs, entropy is in bits, and covariance is signed physical sibling covariance. Full FEI remains OPEN. This is a literature audit with a narrow application; no first-result or latest-best claim is made.

## sources actually read, revisions and theorem locators

Read the current BOARD (22 October 22:07 UTC), B19 STREAM_NOTES v2, own rolling files and the prior A093 reports/derivation/code. Read execution-v2 and the campaign indices/supplement; their earlier endpoint is superseded for this invocation by the user's direct 23 October endpoint. The source-baseline identities and prior literature audit are retained, not reopened as new discoveries. The packet index is an old snapshot; its empty adoption entry is not evidence that prior work did not happen.

The new primary checks are [WWW arXiv:1312.3003v1](https://arxiv.org/pdf/1312.3003v1), Theorems1.1--1.2, Lemma1.5, Section2.3/Lemma2.5 (PDF pp4,11--13), Definition2.1 and AppendixE; and [Shalev arXiv:1806.03646v2](https://arxiv.org/pdf/1806.03646v2), Theorem9 and Section6.2/Theorem31 (pp6,23--24). WWW's primary version page lists only v1 submitted 11 December2013; Shalev lists v1 10June2018 and v2 24January2019. No withdrawal is indicated on these inspected pages. The arXiv-rendered WWW PDF title date says June18,2021, whereas the author-hosted copy says December9,2013; a rendered date alone does not establish a mathematical revision. Retrieval hashes/status are in out/SOURCE_RECEIPTS.json. Corrections or published-version differences beyond these inspected versions remain outside this bounded audit.

The source overlap is precise: WWW supplies the prior whole-set path code and read-k/expected-depth results. Shalev supplies the later O(sqrt(k)) result already recorded in campaign C017. Read count means all occurrences in the tree; the expected-depth FEI theorem explicitly assumes I>=1. The covariance protocol itself has no such influence restriction. These facts do not settle the best known constant or full FEI.

## complete derivation or exact first unsupported line

DERIVATION.md reconstructs the complete covariance account and gives its application. For the natural short-circuit tree computing f_k=OR of k AND3 blocks, C_k=4(7/8)^(k-1)[k-8(1-(7/8)^k)]. Refining its unique positive leaf containing the deleted point yields a complete tree for g_k. A one-point edit changes each old ancestor's reach-weighted covariance by at most8epsilon, so C_g<=C_k+24k epsilon. The exact selector covariance is4r(1-r-epsilon). Together these give Cov(T_F)<=16I(F_k)/3 for k>=2 and hence H(F_k)<26I(F_k) via the primary ternary protocol. The k=1 boundary is paid by H<=4 and I=1/2. The earlier pending23-rate repair is stronger; this application identifies the whole-tree mechanism and does not improve that bound.

Independently, the protocol's expected length is2 sum_v reach(v)Var(f_v). At every split Var(f_v)=2Inf_query+Cov(children)-(mean_plus-mean_minus)^2/4. Complete influence and mean-square telescopes give sum reach Var=2I+Cov(T)-Var(f). This is a reconstruction of the source payment, not a new universal resource. An incomplete tree retains both terminal influence/variance terms, and its terminal spectral entropy remains unpaid.

The first unsupported universal line is a dimension-independent selected complete-tree covariance/occupancy bound for arbitrary Boolean functions, or applying the complete-tree code to nonconstant stopping leaves without encoding their spectra. A bad local selector rate alone refutes neither possibility. AND_n separates expected depth from influence; parity makes covariance negative; an irrelevant prefix makes EVERY-tree covariance payment false with unchanged core H and I.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications are in out/FROZEN_SPEC.json; the explicit GMP grid amendment records that the initial invocation had already been submitted. The final replay uses the complete specification and unchanged declared finite domains. Run `python -X utf8 code/audit_www.py`: GMP k=1..12 rational recurrences, direct k=1,2,3 Boolean trees/spectra up to10 total bits, AND/parity n=1..8 spectra with n<=12 formulas, stopped AND2 and irrelevant-prefix controls. The direct checks validate every constant leaf, no repeated query on a path, local covariance identity, aggregate occupancy identity, edit perturbation and root influence independently of the compressed formula. All {V['exact_assertions']} exact assertions PASS; Python runtime {V['runtime_seconds']:.3f} seconds. The logarithmic26 bound uses integer3^11<2^18. No floating sign, automatic dimension increase, heavy search or GPU is used. {formal}

## proof dependencies and changed downstream conclusions

The explicit funding application depends on WWW's coding inequality and elementary physical covariance algebra; it does not consume the earlier pending23-rate correction as a proof premise. Earlier A093 corrections remain pending independent review and unchanged. This source audit does not open another broad universal candidate. It identifies why the forced-selector obstruction is compatible with a paid complete tree and preserves C019's terminal and single-use obligations. No shared index or other agent file was changed.

## one next mathematical action and independent reviewer

A090/A085 should reconstruct the edited-tree perturbation and actual source-protocol occupancy from the present formulas and code. A028/A061/A064/A095/A096/A097 can compare that signed bill with one inherited mixed query at the SAME original reference, retaining both full terminals and old bookings. The mathematical test is whether the positive residual is actually paid from unused ancestor capacity; covariance alone is neither nonnegative nor an automatic reusable balance.

## actual persistence receipts or precise save blocker

The four required protocol files, derivation, frozen specification, code and exact validation are saved under this run. STATUS.md has two lines; WORKLOG.md and LEARNED.md append only inside A093. out/ARTIFACT_RECEIPTS.json records local hashes and schema checks. Wake warned that identity notes were stale; current task files controlled. The compute snapshot showed memory pressure and very low disk space, so computation stayed small. No work was killed. Local save is distinct from supervisor copy, brain ingestion, external review and downstream use; those remain unverified.

**Universal bridge:** C019 gains an explicit complete-tree covariance payment on the actual GMP forced-selector family, plus a source-bound distinction between protocol occupancy and physical query depth. This resolves the previous stage's literature question without claiming a new best class constant. A universally paid selected tree or same-reference inherited-query/reset invariant is still missing. The shortest NEXT is to compare the signed occupancy bill at one mixed query against the same unused ancestor account, with both full terminal spectra and all earlier debits retained; another isolated class constant would not pay that universal step.
'''
for field in req['report_fields']: assert '## '+field in report
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A093 WWW14 whole-tree audit saved: GMP selector-first Cov<=16I/3 gives H<26I; exact controls PASS; prior23 stronger; review pending; full FEI OPEN.\nNEXT: A090/A085 review edited-tree perturbation/protocol occupancy; compare signed payment at inherited mixed query with SAME reference, both full terminals and old debits.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(f'\n{now} | WWW14/Shalev primary theorem audit; explicit GMP full-tree covariance funding, <26 FEI rate (weaker than prior23). {V["exact_assertions"]} rational assertions PASS. Same-reference universal transfer remains open. No priority claim or external adoption.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(f'\n{now} | WWW14 source protocol: L<=4I+2Cov, H<=log2(3)L+2I; complete T has sum reach Var=2I+Cov-Var. Cov is signed. Natural OR_k(AND3) tree C=4(7/8)^(k-1)[k-8(1-(7/8)^k)]. Minimal-positive deletion refinement changes covariance <=24k8^-k; complete selector-first tree Cov<=16I/3 (k>=2), source rate<26. Earlier23 is stronger; this is a funding explanation. Expected-depth theorem assumes I>=1; read-k counts total tree occurrences; Shalev v2 Theorem31 already gives2sqrt(k)I. Stopped leaves keep spectral entropy. No novelty/best-result claim.\n')
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes(); assert len(data)<20*1024**2
        receipts.append(dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data)))
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write(R/'out/ARTIFACT_RECEIPTS.json',dict(at_utc=now,protocol_fields='PASS',claims_fields='PASS',packet_compatibility='PASS',status_two_lines='PASS',files=receipts,remote_copy='UNVERIFIED',independent_review='PENDING'))
print(json.dumps(dict(status='SAVED',run=str(R),exact_assertions=V['exact_assertions'],files=len(receipts),full_fei='OPEN')))
