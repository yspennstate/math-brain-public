# ProofNet24 P14 — Probability correlation

**Run timestamp:** 2026-09-14 13:36 Asia/Jerusalem  
**Track:** probability / overlapping random null normals / fixed-apex second moment  
**Status:** OPEN, with a new exact size-bias reduction and a new deterministic whitening identity.

## 0. Exact target and source state

The inherited probability state is `probability_open_problem_hourly_latest.md`, and the latest full P14-specific report is `P14_probability_correlation_2026-09-14_1219.md` (Library file `file_00000000e4f48230b3939949a4ecb32b`). I also read the full P24 semigroup report `P24_probability_semigroup_2026-09-14_12-32.md` (Library file `file_0000000082f481f499e47cb6f1d99214`), the full P12 smooth-iid least-singular report `P12_smooth_iid_least_singular_2026-09-14_12-46.md` (Library file `file_00000000936081f6a725f2d3d2568409`), and the current P13 fourth-moment report (Gmail source ID `1a09f693d77cd9d3`, 2026-09-14 13:03 Asia/Jerusalem).

The exact P14 model is unchanged. The ambient row dimension is `m`. After fixing the apex, choose distinct `(m-1)`-subsets `S,T` of the remaining `2m-2` iid rows and define

\[
D=m-|S\cap T|,
\qquad
A=S\cap T,
\qquad
B=S\setminus T,
\qquad
C=T\setminus S.
\]

Then

\[
|A|=m-D,
\qquad
|B|=|C|=D-1.
\]

For the realized shared rows `A`, let

\[
E_A=\operatorname{span}(A)^\perp,
\qquad \dim E_A=D,
\]

and choose an isometry

\[
Q_A:\mathbb R^D\longrightarrow E_A\subset\mathbb R^m.
\]

If `X` is one original iid-coordinate row, then conditional on `A` the private projected rows have law

\[
Y=Q_A^T X\in\mathbb R^D.
\]

The two residual matrices

\[
U=BQ_A,\qquad V=CQ_A
\]

are conditionally independent `(D-1) x D` matrices with iid rows distributed as `Y`. Their unit null directions `v,w` satisfy

\[
u_S=Q_Av,\qquad u_T=Q_Aw,
\qquad
\rho_{ST}^2=(u_S\cdot u_T)^2=(v\cdot w)^2.
\]

The entry law `xi` in the active theorem is centered, variance one, has density bounded by `K`, and is subgaussian with `psi_2` norm at most `kappa`. Conditional on `A`, the projected row `Y` is centered isotropic and uniformly subgaussian, but its coordinates are generally dependent. That dependence must not be discarded.

The ordinary-overlap target is

\[
\boxed{
\mathbb E\big[(1-\rho_{ST}^2)^{-1/2}\mid D\big]
\le 1+\frac{C}{D}+\eta_m(D),\qquad D\ge3,
}
\]

with `D<=2` handled by the existing high-overlap fallback and with an error `eta_m(D)` small enough for the fixed-apex second-moment summation.

The previous P14 run proved the conditional near-parallel estimate

\[
\Pr\{1-(v\cdot w)^2\le\varepsilon\mid A\}
\le
\big[C\sqrt{\varepsilon\log(e/\varepsilon)}\big]^{D-1},
\]

and integrated it to show that the singular edge contributes `O(1/D)`. Hence the sole remaining bounded-density subgaussian obligation is

\[
\boxed{
\mathbb E_A\operatorname{tr}(M_A^2)\le \frac{C}{D},
\qquad
M_A=\mathbb E[vv^T\mid A].
}
\tag{P14-Q}
\]

P24 then sharpened this further: if `nu_A` has even density `f_A` relative to Haar measure on `S^{D-1}`, then

\[
D\operatorname{tr}(M_A^2)-1
=
\frac{2}{D+2}\|\Pi_2(f_A-1)\|_2^2.
\]

Thus only spherical degree two matters; total-variation Haar universality is unnecessary.

This run keeps P14-EDGE intact and attacks only (P14-Q).

---

## 1. New exact theorem: cofactor-volume size bias is perfectly isotropic

The key new observation is that the **unnormalized** null vector has an exact second-moment identity under nothing more than isotropy of the rows. This survives the conditional projection `Q_A^T X` and therefore fits the shared-row model exactly.

Fix the shared block `A`, suppress it from notation, and let

