# account04/B15 — critical logarithmic all-shift tariff for the exact I-projection KL

**Run:** `20260922T101332Z-B15-FEI-r11-n4v2`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NONLINEAR_KL_SCALE_RECOVERY / CRITICAL_COEFFICIENT_THEOREM`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact source state and the quantity actually being paid

This run uses the newest completed account02/B15 negative-credit theorem available at the scientific head,

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T085941Z-account02-B15-r16a/...`

(scientific archive commit `a8b2cd9bc7f615393879ae0cf83f6f5a1083beed`), together with its immediately preceding exact I-projection theorem at commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`.

For a nonconstant Boolean gate/source, write `P=w^+` for its actual nonempty squared spectral law and

\[
r_i=P(i\in S)=\frac{\operatorname{It}_i(G;p)}{v},
\qquad v=V_{p_{\rm out}}.
\]

Let `Q_r` be the unique maximum-entropy conditional-product law on nonempty subsets with the same coordinate marginals.  For an arbitrary symmetric potential `Gamma`, put

\[
a_i=\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad
a_q=\frac{\Gamma(q)+h_2(v)}{v}.
\]

The exact normalized remainder is

\[
\boxed{
R_\Gamma
=\sum_i r_i a_i-a_q-H(P)
=B_{\rm inf}^{\Gamma}+K_{\rm occ},
}
\tag{0.1}
\]

where

\[
B_{\rm inf}^{\Gamma}
=\sum_i r_i a_i-a_q-H_{\max}(r),
\qquad
\boxed{K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P)}.
\tag{0.2}
\]

Thus the exact information-theoretic payment still required is

\[
\boxed{
K_{\rm occ}\ge[-B_{\rm inf}^{\Gamma}]_+.
}
\tag{0.3}
\]

The account02/B15 suspension theorem proves that (0.3), even after every coordinate first moment is optimally paid, contains ordinary FEI isometrically on a codimension-one Boolean face.  It also proves that losing any fixed positive fraction of `K_occ` cannot be repaired by an `O(J)` valuation bank on its sparse one-point-defect suspensions.  The valuation reserve is therefore retained as a distinct arithmetic currency; it is not substituted for the KL in this report.

The previous account04/B15 run tested the most direct multi-shift suggestion: sum *all* signed Boolean convolution violations quadratically.  Its total energy is only `O(I)` on the sparse suspension family, while `K_occ` is `Theta(m I)`, so every fixed quadratic tariff fails.  This run changes method: it keeps the rare-event logarithm rather than the raw `L^2` energy.

## 1. The genuine Boolean calibration family

Let

\[
p=2^{1-m},
\qquad
g_m(x)=1-2\mathbf 1_{\{x=0\}},
\qquad
F_m(y,x)=y\,g_m(x).
\tag{1.1}
\]

The old-coordinate Walsh coefficients of `g_m` have one positive coefficient and otherwise a common negative magnitude:

\[
\widehat g_m(\varnothing)=1-p,
\qquad
\widehat g_m(T)=-p\quad(T\ne\varnothing).
\tag{1.2}
\]

Every old-coordinate influence is exactly `p`, hence

\[
I(g_m)=m p.
\tag{1.3}
\]

For the suspension `F_m`, the influence I-projection is deterministic in the new coordinate `y` and is product Bernoulli-`p` on the `m` old coordinates.  Put

\[
a=\sqrt{1-p},\qquad b=\sqrt p.
\]

Sign-align the square roots of that I-projection with the actual Walsh signs of `g_m`.  The resulting normalized amplitude vector is the Fourier coefficient vector of

\[
\boxed{
G_m(x)=2a^m-\prod_{i=1}^m(a+b x_i).
}
\tag{1.4}
\]

For a nonzero XOR shift `U`, define the full signed convolution defect

\[
C_m(U)=\sum_T b_T b_{T\triangle U}
=\widehat{G_m^2}(U),
\tag{1.5}
\]

where `b_T` denotes the signed I-projection amplitude.  Since `||b||_2=1`, `|C_m(U)|\le1`.

The new nonlinear statistic is the **logarithmic all-shift tariff**

\[
\boxed{
\mathcal L_m
:=\sum_{U\ne\varnothing}
C_m(U)^2\log_2\frac1{C_m(U)^2},
}
\tag{1.6}
\]

with `0 log(1/0)=0`.

Unlike the preceding quadratic energy, (1.6) charges a small Boolean convolution defect by its self-information.  It is still built only from the full family of physical Walsh convolution identities; no arbitrary probability-law relaxation is introduced.

## 2. Exact shift-shell formula

### Theorem 2.1 — every shift is explicit

If `r=|U|>=1`, then

\[
\boxed{
C_m(U)
=(2\sqrt{p(1-p)})^r
-4(1-p)^{m-r/2}p^{r/2}.
}
\tag{2.1}
\]

In particular,

\[
\boxed{
C_1
=2\sqrt{p(1-p)}\left[1-2(1-p)^{m-1}\right],
}
\tag{2.2}
\]

and

\[
\boxed{
C_2
=4p\left[(1-p)-(1-p)^{m-1}\right].
}
\tag{2.3}
\]

### Proof

Write

\[
P_m(x)=\prod_i(a+b x_i).
\]

Then `G_m=2a^m-P_m` and

\[
G_m^2=4a^{2m}-4a^mP_m+P_m^2.
\]

For a nonempty `U` of size `r`,

\[
\widehat P_m(U)=a^{m-r}b^r.
\]

Also

\[
P_m(x)^2
=\prod_i(1+2ab x_i),
\]

so

\[
\widehat{P_m^2}(U)=(2ab)^r.
\]

The constant term contributes nothing to a nonzero shift, hence

\[
\widehat{G_m^2}(U)
=(2ab)^r-4a^{2m-r}b^r,
\]

which is (2.1).  QED.

The adjacent checker reconstructs the entire amplitude vector and all XOR correlations directly through `m=7`; the closed formula matches to floating error below `3e-16`.

## 3. The logarithm restores the missing rare-event scale

### Theorem 3.1 — exact asymptotic tariff scale

For the Boolean family (1.1),

\[
\boxed{
\frac{\mathcal L_m}{4I(g_m)}
=m-3+o(1).
}
\tag{3.1}
\]

### Proof

From (2.2),

\[
C_1^2
=4p(1-p)\left[2(1-p)^{m-1}-1\right]^2
=4p\,[1+O(mp)].
\tag{3.2}
\]

Since `p=2^{1-m}` and `mp->0`,

\[
\log_2\frac1{C_1^2}
=\log_2\frac1{4p}+o(1)
=m-3+o(1).
\tag{3.3}
\]

There are `m` singleton shifts.  Their contribution therefore satisfies

\[
\frac{mC_1^2\log_2(1/C_1^2)}{4mp}
=m-3+o(1).
\tag{3.4}
\]

It remains to show that every higher shift shell contributes `o(I)`.  For `r=2`, Bernoulli's inequality in (2.3) gives

\[
|C_2|\le4(m-2)p^2,
\]

hence

\[
\binom m2|C_2|=O(m^3p^2)=o(mp).
\tag{3.5}
\]

For `r>=3`, (2.1) gives

\[
|C_r|\le(2^r+4)p^{r/2}\le2(2\sqrt p)^r.
\]

Therefore

\[
\sum_{r\ge3}\binom mr|C_r|
=O((m\sqrt p)^3)=o(mp).
\tag{3.6}
\]

Finally, for `0<=x<=1`,

\[
x^2\log_2(1/x^2)
\le\frac{2}{e\ln2}\,x.
\tag{3.7}
\]

Applying (3.7) to (3.5)-(3.6) proves that the entire `r>=2` contribution to `mathcal L_m` is `o(mp)=o(I)`.  Combine with (3.4).  QED.

This is the point at which the nonlinear statistic differs qualitatively from the old quadratic energy: its singleton defects have squared size `~4p`, but the logarithm contributes the missing factor `log_2(1/p)=m-1`.

## 4. Comparison with the exact negative KL credit

The account02/B15 suspension pullback gives here

\[
H_{\max}(r)=m h_2(p),
\qquad
K_{\rm occ}(F_m)=m h_2(p)-H(g_m).
\tag{4.1}
\]

The exact spectrum (1.2) gives

\[
H(g_m)
=-(1-p)^2\log_2(1-p)^2
-(2^m-1)p^2\log_2 p^2,
\tag{4.2}
\]

and hence

\[
\frac{H(g_m)}{I(g_m)}\to4.
\tag{4.3}
\]

Also

\[
\frac{h_2(p)}p
=\log_2\frac1p+\frac1{\ln2}+o(1)
=m-1+\frac1{\ln2}+o(1).
\]

Thus

\[
\boxed{
\frac{K_{\rm occ}(F_m)}{I(g_m)}
=m-5+\frac1{\ln2}+o(1).
}
\tag{4.4}
\]

Combining (3.1) and (4.4) yields the main result of this run.

### Theorem 4.1 — critical coefficient and additive-`O(I)` recovery

\[
\boxed{
K_{\rm occ}(F_m)
=\frac14\mathcal L_m
-\left(2-\frac1{\ln2}\right)I(g_m)
+o(I(g_m)).
}
\tag{4.5}
\]

Numerically,

\[
2-\frac1{\ln2}=0.557304959111036\ldots.
\]

More generally, for every fixed real `theta`,

\[
\boxed{
\frac{\theta\mathcal L_m-K_{\rm occ}(F_m)}{m I(g_m)}
\longrightarrow 4\theta-1.
}
\tag{4.6}
\]

Consequently `theta=1/4` is the **unique scale-critical coefficient** for a transfer of the form

\[
K_{\rm occ}\stackrel{?}{\ge}\theta\mathcal L-O(I)
\tag{4.7}
\]

on this genuine Boolean family:

- if `theta<1/4`, the tariff under-recovers the required KL by order `mI`, so no fixed `O(I)` or `O(J)` reserve can turn it into the no-loss Shannon payment needed by the sparse suspensions;
- if `theta>1/4`, the right side of (4.7) exceeds the actual `K_occ` by order `mI`, so (4.7) itself is false eventually for every fixed `O(I)` correction;
- at `theta=1/4`, the mismatch collapses from order `mI` to the finite asymptotic price `(2-1/ln 2)I`.

In particular, because the limiting correction is `<I`, there exists `m_0` such that

\[
\boxed{
K_{\rm occ}(F_m)\ge\frac14\mathcal L_m-I(g_m)
\qquad(m\ge m_0).
}
\tag{4.8}
\]

Equation (4.8) is a theorem only for this calibration family; it is **not** promoted to arbitrary Boolean spectra.

## 5. Why this is not merely a support refund or a valuation restatement

For `F_m`, every Fourier coefficient on its suspension support is nonzero, and the I-projection has exactly that same support: the new coordinate is deterministic and all old Bernoulli parameters lie in `(0,1)`.  Therefore the account01/B15 exact support-mismatch refund

\[
K_{\rm supp}=-\log_2(1-Q_r(\operatorname{supp}P))
\]

is exactly zero on this family.  The `Theta(mI)` quantity in (4.4) is genuine **shape/dependence KL**, not support mismatch.

Likewise, account02/B15's no-loss theorem already shows that a fixed fractional loss of this KL cannot be repaired by the available `O(J)` arithmetic/valuation bank.  The new logarithmic statistic succeeds precisely because it preserves the sparse rare-event self-information which the raw all-shift `L^2` energy erased.  No packet-integrality hypothesis is used anywhere.

## 6. Weakest surviving Interface-D target

The previous three scalar/quadratic routes all fail on actual Boolean families:

1. first moments alone leave `K_occ` and contain FEI isometrically under suspension;
2. a single complement packet yields only an exponentially small dimension-dependent payment;
3. the complete family of convolution identities with a fixed quadratic tariff is only `O(I)` on the sparse suspension while `K_occ=Theta(mI)`.

The present theorem shows exactly what those mechanisms were missing: **the logarithm of the rarity of each signed convolution defect**.

A source-consistent next target is therefore to first spend the exact support refund

\[
K_{\rm occ}
=K_{\rm supp}+D(P\Vert Q_r(\cdot\mid\operatorname{supp}P)),
\]

and then ask whether, on the remaining physical signed source (especially the composition-prime `c<1` corridor), a canonical support-conditioned logarithmic all-shift tariff satisfies a bound of the form

\[
\boxed{
D(P\Vert Q_r(\cdot\mid\operatorname{supp}P))
\ge \frac14\mathcal L_{\rm phys}-\kappa I
}
\tag{6.1}
\]

for some finite `kappa`, or else whether an actual Boolean prime source refutes it.  The coefficient `1/4` is not a guess: Theorem 4.1 shows that **any full-source transfer intended to survive the sparse Boolean suspension calibration has no other possible leading coefficient**.

Because exact disjoint composition of `K_occ` and of the full remainder is already known, a proof aimed only at composition-prime outer gates could in principle exploit stronger structure and evade the suspension calibration.  But any proposed all-source arithmetic/Shannon transfer that is meant to compose without losing KL must respect (4.6).

## 7. Status and handoff

**Prior missing implication:** pay `[-B_inf^Gamma]_+` from the exact dependence credit `K_occ`, retaining the complete relative entropy.

**New proved inference:** on the account02 sparse Boolean suspensions, the nonlinear full-shift statistic (1.6) recovers `K_occ` at its exact leading scale, and `1/4` is the unique coefficient compatible with an additive `O(I)` remainder.

**Exact refutation:** every coefficient below `1/4` underpays by `Theta(mI)` and every coefficient above `1/4` overclaims a lower bound by `Theta(mI)` on the same genuine Boolean family.  The raw quadratic all-shift payment remains dead.

**Replacement obligation:** prove or refute a source-exact support-conditioned inequality of type (6.1), preferably first on composition-prime balanced `c<1` sources, while retaining the support KL, the residual shape KL, and any valuation reserve as separate currencies.

**Full FEI:** remains **OPEN / NOT PROVED**.
