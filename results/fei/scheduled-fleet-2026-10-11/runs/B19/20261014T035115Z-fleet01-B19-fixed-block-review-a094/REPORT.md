# B19 / A094 independent review — fixed shared-block orbit transport

**Run:** `20261014T035115Z-fleet01-B19-fixed-block-review-a094`  
**Reviewed claim:** `B05-FIXED-SHARED-BLOCK-TRANSPORT-v1`  
**Primary packet:** `A094`  
**Verdict:** **ACCEPTED AT DECLARED MATHEMATICAL SCOPE, WITH ONE SHARPNESS WORDING CORRECTION**  
**Reviewer-derived strengthening:** **PROVED PENDING FRESH A085/A090 REVIEW**  
**Full FEI:** **OPEN**

## 1. Review object and independence

I read the complete B05 report, proof, endpoint interface, claims, checker and
output at canonical commit
`ceda40553dcf6876fdcae33cec59d44001f368e4`.  The review reconstructs the
conditional-coefficient argument directly and uses a separately written
checker.  The author checker is not used as evidence for the analytic proof.

The target is the singleton potential

\[
\Phi(f)=\sum_i q(\widehat f(\{i\})^2),\qquad
q(t)=t\log_2(1/t)+2t/\ln2,
\]

for products `h(X,U,V)=f(X,U)g(X,V)` with disjoint private sets `U,V` and a
fixed reused physical block `X`, `|X|=k`.

## 2. Verdict on the author theorem

Theorems 3.1–3.3 are correct as stated.

For `i in U`, the `X`-orbit of the conditional singleton coefficient of `h`
is the Walsh transform of `F_i G_0`.  Since `|G_0|<=1`, Parseval gives

\[
E_X^h(\{i\})\le E_X^f(\{i\}).
\]

The `V` side is symmetric.  For the empty orbit,

\[
E_X^h(\varnothing)
=\mathbb E_X F_0^2G_0^2
\le\min\{E_X^f(\varnothing),E_X^g(\varnothing)\}.
\]

Every shared singleton is a component of that orbit, so the author's
`kq(min)` payment is valid.  Complete revelation follows from Parseval plus
Jensen.  Sequential revelation is also correct: every child orbit energy is
`sum_B(a_B+sigma b_B)^2`, whose average is the parent orbit energy, and the
empty-orbit weight drops from `k` to `k-1`.

No hidden restriction on the Boolean terminal cores, activation bias or
reveal order is needed.  The theorem does require one fixed shared set `X`
and disjoint private variables.  It does not cover changing overlaps.

### Required wording correction

The report calls the factor `k` the “exact price.”  It is a valid price but is
not sharp.  The mathematical theorem remains correct; only the sharpness
description must be changed.

## 3. Reviewer-derived logarithmic strengthening

Let

\[
\psi_0(t)=0,\qquad
\psi_k(t)=q(t)+t\log_2 k\quad(k\ge1),
\]

and define

\[
\widetilde\Lambda_X(f)=
\psi_k(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})). \tag{3.1}
\]

Then the stronger product bound is

\[
\begin{split}
\Phi(fg)\le{}&
\sum_{i\in U}q(E_X^f(\{i\}))+
\sum_{j\in V}q(E_X^g(\{j\}))\\
&+\psi_k\!\left(
\min\{E_X^f(\varnothing),E_X^g(\varnothing)\}
\right). \tag{3.2}
\end{split}
\]

Consequently

\[
\Phi(fg)\le\widetilde\Lambda_X(f)+
\widetilde\Lambda_X(g). \tag{3.3}
\]

The logarithmic potential retains the same reveal-order contraction:

\[
\mathbb E_\sigma
\widetilde\Lambda_{X\setminus\{x\}}(f\mid x=\sigma)
\le\widetilde\Lambda_X(f). \tag{3.4}
\]

This strictly improves the author's `kq(E)` empty-orbit term to
`q(E)+E log2(k)`.  Because this strengthening was produced during the
review, B19 is a contributor and cannot independently accept it.  It is
**PROVED PENDING FRESH A085/A090 REVIEW**.

