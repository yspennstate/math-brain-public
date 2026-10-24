# B19 / A094 independent review of multifactor Möbius ownership

**Run:** `20261012T015630Z-account01-B19-multifactor-review-a094`  
**Primary packet:** A094, proof-chain challenger  
**Reviewed target:** A023, `B05-A023-MULTIFACTOR-MOBIUS-OWNERSHIP-v1`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** **ACCEPTED at the finite, disjoint point-defect, deterministic factor-first, complete `L+Q` packet scope.** Full FEI remains **OPEN**.

## 1. Immutable target and review independence

The reviewed eight-file B05 bundle is pinned at open-problems commit
`f67766966c46eb8c8a3150ce000a2909d378fc32`, path
`reports/fei-2026-10-11/runs/B05/20261012T013755Z-account01-B05-multifactor-refund-a023/`.
Its report blob is `bfa81a2f818a0fe5f449aea001b7b00f02371a43` and its report SHA256 is
`a15d22819366b02bcad64e87cdd4e4f60750df23d5e1ce320bbbd2ed0041309a`.

The accepted input is the two-factor theorem at author commit
`bdd93bb44cd0335a24e42e06dee81a73b5417768`, independently reviewed at
`4a3a44691f97a208cd6b805c93cdff5508a24cc6`. This reviewer authored that
two-factor review, but did not contribute the new multifactor theorem. The
present review rederives the new combinatorial ownership, physical-chain
realization, and all-order asymptotic independently rather than treating the
two-factor verdict as evidence for those steps.

## 2. Packet reduction and sign aggregation

Let `q_n` be `+1` at one point and `-1` elsewhere, with defect probability
`x=2^{-n}`. For disjoint factors indexed by `B`, relative to the natural
constant sign, their product disagrees exactly when an odd number of defects
occurs. Hence

\[
p_B=\frac{1-\prod_{i\in B}(1-2x_i)}2.
\]

The already accepted scalar complete selector packet is

\[
F(p)=4p(1-p)-2(1-p)^2\log_2(1-p)-2p^2\log_2p
 +(1-2p)^2\log_2|1-2p|.
\]

Direct substitution gives `F(p)=F(1-p)`. Therefore every sign-flipped copy
of the residual product carries the same complete `L+Q` packet. This is the
precise reason that, after one factor is exhausted, the copies of the next
factor-tree over all current leaves may be aggregated into a single stage:
their reach probabilities sum to one, and their packet and future credits are
identical up to this sign symmetry.

This aggregation would be invalid for an unsigned or phase-erased packet. It
is valid for the submitted complete packet.

## 3. Exact Möbius ownership

For `R(empty)=0`, `R(B)=F(p_B)`, define

\[
\Omega(B)=\sum_{C\subseteq B}(-1)^{|B|-|C|}R(C).
\]

Möbius inversion gives

\[
R(A)=\sum_{\varnothing\ne B\subseteq A}\Omega(B).
\]

Fix an order `pi=(i_1,...,i_r)` and `A_j={i_j,...,i_r}`. Assign `Omega(B)`
to the earliest element of `B`. Subtracting the inversions on `A_j` and
`A_(j+1)` proves

\[
\boxed{
\sum_{\substack{B\subseteq A_j\\i_j\in B}}\Omega(B)
=R(A_j)-R(A_{j+1}).
}
\]

Each nonempty `B` has exactly one earliest element, so no interaction is
reused. This statement is exact for arbitrary set functions `R` with
`R(empty)=0`; it does not depend on positivity, entropy, or the dimensions.
The owner is order-dependent, not canonical.

## 4. Exact physical-chain realization

During the `j`th stage, reveal all coordinates of factor `q_(n_i_j)` before
touching the remaining factors. At residual dimension `m`, the continuing
child is `q_(m-1)` times the residual product, while the other child is a
sign-flipped residual product. Sign aggregation from Section 2 therefore
gives the physical credit

\[
\Gamma_{m\mid A_{j+1}}
=R(\{q_m\}\cup A_{j+1})
-\frac12R(\{q_{m-1}\}\cup A_{j+1})
-\frac12R(A_{j+1}).
\]

The continuing node has reach probability `2^(m-n_i_j)`. Writing
`R_m=R({q_m} union A_(j+1))` and `B=R(A_(j+1))`, with `R_0=B`, gives

\[
\begin{aligned}
\sum_{m=1}^{n}2^{m-n}\Gamma_{m\mid A_{j+1}}
&=\sum_{m=1}^{n}2^{m-n}R_m
-\sum_{m=1}^{n}2^{m-1-n}R_{m-1}
-B\sum_{m=1}^{n}2^{m-1-n}\\
&=R_n-B.
\end{aligned}
\]

Thus the physical stage realizes exactly the Möbius owner total. If `P_j`
and `N_j` are its reach-weighted positive and negative parts, then

\[
P_j-N_j=R(A_j)-R(A_{j+1}).
\]

Summing stages yields

\[
\boxed{R(A)+\sum_jN_j=\sum_jP_j.}
\]

The last factor is exhausted, so there is no unpaid terminal packet. Every
node, reach probability, and interaction appears once.

## 5. Independent asymptotic reconstruction

For `r` equal factors, put `delta=2^{-n}` and

\[
p_j(\delta)=\frac{1-(1-2\delta)^j}{2}
=j\delta-j(j-1)\delta^2+O_r(\delta^3).
\]

The scalar expansion is

