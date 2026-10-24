# B18 FEI proof synthesis — curvature-refunded crossing potential

**Date:** 21 September 2026  
**Status:** **PARTIAL / new universal restriction-potential implication. Full Friedgut--Kalai FEI remains OPEN / NOT PROVED.**  
**Route:** APPROACH 11/12: influence-greedy physical restrictions + a nonmodular restricted-potential dual.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context was available or claimed.  
**Novelty:** no publication-priority claim.

Fresh scientific `master` was resolved and refreshed during the run. The new derivation starts from two compatible exact ingredients already on `master`:

1. the B14 posterior-threshold crossing theorem (`account04/B14/20260921T184113Z-posterior-crossing-budget/REPORT.md`, blob `c974b249c6cc513019bd0e58e7711ad808c80844`), especially the exact centered drift identity and block restriction/JS tensorization;
2. the B18 centered tangent-polymatroid synthesis (`account01/B18/20260921T1727Z-centered-tangent-polymatroid/REPORT.md`, blob `46d4487e100229114252a25d5e06f8a58208d039`), which showed that purely modular centering and fixed root-coordinate orderings cannot create the missing credit.

I do not rerun either certificate. The point here is to build a genuinely nonmodular physical-restriction potential and derive a new exact crossing refund from it.

---

## 1. Folded influence and the phase potential

For a Boolean function `f`, write

\[
p_i=\operatorname{Inf}_i(f),\qquad
q_i=\min(p_i,1-p_i),\qquad
\mathcal J(f)=\sum_i q_i.
\]

Multiplication by a character translates the Fourier spectrum, hence preserves spectral entropy and replaces selected `p_i` by `1-p_i`. Therefore both `H(f)` and `J(f)` are character invariant. We may median-center a function so that every remaining coordinate satisfies `p_i=q_i<=1/2`; in that gauge `J=I`.

Use the standard recombination function

\[
\mathfrak j(p)
:=1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right)
=\mathfrak j(1-p),
\tag{1.1}
\]

and define the character-invariant potential

\[
\boxed{\mathcal P(f):=\sum_i \mathfrak j(q_i)}.
\tag{1.2}
\]

Finally set

\[
\boxed{\mathcal F(f):=H(f)-\mathcal P(f).}
\tag{1.3}
\]

The elementary sharp linear cap is

\[
\mathfrak j(p)\le c_*\min(p,1-p),
\qquad c_*={2\over\ln2},
\tag{1.4}
\]

so

\[
0\le \mathcal P(f)\le c_*\mathcal J(f).
\tag{1.5}
\]

Thus a universal bound `F<=K J` would imply the original FEI inequality

\[
H(f)\le (K+c_*)\,I(f).
\tag{1.6}
\]

The new point is that `P` has a strict *survivor curvature refund* under physical restriction, beyond merely paying the usual JS term.

---

## 2. Scalar lemma: reflection strengthens the tangent inequality

### Lemma 2.1 — strict concavity

On `0<p<1/2`, put

\[
y=2\sqrt{p(1-p)}\in(0,1).
\]

Then

\[
\boxed{
\mathfrak j'(p)
={2(1-2p)\over y\ln2}\operatorname{artanh}y>0,
}
\tag{2.1}
\]

and

\[
\boxed{
\mathfrak j''(p)
={4\over\ln2}\,{y-\operatorname{artanh}y\over y^3}<0.
}
\tag{2.2}
\]

Hence `j` is strictly concave on `[0,1/2]`, and by symmetry on the whole interval in the appropriate reflected sense. Also

\[
\mathfrak j'(0+)=2/\ln2=c_*.
\tag{2.3}
\]

### Proof

Write

\[
\mathfrak j(p)
={ (1+y)\ln(1+y)+(1-y)\ln(1-y)\over 2\ln2}.
\]

Differentiating, using `dy/dp=2(1-2p)/y`, gives (2.1). A second differentiation reduces exactly to

\[
{4\over\ln2}\left[-{\operatorname{artanh}y\over y}
+{1-y^2\over y}{d\over dy}\left({\operatorname{artanh}y\over y}\right)\right]
={4\over\ln2}{y-\operatorname{artanh}y\over y^3},
\]

which is negative because `artanh(y)>y` for `0<y<1`. The endpoint derivative follows from `artanh(y)~y`. QED.

### Lemma 2.2 — reflected tangent inequality

For every `0<=p<=1/2` and every `0<=u<=1`,

\[
\boxed{
\mathfrak j(u)
\le
\mathfrak j(p)+\mathfrak j'(p)(u-p)
-\mathfrak j'(p)(2u-1)_+.
}
\tag{2.4}
\]

