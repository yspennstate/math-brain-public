# A028 stopping-tree payment

Full FEI remains OPEN. This run proves a finite unbalanced-activation stopping ledger and independently reconstructs four existing B06 claims at their stated scopes. The new claim awaits independent review; registry adoption and supervisor copying are not asserted.

## exact target, quantifiers, hypotheses and units

All physical inputs are independent uniform signs; Fourier coefficients use the normalized Walsh basis; entropy and KL are in bits. Let g be ANY finite-dimensional Boolean sign, delta=Pr(g=-1), r>=1, p=2^-r, and A_r the indicator of one assignment of r fresh physical controls. Put F=1+A_r(g-1). The control-first tree queries controls in a fixed order, stops at the first failure, and otherwise reaches g with probability p.

At a split let a,b be the actual child Fourier coefficients, q_T=(a_T^2+b_T^2)/2, m_T=(|a_T|-|b_T|)^2/4, mu=sum m_T, and nu=m/mu when mu>0. Define the complete nonnegative logarithmic bill J=sum m_T log2(q_T/m_T)=mu[log2(1/mu)-D_2(nu||q)], with zero terms omitted. Write c=log2(e). The recovered split upper bound is Delta H<=J+3c mu. We prove

    E sum J <= (3+c/e) Q,
    E sum (J+3c mu) <= kappa Q,
    Q=2rp delta,  kappa=3+c(3+1/e)<8.

Therefore if g has an FEI-certified terminal allowance K I(g), the FULL expected upper path bill plus terminal allowance is at most max(kappa,K) I(F). This is uniform in dimension, r, delta and the spectrum of g. It pays the mismatch/KL bill itself, not merely the smaller exact entropy decrement.

The same constant holds for every finite expression built from certified terminals by fresh point activations, sign negations, and products on disjoint physical supports, with arbitrary expression depth and control arities. Fix k0,M0 for bounded-overlap terminals; their constants must not be treated as uniform when these parameters grow. Terminal products are certified by exact disjoint additivity; for an activation-only expression the reached leaves are the original recovered terminal or constants.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. BOARD.md was read first. B06/STREAM_NOTES.md was absent. The report README, CURRENT_STATUS, claim/obstruction/packet indices, STREAM_NEXT_ACTIONS and campaign plan were consulted. Supplemental CAMPAIGN, CLAIMS (C005,C006,C018,C019), COUNTEREXAMPLES (X001,X003,X004,X005), SEED_LEMMAS and NATIVE_MAPPING were read for this route. The sources directory was inventoried; the block restriction and erasure reductions and logarithmic-allocation interfaces are the mathematical inputs. Source hashes and observed scope are recorded in out/source_inventory.json.

The 38-page threshold text was consulted at Theorems A,C,D, Section 8.4 / Proposition 8.9 / Corollary 8.10 and the selector/block interface. Earlier threshold and both percolation versions were consulted for conventions and scope; no spatial theorem is imported. The percolation entropy statements do not make arbitrary restrictions geometric terminals. These text files require cp1252 decoding; an initial UTF-8 read failed and was corrected. This is not a cover-to-cover independent audit of the two large manuscripts.

Original A021 REPORT Sections 3-4 already pay the BALANCED control-first KL bill. This run does not rediscover that result. The extension here retains unbalanced means, the possible sign change in the last child, and a finite constant below the regular terminal constant. A026 GOOD_COORDINATE_TARGET.tex and A027 ADAPTIVE_BLOCK_SELECTION.tex were read from their original runs; reviews are in INDEPENDENT_REVIEW.md. The earlier canonical B05/B19 reports establish the scope obstruction, not a positive premise of this new theorem.

## complete derivation or exact first unsupported line

### 1. Actual control-node packets, including the sign-changing last child

At the active node with s controls left, let u=2^-s. The children are constant +1 and 1+A_(s-1)(g-1). The second child's mean is b0=1-4u delta. All its nonempty coefficients have zero matching coefficient in the constant child. Hence q0=(1+b0^2)/2 and m0=(1-|b0|)^2/4, while m_T=q_T/2 off the empty packet. Parseval gives

    mu=(1-|b0|)/2, m0=mu^2,
    J_s=mu-mu^2+mu^2 log2(q0/mu^2).

For s>=2, b0>=0 even at delta=1; thus mu_s=2u delta. For s=1, mu_1=min(delta,1-delta). The latter is essential: signed disagreement would be delta and is generally NOT the magnitude mismatch. At delta=0 or 1, expressions with zero masses are interpreted continuously.

