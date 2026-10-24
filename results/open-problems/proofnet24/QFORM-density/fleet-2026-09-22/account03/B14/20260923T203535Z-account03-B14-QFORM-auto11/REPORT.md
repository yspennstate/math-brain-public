SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T20:35:35Z.
attacking: Lp localization through an arbitrary disjoint quadratic receiver bank using one physical row: aggregate all off-diagonal receiver couplings in l2 before paying a reciprocal coefficient, while preserving arbitrary shifts, distant fragments and unbounded supports.

# account03/B14 — aggregate-row Lp receiver localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T203535Z-account03-B14-QFORM-auto11`  
Control refresh: math-research-brain main, OWNER CONTROL revision `2026-09-22.15`.  
Status: `SUPPORTING_THEOREM_PROVED / FULL_QFORM_OPEN`.  
Continuity: proved on the branch below; full-target continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Mechanism change after the latest correction

The first candidate for this run was only to replace the preceding nonzero-diagonal receiver by a nonzero physical 2x2 entry. Before using it, I read account03/B15's current correction report (`20260923T202515Z-account03-B15-qform-auto11`). That report proves the sharp translation-uniform Lq theorem for a single quadratic-plus-linear square and explains why a large affine slope cannot improve the bound when nonzero curvature remains: the input law may translate to the moving critical point.

So I did not duplicate that scalar theorem. Instead I retain the whole original-coordinate receiver row until after the singular derivative has been averaged. This gives an l2 aggregate over arbitrarily many off-diagonal couplings, and is exactly the kind of aggregate-before-inversion step requested by the live corrections.

## 2. Two elementary inputs

### Lemma 2.1 — cap-M Riesz bathtub

If a real random variable Y has a probability density bounded by M, then for every `0<alpha<1` and every `s in R`,

\[
\boxed{
\mathbb E|Y-s|^{-\alpha}
\le {2^\alpha M^\alpha\over 1-\alpha}.
}
\tag{2.1}
\]

Proof. The decreasing kernel `|y-s|^{-alpha}` is maximized under the density cap and mass-one constraint by the density `M` on the centered interval of length `1/M`. Hence

\[
M\int_{-1/(2M)}^{1/(2M)}|u|^{-\alpha}du
={2^\alpha M^\alpha\over1-\alpha}.
\]

No support or moment condition appears. QED.

### Lemma 2.2 — product projection cap

For independent cap-one original coordinates `W=(W_1,...,W_m)` and nonzero `a in R^m`, the already source-pinned product-projection theorem in the QFORM corpus gives

\[
\|p_{a^TW}\|_\infty\le {\sqrt2\over\|a\|_2}.
\tag{2.2}
\]

Conditioning on all coordinates except one also gives

\[
\|p_{a^TW}\|_\infty\le {1\over\|a\|_\infty}.
\tag{2.3}
\]

Thus define the aggregate row cap certificate

\[
\boxed{
\mathcal C(a):=
\min\left\{{1\over\|a\|_\infty},{\sqrt2\over\|a\|_2}\right\}.
}
\tag{2.4}
\]

Every affine translate of `a^T W` has the same cap. The l2 alternative is crucial when a row is spread over many individually tiny coordinates.

