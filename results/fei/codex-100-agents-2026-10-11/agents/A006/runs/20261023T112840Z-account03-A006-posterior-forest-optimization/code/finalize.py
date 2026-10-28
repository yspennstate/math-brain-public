from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent.parent;A=R.parent.parent;B=A.parent.parent
def rd(p):return Path(p).read_text(encoding='utf-8')
def wr(p,s):Path(p).write_text(s,encoding='utf-8')
def js(p,o):wr(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ident(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
S8=B/'agents/A008/runs/20261023T062437Z-account03-A008-gate-label-compression'
S10=B/'agents/A010/runs/20261023T110124Z-account03-A010-universal-residual-falsifier'
ids=['A008-RARE-CHILD-MOMENT-AND-FIXED-POLARITY-MIXTURE-OBSTRUCTION','A010-BOUNDED-MIXTURE-VARIATIONAL-RESIDUAL-OBSTRUCTION']
sources=[]
for directory,cid in zip((S8,S10),ids):
 c=next(x for x in json.loads(rd(directory/'CLAIMS.json')) if x['claim_id']==cid)
 assert ident(c)==c['statement_sha256'],cid
 sources.append(c)
js(R/'out/SOURCE_CLAIMS.json',sources)
checks=json.loads(rd(R/'out/CHECK.json'));pilot=json.loads(rd(R/'out/PILOT.json'))
overlap=json.loads(rd(R/'out/OVERLAP.json'));pair=json.loads(rd(R/'out/PAIR.json'));dp=json.loads(rd(R/'out/DP.json'))
assert all(x['status']=='PASS' for x in [checks,pilot,overlap,pair,dp])
assert checks['functions']==14 and checks['truth_inputs']==79076 and checks['actual_anchor_runs']==447308
assert pair['I']=='5/4' and pair['invalid_product_influence']=='3/2'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
js(R/'out/SOURCE_REVIEWS.json',[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'reviewer':'A006','verdict':'HOLDS_FULL_STATED_SCOPE_NO_REPAIR','source':'REVIEW_SOURCES.md','independence':'direct physical truth/certificate reconstruction, separate rational moment implementation; no source executable imports','timestamp_utc':now,'registry_adoption':'NOT_PERFORMED'} for c in sources])
pins=[B/'BOARD.md',B/'claude/B02/STREAM_NOTES.md',S8/'MIXTURE_OBSTRUCTION.md',S8/'CLAIMS.json',S8/'code/persist.py',S10/'MULTIREFERENCE.md',S10/'CLAIMS.json',S10/'code/finalize.py',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
js(R/'out/SOURCE_PINS.json',[{'path':str(p),'sha256_at_final_readback':sha(p)} for p in pins])
protocol=json.loads(rd(pins[-1]))
statement=('For every finite indexed family of nonempty physical supports, put t_j=2^(-width_j), rho=sum_j t_j and give each local subset law mass1-t_j to empty and t_j^2/(1-t_j) to each particular nonempty mask. Choose an actual anchor j with prior t_j/rho, force its local mask uniform nonempty and draw all other local masks independently in fixed order. The full physical-union output law is Q(A)=rho^(-1)sum_(z:union z=A)K(z)mu(z), normalized on nonempty physical sets; its optimal posterior is over the distinct actual pairs(anchor,local-mask-tuple), including allocation ambiguity. An exact two-array union/occupation dynamic program computes Q in O(2^n sum_j 2^width_j) rational operations. If the supports cover all relevant coordinates Q has full nonempty support. In particular for every finite nonempty list of positive clause widths w_j, U the product of disjoint OR clauses on those widths and F=2U(X)[1-U(-Y)]-1 on independent clones, the same anchor construction on both physical clause copies has complete nonempty actual-posterior cost C_Q(F)<155I(F)/24<7I(F). This is a new clause-mask reference, not an original-prime queue or a canonical partition-forest claim.')
hyp=['Uniform independent physical cube for the Boolean cost theorem; entropy and cost in bits.',
 'Local support instances, the anchor draw and the canonical subsequent local mask draws are actual random choices; aliases or shuffled descriptions of one draw tuple are not counted as distinct runs.',
 'The general pushforward normalizes for overlap, but its <7I payment requires the stated disjoint paired-clause Boolean family. No universal influence payment on arbitrary overlapping supports is asserted.',
 'The new reference has its own explicit priors and local probabilities and is not claimed to be a mixture or subfamily of the original prime queues.']
c=dict(claim_id='A006-NORMALIZED-SHARED-TAG-PUSHFORWARD-AND-PAID-CLAUSE-CODE',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256='',contributors=['A006'],
 proof_source=['SHARED_TAG.md sections1--5, including equation(2a) and the exact union/occupation recursion','code/check.py','out/CHECK.json','code/overlap.py','out/OVERLAP.json','code/pair.py','out/PAIR.json','code/union_dp.py','out/DP.json'],
 proof_dependencies=[],review_records=[{'reviewer':'A006','kind':'AUTHOR_ALL_PARAMETER_PROOF_AND_EXACT_FINITE_CHECKS','evidence':['out/CHECK.json','out/OVERLAP.json','out/PAIR.json','out/DP.json'],'acceptance':'INDEPENDENT_AGENT_REVIEW_PENDING','formal_status':'NOT_FORMALLY_CHECKED'}],
 status='AUTHOR_PROOF_EXACT_CERTIFICATES; INDEPENDENT_AGENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A008','A010','A009','A007','A086','Claude/B02','B20'])
c['statement_sha256']=ident(c);js(R/'CLAIMS.json',[c])
nextstep=('A008/A010 independently reconstruct the new sampler and <7I payment, then price full anchor-plus-allocation occupation on one shared-coordinate clause pattern using the exact union DP; retain the same supplied reference and actual posterior, and replace the false product-moment shortcut (5/4 physicalI versus3/2 surrogate). Do not claim success of r original prime queues.')
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B02',packet_id='A006',gap_id='G-J-COST',attempt_id='A006-stage10-normalized-once-anchor-shared-tag',
 method='New normalized anchor-size-biased clause-mask sampler, actual-run posterior refund, full physical-union probability DP and direct Boolean occupation payment.',
 mathematical_delta='Arbitrary finite support-cover normalization and exact rational physical-union DP; complete new-reference cost<155I/24<7I for all paired disjoint-clause widths/counts, including the source queue counterfamily. Exact overlap allocation control and physical5/4-versus3/2 moment failure. Two whole source obstructions reconstructed unchanged.',
 deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY',mathematical_status='NEW_SCOPED_AUTHOR_PROOF; REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=[s['claim_id']+'@'+str(s['version']) for s in sources],claims_created_or_changed=[c['claim_id']+'@1'],
 source_artifacts=['SHARED_TAG.md','REVIEW_SOURCES.md','FROZEN_SPEC.json','OVERLAP_SPEC.json','PAIR_SPEC.json','DP_SPEC.json','out/CHECK.json','out/OVERLAP.json','out/PAIR.json','out/DP.json','out/SOURCE_CLAIMS.json','out/SOURCE_REVIEWS.json'],
 next_consumers=c['next_consumers'],next_action=nextstep,stagnant_substantive_attempts=0,
 blockers=['Universal influence payment of tag, allocation and occupation cost for a suitable representation of arbitrary Boolean functions is open.',
 'The new <7I proof requires disjoint paired clauses; arbitrary overlapping-cover normalization alone does not price its cost.',
 'Unrestricted/r-clause-specialized ORIGINAL prime-queue mixtures remain unresolved by this new dictionary code.',
 'Fresh brain wake degraded: locked attachment/render failure and stale owner-model/state-of-mind/dream; affected notes were not mathematical evidence.',
 'New claim awaits independent review; shared/remote adoption unverified.'],packet_ids=['A006'])
