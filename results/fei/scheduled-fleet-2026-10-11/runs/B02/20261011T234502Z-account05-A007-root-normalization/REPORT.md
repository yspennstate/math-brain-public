# A007 stage 2: reviewed incidence theorem and full activated-tribes ledger

## exact target, quantifiers, hypotheses and units

All logarithms and entropy are in bits except natural logarithms explicitly used in the convex dual. Primary packet A007, bridge C020 / lead target PI-J. First, independently review the whole A009 INCIDENCE_OPTIMIZATION.tex artifact. Second, fulfill the lead's requested activation closure, retaining every conditioned posterior residual term.

For all integers r,w>=1 let m=2^w, let C be r fresh core coordinates, and let m disjoint private blocks each contain w coordinates. Let A_r be the positive core conjunction and B the OR of positive private conjunctions b_l. Define F=2 A_r B-1. Its prime implicants are exactly the m conjunctions A_r b_l. Use one ordered cover per gate, with common core first, then private coordinates, and fixed lambda_l=1/m. The weights satisfy all incidence constraints; the representation/generator are fixed across output sets. Put p=2^-r, rho=2^-w=1/m, Q=(1-rho)^m, b=1-Q, gamma=6/5, v=Var(F), I_c=2rpb and I_d=2p Q m w rho/(1-rho).

There exist actual partition-forest posterior laws with the complete source residual

    R = v(Lambda+log Z) + E[E_eta B_lambda-H(eta)] <= (26/5) I(F).

Here B_lambda includes labels once per used gate, every root rarity, all subset congestion and rank costs, and M_l=1 is explicit. Expectations on nonempty spectral sets use their unconditioned masses. A normalized prior on complete scaled references, chosen globally at j=0, adds exactly v<=2I, so the residual plus prior is <=(36/5)I. This is a PI-J coding closure, not a new FEI class or an all-function theorem. Size/child-count/multiset constants are retained through K_ref in the underlying full entropy bound H(F)<=h2(v)+K_ref I+R.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md was the supervisor's 2026-10-11 23:39 UTC snapshot. B02/STREAM_NOTES.md v2, 2026-10-11 23:35 UTC, was read in full; it directs A007 to review A009, then activation AND tribes, and names PI-J. Own STATUS.md and previous stage results were read. EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was reread in full.

A009/runs/20261011T223308Z-account05-A009-fractional-incidence-optimization: INCIDENCE_OPTIMIZATION.tex, REPORT.md, CLAIMS.json and WEIGHT_CERTIFICATE.json were read. CLAIMS.json is empty: the review pins source hashes, not a fictitious claim ID. A094/runs/20261011T224936Z-account05-A094-proof-chain-challenger/AUDIT.md was read in full. It independently accepts A006 and A007 and identifies a zero-root-cost single-gate rank obstruction. No such single-gate calibration is repeated here.

The source-complete queue interface is the same source_material/reductions/paper/forests.tex read in stage 1: eq:forestconditioning, eq:forestcost, thm:posteriorforest and its lambda-child generator. The seed mixture interface was already read in SEED_LEMMAS Section 2. Source files are hashed again in out/SOURCES.json. A094's acceptance is recorded locally for the original A007 statement, without changing its prior run or any shared registry. This stage supplies a whole A009 review before opening its one activation continuation claim.

## complete derivation or exact first unsupported line

### A. Whole A009 review

The independent reconstruction is saved immediately in REVIEW_A009.md. Verdict HOLDS at stated scopes, with no repair supplied: fixed-law log-weight convex program and sufficient exact dual certificates; actual duplicate-dictator counterexample to joint posterior convexity; full r,m singleton-petal R<=8I continuation and paid prior; geometric sunflower pressure <41I; and affine-plane positive pressure >=7I log((Q+1)/2), all prime powers Q>=16, for every feasible vector and pivotal tie decomposition.

The affine-plane result only bounds positive coordinatewise pressure. Its full conditioned residual, PI-J and FEI are not refuted. Independent finite checks reconstruct physical boundaries at Q=2,3, line geometry at six prime Q, all four rational KKT certificates, and the singleton activation ledger, without importing A009's code. The analytic review proof covers every Q>=16, including nonprime prime powers.

### A2. New retained-normalizer affine-plane consequence

The reviewed affine-plane argument can be strengthened for the coordinatewise fractional bound itself, keeping its negative normalization rather than hoping it is negligible. For every prime power q>=16, all feasible positive weights, and every pivotal tie decomposition, put rho=2^-q, k=q+1, N=qk, u=sum_l lambda_l and z_j=sum_{l through j}lambda_l. Then

    P + v log Z >= [7 log((q+1)/2)-5] I.