Consequently, for every random variable `U in [0,1]` with `E U=p`,

\[
\boxed{
\mathfrak j(p)-\mathbb E\mathfrak j(U)
\ge
\mathfrak j'(p)\,\mathbb E(2U-1)_+.
}
\tag{2.5}
\]

### Proof

If `u<=1/2`, (2.4) is the ordinary tangent bound from concavity. If `u>1/2`, use symmetry `j(u)=j(1-u)` and apply the tangent bound at `p` to `1-u`:

\[
\mathfrak j(u)
\le \mathfrak j(p)+\mathfrak j'(p)(1-u-p)
=\mathfrak j(p)+\mathfrak j'(p)(u-p)-\mathfrak j'(p)(2u-1).
\]

Taking expectations and using `EU=p` proves (2.5). QED.

The extra term in (2.4) is exactly the posterior majority-crossing functional from B14. This is the bridge that was missing from a purely modular potential.

---

## 3. Physical restriction: the potential pays JS and refunds surviving crossings

Median-center a parent `g`, so `p_i<=1/2`. For a physical restriction block `A`, let

\[
p_j(z)=\operatorname{Inf}_j(g_{A=z})
=\mathbb E[\eta_j\mid x_A=z],\qquad j\notin A,
\tag{3.1}
\]

where `eta_j` is the pivotality indicator. Then `E_z p_j(z)=p_j`. Define the individual and total crossing gains

\[
c_j(A):=\mathbb E_z(2p_j(z)-1)_+,
\qquad
C_A:=\sum_{j\notin A}c_j(A).
\tag{3.2}
\]

The exact centered-drift identity from B14 is

\[
\boxed{
\mathcal J(g)-\mathbb E_z\mathcal J(g_{A=z})
=I_A+C_A,
\qquad I_A:=\sum_{i\in A}p_i.
}
\tag{3.3}
\]

Recenter each child after restriction. Since `j` is symmetric, recentering does not alter `P`. Therefore

\[
\begin{aligned}
\Delta_A\mathcal P
&:=\mathcal P(g)-\mathbb E_z\mathcal P(g_{A=z})\\
&=\sum_{i\in A}\mathfrak j(p_i)
 +\sum_{j\notin A}\left[\mathfrak j(p_j)-\mathbb E_z\mathfrak j(p_j(z))\right].
\end{aligned}
\tag{3.4}
\]

Applying Lemma 2.2 coordinatewise gives the **curvature refund**

\[
\boxed{
\Delta_A\mathcal P
\ge
\sum_{i\in A}\mathfrak j(p_i)
+\sum_{j\notin A}\mathfrak j'(p_j)c_j(A).
}
\tag{3.5}
\]

The exact block restriction identity and inherited block-JS tensorization are

\[
\Delta_AH=B_A+JS_A,
\qquad
B_A:=H(X_A\mid X_{A^c}),
\tag{3.6}
\]

\[
JS_A\le\sum_{i\in A}\mathfrak j(p_i).
\tag{3.7}
\]

Subtract (3.5) from (3.6)--(3.7). This yields a new universal corrected-entropy inequality:

### Theorem 3.1 — curvature-refunded restriction payment

For every median-centered Boolean function and every physical block `A`,

\[
\boxed{
\Delta_A\mathcal F
\le
B_A-
\sum_{j\notin A}\mathfrak j'(p_j)c_j(A).
}
\tag{3.8}
\]

Thus `P` does more than absorb the whole block JS recombination term: whenever a surviving pivotality posterior crosses `1/2`, strict concavity returns an additional, explicitly weighted credit. This term is genuinely nonmodular in `A` and therefore is not annihilated by the modular-centering no-go theorem from the previous B18 run.

---

## 4. New critical-core theorem for APPROACH 11/12

Assume `F/J>0`; otherwise `H<=P<=c_*J` already. Among all physical restriction descendants of the starting function, after character recentering, choose a nonconstant descendant `g` maximizing

\[
\rho={\mathcal F(g)\over\mathcal J(g)}.
\tag{4.1}
\]

In its centered gauge, `J=I`. Every centered child satisfies `F(child)<=rho J(child)`, hence for every block `A`,

\[
\Delta_A\mathcal F
\ge
\rho\left(\mathcal J(g)-\mathbb E_z\mathcal J(g_{A=z})\right)
=\rho(I_A+C_A).
\tag{4.2}
\]

Combining (4.2) with Theorem 3.1 proves:

### Theorem 4.1 — curvature-amplified crossing budget

For every physical block `A` of an `F/J`-critical centered core,

