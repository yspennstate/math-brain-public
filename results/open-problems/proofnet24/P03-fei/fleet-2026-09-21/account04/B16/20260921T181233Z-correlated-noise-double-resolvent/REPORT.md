# B16 FEI signed transport — correlated-noise double-resolvent curvature bank

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed semigroup/current identities and a sharp central small-resolvent constant. No novelty or publication-priority claim.

## 0. What moved

This run continues the newest compatible parity-current state rather than reviving a killed basiswise or unsigned route.

The immediately relevant proved inputs are:

1. account04/B16's signed parity minimum-current theorem. For a signed odd fine support `R`, write
   \[
   q=|R|,\qquad k=\#\{\text{clone pairs hit oddly}\},\qquad r=(q-k)/2.
   \]
   After exact same-syndrome aggregation of the live R32 coefficients to `b_R`, the relationwise current energy is
   \[
   2\left(\frac1{qk}-\frac1{q^2}\right)b_R^2,
   \]
   and the singleton layer `q=1` is annihilated exactly.
2. account03/B16's double-resolvent result. The fine/block selector mismatch is a signed current of genuine third curvatures with both inverse-number factors retained; the one-resolvent shortcut can lose `s^2` and is dead.
3. account01/B16 and account02/B18's arbitrary-q-flip Radon/source theorem. The remaining physical payment must keep the fixed Boolean function's original-coordinate influence budget; a unit-weight arbitrary-q-flip frame is false.
4. account04's central Bernoulli/Walsh compiler and pair-correlation flow. Complementary Bernoulli laws and clone correlation already act on the exact signed parity field before norms are taken.

The missing conceptual step was that the parity-current multiplier was still being carried frequency by frequency. This run identifies the *whole* double-resolvent current energy as a positive gap between two genuine Markov noise operators. The gap differentiates into an exact clone-pair curvature-square bank. No endpoint `L2` estimate, positive-part relation sum or unit q-flip frame is used.

The three deliberately different `FLEET_RULES` moves are **#5 ADD A PARAMETER AND DIFFERENTIATE** (introduce an exact clone-flip correlation parameter `lambda`), **#25 COUNT THE SAME THING TWICE** (compute the current energy once from `(q,k)` inverse numbers and once as a noise-semigroup curvature integral), and **#30 ONE SCALE AT A TIME** (separate the central `x,y<=1/2` small-resolvent bank and determine its sharp constant).

---

## 1. Signed paired parity field

Work at one fixed Borel scale after the exact retained-family subtraction. The fine q-flip coordinates are grouped into clone pairs
\[
P_j=\{j0,j1\},\qquad j=1,\ldots,m.
\]
After aggregating **all live signed R32 coefficients with the same fine active syndrome** before squaring, write the odd parity field as
\[
\boxed{
\Phi(S)=\sum_{R:\ |R|\ \mathrm{odd}} b_R\,\chi_R(S),
\qquad
\chi_R(S)=(-1)^{|R\cap S|}.
}
\tag{1.1}
\]
The coefficients `b_R` are signed. In the live compiler they include the `0 mod 4` debits and `2 mod 4` negative credits after same-syndrome cancellation. The retained terminal subtraction stays inside the coefficient field; equivalently one may use the exact difference of the `C_0` and `D_d` Borel potentials before forming (1.1).

For one frequency `R`, define
\[
q_R=|R|,
\qquad
k_R=\#\{j:|R\cap P_j|=1\},
\qquad
r_R=\#\{j:P_j\subseteq R\}.
\tag{1.2}
\]
Then
\[
q_R=k_R+2r_R,
\]
and on the odd sector `q_R,k_R` are odd and `k_R>=1`.

The already-proved diagonal parity-current frame energy is
\[
\boxed{
\mathcal E_{\rm cur}(\Phi)
=2\sum_R
\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)b_R^2.
}
\tag{1.3}
\]

---

## 2. Two genuine noise operators

Let `N_x`, `0<=x<=1`, be the ordinary fine-bit noise operator on the `2m` syndrome bits: independently toggle every fine bit with probability `(1-x)/2`. Thus
\[
N_x\chi_R=x^{q_R}\chi_R.
\tag{2.1}
\]

