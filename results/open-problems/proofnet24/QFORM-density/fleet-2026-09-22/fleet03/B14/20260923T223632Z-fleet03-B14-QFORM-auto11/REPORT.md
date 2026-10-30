SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T22:36:32Z.
attacking: zero-loss connected-support localization — replace arbitrary remote fragments by smooth strictly-subcap single-interval laws without changing the universal QFORM constant, while keeping all support-diameter and floor parameters nonuniform.

# fleet03/B14 — zero-loss connected-support localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T223632Z-fleet03-B14-QFORM-auto11`  
Status: **NEW TARGET-LEVEL LOCALIZATION THEOREM / FULL QFORM OPEN**  
Continuity: **not transferred by this closure argument; full-target continuity remains OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact issue attacked

The owner target permits completely arbitrary fragmented and unbounded cap-one marginals. Earlier B14 work proved that no fixed fragment-count or bounded-diameter extremal reduction is valid. Later whole-law compactification/smoothing work showed that roughness and tails themselves can be removed with no loss in a uniform interval bound. The remaining localization question addressed here is sharper:

> Can one, without silently imposing connected support, prove that the universal QFORM constant is unchanged if every marginal is required to be smooth, strictly below the cap, and supported on one connected interval?

The answer is yes. The price is only that the interval length and the positive density floor are **not uniform** and may respectively tend to infinity and zero. That distinction is essential.

The theorem is stated for an arbitrary Borel output map, so it is not tied to a special QFORM branch.

## 2. Interval-density seminorm

For a probability measure `nu` on `R`, set

\[
\mathcal D(\nu)=\sup_{a<b}\frac{\nu((a,b))}{b-a}\in[0,\infty].
\tag{2.1}
\]

If `D(nu)<=C`, then `nu<=C dx` by the monotone-class/Lebesgue differentiation argument, hence `nu` has an essentially bounded density of height at most `C`. Conversely a density cap `C` gives `D(nu)<=C`.

Let `K` denote the class of one-dimensional probability densities `h` such that for some finite interval `[a,b]`:

1. `h in C_c^infty(R)`;
2. `supp h=[a,b]`;
3. `h(x)>0` for every `a<x<b`;
4. `0<=h(x)<1` for all `x`;
5. `int h=1`.

There is deliberately no common upper bound on `b-a` and no common positive lower bound on `h`.

## 3. Main theorem

### Theorem — `QFORM-SMOOTH-CONNECTED-SUPPORT-ZERO-LOSS-v1`

Let `F:R^n -> R` be any Borel map. Define

