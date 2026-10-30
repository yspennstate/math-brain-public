# A016 stage 4: two weak shared separators with a single paid private reserve

Full FEI remains OPEN. This stage consumes A018's independent acceptance of the previous A016 connected-spine theorem and A019's exclusive derivative account. It closes the recorded next benchmark: two shared coordinates, unequal nonlinear masks, and no uniformly influential shared first pivot. This is a scoped test and payment certificate, not a universal separator-selection theorem or a new literature priority claim.

## exact target, quantifiers, hypotheses and units

All physical bits are independent fair bits in {0,1}; Boolean outputs are signs; entropy and complete reference CE are in bits. For every integer a>=1, every even m>=4, and every list of arbitrary Boolean masks A_j:{0,1}^2->{0,1}, let z,w be shared and let t_j be disjoint m-bit private blocks. Put

\[
c_j(t_j)=(-1)^{t_{j,1}t_{j,2}+\cdots+t_{j,m-1}t_{j,m}},\quad
P_j=1_{t_j=0},\quad f_j=c_j-2A_j(z,w)P_j,\quad F=\prod_j f_j.
\]

Since c_j(0)=1, these are actual Boolean functions. Let delta=2^-m, p_j=E A_j, P=sum p_j, J=I_private(F), d=Inf_z(F)+Inf_w(F), and E_zw=sum_{S contains z,w} Fhat(S)^2. The prescribed stopping tree queries z, then w on both children, and stops with the complete private products. Define T=sum_v Pr(v) 2I(D_v), and T_bad by keeping only nodes with exact B_v>4 Inf_v. The claimed all-parameter statements are

\[
J=am/2+2m\delta P,\quad I(F)=J+d,\quad
T=T_{private}+2E_{zw},\quad T_{private}\le2J,\quad
2E_{zw}\le d,\quad T_{bad}\le T\le2I(F).
\]

All terminal masks have complete uniform code cost am. The same private reserves and the one physical shared budget pay

\[
am+T+(3/\ln2)d\le4I(F).
\]

One fixed whole-set reference, explicitly defined below, has CE<=min(am+2,am+T+(3/ln2)d)<=3I(F). The terminal-inclusive physical-tree ledger is paid at rate4, separately from the stronger rate3 reference estimate.

For a=2 and unequal masks A_1=AND(z,w), A_2=OR(z,w), the root is connected and both shared influences equal delta, hence tend to zero. For every even m>=12, all three internal nodes are exact K4-bad. Nevertheless T/I tends to zero and CE/I tends to2. Thus low influence and badness at both candidate shared pivots do not by themselves prevent a paid stopping prefix.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json completely, revision2026-10-11-execution-v2; BOARD.md beginning with supervisor snapshot2026-10-14 01:10 UTC and later the middle stream entries; B04 STREAM_NOTES.md v2,2026-10-11 23:25 UTC; own STATUS.md and previous run REPORT/CLAIMS/PROGRESS/checker. Required campaign and paper context was read in earlier stages and is not a new theorem dependency here. No external source was needed.

New source-bound reads: A018 run20261013T222945Z-fleet05-A018-shared-data-collision-law REPORT.md sections1-5, including its independent HOLDS verdict for A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1, exact shared-bit TC/reference interface, and still-unproved paired-row scalar proposal. A019 run20261013T235305Z-fleet05-A019-orthogonality-extensions REPORT.md sections2-6 and CLAIMS.json: A019-FOLDED-SEPARATOR-OWNER@1. A020 run20261014T002716Z-fleet05-A020-selector-boundary-tests REPORT.md: sharp width-dependent repeated-owner obstruction and its joint-phase paid control. B04 lead CLAIMS.json pins B04-NODE-BOUNDARY@1; its independent reconstruction in A018 stage2 was already read and consumed in the previous stage. Byte hashes/read scopes are saved in out/SOURCE_RECEIPTS.json. The board is mutable; its final hash is a readback receipt, not a claim that the initial snapshot stayed unchanged.

This work follows protocol dispatch: resume the recorded two-shared-coordinate target and consume useful new ownership/review dependencies. No broad universal candidate is opened; the B04 unreviewed-candidate cap is respected by a scoped application and independent review.

