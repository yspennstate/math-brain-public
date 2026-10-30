SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T15:06:22Z.
attacking: mass-homogeneous chirp-slice localization — extend the newest partner whole-support L2 compiler to a full Lp subprobability scale, then identify exactly when active Fresnel fragmentation destroys the mass power.

# fleet02/B14 r38 — chirp-slice Lp mass homogeneity and an active-Fresnel fragmentation barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: translations and localization; complementary constructions/source-valid counterexamples  
Status: **NEW SUPPORTING LOCALIZATION THEOREM / EXACT-TARGET PROOF-INTERFACE OBSTRUCTION / FULL QFORM OPEN**  
Continuity: separate and not proved here.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The newest fleet03/B14 r38 theorem makes an arbitrary one-variable chirp free at the whole-law `L^2` level, but the full localization issue is the *mass homogeneity* of the unnormalised slice Fourier coefficient. The precise next implication is:

> before refining a curvature-active bank, either prove an unnormalised slice estimate whose critical coefficient is at most a universal constant times the bank-piece mass, or pay a whole-active D'/D5/ridge/hub/Fresnel certificate before refinement.

The theorem below proves that this mass-linear slice condition is sufficient for **zero-tax arbitrary positive localization** at every output `L^p`, `2<=p<4`, and after one independent square receiver it gives an `L^infinity` target bound with the same zero-tax property. The fixed exact-target example in Section 5 proves that fragmenting the active Fresnel coordinate first can violate this mass scaling and forces a growing certificate even though the law itself is unchanged and Claude's completed Theorem A keeps its true density uniformly bounded.

## 2. Exact partner input

The designated partner result actually used is fleet03/B14 r38, `QFORM-CHIRP-SLICE-L2-COMPILER-v1`, source

