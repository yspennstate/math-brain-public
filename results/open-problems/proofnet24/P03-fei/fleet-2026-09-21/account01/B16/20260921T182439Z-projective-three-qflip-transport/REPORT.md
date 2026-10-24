# B16 FEI signed transport — projective three-q-flip transport and a triple inverse-noise payment

**Date:** 21 September 2026  
**Scope:** `account01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** a new universal projective three-translation transport theorem, a sharp folded-incidence corollary, and a correlated product-noise payment. No novelty or publication-priority claim.

## 0. Entering state

This run does not audit the settled read-once certificate. It continues the signed-transport chain after the projective q-flip/noise-frame handoff.

The relevant exact inputs are:

1. for every translation `u`,
   \[
   \beta_f(u)=\frac{1-|c_f(u)|}{2}
   =\min_{\varepsilon=\pm1}\Pr[f(X+u)\ne \varepsilon f(X)]
   \]
   is a translation pseudometric and therefore
   \[
   \beta_f(u)\le \sum_{i:u_i=1}\beta_f(e_i),\qquad
   J(f)=\sum_i\beta_f(e_i);
   \]
2. for three arbitrary translations, the spectral parity vector and the physical q-flip sensitivity vector have the same one- and two-bit marginals; their entire discrepancy is one cubic Walsh coefficient;
3. the current selector-refinement route has already reduced all higher Harsanyi orders to integrated **third** finite differences along genuine q-flip generators.

The missing point was that the existing three-q-flip theorem was paid by the ordinary arbitrary-direction influences `I_f(u)`, while the signed route is organized around the character-folded projective budget `beta_f` and ultimately `J(f)`. The theorem below upgrades the local three-flip transport to exactly that projective budget.

---

## 1. Spectral and physical three-flip laws

Let
\[
f:\mathbb F_2^n\to\{-1,+1\},
\qquad
c_f(u)=\mathbb E_X f(X)f(X+u).
\]

Let `Xi` be the spectral sample,
\[
\Pr(\Xi=\xi)=\widehat f(\xi)^2.
\]
For translations `u,v,w`, define spectral parity bits
\[
A_u=\langle \Xi,u\rangle\pmod2
\]
and physical q-flip bits
\[
B_u=1_{\{f(X)\ne f(X+u)\}}.
\]

Write
\[
\tau_f(u,v,w)
=\mathbb E_X f(X)f(X+u)f(X+v)f(X+w).
\]

Using sign encodings
\[
\alpha_u=(-1)^{A_u},\qquad
\gamma_u=(-1)^{B_u}=f(X)f(X+u),
\]
one has
\[
\mathbb E\alpha_u=\mathbb E\gamma_u=c_f(u),
\]
and
\[
\mathbb E\alpha_u\alpha_v
=\mathbb E\gamma_u\gamma_v
=c_f(u+v).
\]
Thus the two three-bit laws agree in Walsh degrees `0,1,2`. Their only possible difference is degree three:
\[
\mathbb E\alpha_u\alpha_v\alpha_w
=c_f(u+v+w),
\qquad
\mathbb E\gamma_u\gamma_v\gamma_w
=\tau_f(u,v,w).
\]

Put
\[
d=\frac{\tau_f(u,v,w)-c_f(u+v+w)}8.
\tag{1.1}
\]
Then at every `a in {0,1}^3` the two probability masses differ by `+d` or `-d`, alternating by cube parity. Consequently
\[
\boxed{
W_1^{\rm Ham}
(\operatorname{Law}(A_u,A_v,A_w),
 \operatorname{Law}(B_u,B_v,B_w))
=4|d|
=\frac12|\tau_f(u,v,w)-c_f(u+v+w)|.
}
\tag{1.2}
\]
Indeed the total positive excess is `4|d|`, so Hamming transport costs at least this much; matching the two parity classes along any perfect matching of the 3-cube attains it.

---

## 2. `B16-PROJECTIVE-THREE-QFLIP-TRANSPORT` — PROVED

### Theorem 2.1

For every Boolean `f` and every three translations `u,v,w`,
\[
\boxed{
W_1^{\rm Ham}
(\operatorname{Law}A,\operatorname{Law}B)
\le
2\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}.
}
\tag{2.1}
\]

Hence
\[
\boxed{
W_1^{\rm Ham}
(\operatorname{Law}A,\operatorname{Law}B)
\le
\frac23\bigl(\beta_f(u)+\beta_f(v)+\beta_f(w)\bigr),
}
\tag{2.2}
\]
and equivalently
\[
\boxed{
|\tau_f(u,v,w)-c_f(u+v+w)|
\le
4\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}
\le
\frac43\sum_{t\in\{u,v,w\}}\beta_f(t).
}
\tag{2.3}
\]

Both constants `2` in (2.1) and `2/3` in (2.2) are sharp.

### Proof

We split by the rank of `span{u,v,w}`.

#### Rank three

Because `u,v,w` are linearly independent, there exists a Walsh character `chi_a` whose prescribed signs on these three directions are
\[
\chi_a(u)=\operatorname{sgn}c_f(u),\quad
\chi_a(v)=\operatorname{sgn}c_f(v),\quad
\chi_a(w)=\operatorname{sgn}c_f(w),
\]
with an arbitrary choice when a correlation is zero. Put `g=chi_a f`.

Multiplication by a character complements the spectral and physical q-flip bits in exactly the same coordinates:
\[
A_t(g)=A_t(f)\oplus\langle a,t\rangle,\qquad
B_t(g)=B_t(f)\oplus\langle a,t\rangle.
\]
Thus their Hamming `W_1` distance is unchanged. Also
\[
\Pr(B_t(g)=1)
=\frac{1-\chi_a(t)c_f(t)}2
=\beta_f(t)
\quad (t=u,v,w).
\tag{2.4}
\]

For `g`, the two three-bit laws still differ by the alternating perturbation `+-d` from (1.1), with `|d|` unchanged. Fix one coordinate, say `u`. In the four states with `A_u=1`, exactly two carry the positive part of the signed difference and two the negative part. Whichever law has the positive excess on those two states must place at least total mass `2|d|` in the slice `u=1`. Both laws have slice mass `beta_f(u)` by (2.4). Therefore
\[
2|d|\le \beta_f(u).
\]
The same argument applies to `v` and `w`. Using (1.2),
\[
W_1=4|d|
\le2\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}.
\]

#### Rank two

If the three directions are not the three distinct nonzero vectors of a two-dimensional subspace, the three-bit vectors are determined by at most two distinct nonzero q-flip bits. Their two-bit laws are identical, so `W_1=0`.

Otherwise, after relabeling,
\[
w=u+v.
\]
The spectral parity satisfies
\[
A_u\oplus A_v\oplus A_w=0
\]
identically. On the physical side,
\[
B_u\oplus B_v\oplus B_w=1
\]
exactly on a frustrated parallelogram:
\[
Q_f(X;u,v)
=f(X)f(X+u)f(X+v)f(X+u+v)=-1.
\]
Hence by (1.2)
\[
W_1=P_f(u,v):=\Pr(Q_f=-1).
\]
Choose an optimal projective sign for direction `u`. Its derivative-error indicator has mean `beta_f(u)`, and `Q_f=-1` only when that error bit differs between `X` and `X+v`; therefore
\[
P_f(u,v)\le 2\beta_f(u).
\]
By symmetry of the three nonzero directions of the parallelogram,
\[
P_f(u,v)\le2\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}.
\]

#### Rank at most one

Again the three-bit vectors are determined by at most one nonzero bit, and the one-bit laws agree, so `W_1=0`.

This proves (2.1). Since `min(a,b,c)<= (a+b+c)/3`, (2.2) follows; (2.3) follows from (1.2).

For sharpness, take a Boolean function on a two-dimensional cube with exactly one minority vertex. For the three nonzero directions,
\[
\beta_f(u)=\beta_f(v)=\beta_f(w)=\frac12,
\]
while every parallelogram is frustrated, so `W_1=1`. Thus equality holds in both (2.1) and (2.2). QED.

---

## 3. Folded original-coordinate incidence for arbitrary triple families

Let `lambda_r>=0` weight arbitrary translation triples
\[
(u_r,v_r,w_r).
\]
Define the physical incidence
\[
L_i
=
\sum_r\lambda_r
\bigl(
1_{\{i\in\operatorname{supp}u_r\}}
+
1_{\{i\in\operatorname{supp}v_r\}}
+
1_{\{i\in\operatorname{supp}w_r\}}
\bigr).
\tag{3.1}
\]

The projective path inequality gives
\[
\beta_f(u_r)+\beta_f(v_r)+\beta_f(w_r)
\le
\sum_i
\bigl(
1_{i\in u_r}+1_{i\in v_r}+1_{i\in w_r}
\bigr)\beta_f(e_i).
\]
Therefore Theorem 2.1 yields:

### Corollary 3.1 — `B16-PROJECTIVE-THREE-FRAME`

\[
\boxed{
\sum_r\lambda_r W_{1,r}
\le
\frac23\sum_i L_i\beta_f(e_i).
}
\tag{3.2}
\]
If `L_*:=max_i L_i`, then
\[
\boxed{
\sum_r\lambda_r W_{1,r}
\le
\frac{2L_*}{3}J(f).
}
\tag{3.3}
\]
Equivalently, the corresponding cubic-correlation defects satisfy
\[
\boxed{
\sum_r\lambda_r
|\tau_r-c_{u_r+v_r+w_r}|
\le
\frac{4L_*}{3}J(f).
}
\tag{3.4}
\]

This is the folded/original-coordinate version of the three-q-flip source frame required by the double-resolvent selector current. It does not require the q-flip directions themselves to be physical coordinates.

A dual form is immediate: for every `1`-Lipschitz observable `phi_r` on the three-bit Hamming cube,
\[
\left|
\mathbb E\phi_r(A)-\mathbb E\phi_r(B)
\right|
\le W_{1,r},
\]
so the same frame pays any already-signed aggregate whose local third-curvature observable has controlled Hamming Lipschitz norm.

---

## 4. Correlated product-noise directions and three inverse singularities

The min-form (2.1) is stronger than the sum-form when noise parameters are small.

Let `(U_p,V_q,W_r)` be **any joint law** of three random translations; independence between the three directions is not required. Assume only that each marginal is physical product noise:
every coordinate of `U_p` is independently present with probability `p`, and similarly for `V_q,W_r` with probabilities `q,r`.

The projective path inequality holds realization by realization, hence
\[
\mathbb E\beta_f(U_p)\le pJ(f),
\quad
\mathbb E\beta_f(V_q)\le qJ(f),
\quad
\mathbb E\beta_f(W_r)\le rJ(f).
\tag{4.1}
\]
From (2.1),
\[
\begin{aligned}
\mathbb E W_1(U_p,V_q,W_r)
&\le
2\,\mathbb E\min\{\beta(U_p),\beta(V_q),\beta(W_r)\}\\
&\le
2\min\{p,q,r\}\,J(f).
\end{aligned}
\tag{4.2}
\]
Thus even a **triple inverse-noise singularity** is integrable:
\[
\boxed{
\int_0^{1/2}\!\!\int_0^{1/2}\!\!\int_0^{1/2}
\frac{\mathbb E W_1(U_p,V_q,W_r)}{pqr}
\,dp\,dq\,dr
\le 6J(f).
}
\tag{4.3}
\]

Indeed
\[
\int_{[0,a]^3}\frac{\min(p,q,r)}{pqr}\,dp\,dq\,dr
=6a,
\]
because on `0<p<q<r<a` the integrand is `1/(qr)`; integrating first in `p`, then `q`, then `r`, gives `a`, and there are six orderings. At `a=1/2` this is `3`; multiplying by the factor `2J` in (4.2) gives `6J`.

Using (1.2), the cubic correlation defect obeys the companion estimate
\[
\boxed{
\int_{[0,1/2]^3}
\frac{
\mathbb E|\tau_f(U_p,V_q,W_r)-c_f(U_p+V_q+W_r)|
}{pqr}\,dp\,dq\,dr
\le12J(f).
}
\tag{4.4}
\]

The absence of an independence requirement between `U_p,V_q,W_r` is important for the live paired-selector route: clone-pair thinning is correlated inside a pair. A compiler push-forward only has to identify the three **marginal** physical noise laws (or dominate their projective incidence); it need not manufacture independent q-flip directions.

The same argument works for inhomogeneous product marginals:
if `Pr(i in U)=p_i`, `Pr(i in V)=q_i`, `Pr(i in W)=r_i`, then
\[
\mathbb E W_1(U,V,W)
\le
2\min\left\{
\sum_i p_i\beta_i,\,
\sum_i q_i\beta_i,\,
\sum_i r_i\beta_i
\right\}.
\tag{4.5}
\]

---

## 5. Interface with the fully refunded double-resolvent current

The account03 double-resolvent theorem writes the fine/block selector mismatch as an integral of genuine **third finite differences** with two inverse-number parameters. The account03/B18 q-flip lift showed that arbitrary translations, not only physical basis vectors, have the same exact three-bit discrepancy structure. Theorem 2.1 above adds the piece needed by the signed/folded route:

> the local q-flip three-bit transport is paid by the **projective** translation budget `beta`, and hence by original-coordinate `J(f)`, with a sharp constant and without choosing a Hamming path inside the compiler.

Therefore the remaining compiler obligation can be stated more narrowly.

If the already-signed, terminal-retaining double-resolvent curl can be pushed forward to a weighted family of three physical translation marginals with bounded incidence `L_*`, Corollary 3.1 pays it by `2L_*J/3`. If the push-forward is a correlated product-noise family, (4.3) shows that even three inverse-noise singularities are harmless at the source level.

What is **not** proved is that the live fully refunded compiler curl has either representation. In particular, this report does not take absolute values of individual R32 relations or separate the terminal mixed difference from the signed curl.

---

## 6. Exact falsification check

The companion checker tests only the new projective inequality. It does not rerun the read-once certificate or any settled FEI audit.

Using exact integer correlation numerators it verifies
\[
|\tau-c_{u+v+w}|
\le4\min\{\beta(u),\beta(v),\beta(w)\}
\]
for:

- every Boolean function and every ordered translation triple through `n=3` (`132,128` exact function/triple instances across `n=1,2,3`);
- `200` deterministic Boolean truth tables in `n=4`, all `4,096` ordered translation triples each (`819,200` further exact instances).

The sharp ratio `1` is attained already on the two-dimensional one-minority-vertex example. The proof above, not the finite check, establishes the all-dimensional theorem.

---

## 7. Before / after and next attack

**Before:** the third-curvature compiler had an arbitrary-q-flip three-local theorem paid by ordinary q-flip influences, while the signed FEI route's genuine budget is the character-folded original-coordinate quantity `J(f)`. It was still unclear whether the three-local bridge respected that fold.

**After:** the three-q-flip transport admits the sharp projective bound
\[
W_1\le2\min\beta\le\frac23\sum\beta,
\]
hence a physical-incidence frame with no dimension loss. Under product-noise marginals, the stronger min bound makes even a triple inverse-noise integral finite (`<=6J`), and this remains true for correlated triples.

**Next B16 attack:** compute the three translation marginals induced by the actual pair-thinning/double-resolvent curl after same-syndrome signed aggregation. The target is now explicit: either show their weighted physical incidence is bounded, or show they are (possibly correlated) product-noise marginals. If authentic compiler coefficients violate both, preserve the resulting growing incidence as the obstruction and retain more signed cancellation before taking a local transport norm.

**Full FEI remains OPEN.**