The node has physical reach w_s=p/u. Its queried influence is d_s=2u delta, including s=1. Thus sum_s w_s d_s=2rp delta=Q and sum_s w_s mu_s<=Q. Physical data influence is p I(g), so I(F)=Q+pI(g) exactly. Every payment below is drawn from Q; pI(g) is reserved for the terminal.

### 2. Pay the complete logarithmic bill

Since q0<=1, for s>=2,

    J_s <= 2u delta+8u^2 delta^2 log2(1/(2u delta)).

For delta>0 write L=log2(1/(2delta)). Each summand 2^-s(s+L) is nonnegative for s>=2 and delta<=1. Therefore its finite sum is bounded by the infinite sum, even when L<0. Using sum_(s>=2)2^-s=1/2 and sum_(s>=2)s2^-s=3/2 gives

    sum_(s=2..r) w_s J_s
    <=2p delta[(r-1)+6delta+2delta L]
    <=2p delta(r+3).

The scalar inequality 6delta+2delta log2(1/(2delta))<=4 on [0,1] follows because its derivative is 6+2L-2c>=4-2c>0 and its value at 1 is 4. Here c<2 follows from ln2>1/2. The delta=0 limit is zero.

At the last node, set a=min(delta,1-delta)<=delta. The preceding packet formula and the scalar maximum x log2(1/x)<=c/e yield

    J_1 <= a+2a^2 log2(1/a) <= (1+2c/e)delta.

If r>=2, w_1=2p and these estimates give

    J_tree <=2p delta[r+4+2c/e]
           <=(3+c/e) Q.

The last inequality uses r>=2. If r=1, J_tree<= (1+2c/e)Q <=(3+c/e)Q, because c/e<2. Adding the full linear allowance 3c sum w_s mu_s<=3c Q proves kappa=3+c(3+1/e).

The strict bound kappa<8 is rationally certified: e>8/3 and ln2>=56/81 imply (3+1/e)/ln2 < (27/8)(81/56)=2187/448<5. Thus kappa<3+5=8. No floating approximation supplies a sign in this argument.

### 3. Exact entropy and terminal ledger

Independently, with eta(t)=t log2(1/t), m=1-2delta and v=4delta(1-delta), the spectrum gives

    H(F)-pH(g)
    =eta((1-2pdelta)^2)-p eta(m^2)
     +4p(1-p)delta^2 log2(1/(4p^2delta^2))+2rpv.

This expression includes the exceptional empty-control/data coefficient and ALL terminal entropy. The exact path costs telescope to this value; the upper mismatch bill bounds it by kappa Q. For terminal allowance K I(g),

    E sum(J+3c mu)+p K I(g)
    <=kappa Q+K pI(g)<=max(kappa,K) I(F).

Inactive leaves are constants with zero influence and entropy. Nothing assumes an FEI bound on arbitrary g: the terminal K is an explicit hypothesis.

### 4. Arbitrary depth without spending influence twice

Given a syntactic expression with fresh activation controls and physically disjoint product factors, construct its tree recursively. At an activation expose controls, stop on failure, and on success execute the core tree. At a product execute each factor's tree in any fixed order. If a residual factor is constant, its sign only changes the residual product's global output sign. For independent factors, squared spectra tensorize; H and I add, and all split q,m,J are unchanged by multiplication by an unqueried disjoint Boolean factor, since its Fourier squared masses sum to one. Thus factorwise path bills add as well. Global output negation leaves these quantities unchanged.

By induction over the expression, every activation pays its newly queried controls and passes its reserved weighted core influence to the core tree. Each product sums physically disjoint budgets. The expression tree is finite and each queried physical coordinate is used at most once along a path. At the stopping leaves, the remaining function is a product of the named certified terminals on disjoint cubes, with the sum of their valid FEI allowances. The constant is the maximum of kappa and their constants, independent of activation depth, arity, bias and number of factors.

For regular terminals take C_reg=log2(4+e)+2log2(e*pi)>8; for bounded-overlap terminals use 41+7log2(k0)+(29/5)log2(M0)>8; for uniform threshold/parity formula terminals use 744. The control closure preserves each of these constants. These are source-reported terminal theorems used conditionally on their recovered acceptance; this run does not re-audit their full proofs. The affine-dimension-four terminal theorem reviewed here has constant 7/2+2/ln2<8, so its activation closure has constant kappa<8.