`yspennstate/math-open-problems@0bd14ffdefeeb7e94e99c9f48b4220aa40ff55be`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T143741Z-fleet03-B14-QFORM-r38/REPORT.md`.

For a cap-one probability variable `X` independent of `(L,Y)`, with

`P{L in dl,Y in dy}=nu_l(dy) dl`, `int nu_l(R) dl=1`,

and

`ess sup_l |hat(nu_l)(t)| <= A |t|^{-1/2}`,

it proves that for arbitrary measurable real `H`,

`T=H(X)+2XL+Y`

obeys

`|phi_T(t)| <= sqrt(pi A)|t|^{-3/4}`

and has an `L^2` density. The proof is whole-law Plancherel in the genuine original coordinate `X`; multiplication by `exp(itH(X))` is unimodular, so arbitrary quadratic self-phase, translations, distant fragments, unbounded supports and moments cost nothing.

I now keep the partner proof unnormalised and compute its full mass homogeneity.

## 3. Subprobability chirp-slice `L^p` compiler

Let `X` have a probability density `f` with `0<=f<=1`. Let the bank be a finite positive measure of total mass `m`, `0<m<=1`, on `(L,Y)`, independent of `X`, with Lebesgue disintegration

`mu_{L,Y}(dl,dy)=nu_l(dy) dl`,

so

`int nu_l(R) dl=m`.

Assume that for some `A>0`, every `t!=0` satisfies

`ess sup_l |hat(nu_l)(t)| <= A |t|^{-1/2}`.                 (3.1)

Let `H:R->R` be any measurable real function and let `mu_T` be the pushforward submeasure under

`T=H(X)+2XL+Y`.                                               (3.2)

### Theorem `QFORM-CHIRP-SLICE-LP-MASS-HOMOGENEITY-v1`

For every `t!=0`,

`|hat(mu_T)(t)| <= min{m, sqrt(pi m A)|t|^{-3/4}}`.            (3.3)

For every `4/3<q<=2`, put `p=q/(q-1)`, so `2<=p<4`. Then `mu_T` has an `L^p` density and

`boxed:
||p_T||_p <= (2pi)^(-1/q) [6q/(3q-4)]^(1/q)
             (pi A)^(2/(3q)) m^(1-2/(3q)).`                  (3.4)

In particular, if a positive localization of the bank into submeasures `mu_j` has masses `m_j` and slice constants

`A_j <= A_0 m_j`,                                             (3.5)

then

`||p_{T,j}||_p <= C_{p,A_0} m_j`,                             (3.6)

and summing an arbitrary finite or countable localization gives exactly the same whole-law constant because `sum_j m_j=1`. There is no fragment-count, fragment-location, support-diameter, translation, tail, or moment factor.

### Proof

For fixed `t!=0`, define exactly as in fleet03/B14 r38

`G_t(l)=int f(x) exp(itH(x)) exp(2itlx) dx`,

and

`B_t(l)=hat(nu_l)(t)`.

Whole-law Plancherel gives

`int |G_t(l)|^2 dl <= pi/|t|`.                                (3.7)

Positivity and the total bank mass give

`||B_t||_1 <= m`,                                             (3.8)

while (3.1) gives

`||B_t||_infinity <= A|t|^{-1/2}`.                            (3.9)

Therefore

`||B_t||_2 <= (mA)^(1/2)|t|^{-1/4}`.                          (3.10)

The exact characteristic-function identity is

`hat(mu_T)(t)=int G_t(l)B_t(l) dl`.                            (3.11)

Cauchy-Schwarz with (3.7)-(3.10) gives the nontrivial part of (3.3), and the trivial bound is the total mass `m`.

Set

`K=sqrt(pi m A)`,

and let `t_0` solve `K t_0^{-3/4}=m`, namely

`t_0=(pi A/m)^(2/3)`.                                         (3.12)

For `q>4/3`, using (3.3) on the positive and negative half-lines,

`int |hat(mu_T)(t)|^q dt
 <= 2[m^q t_0 + K^q int_{t_0}^infinity t^{-3q/4}dt]`

` = [6q/(3q-4)] m^q t_0`

` = [6q/(3q-4)] (pi A)^(2/3)m^(q-2/3).`                       (3.13)

The inverse Fourier operator has Hausdorff-Young norm at most `(2pi)^(-1/q)` from `L^q` to `L^p` with `p=q/(q-1)`. Taking the `q`th root of (3.13) proves (3.4). If `A_j<=A_0m_j`, the mass exponent in (3.4) becomes

`1-2/(3q)+2/(3q)=1`,

which proves (3.6) and the zero-tax mixture statement. QED.

For the convenient choice `q=3/2`, `p=3`, (3.4) is

`boxed:
||p_T||_3 <= (9/pi)^(2/3)(pi A)^(4/9)m^(5/9).`                (3.14)

This recovers the partner `L^2` mass scaling at `q=2` and identifies the entire interpolation scale up to, but not including, the critical `L^4` endpoint.

## 4. One independent square upgrades the mass-homogeneous branch to `L^infinity`

Let `Z` be independent of everything above, with density at most one, and let

`S=a(Z-b)^2`, `a!=0`,                                         (4.1)

where `b` is arbitrary. If `h` is the density of `(Z-b)^2`, then for `y>0`

`h(y)=[f_Z(b+sqrt(y))+f_Z(b-sqrt(y))]/(2sqrt(y)) <= y^{-1/2}`. (4.2)

For `1<=q<2`,

`int h(y)^q dy <= E|Z-b|^{-(q-1)}`.                            (4.3)

For `r=q-1 in [0,1)`, the cap-one interval bound

`P(|Z-b|<u)<=min(1,2u)`

and layer cake give the sharp rearrangement estimate

`E|Z-b|^{-r} <= 2^r/(1-r)=2^(q-1)/(2-q)`.                     (4.4)

After scaling by `a`,

`||p_S||_q <= [2^(q-1)/(2-q)]^(1/q)|a|^(1/q-1).`              (4.5)

Since `p=q/(q-1)` is conjugate to `q`, Young's convolution inequality and (3.4) yield

`boxed:
||p_{T+S}||_infinity
 <= (2pi)^(-1/q)[6q/(3q-4)]^(1/q)
    [2^(q-1)/(2-q)]^(1/q)
    (pi A)^(2/(3q))m^(1-2/(3q))|a|^(1/q-1).`                 (4.6)

Under the mass-homogeneous slice condition `A<=A_0m`, the right side is exactly linear in `m`. Thus arbitrary positive localization of the entire bank transfers the same `L^infinity` constant without any fragment/support/translation/moment tax, provided the square coordinate is kept whole and independent.

At `q=3/2`,

`||p_S||_(3/2) <= 2|a|^(-1/3)`,                               (4.7)

and

`boxed:
||p_{T+S}||_infinity
 <= 2*9^(2/3)*pi^(-2/9) A^(4/9)m^(5/9)|a|^(-1/3).`            (4.8)

The absolute coefficient in (4.8) is

`2*9^(2/3)*pi^(-2/9)=6.709867112379598...`.                   (4.9)

If `A<=A_0m`, (4.8) becomes

`||p_{T+S}||_infinity <= 6.709868 A_0^(4/9)|a|^(-1/3)m`.       (4.10)

This is a genuine target-style localization lemma: arbitrary shifts are allowed through `H` and `b`; the bank may have arbitrary remote/countable fragments and unbounded support; no moment or diameter enters; and conditioning-generated affine terms are retained.

Scope warning: the bare three-large-eigenvalue hypothesis does not itself guarantee a disjoint whole square coordinate or (3.5). This is a supporting branch, not the full theorem.

## 5. Exact-target active-Fresnel fragmentation barrier

The mass-linear condition (3.5) is not automatic when one fragments the coordinate that supplies the Fresnel curvature.

Let

`X,L,W,Z` be independent `Uniform[0,1]`,

and consider the fixed quadratic form

`Q=2XL+W^2+Z^2`.                                               (5.1)

Its symmetric coefficient matrix is

`[[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]`,

with spectrum

`{1,-1,1,1}`.                                                  (5.2)

So (5.1) lies strictly inside the exact owner target.

Partition only the active Fresnel coordinate `W` into the `N` equal intervals

`I_j=[j/N,(j+1)/N]`, `j=0,...,N-1`,                            (5.3)

without changing the probability law. Each submeasure has mass

`m_j=1/N`.                                                     (5.4)

For the `j`th piece, the slice Fourier transform in the `Y=W^2` variable is

`F_j(t)=int_{j/N}^{(j+1)/N} exp(itw^2) dw`.                    (5.5)

Let

`A_j^*=sup_{t>0} sqrt(t)|F_j(t)|`                              (5.6)

be the smallest admissible coefficient in (3.1). Choose

`t_j=N^2/[8(j+1)]`.                                            (5.7)

Across `I_j`, the phase varies by

`t_j[((j+1)^2-j^2)/N^2]=(2j+1)/[8(j+1)]<1/4`.                 (5.8)

After rotating by the phase at the left endpoint, the real part of the integrand is therefore at least `cos(1/4)`, so

`|F_j(t_j)| >= cos(1/4)/N`.                                    (5.9)

Consequently

`boxed:
A_j^* >= c_0 (j+1)^(-1/2),
 c_0=cos(1/4)/sqrt(8)=0.3425622718837383... .`                 (5.10)

In particular, `A_j^*/m_j` is not uniformly bounded under refinement.

Now force the fragment-first route: apply the `q=3/2` chirp-slice `L^3` estimate separately to every `W`-piece, convolve each piece with the whole independent square `Z^2` via (4.8), and only then sum the positive output subdensities. Even if each slice coefficient is chosen optimally as `A_j^*`, the resulting black-box certificate is at least

`C_0 N^(-5/9) sum_{j=0}^{N-1}(A_j^*)^(4/9)`,                  (5.11)

where

`C_0=2*9^(2/3)*pi^(-2/9)=6.709867112379598...`.

Using (5.10),

`certificate_N
 >= C_0 c_0^(4/9)N^(-5/9) sum_{k=1}^N k^(-2/9)`

` >= C_0 c_0^(4/9)(9/7)N^(-5/9)[(N+1)^(7/9)-1]`.              (5.12)

Hence

`boxed:
certificate_N >= (5.3589037585...+o(1)) N^(2/9).`             (5.13)

The certificate diverges although the probability law in (5.1) is literally unchanged by the bookkeeping partition.

This is `QFORM-ACTIVE-FRESNEL-FRAGMENT-LP-BARRIER-v1`: it refutes only the proof ordering “partition a curvature-active coordinate, apply the chirp-slice magnitude certificate piecewise, then sum.” It does **not** refute the chirp-slice theorem or QFORM.

## 6. Required Claude result applied to the same obstruction

I read the required pinned Claude directory at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed `COUNTEREXAMPLE_SEARCH.md` Theorem A states that when every eigenvalue of an `n`-dimensional symmetric form has modulus at least `sigma`, linear terms allowed,

`||p_Q||_infinity <= (n/sigma)(d/(d-1)) kappa_d^(1/d), d=n-1`. (6.1)

For the **same fixed exact-target form** (5.1), `n=4`, `sigma=1`, `d=3`, so Theorem A gives

`boxed:
||p_Q||_infinity <= 6 kappa_3^(1/3),`                          (6.2)

independently of `N`. Thus a completed source theorem uniformly controls the true law while the forced fragment-first chirp-slice/square certificate grows like `N^(2/9)`. This is a real inequality/obstruction comparison, not a numerical heuristic.

The same pinned Claude sources also confirm the broader proof map used here: D' tolerates row-volume marginal below `3/4`, D5 gives a fifth-volume bound with no marginal gate, and Theorem H/Fresnel mechanisms aggregate active curvature before absolute-value localization. None licenses normalizing a curvature-active fragment first.

## 7. Localization rule and remaining gap

The safe localization order is now sharper:

`whole active chirp/Fresnel aggregation -> retain unnormalised mass -> Lp or reciprocal receiver -> outside/phase-only localization`.

Arbitrary positive bank localization is zero-tax whenever its unnormalised slice Fourier coefficient retains a full bank-mass factor. Fragmenting the coordinate that creates the stationary/Fresnel scale can destroy that factor even for compact unit intervals and a fixed four-dimensional exact-target law.

The next unpaid implication is `QFORM-MASS-HOMOGENEOUS-SLICE-OR-WHOLE-ACTIVE-EXIT-v1`: in every surviving no-pivot/N3 configuration, before active refinement, force either

1. an unnormalised slice estimate `A_j<=A_0m_j` for the chosen localization,
2. a whole-law D'/D5/ridge/mixed-hub/Fresnel/bank certificate, or
3. a phase-sensitive aggregate estimate that preserves cancellation across the active pieces.

A fixed fragment count, bounded diameter, hidden moments, post-rotation independence, or treating a small quadratic coefficient as a small random perturbation cannot replace this step.

## 8. Status

The unrestricted QFORM conjecture remains OPEN. The result above is a quantitative supporting localization theorem plus an exact-target obstruction to a specific localization order. Continuity remains separate. No support, moment, centering, log-concavity, identical-law, diagonal-basis, or post-rotation independence assumption was introduced.