## 4. Proof of the strengthening

Let `z_x=hhat({x})^2` for `x in X`, `s=sum_x z_x`, and if `s>0` put
`p_x=z_x/s`.  Direct entropy decomposition gives

\[
\sum_{x\in X}q(z_x)
=q(s)+sH(p)
\le q(s)+s\log_2 k. \tag{4.1}
\]

The author proof gives

\[
s\le E_X^h(\varnothing)le
m:=\min\{E_X^f(\varnothing),E_X^g(\varnothing)\}.
\]

Both `q(t)` and `t log2(k)` are increasing, proving the shared part of
(3.2).  The private terms are exactly those in the author proof.

For revelation, let `Z_sigma` be a child empty-orbit energy.  Its mean is the
parent energy `e`.  If `k>=2`, concavity gives

\[
\mathbb E_\sigma\psi_{k-1}(Z_\sigma)
\le\psi_{k-1}(e)\le\psi_k(e).
\]

For `k=1`, the child has no shared empty-orbit charge.  The private terms
contract by the same Jensen calculation as in the author proof.  This proves
(3.4).

## 5. Logarithmic dependence is necessary at this abstraction

The remaining `log k` is not merely an artifact of (4.1).  Let `X` contain
`k=2r+1` variables and let `M_k` be odd majority.  Take `f=M_k`, `g=1`, and
no private variables.  Parseval gives

\[
E_X^f(\varnothing)=E_X^g(\varnothing)=1.
\]

For every `i in X`,

\[
\widehat M_k(\{i\})=
\frac{\binom{2r}{r}}{4^r}.
\]

Stirling's formula yields

\[
\widehat M_k(\{i\})^2\sim\frac{2}{\pi k},
\qquad
\Phi(M_k)=\frac{2}{\pi}\log_2 k+O(1). \tag{5.1}
\]

Since `q(1)=2/ln2` is constant, no estimate of the form

\[
\Phi(fg)\le\text{private orbit terms}+Cq(m)
\]

with absolute `C` can hold for all fixed-block products.  Thus an
address-count-independent proof must use additional information—physical
influence, signed KL/upper-set refund, or a changing-core ownership rule—not
empty-orbit energy alone.  This is not an FEI counterexample: majority has
total influence of order `sqrt(k)`.

## 6. Independent computation

`REVIEW_CHECK.py` independently implements Walsh transforms and both
potentials.  It checks:

- all `65,536` pairs of Boolean factors on `(x,y,u)` and `(x,y,v)`;
- original and logarithmic product inequalities;
- original and logarithmic sequential-revelation inequalities;
- `5,000` seeded tests with `k=1,2,3,4` and one or two private variables;
- the majority formula through `k=1001`.

All checks pass.  The analytic arguments, not floating output, certify the
all-parameter claims.

## 7. Literature and scope comparison

O'Donnell–Tan's composition theorem assumes inner functions on disjoint
variable blocks and a product-biased FEI+ hypothesis for the outer function.
It does not imply a product theorem with a reused physical block `X`, nor
does it provide the orbit potential or the signed upper-set payment here.

Potapov's September 2026 theorem concerns root FEI for plateaued and partially
bent functions.  It does not control `Phi`, fixed-block orbit transport, or
restriction-tree mismatch/KL charges.

No novelty or priority claim is accepted for the logarithmic potential.
The comparison is only a scope check against the currently cited primary
sources; see `LITERATURE.md`.

## 8. Exact campaign consequence

The author v1 theorem is accepted and may be reused at its fixed-block scope.
The reviewer v2 logarithmic strengthening requires fresh review.  Neither
result completes A023 because:

1. the bound still depends on `log |X|`;
2. changing overlaps such as `{x,y}` followed by `{y,z}` can recharge an
   orbit;
3. the exact signed identity `Delta_i U=B_i-Gamma_i+KL_i` has not been paid;
4. no physical first-owner stopping rule is constructed.

The next unpaid step is therefore sharper than before: **the factor `k` is
removed, but the majority family proves that empty-orbit energy alone cannot
remove `log k`.**  Full FEI remains **OPEN**.

