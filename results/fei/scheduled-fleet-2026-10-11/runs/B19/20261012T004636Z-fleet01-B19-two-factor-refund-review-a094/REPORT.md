# B19 / A094 independent review of the B05 two-factor refund

**Run:** `20261012T004636Z-fleet01-B19-two-factor-refund-review-a094`  
**Primary packet:** A094 (proof-chain challenger)  
**Reviewed target:** A023, `B05-A023-TWO-FACTOR-SIGNED-REFUND-v1`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** **ACCEPTED AT THE EXACT TWO-FACTOR, DISJOINT, FACTOR-FIRST SCOPE.** Full FEI remains **OPEN**.

## 1. Immutable target and independence

The reviewed bundle is at open-problems commit
`bdd93bb44cd0335a24e42e06dee81a73b5417768`, path
`reports/fei-2026-10-11/runs/B05/20261012T003201Z-fleet01-B05-tensor-refund-a023/`.
The report blob is `47383ab5e161b0e41584eda7eecf04e2c5d4aead`.

B19 previously contributed a phase-sign argument used by the predecessor
one-chain theorem.  That sign theorem is not used here.  The present review
starts from the spectral-entropy definition, reconstructs the scalar packet
from full selector truth tables, and proves the weighted cancellation on a
formal basis.  Thus the accepted claim is the sign-agnostic two-factor theorem;
no inherited all-dimension sign is being reviewed by its contributor.

## 2. Scalar packet reconstructed from entropy

Let `h` be Boolean, `c` constant, and `p=Pr[h!=c]`.  Form the physical
selector `g` with children `h,c`.  For a nonempty Fourier cell of `h`, the two
parent coefficients are `hhat(S)/2`, so

\[
 H(g)-\tfrac12H(h)
\]

receives exactly `hhat(S)^2` from that cell.  Their sum is
`Var(h)=4p(1-p)`.  The empty-cell parent coefficients have magnitudes
`1-p,p`.  Direct substitution gives

\[
\boxed{F(p)=4p(1-p)-2(1-p)^2\log_2(1-p)-2p^2\log_2p
+(1-2p)^2\log_2|1-2p|.}
\]

This independently proves the target's complete `L+Q` formula, including
`F(p)=F(1-p)` and `F(0)=F(1)=0`.  The removable case `p=1/2` is included by
the zero-log convention.  Importantly, this derivation proves the stronger
scalar statement for every genuine Boolean child `h`; it does not assume the
point-defect spectrum.

## 3. Two factor orders and exact ownership

For `q_n` equal to `+1` at one point and `-1` elsewhere, let

\[
x=2^{-a},\quad y=2^{-b},\quad p=x+y-2xy,
\]

\[
D_a=F(x),\quad D_b=F(y),\quad R_{a,b}=F(p),\quad
\Xi_{a,b}=R_{a,b}-D_a-D_b.
\]

If the `a` factor is exhausted first, define `R_(0,b)=D_b` and

\[
\Gamma_{m\mid b}=R_{m,b}-\tfrac12R_{m-1,b}-\tfrac12D_b.
\]

Then, purely formally,

\[
\begin{aligned}
\sum_{m=1}^{a}2^{m-a}\Gamma_{m\mid b}
&=\sum_{m=1}^{a}2^{m-a}R_{m,b}
-\sum_{m=1}^{a}2^{m-a-1}R_{m-1,b}
-D_b\sum_{m=1}^{a}2^{m-a-1}\\
&=R_{a,b}-D_b=D_a+\Xi_{a,b}.
\end{aligned}
\]

All interior `R_(m,b)` coefficients cancel; `R_(0,b)=D_b` combines with the
geometric terminal term.  Exchanging `a,b` proves the reverse order.

The physical leaf check also closes: after exhausting the first factor, the
second child is either `q_b` or `-q_b` against the inherited constant.  Its
disagreement mass is respectively `1-y` or `y`, hence every leaf packet is
`D_b` by symmetry and their total expected terminal charge is exactly one
`D_b`.