\[
C_{\rm all}(F)=\sup_{f_1,\ldots,f_n}\mathcal D\!\left(
F_\#\bigotimes_{i=1}^n f_i(x_i)dx_i\right),
\tag{3.1}
\]

where each `f_i` is an arbitrary probability density with `0<=f_i<=1`. Define `C_conn(F)` by the same formula with every `f_i` restricted to `K`. Then

\[
\boxed{C_{\rm all}(F)=C_{\rm conn}(F)}
\tag{3.2}
\]

including the value `+infinity`.

Consequently the full QFORM universal density constant is exactly unchanged if one restricts the input class to independent marginals that are smooth, compactly supported on a **single interval**, strictly positive on the interval interior, and strictly below one everywhere.

The reduction is zero-loss in the density constant and introduces no moment, common support radius, common centre, diameter, fragment-count, or separation parameter.

### Proof

Only `C_all<=C_conn` is nontrivial.

#### Step 1. Whole-law compact smooth approximation

Fix an arbitrary cap-one probability density `f`. We first recall a self-contained cap-preserving compactification. For `R>0`, let

\[
\delta_R=\int_{|x|>R}f(x)\,dx.
\]

Choose an interval `I_R` outside `[-R,R]` of length `delta_R` and put

\[
g_R^0=f\,1_{[-R,R]}+1_{I_R}.
\tag{3.3}
\]

Then `0<=g_R^0<=1`, `int g_R^0=1`, and

\[
\|g_R^0-f\|_1\le2\delta_R\to0.
\tag{3.4}
\]

Let `eta_epsilon` be a nonnegative compactly supported smooth probability mollifier. Then

\[
g_{R,\varepsilon}=g_R^0*\eta_\varepsilon
\tag{3.5}
\]

is a smooth compactly supported probability density with `0<=g_{R,epsilon}<=1`, and for fixed `R`,

\[
\|g_{R,\varepsilon}-g_R^0\|_1\to0.
\tag{3.6}
\]

Thus for every `delta>0` there is a smooth compact cap-one probability `g` with

\[
\|g-f\|_1<\delta.
\tag{3.7}
\]

No tail moment was used; tail **mass** alone was relocated.

#### Step 2. Fill every gap with arbitrarily small mass while preserving the cap

Fix such a smooth compact `g`. Choose once and for all a function

\[
\psi\in C_c^\infty((-1,1)),\qquad
\psi>0\ \text{on }(-1,1),\qquad
\int\psi=1.
\]

Choose `m in R` and `L>0` so large that

\[
\operatorname{supp} g\subset(m-L,m+L),
\qquad
L>\|\psi\|_\infty.
\tag{3.8}
\]

Set

\[
q_{m,L}(x)=\frac1L\psi\!\left(\frac{x-m}{L}\right).
\tag{3.9}
\]

Then `q_{m,L}` is a smooth probability density, is positive on the entire interval `(m-L,m+L)`, has support closure `[m-L,m+L]`, and

\[
\|q_{m,L}\|_\infty=\frac{\|\psi\|_\infty}{L}<1.
\tag{3.10}
\]

For `0<epsilon<1`, define

\[
h=(1-\varepsilon)g+\varepsilon q_{m,L}.
\tag{3.11}
\]

Then `h` is a probability density and

\[
0\le h(x)
\le(1-\varepsilon)+\varepsilon\|q_{m,L}\|_\infty
<1.
\tag{3.12}
\]

Moreover `h>0` throughout `(m-L,m+L)`, while it vanishes outside `[m-L,m+L]`; hence its support is one connected compact interval. Finally

\[
\|h-g\|_1
=\varepsilon\|q_{m,L}-g\|_1
\le2\varepsilon.
\tag{3.13}
\]

Combining (3.7) and (3.13), every arbitrary cap-one probability density is an `L^1` limit of densities in `K`.

The bridge density across a remote gap is allowed to be tiny: its scale is `epsilon/L`. Thus the construction never pays the distance between fragments. If the original compact approximation spans an enormous interval, `L` may be enormous; this is harmless because no theorem is allowed to use a diameter-dependent constant in this reduction.

#### Step 3. Tensorization and pushforward

For probability densities,

\[
\left\|\prod_{i=1}^n f_i-\prod_{i=1}^n h_i\right\|_1
\le\sum_{i=1}^n\|f_i-h_i\|_1,
\tag{3.14}
\]

by the telescoping identity. Therefore choose `h_i^{(k)} in K` so the product measures converge in total variation to the original product law.

Pushforward by a Borel map contracts total variation. Hence, for every finite interval `J`,

\[
F_\#\!\left(\bigotimes_i h_i^{(k)}dx_i\right)(J)
\longrightarrow
F_\#\!\left(\bigotimes_i f_i dx_i\right)(J).
\tag{3.15}
\]

If `C_conn(F)<infinity`, every left-hand side is at most `C_conn(F)|J|`; passing to the limit gives the same inequality for the arbitrary product law. Thus `C_all(F)<=C_conn(F)`. The reverse inequality is immediate because `K` is a subclass. This proves (3.2). `square`

## 4. Exact QFORM corollary

For

\[
F_A(x)=x^TAx+b^Tx+c,
\]

Theorem (3.2) applies for each fixed `(A,b,c)`. Taking the supremum over all dimensions and all symmetric matrices with `s_3(A)>=1` yields:

> To prove the original universal essential-density conjecture with constant `C`, it is enough to prove that same `C` for independent one-dimensional laws in `K`.

In particular, **disconnected support is not an irreducible analytic regime for a uniform bound**. It is a closure regime. But this statement must not be misread as an extremal theorem: a maximizing or near-maximizing law may still be highly fragmented, and earlier fixed-fragment-count/bounded-diameter obstructions remain valid. The connected approximants merely place an arbitrarily small positive bridge across the gaps and then use closure of a uniform interval estimate.

This also does not create a useful uniform density floor. The minimum of the approximating density can tend to zero as gaps grow. Any proof on `K` must be uniform as both

\[
\inf_{(a,b)}h\downarrow0
\quad\text{and}\quad
b-a\uparrow\infty.
\tag{4.1}
\]

## 5. Designated partner result applied to an actual target inequality

I apply the completed fleet04/B14 scale-covariant conjugate-shear theorem:

`yspennstate/math-open-problems@2ac84e141e8e939506cbd5cd8314589141b714d5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T051013Z-fleet04-B14-scale-shear-r7/REPORT.md`.

For independent cap-one `X_1,...,X_4`, it proves for

\[
Q=2cX_1X_2+\frac d2
\big((1-\alpha)X_3+(1+\alpha)X_4-\beta\big)^2
+\ell_1X_1+\ell_2X_2+\gamma
\tag{5.1}
\]

the target-level estimate

\[
\|p_Q\|_\infty\le4+2\log8<8.159
\tag{5.2}
\]

whenever `|c|>=1` and `|d|(1+alpha^2)>=1`. The theorem is uniform in every displayed translation and affine term.

Take the concrete target-valid specialization

\[
c=d=1,\qquad\alpha=0,
\tag{5.3}
\]

so

\[
Q=2X_1X_2+\frac12(X_3+X_4-\beta)^2
+\ell_1X_1+\ell_2X_2+\gamma.
\tag{5.4}
\]

The homogeneous matrix has nonzero eigenvalues `{1,-1,1}` and therefore exactly meets the three-large-eigenvalue threshold.

Now let any of the four marginals be arbitrarily remote and fragmented; for example one may take

\[
f_N=1_{E_N},\qquad
E_N=\bigcup_{j=1}^N[4j,4j+N^{-1}],
\tag{5.5}
\]

whose span diverges and whose component count is unbounded. Theorem (3.2) supplies smooth connected-support strict-subcap approximants `h_{N,k}` with

\[
\|h_{N,k}-f_N\|_1\to0.
\tag{5.6}
\]

Apply the partner estimate (5.2) to the product of these connected approximants. For every interval `I`,

\[
\Pr\{Q_k\in I\}
\le(4+2\log8)|I|.
\tag{5.7}
\]

Product total variation and pushforward contraction then give, for the original arbitrarily fragmented laws,

\[
\boxed{
\Pr\{Q\in I\}
\le(4+2\log8)|I|
}
\tag{5.8}
\]

and therefore

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le4+2\log8<8.159.}
\tag{5.9}
\]