Now fix `0<=y,lambda<=1` and put
\[
p=(1-y)/2.
\]
For every clone pair independently choose a toggle pair `(Z_0,Z_1)` with law
\[
\boxed{
\begin{aligned}
\nu_{y,\lambda}(00)&=(1-p)^2+\lambda p(1-p),\\
\nu_{y,\lambda}(11)&=p^2+\lambda p(1-p),\\
\nu_{y,\lambda}(10)&=\nu_{y,\lambda}(01)=(1-\lambda)p(1-p).
\end{aligned}}
\tag{2.2}
\]
Let `C_{y,lambda}` be convolution by the product of these pair laws.

The one-clone marginals do not depend on `lambda`. At `lambda=0` the two clone flips are independent, while at `lambda=1` the two clones flip together. For a pair hit by a Walsh frequency in zero, one or two clones, the eigenvalues are respectively
\[
1,\qquad y,\qquad a_{y,\lambda}:=y^2+\lambda(1-y^2).
\tag{2.3}
\]
Therefore
\[
\boxed{
C_{y,\lambda}\chi_R
=y^{k_R}a_{y,\lambda}^{r_R}\chi_R.
}
\tag{2.4}
\]
In particular
\[
C_{y,0}=N_y,
\qquad
C_{y,1}\chi_R=y^{k_R}\chi_R.
\tag{2.5}
\]
The endpoint `lambda=1` is the exact block-correlated clone noise: even occupancy of a clone pair is invisible, odd occupancy receives one factor `y`.

---

## 3. `P03-B16-CORRELATED-NOISE-DOUBLE-RESOLVENT` — PROVED

Let `B_y:=C_{y,1}`. Then
\[
\boxed{
\mathcal E_{\rm cur}(\Phi)
=2\int_0^1\!\int_0^1
\frac{\langle\Phi,N_x(B_y-N_y)\Phi\rangle}{xy}
\,dx\,dy.
}
\tag{3.1}
\]
Here the inner product is uniform on the fine syndrome cube. The apparent singularities at `x=0` or `y=0` are removable on the odd sector; the singleton mode has zero gap.

### Proof

On a Walsh frequency `R`, the integrand multiplier is
\[
x^{q_R}(y^{k_R}-y^{q_R}).
\]
Thus its double integral is
\[
2\int_0^1x^{q_R-1}dx
\int_0^1(y^{k_R-1}-y^{q_R-1})dy
=2\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right).
\]
Parseval gives (3.1). `square`

This is not a generic norm estimate. It is an exact operator identity for the already-signed coefficient field.

### Positivity at every correlation scale

Differentiating (2.4),
\[
\boxed{
\partial_\lambda C_{y,\lambda}\chi_R
=r_R(1-y^2)y^{k_R}
\bigl(y^2+\lambda(1-y^2)\bigr)^{r_R-1}\chi_R.
}
\tag{3.2}
\]
Every multiplier is nonnegative. Hence
\[
\partial_\lambda C_{y,\lambda}\succeq0
\tag{3.3}
\]
as a quadratic-form operator, and
\[
B_y-N_y=\int_0^1\partial_\lambda C_{y,\lambda}\,d\lambda.
\tag{3.4}
\]
Consequently
\[
\boxed{
\mathcal E_{\rm cur}
=2\int_0^1\!\int_0^1\!\int_0^1
\frac{\langle\Phi,N_x\partial_\lambda C_{y,\lambda}\Phi\rangle}{xy}
\,d\lambda\,dy\,dx,
}
\tag{3.5}
\]
and every integrand in (3.5) is nonnegative.

This is the key structural gain: the double inverse-number current is a **positive correlation-flow expenditure**, not an endpoint difference that has to be bounded by triangle inequality.

---

## 4. Exact clone-pair curvature-square form

For a clone pair `P_j={j0,j1}`, let `tau_a` denote XOR-translation by the fine syndrome bit `a` and define the four-point pair curvature operator
\[
\boxed{
D_j=(I-\tau_{j0})(I-\tau_{j1}).
}
\tag{4.1}
\]
Thus
\[
(D_j\Phi)(S)
=\Phi(S)+\Phi(S\triangle P_j)
-\Phi(S\triangle\{j0\})
-\Phi(S\triangle\{j1\}).
\tag{4.2}
\]
On a Walsh frequency, `D_j` has eigenvalue `4` if `R` contains both clones of pair `j` and eigenvalue `0` otherwise. In particular
\[
D_j^2=4D_j.
\tag{4.3}
\]

