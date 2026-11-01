"""Freeze a review packet and stage mathematical drafts; never ingest anything."""
import datetime
import difflib
import json
import pathlib

root=pathlib.Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,value):
    (root/name).write_text(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

check=json.loads((root/'verification.json').read_text(encoding='utf-8'))
retrieval=json.loads((root/'brain_retrieval.json').read_text(encoding='utf-8'))
summary=[dict(query=x['query'],elapsed_s=x['elapsed_s'],limit=x['limit'],
              hits=[dict(id=r['id'],title=r['title'],source_id=json.loads(r['metadata_json']).get('source_id')) for r in x['rows']]) for x in retrieval]
write('brain_retrieval_summary.json',summary)

sources=dict(target='P0162',worker='w513',checked_at=now,current_openness='UNKNOWN',statement_verified=True,
    novelty_claim=False,owner_solved_retired_checked='bounded targeted check only; not exhaustive',
    primary_sources=[
        dict(id='arxiv:2606.00246v1',url='https://arxiv.org/html/2606.00246v1',sections=['Introduction definitions and FEI conjecture','Ansatz 1.1','Appendix B Eq.32'],
             finding='Full target verified. Chosen-coordinate reduction, exact extra term, equivalence up to constants; no full solution claimed.'),
        dict(id='odonnell-wright-zhou-2011',url='https://www.cs.cmu.edu/~odonnell/papers/fei.pdf',
             finding='Author-hosted primary paper gives the full FEI formula and Boolean codomain.'),
        dict(id='arxiv:2312.08271',url='https://arxiv.org/abs/2312.08271',
             finding='Primary abstract gives an influence-entropy bound retaining coordinate logarithms; not a full FEI solution.'),
        dict(id='arxiv:2609.21563',url='https://arxiv.org/abs/2609.21563',
             finding='September 2026 primary abstract claims plateaued/partially-bent special cases, not full FEI.'),
    ],historical_source=dict(id='Friedgut-Kalai-1996',doi='10.1090/S0002-9939-96-03732-X',
        original_pdf_access='web open failed; the statement is verified in later primary papers'),
    prior_owner_work=[
        dict(path='~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv',row=553,status='attempted_un'),
        dict(card_id='claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba',
             finding='Prior singleton-spectrum obstruction; the uniform singleton law violates Boolean convolution identities. Not recomputed.'),
        dict(card_id='claim_d15d0160e58b4c9183707be9f49462d2',memory_slug='fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23',
             finding='Small-influence reduction and arbitrary-coordinate obstructions already recorded. No novelty claimed for these principles.'),
        dict(path='~/<private-repo>/06_math_research/prob1000_lean_20260908/ultracode_20260909/F0090/memo.md',
             finding='Prior claimed FEI for a percolation-crossing subclass, using geometric arm inputs. Not a full FEI proof and not audited here.'),
    ],prior_searches=[
        dict(paths=['probability_1000_attempts_H_20260912','probability_1000_attempts_I_20260914'],terms=['P0162','Fourier entropy','FEI','Friedgut.*Kalai'],
             finding='No matching records in targeted readable mathematical files.'),
        dict(path='~/brain_workers/teams/W0300_O/TEAM_BOARD.md',finding='No P0162 row; no board edited.'),
    ],status_search=dict(date='2026-10-10',scope='bounded public primary literature search and named local records',
        finding='No full resolution found within these checks. Current openness remains UNKNOWN; absence of a hit is not certification.'),
    blind_evaluation_material_opened=False,formal_check=dict(performed=False,theorem=None,assumptions=None,trusted_axioms=None,admitted_placeholders=False))
write('SOURCE_STATUS.json',sources)

prior='''P0162 was tier 5/attempted_un on 7 September. Its exact brain attempt card explains why entropy-versus-cardinality alone fails: the uniform singleton law is not a Boolean squared spectrum. H/I targeted searches found no separate target records. The cited F0090 memo claims a percolation-crossing subclass using arm probabilities and dyadic boxes; those geometric hypotheses do not apply to arbitrary Boolean f. It is not used as a proof input here.

The live brain returned six target-related cards, including read-once-formula and linear-threshold results. A read-once representation or a threshold representation is an additional hypothesis; neither theorem supplies a general FEI bound. Their memory verification labels are not independent audits performed in this session. The directly useful card is claim_d15d0160e58b4c9183707be9f49462d2: its large-influence restriction bound exactly matches the elementary bound proved here, and its source memory already refutes arbitrary-coordinate lifts in the small-influence regime. The present result provides a transparent alternative bent/iterated-majority witness and a simultaneous global constant-4 bound. No record-function or majority-point-flip computation from the old work was repeated.

The mathematical gap is a dimension-free aggregate conditional-entropy budget over complete restriction trees. The good-coordinate condition is sufficient but is not asserted to follow from FEI. The arbitrary-coordinate condition is false. Current global openness and novelty are not certified.'''
write('PRIOR_ATTEMPTS.md',prior+'\n')
attempt=(root/'STATEMENT.md').read_text(encoding='utf-8')+'\n\n'+prior
for name in ('BRIDGE_CHECKPOINT.md','ENTROPY_BOUND.md','SMALL_INFLUENCE_OBSTRUCTION.md','FAMILY_FEI4.md'):
    attempt+='\n\n'+(root/name).read_text(encoding='utf-8')
attempt+='\n\nVerification command: python -X utf8 ~/brain_workers/w513/verify_bridge.py . Receipt: verification.json. These are arithmetic checks, not a formal proof or an independent audit.\n'
write('ATTEMPT.md',attempt)

common=dict(source_id='owner-probability-campaign-w513-p0162-20261010',url=None,
            revision='worker-proof-2026-10-10-review-pending',license='owner-own-work',excerpt=None)
def entry(key,name,kind,title,statement,proof,assumptions):
    return dict(key=key,namespace='probability.boolean-fourier',logical_name=name,kind=kind,title=title,
        statement=statement,proof_text=proof,assumptions=assumptions,domain='analysis of Boolean functions',source=common.copy(),
        review_status='DRAFT: independent mathematical audit pending; not an independently checked theorem',
        author_status='worker proof' if proof else 'concept',novelty_claim=False)

entries=[
 entry('restriction-def','fourier-restriction-entropy-and-conditional-term','definition','Fourier restriction entropy and its conditional term',
  'For a Boolean f on a finite uniform sign cube, split on coordinate i. With a_S=hat(f+)(S), b_S=hat(f-)(S), P_S=a_S^2, Q_S=b_S^2 and R_S=(P_S+Q_S)/2, set q_S=(a_S-b_S)^2/[2(a_S^2+b_S^2)] when R_S>0. Zero-weight terms are zero. Entropies use base 2. Define Delta_i=H(f)-[H(f+)+H(f-)]/2, B_i=sum_S R_S h(q_S), where h is binary entropy, and JS(P,Q)=H(R)-[H(P)+H(Q)]/2. All three spectra P,Q,R are normalized probability laws; Inf_i(f)=sum_S R_S q_S.',None,
  ['Uniform product measure','Boolean codomain {-1,1}','Squared Walsh coefficients','Base-2 entropy; continuous zero conventions']),
 entry('restriction-identity','fourier-restriction-jensen-shannon-identity','lemma','Exact restriction identity and a bounded Jensen-Shannon term',
  'For a Boolean f on a finite uniform sign cube, split on i. Let a_S=hat(f+)(S), b_S=hat(f-)(S), P=a^2, Q=b^2, R=(P+Q)/2, and q_S=(a_S-b_S)^2/[2(a_S^2+b_S^2)] at positive R_S. Zero-weight terms vanish. Let h be binary entropy in bits, B_i=sum R_S h(q_S), Delta_i=H(f)-[H(f+)+H(f-)]/2 and JS(P,Q)=H(R)-[H(P)+H(Q)]/2. Then Delta_i=B_i+JS(P,Q), with 0<=JS(P,Q)<=(2/ln 2)Inf_i(f), where Inf_i=sum(a-b)^2/4. Consequently B_i<=Delta_i<=h(Inf_i(f))+(2/ln 2)Inf_i(f). Delta_i is not identically B_i.',
  'Parent coefficient pairs are (a+b)/2 and (a-b)/2; their squared marginal is R=(a^2+b^2)/2. Finite entropy chain rule gives H(f)=H(R)+sum R h(q), hence Delta=B+JS. The one-index JS contribution in nats for x,y>=0 is at most (sqrt(x)-sqrt(y))^2/2: putting u=|x-y|/(x+y), differentiate the equivalent inequality (1+u)ln(1+u)+(1-u)ln(1-u)<=2(1-sqrt(1-u^2)); it follows from atanh(u)<=u/sqrt(1-u^2), obtained by integrating (1-v^2)^-1<=(1-v^2)^-3/2. Endpoints follow by continuity. Summing, (|a|-|b|)^2<=(a-b)^2 gives JS<=(1/(2ln2))sum(a-b)^2=(2/ln2)Inf_i. JS>=0 by entropy concavity. Jensen concavity of h gives B<=h(sum Rq)=h(Inf_i).',
  ['All normalization and definitions of fourier-restriction-entropy-and-conditional-term']),
 entry('bad-route','refuted-arbitrary-coordinate-fei-restriction-route','concept','Refuted route: charge restriction entropy at every coordinate',
  'The proposed rule that there is a universal K with Delta_i(f)<=K Inf_i(f) for every coordinate of every uniform Boolean f is false. It remains false when all individual influences are bounded by an arbitrarily small fixed tau. This refutation concerns an arbitrary coordinate, not the existence of a good coordinate or the FEI conjecture itself. The family in small-influence-fei-four-bad-coordinate-witness gives Delta_i/Inf_i arbitrarily large while H(f)<=4I(f).',None,
  ['Delta_i is the actual entropy increment, including its Jensen-Shannon term','The quantifier every coordinate is essential to the refuted route']),
 entry('small-family','small-influence-fei-four-bad-coordinate-witness','lemma','Small influences and a bad restriction coordinate coexist with global FEI constant 4',
  'Let m>=2 be even, N=2^m, and d>=1. On binary m-bit inputs put g(x)=(-1)^(sum_{j=1}^{m/2}x_(2j-1)x_(2j)), h=g-2 delta_0, and let F_m restrict on a new sign selector to g or h. Let G_d be iterated majority of three on 3^d disjoint uniform bits, starting from a dictator at d=0. Substitute disjoint balanced G_d copies for all m+1 inputs of F_m to obtain f_(m,d). Every individual influence is at most alpha=2^-d. A selector-block leaf v has influence alpha/N and Delta_v(f_(m,d))/Inf_v(f_(m,d))>=alpha*m. Nevertheless H(f_(m,d))<=[4-(2/3)^d]I(f_(m,d))<=4I(f_(m,d)). Thus for every tau>0 and M>0, some such Boolean f has all influences <=tau, one restriction ratio >=M, and a global FEI bound with constant 4.',
  'The two-bit quadratic has four Walsh magnitudes 1/2; disjoint products give ghat(S)=sigma_S/sqrt(N). Decompose F_m=A+zB with Ahat=sigma/sqrt(N)-1/N, Bhat=1/N. Each old coordinate has influence 1/2+1/N: the point flip adds an edge at zero to h, giving child influence 1/2+2/N; the selector has influence 1/N. Hence I(F_m)=m/2+(m+1)/N, and H(F_m)<=m+1<=3I(F_m). Balanced disjoint block composition gives H(F(G,...,G))=H(F)+I(F)H(G) and I(F(G,...,G))=I(F)I(G): a physical spectral subset uniquely identifies its active outer blocks, with independent gadget spectra conditional on that set. For G_d, its base four coefficients have squared mass 1/4, yielding H(G_d)=4(beta-1), I(G_d)=beta=(3/2)^d and leaf influence alpha=2^-d. Thus H(f)<=I(F_m)(4beta-1)=[4-1/beta]I(f). To bound the bad leaf increment, E[G_d+]=alpha and E[G_d-]=-alpha by monotonicity and balance. In the empty remaining-selector Fourier sector the restriction coefficients are c_U(Ahat+alpha Bhat) and c_U(Ahat-alpha Bhat), where for each active-block set S, sum_U c_U^2=1 by balance and Parseval. Here q=alpha^2 Bhat^2/(Ahat^2+alpha^2 Bhat^2)<=4alpha^2/N<=1/N, since Ahat^2>=1/(4N). This sector contributes at least alpha^2 m/N to B_v. The exact restriction identity gives Delta_v>=B_v, while Inf_v=alpha/N, proving the ratio. Choose d with alpha<=tau and even m>=M/alpha. All independence uses are on explicitly disjoint product blocks.',
  ['m even and at least 2','d at least 1','Disjoint balanced gadget blocks','Uniform product measure and Boolean output','Binary and sign cube coordinates identified by x_sign=(-1)^x_binary']),
 entry('tree-budget','fourier-entropy-complete-restriction-tree-budget','lemma','Exact remaining conditional-entropy budget on a complete restriction tree',
  'For any finite adaptive uniform Boolean restriction tree whose leaves are constant and whose internal node v fixes one unfixed coordinate i(v), write w_v=2^-depth(v). At node v let a,b be the Walsh coefficients of its two restrictions, R=(a^2+b^2)/2, q=(a-b)^2/[2(a^2+b^2)] where R>0, and B_v=sum R h(q), with binary entropy h in bits and zero-weight terms omitted. H(f) is Shannon entropy of the squared Walsh spectrum and I(f)=sum_S |S|hat(f)(S)^2. Then sum_v w_v B_v<=H(f)<=sum_v w_v B_v+(2/ln2)I(f). A dimension-free bound on that aggregate budget would prove FEI; FEI implies the budget for every such complete tree. Constants differ by at most 2/ln2.',
  'The exact node identities H(f_v)=average child H+Delta_v and I(f_v)=average child I+Inf_i(f_v) telescope with weights 2^-depth(v). Constant leaves have zero entropy and influence, so H(f)=sum w Delta_v and I(f)=sum w Inf_i. Apply Delta=B+JS and 0<=JS<=(2/ln2)Inf_i at each node. Uniform product measure supplies these weights; no dependent conditional estimates are multiplied.',
  ['Every leaf is a constant Boolean function','Each split fixes an unfixed coordinate','Uniform product measure','Restriction conditional term as defined above']),
 entry('remaining-gap','fei-aggregate-conditional-entropy-bridge-open','concept','Missing bridge: a dimension-free aggregate conditional-entropy estimate',
  'Unproved bridge for P0162: find an absolute K such that every uniform Boolean f has a complete restriction tree with sum_v 2^-depth(v) B_v<=K I(f). The exact tree-budget lemma makes this equivalent to FEI up to constants. A per-node good-coordinate bound is sufficient but has not been proved here. An arbitrary-coordinate bound is false, even for all-small-influence functions satisfying H<=4I. Current global openness is UNKNOWN after bounded checks; this draft makes no novelty claim.',None,
  ['Finite uniform Boolean cubes','Dimension-free K required','Do not replace exists a suitable coordinate by every coordinate']),
]
relations=[
 dict(from_key='restriction-identity',to_key='restriction-def',kind='depends_on',rationale='The identity "Delta_i=B_i+JS(P,Q)" uses the definition "B_i=sum_S R_S h(q_S)" with normalized restriction spectra.'),
 dict(from_key='small-family',to_key='restriction-identity',kind='depends_on',rationale='The family\'s "Delta_v/Inf_v>=alpha*m" uses the exact identity\'s "B_i<=Delta_i" after a lower bound on the empty-selector sector.'),
 dict(from_key='small-family',to_key='bad-route',kind='refutes',rationale='The family has "one restriction ratio >=M" for every M while "all influences <=tau"; this refutes a fixed K at "every coordinate" in the proposed route.'),
 dict(from_key='tree-budget',to_key='restriction-identity',kind='depends_on',rationale='The tree bounds "sum_v w_v B_v<=H(f)<=sum_v w_v B_v+(2/ln2)I(f)" telescope "Delta_i=B_i+JS(P,Q)" and its JS bound.'),
 dict(from_key='remaining-gap',to_key='tree-budget',kind='depends_on',rationale='The missing estimate "sum_v 2^-depth(v) B_v<=K I(f)" would combine with the tree lemma to give the full dimension-free FEI inequality.'),
 dict(from_key='small-family',to_existing_logical='math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence',kind='specializes',rationale='The existing target asks to "Bound the Shannon entropy of the squared Fourier coefficients of every Boolean function by a universal constant times its total influence"; this lemma proves "H(f)<=4I(f)" only for the explicitly defined f_(m,d) family.'),
]
bundle=dict(spec='mathbrain-draft-v1',author_agent='w513',bundle_slug='p0162-restriction-budget-small-influence-witness-001',entries=entries,relations=relations)
bundle_text=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
write('bundle_001.json',bundle_text)
inbox=pathlib.Path('~/math-brain-inbox/w513')
assert inbox.resolve()==pathlib.Path('~/math-brain-inbox/w513').resolve()
inbox.mkdir(parents=True,exist_ok=True)
staged=inbox/'bundle_001.json.part'
if staged.exists() and staged.read_text(encoding='utf-8')!=bundle_text:
    raise RuntimeError('Different staged bundle already exists; preserve it and select a new number.')
staged.write_text(bundle_text,encoding='utf-8')
write('INBOX_RECEIPT.json',dict(prepared=True,prepared_at=now,path=str(staged),submitted=False,
    reviewed=False,ingested=False,retrievable=False,reason='Complete .part intentionally awaits independent review; no live integration was run.',
    entries=len(entries),relations=len(relations)))
patchdir=root/'patches';patchdir.mkdir(exist_ok=True)
live='~/math-brain-inbox/w513/bundle_001.json'
patch=''.join(difflib.unified_diff([],bundle_text.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(patchdir/'01_p0162_bridge_bundle.diff').write_text(patch,encoding='utf-8')

chain=next(x for x in summary if x['query']=='chain-rule')
repair=dict(status='bounded proposal; not deployed',scope='P0162 restriction-entropy cards and their local graph relations only',
    measured_failure=dict(kind='reasoning and targeted lexical retrieval',command=check['command'],
        omitted_jensen_shannon_identity_error_bits=check['discarded_identity_error_bits'],
        exact_identity_error_bits=check['corrected_identity_error_bits'],chain_query=chain),
    proposed_repair='Attach the exact JS+conditional-term card and the typed small-family counterexample to P0162. Preserve exists-a-good-coordinate scope; expose the additive constant when transferring a reduction. Keep metric covering entropy distinct from finite Shannon entropy. Do not modify global ranking or recall controls.',
    after_deployment_retrieval_measurement=None,
    validation='Replay the exact two-bit witness and the three-bit arithmetic suite; then have independent auditors test the chosen-coordinate scope before promoting the card.',
    limitations='No native-engine recall score improvement, ingestion, or independent theorem audit is claimed.')
write('RETRIEVAL_REPAIR.json',repair)
hook=dict(id='p0162-w513-01',area='math',event='stage-start',
    cue='A restriction-entropy proof transfers a source reduction or changes a chosen-coordinate quantifier.',
    fire_when='Using the small-influence reduction to assert every coordinate has Delta_i<=K Inf_i, or treating Delta_i as B_i.',
    silent_when='The proof retains Delta_i=B_i+JS and the selected-coordinate or aggregate-tree scope, with constants and hypotheses explicit.',
    text='Before charging restriction entropy to influence, retain Delta=B+JS and the source quantifier. A bad split can coexist with tiny influences and H<=4I; a suitable split or an aggregate budget still needs proof.',
    evidence='~/brain_workers/w513/verification.json: two-bit Delta=2, B=1, JS=1; FAMILY_FEI4.md; memory slug fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23',proposer='w513')
write('HOOK_PROPOSAL.jsonl',json.dumps(hook,ensure_ascii=False)+'\n')
write('PROGRESS_EVENT.json',dict(agent='w513',row='S1.P0162.w513-L6',
    event='P0162: constant-4 special family with arbitrarily small influences and unbounded bad-coordinate cost; exact gap and measured checks saved, independent audit pending.',
    evidence=str(root/'FAMILY_FEI4.md'),published=False,
    reason='Worker write boundary: the shared progress page and hooks proposal are left for the validating reviewer; local durable event is ready.'))

claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
claims=[row for row in claims if row['id']!='w513-P0162-N1']
claims[0].update(id='w513-P0162-target',source=dict(ranking_id='P0162',primary_url='https://arxiv.org/html/2606.00246v1',state='statement verified; current openness UNKNOWN'),
    independent_reviewer='w515; pending',remaining_gap='Dimension-free aggregate conditional-entropy estimate for arbitrary Boolean spectra.')
claims.append(dict(id='w513-P0162-N1',status='numerical evidence',statement='Exact integer Walsh transforms followed by floating-point entropy passed the bounded regression suite reported in verification.json.',
    assumptions=['Self-generated truth tables; no blind test material','Three-bit exhaustive checks and explicit rare-switch witnesses','Fresh gate in compute_gate.json'],
    source=dict(type='owner-own-work',path='verify_bridge.py',command=check['command']),proof_or_counterexample=check,
    independent_reviewer='w515; pending',remaining_gap='These checks are arithmetic evidence; general lemmas require their written proofs and independent audit.',independently_checked=False))
write('CLAIMS.jsonl',''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims))

review='''P0162 review packet for w515. Adversary w514 receives STATEMENT.md only first; PEER_OUTBOX.jsonl records failed delivery and sequence. No peer audit is claimed.

Main result: FAMILY_FEI4.md proves a special family with H<=4I, all influences arbitrarily small, and one arbitrary-coordinate restriction cost arbitrarily large. It is not a solution of P0162 and makes no novelty claim. ATTEMPT.md is the complete statement/prior-digest/proof packet. CLAIMS.jsonl separates the target, six worker-proved lemmas and arithmetic evidence. SOURCE_STATUS.json states the bounded source checks and UNKNOWN current openness.

BRIDGE_HYPOTHESES.md compares the returned finite Shannon chain-rule theorem, metric entropy, KL/Hellinger inequality and special-class FEI cards against the exact proof need, including the log conversion and zero-mass cases.

Check the normalized spectra and the exact JS term in L1/L2, then the two-bit base of the bent product, the edge count I(F_m)=m/2+(m+1)/2^m, balanced disjoint block entropy composition, and the empty-selector sector in L4/L6. The parameter choice must preserve one bad coordinate, not every coordinate. L5 must telescope only trees with constant leaves and their actual weights. The one unresolved mathematical gap is the dimension-free aggregate conditional-entropy budget.

Run python -X utf8 ~/brain_workers/w513/verify_bridge.py. It opens no stores and uses the fresh bounded gate. The receipt is verification.json. No Lean/formal check was performed, no theorem/axiom receipt exists, and no admitted placeholder counts as proof. Brain metadata labels or hashes do not replace this audit.

Return KEEP/FIX/DROP per L1-L6, with the exact gap for a FIX/DROP. An independent check is still required; cross-account keeps are required before shared theorem/edge promotion. If w515 adds a new result of their own, w518 is its independent referee.

The complete DRAFT is staged as ~/math-brain-inbox/w513/bundle_001.json.part. It is not submitted or ingested. After mathematical keeps, the validating coordinator can rename the staged file to bundle_001.json and integrate it. patches/01_p0162_bridge_bundle.diff is the exact proposed addition with live-path headers. Do not run live integration from this worker. The local hook/progress proposals are HOOK_PROPOSAL.jsonl and PROGRESS_EVENT.json; their shared publication is not claimed.

NEXT: Audit L6's balanced composition and empty-selector sector, then accept or correct the typed draft; retain the aggregate conditional-entropy estimate as the unclosed P0162 gap.
'''
write('REVIEW_PACKET.md',review)
ratio=check['rare_switch'][-1]['ratio']; composed=check.get('composed_small_influence_witness',{})
report=f'''Saved a precise FEI attempt and an explicit special family: arbitrarily small individual influences and arbitrarily large cost at one restriction coordinate coexist with H(f)<=4I(f). The full P0162 conjecture is not proved. The remaining gap is a dimension-free aggregate conditional-entropy budget. These principles are partly already recorded in the brain; no novelty claim is made.

The useful brain card was claim_d15d0160e58b4c9183707be9f49462d2. Its selected-coordinate scope matches our derivation. Read-once and threshold-function cards require additional structural hypotheses. The exact restriction identity includes Jensen-Shannon divergence; the May 2026 paper's Appendix B agrees. An extraction that omits that term fails by 1 bit on a two-bit Boolean witness, while the corrected identity has zero error there.

Measurement command: {check['command']}. All {check['exhaustive']['coordinate_checks']} exhaustive three-bit coordinate checks passed, with maximum identity residual {check['exhaustive']['max_residual']}. At m=10 the rare-selector Delta/Inf ratio is {ratio:.6f}, versus the proved lower bound 9. The nine-bit disjoint-majority witness has H/I={composed.get('entropy_over_total_influence','not yet recorded')}; its composition residual is {composed.get('composition_entropy_residual','not yet recorded')}. Runtime was {check['elapsed_s']:.3f} seconds, within a fresh 30-second, one-process, no-GPU gate. These are arithmetic checks, not independent mathematical audits.

The memory recall timed out at 62.755 seconds; a targeted cited-memory fallback was used. The bounded read-only lexical chain query returned {[x['title'] for x in chain['hits']]}; RETRIEVAL_REPAIR.json proposes a P0162-only typed bridge/quantifier attachment. No native recall-score improvement or global control change is claimed.

Risk: extending one bad coordinate to all coordinates would be a false inference. Dropping balance or disjointness breaks the composition proof. Numerical entropy checks do not prove the all-dimension statements; written proofs await w515. Current global openness is UNKNOWN after bounded local/current-primary checks.

Apply after mathematical keeps: the validating coordinator renames ~/math-brain-inbox/w513/bundle_001.json.part to bundle_001.json and runs its own integration process; patches/01_p0162_bridge_bundle.diff is the reviewable unified addition. This worker did not integrate or edit live files. Submitted, reviewed, ingested and retrievable are all false in INBOX_RECEIPT.json.

Peer sending failed because no team membership was present and w514 was unregistered; a statement-first durable outbox is saved. Local hook/progress proposals await shared publication under the worker write boundary.

NEXT: w515 independently checks L6's balanced composition and empty-selector sector, then reviews the draft while keeping the general aggregate conditional-entropy budget open.
'''
write('REPORT.md',report)
print(json.dumps(dict(packet='REVIEW_PACKET.md',staged_draft=str(staged),entries=len(entries),relations=len(relations),claims=len(claims),independent_audit=False,ingestion=False)))