This is an actual application of the partner theorem through the new localization interface: arbitrary fragment count, arbitrary separation, support diameter and deterministic translation are removed by an arbitrarily light connected bridge, while the numerical constant is unchanged.

I do **not** use fleet04/B14 r9's later-corrected interval-only rough-hub `L^infinity` inference. Only the completed r7 theorem above is used.

## 6. Consequence for the current proof tree

The new localization theorem changes what the remaining rough-law endpoint must look like.

A full proof may now assume, with no loss in the universal essential-density constant, that every input marginal is:

- `C_c^infinity`;
- strictly below the density cap one;
- positive on the interior of one compact interval;
- zero outside that interval.

Thus literal gaps and isolated fragments need not be handled combinatorially in the analytic core. What **cannot** be assumed uniformly is a bounded support diameter, a common centre, a positive lower density floor, bounded derivatives, log-concavity, or any moment bound. The analytic estimate must remain stable as the artificial bridges become arbitrarily thin and long.

Combined with the already proved generic-matrix/strict-margin closure, one may equivalently seek a uniform theorem on this smooth connected-support law class and generic symmetric matrices with `s_3>1`; all degeneracy parameters are allowed to approach their limiting values. This is a reduction of the analytic core, not a proof of it.

## 7. Status

- `QFORM-SMOOTH-CONNECTED-SUPPORT-ZERO-LOSS-v1`: **PROVED**.
- Full QFORM essential-density theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous density: **OPEN**. Total-variation closure of a uniform height bound does not by itself preserve continuity of the limiting density.
- No Gaussian, log-concavity, moment, bounded-diameter, fixed-fragment-count, post-rotation independence, arbitrary-joint coarea, or pointwise law-uniform quadratic Fourier decay assumption is used.

The next B14 implication should exploit this reduction in the genuinely overlapping near-degenerate pivot branch: since support gaps can be filled for free, one can work with smooth positive original-coordinate densities and seek a uniform whole-active estimate that survives when the bridge floor tends to zero, rather than separately localizing every distant fragment.