This is still not a lower bound on the full partition-forest residual or PI-J. It proves the coordinatewise fractional bound cannot obtain an absolute constant even by optimizing all weights and retaining its negative v log Z.

To prove it, retain the row mass in Holder instead of replacing it by one. The reviewed cap q_{j,l}<=2/k gives

    P >=7I log(k/2)-(11/5) sum_j alpha_j log z_j
       >=7I log(k/2)+(11/5)I log(q/u).

The second step uses point transitivity of the affine-plane Boolean function, hence constant alpha_j, and Jensen: average_j z_j=u/q, because each line contains q points. Incidence gives 0<u<=q. Root product expansion gives D>=rho u, so Z=D/(1+D)>=rho u/(1+rho u), and therefore

    log Z >=-q+log u-log(1+rho q).

This inequality retains the entire negative normalizer. The reviewed clean-event influence bound and the union bound on the true probability give

    I>=2qN rho(1-epsilon_q), v<=4N rho,
    qv/I<=2/(1-epsilon_q)<=4, v/I<=4/q<=1/4.

Thus v-(11/5)I<0. Adding the two displayed bounds, the scale-dependent part is (v-(11/5)I)log u, minimized at the largest allowed u=q. Consequently

    P+v log Z >=7I log(k/2)+v log q-qv-v log(1+rho q)
       >=7I log(k/2)-5I,

since log q>=0, rho q<=1, qv<=4I and v<=I. This is an all-weight proof, not a statement about uniform weights only. In particular making root weights arbitrarily small makes the label pressure increase faster than the negative normalizer can refund it. A009's original scope remains accepted; this stronger retained-normalizer consequence is A007's new contribution and awaits independent review.

### B. Exact Boolean law and real forest laws

For a private Fourier set T, write T_l=T intersect block l, s_l=|T_l|, t=#nonempty T_l. Product expansion of B=1-product_l(1-b_l) gives Bhat(empty)=b and, for T nonempty,

    Bhat(T)=-product_l [ -rho if T_l nonempty; 1-rho otherwise ].

For every nonempty U union T, U in C, Fhat(U,T)=2p Bhat(T), and Fhat(empty)=2pb-1. Hence

    v=4pb(1-pb), I(F)=I_c+I_d,
    E t =4p Q m rho =4p Q,
    E K-v=4p^2 Q(m rho-b)=4p^2 Q^2.

The touched-block formulas follow by tensor norms: each complementary factor has total squared norm 1-rho and nonempty mass rho(1-rho); summing contributions of a touched block gives Q rho. Physical edge counts give I_c=2rpb and I_d=2p Q m w rho/(1-rho), independently of spectral calculation.

The posterior consists only of these distinct finite queue runs:

- U nonempty, T empty: one gate owns all U; choose the m roots uniformly, with no children. H(eta)=log m.
- U and T nonempty: choose a touched petal as root, assign it all U and its T_l, and give every other touched petal its own T_l. Attach each child through the first selected core coordinate; choose all ordered child-gate sequences. There are t*(t-1)!=t! distinct events, chosen uniformly, so H(eta)=log(t!).
- U empty, T nonempty: each touched block owns its coordinates and is an isolated source component. All t touched gates are roots, queued in the fixed initial order; H(eta)=0.

All chosen subsets are nonempty, partition the output and lie in the owning support. Each gate is visited once. For mixed sets the root reaches every used gate through the selected core coordinate; its strongly connected component is the unique source. Thus these are actual admissible partition forests. Child permutations are distinct chronological random draws, not alternative descriptions of a single run. The small-domain checker constructs their actual ownership/child traces independently and checks uniqueness.

### C. Root rarity and normalization, kept together

All pi_l=p rho, so every root rarity is r+w. With fixed lambda_l=1/m,

    D=product_l(1+lambda_l pi_l)-1=(1+p rho/m)^m-1,
    Lambda+log Z=log D=-(r+w)+delta,
    0<=delta<=p rho log e.

The last bound follows from p rho<=D<=p rho exp(p rho), not from floating point. Therefore the exact root part, including normalization, is

    v log D+(r+w) E K = v delta+(r+w)(E K-v).

Core rarity and all petal rarity are canceled once per nonempty set; exceptional extra roots retain both scales. Since E K-v<=4p^2 Q m rho,

    (r+w)(E K-v)/I_d <=2p(1-rho)(1+r/w)<=2,

