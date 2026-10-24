# B05 / A023 — uniform positive-credit payment for all finite point-defect products

**Run:** `20261012T023149Z-account01-B05-positive-credit-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `B05_RARE_REFUNDS`  
**Status:** scoped theorem author-proved, independent A087/A090/A094 review pending; full FEI remains **OPEN**.

## 1. Objective and prior status

The preceding A023 run proved, pending review, exact ordered Möbius ownership
for every finite disjoint product of genuine Boolean point defects. For any
factor-first order it gave

\[
R(A)+\sum_jN_j=\sum_jP_j,
\]

with every positive or negative physical-tree credit used once. Its first
unsupported line was a dimension-independent influence bound on the positive
side.

This run freezes exactly that line:

> For arbitrary factor count, factor dimensions, and deterministic factor
> order, bound the complete reached positive-credit sum by nonreused physical
> influence, or exhibit a growing counterfamily.

## 2. PROVED: universal bound for the declared family

Let (q_n) be (+1) at one point of the uniform (n)-cube and (-1)
elsewhere. Let

\[
f=\prod_{j=1}^r q_{n_j}
\]

on pairwise disjoint physical blocks. Choose any deterministic order of the
factors and exhaust each current factor before moving to the next. If (P_j)
is the complete reach-weighted positive credit accumulated while exhausting
factor (j), then

\[
\boxed{\sum_{j=1}^rP_j<24\sum_{j=1}^r I(q_{n_j})=24I(f).} \tag{2.1}
\]

Combining (2.1) with the preceding exact single-use identity gives

\[
\boxed{R(A)+\sum_{j=1}^rN_j<24I(f).} \tag{2.2}
\]

The quantifiers are: every finite (r), every list of positive integer
dimensions (n_1,\ldots,n_r), and every deterministic factor order. The
stopping tree is physical and finite. No factor, interaction, ancestor credit,
terminal packet, or physical influence is reused. The order need not be
optimized.

This completes the scoped A023 payment theorem for the unbounded declared
family. It is not a theorem about arbitrary Boolean functions.

## 3. Proof: dyadic secant variation

For a collection of unrevealed factors with disagreement probability
(y\in[0,1/2]), write its complete conditional-label plus phase packet as

\[
F(p)=4p(1-p)-2(1-p)^2\log_2(1-p)-2p^2\log_2p
 +(1-2p)^2\log_2(1-2p).
\]

Consider the current factor (q_a), put (delta=2^{-a}), and define

\[
\varphi_y(x)=F(y+(1-2y)x),\qquad
s_y(x)=\frac{\varphi_y(x)-\varphi_y(0)}x.
\]

At residual dimension (m\ge2), with (x=2^{-m}), the exact local credit is

\[
\Gamma_m(y)=x[s_y(x)-s_y(2x)].
\]

The node is reached with probability (delta/x). Its reached positive credit
is therefore

\[
\delta[s_y(x)-s_y(2x)]_+ . \tag{3.1}
\]

Direct differentiation gives

\[
F'''(p)=-\frac4{(\ln2)p(1-p)(1-2p)}<0,qquad 0<p<1/2. \tag{3.2}
\]

Thus (arphi_y'') is decreasing. Moreover,

\[
s_y'(x)=x^{-2}\int_0^x t\varphi_y''(t)\,dt. \tag{3.3}
\]

The integral in (3.3) changes sign at most once, so (s_y) is first
nondecreasing and then nonincreasing. Hence its positive variation on any
decreasing dyadic sequence is at most its full range.

The exact first derivative is

\[
F'(p)=4-8p+\frac4{\ln2}igl[(1-p)\ln(1-p)-p\ln p
 -(1-2p)\ln(1-2p)\bigr].
\]

Using (|t\ln t|\le1) and (ln2>2/3) gives (|F'|<22), hence
(|s_y|<22). Equation (3.1) therefore contributes less than
(44delta) over all (m\ge2).

At (m=1), both children have packet (F(y)), the parent has
(F(1/2)=2), and the reach probability is (2delta). Nonnegativity of the
complete packet bounds this last contribution by (4delta). Thus

\[
P(a\mid y)<48\delta. \tag{3.4}
\]

Since (I(q_a)=2a\delta\ge2\delta), equation (3.4) yields
(P(a\mid y)<24I(q_a)). Summing over stages proves (2.1).

The endpoint (y=1/2) is harmless because (arphi_y) is constant. At
(y=0), the logarithmic singularity in (F'') is integrable in (3.3).

## 4. Exact scope and obstruction controls

| Control | Result |
|---|---|
| Sparse one-point defects | The theorem family itself; rare logarithms are retained in the complete packet. |
| Near tensors | Every finite disjoint product of point defects is covered, with arbitrary unequal dimensions. |
| Prime Boolean gates | Each factor is an AND/OR-type prime gate up to signs and relabeling. |
| Factor order | Every deterministic order works; no optimization is assumed. |
| Rare activation | A fresh activation scales reached conditional terms by its reach probability; its separate selector/control packet is not silently charged here. |
| Bent selector | Not used; the earlier positive bent telescope remains compatible. |
| Addressing / multiplexers | Not covered. Unrelated leaves do not reduce to one scalar disagreement parameter. |
| Shared-variable interference | Not covered; pairwise disjoint physical blocks are essential. |
| Parity-zero erasure | No packet is erased; the complete (L+Q) quantity is retained. |

The result is not a Boolean counterfamily and does not prove FEI. It proves
that the previously open positive-credit inequality does hold uniformly on
the complete disjoint point-defect product family.

## 5. Verification

Command:

`python3 verify_positive_credit.py`

The final checker completed in 29.6 seconds and recorded **PASS** with 7,852
assertions, 1,333 complete ledgers, and 4,519 factor stages. It used exact
`Fraction` arithmetic for probabilities and a rigorous rational atanh-series
enclosure for logarithms; there was no randomness.

Coverage:

- every dimension tuple in ({1,\ldots,5}^r), every order, for
  (1\le r\le3);
- every tuple in ({1,\ldots,4}^4) in both forward and reverse orders;
- equal and strongly unbalanced lists through eight factors and dimension 19;
- the exact stage bound (P(a\mid y)<48\,2^{-a});
- the complete ledger bound (sum P_j<24I(f));
- 1,999 rational points checking the closed numerator behind (F'''<0).

The largest checked ratio was (2), attained by the one-bit endpoint. The
constant 24 is deliberately elementary, not claimed optimal. The
all-dimensional theorem is the analytic proof, not a finite extrapolation.

An initial overbroad interval grid exceeded the 60-second pilot and was
terminated without result. A second broader grid completed near the cap but
was not used as the archived certificate after the script was reduced. The
reported output belongs to the final archived script.

## 6. Mathematical movement and remaining gap

**Previous value/status:** exact multifactor ownership, but no bound on
(sum_jP_j/I(f)); the tracked quantity could in principle grow with factor
count or dimensions.

**New value/status:** for the full declared unbounded family and every order,

\[
\frac{\sum_jP_j}{I(f)}<24.
\]

This closes the first unsupported inequality of the preceding A023 run and
satisfies A023's requirement for a complete, physical, finite, single-use
payment on a nontrivial unbounded family, pending independent review.

The new first unsupported line is:

> Extend the bounded-variation mechanism to branching trees with unrelated
> Boolean leaves or shared physical variables, while preserving a single-use
> influence/KL budget and surviving whole-set addressing.

The scalar reduction (F(p)) is lost in that setting. A next attempt should
seek an operator-valued or conditional-distribution analogue of the secant
slope whose positive variation is controlled by nonreused physical influence.

## 7. Source pins and review

- Immediate predecessor: `yspennstate/math-open-problems` commit
  `f67766966c46eb8c8a3150ce000a2909d378fc32`, run
  `20261012T013755Z-account01-B05-multifactor-refund-a023`, REPORT blob
  `bfa81a2f818a0fe5f449aea001b7b00f02371a43`.
- Independently accepted two-factor input: author commit
  `bdd93bb44cd0335a24e42e06dee81a73b5417768`; B19 review commit
  `4a3a44691f97a208cd6b805c93cdff5508a24cc6`.
- B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`;
  protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
  stream-index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`;
  current-status blob `85007f41958664832e8642df23ce73e89305188e`.

No external novelty or priority claim is made. The neighboring literature
scope remains the source-pinned B19 review of disjoint composition and
stopping-tree work. The new claim requires independent A087/A090/A094
reconstruction, especially equations (3.2)–(3.4) and the combination with the
pending multifactor ownership theorem.

## 8. Delivery distinctions

- Model: Codex as exposed by this run; separate reasoning-effort metadata was
  not exposed.
- Subagents: none.
- Scheduler or graph mutation: none.
- Mathematical result: author-proved, independent review pending.
- Native Brain ingestion: not claimed.
- Full FEI: **OPEN**.