\[
\boxed{
B_A
\ge
\rho I_A
+\sum_{j\notin A}\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(A).
}
\tag{4.3}
\]

Since

\[
B_A\le H(X_A)\le\sum_{i\in A}h_2(p_i),
\tag{4.4}
\]

we obtain the all-block scalar form

\[
\boxed{
\sum_{j\notin A}
\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(A)
\le
\sum_{i\in A}\bigl[h_2(p_i)-\rho p_i\bigr].
}
\tag{4.5}
\]

This is stronger in structure than the earlier crossing budget: the recombination bank `j(p_i)` has been removed from the revealed-coordinate slack, and the same `j` reappears as a **positive derivative coefficient on actual posterior crossings of surviving coordinates**.

### Corollary 4.2 — uniform curvature coefficient

Taking `A={i}` in (4.3)--(4.4) gives

\[
h_2(p_i)\ge\rho p_i.
\tag{4.6}
\]

For `rho>2`, let `sigma(rho) in (0,1/2)` be the unique solution of

\[
{h_2(\sigma)\over\sigma}=\rho.
\tag{4.7}
\]

Then every `p_i<=sigma(rho)`. Since `j'` is decreasing on `[0,1/2]`, define

\[
\kappa(\rho):=\mathfrak j'(\sigma(\rho))>0.
\tag{4.8}
\]

Equation (4.5) implies the simpler dimension-free form

\[
\boxed{
\bigl(\rho+\kappa(\rho)\bigr)C_A
\le
\sum_{i\in A}\bigl[h_2(p_i)-\rho p_i\bigr]
\quad\text{for every }A.
}
\tag{4.9}
\]

This is the first place in this route where the restriction potential produces a strict coefficient gain on the B14 posterior-crossing functional.

---

## 5. Complement form and a new Han/curvature conservation law

Let `B=A^c`. Since

\[
B_A=H(X_A\mid X_B)=H(X)-H(X_B),
\]

and at the critical core

\[
H=\rho I+\mathcal P,
\]

(4.3) is equivalent to

\[
\boxed{
H(X_B)
+\sum_{j\in B}
\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(B^c)
\le
\mathcal P+\rho I_B,
}
\tag{5.1}
\]

where `I_B=sum_{j in B}p_j`.

Now average (5.1) over a uniformly random `q`-subset `B`. Put

\[
h_q:=\mathbb E_{|B|=q}H(X_B),
\qquad
A_q:=h_q-{q\over n}H.
\tag{5.2}
\]

Because `E I_B=(q/n)I`, the `rho` terms cancel *exactly*. We get:

### Theorem 5.1 — fixed-cardinality curvature budget

For every `1<=q<=n-1`,

\[
\boxed{
\mathbb E_{|B|=q}
\sum_{j\in B}
\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(B^c)
\le
\left(1-{q\over n}\right)\mathcal P-A_q.
}
\tag{5.3}
\]

In particular,

\[
\boxed{
A_q\le\left(1-{q\over n}\right)\mathcal P.
}
\tag{5.4}
\]

This is a genuinely nonmodular refinement of the previous fixed-cardinality conservation law: the modular criticality corrections cancel under fixed-q averaging, but the survivor-curvature term in (5.3) **does not**. Its budget is the residual phase potential after subtracting the Han excess.

For `q=n-1`,

\[
A_{n-1}={\operatorname{DTC}(X)\over n},
\]

so (5.4) recovers

\[
\operatorname{DTC}(X)\le\mathcal P.
\tag{5.5}
\]

More importantly, the full crossing term remains:

\[
\boxed{
\sum_i\sum_{j\ne i}
\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(\{i\})
\le
\mathcal P-\operatorname{DTC}(X).
}
\tag{5.6}
\]

Thus a high-`rho` critical core has a dimension-free total budget for **all one-coordinate-induced posterior majority crossings at once**. Since `P<=c_*I`,

\[
\boxed{
\rho\sum_i\sum_{j\ne i}c_j(\{i\})
\le {2\over\ln2}I.
}
\tag{5.7}
\]

This is a concrete APPROACH-11 dichotomy: if a greedy restriction tree repeatedly creates many `1/2` crossings among surviving pivotality posteriors, the finite bank `P-DTC` is exhausted; if it does not, the function is forced into a transversely stable regime in which the surviving derivative posteriors almost never switch their Bayes-majority prediction under one-bit restrictions.

---

## 6. Terminal face consequences

Take `B={k}` in (5.1). Revealing all other variables leaves a one-bit residual function, hence

\[
c_k([n]\setminus\{k\})=p_k.
\]

Therefore every coordinate of the corrected critical core obeys

