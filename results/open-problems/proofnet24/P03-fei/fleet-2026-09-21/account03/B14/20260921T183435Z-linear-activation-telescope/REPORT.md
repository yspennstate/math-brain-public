# B14 — linear delayed-activation telescope and a tensor-padding no-go for fixed noise-scale potentials

**Run:** `20260921T183435Z-b14-fei-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED new universal auxiliary identities and a no-go theorem. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** **UNVERIFIED; no novelty claim.**

This run followed the live FEI order and read `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` before the derivation. It did not recheck the read-once certificate or repeat the known finite sweeps. It preserves the known failure of every-prescribed-coordinate payment and starts from the newest mass-weighted erasure / restriction-critical handoffs.

The immediate predecessor in this slot showed that the quadratic influence potential
\[
P_2(f)=\frac{2}{\ln2}\left(I(f)-\frac13\sum_i\operatorname{Inf}_i(f)^2\right)
\]
absorbs the Jensen--Shannon restriction term but that its special child-modulation rebate dies under the hard recursive composition. The compatible mass-weighted composition theorem showed that the genuinely new outer erasure tax is transported by **singleton activation mass before squaring**, and suggested finding a linearly transported reserve.

This run asks exactly that question.

---

## 1. Exact statement attempted

Let
\[
\mu_f(S)=\widehat f(S)^2,
\qquad I(f)=\sum_S |S|\mu_f(S).
\]
Can one build an influence-bounded potential whose restriction drop is exactly a **linear delayed-activation mass**, so that higher Fourier shells become singleton activation later in a physical restriction tree and can pay erasure nonlocally?

The answer to this first part is **yes**, with an exact one-parameter family. However, a second theorem shows that **no fixed noise scale, nor any fixed mixture of such scales without a trivial influence atom, can improve the universal local selector constant**: disjoint tensor powers erase the rebate while preserving the raw local entropy-decrement ratios.

Thus the linearly transported reserve exists and telescopes, but a successful FEI proof must use it in a state-adaptive or block-sensitive way after critical-core localization, not as another fixed scalar potential.

---

## 2. PROVED: exact restriction identity for every Fourier-degree potential

Let `Phi:{0,1,2,...}->R` with `Phi(0)=0`, and define
\[
\mathcal P_\Phi(f)
:=\sum_{S\subseteq[n]}\widehat f(S)^2\Phi(|S|).
\tag{2.1}
\]
Write
\[
d_k:=\Phi(k)-\Phi(k-1),\qquad k\ge1.
\tag{2.2}
\]

### Theorem 2.1 — degree-potential drop

For every Boolean `f` and every physical coordinate `i`,
\[
\boxed{
\Delta_i\mathcal P_\Phi
:=\mathcal P_\Phi(f)
-\frac{\mathcal P_\Phi(f_{i=+1})+\mathcal P_\Phi(f_{i=-1})}{2}
=\sum_{T\not\ni i}\widehat f(T\cup\{i\})^2\,d_{|T|+1}.
}
\tag{2.3}
\]

If `0<=d_k<=L` for every `k`, then
\[
0\le \mathcal P_\Phi(f)\le L I(f),
\qquad
0\le\Delta_i\mathcal P_\Phi\le L\operatorname{Inf}_i(f).
\tag{2.4}
\]

### Proof

Put `a_T=hat f(T)` and `b_T=hat f(T union {i})` for `T` not containing `i`. The two physical restrictions have Fourier coefficient `a_T+b_T` and `a_T-b_T` at `T` (up to the harmless sign convention for which child is called plus). Therefore
\[
\frac12\left[(a_T+b_T)^2+(a_T-b_T)^2\right]=a_T^2+b_T^2.
\]
Hence the averaged child potential is
\[
\sum_{T\not\ni i}(a_T^2+b_T^2)\Phi(|T|),
\]
whereas the parent contribution from the same pair is
\[
a_T^2\Phi(|T|)+b_T^2\Phi(|T|+1).
\]
Subtracting pair by pair gives (2.3). If the increments lie in `[0,L]`, then
`0<=Phi(k)<=Lk`, proving (2.4). QED.

This is an exact physical-restriction identity; no FEI assumption or every-coordinate payment is used.

---

## 3. PROVED: the noise-stability activation potential

For `0<=z<1`, set
\[
\Phi_z(k)=1+z+\cdots+z^{k-1}={1-z^k\over1-z},
\qquad \Phi_z(0)=0.
\tag{3.1}
\]
Then `d_k=z^{k-1}`. If
\[
M_f(z):=\sum_S\widehat f(S)^2z^{|S|}=\operatorname{Stab}_z(f),
\]
define
\[
\boxed{
P_z(f):={1-M_f(z)\over1-z}.
}
\tag{3.2}
\]
Since `1-z^k<=(1-z)k`,
\[
\boxed{0\le P_z(f)\le I(f).}
\tag{3.3}
\]
The exact drop is
\[
\boxed{
\Delta_iP_z(f)=A_i^{(z)}(f)
:=\sum_{S\ni i}\widehat f(S)^2z^{|S|-1}.
}
\tag{3.4}
\]

Two endpoints are especially informative:

- `z=0`:
  \[
  P_0(f)=1-\widehat f(\varnothing)^2=\operatorname{Var}(f),
  \qquad
  \Delta_iP_0=\widehat f(\{i\})^2.
  \tag{3.5}
  \]
  So the singleton activation mass appearing in the mass-weighted composition theorem is **exactly the physical-restriction drop of variance**.
- `z->1`:
  \[
  P_z(f)\to I(f),
  \qquad A_i^{(z)}\to\operatorname{Inf}_i(f).
  \tag{3.6}
  \]
  This endpoint is the trivial influence potential.

### Random-restriction interpretation

Independently restrict every physical coordinate other than `i` with probability `z`, and average uniformly over all chosen restriction signs. After a fixed restricted set `R`, the singleton coefficient at `i` is a signed sum of the original coefficients `hat f(U union {i})` with `U subseteq R`; averaging its square over the restriction signs kills the cross terms. Averaging also over `R` gives
\[
\boxed{
\mathbb E\bigl[\widehat {f_R}(\{i\})^2\bigr]
=A_i^{(z)}(f).
}
\tag{3.7}
\]
Thus `A_i^(z)` is literally **future singleton activation after a z-random physical restriction**. It tracks higher shells before they have fallen all the way to level one.

---

## 4. PROVED: exact restriction-tree payment

Consider any finite adaptive physical restriction tree. At an internal node `u`, reached with probability `w_u`, let the current Boolean function be `f_u` and let the queried coordinate be `i(u)`. By telescoping (3.4),
\[
\sum_{u\text{ internal}}w_u A_{i(u)}^{(z)}(f_u)
=P_z(f)-\sum_{\ell\text{ leaf}}w_\ell P_z(f_\ell).
\tag{4.1}
\]
In particular, for a complete tree whose leaves are constants,
\[
\boxed{
\sum_{u}w_u A_{i(u)}^{(z)}(f_u)=P_z(f)\le I(f).
}
\tag{4.2}
\]
At `z=0`,
\[
\boxed{
\sum_u w_u\widehat {f_u}(\{i(u)\})^2
=\operatorname{Var}(f)\le I(f).
}
\tag{4.3}
\]

This is the desired **linear, globally summable activation reserve**. It does not square the singleton activation and does not charge it repeatedly: every unit of this potential can be spent only once along the tree.

### Compiler corollary

If for some constants `K,lambda>=0` and one fixed `z` every nonconstant Boolean state has an existential physical coordinate `i` satisfying
\[
\Delta_iH(f)
\le K\operatorname{Inf}_i(f)+\lambda A_i^{(z)}(f),
\tag{4.4}
\]
then choosing such a coordinate recursively and using the exact entropy/influence restriction telescopes plus (4.2) gives
\[
\boxed{H(f)\le (K+\lambda)I(f).}
\tag{4.5}
\]
Thus (4.4) would be a full-FEI compiler. The remaining issue is whether a fixed-scale activation term actually lowers the worst universal selector cost.

---

## 5. REFUTED: a fixed noise scale improves the universal local selector

Define the raw restriction-selector supremum
\[
\rho_*:=\sup_f\min_{i:\,p_i>0}{\Delta_iH(f)\over p_i},
\qquad p_i=\operatorname{Inf}_i(f).
\tag{5.1}
\]
For fixed `0<=z<1` and `lambda>=0`, define
\[
\rho_{z,\lambda}
:=\sup_f\min_{i:\,p_i>0}
{\Delta_iH(f)-\lambda A_i^{(z)}(f)\over p_i}.
\tag{5.2}
\]

### Theorem 5.1 — tensor-padding no-go

For every fixed `z<1` and finite `lambda>=0`,
\[
\boxed{\rho_{z,\lambda}=\rho_*.}
\tag{5.3}
\]
So a fixed noise-stability activation rebate does **not improve the universal selector constant at all**.

### Proof

The inequality `rho_{z,lambda}<=rho_*` is immediate because the rebate is nonnegative.

For the reverse inequality, fix any nonconstant Boolean seed `g` and form the disjoint tensor/product power
\[
F_m(x^{(1)},\ldots,x^{(m)})
=\prod_{r=1}^m g(x^{(r)}).
\tag{5.4}
\]
Its Fourier law is the product of `m` independent copies of the spectral law of `g`. Therefore
\[
H(F_m)=mH(g),\qquad I(F_m)=mI(g).
\tag{5.5}
\]
For a physical coordinate `i` in any one copy,
\[
p_i(F_m)=p_i(g),
\qquad
\Delta_iH(F_m)=\Delta_iH(g).
\tag{5.6}
\]
Let `M_g(z)=Stab_z(g)`. Since `g` is nonconstant and `z<1`,
\[
0\le M_g(z)<1.
\tag{5.7}
\]
Factorization of the spectral law gives
\[
\boxed{
A_i^{(z)}(F_m)
=A_i^{(z)}(g)M_g(z)^{m-1}.
}
\tag{5.8}
\]
Hence, uniformly over the finitely many relevant coordinates of the seed,
\[
{\Delta_iH(F_m)-\lambda A_i^{(z)}(F_m)\over p_i(F_m)}
\longrightarrow
{\Delta_iH(g)\over p_i(g)}.
\tag{5.9}
\]
Taking the minimum over physical coordinates, then `m->infinity`, shows
\[
\rho_{z,\lambda}\ge
\min_i{\Delta_iH(g)\over p_i(g)}.
\]
Finally take the supremum over `g` to obtain `rho_{z,lambda}>=rho_*`. QED.

This does **not** refute FEI, the raw selector programme, or the tree reserve (4.2). It refutes only the hope that a **fixed scalar noise scale** added as a local potential rebate lowers the worst selector constant.

---

## 6. PROVED: the same no-go for every fixed noise-scale mixture

Let `nu` be a probability measure on `[0,1]` and define
\[
P_\nu(f)=\int P_z(f)\,d\nu(z),
\qquad
A_i^{(\nu)}(f)=\int A_i^{(z)}(f)\,d\nu(z).
\tag{6.1}
\]
Then `0<=P_nu<=I` and the exact tree telescope remains valid with `A_i^(nu)`.

If `nu({1})=0`, dominated convergence applied to (5.8) gives
\[
{A_i^{(\nu)}(F_m)\over p_i(F_m)}\to0.
\tag{6.2}
\]
Therefore the analogue of (5.3) again equals `rho_*`.

If `theta=nu({1})>0`, then
\[
P_\nu=\theta I+(1-\theta)P_{\nu_0},
\qquad
A_i^{(\nu)}=\theta p_i+(1-\theta)A_i^{(\nu_0)}.
\tag{6.3}
\]
The only rebate surviving tensor padding is the `theta p_i` term, which is exactly the drop of the trivial influence component `theta I`. In a telescoping FEI compiler its root cost cancels the same constant gained locally. Thus a fixed mixture cannot obtain a genuine universal improvement from its level-only component.

This precisely narrows the predecessor's proposed “hierarchy tracking activation before squaring”: **a fixed hierarchy of degree/noise scales is not enough.** It must become state-adaptive, block-sensitive, or be applied after a localization that removes tensor padding.

---

## 7. Exact numerical dead-route illustration

Take the balanced 3-bit majority function. Its spectral law has mass `1/4` on each singleton and mass `1/4` on the triple. Hence
\[
H=2,\qquad I={3\over2},\qquad {H\over I}={4\over3}.
\]
At `z=1/2`,
\[
M_g(1/2)={3\over4}{1\over2}+{1\over4}{1\over8}={13\over32},
\]
for each coordinate
\[
p_i={1\over2},\qquad
A_i^{(1/2)}={1\over4}+{1\over4}{1\over4}={5\over16},
\]
so the normalized rebate is `5/8` for one copy. For `m` disjoint product copies it is exactly
\[
{A_i^{(1/2)}(F_m)\over p_i(F_m)}
={5\over8}\left({13\over32}\right)^{m-1}.
\tag{7.1}
\]
Numerically:

- `m=1`: `0.625`;
- `m=2`: `0.25390625`;
- `m=3`: `0.1031494140625`;
- `m=5`: `142805/8388608 = 0.017023682594299316`;
- `m=10`: `53022496865/281474976710656 = 0.00018837374989644218`.

Meanwhile `H(F_m)/I(F_m)=4/3` and every raw local entropy-decrement ratio is unchanged from the seed. This is the decisive numerical shape behind Theorem 5.1.

---

## 8. PROVED: minimal restriction-critical cores are tensor-prime

The tensor-padding obstruction is real for arbitrary states, but the newest B14 programme already localizes a hypothetical FEI counterexample to a physical restriction descendant maximizing `H/I`. One can sharpen that localization.

### Lemma 8.1 — tensor-prime critical core

Among all nonconstant physical restriction descendants of a Boolean `f`, choose one `g` maximizing
\[
R(g)=H(g)/I(g),
\]
and among ties choose one with the fewest relevant variables. Then `g` cannot factor as
\[
g(x_A,x_B)=g_1(x_A)g_2(x_B)
\tag{8.1}
\]
with disjoint nonempty relevant blocks and both factors nonconstant.

### Proof

For a disjoint product,
\[
H(g)=H(g_1)+H(g_2),\qquad I(g)=I(g_1)+I(g_2),
\]
so `R(g)` is the influence-weighted average of `R(g_1)` and `R(g_2)`. Fixing every variable in block `B` to any physical assignment makes `g_2` a sign and leaves `+-g_1`; hence `g_1` is, up to sign, a physical restriction descendant of `g`. The same holds for `g_2`. Maximality gives `R(g_1),R(g_2)<=R(g)`. Since their weighted average equals `R(g)`, both must equal `R(g)`. But either factor then gives a same-ratio descendant with fewer relevant variables, contradicting the tie-breaking choice. QED.

Thus disjoint tensor padding can always be stripped before analyzing the genuinely hard critical core. This does not itself give a positive activation lower bound, but it identifies the right domain on which to seek one.

---

## 9. Attempted refutation and exact dead route

The attempted stronger route was:

> “Use `P_z=(1-Stab_z)/(1-z)` at one fixed `z<1`; because its drop sees future singleton activation linearly and telescopes globally, subtract a multiple of it and obtain a strictly smaller universal restriction-selector constant.”

Theorem 5.1 **REFUTES** this route in its fixed-scale form. Tensor powers preserve every raw local entropy-decrement ratio while multiplying the activation rebate by `Stab_z(g)^(m-1)`, so the universal supremum returns exactly to the raw selector supremum.

A fixed mixture of scales is also refuted except for its atom at `z=1`, and that atom is just the trivial influence potential whose local gain cancels its root cost.

What survives is the nonlocal identity (4.2), the random-restriction interpretation (3.7), and critical-core tensor-primality (Lemma 8.1).

---

## 10. OPEN / CONDITIONAL / PROVED / REFUTED ledger

### PROVED in this run

1. Exact drop formula (2.3) for every Fourier-degree potential.
2. Exact influence-bounded noise-stability potential `P_z` and activation drop (3.2)--(3.4).
3. `P_0=Var(f)` with singleton activation as its exact restriction drop.
4. `A_i^(z)` equals expected future singleton mass after independent `z`-random physical restrictions of the other coordinates.
5. Exact adaptive restriction-tree telescope `sum w_u A_u=P_z(f)<=I(f)`.
6. Full-FEI compiler (4.4)--(4.5), conditional only on obtaining the stated existential local payment.
7. Tensor-padding theorem `rho_{z,lambda}=rho_*` for every fixed `z<1` and finite `lambda`.
8. Fixed-mixture extension: without an atom at `1`, the rebate vanishes under tensor powers; an atom at `1` is exactly a trivial influence component.
9. Minimal-dimensional restriction-critical descendants are tensor-prime.

### CONDITIONAL

- If one can obtain a **state-adaptive or block-sensitive** version of (4.4) whose scale-change cost itself telescopes, then (4.2) supplies a genuine global activation budget and the usual influence telescope supplies the rest.
- The earlier `P2` Jensen--Shannon absorption and newest arbitrary-bias mass-weighted erasure identity remain inherited inputs, not re-audited claims of this run.

### REFUTED / retired

- Every-prescribed-coordinate universal payment remains false and is not used.
- First-order `P2` modulation as a recursive amplifier remains refuted on the Numaro recursion.
- A fixed `z<1` noise-stability activation potential cannot improve the universal local selector constant.
- A fixed noise-scale mixture cannot repair that failure except through the trivial `z=1` influence component.
- A finite/structured calculation is not full FEI closure.

### OPEN

- Full uniform-cube FEI.
- Finiteness of the raw potential-free selector supremum `rho_*` / mass-weighted erasure selector constant.
- A positive activation theorem on **minimal tensor-prime restriction-critical cores**.
- A state-adaptive-scale or genuinely block-sensitive activation potential compatible with the exact arbitrary-bias erasure refund.

---

## 11. Next attack

Use the random-restriction meaning (3.7) rather than another fixed scalar potential. On a minimal tensor-prime restriction-critical core `g`, choose a state-dependent restriction probability `z(g)` (for example by a fixed quantile of the nonconstant noise-stability curve). Then:

1. independently restrict other coordinates at rate `z(g)`;
2. apply the exact arbitrary-bias refunded erasure identity in those descendants, where `A_i^(z)` is the averaged singleton activation available;
3. seek a data-processing/amortization inequality pulling that refunded payment back to the root;
4. charge scale changes between parent and children to an explicit stability-quantile potential rather than pretending `z` is fixed.

The precise next lemma to try is a **critical-core-only delayed-activation selector**: either some coordinate already has the required small refunded erasure, or a random restriction level creates enough expected singleton activation to decrease a state-dependent stability reserve by a universal multiple of the excess. Theorem 5.1 says the scale must adapt (or the reserve must use block geometry); Lemma 8.1 says irrelevant disjoint tensor padding can be removed first.

Full FEI remains OPEN.
