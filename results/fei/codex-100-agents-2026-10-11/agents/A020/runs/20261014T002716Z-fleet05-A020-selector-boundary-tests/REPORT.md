# A020 stage 3: joint shared phase defeats dimension-free repeated-owner payment

Full FEI remains OPEN. This stage independently reviews A019's single-separator ownership correction and refutes its natural extension to an unbounded shared block. The extension is a diagnostic proposed here, not a statement attributed to A019. The obstruction is connected, survives every global character orientation, and has a complete reference costing at most 4I.

## exact target, quantifiers, hypotheses and units

All cubes are uniform, all functions are Boolean signs, and entropy/CE are in bits. Write shared bits as Z_i in {0,1}, with sign characters (-1)^Z_i. For arbitrary integers k,r>=1, take disjoint private bits y_1,...,y_r and define A(Z)=product_i Z_i, f_j(Z,y_j)=(-1)^(A(Z)y_j), and F=product_j f_j=(-1)^(A(Z)(xor_j y_j)). Set delta=2^-k and J=I_private(F).

For a choice of shared characters chi_{C_j}, let f'_j=chi_{C_j}f_j and F'=product_j f'_j. Define the repeated shared influence loss L(C)=sum_j I_Z(f'_j)-I_Z(F'). The target tested is whether min_C L(C)<=KJ, or even <=K I(F), for a universal K independent of k,r. Both statements are false. This does not refute one-bit A019-FOLDED-SEPARATOR-OWNER@1, nor establish an FEI counterexample.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 00:19 UTC, B04 STREAM_NOTES.md v2 (2026-10-11 23:25 UTC), own STATUS.md and prior stage outputs. Read the execution protocol in full: 2026-10-11-execution-v2. Required campaign/context sources were consumed in the earlier stages; no new paper theorem is needed for the main obstruction.

New source-bound reads: A018 run 20261013T222945Z-fleet05-A018-shared-data-collision-law REPORT.md, shared-separator collision/TC interface and its unresolved averaged scalar bound; A019 run 20261013T235305Z-fleet05-A019-orthogonality-extensions REPORT.md sections 2-6 and CLAIMS.json, especially A019-FOLDED-SEPARATOR-OWNER@1; A016 run 20261013T214508Z-fleet05-A016-addressing-benchmark REPORT.md, connected shared-bit spine and its separator-first repair. The stream lead's finite census request was settled in stage 2; dispatch now consumes this new ownership dependency. No paired-row scalar search is repeated. Source hashes are persisted separately.

## complete derivation or exact first unsupported line

### Independent reconstruction of the one-bit owner theorem

For arbitrary modules with one common bit z and disjoint private cubes, fold each module by chi_z so its child correlation q_j=E[a_j b_j]>=0. Then delta_j=(1-q_j)/2<=1/2. Character multiplication permutes squared Fourier labels and complete reference labels, preserving H and CE; private influences are unchanged. Independence of private cubes gives delta_*=(1-product_j q_j)/2. The original product's separator influence is delta_* or 1-delta_*, hence at least delta_*.

The Boolean private function a_j b_j has variance 1-q_j^2=4delta_j(1-delta_j). Parseval/Poincare and the physical-edge union bound imply 4delta_j(1-delta_j)<=I(a_j b_j)<=I(a_j)+I(b_j)=2J_j. Thus J_j>=delta_j. The loss sum delta_j-delta_* is nonnegative because the number of disagreements minus its parity is nonnegative. It is at most J-delta_*. With a_j=1,b_j a private character, equality holds for every r, proving the optimal coefficient 1.

For completeness independently expand D=(product a_j-product b_j)/2 in physical private derivatives. With C_j=sum_U |U| ahat_j(U)bhat_j(U) and Q_-j=product_{h!=j}q_h,

I(D)=sum_j [I(a_j)+I(b_j)-2Q_-j C_j]/4
=sum_j [(1-Q_-j)J_j/2+Q_-j kappa_j],

where kappa_j=I((a_j-b_j)/2). The pointwise squared derivative inequality gives kappa_j<=J_j; each summand t_j is nonnegative and <=J_j. There is one such account per disjoint private block.

The reference part of A019's claim follows conditionally on the accepted B04-NODE-BOUNDARY@1: Delta_z H<=(3/ln2)delta_*+2sum t_j. For supplied normalized terminal references Q_0,Q_1 let q=(Q_0+Q_1)/2 and R=(P_0+P_1)/2. The parent erased law is R. Multiplying q by the actual parent conditional selector law yields a normalized root reference and KL(parent||root)=KL(R||q)<=avg KL(P_b||Q_b), by log-sum. Therefore CE_root<=avg c_b+Delta_z H. Summing the supplied exclusive allocations avg c_(j,b)+2t_j<=KJ_j gives CE_root<=K I(original) for K>=3/ln2. No existence of these allocations has been supplied. Review verdict: HOLDS at stated scope, with its previously accepted node-boundary dependency retained; the private-owner/derivative proof is independently reconstructed above and checked on 256 arbitrary ordered module pairs. No repair to the source theorem is needed.

### A connected multibit obstruction, including all character orientations

Every private coordinate of F has influence delta. A shared coordinate is pivotal precisely when the other k-1 shared bits are all 1 and the private parity is 1, giving influence 2^{-(k-1)}/2=delta. Thus J=r delta, I_Z(F)=k delta, I(F)=(r+k)delta. Each module also has shared influence k delta. Its unfurled repeated loss is k(r-1)delta.

For coordinate i let c_i be the number of module characters containing i. Character multiplication complements its module influence when present. Therefore

L(C)=sum_i [(r-1)delta+(c_i-(c_i mod 2))(1-2delta)].

Since delta<=1/2 and c_i-(c_i mod2)>=0, the exact minimum over ALL module shared-character choices is k(r-1)delta. Equality is attained with no characters. This is an actual global-character minimization; context-dependent nonlinear gauges are not included and need not preserve H.

Taking r=k^2 gives min L/I(F)=k-1, min L/J=k-1/k, and I(F)=(k^2+k)2^-k tending to zero. Hence no absolute constant pays this repeated loss with either private or whole influence. The small exact witness k=2,r=3 already has min L=1>J=3/4.

The algebraic normal form of the sign exponent is sum_j (product_i Z_i)y_j. Each monomial contains every shared variable and one private variable, so the variable-interaction hypergraph is connected. A sign tensor factorization over a proper partition would express this unique ANF as a sum of polynomials on separate variable blocks, which these crossing monomials prohibit. Adding any global character changes only linear monomials. Thus spectator removal or exact physical tensor factorization does not remove the obstruction.

### What repeated one-coordinate payment actually proves

For general modules sharing k bits, fix coordinate i and context w=Z without i. Fold each conditional one-bit module edge separately. The reviewed theorem gives ell_i(w)=sum_j delta_(j,i)(w)-delta_*,i(w)<=sum_j J_(j,i)(w)-delta_*,i(w). Averaging contexts gives E sum_j J_(j,i)=J for EACH i. Consequently sum_i E ell_i<=kJ-sum_i E delta_*,i. Our family attains equality: only the all-one context contributes, where every delta_j=J_j=1/2 and delta_*=1/2. The width factor k is unavoidable for this diagnostic. Conditional folding need not integrate to one entropy-preserving global character; it is not a general closure theorem. In our family no negative correlations occur, so the diagnostic agrees with the actual minimum character loss.

### Full normalized joint reference and exact spectral refund

Let chi_Y=(-1)^(xor_j y_j). Then F=1-A+A chi_Y. The coefficient at the empty set is 1-delta. Every other set in the family {shared subset} times {empty private subset, all private bits} has coefficient magnitude delta. All other coefficients vanish. There are 2^{k+1}-1 such nonempty sets. Let epsilon=2delta-delta^2; their total mass is epsilon.

An explicit parameter-fixed complete reference assigns Q(empty)=(1-delta)^2 and Q(S)=delta^2 to each of those nonempty sets, zero elsewhere. It is normalized since (1-delta)^2+(2^{k+1}-1)delta^2=1. A complete decoder distinguishes the empty set and enumerates the shared subset and private-parity flag. This Q is given by the family formula, not a generic oracle for an unknown spectrum. Its full CE equals

H_k=-(1-delta)^2 log2((1-delta)^2)+2k epsilon.

Using -(1-epsilon)ln(1-epsilon)<=epsilon and ln2>1/2,

H_k<=(2k+1/ln2)epsilon<=(4k+2/ln2)delta<4(k+1)delta<=4I(F).

Each module has the same entropy H_k, because replacing its private bit by the parity of all private bits embeds the same Fourier probability law. Hence shared multiplication refunds exactly (r-1)H_k. A bound on influence loss alone cannot discard this spectral refund. These are FEI controls and payment diagnostics, not new universal entropy closure.

### Exact shared-block-first tree has no K4 bad-node bill

Query shared bits in any order; a zero answer makes the remaining function constant +1, and the all-one terminal is the private parity character. Every terminal has entropy zero and a complete point-mass reference of cost zero; its remaining private influence is retained, not charged again.

At an all-one prefix with ell shared bits remaining, let d=2^-ell. The exact erasure B for the next shared query is

B=q_0 h2(d^2/q_0)+2d-2d^2,  q_0=(1-d)^2+d^2.

This follows by pairing the two selector Fourier sectors: the empty erased row has weights (1-d)^2,d^2, and the other 2^ell-1 erased rows each have equal weights d^2,d^2. The entropy inequality q h2(a/q)<=a log2(q/a)+a/ln2 and q_0<=1 give

B<=2d+d^2(2ell-2+1/ln2)<3d,

since 2ell d<=1 and 1/ln2<2. Thus every visited shared query is K4 good and the localized bad-node bill is exactly zero. At every depth the visit-weight times conditional influence equals delta, so consumed shared influence totals k delta. The reviewed JS bound M<=2d/ln2 then also bounds the full entropy telescope by (3+2/ln2)k delta with zero terminal CE. The sharper explicit joint reference above supplies CE<=4I directly. This family exposes a failure of repeated module ownership, while supporting a successful adaptive shared-block policy.

### Honest remaining gap

The first unsupported universal line is existence, for arbitrary unequal or overlapping shared phase masks and supplied terminal references, of a dimension-free joint refund/owned-reserve inequality that pays the signed collision excess without spending each J_j once per shared coordinate. Neither the formula family nor the conditional width-k diagnostic proves that line. A018's averaged paired-row inequality is not used, proved or refuted here. The adaptive C019 localized stopping-tree theorem remains open.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before pilot/search: helper A020 joint-phase-block v1; full tables k=1..8,r=1..6 (48 cases, n<=14), pilot k,r=1..3 (9 cases); no symmetry reduction; character-formula domain k=1..4,r=1..3 (5,050 orientations); independent arbitrary one-bit module pair review (256 cases). Integer Walsh, direct character sums for n<=7, physical edge counts, exact Fraction energy, ANF connectedness and outward 40-term rational logarithm intervals were used. For log series 2sum_{j<40}z^{2j+1}/(2j+1), the omitted tail is at most 2z^81/[81(1-z^2)], after reducing integer arguments by powers of 2. Entropy signs are certified in nats against a lower interval for ln2. Every full case checks the full spectral law, all individual influences, normalized reference, CE<=4I and every visited prefix's B<4d.

Commands from this run directory: `python -X utf8 code/check.py --pilot`; `python -X utf8 code/check.py`; after the ancillary-only repair, `python -X utf8 code/check.py --review-only`; `python -X utf8 code/growth.py`.

Pilot completed 9 cases in 0.0913385 seconds. All 48 full-family cases were saved after passing their checks in 9.4847407 seconds; the ensuing ancillary review then failed because Python /2 produced a float for a derivative. No failed assertion was accepted. Replacing both derivative constructors by Fraction(a-b,2) and rerunning only the ancillary phase passed all 256 pair reviews and 5,050 character-formula orientations. The earlier missing-out-directory pilot failure and this helper error are preserved in out/PILOT_RECEIPT.md and out/REVIEW_HELPER_FAILURE.json. FORMULA_SPEC.json froze the additional k=2..32,r=k^2 domain; code/growth.py passed 31 rational closed-form cases, including n=1056 without constructing truth tables. The all-dimensional result rests on the analytic proof above, not on finite extrapolation. Character enumeration independently checks the analytic loss expression, not a second full physical-table implementation of every orientation.

Estimated memory 60 MB with bound 150 MB; no job expected >300 MB, hence memok was not triggered. Pilot/full bounds were 60/120 seconds; formula job 30 seconds. No dimension escalation, GPU, background task, external write or git operation occurred.

## proof dependencies and changed downstream conclusions

The multibit counterexample, character minimum, connectedness and explicit reference bound are self-contained. The auxiliary one-bit independent review and entropy telescope retain B04-NODE-BOUNDARY@1 and the previously reviewed JS interface at their stated scopes; ownership is reconstructed independently. A019's theorem is preserved exactly and receives a new independent scope-bound review record. No original claim is repaired or silently generalized.

A016/A018/A019/A064/A090/A091/A095/A097 should exclude any extension that pays repeated shared-owner loss by one copy of private or total I regardless of separator width. The correct conditional diagnostic pays kJ and is sharp. This rules out one candidate proof architecture, not all shared-block stopping/reference policies. Source adoption, supervisor copying and external review of the new obstruction remain unverified.

## one next mathematical action and independent reviewer

Next: on two shared coordinates with unequal Boolean phase masks, derive the exact joint spectral refund and the signed insertion excess against supplied complete terminal references, and check whether a single private reserve suffices or is reused. Use the present joint-phase family as a mandatory equality/control fixture. A018 should review the spectral refund; A019 and A090/A091 should independently check the character minimum and the one-bit versus block ownership distinction. These are handoffs recorded on disk, not messages sent to other agents.

## actual persistence receipts or precise save blocker

The run contains the four required protocol files, frozen specs, code/ and out/ with exact saved certificates and honest failure receipts. Rolling STATUS.md is two lines; WORKLOG.md and LEARNED.md are appended. out/PERSISTENCE_RECEIPTS.json records final schema, hashes, counts and size checks. Local durable persistence is verified separately from independent acceptance or supervisor/mirror propagation; neither propagation nor public release is claimed.

## Universal bridge

This stage moves C019 by an all-dimensional connected falsifier: even optimal shared-character folding leaves repeated owner loss/I=k-1 on r=k^2 modules, so one private reserve cannot be reused across an unbounded separator block. It simultaneously calibrates C020 with an explicit normalized complete joint reference costing <=4I, an exact spectral refund and zero K4 bad-node bill for a shared-block-first physical tree. What remains is a universal joint refund or exclusive terminal-reserve construction for unequal shared masks, together with a paid adaptive choice of physical separator. NEXT tests that exact insertion/refund interface rather than another class census because it directly addresses the dimension-free resource that the full FEI stopping/reference bridge still lacks.
