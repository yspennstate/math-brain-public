from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
report=r'''# exact target, quantifiers, hypotheses and units

A050/B10 scoped repair is proved locally, with independent review pending. Full FEI remains OPEN. The failed potential is the universal biased singleton tax-free claim J<=M, where M=H(S_X|S_Y), J=I(X;T) in the actual physical-child/squared-spectrum channel, and L=H(F)-E H(F_X)=M+J. All entropies are Shannon bits and include the empty coefficient. This stage repairs that existing failed statement rather than opening another broad candidate while B10's review cap is reached.

Additional hypothesis (OI): in a common normalized product Fourier basis for two Boolean children g,h, every residual label T in their shared support satisfies |G_T|=|H_T|. Labels appearing in only one child are unrestricted. For any interior selector bias p, this implies J<=M exactly. For a fair selector it implies the stronger paid decrement L<=4 Inf_X(F), with sharp constant 4. For every finite physical fair restriction tree satisfying OI at every queried node, with arbitrary Boolean terminal leaves,

    H(F) <= 4[I(F)-E H-independent I(F_leaf)] + E H(F_leaf)
         = 4[I(F)-E I(F_leaf)] + E H(F_leaf).

The first display's 'H-independent' phrase is only explanatory: the exact formula is the second line. In particular, if all leaves satisfy H<=C_leaf I, then H(F)<=max(4,C_leaf) I(F). No hypothesis about terminal entropy is silently added. A stopping tree means actual physical restrictions, fair branch probabilities, no repeated physical query along a path, and a finite set of nodes; no spectral conditioning is substituted for physical restriction.

The hypothesis is the weakest sufficient one in the explicitly ordered tested chain below, not claimed globally weakest or necessary. Our unbounded application is a fresh fair selector between arbitrary equal-rank quadratic signs on the same arbitrarily large data block, including arbitrary linear/constant terms. Those functions have H(F)<=4 I(F); branches may have partially overlapping affine Fourier supports. Tensor products and hierarchical multiplexers with disjoint balanced child data blocks and these modules as leaves preserve the stated tree admission and bound. A common arbitrary independent factor preserves OI and the local decrement, while retaining its entire entropy as a terminal obligation.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full, revision 2026-10-11-execution-v2. Read README, CURRENT_STATUS snapshot 2026-10-11T20:06:24Z, claim/obstruction/packet registries, stream next actions, campaign plan B10/A050 acceptance contract. Board read at start: supervisor snapshot 2026-10-11 22:57 UTC. B10 STREAM_NOTES.md does not exist at the prescribed path. This absence is recorded as an access limitation; no contrary direction is inferred.

Read A046 REPORT (20261011T214251Z), A047 REPORT (20261011T220210Z), A048 REPORT (20261011T221822Z), A049 REPORT (20261011T224133Z), and A096 REPORT (20261011T215017Z). A046 identifies the original biased AND obstruction. A047 proves the already-known disjoint-support identity M=J=h2(p). A048's sections 1-4 require retaining common-factor terminal entropy and contracting irrelevant coordinates. A049 supplies the common-bias minimal witness and prevents balanced-child/fair-residual repairs. A096's projection tax is not needed here; the board records its sign typo and pending reviews. No such upstream author result is used as an unproved mathematical premise.

Earlier report tree runs B05/B09/B19 were inspected, with B09's channel and failed tax-free potential reconstructed independently below. Read supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source catalog; read ONE_BIT_ENDPOINT, BLOCK_RESTRICTION_IDENTITY, GAMMA_ENDPOINT_LEDGER, OVERLAPPING_PRODUCT_NOTE. Exact chain rules are distinct from a paid whole entropy; lifetime is distinct from dissipation; overlapping physical inputs do not give tensor additivity.

Inspected all four supplied paper texts with cp1252 decoding after a UTF-8 read failed. Threshold 38pp Proposition 7.1, Corollary 7.2 and section 8 shared-data identities are scope context; equal-rank OI permits shared data and partial overlap beyond disjoint spectral support. Earlier threshold 29pp does not contain that later shared-data scope. Percolation 30pp introduction and Theorems 1.1-1.3 distinguish spectral J from physical I under biases and concern crossing classes. Its other 31pp version has a weaker/conditional overlap-exponent claim. No percolation theorem, complete paper proof audit, or novelty claim is assumed here. SOURCE_MANIFEST.json binds source bytes and actual inspection scope.

# complete derivation or exact first unsupported line

## 1. Exact overlap law, with arbitrary product-biased data

Let G_T,H_T be real normalized child coefficients; both squared lists have sum one. Let C be their common support, w=sum_C G_T^2=sum_C H_T^2, b=sum_{T in C:G_T=-H_T} G_T^2, and a=1-w. Under OI every common coefficient is equal or opposite; outside C the two exclusive support masses each total a. For F=g at X=0 and h at X=1, independent P(X=1)=p, the parent selector-absent and selector-present masses in residual fiber T are

    A_T=((1-p)G_T+p H_T)^2,
    B_T=p(1-p)(H_T-G_T)^2,
    Q_T=A_T+B_T=(1-p)G_T^2+p H_T^2.

The physical-channel joint masses are (1-p)G_T^2,p H_T^2. Therefore L=M+J by the entropy chain rule, independently of any uncertainty theorem. In a common fiber, the posterior physical probability is p. In an exclusive fiber it is 0 or 1. Thus H(X|T)=w h2(p), and

    J=a h2(p).

On common equal-sign fibers B_T/Q_T=0; on common opposite-sign fibers it is 4p(1-p); on g-only fibers it is p; on h-only fibers it is 1-p. Their Q masses are respectively the common weights, (1-p)a,pa. Consequently

    M=a h2(p)+b h2(4p(1-p)),
    M-J=b h2(4p(1-p))>=0,
    L=2a h2(p)+b h2(4p(1-p)).                 (1)

This repairs J<=M for all interior biases, with no additive tax. At p=1/2, h2(4p(1-p))=h2(1)=0, so M=J=a and L=2a. Parseval gives c=E[gh]=w-2b, hence the actual physical selector influence is

    d=P(g!=h)=(1-c)/2=a/2+b.

Therefore L=2a<=4d, with equality exactly when b=0 (including the zero case). This is a payment of the complete decrement, not only of J. Under biased selector inputs d is still the physical pivotal probability; the biased spectral selector energy is 4p(1-p)d. Formula (1) is not a dimension-independent linear payment by that spectral energy as p tends to zero.

## 2. Terminal-corrected physical tree, influence never reused

At a fair physical split i of any Boolean u, every other coordinate influence is the average of the corresponding child influences, by conditioning the pivotal event on x_i. Hence

    I(u)=Inf_i(u)+(I(u_0)+I(u_1))/2.

For a finite physical tree with node reach weights pi_v, repeated substitution yields sum_v pi_v Inf_{i_v}(u_v)=I(F)-E I(F_leaf). Entropy telescopes on precisely the same tree as H(F)-E H(F_leaf)=sum_v pi_v L_v. OI and (1) imply

    H(F)-E H(F_leaf) <=4 sum_v pi_v Inf_{i_v}(u_v)
                         =4[I(F)-E I(F_leaf)].       (2)

This proves the target and max-constant closure. An irrelevant query has identical children and L=d=0; it incurs no artificial bias tax. If OI fails at some queried nodes, define the actual excess e_v=max(0,L_v-4d_v). The same argument gives the honest version of (2) with +sum_bad pi_v e_v. Bounding that bad-node residual is the remaining universal obligation, not a theorem asserted here.

## 3. Equal-rank quadratic signs, including shared data

Use uniform x in F_2^n. A quadratic sign is f(x)=(-1)^{q(x)}, where q has degree at most two including linear and constant terms. Let B be the polar alternating matrix: q(x+u)+q(x)+q(u)+q(0)=x^T B u, and r=rank(B). Its autocorrelation is

    E_x f(x)f(x+u)=(-1)^{q(u)+q(0)} 1_{u in ker B}.

The phase u->q(u)+q(0) is linear on ker B because its polar form vanishes there. Fourier inversion of the autocorrelation therefore gives fhat(S)^2=2^-r on one affine coset of (ker B)^perp and zero elsewhere. The support has 2^r elements. This proves the flat-spectrum fact for arbitrary n without assuming a literature result.

Any pair of quadratic signs with the same polar rank r has equal nonzero Fourier magnitude 2^(-r/2); it satisfies OI even if affine supports overlap only partly. For an affine support of dimension r, at least r coordinates vary: projection into all varying coordinates is injective, so their count is >=r. Every varying coordinate is fair on that affine support, giving I(f)>=r/2 and H(f)=r<=2 I(f). Thus the selector-first tree has two leaves paid at constant 2; (2) gives H(F)<=4 I(F) on this unbounded shared-data family. Rank zero includes characters and constants.

Strict partial-overlap example: g=(-1)^{y1*y2}, h=(-1)^{y2*y3} on three uniform bits. Both ranks are 2. Their common support is {empty,{y2}}, both common coefficients +1/2, so w=1/2,b=0,d=1/4. The fair selector F has L=1=4d, H(F)=3 and I(F)=5/4. This proves sharpness of local constant 4 while its full H/I is 12/5, not an FEI counterexample.

## 4. Ordered repairs, operations, and exclusions

The tested nested list is R1: distinct characters; R2: disjoint child Fourier supports; R3: OI; R4: unrestricted actual Boolean children. R1 implies R2 implies R3. Both sufficient implications are strict: a constant paired with a balanced fresh-character times a bent function gives disjoint non-character support; the quadratic example above gives partial overlap satisfying R3. R4 fails J<=M on the original biased AND witness. Thus R3 is the weakest sufficient condition in this tested ordered list only. Equal-rank quadratic pairs and isospectral pairs are useful additional subfamilies of R3; neither a global necessity theorem nor a globally weakest hypothesis is claimed.

For an arbitrary independent common Boolean factor k, child coefficients become G_T K_U,H_T K_U. Intersections factor and nonzero common magnitudes remain equal; w,b,d,M,J,L stay unchanged because sum_U K_U^2=1. However terminal entropy gains H(k), and terminal influence gains I(k); (2) retains both. No FEI bound on arbitrary k follows. Multiplying both children by a uniform residual character permutes their spectra, preserves w,b,d, and makes balanced versions if the character is on a fresh bit. Biased coordinate multiplication is not claimed to be a spectral permutation.

For disjoint tensors of admitted pairs, shared supports are products and magnitudes multiply, so OI remains true. For admitted physical trees, process factors one at a time; the other factors are common terminal factors at each query. Influence and entropy add, and leaf constants remain unchanged. For balanced Boolean branches on disjoint physical data blocks, their Fourier supports are disjoint in the full data label space: the only possible intersection is empty, and balancing removes it. Therefore a recursively built fresh-selector hierarchy of disjoint balanced OI modules admits a tree querying outer selectors and then each reached module's selector, with equal-rank quadratic leaves. Balance may be enforced using a fresh common character. Arbitrary depth, module dimension and tensor count are permitted; H<=4I persists. Physical selectors are fresh, and only the data inside each module may be shared.

OI is not closed under arbitrary data restriction. In the partial-overlap example, set y1=0: g becomes constant 1 while h remains a rank-2 quadratic. At their common empty label the magnitudes are 1 and 1/2, violating OI. Consequently we require OI only at actual queried nodes of the chosen tree and do not assert hereditary admission for every tree. Arbitrary weighted thresholds, arbitrary low-energy shared-data multiplexers, all reused-selector circuits, and percolation crossings are not shown to satisfy it. The accepted sparse-bent point-surgery obstruction has typical child g and child g-2 point: its coefficients are generally perturbed in magnitude, so this repair is not an admission proof for that obstruction tree. Blindly declaring it admissible would be the first unsupported line.

## 5. Retain the original obstruction

For biased AND sign 1-2XY with P(X=1)=P(Y=1)=1/4, squared parent masses (empty,X,Y,XY) are (196,12,12,36)/256; the residual Y-present mass is 3/16. The child at X=0 is constant, and the child at X=1 has spectral masses (1/4,3/4), so

    J-M=2 h2(3/16)-H(196,12,12,36 over 256)-(1/4)h2(3/4)>1/16.

The exact rational-log sign is reproduced in out/ORIGINAL_COUNTEREXAMPLE.json. The common empty magnitude is 1 versus 1/2, so the witness violates OI exactly where the repair requires it. Fair residual coordinates and balanced children alone do not repair the claim (A047/A049); common fresh-character balancing preserves that failing common magnitude ratio. In the uniform cube this AND is a harmless flat bent spectrum and does not disprove FEI.

The first unsupported universal line is the existence for every Boolean F of a physical stopping tree whose bad-node excess sum and complete terminal entropy are paid by one dimension-independent influence budget. Equation (2) proves that payment exactly on its declared nodewise hypothesis, not that hypothesis for all functions.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before searching. Exhausted all ordered Boolean pairs on 0,1,2,3 fair residual bits: 4+16+256+65536=65,812 pairs, no symmetry quotient. Tested every admitted pair by actual selector truth table, integer FWHT and Fraction probabilities; exact entropy equality was checked as rational coefficient vectors of prime logarithms, with identical vectors cancelling (no assumption of logarithmic algebraic independence). 16,788 pairs satisfy OI. Equal-rank quadratic validation separately covers 12,800 ordered pairs among the 128 quadratic truth tables on three bits. Biased-selector formula checks use p=1/8,1/4,1/2,3/4 for every admitted pair through two residual bits and the explicit partial-overlap example; common-factor checks use two prescribed Boolean factors. Maximum explicit dimension is seven; memory estimate 40 MB, runtime cap 60 seconds, no heavy job, no >300 MB allocation, no dimension escalation or GPU.

Command: python -X utf8 runs/20261011T230000Z-account05-A050-repair-with-scope/code/check.py. out/CHECK.json records PASS, 102,773 exact assertions, arithmetic runtime 10.3932101 seconds. No floating entropy comparison supplies evidence. The all-dimensional proof is the displayed derivation, not this census. The failed UTF-8 text read was an input encoding issue; cp1252 read succeeded. The original biased AND sign is reproduced by an independent rational atanh enclosure with range reduction; negative endpoint multiplication reverses interval endpoints and division uses all four corners of the positive ln2 interval. Its finite sign is secondary regression evidence.

# proof dependencies and changed downstream conclusions

The proof uses only exact product Fourier expansion, finite Parseval, entropy chain rules, physical pivotal conditioning, affine-character orthogonality and elementary logarithm remainder estimates proved in code. No unaccepted B09 upper uncertainty theorem, A096 tax bound, or upstream quadratic theorem is a mathematical premise. A047 disjoint-support identity is credited as the already established special case, not rediscovered as new. A048 terminal-factor guards are fully respected.

Downstream change: A095 can extract a proved unbounded equal-rank quadratic shared-data selector theorem H<=4I; A057/A064/A073 can use the exact OI node decrement and actual bad-node residual in a proposed C019 transport. A048's arbitrary common factor remains terminal, and A049's witness is excluded by a checkable magnitude condition. B10's cap is respected by repairing the existing failed potential with one bundled scoped version. The universal good-tree existence and bad-node payment remain open.

# one next mathematical action and independent reviewer

NEXT: for the accepted sparse-bent surgery family, quantify the excess in (2) at the first node where OI fails, using exact child magnitudes and the already specified control-first tree; determine whether earlier control influence pays that excess with its terminal core retained. This directly tests extension of the payment mechanism beyond flat spectra. A092 primary independent reviewer; A087 alternate, with A094 quantifier/terminal audit. Consumers A095, A057, A064, A073, A048, B09 and B20.

# actual persistence receipts or precise save blocker

Saved only inside A050: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, SCOPED_REPAIR.tex, REPAIR_APPLICATIONS.md, FROZEN_SPEC.json, SOURCE_MANIFEST.json, code/check.py, code/finalize.py and exact output/receipts. Rolling STATUS.md is two lines; WORKLOG.md and LEARNED.md are current. Finalizer validates exact protocol key sets, statement hashes, progress-copy identity and all artifact sizes below 20 MB, then writes out/PERSISTENCE.json. No git, Brain write, messages, shared-index write or another-agent mutation was performed. Supervisor copying, mirror verification, downstream use and independent acceptance are pending and unclaimed.

# Universal bridge

This stage advances C019 stopping-tree payment from disjoint spectral children to children with equal magnitudes on their entire overlapping support: the complete decrement is paid sharply at 4 times actual selector influence, and the same-tree telescope preserves all terminal entropy and spends influence once. Equal-rank quadratic branches with shared data, tensor products and specified balanced disjoint-data hierarchies satisfy the condition in all dimensions; arbitrary data restrictions do not. What remains is a universal good-tree or bounded bad-node-excess theorem plus terminal payment. NEXT targets the exact nonflat sparse-bent failure node of that theorem, rather than expanding an isolated census or asserting another class alone solves FEI.
'''
report=report.replace('H(F) <= 4[I(F)-E H-independent I(F_leaf)] + E H(F_leaf)\n         = 4[I(F)-E I(F_leaf)] + E H(F_leaf).','H(F) <= 4[I(F)-E I(F_leaf)] + E H(F_leaf).').replace("The first display's 'H-independent' phrase is only explanatory: the exact formula is the second line. ",'')
(R/'REPORT.md').write_text(report,encoding='utf-8')
statement='For every Boolean child pair in a common normalized product Fourier basis satisfying |G_T|=|H_T| on shared support, with shared mass w and opposite-sign shared mass b, a fresh selector of bias p has J=(1-w)h2(p), M=J+b h2(4p(1-p)), hence J<=M. For a fair selector L=2(1-w)<=4 Inf_X, with sharp local constant 4. Every finite fair physical restriction tree satisfying this hypothesis at each queried node obeys H(F)<=4[I(F)-E I(F_leaf)]+E H(F_leaf). Equal-polar-rank quadratic Boolean children on arbitrary shared uniform data satisfy the hypothesis and H(F)<=4I(F); disjoint tensors and declared balanced disjoint-data selector hierarchies preserve the bound, while arbitrary common independent factors retain their terminal entropy.'
claim={'claim_id':'A050-OI-SCOPED-REPAIR','version':1,'exact_statement':statement,'hypotheses':['Actual Boolean sign children, common normalized product Fourier basis, equal magnitudes on shared support','Fresh independent selector; uniform physical coordinates for influence telescope','Finite physical restriction tree, hypothesis at each queried node; terminal entropy retained'],'statement_sha256':sha(statement.encode()),'contributors':['A050'],'proof_source':str(R/'REPORT.md'),'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Universal existence of a stopping tree paying bad-node excess and complete terminal entropy.','next_consumers':['A092','A087','A095','A057','A064','A073','B20']}
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B10','packet_id':'A050','gap_id':'G-R-MISMATCH','attempt_id':'A050-OI-v1','method':'Exact shared-support Fourier partition and physical same-tree telescope; quadratic autocorrelation admission','mathematical_delta':'Tax-free biased helper repaired under equal overlapping magnitudes; sharp fair-selector payment 4; terminal-corrected tree closure and unbounded equal-rank quadratic shared-data application','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_REPAIR_PROVED_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A050-OI-SCOPED-REPAIR/v1'],'source_artifacts':['REPORT.md','SCOPED_REPAIR.tex','REPAIR_APPLICATIONS.md','code/check.py','out/CHECK.json'],'next_consumers':['A092','A087','A095','A057','A064','A073','B20'],'next_action':'Quantify first non-OI-node excess on sparse-bent surgery control-first tree, retaining terminal core and nonreused influence.','stagnant_substantive_attempts':0,'blockers':['B10 lead notes absent; independent review and supervisor mirror pending'],'packet_ids':['A050']}
for n in ['PROGRESS.json','PACKET_DELTA.json']: (R/n).write_text(json.dumps(progress,indent=2),encoding='utf-8')
(R/'SCOPED_REPAIR.tex').write_text(r'''\documentclass{article}
\usepackage{amsmath,amssymb}
\begin{document}
\section*{A050 scoped repair (full FEI remains open)}
Let $g,h$ be Boolean signs in a common normalized product Fourier basis.
Assume $|G_T|=|H_T|$ whenever both coefficients are nonzero.
Let $w=\sum_{G_TH_T\ne0}G_T^2$ and
$b=\sum_{G_T=-H_T\ne0}G_T^2$.
For a fresh physical selector with probability $p$ of choosing $h$,
\[
J=(1-w)h_2(p),\quad M=J+b h_2(4p(1-p)),\quad L=M+J.
\]
Indeed shared fibers have physical posterior $p$; exclusive fibers have
deterministic posterior. The selector-present parent probabilities in each
fiber are $0$, $4p(1-p)$, $p$, or $1-p$, respectively.
Thus $J\le M$. At $p=1/2$, $L=2(1-w)$ and
$d=\Pr(g\ne h)=(1-w)/2+b$, so $L\le4d$.
The pair $g=(-1)^{y_1y_2},h=(-1)^{y_2y_3}$ has $w=1/2,b=0$
and attains equality with $d=1/4$.
For a finite fair physical tree with this condition at each queried node,
\[
H(F)\le4\bigl(I(F)-\mathbb E I(F_{\rm leaf})\bigr)
       +\mathbb E H(F_{\rm leaf}).
\]
This follows by telescoping both entropy and
$I(u)=\operatorname{Inf}_i(u)+(I(u_0)+I(u_1))/2$ on the same tree.
For a quadratic sign with polar matrix $B$, autocorrelation is a character
on $\ker B$ and zero off it; Fourier inversion gives a flat affine spectrum
of dimension $r=\operatorname{rank}B$. Hence $H=r\le2I$.
Equal-rank quadratic children meet the hypothesis and their fair selector
satisfies $H(F)\le4I(F)$. All terminal costs remain explicit.
No universal existence of such a tree is proved.
\end{document}
''',encoding='utf-8')
(R/'REPAIR_APPLICATIONS.md').write_text('''OI is equal child Fourier magnitudes wherever supports overlap.

| Intended application / operation | Verdict | Reason |
|---|---|---|
| Disjoint-support selector | YES | Shared-support condition vacuous |
| Isospectral children with arbitrary signs | YES | Shared masses agree |
| Equal-rank quadratic branches, shared data | YES, H<=4I | Flat affine spectra of equal mass |
| Partial quadratic overlap example | YES, local 4 sharp | w=1/2, opposite mass zero |
| Common independent factor | LOCAL YES | Magnitudes multiply; terminal H(factor) retained |
| Disjoint tensor products | YES | Product intersections; tree factor by factor |
| Uniform common-character balancing | YES | Spectrum permutation |
| Fresh-selector hierarchy on balanced disjoint-data modules | YES, H<=4I | Outer child supports disjoint, inner modules admitted |
| Arbitrary data restrictions | NO | Setting y1=0 in example leaves constant versus bent |
| Sparse-bent point surgery | NOT ESTABLISHED | Perturbation changes shared magnitudes |
| Arbitrary weighted thresholds / reused selectors | NOT ESTABLISHED | No nodewise admission proof |
| Percolation crossing families | NOT ESTABLISHED | No nodewise admission proof |

Nested tested repair chain: distinct characters => disjoint support => OI => unrestricted. The first three suffice; unrestricted fails on biased AND. OI is weakest in that tested chain, not globally weakest. A paid local decrement does not pay arbitrary terminal entropy.
''',encoding='utf-8')
# Source-byte receipts distinguish inspection from theorem acceptance.
paths=[]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']: paths.append(base/name)
paths.extend(base.glob('runs/*/*/REPORT.md'))
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
paths.extend(supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'])
paths.extend((supp/'sources').glob('*.md'))
team=A.parents[1]
paths.append(team/'BOARD.md')
paths.extend((team/'context').glob('*.txt'))
for a in ['A046','A047','A048','A049','A096']: paths.extend((team/'agents'/a).rglob('REPORT.md'))
manifest=[{'path':str(p),'sha256':sha(p.read_bytes()),'scope':'byte receipt; reading scope specified in REPORT, not independent proof acceptance'} for p in paths if p.is_file()]
(R/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A050 scoped repair complete: equal overlapping Fourier magnitudes pay L<=4 Inf; 102,773 exact checks; review pending; full FEI OPEN.\nNEXT: A092/A087 review; quantify first non-OI-node excess on sparse-bent control-first tree with terminal entropy retained.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write('\n2026-10-12 A050 stage: read protocol/board and B10 originals; lead notes absent. Proved equal-shared-magnitude tax-free repair and sharp fair-selector decrement 4, exact physical tree telescope, equal-rank quadratic admission. 65,812 pair screenings plus 12,800 quadratic pairs, 102,773 exact assertions PASS (10.393s). Arbitrary data restriction fails; common factors retain terminal entropy. Full FEI open; reviews pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('\nOI: |G_T|=|H_T| on shared Fourier support. Shared mass w, opposite shared mass b give J=(1-w)h2(p), M=J+b h2(4p(1-p)). Fair selector L=2(1-w), d=(1-w)/2+b, sharp L<=4d. Finite OI-node physical tree: H<=4(I-E Ileaf)+E Hleaf. Equal-rank quadratic signs have flat equal-amplitude spectra and H<=2I; selectors H<=4I. Common tensors preserve OI, arbitrary restrictions do not. Example q12/q23 with y1=0 becomes constant versus bent and fails OI. Universal bad-node residual and terminal payment remain open.\n')
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
ckeys=set(protocol['required_per_run']['claim_fields']); pkeys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==ckeys
assert set(progress)==pkeys
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
receipts={str(p.relative_to(R)):sha(p.read_bytes()) for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json'}
(R/'out'/'PERSISTENCE.json').write_text(json.dumps({'status':'PASS','schema_keys_exact':True,'schema_note':'Protocol explanatory suffix on packet_ids normalized to packet_ids, as required by its compatibility contract.','progress_copy_identical':True,'local_only':True,'files':receipts},indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','files':len(receipts),'claims':1,'full_fei':'OPEN'}))