The explicit source used for (2.2) in this slot is the preceding collective-leakage report at `math-open-problems@20e9f45a5d8c8d79034aa09318d8922daae66599`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T103613Z-account03-B14-QFORM-r33/REPORT.md`, equation (1.3).

## 3. Main theorem — one entire receiver row, not one coefficient

### Theorem 3.1 — `QFORM-LP-AGGREGATE-ROW-RECEIVER-LOCALIZATION-v1`

Let `1<q<2` and `p=q/(q-1)`. Let `W=(W_1,...,W_m)` have independent real probability densities bounded by one. Let `Z` be any random object independent of `W`. Suppose that, conditional on `Z=z`, another variable `T_z`, built from variables independent of the complete bank `W`, has a density satisfying

\[
\|p_{T_z}\|_p\le K
\tag{3.1}
\]

for almost every `z`, with the same K.

Let `C` be an arbitrary real symmetric `m x m` matrix and allow arbitrary measurable affine terms `beta(z) in R^m`, `gamma(z) in R`. Put

\[
R_z(W)=W^T C W+\beta(z)^T W+\gamma(z),\qquad Q=T_Z+R_Z(W).
\tag{3.2}
\]

Choose an original receiver coordinate `i` whose physical row

\[
a_i=(C_{i1},...,C_{im})\ne0.
\tag{3.3}
\]

Then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le
K\left({2^{q-1}\over 2-q}\right)^{1/q}
\mathcal C(a_i)^{(q-1)/q}.
}
\tag{3.4}
\]

In particular, using only the l2 row norm `r_i=||a_i||_2`,

\[
\boxed{
\|p_Q\|_\infty
\le
K\left({2^{3(q-1)/2}\over 2-q}\right)^{1/q}
 r_i^{-(q-1)/q}.
}
\tag{3.5}
\]

At the rough-hub conjugate exponents `p=3`, `q=3/2`,

\[
\boxed{
\|p_Q\|_\infty\le 2K\,\mathcal C(a_i)^{1/3}
\le 2^{7/6}K\,r_i^{-1/3}.
}
\tag{3.6}
\]

The density on this branch has a continuous representative. Every constant is independent of receiver dimension, all receiver coefficients outside the selected row norm, every affine translation, support radii, fragment counts and separations, and all moments.

### Proof

Relabel the selected coordinate as `U=W_1` and write the remaining receiver coordinates as `V`. Write

\[
d=C_{11},\qquad c=(C_{12},...,C_{1m}),\qquad a_1=(d,c).
\]

For fixed `z` and `v`, the receiver is a one-variable quadratic

\[
g_{z,v}(u)=d u^2+2(c^Tv+\beta_1(z)/2)u+H_z(v),
\tag{3.7}
\]

where `H_z(v)` is completely arbitrary. It contains all receiver curvature and cross-terms not involving U, every remaining affine term, and the scalar shift.

If `d!=0`, the pushforward of U by (3.7) has a density `h_{z,v}`. At every regular output the two possible quadratic preimages have derivative magnitudes equal to each other. Since `f_U<=1`, evaluating the density at an output generated by U gives

\[
h_{z,v}(g_{z,v}(U))
\le
{1\over |dU+c^Tv+\beta_1(z)/2|}.
\tag{3.8}
\]

Indeed the density is a sum of at most two terms `f_U(u_k)/|g'(u_k)|`, while `|g'(u_k)|=2|d u_k+c^Tv+beta_1/2|` and the two derivative magnitudes coincide.

If `d=0`, then `c!=0` because the selected row is nonzero. For almost every v the map in u is affine and its density is at most `1/[2|c^Tv+beta_1/2|]`, hence (3.8) still holds. The exceptional zero-slope hyperplane has probability zero because `c^TV` has an absolutely continuous law.

Set `alpha=q-1 in (0,1)`. Using `int h^q=E[h(Y)^(q-1)]`, (3.8) gives

\[
\|h_{z,v}\|_q^q
\le
\mathbb E_U |dU+c^Tv+\beta_1(z)/2|^{-\alpha}.
\tag{3.9}
\]

Now average over V only after this singular power has been formed. Minkowski and the concavity of `x^(1/q)` give

\[
\begin{aligned}
\|p_{R_z}\|_q
&\le \mathbb E_V\|h_{z,V}\|_q\\
&\le
\left(
\mathbb E_{U,V}
|dU+c^TV+\beta_1(z)/2|^{-\alpha}
\right)^{1/q}.
\end{aligned}
\tag{3.10}
\]

The variable inside the absolute value is exactly the original-coordinate product projection `a_1^T W` plus a translation. By (2.4) its density cap is at most `mathcal C(a_1)`. Applying Lemma 2.1 to (3.10) gives

\[
\|p_{R_z}\|_q
\le
\left({2^\alpha\over1-\alpha}\right)^{1/q}
\mathcal C(a_1)^{\alpha/q},
\tag{3.11}
\]

which is (3.4). Using `mathcal C(a_1)<=sqrt(2)/r_1` gives (3.5).

Conditional on Z=z, the core `T_z` is independent of the receiver bank W. Young-Hoelder convolution therefore yields (3.4) for `Q|Z=z`, uniformly in z. Averaging in z preserves the same essential bound.

For each z, convolution of an `L^p` density and an `L^q` density with finite conjugate exponents is continuous and vanishes at infinity. The conditional sup bound is uniform in z, so dominated convergence gives a continuous representative after averaging over Z. QED.

## 4. Why this is stronger than paying one physical coefficient

Suppose the selected receiver row has zero diagonal and m equal off-diagonal coefficients `m^(-1/2)`. Then

\[
\|a_i\|_2=1,\qquad \|a_i\|_\infty=m^{-1/2},
\]

so

\[
\mathcal C(a_i)\le\sqrt2
\tag{4.1}
\]

uniformly in m. The theorem therefore pays the whole diffuse row by the fixed factor `2^(7/6)` at q=3/2.

By contrast, selecting one off-diagonal coefficient first gives scale `m^(-1/2)` and a q=3/2 reciprocal cost proportional to `m^(1/6)`. The preceding physical-diagonal theorem is unusable because the diagonal is exactly zero. Thus (3.4) closes a genuine diffuse off-diagonal localization gap rather than merely changing constants.

## 5. Actual application of designated partner account04/B14

The designated partner report is

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

I use only its still-valid slice-Fourier equation (3.6), not its corrected interval-only rough-hub L-infinity inference. In the partner's heavy-null residual-diffuse normal form,

\[
|\widehat\mu_{l,g}(t)|
\le4\sqrt\pi\,|\gamma t|^{-1/2},
\tag{5.1}
\]

uniformly in arbitrary conditioning-generated affine leakage and all support/tail geometry.

Write the physical hub slope as `L=hV+q_0`. After changing the slice variable,

\[
|\widehat\mu_l(t)|
\le A|t|^{-1/2},\qquad
A={4\sqrt\pi\over |h|\sqrt{|\gamma|}}.
\tag{5.2}
\]

Retain any measurable real hub phase `H(X_0)` and define `T=H(X_0)+2X_0L+Y`. If

\[
F_t(l)=\int f_0(x)e^{itH(x)}e^{2itlx}dx,
\]

then Plancherel gives

\[
\int |F_t(l)|^2dl\le {\pi\over|t|}.
\tag{5.3}
\]

Because `|mu_hat_l(t)|` is bounded both by its slice mass and by (5.2), its squared l-integral is at most `A|t|^(-1/2)`. Cauchy-Schwarz therefore gives the whole-law estimate

\[
|\phi_T(t)|
\le
\min\left\{1,
2\pi^{3/4}|h|^{-1/2}|\gamma|^{-1/4}|t|^{-3/4}
\right\}.
\tag{5.4}
\]

Integrating the 3/2 power exactly at the crossover and applying inverse Hausdorff-Young gives

\[
\boxed{
\|p_T\|_3
\le
3^{4/3}2^{8/9}
|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{5.5}
\]

Now append an arbitrary disjoint original-coordinate quadratic receiver bank with selected physical row norm `r_i>0`. Applying Theorem 3.1 at `p=3,q=3/2` yields the actual partner-derived inequality

\[
\boxed{
\|p_Q\|_\infty
\le
3^{4/3}2^{17/9}
\mathcal C(a_i)^{1/3}
|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{5.6}
\]

Using only the aggregate l2 row norm,

\[
\boxed{
\|p_Q\|_\infty
\le
3^{4/3}2^{37/18}
 r_i^{-1/3}|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{5.7}
\]

At unit active scales `r_i,|h|,|gamma|>=1`, the constant in (5.7) is

\[
17.98645406618923\ldots.
\tag{5.8}
\]

The density is continuous on this branch.

## 6. Exact-target diffuse-star stress family

For `m>=2`, take mutually independent arbitrary cap-one variables and define

\[
L={X_1+X_2+X_3+X_4\over2},\qquad
V={X_1+X_2-X_3-X_4\over2},
\]

\[
Q_m=
2X_0L+{1\over2}V^2
+{2X_5\over\sqrt m}\sum_{j=1}^m X_{5+j}.
\tag{6.1}
\]

The deterministic coefficient vectors defining L and V are orthonormal. In the corresponding deterministic basis, the first core has nonzero spectrum

\[
\{1,-1,1/2\}.
\tag{6.2}
\]

The last term is a disjoint star with coupling row `m^(-1/2)(1,...,1)`, hence its nonzero spectrum is `{1,-1}`. Therefore the complete form has nonzero spectrum

\[
\boxed{\{1,-1,1/2,1,-1\}},
\tag{6.3}
\]

so it lies inside the exact owner target for every m.

The selected receiver hub `X_5` has zero physical diagonal and every individual coupling tends to zero, but its complete physical row has l2 norm one. The partner-core identification from the preceding checked control is `|h|=2^(-1/2)`, `|gamma|=1`. Thus (5.7) gives

\[
\boxed{
\|p_{Q_m}\|_\infty
\le
3^{4/3}2^{41/18}
=20.98172098721166\ldots
}
\tag{6.4}
\]

for every m and every admissible product law, with a continuous density. The estimate is uniform under arbitrary translations, distant fragmentation and unbounded support.

This family exhibits the gain clearly: a one-coordinate payment sees only `m^(-1/2)` and deteriorates, while aggregate-row localization sees the invariant l2 resource `1` before any reciprocal is taken.

## 7. Scope and remaining full-target implication

The unrestricted QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. The theorem requires a source-disjoint `L^p` core and a disjoint receiver bank containing one nonzero physical row. The bare condition `s_3(A)>=1` has not been shown to force that decomposition with both the core constant and the aggregate receiver row norm universally controlled.

The useful reduction is sharper than in the preceding B14 run: **inside any disjoint quadratic receiver bank, a nonzero physical diagonal is no longer needed. An arbitrary diffuse off-diagonal row is enough, and all same-bank curvature away from that row is free.** The next obstruction is the genuinely overlapping case where the row providing the third smoothing resource reuses original coordinates already needed to produce the `L^p` core. There product provenance must be preserved jointly rather than recovered after conditioning.

Full-target continuity remains open, although continuity is proved on Theorem 3.1's branch.

## 8. Integrity

- Current source corrections were refreshed before publication.
- account03/B15's latest correction was used to avoid a duplicate/false affine-slope route; its nonzero-curvature warning is respected.
- Designated partner account04/B14 is actually applied at equations (5.1)-(5.7), using only its valid slice-Fourier estimate.
- No Gaussianity, log-concavity, compact support, connected support, moment assumption, rotation-induced independence, arbitrary-joint coarea estimate, uniform pointwise quadratic-phase decay, finite fragment-count assumption or Monte Carlo inference is introduced.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