\[
Y_1,\ldots,Y_{D-1}\in\mathbb R^D
\]

be iid projected private rows. They satisfy

\[
\mathbb E(Y_iY_i^T)=I_D.
\]

Let `C` be their generalized cross product, oriented in any measurable way, defined by

\[
a\cdot C
=
\det
\begin{pmatrix}
Y_1\\
\vdots\\
Y_{D-1}\\
a
\end{pmatrix}
\qquad(a\in\mathbb R^D).
\]

Because the projected row law is absolutely continuous, `C != 0` almost surely. Put

\[
R=\|C\|,
\qquad
v=C/R,
\qquad
W=\frac{R^2}{D!}.
\]

The orientation of `v` is irrelevant below; only `vv^T` and squared inner products occur.

### Proposition P14-COF-ISO — PROVED

For every realization of `A` for which `Q_A` is defined,

\[
\boxed{
\mathbb E[CC^T\mid A]=(D-1)!\,I_D.
}
\tag{1.1}
\]

Consequently

\[
\boxed{
\mathbb E[R^2\mid A]=D!,
\qquad
\mathbb E[W\,vv^T\mid A]=\frac{I_D}{D}.
}
\tag{1.2}
\]

If `(W',w)` is an independent copy from the second private block, then

\[
\boxed{
\mathbb E\big[WW'(v\cdot w)^2\mid A\big]=\frac1D.
}
\tag{1.3}
\]

#### Proof

For arbitrary deterministic `a,b in R^D`, expand the two determinants:

\[
(a\cdot C)(b\cdot C)
=
\det(Y_1,\ldots,Y_{D-1},a)
\det(Y_1,\ldots,Y_{D-1},b).
\]

Expanding over permutations `sigma,tau in S_D` and using independence of the rows gives

\[
\mathbb E[(a\cdot C)(b\cdot C)]
=
\sum_{\sigma,\tau}
\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
 a_{\sigma(D)}b_{\tau(D)}
\prod_{i=1}^{D-1}
\mathbb E[Y_{i,\sigma(i)}Y_{i,\tau(i)}].
\]

Isotropy makes each row covariance the identity, so the product is nonzero only when

\[
\sigma(i)=\tau(i),\qquad i=1,\ldots,D-1.
\]

Since `sigma,tau` are permutations, this forces `sigma=tau`. Hence

\[
\mathbb E[(a\cdot C)(b\cdot C)]
=
\sum_{\sigma\in S_D}a_{\sigma(D)}b_{\sigma(D)}
=(D-1)!\,a\cdot b.
\]

This is exactly (1.1). Taking traces yields

\[
\mathbb E R^2=D(D-1)!=D!.
\]

Since `CC^T=R^2vv^T`, division by `D!` gives (1.2). For two independent copies,

\[
\mathbb E[WW'(v\cdot w)^2]
=
\operatorname{tr}
\left(
\mathbb E[Wvv^T]\,
\mathbb E[W'ww^T]
\right)
=
\operatorname{tr}\left((I_D/D)^2\right)
=1/D.
\]

No coordinate independence of the projected row is used. QED.

### Interpretation

The quadratic obstruction is therefore **entirely a normalization-bias problem**. Before dividing the generalized cross product by its random volume `R`, the degree-two tensor is exactly isotropic. The only possible source of excess purity is correlation between the line direction and its cofactor volume.

This is closely matched to P24-H2: P24 says only degree two matters; P14-COF-ISO says the degree-two error is created solely by removing the natural `R^2` size bias.

---

## 2. New size-biased reference measure and chi-square reduction

Let `nu_A` be the conditional law of the unoriented line `v`. Define

\[
r_A(v)=\mathbb E[W\mid v,A]
\]

as a regular conditional expectation. Because `W>0` almost surely, `r_A(v)>0` for `nu_A`-almost every line. Define the size-biased line measure

\[
\boxed{
\mu_A(dv)=r_A(v)\,\nu_A(dv).
}
\tag{2.1}
\]

By (1.2), `mu_A` is a probability measure and

\[
\boxed{
\int vv^T\,d\mu_A(v)=I_D/D.
}
\tag{2.2}
\]

Thus `mu_A` need not be Haar, but it is an **exact spherical 2-design at the level needed by the quadratic observable**.

### Proposition P14-SIZEBIAS — PROVED

Let

\[
M_A=\int vv^T\,d\nu_A(v).
\]

Then

\[
\boxed{
D\operatorname{tr}(M_A^2)-1
\le
\chi^2(\nu_A\|\mu_A).
}
\tag{2.3}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}(M_A^2)
\le
\frac1D\int \frac{1}{r_A(v)}\,d\nu_A(v).
}
\tag{2.4}
\]

Therefore the P14 quadratic theorem follows from the dimension-free averaged condition

\[
\boxed{
\mathbb E_A\chi^2(\nu_A\|\mu_A)=O(1).
}
\tag{2.5}
\]

This is a different sufficient criterion from P24's chi-square-to-Haar condition. P24 needs `chi^2(nu_A || Haar)=O(D)`; the new criterion asks only for constant chi-square distance from the endogenous cofactor-volume-size-biased law `mu_A`, which already has the correct degree-two tensor exactly.

#### Proof

Since `d mu_A = r_A d nu_A`,

\[
a(v):=\frac{d\nu_A}{d\mu_A}(v)=\frac1{r_A(v)}.
\]

On `L^2(mu_A)` define the symmetric positive integral operator

\[
(Tf)(v)=\int (v\cdot w)^2 f(w)\,d\mu_A(w).
\]

By (2.2), for every unit `v`,

\[
\int (v\cdot w)^2\,d\mu_A(w)
=v^T(I_D/D)v=1/D.
\]

Thus every row and column integral of the nonnegative kernel equals `1/D`. Schur's test gives

\[
\|T\|_{L^2(\mu_A)\to L^2(\mu_A)}\le1/D.
\]

Now

\[
\operatorname{tr}(M_A^2)
=
\iint(v\cdot w)^2\,d\nu_A(v)d\nu_A(w)
=
\langle a,Ta\rangle_{L^2(\mu_A)}
\]

and hence

\[
\operatorname{tr}(M_A^2)
\le
\frac1D\int a(v)^2\,d\mu_A(v)
=
\frac1D\int \frac1{r_A(v)}\,d\nu_A(v).
\]

Finally,

\[
1+\chi^2(\nu_A\|\mu_A)
=
\int a^2\,d\mu_A
=
\int \frac1{r_A}\,d\nu_A,
\]

which gives (2.3). QED.

### A weaker lower-tail criterion

For every fixed `c in (0,1)`, splitting according to `{r_A>=c}` gives

\[
\boxed{
\lambda_{\max}(M_A)
\le
\frac{1}{cD}
+
u_A\{r_A<c\}.
}
\tag{2.6}
\]

Indeed, for any unit `z`,

\[
\int_{r_A\ge c}(z\cdot v)^2d\nu_A
\le
\frac1c\int r_A(v)(z\cdot v)^2d\nu_A
=\frac1{cD},
\]

while the bad part is at most its mass. Since `M_A` is positive semidefinite with trace one,

\[
\operatorname{tr}(M_A^2)\le\lambda_{\max}(M_A).
\]

Therefore another sufficient target is

\[
\boxed{
\mathbb E_Au_A\{r_A<c\}=O(1/D)
}
\tag{2.7}
\]

for one fixed `c>0`.

This turns the angular-decorrelation problem into a concrete question about **directions along which the conditional cofactor-volume second moment is anomalously small**.

---

## 3. Exact Blaschke–Petkantschin form of the new obstruction

Assume the projected private row has density `g_A` on `R^D`. For a line direction `theta in S^{D-1}`, define

\[
J_{p,A}(\theta)
=
\int_{(\theta^\perp)^{D-1}}
\left|\det_{\theta^\perp}(y_1,\ldots,y_{D-1})\right|^p
\prod_{i=1}^{D-1}g_A(y_i)\,dy_i.
\tag{3.1}
\]

The linear Blaschke–Petkantschin formula gives the null-line density

\[
f_A(\theta)=\frac{J_{1,A}(\theta)}{Z_{1,A}},
\qquad
Z_{1,A}=\int J_{1,A}\,d\sigma_D.
\tag{3.2}
\]

The same change of variables shows that the conditional normalized cofactor-volume mean is

\[
\boxed{
 r_A(\theta)
 =
 \frac{J_{3,A}(\theta)}{D!\,J_{1,A}(\theta)}.
}
\tag{3.3}
\]

Indeed the BP Jacobian already contributes one factor of the hyperplane determinant, and multiplication by `W=|det|^2/D!` changes `J_1` to `J_3/D!`.

Consequently the new chi-square criterion is exactly

\[
\boxed{
1+\chi^2(\nu_A\|\mu_A)
=
\frac{D!}{Z_{1,A}}
\int_{S^{D-1}}
\frac{J_{1,A}(\theta)^2}{J_{3,A}(\theta)}\,d\sigma_D(\theta).
}
\tag{3.4}
\]

This is a sharper determinant-density target than the previous full `L^2` bound on `J_1/Z_1`: the numerator and denominator are paired at the **same direction**, and `J_3` is precisely the compensating volume-size bias that restores exact second-order isotropy.

For Gaussian projected rows, rotational invariance makes `r_A(theta)` independent of `theta`; since its `nu_A`-mean is one, `r_A==1`, `mu_A=nu_A=Haar`, and (2.3) is sharp with

\[
\operatorname{tr}(M_A^2)=1/D.
\]

### Important failed shortcut: raw inverse determinant moments

Jensen gives

\[
\frac1{\mathbb E[W\mid v]}
\le
\mathbb E[W^{-1}\mid v],
\]

so one could try to replace (2.4) by a bound on `E W^{-1}`. That route is unusable even in the Gaussian benchmark. For a Gaussian `(D-1)xD` matrix,

\[
R^2=\det(YY^T)
\]

has a Bartlett product containing a `chi^2_2` factor, and

\[
\mathbb E[(\chi^2_2)^{-1}]=\infty.
\]

Thus

\[
\mathbb E[W^{-1}]=\infty
\]

although `r_A==1` and the desired purity is exactly `1/D`. The conditional expectation `r_A(v)` is essential: it averages away irrelevant radial determinant singularities before taking an inverse.

---

## 4. A second exact reduction: complementary whitening produces an orthogonal pair

There is another structural identity that keeps the overlap dependence exactly rather than replacing it by independence.

Fix `A` and stack **all** `2D-2` private projected rows from `B union C` into

\[
Y\in\mathbb R^{(2D-2)\times D}.
\]

Almost surely `Y` has full column rank. Put

\[
G=Y^TY,
\qquad
Z=YG^{-1/2},
\qquad
Z^TZ=I_D.
\]

Let `v,w` be the unit null directions of `Y_B,Y_C`. Define

\[
x=\frac{G^{1/2}v}{\sqrt{v^TGv}},
\qquad
y=\frac{G^{1/2}w}{\sqrt{w^TGw}}.
\]

### Proposition P14-WHITE — PROVED

One has

\[
\boxed{x\perp y}
\tag{4.1}
\]

and

\[
\boxed{
\rho_{ST}
=
\frac{x^TG^{-1}y}
{\sqrt{(x^TG^{-1}x)(y^TG^{-1}y)}}.
}
\tag{4.2}
\]

#### Proof

Since `Y_Bv=0`,

\[
Z_B(G^{1/2}v)=Y_BG^{-1/2}G^{1/2}v=0,
\]

and similarly `Z_C(G^{1/2}w)=0`. Thus `Zx` is supported only on the `C` rows, while `Zy` is supported only on the disjoint `B` rows. Because `Z^TZ=I`,

\[
x\cdot y=(Zx)\cdot(Zy)=0.
\]

Solving for `v,w` in terms of `x,y` gives (4.2). QED.

### Exchangeability interpretation

Conditional on `A`, the `2D-2` private rows are iid. Hence the original fixed labels `(B,C)` have the same law as first sampling the entire private pool and then choosing a uniformly random balanced partition into two blocks of size `D-1`. The whitened problem can therefore be stated as follows:

> Start from the random Parseval frame `Z=Y(Y^TY)^(-1/2)`. Choose a uniform balanced half-partition of its rows. The two endpoint null directions of the complementary compressed Gram matrices are orthogonal. Prove that their relative orientation with the inverse full Gram `G^{-1}` is sufficiently mixed that (4.2) has second moment `O(1/D)`.

This is a precise exchangeable-pair / random-partition formulation of the remaining theorem.

### Equivalent endpoint-eigenvector formulation

Let

\[
H_B=Z_B^TZ_B.
\]

Since `Z_B^TZ_B+Z_C^TZ_C=I`, the vector `x` is a `0`-eigenvector of `H_B` and `y` is a `1`-eigenvector of `H_B`. Equivalently, if `R_B` is the balanced diagonal sign matrix that is `+1` on `B` and `-1` on `C`, then

\[
2H_B-I=Z^TR_BZ,
\]

and `x,y` are its `-1,+1` endpoint eigenvectors. Thus the remaining problem is a **balanced random-sign compression endpoint-eigenvector mixing theorem** for the polar factor of an iid-row matrix.

This formulation is closer to exchangeable-pair and random-matrix methods than a full angular-density theorem.

---

## 5. Why whitening or good conditioning alone cannot solve the problem

A tempting route is to argue that the full private Gram `G` is well-conditioned and therefore complementary null directions must be decorrelated. That is false as a deterministic statement, even under exact full-pool isotropy.

### Proposition P14-PARSEVAL-COUNTEREXAMPLE — PROVED

For every `D>=3`, there are arbitrarily small perturbations of full-spark Parseval frames

\[
Z\in\mathbb R^{(2D-2)\times D},
\qquad Z^TZ=I_D,
\]

for which the covariance of the null line of a uniformly chosen `(D-1)`-row block has an eigenvalue bounded below by a universal positive constant. In particular, exact full-pool isotropy and full spark alone do **not** imply

\[
\operatorname{tr}(M^2)=O(1/D).
\]

#### Construction

Start from a Parseval frame `Z_0` with first two rows

\[
z_1=z_2=e_1/\sqrt2,
\]

and with the remaining `2D-4` rows lying in `e_1^\perp` and forming a generic Parseval frame there. Such a frame can be obtained by taking any generic full-rank `(2D-4)x(D-1)` matrix and right-whitening it; genericity makes every `D-1` of those rows independent.

If a uniformly chosen block `B` of `D-1` rows excludes both special rows, then its rows span `e_1^\perp`, so its null line is exactly `e_1`. The probability of this event is

\[
p_D
=
\frac{\binom{2D-4}{D-1}}{\binom{2D-2}{D-1}}
=
\frac{D-2}{2(2D-3)}
\longrightarrow \frac14.
\]

The duplicated first two rows make some other blocks rank-deficient. Perturb all rows generically by an arbitrarily small amount and right-whiten again. For almost every perturbation all `(D-1)`-row blocks become full rank, `Z^TZ=I` remains exact after whitening, and by continuity the null directions of all blocks excluding the first two rows remain arbitrarily close to `e_1`. Hence

\[
\lambda_{\max}(M)\ge p_D-o(1),
\]

so the purity stays bounded away from zero.

This kills the proposed shortcut “whiten the full private pool, use `Z^TZ=I`, and conclude random-half null isotropy.” Some genuinely probabilistic orientation information about the iid-row polar frame is indispensable.

---

## 6. The exact relative-orientation target after whitening

The whitening identity nevertheless isolates a clean next theorem.

If `(x,y)` were a Haar-uniform ordered orthonormal pair, then for every deterministic symmetric matrix `H`,

\[
\boxed{
\mathbb E (x^THy)^2
=
\frac{D\operatorname{tr}(H^2)-(\operatorname{tr}H)^2}
{D(D-1)(D+2)}.
}
\tag{6.1}
\]

Proof: conditional on `x`, `y` is uniform on `x^perp`, so

\[
\mathbb E[(x^THy)^2\mid x]
=
\frac{\|Hx\|^2-(x^THx)^2}{D-1},
\]

and the spherical second/fourth moment formulas yield (6.1).

For positive definite `H`, if `kappa(H)<=K_0`, then

\[
\mathbb E
\frac{(x^THy)^2}{(x^THx)(y^THy)}
\le
\frac{K_0^2D}{(D-1)(D+2)}
=O_{K_0}(1/D).
\tag{6.2}
\]

Thus the post-whitening theorem does **not** need total-variation Haar behavior. It only needs a second-order relative-orientation estimate for the endpoint pair with respect to `H=G^{-1}`.

A concrete alternate target is therefore:

### P14-RELORIENT — OPEN

On the ordinary large-`D` strata, prove on a high-probability bounded-condition-number event for the full private Gram that

\[
\mathbb E
\left[
\frac{(x^TG^{-1}y)^2}
{(x^TG^{-1}x)(y^TG^{-1}y)}
\middle|D
\right]
\le \frac{C}{D},
\]

where `(x,y)` are the complementary endpoint null directions generated by a uniformly random balanced row partition of the polar frame `Z`.

This is an exchangeable random-partition statement and seems better aligned with the dependence structure than pretending the projected coordinates are iid.

---

## 7. Exact low-dimensional warning: normalized lines can be anisotropic even when the weighted tensor is isotropic

The normalization-bias issue is real, not an artifact of the proof.

Take `D=2` and let a row have iid coordinates `xi` with the centered two-point law

\[
\Pr\{\xi=-1\}=2/3,
\qquad
\Pr\{\xi=2\}=1/3.
\]

Scaling to variance one does not change its direction. For one row `(xi_1,xi_2)`, a unit null vector is proportional to `(xi_2,-xi_1)`. Its off-diagonal second moment is exactly

\[
\mathbb E\left[-\frac{\xi_1\xi_2}{\xi_1^2+\xi_2^2}\right]
=-\frac1{10},
\]

so the normalized line law is not Haar. Yet P14-COF-ISO gives exact isotropy after weighting by the squared cofactor norm. Convolving the two-point law with an arbitrarily small centered Gaussian (and recentering/rescaling if desired) gives a bounded-density subgaussian law with the same nonzero anisotropy by continuity.

This does not contradict the P14 theorem because `D=2` is deliberately isolated as a singular high-overlap stratum. It does show why one cannot expect “isotropic rows imply Haar null line” pointwise in `D`, and why the volume-normalization mechanism must be controlled rather than ignored.

---

## 8. Peer audit — P24-H2

**AUDIT_FOR:** P24 Probability Semigroup  
**Source:** Library file `file_0000000082f481f499e47cb6f1d99214`, claim `P24-H2`.  
**Verdict:** PROVED independently.

Let `nu` have density `f` with respect to normalized Haar measure `sigma_D`, let

\[
M=\int vv^Tf(v)d\sigma_D(v),
\qquad
B=M-I_D/D,
\]

and let `H` be symmetric traceless. Put `h_H(v)=v^THv`. The standard spherical fourth moment gives

\[
\int h_H(v)h_K(v)d\sigma_D(v)
=
\frac{2\operatorname{tr}(HK)}{D(D+2)}.
\]

Also

\[
\int h_H(v)(f(v)-1)d\sigma_D(v)=\operatorname{tr}(HB).
\]

Therefore the degree-two projection is exactly

\[
\Pi_2(f-1)(v)
=
\frac{D(D+2)}2 v^TBv.
\]

Taking the `L^2` norm gives

\[
\|\Pi_2(f-1)\|_2^2
=
\frac{D(D+2)}2\operatorname{tr}(B^2).
\]

Since

\[
\operatorname{tr}(M^2)=1/D+\operatorname{tr}(B^2),
\]

we obtain

\[
\boxed{
D\operatorname{tr}(M^2)-1
=
\frac{2}{D+2}\|\Pi_2(f-1)\|_2^2.
}
\]

The constants and normalization in P24-H2 are correct.

### How the new P14 lemma interacts with P24-H2

P24-H2 identifies the exact angular harmonic that must be controlled. P14-COF-ISO identifies an endogenous reweighting of the same line law under which that harmonic vanishes exactly. Thus the remaining task can be viewed either as

1. directly controlling `Pi_2(f_A-1)`, or
2. controlling how far the unweighted line law `nu_A` is from its cofactor-volume-size-biased 2-design `mu_A`.

The second formulation does not require differentiability of the density and may therefore be better suited to the original bounded-density hypothesis than the full Fisher-score route.

---

## 9. Literature audit and assumption correction

Nguyen--Vu, *Normal vector of a random hyperplane* (arXiv:1604.04897, IMRN 2018), is correctly usable for the single-normal `l_infinity` delocalization input under normalized subgaussian iid entries. Their Theorem 1.4 states the largest-coordinate bound without a symmetry assumption. However, the same theorem's **fixed-vector inner-product Gaussian limit explicitly adds the assumption that the entry law is symmetric**. Therefore a future P14 moment-comparison proof for general centered bounded-density subgaussian entries must not cite that fixed-vector normality statement without either adding symmetry or supplying a nonsymmetric replacement.

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures* (arXiv:1507.07949), proves that if coordinate densities are bounded by one, every `k`-dimensional marginal density is bounded by `2^{k/2}`. Its one-dimensional case gives the `sqrt(2) K` scalar-density cap used in P14-EDGE after scaling. This use remains valid because the scalar projection is taken in the **original independent-coordinate space** before conditioning on the other projected coordinates.

P12 and the latest P13 report reinforce the same conditioning discipline: one may condition on shared rows and then use fresh-row independence, but one must not import iid-coordinate matrix theorems into `BQ_A` after projection merely because its rows are independent.

---

## 10. Failed-route graveyard, updated

1. **Treat `v,w` as independent without conditioning on the shared block.** Invalid. They are conditionally independent given `A`; unconditionally they share the random complement `E_A`.

2. **Apply iid-entry rectangular least-singular-value theorems directly to `BQ_A`.** Invalid. Conditional on `A`, its rows are iid but their coordinates are dependent.

3. **Prove full total-variation or full `L^2` convergence to Haar.** Unnecessarily strong. P24-H2 shows only degree two is needed, and P14-EDGE already handles the singular near-one tail separately.

4. **Whiten the full private pool and use only `Z^TZ=I`.** Disproved by P14-PARSEVAL-COUNTEREXAMPLE. Exact Parseval structure plus full spark can still have a random-half null line with constant anisotropy.

5. **Use only the condition number of the full private Gram.** Also insufficient deterministically. The missing information is the relative orientation between `G^{-1}` and the complementary endpoint directions selected by the random partition.

6. **Replace the new size-biased criterion by a raw inverse determinant moment.** Invalid even for Gaussian rows: `E det(YY^T)^{-1}=infinity` in the `(D-1)xD` case because the Bartlett product contains `chi^2_2`.

7. **Use Nguyen--Vu fixed-vector Gaussian normality for nonsymmetric entries.** The primary theorem explicitly assumes symmetry for that clause. The `l_infinity` delocalization clause does not have this extra assumption.

8. **Use finitely many ordinary moments to control the singular kernel.** Insufficient near `|rho|=1`; P14-EDGE is the separate edge input.

9. **Condition on a global operator-norm event before invoking fresh-row independence.** Avoid this. As emphasized in P13, use the norm event only as a deterministic implication inside an intersection, or condition on variables that genuinely leave the fresh rows independent.

---

## 11. Exact ledger

### PROVED

- **P14-R1:** conditional shared-row reduction to two independent residual `(D-1)xD` matrices in `E_A`.
- **P14-R2:** conditional independence of residual null lines given `A`.
- **P14-R3:** `E[(v·w)^2|A]=tr(M_A^2)`.
- **P14-EDGE:** bounded-density subgaussian high-correlation tail
  \[
  P(1-rho^2<=eps|A) <= [C sqrt(eps log(e/eps))]^{D-1}.
  \]
- **P14-EDGE-INT:** the singular edge contributes `O(1/D)`.
- **P14-REDUCTION:** the full ordinary-stratum kernel bound reduces to `E_A tr(M_A^2)=O(1/D)`.
- **P24-H2, independently audited:** exact degree-two identity.
- **P14-COF-ISO (new):** `E[CC^T|A]=(D-1)!I`, hence `E[Wvv^T|A]=I/D` and `E[WW'(v·w)^2|A]=1/D`.
- **P14-SIZEBIAS (new):** with `mu_A=r_A nu_A`,
  \[
  D tr(M_A^2)-1 <= chi^2(nu_A||mu_A).
  \]
- **P14-SIZEBIAS-TAIL (new):**
  \[
  lambda_max(M_A)<=1/(cD)+nu_A{r_A<c}.
  \]
- **P14-BP-VOL (new):** `r_A(theta)=J_{3,A}(theta)/(D!J_{1,A}(theta))` and the exact determinant-ratio expression (3.4).
- **P14-WHITE (new):** after full-pool whitening the two complementary null directions become exactly orthogonal, with original correlation given by the `G^{-1}`-metric formula (4.2).
- **P14-PARSEVAL-COUNTEREXAMPLE (new):** full-pool exact isotropy/full spark alone does not force random-half null covariance `O(1/D)`.
- **Literature correction:** Nguyen--Vu's fixed-vector normality clause requires symmetric entries; their max-coordinate delocalization clause does not.

### CONDITIONAL

- The full P14 ordinary-stratum theorem follows if
  \[
  E_A chi^2(nu_A||mu_A)=O(1).
  \]
- It also follows if, for one fixed `c>0`,
  \[
  E_A nu_A\{r_A<c\}=O(1/D).
  \]
- Equivalently through the determinant-density route, it is enough to control the harmonic mean
  \[
  E_A\left[\frac{D!}{Z_{1,A}}\int J_{1,A}^2/J_{3,A}\,d\sigma_D\right]=O(1).
  \]
- P24's previously established sufficient criteria remain valid: averaged degree-two energy `O(D)`, line Fisher information `O(D)`, line entropy `O(1)`, or line chi-square-to-Haar `O(D)`.
- The whitening route closes if one proves the second-order relative-orientation estimate P14-RELORIENT for the balanced random partition endpoint pair.

### DISPROVED / REJECTED

- Full-pool Parseval/isotropy by itself implies the quadratic theorem.
- Bounded condition number by itself implies the quadratic theorem.
- Raw inverse determinant moments can replace the conditional volume-bias factor `r_A`.
- Projected residual coordinates may be treated as iid after conditioning on `A`.
- Nguyen--Vu fixed-vector normality may be imported for arbitrary nonsymmetric subgaussian entries.
- Total-variation Haar universality is a necessary target.

### OPEN

1. **Main theorem:**
   \[
   E_A tr(M_A^2)<=C/D
   \]
   uniformly for all ordinary `D>=3` under centered variance-one bounded-density subgaussian coordinates.
2. Prove `E_A chi^2(nu_A||mu_A)=O(1)` or the weaker volume-bias lower-tail criterion.
3. Prove P14-RELORIENT for the balanced random-half partition of the polar frame.
4. Determine whether the determinant ratio `J_3/(D!J_1)` admits a robust lower-tail bound from product-density anti-concentration plus subgaussianity.
5. Extend P14-EDGE beyond subgaussian tails without losing the integrable small-`Y` exponent.
6. Obtain two independent worker audits before any complete-theorem declaration.

---

## 12. Next attack

The highest-value next move is no longer to differentiate the full null-line density. Run two narrower routes in parallel.

### Route A — cofactor-volume bias

Prove, for a fixed numerical `c>0`,

\[
\boxed{
\mathbb E_A\nu_A\left\{
\frac{J_{3,A}(v)}{D!J_{1,A}(v)}<c
\right\}
\le \frac{C}{D}.
}
\]

This would close the quadratic theorem immediately by (2.6), uses no smooth score, and targets exactly the normalization defect that survives after the unnormalized cofactor tensor is shown to be isotropic.

A reasonable first sublemma is a conditional determinant-moment comparison for the hyperplane-section row law that controls `J_3/J_1` without introducing raw inverse determinants. Any proposed inequality must be tested against the Gaussian fact that raw inverse determinant moments diverge while the conditional ratio is perfectly benign.

### Route B — random-partition endpoint mixing

Conditional on the entire private pool, expose only a uniform balanced row partition and study the `-1,+1` endpoint eigenvectors of

\[
Z^TR_BZ.
\]

The target is a second-order estimate relative to `H=G^{-1}`, not a total-variation statement. The Parseval counterexample shows that one must use probabilistic structure of the iid-row polar factor beyond `Z^TZ=I`; the right hypotheses are likely quantitative row-spread/incoherence plus randomness inherited from the iid pool.

The two routes are compatible: Route A isolates normalization bias before whitening; Route B isolates relative orientation after whitening. Either one at the required scale, combined with the already-proved P14-EDGE estimate, finishes the bounded-density subgaussian D-stratified correlation theorem.

---

## 13. Primary references checked this run

- H. H. Nguyen and V. H. Vu, *Normal vector of a random hyperplane*, arXiv:1604.04897; IMRN 2018. Theorem 1.4: max-coordinate delocalization under normalized subgaussian iid entries; the fixed-vector Gaussian limit additionally assumes symmetry.
- G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; Israel J. Math. 216 (2016). Product marginal density bound, including the one-dimensional `sqrt(2)` constant after normalization.
- P14 prior report: Library `file_00000000e4f48230b3939949a4ecb32b`.
- P24 semigroup report: Library `file_0000000082f481f499e47cb6f1d99214`.
- P12 smooth-iid report: Library `file_00000000936081f6a725f2d3d2568409`.
- P13 fourth-moment report: Gmail source ID `1a09f693d77cd9d3`.

**Bottom line:** the high-correlation edge remains solved. The quadratic obstruction is now sharpened twice: first to an exact cofactor-volume size-bias comparison against a second-order-isotropic reference measure, and second to a balanced random-partition relative-orientation problem after full-pool whitening. The strongest deterministic shortcut suggested by whitening is explicitly false, so the next proof must use genuine probabilistic mixing or a conditional determinant-volume theorem.