## complete derivation or exact first unsupported line

### 1. Physical influence and genuine weak pivots

Flipping the value at the private origin adds two directed pivotal edges in each private direction because the paired quadratic equals+1 at the origin and at every adjacent point. A module activated at shared value b therefore has private influence m/2+2m delta. Averaging its activation gives J_j=m/2+2m delta p_j, and different private blocks cannot cancel each other's influences in the product. Hence J=sum J_j as displayed.

For a shared edge b,b' let s(b,b') be the number of masks whose value changes. Each changed module toggles precisely when its independent private block is at zero. Thus the product edge disagreement probability is

\[
d(b,b')=[1-(1-2\delta)^{s(b,b')}]/2.
\]

Average over the other shared bit to obtain each actual shared influence. Union bound gives d<=delta sum_j I(A_j as a Boolean sign). Each two-bit mask has I(A_j)<=4p_j: in each direction at most twice its support fraction is pivotal. Therefore d<=4delta P. In particular, for fixed a every shared influence is at most a delta and vanishes with m; no constant-influence shared pivot is assumed.

### 2. Reconstruct the accepted one-bit ownership interface

For arbitrary one-shared-bit modules with disjoint private cubes, character folding gives delta_j=min(d_j,1-d_j), q_j=1-2delta_j>=0. Their folded shared product has delta_*=(1-product q_j)/2; the original product has shared influence delta_* or1-delta_* and at least delta_*. For k_j=a_j b_j, Parseval/Poincare and the product-edge union bound give

4delta_j(1-delta_j)=Var(k_j)<=I(k_j)<=I(a_j)+I(b_j)=2J_j.

So J_j>=delta_j, and parity of independent disagreements proves 0<=sum delta_j-delta_*<=J-delta_*. The private-character fixture a_j=1,b_j=chi_{t_j} gives equality for every number of modules, establishing coefficient1 sharpness. Character shifts preserve Fourier entropy and pushed-forward complete CE.

For C_j=sum_U |U| ahat_j(U)bhat_j(U), a private derivative expansion gives I(D)=sum_j[J_j-Q_-j C_j]/2. Since kappa_j=(J_j-C_j)/2, this is t_j=(1-Q_-j)J_j/2+Q_-j kappa_j, with0<=t_j<=J_j. A normalized reference supplied for each child lifts through the mixture of child references and the actual parent conditional selector law. Log-sum gives root KL<=average child KL, hence root CE<=average terminal CE+Delta H. Inserting the reviewed B04-NODE-BOUNDARY@1 yields A019's stated sufficient allocation. This independently reconstructs A019-FOLDED-SEPARATOR-OWNER@1 at its exact scope, without a repair or use of its unproved optional scalar inequality. The present finite tests validate its derivative formula on a new restricted module family; they are not an exhaustive census of arbitrary modules. Verdict HOLDS; the universal allocation-existence line remains outside its statement.

### 3. A stricter half-private account for every actual shared edge

Fix one of z,w and a value of the other. Denote module endpoints by a_j,b_j. Let e_j indicate whether its mask changes and let Q_-j=(1-2delta)^{sum_{h!=j} e_h}. Its intrinsic derivative is0 or plus/minus P_j, so