Let `C_{y,lambda}^{(j)}` apply the pair-correlated noise (2.2) to every pair except `j` and act as the identity on `j`. Direct differentiation of the product law gives
\[
\boxed{
\partial_\lambda C_{y,\lambda}
=\frac{1-y^2}{4}
\sum_{j=1}^m C_{y,\lambda}^{(j)}D_j.
}
\tag{4.4}
\]
Because all operators commute and (4.3) holds,
\[
\boxed{
\langle\Phi,N_x\partial_\lambda C_{y,\lambda}\Phi\rangle
=\frac{1-y^2}{16}
\sum_j
\langle D_j\Phi,
N_x C_{y,\lambda}^{(j)}D_j\Phi\rangle.
}
\tag{4.5}
\]
Substituting into (3.5),
\[
\boxed{
\mathcal E_{\rm cur}
=\frac18
\int_0^1\!\int_0^1\!\int_0^1
\frac{1-y^2}{xy}
\sum_j
\langle D_j\Phi,
N_x C_{y,\lambda}^{(j)}D_j\Phi\rangle
\,d\lambda\,dy\,dx.
}
\tag{4.6}
\]
Every term in (4.6) is nonnegative.

### Interpretation

Equation (4.6) is an exact **curvature-square compiler** for the signed parity current.

- Both inverse-number factors survive as the `dx/x` and `dy/y` resolvents.
- The singleton syndrome is absent because it has no doubled clone pair, hence every `D_j` kills it.
- Negative R32 credits are combined inside the signed field `Phi` before `D_j` and before squaring.
- The terminal-code subtraction stays inside `Phi`; no terminal payment is added a second time here.
- No q-flip generator is replaced by a Hamming path in physical coordinates.

The remaining physical problem is therefore narrower than an arbitrary q-flip frame: pass the **specific pair-curvature square bank (4.6)** through the existing q-flip Radon/original-cut map while keeping the fixed function's physical influence budget.

---

## 5. Sharp central small-resolvent subbank

To isolate the exact central part without spending any endpoint/terminal bank, restrict both inverse-noise parameters to
\[
0\le x,y\le1/2.
\]
Define
\[
\mathcal E_{\rm cent}
:=2\int_0^{1/2}\!\int_0^{1/2}
\frac{\langle\Phi,N_x(B_y-N_y)\Phi\rangle}{xy}
\,dx\,dy.
\tag{5.1}
\]
It is nonnegative and satisfies `E_cent<=E_cur` by the pointwise positivity above.

For one frequency `(q,k)`, its exact multiplier is
\[
\boxed{
\varepsilon_{q,k}
=2\frac{2^{-q}}q
\left(
\frac{2^{-k}}k-\frac{2^{-q}}q
\right).
}
\tag{5.2}
\]
The inherited Ward refinement multiplier is
\[
W_q=1-1/q.
\tag{5.3}
\]

### Theorem 5.1 — sharp central/Ward ratio

For all odd `q>=1` and odd `1<=k<=q` with `q-k` even,
\[
\boxed{
0\le\varepsilon_{q,k}
\le\frac{11}{192}\left(1-\frac1q\right).
}
\tag{5.4}
\]
The constant `11/192` is sharp and occurs at
\[
(q,k)=(3,1),
\qquad
\varepsilon_{3,1}=\frac{11}{288}.
\tag{5.5}
\]

### Proof

For fixed `q`, the function `2^{-k}/k` is strictly decreasing in positive integer `k`, so the ratio is maximized at `k=1`. At `q=3`, direct substitution gives `11/192` after division by `W_3=2/3`.

For every odd `q>=5`,
\[
\frac{\varepsilon_{q,1}}{W_q}
=
\frac{2^{1-q}}{q-1}
\left(\frac12-\frac{2^{-q}}q\right)
<\frac{2^{-q}}{q-1}
\le\frac1{128}
<\frac{11}{192}.
\]
The `q=1` mode is zero on both sides. `square`