\[
F(p)=4p+p^2\left(2\log_2\frac1p-4+\frac3{\ln2}\right)
+O\!\left(p^3\log\frac1p\right).
\]

Apply the `r`th forward difference in `j`. For every fixed `r>=3`, all
degree-at-most-two polynomial terms vanish, including the coefficient of
`log(1/delta)`. The only quadratic term that survives is `j^2 log j`:

\[
\boxed{
\Omega_r(n)=c_r\delta^2+O_r(\delta^3\log(1/\delta)),
\quad
c_r=-2\sum_{j=1}^r(-1)^{r-j}{r\choose j}j^2\log_2j.
}
\]

The submitted proof obtains the sign from an improper repeated-derivative
integral. An independent endpoint-safe reconstruction is as follows. For
`2<alpha<min(3,r)`, the compensated Laplace representation of `x^alpha`
and cancellation of all degree-two compensation terms give

\[
A_r(\alpha):=\sum_{j=0}^r(-1)^{r-j}{r\choose j}j^\alpha
=\frac{(-1)^r}{\Gamma(-\alpha)}
\int_0^\infty(1-e^{-t})^r t^{-\alpha-1}\,dt.
\]

Since `1/Gamma(-alpha)=-2(alpha-2)+o(alpha-2)` and `A_r(2)=0`, differentiation
at `alpha=2` yields

\[
\sum_{j=1}^r(-1)^{r-j}{r\choose j}j^2\ln j
=2(-1)^{r+1}\int_0^\infty\frac{(1-e^{-t})^r}{t^3}\,dt.
\]

The integral is finite and strictly positive for every `r>=3`: near zero its
integrand is `O(t^(r-3))`, and at infinity it is `O(t^-3)`. Consequently

\[
\boxed{
c_r=\frac{4(-1)^r}{\ln2}
\int_0^\infty\frac{(1-e^{-t})^r}{t^3}\,dt,
\qquad \operatorname{sgn}(c_r)=(-1)^r.
}
\]

For `r=3`, `c_3=24-18log_2(3)<0` follows exactly from `3^3>2^4`.
Therefore pair-only accounting and an `O(delta^r)` price for fixed `r` are
both genuinely refuted.

## 6. Independent computation

`INDEPENDENT_MULTIFACTOR_REVIEW.py` imports none of the submitted code. It
checks:

- Möbius reconstruction and earliest-owner identities over formal rational
  basis vectors for every order through six factors;
- the physical weighted telescope symbolically through depth 200;
- direct truth-table/Walsh reconstruction and sign symmetry for genuine
  products through four factors and eight variables;
- alternating coefficient signs for `3<=r<=20`, with the `r=3` sign also
  certified by the integer inequality `3^3>2^4`.

Command:

`python3 INDEPENDENT_MULTIFACTOR_REVIEW.py`

Observed result: **6,152 assertions passed, zero failures, no randomness**.
Formal cancellations use `fractions.Fraction`; truth-table diagnostics use a
100-digit `decimal.Decimal` context. The analytic proof, not floating-point
agreement, supplies the all-`r` bridge. The submitted rigorous interval
checker and its 566-pass output were also inspected; its signed interval
division uses all four quotient corners.

## 7. Controls and exact scope

Accepted:

1. every finite family of disjoint genuine Boolean point defects;
2. every fixed deterministic factor-first order;
3. exact earliest-factor ownership of all Möbius interactions;
4. exact aggregation into the physical complete-`L+Q` tree;
5. the single-use signed identity;
6. the fixed-`r` order-`delta^2` asymptotic and alternating nonzero coefficient.

Not accepted or implied:

- nonnegative nodewise credit;
- a dimension-independent bound on `sum_j P_j` by influence;
- a canonical or order-independent allocation;
- shared-variable products or reused physical selectors;
- unrelated addressing/multiplexer branches;
- arbitrary stopping trees;
- a counterfamily with unbounded `H/I`;
- full FEI.

The point-defect factors are genuine AND/OR-type prime gates. Sparse defects
and finite near tensors are covered. Bent selectors, parity-zero erasure,
shared-variable interference, and whole-set addressing are not used. A fresh
rare activation only scales reached conditional terms; its own control packet
remains separate.

## 8. Remaining universal leaf

The first unsupported inequality is exactly:

> Is there a dimension-independent `C` and, for every finite list of point
> defects, an order or stopping rule such that
> `sum_j P_j <= C sum_i I(q_(n_i))`, with each physical influence used once?

Even a positive answer for this disjoint family would still require a new
argument for addressing, unrelated branches, and shared variables. The
accepted signed identity does not provide this inequality.

## 9. Literature and disposition

The neighboring primary sources already checked in the accepted two-factor
review concern disjoint biased composition, decision trees, and stopping-tree
restriction increments. No external novelty or priority claim is made for the
present source-bound campaign theorem. This review addresses mathematical
validity and scope only.

**Final verdict:** `B05-A023-MULTIFACTOR-MOBIUS-OWNERSHIP-v1` is
`INDEPENDENTLY_ACCEPTED_AT_DECLARED_SCOPE`. It is a reusable restricted
accounting theorem, not the missing FEI influence payment.

Full FEI remains **OPEN**.

## 10. Configuration

- Model: Codex; runtime version and reasoning-effort metadata were not exposed.
- Subagents: none.
- Scheduler, shared registry, and graph mutation: none.
- Native Brain ingestion: not claimed.
