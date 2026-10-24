# B16 FEI signed transport — projective q-flip metric and original-coordinate noise-frame payment

**Date:** 21 September 2026  
**Scope:** `account01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact universal source-side lemmas and a new sufficient compiler-frame criterion. No novelty or publication-priority claim.

## 0. Entering state

This run does not audit the settled read-once certificate. It continues the newest compatible signed-transport state.

The immediately relevant proved inputs are:

1. account01/B16's exact central Hardy/Radon payment for a physical cut, including the Hardy-resolved Gram identity and the fact that high odd Fourier degree is automatically damped;
2. account02/B18's extension of the central source square to **every nonzero q-flip pivot** `u`, with
   \[
   \mathcal S_u\le \frac1{40}E_u^2,
   \qquad E_u=I_u(1-I_u),
   \]
   and its conditional compiler criterion reducing the universal problem to a dimension-free weighted pivot frame;
3. account04/B16's signed parity-current diagonalisation, which kills the singleton syndrome exactly and gives a nonnegative double-resolvent current after equal-syndrome signed aggregation, but leaves the passage from current edges to authentic original-coordinate q-flip capacity as the residual obligation.

The obstruction in the previous state was therefore no longer local q-flip geometry. It was **original-coordinate payment of the q-flip frame**. The result below supplies a direct source-side payment whenever the compiler's pivot measure has bounded original-coordinate incidence, and an especially clean version for product-noise mixtures.

---

## 1. The projective translation cost

Let `G=F_2^n` and `f:G->{-1,+1}`. For any translation `u in G`, define
\[
I_f(u)=\Pr_X\{f(X+u)\ne f(X)\}
      =\frac{1-c_f(u)}2,
\qquad
c_f(u)=\mathbb E_X f(X)f(X+u).
\tag{1.1}
\]

The q-flip source square depends on
\[
E_f(u)=I_f(u)(1-I_f(u)).
\tag{1.2}
\]

The correct signed quantity for original-coordinate geometry is not `I_f(u)` itself, because multiplying `f` by a character can replace `I_f(u)` by `1-I_f(u)`. Define instead
\[
\boxed{
\beta_f(u):=\min\{I_f(u),1-I_f(u)\}
=\frac{1-|c_f(u)|}{2}.
}
\tag{1.3}
\]
Equivalently,
\[
\boxed{
\beta_f(u)
=\min_{\varepsilon\in\{\pm1\}}
\Pr_X\{f(X+u)\ne\varepsilon f(X)\}.
}
\tag{1.4}
\]

Thus `beta_f(u)` is the least disagreement after allowing the correct projective sign for that translation.

## Theorem 1.1 — `B16-PROJECTIVE-TRANSLATION-PSEUDOMETRIC`

For every Boolean `f` and all `u,v in G`,
\[
\boxed{
\beta_f(u+v)\le \beta_f(u)+\beta_f(v).
}
\tag{1.5}
\]
In particular, for the physical coordinate basis `e_1,...,e_n`,
\[
\boxed{
\beta_f(u)\le\sum_{i:u_i=1}\beta_f(e_i).
}
\tag{1.6}
\]

### Proof

Choose signs `eps_u,eps_v in {+1,-1}` attaining (1.4) for `u` and `v`. Consider the two bad events
\[
A=\{f(X+u)\ne\varepsilon_u f(X)\},
\]
\[
B=\{f(X+u+v)\ne\varepsilon_v f(X+u)\}.
\]
Translation invariance gives
\[
\Pr(A)=\beta_f(u),\qquad \Pr(B)=\beta_f(v).
\]
If neither bad event occurs then
\[
f(X+u+v)=\varepsilon_v\varepsilon_u f(X).
\]
Hence
\[
\Pr\{f(X+u+v)\ne\varepsilon_u\varepsilon_v f(X)\}
\le \Pr(A\cup B)
\le\beta_f(u)+\beta_f(v).
\]
Minimising over the sign allowed in the definition of `beta_f(u+v)` proves (1.5). Iteration along a coordinate path gives (1.6). QED.

### Relation to the folded influence budget

Put
\[
J(f):=\sum_{i=1}^n\beta_f(e_i).
\tag{1.7}
\]
This is exactly the minimum total influence among character twists of `f`: if `chi_a` is a Walsh character, multiplying by `chi_a` changes the `i`th physical influence from `I_f(e_i)` to either `I_f(e_i)` or `1-I_f(e_i)`, independently according to `a_i`. Therefore
\[
J(f)=\min_a I(\chi_a f).
\tag{1.8}
\]
Theorem 1.1 shows that `J(f)` is also a path budget for **every** q-flip direction.

---

## 2. A universal q-flip capacity payment

Because replacing `I_f(u)` by `1-I_f(u)` does not change (1.2),
\[
E_f(u)=\beta_f(u)(1-\beta_f(u)),
\qquad 0\le\beta_f(u)\le\frac12.
\tag{2.1}
\]

The elementary one-variable maximum
\[
\max_{0\le b\le1/2} b(1-b)^2=\frac4{27}
\quad\text{at }b=\frac13
\tag{2.2}
\]
gives the following.

## Theorem 2.1 — `B16-QFLIP-CAPACITY-BY-PROJECTIVE-LENGTH`

For every q-flip direction `u`,
\[
\boxed{
E_f(u)^2\le\frac4{27}\,\beta_f(u).
}
\tag{2.3}
\]
Consequently, for any nonnegative pivot weights `lambda_u`,
\[
\boxed{
\sum_u\lambda_u E_f(u)^2
\le\frac4{27}\sum_u\lambda_u\beta_f(u).
}
\tag{2.4}
\]
If directions are written in the physical basis and
\[
L_i:=\sum_{u:u_i=1}\lambda_u,
\qquad L_*:=\max_iL_i,
\tag{2.5}
\]
then
\[
\boxed{
\sum_u\lambda_u E_f(u)^2
\le\frac4{27}\sum_iL_i\beta_f(e_i)
\le\frac{4L_*}{27}J(f).
}
\tag{2.6}
\]

### Proof

Equation (2.3) follows from
\[
E_f(u)^2
=\beta_f(u)^2(1-\beta_f(u))^2
=\beta_f(u)\,[\beta_f(u)(1-\beta_f(u))^2]
\le\frac4{27}\beta_f(u).
\]
Sum with nonnegative weights. Then apply (1.6) and interchange the two finite sums:
\[
\sum_u\lambda_u\beta_f(u)
\le\sum_u\lambda_u\sum_{i:u_i=1}\beta_f(e_i)
=\sum_iL_i\beta_f(e_i).
\]
This proves (2.6). QED.

This is a genuine dimension-free version of account02/B18's required frame bound whenever the compiler supplies bounded original-coordinate weighted incidence.

---

## 3. Direct payment of the arbitrary-pivot central square

Account02/B18 proved, for every nonzero q-flip pivot and every quotient basis,
\[
\mathcal S_u\le\frac1{40}E_f(u)^2.
\tag{3.1}
\]
The zero pivot may be assigned `S_0=0`. Combining (3.1) with Theorem 2.1 gives immediately:

## Corollary 3.1 — `B16-QFLIP-SOURCE-FRAME-BY-INCIDENCE`

For every nonnegative weighted q-flip family,
\[
\boxed{
\sum_u\lambda_u\mathcal S_u
\le\frac1{270}\sum_u\lambda_u\beta_f(u)
\le\frac1{270}\sum_iL_i\beta_f(e_i).
}
\tag{3.2}
\]
In particular, if `L_*<=L`,
\[
\boxed{
\sum_u\lambda_u\mathcal S_u\le\frac{L}{270}J(f).
}
\tag{3.3}
\]

Thus the B18 frame condition
\[
\sum_r\lambda_rE_{u_r}^2\le A I(f)
\]
can be replaced, on the signed/folded route, by the more geometric task of proving a bounded **original-coordinate incidence** for the compiler's q-flip pivot measure. No comparison of arbitrary q-flip influence directly to total physical influence is required.

If the already fully refunded and KL-subtracted remainder has the representation
\[
\operatorname{UNPAID}
\le\Lambda\sum_u\lambda_u\mathcal S_u,
\tag{3.4}
\]
then (3.3) yields the explicit descent payment
\[
\boxed{
\operatorname{UNPAID}\le\frac{\Lambda L}{270}J(f).
}
\tag{3.5}
\]
This is still conditional on the compiler representation (3.4) and the incidence bound. It is not a proof of full FEI.

---

## 4. Edge-current form: the interface to the new parity-current theorem

The newest parity-current representation naturally produces edges between q-flip generators. Let `h_a in G` label the generator at current vertex `a`. An edge `(a,b)` has q-flip pivot
\[
u_{ab}=h_a+h_b.
\tag{4.1}
\]
Let `lambda_ab>=0` be any nonnegative edge weights supplied **after** all required signed aggregation, and let
\[
d_a:=\sum_{b\ne a}\lambda_{ab}.
\tag{4.2}
\]
The projective triangle inequality gives
\[
\beta_f(h_a+h_b)\le\beta_f(h_a)+\beta_f(h_b).
\]
Therefore:

## Corollary 4.1 — `B16-EDGE-CURRENT-PROJECTIVE-PAYMENT`

\[
\boxed{
\sum_{a<b}\lambda_{ab}\mathcal S_{h_a+h_b}
\le\frac1{270}\sum_a d_a\beta_f(h_a).
}
\tag{4.3}
\]

This is exactly the shape needed by the parity-current handoff. It converts the missing edge-to-source payment into a **weighted vertex-load problem**. It also keeps the q-flip geometry intact; no Hamming path between two arbitrary pivots is chosen inside the compiler.

If the current vertices themselves are the physical coordinate directions and `max_a d_a<=D`, then
\[
\sum_{a<b}\lambda_{ab}\mathcal S_{e_a+e_b}
\le\frac{D}{270}J(f).
\tag{4.4}
\]
If the `h_a` are nonphysical q-flips, (4.3) remains true but one still has to pay `sum_a d_a beta_f(h_a)` from original coordinates. Theorem 1.1 does this whenever the weighted physical incidence of the `h_a` is bounded.

This identifies a sharper residual obligation than the previous generic arbitrary-pivot frame: **bound the incidence/vertex load of the actual fully refunded parity current in original-coordinate projective length, or exploit signed cancellations before the nonnegative edge square if such a bound is false.**

---

## 5. Product-noise semigroup payment

The projective metric gives a particularly clean noise interpolation. Let `U_p in F_2^n` have independent coordinates
\[
\Pr[(U_p)_i=1]=p,
\qquad 0\le p\le\frac12.
\tag{5.1}
\]
For every realization, Theorem 1.1 gives
\[
\beta_f(U_p)\le\sum_i (U_p)_i\beta_f(e_i).
\]
Taking expectation,
\[
\boxed{
\mathbb E\,\beta_f(U_p)\le pJ(f).
}
\tag{5.2}
\]
Hence:

## Theorem 5.1 — `B16-PRODUCT-NOISE-QFLIP-FRAME`

For every Boolean `f` and `0<=p<=1/2`,
\[
\boxed{
\mathbb E E_f(U_p)^2\le\frac{4p}{27}J(f),
}
\tag{5.3}
\]
and for the arbitrary-pivot central source square,
\[
\boxed{
\mathbb E\mathcal S_{U_p}\le\frac{p}{270}J(f).
}
\tag{5.4}
\]

The small-noise factor is exactly linear in `p`. Therefore the singular inverse-noise mixture is still integrable:
\[
\boxed{
\int_0^{1/2}\frac1p\,\mathbb E\mathcal S_{U_p}\,dp
\le\frac1{540}J(f).
}
\tag{5.5}
\]
Equivalently, for any nonnegative measurable mixture density `w(p)`,
\[
\boxed{
\int_0^{1/2}w(p)\,\mathbb E\mathcal S_{U_p}\,dp
\le\frac{J(f)}{270}\int_0^{1/2}p\,w(p)\,dp.
}
\tag{5.6}
\]

This is a direct dimension-free **noise-semigroup payment** for arbitrary q-flip source squares in the original physical basis. It is especially compatible with the current double-resolvent programme: if the fully refunded compiler pivot measure can be represented or dominated by a positive mixture of product-noise direction laws with bounded first moment `int p w(p) dp`, the B18 frame obstruction closes immediately at the source level.

The theorem does not assert that the present parity-current weights already have this representation. Establishing or refuting that representation is the next compiler calculation.

---

## 6. Why this does not contradict the unit-weight q-flip obstruction

The B18 dummy-extended two-variable example shows that an unweighted arbitrary q-flip basis can have
\[
\sum_j E_{U_j}^2=\Theta(n)J(f).
\]
Theorems 2.1 and 5.1 do not contradict this. A generic dense q-flip basis has original-coordinate incidence `L_*=Theta(n)`, while product-noise weights have expected incidence exactly `p` per coordinate. The missing normalization is therefore visible geometrically:

- arbitrary unit-weight q-flip bases: large incidence, no dimension-free payment from the positive envelope;
- product-noise mixture or bounded-degree current: bounded incidence, dimension-free payment;
- fully signed compiler: may do better still through cancellation before squaring.

This separates the genuine compiler question from the already-solved source question.

---

## 7. Exact falsification check

The companion standard-library checker does **not** rerun any settled read-once certificate. It exhausts all `65,812` Boolean functions through dimension four and checks:

- `16,793,872` exact rational instances of the projective triangle inequality;
- `1,050,696` exact instances of `E_u^2 <= (4/27) beta_u`;
- `263,008` exact product-noise inequalities at `p=1/64,1/16,1/4,1/2`.

It passes. The largest observed finite-grid ratio
\[
\frac{\mathbb E E_{U_p}^2}{pJ(f)}
\]
was
\[
\frac{76819125}{536870912}=0.143086770549\ldots
\]
at `n=4,p=1/64`, below the analytic constant `4/27=0.148148...`. The analytic proofs, not the enumeration, establish the theorems.

Checker SHA-256 of the locally executed bytes:
`5fbfd7dcdd8f2a16405eda85bc47ef289c2449c9a41fdf51f90ad1e2d0448e9b`.

Verification-output SHA-256:
`58ebe1a2b93f79855bdc06902046761eb1242e91370cb26c6c83e3a05d1b9cb0`.

---

## 8. Before / after and next attack

**Before:** the source theorem paid each individual q-flip square, and the parity-current theorem supplied a signed double-resolvent normalization, but the route still required an abstract dimension-free arbitrary-pivot frame. The known dense-basis example showed that no unit-weight frame could hold.

**After:** `beta_f(u)=(1-|c_f(u)|)/2` is an exact projective translation pseudometric. It converts q-flip capacity to original-coordinate path length with the universal scalar factor `4/27`, and converts the central q-flip source square to weighted incidence with factor `1/270`. Product-noise pivots have incidence exactly `p` in expectation, yielding the integrated inverse-noise payment `J/540`.

The next B16 calculation should therefore target the **actual fully refunded parity-current pivot measure** and ask one concrete question:

> Can its post-aggregation nonnegative edge weights be represented/dominated by a product-noise mixture with bounded `int p w(p)dp`, or at least shown to have bounded original-coordinate weighted incidence `L_*`?

If yes, Corollary 3.1 closes the arbitrary-q-flip frame obstruction without another local inequality. If no, the failing family gives a rigorous obstruction and the route must retain more signed cancellation before the square.

**Full FEI remains OPEN.**