First unsupported universal line: every arbitrary Boolean root admits such a finite fresh-activation/disjoint-product decomposition into certified terminals, or a different cheap physical tree reaching such terminals. No such representation theorem is proved. Arbitrary cores admitted as leaves would leave pH(g) unpaid and preserve full-FEI hardness via tensor amplification. Shared-input products and general signed multiplexer cells are excluded by actual hypothesis failures, not assumed to satisfy this lemma.

## executed validation with domain, arithmetic, commands and outputs

The specification out/FROZEN_SPEC.json was written before search. It fixes all cores in dimensions 0,1,2,3, r=1,2,3,4: 1112 activations, no symmetry reduction. A written census-total arithmetic typo was corrected from 33042 to 32906 with the frozen domains unchanged; the actual counts are 2,8,128,32768. The exact magnitude-mismatch extension was frozen in out/VALIDATION_EXTENSION.json before its execution, on the identical activation domain.

Command from A028: `python -X utf8 runs\20261011T221633Z-fleet05-A028-stopping-tree-payment\code\check.py`. Integer Walsh spectra are independently compared with coefficient formulas and direct physical edge counts. Entropy identities are equality of rational vectors multiplying logs of primes, which is sufficient to establish exact equality and needs no conjecture about logarithm independence. The checker also reconstructs the A027 core-fiber entropy identity, every A026 proxy inequality through n=4 modulo global sign, and the 32-bit threshold proxy via combinatorial Walsh summation. It does not use floating entropy signs. Infinite parameter bounds are supplied by the analytic proofs above and in the independent review.

The final v2 pass recorded 106858 assertions in 11.587 seconds, including the actual magnitude mismatch laws, in out/validation.json. The first v1 pass had 102410 assertions and 7.587 seconds. No heavy job or GPU was used; estimated memory is below 40 MB. No automatic dimension escalation, formal proof assistant, or external peer review is claimed.

## proof dependencies and changed downstream conclusions

The new claim uses the recovered actual-child mismatch bound Delta H<=J+3mu/ln2, Parseval, physical influence decomposition, and exact entropy/product identities. It does not depend on A026 or A027 for its activation calculation. Terminal certification may use the recovered paper or the reviewed A026 theorem. A021 is prior scope calibration, not an unproved premise.

Independent reviews here accept A026-AFFINE4-GOOD-COORDINATE v1, A026-AMPLITUDE-K4-THRESHOLD-NOGO v1, A027-DATA-FIRST-PROPER-BLOCK v1 and A027-CORE-BLOCK-HARDNESS v1 at their exact stated scopes; the originals are unchanged. Their review records are source-bound in CLAIMS.json and INDEPENDENT_REVIEW.md. This addresses the existing B06 pending-candidate cap before proposing the new narrower stopping lemma. The reviews are local mathematical acceptance, awaiting supervisor adoption; no shared index was edited.

A028's complete unbalanced control-path cost can feed A023/A029/A064/A065 without the error of equating magnitude mismatch with disagreement at the last node. A026 affine terminals can be inserted without using their full small-dimension proof again. A027's low-density core-block hardness remains intact; this new tree stops at a certified core and does not erase its entropy.

## one next mathematical action and independent reviewer

Consume A029's transport interface and derive the shifted-empty-row correction when a proper subset of a low-density core is revealed BEFORE its controls. The objective is a subtree residual paid by the remaining physical core boundary, extending beyond syntactically fresh activation closure. A087 is the independent reviewer of the new lemma; A094 should challenge the terminal admission and full dependency chain. The review records created here can be adopted by B20 after source inspection; no messages or registry writes were performed.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, independent review, proof checkpoint, frozen specs, checker and exact outputs are saved inside the designated A028 run. Rolling STATUS has two lines, WORKLOG is dated, and LEARNED retains exact hypotheses and constants. out/persistence_receipt.json records SHA256 and bytes of the saved artifacts; code/finalize.py checks exact protocol fields and progress-copy equality. Supervisor GitHub/Brain copying, independent acceptance of the NEW lemma, and downstream use remain unobserved.

## Universal bridge

This stage moves C019 by paying the complete unbalanced control-first mismatch/KL plus linear path bill with the finite coefficient kappa=3+log2(e)(3+1/e)<8, then retaining and separately paying the terminal entropy. It preserves the recovered regular, fixed-overlap and threshold-formula constants under arbitrary fresh activation/disjoint-product depth and reviews the existing B06 finite and proper-block premises. The universal structural admission of arbitrary roots is still open; rarity alone cannot provide it because arbitrary terminal cores retain full FEI. NEXT targets the exact remaining-core/shifted-row transport after a proper partial core exposure, which is the shortest route beyond this syntactic class because further terminal examples would not remove the representation gap.