using p<=1/2 and rp<=1/2. Also

    v delta<=4pb *p rho log e<=(log e)I_c.

This pays the entire root/normalization contribution by 2I_d+(log e)I_c. No base rarity is left unpaid in this uniform-width closure. The negative normalization has already done its mathematical job before taking an upper bound.

### D. Every rank term

F_l^j is the logarithm of the physical position in gate l divided by the selected-predecessor count plus one. For a selected core coordinate of rank j, the preceding core selection is Bin(j-1,1/2), including on core-only spectra. For a selected private coordinate at internal rank j, the preceding core selection and preceding private selection in its own block are jointly Bin(r+j-1,1/2). Indeed, conditioning on this private coordinate being selected makes the other private coordinates in that block uniform: the conjunction's nonempty Fourier coefficients all have the same magnitude. The coefficient 2p Bhat(T) is independent of U, so the core subset is independently uniform.

This conditional assertion remains valid under our root posterior: every private coordinate is assigned to its own gate; its F_l^j depends on A, not on which touched gate became root. Core coordinates see the same order at every root.

For any rank h, the identity E[1/(1+Bin(h-1,1/2))]=2(1-2^-h)/h and Jensen give

    E log[h/(1+Bin(h-1,1/2))] <=1.

Consequently the whole natural rank term (gamma/ln2) E sum_j F_tau(j)^j is at most gamma I(F). Cover multiplicity is exactly zero because M_l=1, not because it has been discarded.

### E. Every subset-congestion and gate-label term

The root of a mixed star owns U union T_l and has s_root=kappa_root, hence zero congestion. A private leaf owns s_l>=1 coordinates while kappa_l=|U|+s_l. Its congestion is gamma s_l log(1+|U|/s_l). Core-only and empty-core sets have zero congestion. Pointwise s log(1+u/s)<=u log e, so the full congestion is at most gamma |U| t log e on nonempty-data sets. Conditional on T nonempty, U is uniform, yielding

    E congestion <= gamma (r/2) E t log e
       =2gamma rp Q m rho log e <=gamma(log e)I_c.

For the last inequality Q m rho<=1-Q=b: expand (1-rho)^-m>=(1+rho)^m>=1+m rho and rearrange. This is the key activation payment: a shared-core subset charge is paid once from the core influence, without charging log(r+1) separately to every private spectral coordinate.

Each used gate contributes L_l=log m=w. On core-only spectra, posterior entropy log m cancels that label exactly. On every other spectral set there are t used gates, with nonnegative posterior entropy, hence

    E labels-H(eta) <=w E t=4p Q m rho w
       =2(1-rho)I_d<=2I_d.

The exact ledger retains the mixed-set saving -log(t!) rather than requiring it for the upper bound. Every label is counted once per used gate, not once per selected coordinate.

### F. Full residual assembly and paid prior

Summing C, D and E retains the whole B cost and its actual-run entropy:

    R <=(4+gamma)I_d + [gamma+(1+gamma)log e]I_c.

Since gamma=6/5 and ln2>2/3 by the positive atanh series, log e<3/2. Thus the second coefficient is <9/2 and the first is 26/5. This proves R<=(26/5)I for all r,w without increasing a computational dimension.

For a fixed prior use lambda_l^(j)=2^-j/m, w_j=1/[(j+1)(j+2)], j>=0, on entire conditioned generators. The references are subprobabilities and the weights sum to one. Choosing component j=0 globally adds v log(1/w_0)=v<=4pb<=2I_c/r<=2I. Thus R+paid prior<=(36/5)I. Each component keeps its own D_j, labels and all costs together. No free output-dependent scale choice is used.

The complete entropy inference still has h2(v)+K_ref I outside R; the theorem does not equate residual and entropy. The extra binary split is influence-paid via the baseline h2(v)<=2I.

### G. Honest universal boundary

No line in the activation theorem remains unsupported after the preceding derivation; independent review of this new continuation is pending. The first unsupported universal line is that arbitrary PI-J spectra permit a joint law whose gate-label and rank/subset cost is influence-paid. Our binomial rank law and product touched-block mass rely on disjoint conjunction petals. They do not follow from root cancellation for arbitrary overlapping prime implicants. A009's affine-plane coordinatewise pressure failure is a useful next test, not an obstacle already bypassed by this theorem.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json fixes the domain before the job: four rational KKT certificates (one Boolean, three explicitly abstract); six prime affine geometries Q=2,3,5,7,17,19, with complete physical boundary censuses only at Q=2,3; epsilon arithmetic for Q=16..128; 12 A009 singleton activations r=1..3,m=1..4; six activated-tribes cases r=1..3,w=1..2,m=2^w,n<=11. No automatic dimension escalation, GPU or background worker. Estimated memory 60 MB, below the 300 MB preflight threshold.