Writing the reached signed sum as `P_(a|b)-N_(a|b)` therefore gives

\[
\boxed{R_{a,b}+N_{a\mid b}=D_b+P_{a\mid b}.}
\]

This is a valid no-double-spend statement for the declared tree: each reached
node occurs once with its reach weight and the terminal expectation occurs
once.  The assignment of `Xi_(a,b)` to the first phase is order-dependent
bookkeeping, not a canonical factor decomposition.  No many-factor ownership
principle follows from it.

## 4. Cross-term sign and asymptotic

Independent rational intervals give

\[
\Xi_{4,4}=-0.010386947315\ldots<-0.01038,
\qquad
\Xi_{5,5}=0.002396507006\ldots>0.00239.
\]

Thus exact additivity is refuted in both directions.

For the infinite equal-factor statement, Taylor expansion with remainder at
zero gives

\[
F(p)=4p+p^2\left(2\log_2\frac1p-4+\frac3{\ln2}\right)
-\frac{2}{\ln2}p^3+O(p^4).
\]

Putting `delta=2^-n` and `z=2delta(1-delta)`, the linear part contributes
`-8delta^2`; the quadratic-log part contributes

\[
\delta^2\left(4n-16+\frac6{\ln2}\right)+O(n\delta^3).
\]

Hence

\[
\boxed{\Xi_{n,n}=\delta^2\left(4n-24+\frac6{\ln2}\right)
+O(n\delta^3).}
\]

The target coefficient and eventual positivity are correct.  The checker
corroborates positivity for `5<=n<=40`; this finite range is not used as the
infinite bridge.  Since `D_n=4delta+O(n\delta^2)`, the relative cross term is
`O(n2^-n)` and cannot be an FEI counterfamily.

## 5. Independent computation

`INDEPENDENT_CHECK.py` imports no target code.  It uses:

- complete truth tables and exact Walsh transforms to compute
  `H(selector)-H(child)/2` directly for `2<=a,b<=4`;
- a formal exact basis for the weighted telescope through depth 200;
- both physical factor orders and both positive/negative ledgers for
  `2<=a,b<=10`;
- exact rational logarithm intervals with explicit tails;
- no randomness.

Command:

```text
python3 INDEPENDENT_CHECK.py
```

It reports 939 checks, zero failures, and the two rigorous cross-term signs.

## 6. Primary-source scope check

O'Donnell--Tan prove a disjoint biased-composition theorem for FEI+; they also
explicitly explain why naive componentwise FEI constants do not simply compose.
Wan--Wright--Wu treat decision-tree communication bounds, while
Gonzalez--MacManus--Pereyra treat stopping-tree restriction increments.  These
are the correct neighboring frameworks, but none of the checked statements is
the target's exact `L+Q` two-point-defect cross-term identity.  This review does
not make a first/novelty/priority claim.

Primary sources checked on 2026-10-12 UTC:

- https://arxiv.org/abs/1304.1347
- https://arxiv.org/abs/1312.3003
- https://arxiv.org/abs/2606.00246

## 7. Exact accepted scope and remaining obstruction

Accepted:

1. the scalar packet formula for arbitrary Boolean child versus a constant;
2. both exact two-factor, disjoint, point-defect factor-first telescopes;
3. the positive/negative single-use ledger at that scope;
4. the sign-changing finite cross term and the equal-factor asymptotic.

Not accepted or implied:

- shared-variable products;
- arbitrary branching among unrelated leaves;
- a canonical, order-independent allocation of `Xi`;
- unique ownership of pair and higher Möbius interactions for three or more
  factors;
- a dimension-independent influence bound on total positive credits and
  terminals;
- full FEI.

The next exact obstruction is to define and prove a first-revelation ownership
rule for all higher interactions without history reuse.  The present theorem is
a reusable two-factor interface, not the missing universal payment theorem.