Thus the genuinely central double-resolvent portion uses at most about `5.7292%` of the Ward refinement bank frequency by frequency. The complement of (5.1) is **not spent here**; it remains available for the existing R16/moment and terminal-band mechanisms.

---

## 6. Relation to the full current bound

The same semigroup identity recovers the inherited sharp relationwise estimate
\[
\boxed{
\mathcal E_{\rm cur}
\le\frac23
\sum_R b_R^2\left(1-\frac1{q_R}\right),
}
\tag{6.1}
\]
with equality possible at `(q,k)=(3,1)`. Indeed
\[
\frac{2(1/(qk)-1/q^2)}{1-1/q}
=
\frac{2(q-k)}{qk(q-1)}
\le\frac23.
\]
The novelty of this run is not the scalar `2/3`; it is the operator identity (4.6), which locates exactly **where that energy lives**: in a positive double-resolvent sum of signed clone-pair curvatures.

---

## 7. Why this does not repeat a killed shortcut

1. **Not a unit-weight arbitrary-q-flip frame.** The entire multiplier is generated by the two resolvents and the correlation gap; there is no unit sum over pivots.
2. **Not the dead one-resolvent route.** Both `1/q` and `1/k-1/q` are retained exactly. Removing the pair-correlation gap would reintroduce the known `s^2` overpayment.
3. **Not generic endpoint `L2`.** No endpoint evaluation is bounded. The endpoint difference `B_y-N_y` is integrated through the PSD derivative `partial_lambda C` at every correlation scale.
4. **Not unsigned relation payment.** Signed coefficients are aggregated into `b_R` before the quadratic form. The `2 mod 4` negative credits are not positive-parted relation by relation.
5. **Not double use of the terminal band.** The retained-code subtraction stays inside the same field; Section 5 explicitly leaves the complement of the central subbank unassigned.

---

## 8. Exact falsification check

`check_correlated_noise_double_resolvent.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks:

- 80 exact one-pair transition/eigenvalue and `lambda`-derivative identities;
- 24 signed multi-frequency configuration-space operator identities against (3.2)--(3.5);
- 24 exact curvature-square identities (4.5);
- 820 exact full double-resolvent multipliers through odd degree 79;
- 820 exact central-truncation multipliers and the sharp `11/192` bound.

The checker returns `PASS`. The largest full/Ward ratio is exactly `2/3` at `(3,1)`, and the largest central/Ward ratio is exactly `11/192` at `(3,1)`.

Checker SHA-256:
`352ff99acd661ead8c6d1b15d99e5bad8878f037c2cca0749c8b71fc8b14f8d6`.

Recorded stdout SHA-256:
`ac2e82cb07d731016de9eb1ccead10a93c5ac80f279606b954b2aead78ab107d`.

The finite checks are falsification evidence only; Sections 2--5 are algebraic proofs.

---

## 9. Status and next exact target

### PROVED this run

1. `P03-B16-CORRELATED-NOISE-DOUBLE-RESOLVENT`, equation (3.1).
2. Positivity of the full `lambda` correlation flow, equations (3.2)--(3.5).
3. The exact pair-curvature-square representation (4.6).
4. The central small-resolvent multiplier (5.2) and sharp Ward ratio `11/192`.

### PRESERVED / UNSPENT

- signed R32 cancellation and negative entropy credits;
- exact same-syndrome multiplicity before squaring;
- genuine q-flip clone geometry;
- original physical-coordinate geometry (not replaced by an abstract path);
- R16/moment refunds;
- the separate terminal-band payment.

### OPEN

Full unrestricted FEI remains **OPEN / NOT PROVED**.

The next target is now concrete: take one term
\[
\langle D_j\Phi,
N_x C_{y,\lambda}^{(j)}D_j\Phi\rangle
\]
from (4.6), insert the exact live Borel/MacWilliams representation of `Phi`, and push that **already-squared signed pair curvature** through the dependent-q-flip Radon identity. The first target should be the central region `x,y<=1/2`, because (5.4) shows it costs at most `11/192` of the available Ward bank and touches none of the endpoint/terminal allocation. The sought estimate must be in the original physical cut frequencies before any absolute value. If it fails on authentic R32 data, preserve that counterexample and leave the high/terminal region untouched rather than returning to unit-weight, one-resolvent or endpoint-`L2` bounds.
