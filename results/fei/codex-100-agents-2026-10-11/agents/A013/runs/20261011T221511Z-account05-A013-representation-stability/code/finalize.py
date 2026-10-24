from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
SUP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
TEAM=Path('~/brain_workers/FEI100_20261011')
rid=RUN.name; now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(path,x):
 path.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
v=json.loads((RUN/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))
proof=RUN/'COVER_STABILITY.tex'
sources=[REPORTS/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
sources += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/OVERLAPPING_PRODUCT_NOTE.md','sources/ERASURE_REDUCTION.md','sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']]
sources += list((TEAM/'context').glob('*.txt'))+[TEAM/'BOARD.md']
sources += [TEAM/'agents/A011/runs/20261011T213831Z-account05-A011-representation-existence'/x for x in ['REPORT.md','STRUCTURED_COVER.tex']]
sources += [TEAM/'agents/A012/runs/20261011T215648Z-account05-A012-sparse-activation-accounting/REPORT.md',TEAM/'agents/A086/runs/20261011T214823Z-account05-A086-joint-code-referee/JOINT_CODE_REVIEW.md']
sources += list((REPORTS/'runs').glob('*/*/REPORT.md'))
sources += [TEAM/'claude/B03/STREAM_NOTES.md']
receipts=[]
for p in sources:
 if p.exists():receipts.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
write(RUN/'out/SOURCE_RECEIPTS.json',receipts)
board=(TEAM/'BOARD.md').read_text(encoding='utf-8-sig')
print('\n'.join(line for line in board.splitlines() if any(x in line for x in ['A011 |','A012 |','A013 |','A086 |'])))
notes=TEAM/'claude/B03/STREAM_NOTES.md'
print('B03 notes present:',notes.exists())
if notes.exists():print(notes.read_text(encoding='utf-8-sig'))
statement=('For every ordered Boolean gate union, physical restriction gives an exact cover with no extra gates or inner regular functions, shrinking relevant supports and inherited ranks, conditional gate probabilities p_l^a<=2^|A|p_l and explicit independent-root and label ledgers. Disjoint sign products admit the parity-of-sign cover with explicit count and product gate probabilities; fresh physical selector covers have dyadic conditional probability and incidence-scaling ledgers, while reused selectors require actual branch restriction first. For every balanced Boolean core g with complete nonempty spectral subprobability reference of cost c_g and r>=1 fresh point controls, p=2^-r, there is a full normalized vacuum-separated projected reference for F=1+A_r(g-1) with cross entropy C_F<=h2(2p-p^2)+2r(2p-p^2)+p*c_g<=p*c_g+(6+2/ln(2))*p*r. Consequently c_g<=K I(g) gives C_F<=max(K,6+2/ln(2)) I(F), stable under disjoint tensor references, fresh-character balancing and balanced-core activation, with no repeated influence charge. This is not a universal construction of the core reference or a bound on the original queue infimum.')
statement+=' Additionally, fixing the ten active controls of the actual two-gate union A_10*(z AND (y1 OR y2)) increases each of the Section 5 worst-degree gate-label, subset-allocation and rank/rarity helper expectations, with exact parent upper bounds 5/1024,55/1024,231/1024 and child bounds 17/16,at least 1/16,3/10. This is pointwise, not an averaged obstruction. Four explicit same-physical-selector multiplexer iterations have raw cover read d+1 but reduce exactly to two gates with root probability 1/9 at weights 1/2, H=2 and I=3/2.'
claim=dict(claim_id='A013-VACUUM-PROJECTED-COVER-STABILITY',version=1,exact_statement=statement,
 hypotheses=['Boolean signs on uniform finite physical cubes','entropy and reference cost in bits','ordered gates are finite Boolean combinations of regular functions','disjoint physical input blocks for tensor claims','balanced core, r>=1 fresh independent controls, complete core reference with finite cross entropy for activation theorem','actual conditional restriction before any reused-selector multiplexer'],
 statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A013/account05'],
 proof_source={'path':str(proof),'sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'validation':str(RUN/'out/EXACT_RESULTS.json')},
 proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['The unchanged physical-leaf transcript has influence-paid cost on all rare balanced-core activations','A011 boundary admission is automatically preserved by retaining the restricted tree','Formal selectors reused in branches may be treated as fresh independent inputs'],
 first_unproved_line=None,next_consumers=['A011','A012','A017','A028','A058','A086','A094','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
write(RUN/'CLAIMS.json',[claim])
ledger={
 'restriction':{'gate_count':'N_a<=N','regular_inner_count':'M_l,a<=M_l','support':'R_l,a subset R_l minus A','rank':'inherited coordinate deletion decreases rank; ratio rank/(predecessor intersection+1) need not decrease','probability':'p_l,a=Pr(E_l|X_A=a)<=min(1,2^|A| p_l); may vanish','root_odds':'lambda_l min(p_l,a,1/2)','root_entropy':'sum_l h2(odds/(1+odds))','root_normalizer':'sum_l log2(1+odds)','root_set_cost_change':'Lambda_a-Lambda+sum_roots log2(pi_l/pi_l,a), at unchanged retained lambda','label_entropy':'uniform attachment log2 d_a(j)<=log2 d(j); pi-weighted label KL<=log2(2^|A| W/W_a), W_a>0'},
 'disjoint_tensor':{'positive_gate_count':'(prod_i(N_i,+ + N_i,-)+prod_i(N_i,+ - N_i,-))/2','inner_count':'sum_i M_i','gate_probability':'prod_i p_i','gate_root_pi':'min(prod_i p_i,1/2)','attachment_degree':'d_i,+/-(j) prod_k!=i(N_k,+ + N_k,-) is an upper bound','artificial_label_entropy':'b H(L|B=1)+(1-b)H(L|B=0)=sum_i H(L_i)-h2(b)','complete_reference_cost':'sum_i c_i','influence':'sum_i I_i'},
 'fresh_multiplexer':{'gate_count':'sum_b N_b','inner_count':'M_b,l+path_depth_b','gate_probability':'2^-depth_b p_b,l','root_pi':'2^-depth_b p_b,l for nonzero depth','feasible_weight_scale':'c=min(1,min_selector_j 1/sum_l:j in R_l,new lambda_l)','root_odds':'c lambda_l 2^-depth_l p_l','root_log_odds_increase':'between depth_l-1+log2(1/c) and depth_l+log2(1/c)','latent_label_entropy':'H(B)+sum_b Pr(B=b)H(L|B=b); H(B)=expected depth for dyadic leaves'},
 'reused_multiplexer':{'necessary_update':'restrict g_b and every gate to selector assignment b first','gate_probability':'2^-a Pr(E_b,l|selector=b)','failure_witness':'g_+(x)=x,g_-(x)=-x, reused selector x gives constant +1'},
 'activation_repair':{'p':'2^-r','nonempty_spectral_mass':'v=2p-p^2','control_reference':'Q(S,empty)=sum_j=max(1,max(S))^r 4^-j','core_reference':'Q(S,T)=p^2 R_g(T), T nonempty','vacuum_mass':'full reference assigns 1-v to empty','nonempty_reference':'v Q(S,T)/q_star, q_star=sum_nonempty Q<=1','exact_cost':'h2(v)+sum_nonempty P log2(1/Q)+v log2(q_star)','cost_bound':'h2(v)+2r v+p c_g <=p c_g+(6+2/ln2)pr','influence':'p(I(g)+r)','unpaid_term':'arbitrary balanced core reference cost c_g'},
 'iteration':{'tensor_cost':'additive for disjoint references','balancing_cost':'unchanged by fresh-character spectrum translation; influence increases by 1','activation_cost':'c_new<=p c_old+C_star p r, C_star=6+2/ln2','activation_influence':'I_new=p I_old+p r','depth_independent_constant':'max(K_initial,C_star)','local_charge_weight':'product of all later activation probabilities','cover_gate_growth':'tensor multiplies sign-cover counts; mux sums counts; restriction adds none'},
 'scope':'Complete projected reference repair; no universal core-code claim and no queue-infimum comparison',
 'validation_file':'out/EXACT_RESULTS.json'}
write(RUN/'STABILITY_LEDGER.json',ledger)
lead=json.loads((RUN/'out/LEAD_LEDGER_RESULTS.json').read_text(encoding='utf-8'))
ledger['late_lead_direction']=lead
write(RUN/'STABILITY_LEDGER.json',ledger)
progress={
 'protocol_revision':protocol['revision'],'run_id':rid,'stream':'B03','packet_id':'A013','gap_id':'G-J-COST','attempt_id':'A013-STABILITY-1','method':'Consume A011/A012 transcript obstruction; pushforward Kraft masses and normalize vacuum separately; exact conditional cover transport',
 'mathematical_delta':'Full rare balanced-core reference cost repaired to p*c_g+(6+2/ln2)*p*r, stable under disjoint tensor references and balancing. All gate/name/root updates explicit; arbitrary core c_g remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'RESTRICTED_STABILITY_AUTHOR_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['COVER_STABILITY.tex','STABILITY_LEDGER.json','out/EXACT_RESULTS.json','out/FROZEN_SPEC.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A086/A094 independently reconstruct the projected reference and its normalization; then replace constant stopping leaves by two colliding nonconstant low-boundary leaves and compute the full projected cost, retaining both core costs.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal paid balanced-core reference remains open','B03 STREAM_NOTES.md absent at initial intake','Independent review, supervisor adoption and mirror verification pending','Successful checker unexpectedly took 65.065931 seconds, exceeding frozen pilot cap 60; no new search launched'],
 'packet_ids':['A013']}
expected_progress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
progress['mathematical_delta']+=' Late lead v1 consumed: explicit pointwise counterexample to all three queue helper-charge monotonicities and exact four-depth same-selector reduced ledger.'
progress['source_artifacts']+=['out/LEAD_FROZEN_SPEC.json','out/LEAD_LEDGER_RESULTS.json']
progress['next_action']='A086/A094 review both projected reference and queue-charge obstruction; derive averaged queue transport retaining actual child probabilities and the original queue root normalizers.'
progress['blockers']=[x for x in progress['blockers'] if 'STREAM_NOTES' not in x]
assert set(progress)==expected_progress
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)
report=f'''# A013 / B03 representation stability

## exact target, quantifiers, hypotheses and units

Transport every finite ordered gate union through actual physical restriction, disjoint sign tensor product, and physical multiplexer composition, explicitly accounting for gates, regular inner functions/orders, labels, reference-root probabilities and normalizers. Entropy and complete reference costs are in bits; influence is total physical flip probability. Fresh independent selectors and disjoint tensor blocks are hypotheses, not inferred after reuse.

New dependency-consuming result: for every balanced Boolean core g with complete nonempty subprobability reference cost c_g, r>=1 fresh point controls, p=2^-r, F=1+A_r(g-1), an explicit full normalized reference has cross entropy

    C_F <= h2(2p-p^2)+2r(2p-p^2)+p*c_g
        <= p*c_g+(6+2/ln2)*p*r.

If c_g<=K I(g), its full cost is <=max(K,6+2/ln2)I(F). The constant is below 8.886 and does not grow with disjoint tensor/reference composition, fresh-character balancing, or balanced-core activation depth. The arbitrary core cost remains present. This closes the activated-literal transcript failure at the complete projected-reference level, not at the original incidence-queue infimum. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, was read in full. Campaign README/CURRENT_STATUS, claim/obstruction/packet registries, stream actions, A013 contract, and relevant plan sections were consulted. Large combined reads were truncated by the tool; targeted rereads recovered the B03 contract and relevant identities. The registry snapshot is historical; the board and original live agent reports supply the newer state. Earlier runs B05, B09 and B19 were consulted for obstruction/review scopes only; none is a proof premise.

The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted. Specific source notes: OVERLAPPING_PRODUCT_NOTE (disjointness/reuse guard), ERASURE_REDUCTION and BLOCK_RESTRICTION_IDENTITY (actual restriction interface). C008/C013/C035 are calibration; none is advertised as new. X004/X005/X007/X013 rule out silently discarding overlap, arbitrary-core cost, or Boolean ancestry.

Threshold 38-page text: Sections 4.5 and 5.1-5.3, Proposition 5.5 in Section 5.6, Proposition 8.6 and Corollaries 8.7-8.8 in Section 8.2, and Section 8.4 activation identities. Earlier 29-page opening and constants were checked as historical context; its older constant is not imported. Percolation 30-page and earlier 31-page introductions, definitions and opening theorem scopes were read; their geometric hypotheses supply no premise for this algebraic cover transport.

A011 original REPORT/STRUCTURED_COVER (20261011T213831Z), A012 original REPORT (20261011T215648Z), and A086 JOINT_CODE_REVIEW (20261011T214823Z) were read. A086 independently accepts A011 at its stated boundary-admission scope. This run consumes that actual interface and A012's physical-label obstruction, rather than opening a separate broad candidate. The proof reconstructs all identities locally, so proof_dependencies is empty. One bundled candidate is submitted. No new independent acceptance is asserted. B03 STREAM_NOTES.md was absent, and no lead instruction was overridden. BOARD.md was read initially and reread during finalization. Source hashes are in out/SOURCE_RECEIPTS.json. No external literature novelty claim or online theorem attribution is made.

## complete derivation or exact first unsupported line

COVER_STABILITY.tex is the complete standalone proof; STABILITY_LEDGER.json is the operation-by-operation interface. Restriction commutes with union and actual inner-gate restriction, preserves inherited desirability orders, removes relevant coordinates, and makes p_l conditional on the fixed physical event. Rank decreases but rank divided by occupied predecessor count need not decrease. Root odds and normalizers must therefore be recomputed; no unproved monotonicity is used. Independent root-vector entropy is sum h2(q_l), and weighted label divergence has the explicit bound log2(2^|A| W/W_a), when W_a>0.

Tensor cover uses the supplied covers of both signs, with positive gate count half the sum of the products of signed count sums and differences. Tensor probabilities multiply only on disjoint physical blocks. A negative cover can be formed as one intersection of all complements but its regular-inner count can worsen. The tensor minterm cover of t independent literals has 2^(t-1) positive gates despite zero spectral entropy. This separates cover growth from paid complete reference cost.

Fresh multiplexers attach the actual selector cell to each branch gate and add its path literals. Selector overlap imposes a new incidence weight scale. Reused-selector multiplexers first restrict the branch to the selected physical assignment; g_+(x)=x,g_-(x)=-x on selector x computes the constant +1. Root probabilities based on unreduced formal branches are invalid.

For activation, sum the old transcript's Kraft masses over all witnesses decoding the same Fourier set. Constant stopping leaves contribute Q(S,empty)=sum_(j>=max S)4^-j, while core leaves contribute Q(S,T)=p^2 R_g(T). These are actual projected reference masses, not an asserted incoherent Fourier decomposition. Their total mass is <=1. The exact Boolean spectrum has empty atom (1-p)^2, control-only nonempty atoms p^2, and core atoms p^2 ghat(T)^2. Replace the projected empty atom by its actual mass and normalize the entire nonempty reference. Exact cross entropy retains the correction v log2(q_star), with its nonpositive sign. Bounding the remaining terms proves the complete cost above; no leaf-label or terminal cost is discarded without a valid reference. Products of full references add cost; character translation balances without changing cost; activation weights all older cost and influence by the same p. Expanding recurrences pays each local activation charge once.

First unsupported universal line: every arbitrary balanced Boolean core admits a complete reference with c_g<=K I(g) for one absolute K. It is not assumed. Nor is the original queue's variational infimum bounded by this alternative reference. Arbitrary physical data restrictions can make the core unbalanced, and restriction may destroy a retained tree's boundary or orthogonality admission; pruning/re-certification is separate work.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json, helper A013-exact-v1, no symmetry reduction. All 256 labelled three-bit Boolean minterm covers and all six singleton restrictions (1536 cases); all 256 pairs of two-bit Boolean branches checked as disjoint products, fresh multiplexers and physically reused multiplexers; all 78 balanced cores on n=1,2,3 activated for r=1,2,3,4 (312 cases, maximum physical dimension seven). Integer FWHT and exact Fraction arithmetic check spectra, projection masses, root probabilities and physical influence. Outward rational logarithm intervals use the 32-term atanh series plus its proved geometric tail. No floating sign is a proof premise.

Command from A013:

    python -X utf8 runs\\{rid}\\code\\validate.py

Final result: PASS, {v['exact_assertions']:,} exact assertions, zero failures; output out/EXACT_RESULTS.json. Two implementation corrections were needed: Walsh's bit-zero sign convention reverses the fresh selector coefficient when g is selected at bit one; the r=1 character reference equals the true spectrum, so its Gibbs comparison is certified by exact equality rather than a strict interval sign. Both failures and corrections are retained in out/VALIDATION_HISTORY.json.

Observed successful checker runtime: {v['elapsed_seconds']:.6f} seconds. This unexpectedly exceeded the frozen 60-second pilot budget by 5.065931 seconds; this is an execution deviation, not a claimed compliant pilot. The process completed and no further search was started. Future searches need an internal 55-second cutoff and smaller rational expressions. Memory estimate 90 MB; no >300 MB planned job or heavy job, no automatic dimension increase, GPU, background helper or window. The exact finite cases validate implementations; the all-r result follows from the analytic proof.

## proof dependencies and changed downstream conclusions

One bundled author-proved claim A013-VACUUM-PROJECTED-COVER-STABILITY@1, pending A086/A094 review. All critical algebra and the Gibbs argument are reconstructed in the proof, without an unreviewed campaign premise. A011/A012 are source-bound motivation and interfaces; C013 is a known activation identity, not the claimed delta.

A011 can replace the constant-sized rare-literal transcript charge by the explicit normalized projected-reference cost. A012's observation that latent-label entropy must be erased is satisfied by a valid decoder pushforward plus vacuum separation. A017/A058 have a precise fresh/reused selector probability rule; A028 gets a restriction ledger that does not silently preserve admission. These are proposed downstream substitutions, not claimed observed use or shared-index adoption. Full FEI and the arbitrary-core reference obligation remain open.

## one next mathematical action and independent reviewer

A086 primary and A094 alternate should independently reconstruct the projected-reference mass and normalized cross entropy, including zero reference atoms, empty coefficient, and the sign of v log2(q_star). Then extend the repair to two colliding nonconstant low-boundary leaves, keeping both terminal costs; this tests the collision term rather than recomputing a known activation class. No messages were sent; handoff is saved locally.

## actual persistence receipts or precise save blocker

Required REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA, COVER_STABILITY.tex, STABILITY_LEDGER.json, checker, frozen spec, exact output, source and persistence receipts are written only within A013. Protocol field sets and all JSON parses are checked by code/finalize.py; receipts include SHA256 and byte lengths. STATUS has exactly two lines; WORKLOG is dated and appended; LEARNED records durable identities and scope limitations. No shared index, other agent folder, read-only source, brain, git, mail, trading tree or remote repository was changed. Independent review, supervisor copying, mirror verification and adoption remain pending. No local save blocker.

## Universal bridge

This stage moves C020 whole-set witness cost by repairing the full projected-reference cost of rare balanced-core activation: the old constant transcript overhead is replaced by an explicit influence-paid (6+2/ln2)pr charge, with the entire p*c_g core bill retained and a depth-independent composition constant. It also isolates the exact gate/root/name and admission failures under physical restriction and selector reuse. What remains is an absolute paid complete code for arbitrary cores and, next, a collision-aware repair when both stopping leaves are nonconstant. NEXT is the shortest route toward full FEI because it directly removes the live A011/A012 bottleneck in a valid full reference and probes the next unpaid overlap term rather than treating rare activation as a new easy class.
'''
report=report.replace('B03 STREAM_NOTES.md was absent, and no lead instruction was overridden.', 'B03 STREAM_NOTES.md was absent initially but its v1 appeared at final intake, timestamped 22:30 UTC. Its A013 direction was then consumed in the added queue-charge obstruction and four-depth reused-selector ledger. No direction was overridden.')
report=report.replace('No further search was started.', 'No further search in that family was started.')
report=report.replace('and no further search was started.', 'and no further search in that family was started.')
extra='''\nLate lead-directed supplement: COVER_STABILITY.tex final two sections prove that all three Section 5 helper-charge expectations may strictly increase on one actual restriction of a read-two union. The core is h=(z AND y1) OR (z AND y2), with mean -1/4, I=5/4. Activate on r=10 point controls and restrict those controls active. Parent I=55/4096. Parent label/subset/rank-rarity upper bounds are 5/1024,55/1024,231/1024; child values/lower bounds are 17/16,1/16,3/10. Rank/rarity here means the actual G_j helper before averaging; the coarse (24/5)I log2 k term also rises from 33/512 to 6. These statements hold irrespective of assignment optimization. The rare child's physical probability 1/1024 is retained, so this refutes pointwise monotonicity, not expected stopping-tree transport.\n\nThe lead's four-level shared-selector request is fulfilled by F_0=y,F_d=MUX_x(F_(d-1),z_d), d=1..4. Formal read d+1 reduces to actual read two, with two gates of probability 1/4, lambda=1/2, root odds 1/8, root probability 1/9, Lambda=2 log2(9/8), root-vector entropy 2 h2(1/9), attachment selector-name entropy one bit, H=2,I=3/2. Contradictory intermediate clauses have zero probability and are removed. Exact four-depth tables and root ledger are in out/LEAD_LEDGER_RESULTS.json.\n'''
report=report.replace('## executed validation with domain, arithmetic, commands and outputs',extra+'\n## executed validation with domain, arithmetic, commands and outputs')
report=report.replace('## proof dependencies and changed downstream conclusions',f'''Lead supplement was frozen separately in out/LEAD_FROZEN_SPEC.json before execution. Command: python -X utf8 runs\\{rid}\\code\\lead_ledger.py. Output: {lead['exact_assertions']} further exact assertions, zero failures, {lead['elapsed_seconds']:.6f} seconds, with an internal 55-second cutoff and maximum 60-second pilot. The r=10 comparison uses analytic activation identities and rational bounds (log2(13)<4 follows from 13<16), not an automatically enlarged truth-table search. Total exact assertions across the two passed helpers: {v['exact_assertions']+lead['exact_assertions']:,}.\n\n## proof dependencies and changed downstream conclusions''')
report=report.replace('Then extend the repair to two colliding nonconstant low-boundary leaves, keeping both terminal costs; this tests the collision term rather than recomputing a known activation class.', 'Then derive averaged queue-charge transport with actual child probabilities and original root normalizers; the explicit pointwise obstruction identifies which rare-child weight must be retained.')
report=report.replace('What remains is an absolute paid complete code for arbitrary cores and, next, a collision-aware repair when both stopping leaves are nonconstant.', 'What remains is an absolute paid complete code for arbitrary cores and averaged queue transport retaining the rare child probabilities; the late lead-directed counterexample rules out simply asserting pointwise monotonicity of any of the three helper charges.')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
write(RUN/'out/VALIDATION_HISTORY.json',{'attempts':[{'result':'failed','assertion':12340,'cause':'bit-one g branch has Fourier selector coefficient (hhat-ghat)/2 in checker convention','correction':'reverse two selector coefficient signs; Boolean proof unchanged'},{'result':'failed','assertion':20495,'cause':'r=1 character projected full reference equals actual spectrum','correction':'allow exact ref==P as proof of equality; otherwise require strict interval gap'},{'result':'PASS','assertions':v['exact_assertions'],'runtime_seconds':v['elapsed_seconds'],'budget_deviation':'successful checker exceeded 60-second frozen pilot cap by 5.065931 seconds'}]})
(ROOT/'STATUS.md').write_text('STATE: A013 cover transport, projected activation repair and lead-directed queue-charge obstruction complete; 52,513 exact checks; review pending; full FEI OPEN.\nNEXT: A086/A094 reconstruct proofs; derive averaged queue-charge transport retaining actual rare-child probabilities and original root normalizers.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} — {rid}: consumed A011/A012 obstruction and A086 acceptance; proved explicit restriction/tensor/mux gate and root ledger, plus full activation cost <=p*c_g+(6+2/ln2)pr. Checked 52,366 exact assertions over 1536 restrictions, 256 branch pairs and 312 balanced-core activations. Corrected checker sign and equality cases. Successful runtime 65.065931s exceeded the 60s pilot cap; no additional search in that family launched. Late B03 notes v1 consumed: analytic pointwise obstruction for all three queue charges, plus exact same-selector d=1..4 ledger, 147 further checks in 0.001505s. Review/adoption pending; averaged transport, arbitrary-core code and original queue optimum remain open.\n')
(ROOT/'LEARNED.md').write_text('''# Durable A013 facts

- Actual restriction commutes with ordered gate unions and preserves regular desirability orders. Ranks decrease; rank/(occupied predecessors+1) may increase (3/2 -> 2). Recompute subset normalizers.
- Conditional gate probabilities may vanish or increase by 2^|A|. Retained weights are incidence-feasible, but root odds lambda*pi and Lambda must change. Root/name costs are reference laws, not physical witness-root probabilities.
- Reused selectors require g_b restricted to selector=b before applying fresh-selector formulas. g_+(x)=x,g_-(x)=-x selected on x gives constant +1.
- Disjoint tensor spectra/references add complete cost and influence, even if an explicit positive minterm cover grows exponentially.
- For any balanced core with complete nonempty reference cost c_g, point activation on r>=1 fresh bits has a normalized projected reference cost <=h2(2p-p^2)+2r(2p-p^2)+p*c_g<=p*c_g+(6+2/ln2)pr, p=2^-r. Full arbitrary-core bill survives. Independent review pending.
- Sum identical decoded transcript outputs, then code empty/nonempty separately. Projection alone leaves a constant empty-atom bill on rare activation; vacuum separation removes it.
- Product references, fresh-character balancing and balanced-core activation preserve constant max(K,6+2/ln2) without depth loss. Restriction does not automatically preserve balance, boundary admission or orthogonality.
- Exact Walsh checker convention: bit-zero character sign +1; selecting g on bit-one yields (hhat-ghat)/2. Gibbs can be equality; exact reference=P handles equality before interval comparisons.
- Frozen 60s checker unexpectedly took 65.065931s under the shared machine. Future computation needs an internal 55s cutoff; do not relaunch a passing enumeration just to improve timing.
- Late B03 v1 direction consumed: actual ten-control restriction of OR(AND(z,y1),AND(z,y2)) increases label/subset/rank-rarity helper expectations from upper bounds 5/1024,55/1024,231/1024 to child bounds 17/16,1/16,3/10. This is pointwise only; child weight is 1/1024. No direction was rejected.
- Four levels F_d=MUX_x(F_(d-1),z_d) using the same physical x have formal read d+1 but reduce to MUX_x(y,z_d): two probability-1/4 gates, lambda=1/2, root probability 1/9, H=2,I=3/2. Contradictory clauses are not nonconstant queue gates.
''',encoding='utf-8')
required=protocol['required_per_run']['report_fields']
for heading in required:assert '## '+heading in report
for p in RUN.rglob('*.json'):json.loads(p.read_text(encoding='utf-8'))
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in RUN.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write(RUN/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'local_schema_check':'PASS','claim_count':1,'files':files,'remote_mirror':'not performed; supervisor-owned'})
print('Required artifacts, exact protocol fields, JSON parses, sizes and rolling status: PASS')