js(R/'PROGRESS.json',progress);wr(R/'PACKET_DELTA.json',rd(R/'PROGRESS.json'))
wr(R/'REPORT.md',f'''# A006 stage10: a normalized once-per-set shared tag

## exact target, quantifiers, hypotheses and units

C020 whole-set witness cost after the original-prime queue route's actual Boolean obstructions. For ANY finite support cover, construct a new normalized actual-run law and an exact physical-union mass dynamic program. For EVERY finite nonempty list of positive clause widths, put U=product of the corresponding disjoint OR indicators and F=2U(X)[1-U(-Y)]-1 on two independent copies. The new code has complete nonempty cost C<155I/24<7I, including the source family with2^w equal-width clauses. Entropy is in bits; influence is physical flip influence. The cost proof needs this disjoint clause representation; normalization is valid with overlap. This is a new clause-mask reference, not an old prime-queue subfamily, not a canonical forest bound, and not full FEI. No novelty claim for FEI on read-once formula families is made.

## sources actually read, revisions and theorem locators

Fresh BOARD.md dated2026-10-23 11:24 UTC, B02 STREAM_NOTES.md v2 and A006 STATUS. The board already reports A009 arbitrary one/two connector blocks and A008/A010 original-queue obstructions; those replace the old connector NEXT. Read A008 run20261023T062437Z REPORT and the entire MIXTURE_OBSTRUCTION.md; A010 run20261023T110124Z REPORT, entire MULTIREFERENCE.md and exact CLAIMS; A009 run20261023T105539Z REPORT supplies dispatch/scope context, not an accepted proof dependency. Source builders' statement/hypothesis hash conventions were read. Original queue mechanics, campaign intake/registries/papers and machine instructions are inherited from prior source reads, not claimed freshly reread in full. Protocol revision{protocol['revision']} supplies exact fields. Source statements and identities are in out/SOURCE_CLAIMS.json; byte pins at finalization are in out/SOURCE_PINS.json and are not historical or remote receipts. A010's scoped acceptance of stage9 is consumed without rewriting stage9.

## complete derivation or exact first unsupported line

SHARED_TAG.md gives the full proof. For local width w_j let t_j=2^-w_j, empty-mask probability1-t_j, and each nonempty-mask probability t_j^2/(1-t_j). Choose an ACTUAL first anchor with prior proportional t_j, force its mask uniform nonempty, and sample the remaining local masks once in canonical order. On a disjoint paired output touching K clauses, every actual anchor joint mass is mu(A)/(2rho), so Q(A)=Kmu(A)/(2rho). This is normalized by E_muK=2rho. The actual posterior is uniform over its K different first anchor draws, giving the earned log K refund. No shuffled descriptions or aliases are counted as new runs.

For overlapping supports, use the complete pushforward Q(A)=sum_(union z=A)K(z)mu(z)/rho, summing actual anchor AND local-allocation events before taking the posterior. A two-array exact union/occupation recursion computes every mass in O(2^n sum2^width) rational operations. It supplies a normalized full-support law on any relevant-coordinate cover, but asserts no polynomial complexity or universal influence price.

For the disjoint paired Boolean family, write q=product(1-t_j), D=sum w_jt_j/(1-t_j). Direct indicators and physical pivots give I=2qD and the exact paired clause-occupation moment M_j=4qt_j. The complete cost is

    C=v[2sum(-log(1-t_j))+log(2rho)]+2sum M_j log((1-t_j)/t_j)-E_P log K.

Using v<=4q, the base plus occupation terms are bounded by8q sum h2(t_j). The elementary bound h2(2^-w)<(4/3)w2^-w/(1-2^-w) pays these by16I/3. The positive tag term is<9I/8 using D>=2rho, sup ln x/x=1/e, e>8/3 and ln2>2/3. Keeping or omitting only the NONNEGATIVE actual refund yields C<155I/24<7I. No known entropy of F is used to price this code. The original bounded-mixture obstruction remains true, since this sampler uses different dictionaries and local laws; success of r clause-specialized ORIGINAL queues is not established.

The honest first unsupported universal line is influence payment for a suitable shared-support representation under the full anchor-plus-allocation pushforward. Disjoint moment identities cannot simply be imported. The six-bit overlapping example has actual I=5/4 while the disjoint product surrogate is3/2. This falsifies the shortcut, not the new normalized reference or FEI. A universal representation/occupation theorem is still needed.

## executed validation with domain, arithmetic, commands and outputs

All jobs had frozen specifications before execution, no symmetry reduction or automatic dimension increase. Main commands: python -X utf8 code/check.py --pilot, then python -X utf8 code/check.py. Pilot PASS:5 functions,164 truth inputs,332 actual anchor runs,{pilot['assertions']} assertions in{pilot['seconds']:.6f}s. Main PASS:14 actual functions on the exact frozen width lists,79,076 direct truth inputs,447,308 distinct actual anchor runs,{checks['assertions']} assertions in{checks['seconds']:.6f}s. The pilot overlaps the main domain and is not added. Maximum physical dimension is16. Integer Walsh spectra, direct physical flips, complete nonempty output enumeration, actual conditional anchor draws and Fraction aggregation verify normalization, occupation identities, posterior uniformity and certified C<7I intervals. The negative control counting the K anchors twice has total mass>1, while the actual law sums to1. Direct code cost, pre-refund cost and earned-refund interval agree. Main also reconstructs complete positive/negative prime tables at source w1,w2, the rare-label transition invariant, rational offspring/root-product bounds, and integer budget inductions through w128. Source analytic proofs supply their all-w quantifiers.

Separate command python -X utf8 code/overlap.py follows OVERLAP_SPEC: all24 actual anchor events on two overlapping width-two supports, PASS:{overlap['assertions']} assertions. Center singleton mass is5/18, with four actual-run posterior weights9/20,9/20,1/20,1/20; collapsing the allocations incorrectly gives1/36. Command python -X utf8 code/pair.py follows PAIR_SPEC: all768 actual events and64 truth inputs for one overlapping paired function, PASS:{pair['assertions']} assertions. Direct character sums and physical flips certify I=5/4, rather than the invalid3/2 product surrogate, and a finite rigorous cost interval is saved. Command python -X utf8 code/union_dp.py follows DP_SPEC: independently implemented exact union DP agrees POINTWISE with24+768 distinct-anchor oracle events on every nonempty output of the two references; its pair-cost interval equals the saved direct-event interval. PASS:{dp['assertions']} recorded assertions. These checks do not prove a cost theorem for arbitrary overlaps.

All mathematical acceptance uses integers/Fraction and atanh log intervals with proved remainder/outward dyadic rounding; elapsed time alone is floating telemetry. Frozen memory estimates main120MB, controls20--25MB; pilot55s/full180s and controls10--15s. No job expected above300MB was started, so memok admission was not required. Jobs were sequential, bounded and below campaign limits; no GPU, detached worker, visible window, remote compute or Lean compiler. No formal-kernel acceptance is claimed. Source helpers are not imported; the small overlap cost/DP controls reuse only A006's own interval-arithmetic routine and distinguish that shared arithmetic from independent probability aggregation.

## proof dependencies and changed downstream conclusions

REVIEW_SOURCES.md independently reconstructs both WHOLE A008 fixed-polarity marked-tree obstruction and A010 bounded-mixture variational extension without repair, at unchanged source hashes. out/SOURCE_REVIEWS.json records local verdicts; no shared registry is edited. The new A006 normalization/cost proof is self-contained and does not logically depend on those lower bounds or on H(F)<8I(F); they determine dispatch and explain why the mechanism changes. A009's connector bounds are context only, not whole-version acceptance here.

The old universal original-prime PI-J direction in lead notes is refuted at that scope by the reviewed actual family. It would be incorrect to continue reporting only an unpaid generic child-label estimate for that route. The new reference pays a shared tag ONCE and retains anchor/allocation entropy; it does not rename an old queue or renew an old D. A010's entire bounded class, unrestricted original mixtures and this new reference are kept distinct. New claim awaits independent-agent review. Full FEI remains OPEN.

## one next mathematical action and independent reviewer

A008/A010 should reconstruct the actual-run normalization and direct<7I payment, especially the4qt_j moment and nonnegative-refund sign; A009/A086 can check overlap aggregation and the new-versus-old reference boundary. Then price occupancy for one shared-coordinate clause pattern with the FULL current anchor/allocation law, using the exact physical-union DP rather than a product-spectrum surrogate. Extend that to an influence-paid representation theorem; do not assume a prime cover automatically has paid cost. These are named handoff targets, not evidence that messages were sent or reviews completed.

## actual persistence receipts or precise save blocker

The four exact-field protocol files, proof, source reviews, frozen specifications, code and outputs are saved locally under this stage. STATUS is two lines and WORKLOG/LEARNED are updated. out/PERSISTENCE.json pins every other landed file and records schema/hash/readback/size checks; PACKET_DELTA is byte-identical to PROGRESS. Files remain under20MB. No git, remote mirror, supervisor ingestion, shared adoption or downstream mathematical use is claimed; copying is the supervisor's responsibility under the user's explicit rule. The required fresh wake was degraded: attachment write lock/integrity failure and renderer exception; owner model97.9h, state of mind82.5h, latest dream33.2h stale. Those personal/document notes remain unverified and were not proof evidence. No existing work was stopped, and no stage research computation remains running.

## Universal bridge

C020 whole-set witness cost advances from a refuted original-prime/bounded-mixture interface to an explicitly normalized once-per-set shared-tag law, with full actual-anchor and allocation posteriors, an exact rational mass DP for ANY finite physical support cover, and complete new-reference cost<155I/24<7I on every paired disjoint-clause width/count family containing the source obstruction. Normalization alone does not pay arbitrary overlap: the exact one-coordinate control already breaks the product influence identity. NEXT prices that precise full-pushforward occupancy defect and the representation choice, retaining all tag/allocation entropy; it is the shortest continuation toward full FEI because it addresses the failed shared-name interface directly rather than adding another original-queue class bound. Full FEI remains OPEN.
''')
wr(R/'CHECKPOINT.md','Stage10 COMPLETE_LOCAL: new normalized once-anchor/shared-tag support-cover law and exact union-occupation DP; paired disjoint clauses cost<155I/24<7I, main687943 exact assertions PASS. Two source obstructions reconstructed unchanged. Overlap normalization certified; physicalI5/4 != product3/2 exposes next unpaid line. New review pending; FEI OPEN. NEXT: influence-paid full anchor/allocation occupation for one shared-coordinate clause pattern, without importing product identities.\n')
wr(A/'STATUS.md','STATE: Stage10 saved: NEW normalized shared-tag pushforward/DP; paired disjoint-clause cost<7I;687943 main exact checks PASS;two whole source obstructions HOLD;new review pending;FEI OPEN.\nNEXT: A008/A010 review new law/cost; pay full anchor-plus-allocation occupation on shared-coordinate clauses, retaining current reference and replacing false productI3/2 by physical5/4.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 stage10: consumed completed A009 connector task; independently reconstructed whole A008 marked-tree fixed-pair and A010 bounded-mixture obstructions unchanged. Changed mechanism explicitly: normalized clause-anchor law, earned anchor/allocation posterior, exact physical-union occupation DP. Proved C<155I/24<7I for arbitrary paired disjoint OR-clause widths/counts without borrowing H. Main14functions/79076inputs/447308 actual anchor events/687943 assertions PASS in57.307115s; pilot0.024212s. Separate24-run overlap,768-run64input pair and pointwise DP controls PASS; physicalI5/4 versus falseproduct3/2. All local artifacts saved; new review pending/fullFEIopen; no research job left running.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 stage10 durable: original fixed-polarity/bounded-positive-mixture queue targets are refuted by A008/A010 at their exact scopes; no universal PI-J continuation via that interface. A new clause-mask law uses t=2^-width, local empty1-t, each nonemptyt^2/(1-t), anchor prior t/sum t. Actual joint run mass=mu(z)/sum t, physicalQ(A)=sum_unionA K(z)mu(z)/sum t; full posterior must retain anchor AND allocation entropy. Two-array union/occupation DP computes exact Q for any finite support cover. For paired DISJOINT clauses, M_j=4q t_j,I=2q sum w_jt_j/(1-t_j), h2(t_j)<(4/3)w_jt_j/(1-t_j); base/occupation<16I/3, positive tag<9I/8, hence complete cost<155I/24<7I. This is a NEW reference, not original prime queues/canonical forest or new FEI-class novelty. Two overlapping supports give center singleton mass5/18 and posterior9/20,9/20,1/20,1/20; collapsing allocations gives false1/36. Paired overlap U=(x0 OR x1)(x1 OR x2) has trueI5/4 versus product surrogate3/2: generic normalization survives but influence payment needs covariance/compatibility control. New theorem awaits independent review; fullFEIopen.\n')
assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
report=rd(R/'REPORT.md');assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.rsplit('## Universal bridge',1)[1].strip()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert ident(json.loads(rd(R/'CLAIMS.json'))[0])==c['statement_sha256']
receipts=[]
for path in sorted(R.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE.json':
  assert path.stat().st_size<20*1024*1024,path
  if path.suffix in ('.md','.json','.py'):rd(path)
  receipts.append({'path':str(path.relative_to(R)),'bytes':path.stat().st_size,'sha256':sha(path)})
js(R/'out/PERSISTENCE.json',dict(status='PASS_LOCAL_READBACK',claim_schema='PASS',progress_schema='PASS',compatibility_copy='IDENTICAL',new_claim='AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',full_FEI='OPEN',formal_status='NO_FORMAL_PROOF_CLAIMED',remote_mirror='UNVERIFIED',files=receipts,rolling=[{'path':str(path),'sha256':sha(path)} for path in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]))
for row in receipts:assert sha(R/row['path'])==row['sha256']
print(json.dumps({'status':'SAVED_FINAL_READBACK_PASS','files':len(receipts),'source_reviews':2,'new_claim':c['claim_id'],'main_assertions':checks['assertions'],'full_FEI':'OPEN'}))