\[
\boxed{
h_2(p_k)+p_k\mathfrak j'(p_k)\le\mathcal P.}
\tag{6.1}
\]

This improves the earlier terminal condition for an `H/J`-critical core by removing total correlation from the right-hand budget.

For a surviving pair `B={j,k}`, (5.1) gives an analogous mixed-face constraint. If `c_{jk}` denotes the probability that a random `(j,k)` face is non-affine, then after revealing all other coordinates

\[
c_j(B^c)=p_j-{c_{jk}\over2},
\qquad
c_k(B^c)=p_k-{c_{jk}\over2}.
\]

Hence

\[
\boxed{
\left(\rho+{\mathfrak j'(p_j)+\mathfrak j'(p_k)\over2}\right)c_{jk}
\ge
H(X_j,X_k)
+p_j\mathfrak j'(p_j)+p_k\mathfrak j'(p_k)-\mathcal P.
}
\tag{6.2}
\]

Whenever the right side is positive, the corrected-potential core must carry a definite density of genuinely non-affine two-faces. This is a direct Boolean-geometric consequence rather than a free spectral-law relaxation.

---

## 7. Numerical calibration at the current unrestricted lower-bound scale

This section is calibration only; none of the preceding proofs is numerical.

The current inherited unrestricted lower-bound ratio is

\[
C_0=6.521845710923046575.
\]

Because `c_*=2/ln2=2.8853900817779268...`, matching that scale through the corrected potential would require

\[
\rho_0=C_0-c_*
\approx3.636455629145120.
\]

Solving `h_2(sigma)/sigma=rho_0` gives

\[
\sigma(\rho_0)\approx0.196692512551412,
\]

and then

\[
\kappa(\rho_0)=\mathfrak j'(\sigma(\rho_0))
\approx2.388515187682460.
\]

Thus the effective crossing coefficient in (4.9) becomes

\[
\boxed{
\rho_0+\kappa(\rho_0)
\approx6.024970816827580.
}
\tag{7.1}
\]

This number is notable because the earlier potential-free structured experiments peaked near `6.0037` on width-two tribes. It does **not** prove a universal `6.025` step bound; it says that after the exact phase-potential refund, a proof at the current FEI lower-bound scale would only need to defeat corrected critical cores satisfying an all-block crossing inequality with an effective coefficient about `6.025`.

---

## 8. What is proved, what is killed, and the next exact target

### PROVED in this run

1. The reflected tangent inequality (2.4)--(2.5) for the FEI recombination function `j`, with an explicit derivative and strict concavity formula.
2. The nonmodular survivor-curvature refund (3.5).
3. The corrected-entropy restriction inequality (3.8): after subtracting `P`, the entire block JS term is paid and every surviving threshold crossing returns additional credit.
4. The `F/J`-critical all-block theorem (4.3), and its curvature-amplified scalar form (4.9).
5. The complement formulation (5.1) and fixed-cardinality Han/curvature conservation law (5.3).
6. The dimension-free global singleton-crossing budget (5.6)--(5.7).
7. Terminal one-face and two-face rigidity constraints (6.1)--(6.2).

### KILLED / narrowed

- A potential that merely subtracts `sum_i j(p_i)` *without retaining its survivor Jensen gap* throws away the useful part. The nonmodular curvature term in (3.5) is the part that survives the previous modular-cancellation no-go.
- Merely choosing a better fixed ordering of root spectral coordinates remains insufficient, as proved in the prior B18 run. The new credit lives under **physical restriction**, because `p_j(z)` changes branch by branch.
- The present theorem does not itself bound `rho`; arbitrary abstract marginal profiles can still satisfy the scalar relaxations. Boolean mixed-face / transverse geometry remains essential.

### Next exact target

Use (5.6) as the branch-adaptive resource inequality. There are now only two regimes:

1. **crossing-rich:** repeated influence-greedy restrictions create substantial `c_j({i})`; then the finite bank `P-DTC<=c_*I` is consumed at rate at least `rho` per crossing, and one should telescope this into a bounded-depth entropy payment;
2. **crossing-poor:** the sum of all one-bit-induced majority crossings is `O(I/rho)`. Combine this transverse stability with the fresh near-subcube / derivative-support geometry to force either a low-cost physical restriction or an affine/near-character structure, which has small corrected entropy.

A theorem proving that every non-affine corrected critical core falls into the first alternative with a dimension-free amount of crossing, or else admits a physical block with corrected restriction ratio below `rho`, would close this APPROACH-11/12 reduction. That theorem is **not yet proved**.

**Full FEI remains OPEN / NOT PROVED.**