\[
\kappa_j=m\delta e_j/2,\qquad
J_{j,edge}=m/2+m\delta(A_j(b)+A_j(b')).
\]

The independently reconstructed formula gives

\[
t_{j,edge}=(1-Q_{-j})J_{j,edge}/2+Q_{-j}\kappa_j.
\]

Here Q_-j is between0 and1 and kappa_j<=J_{j,edge}/2 (already true for delta<=1/2). Consequently0<=t_{j,edge}<=J_{j,edge}/2. Average over the other shared bit and sum the two query directions. This defines one owned account u_j, not a fresh private budget for each direction. Since each direction's averaged J_edge equals J_j, u_j<=J_j. Put T_private=2sum_j u_j<=2J.

The root z derivative contains one additional remaining-w energy E_zw. After z is restricted, the w derivatives have only private coordinates. Their weighted private energies give precisely the two edge averages just used. Equivalently Parseval gives

\[
T_{private}=2\sum_S |S\cap private|\,|S\cap\{z,w\}|\widehat F(S)^2,\qquad
T=T_{private}+2E_{zw}.
\]

Also E_zw<=min(Inf_z,Inf_w), so2E_zw<=d. Thus T<=2J+d<=2I. Exact bad-node filtering can only decrease this nonnegative bill. No assertion that those nodes are good is needed.

### 4. Retain every terminal and pay the shared cross energy once

At each of the four physical leaves use the normalized uniform reference on all am private Fourier bits, costing am, including the empty set. Assign each private block the single budget4J_j. Its terminal code and both directional boundary accounts cost m+2u_j<=m+2J_j; the remaining private reserve is at least2J_j-m=4m delta p_j. Summing gives reserve at least4m delta P.

The two-query influence telescope consumes exactly d, and the reviewed node inequality sums to

Delta_block H<=T+(3/ln2)d.

Write c=3/ln2. Since ln2>1/2, c<6. The extra shared/cross terms cost c d+2E_zw<= (c+1)d<7d. The single shared allocation4d leaves an additional need at most3d<=12delta P. The above private reserve is at least16delta P for m>=4. Therefore

am+T+c d<=4(J+d)=4I.

Every component is named: leaf cost m, owned private boundary2u_j, shared budget4d, and the residual point-edit reserve. No child entropy or KL rebate is spent a second time. The sufficient rate4 bound uses the reviewed node lemma; the exact T<=2I statement is self-contained.

### 5. One fixed normalized whole-set reference

For private Fourier set R and shared set L subset {z,w}, define actual row mass r(R)=sum_L Fhat(L,R)^2 and the fixed conditional nu(L|R)=Fhat(L,R)^2/r(R). Set

Q(L,R)=2^-am nu(L|R).

These conditionals are explicit functions of the four known leaf spectra: Fhat(L,R)=one-quarter sum_b chi_L(b) product_j[c_jhat(R_j)-2delta A_j(b)]. They are fixed for the function before sampling, not a choice of a new reference after observing a row. All private rows are positive: each terminal module coefficient is u times a sign or u times a sign minus2delta, nonzero for even m>=4. Reference normalization is exactly one. The zero true atoms are harmless and all branch, private, empty-sector and final shared ambiguity costs are included.

Its complete CE is am+B_block. Since B_block<=2 and I>=am/2, and am>=4,

CE<=am+2<=3I.

More substantively, entropy concavity of r=average actual terminal spectra gives H(r)>=average H(leaf). Hence CE<=am+H(F)-average H(leaf)<=am+T+c d<=4I: the owned physical ledger pays this same fixed reference. This concavity comparison is proved directly; neither A018's optional scalar inequality nor an oracle universal FEI reference is assumed. The rate3 bound is a width-two code bound, not advertised as a universal or new restricted FEI theorem.

### 6. Unequal AND/OR fixture: every shared query is bad and weak

Take a=2, A_1=zw and A_2=z OR w. Exactly one module changes on every shared edge, so Inf_z=Inf_w=delta, J=m+2m delta, I=m+(2m+2)delta. The unique GF(2) phase is the sum of the private quadratic phases plus zw P_1+(z+w+zw)P_2. The distinct highest monomials zw product t_1 and zw product t_2 connect all coordinates; they cannot cancel. Thus no nontrivial disjoint sign factor removes the shared interaction.

Write u=2^-m/2. The bent private coefficients are u e_j, e_j in {+1,-1}, with multiplicities N_+=(2^m+2^{m/2})/2, N_-=(2^m-2^{m/2})/2. For each private sign pair the four shared coefficients, in empty,z,w,zw order, are

\[
\delta e_1e_2-(3/2)\delta u e_1-(1/2)\delta u e_2+\delta^2,\quad
\delta u(e_1+e_2)/2-\delta^2,\quad
\delta u(e_1+e_2)/2-\delta^2,\quad
\delta u(e_1-e_2)/2+\delta^2.
\]

The closed spectrum gives E_zw=delta(1+delta)/2. The owned edge accounts give T_private=4m delta(1+delta), and therefore

\[
T=(4m+1)\delta(1+\delta).
\]

For equal private signs, the empty,z row weights are delta^2(1 minus/plus u)^4 and delta^3(1 minus/plus u)^2. Their ratio is at least1/(2delta), as (1-u)^2>=1/2 for m>=4. Keeping only the smaller-weight entropy term yields

\[
B_z\ge \delta(1-\delta)^2(m-1)/2.
\]

Indeed the two equal-sign classes have total smaller-sector mass delta(1-delta)^2/2, using the displayed multiplicities. On either z child exactly one module is a one-selector private point splice, while the other is an independent spectator. Each splice row has weights (u e-delta)^2 and delta^2, ratio at least1/(2delta), and there are1/delta rows. Therefore B_w,child>=delta(m-1). For even m>=12 both lower bounds exceed4delta; all three actual internal nodes are bad. This refutes the proposed *necessary* heuristic that a paid shared-first prefix requires a constant-influence or K4-good shared first pivot. It does not refute a sufficient good-pivot policy or universal coordinate selection.

Despite this exact badness,

T/I=[(4+1/m)delta(1+delta)]/[1+(2+2/m)delta] tends to0.

The complete reference is between2m and2m+2, and I/m tends to1. Thus CE/I tends to2. The registered limiting cost and boundary statements require only these squeeze bounds.

### 7. Honest universal gap and nonduplication

The first unsupported universal line is existence of a dimension-free separator/private-account policy with complete terminal references when a derivative changes an arbitrary terminal core, rather than a signed private point indicator with kappa<=J_edge/2. No such policy is proved. With k shared coordinates the present half-account only gives T_private<=kJ: it reuses the directional allowance k times, precisely the width problem exposed by A020. Moving from the two-bit test to arbitrary width by changing2 to k is not a universal closure.

The next mathematical target is to replace one point edit by an arbitrary child-certified private core and test whether kappa<=J_edge/2, or a signed terminal slack that replaces it, survives. This attacks the actual hypothesis enabling the paid ledger rather than collecting another bent-class example. A018's paired-row scalar target is preserved and is not repeated; A019/A020's own targets remain theirs.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the pilot. Domain: every one-module two-bit mask at m=4,6,8,10 (64 cases), every ordered mask pair at m=4 (256 cases), eight fixed triples at m=4, and four fixed pairs at m=6; total332 cases, n<=14. No symmetry quotient, randomization or automatic dimension escalation. Pilot four cases; full job maximum60 seconds, memory estimate80MB. No >300MB job was planned, so the memok gate was not required; observed peak memory was not measured. Jobs were sequential, with no GPU or background computation.

Commands from A016:

`python -X utf8 runs\20261014T011255Z-fleet05-A016-addressing-benchmark\code\check.py --pilot`

PASS:4 cases,156 exact assertions,0.0584501seconds.

`python -X utf8 runs\20261014T011255Z-fleet05-A016-addressing-benchmark\code\check.py`

Final PASS:332 cases,13,828 exact assertions,51.113445seconds. Actual integer truth tables/Walsh spectra, physical edge counts, separately constructed terminal spectra and actual tree descendants verify I, every private derivative account, raw/localized charges, exact K4 labels, normalized root Q, and complete-reference/payment bounds. Each completed fixture was saved immediately in out/PARTIAL.json. The earlier full attempt stopped on the constant mask15 after15 cases because independent entropy intervals made an exact-zero B upper endpoint positive. The corrected helper proves zero structurally from disjoint spectral sectors; no tolerance is used. out/FIRST_FAILURE.json preserves the failure and correction.

FORMULA_SPEC.json separately froze ten even values m=4,6,8,10,12,16,24,32,64,128. The four Walsh-sign classes and their multiplicities are analytically proved above; no high-dimensional truth table was constructed.

`python -X utf8 runs\20261014T011255Z-fleet05-A016-addressing-benchmark\code\formula.py`

Final PASS:10 exact closed-spectrum cases,82 assertions,0.9431004seconds. A first formula attempt failed to certify a sign at m128 because H-H(erased) subtracted two large entropy intervals. Direct positive rowwise conditional entropy terms certify the sign at unchanged precision. out/FORMULA_FAILURE.json preserves this correction. The widest m128 entropy intervals certify the required lower sign only; their midpoints are not reported as numerical values, and precision was not increased after the required sign was obtained.

All logarithms use Fraction range reduction and the36-term series 2sum_{j<36} z^(2j+1)/(2j+1), z=(q-1)/(q+1) in [0,1/3], with positive tail bounded by2z^73/[73(1-z^2)]. Division by an enclosing ln2 interval and outward2^-90 rounding gives proved bit intervals. No floating sign, entropy tolerance or limit extrapolation is accepted.

For the unequal pair the exact tables at m4 andm6 agree with the closed formula. Example m12: both shared influences1/4096; B_z/Inf is enclosed around6.72436464, B_child/Inf around13.44181459; all three nodes are bad; T/I=200753/201433088 and complete CE/I is enclosed around1.999352689. The analytical inequalities, not these finite numbers, establish every even m>=12 and both limits.

## proof dependencies and changed downstream conclusions

The family, exclusive half-account, exact T, connected unequal fixture, bad-node lower bounds, normalized reference and rate3 bound are self-contained. Only the terminal-inclusive rate4 ledger and its comparison to the same reference use B04-NODE-BOUNDARY@1, retaining A018's prior independent reconstruction. A019-FOLDED-SEPARATOR-OWNER@1 is independently reconstructed analytically at its stated scope; the stricter half-account is proved directly here. A018's current acceptance of A016's previous theorem is consumed, without editing the immutable original run or counting it as two reviews. A020's unbounded-width obstruction remains valid and constrains the next step.

B04/A018/A019/A020/A028/A064/A090/A091/A095/A097 receive a weak-pivot equality/control fixture and an explicit single-reserve ledger, including every terminal. They may use it to challenge arguments that require a good first shared query or accidentally duplicate private slack. It supplies no general all-dimensional reference construction, scalar paired-row proof, or public-priority claim. New scoped theorem independent review and supervisor adoption remain pending.

## one next mathematical action and independent reviewer

Replace one module's signed point-indicator derivative by a difference between two arbitrary child-certified private cores. Derive or refute the half-private account with both supplied terminal CE costs retained, and isolate the exact signed slack needed if kappa exceeds J_edge/2. Use the unequal AND/OR family as a mandatory weak-and-bad shared-pivot fixture and A020 as the width guard. Reviewers: A018/A019 for the owned account and reference, A090/A091 for the complete rate4 ledger. This is one mathematical action directed at the enabling hypothesis, not a new dimension census.

## actual persistence receipts or precise save blocker

The four protocol files, code/, out/ exact results/checkpoints, frozen specs, failure/correction records and source receipts are saved in this assigned run only. STATUS.md remains two lines; WORKLOG.md is appended and LEARNED.md updated. code/persist.py validates exact protocol key sets, identical PACKET_DELTA, report fields, final Universal bridge paragraph, file-size bounds and artifact hashes; out/PERSISTENCE.json records actual readback receipts. Independent review of the new theorem, supervisor copying and remote mirror verification are distinct and pending. No other agent or shared source tree was modified.

## Universal bridge

This stage advances C019 from a paid constant-influence shared pivot to a concrete connected two-separator family where both shared influences tend to zero and every internal query is exact K4-bad: its complete localized bill is bounded by2I, and a single physical/private allocation pays terminal code plus boundary and JS insertion at4I. C020 receives the same fixed normalized whole-set reference at3I, with CE/I tending to2 in the unequal AND/OR control. What remains is the arbitrary-core replacement for the half-private derivative inequality and a separator-width-independent policy; the present proof does not supply either. NEXT tests that precise account with supplied arbitrary terminal cores because it removes the class-specific hypothesis doing the payment, which is the shortest route from this benchmark to the universal stopping/reference bridge rather than another isolated bent-family result.