Command from A007: `python -X utf8 runs/20261011T234502Z-account05-A007-root-normalization/code/check.py --freeze`, then without `--freeze`. Independent integer Walsh transforms and physical edge counts certify coefficients, variance and influence. Fraction arithmetic certifies root-count and touched-block identities, KKT stationarity, initial-root algebra and incidence. Actual forest traces are constructed and deduplicated. The complete residual is a rational linear combination of logarithms of rational numbers; a 24-term rational atanh expansion, with its geometric tail bound, encloses each logarithm. Signed coefficient multiplication uses the proper endpoint orientation. Thus every finite residual sign is an exact interval certificate, not a floating-point search. Numeric ratio fields are display-only; exact endpoints are persisted in out/CHECK.json. The saved output records assertion count and observed runtime.

These finite checks support the review and proof. They do not prove all-r,w closure or all-Q affine pressure by extrapolation; the complete analytic bridges are in the derivations and REVIEW_A009.md. A009's code was not imported or executed.

Observed main pilot: 221,543 assertions, 30,716 distinct constructed partition traces, 1.058 seconds. A separate frozen follow-up (`code/normalizer_check.py --freeze`, then without the flag) checked the new retained-normalizer rational premises at q=16..128 and five positive total-weight scales per q, totaling 565 scalar cases and 2,712 assertions in 0.012 seconds. It estimated 5 MB and introduced no extra truth-table dimensions. NORMALIZER_FROZEN_SPEC.json and out/NORMALIZER_CHECK.json preserve that job. Total exact assertions across both jobs: 224,255. The all-weight/all-prime-power normalizer proof is analytic, not inferred from these finite scales.

## proof dependencies and changed downstream conclusions

Dependencies are the conditioned forest theorem, elementary finite entropy algebra and complete-reference mixture interface. The activation proof reconstructs its spectral/root/forest identities rather than assuming A009's unreviewed R<=8I. A094's acceptance of A007 v1 is consumed as review evidence, not as a premise for any new structural inequality.

Changed downstream conclusion: the common-core root theorem now has one source-complete PI-J continuation paying base rarity, labels, ranks and subset congestion uniformly, with R<=26I/5 for every activated tribes representation and an explicit paid prior. A009's entire theorem is independently accepted at the source's exact scopes, including its distinction between fixed-law convexity and joint nonconvexity. The new affine-plane consequence rules out the coordinatewise fractional bound even after retaining v log Z for every feasible scale, but A009/A010 must not treat this as a full PI-J obstruction. A006/A008 can reuse the exact activation congestion payment rather than a per-private-coordinate log(r+1) surcharge.

## one next mathematical action and independent reviewer

Next: derive a root-aware, data-witness-preserving transfer for overlapping PI-J forests, and have A009 apply it to the affine-plane whole-set code while retaining its joint label/rank bill. The first targeted missing quantity is the joint expectation replacing our product touched-block law, not another prime-weight optimization of its already refuted coordinatewise pressure. A086/A094 should independently reconstruct the activated-tribes conditional rank law, chronological stars and congestion-to-core-influence payment. A085 can challenge the interval certificates and this independent A009 review.

## actual persistence receipts or precise save blocker

The assigned run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, REVIEW_A009.md, FROZEN_SPEC.json, code/check.py, exact outputs, source hashes and persistence receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. Source statement hashes and review records bind the reviewed versions; prior runs and all other agents' files remain untouched. Supervisor copying, mirror verification and independent acceptance of the new continuation are pending.

## Universal bridge

C020 whole-set witness cost, in the lead's PI-J formulation, moves from a paid root component to a full residual <=26I/5 (<=36I/5 with a fixed paid prior) under shared-conjunction activation of tribes, while the whole A009 incidence artifact receives independent reconstruction. The retained-normalizer affine-plane consequence proves P+v log Z >=[7log((q+1)/2)-5]I for every feasible weight, eliminating normalization rescue of the coordinatewise bound. Universally, the product touched-block law and conditional binomial rank law still need replacements for overlapping prime implicants; the actual joint cost remains open. NEXT targets a data-witness-preserving transfer on that affine-plane whole-set code, so it addresses the exact universal bottleneck rather than adding another isolated calibrated family.
