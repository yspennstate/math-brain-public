SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T17:32:17Z.
attacking: whole-active receiver-core coupling — derive a translation-uniform, mass-homogeneous localization/mixture principle for the newest partner quadratic-receiver theorem, and isolate the exact loss caused by normalizing every active score fragment first.

# fleet02/B14 r41 — pre-Jensen receiver localization and active-score fragmentation barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** translations and localization / complementary constructions and source-valid counterexamples  
**Status:** NEW SUPPORTING LOCALIZATION THEOREMS + EXACT-TARGET PROOF-ORDER OBSTRUCTION. **Full unrestricted QFORM remains OPEN.**  
**Continuity:** separate; only essential boundedness is asserted below.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and fresh brain controls were consumed. The current Claude continuation at `c4c23b784395630c094ba299a50712209921d1ae` was read; its proposed `(SP)` adapted-hub estimate is explicitly OPEN and is not used here.

## 1. Exact sources actually used

Newest designated partner fleet03/B14:

`yspennstate/math-open-problems@e786ed60fea4db8a672faaffc35531bb06eb9b57`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T164047Z-fleet03-B14-QFORM-auto11/REPORT.md`.

Its proved `QFORM-HYBRID-QUADRATIC-RECEIVER-LP-v1` says: for `4/3<r<2`, `p=r/(r-1)`, independent cap-one original coordinates `Z=(Z_i)` and `W`, a conditional core `T_z` independent of `W` with

    ||p_{T_z}||_p <= K_r

uniformly, and

    Q=T_Z+s(Z)+dW^2+(2c^T Z+e)W,
    R_0=sqrt(d^2+||c||_2^2)>0,

one has

    ||p_Q||_infinity
      <= K_r 2^{3(r-1)/(2r)}(2-r)^{-1/r}
             R_0^{-(r-1)/r}.                                    (1.1)

All shifts and supports are arbitrary.

The required Claude source was freshly read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In Section 6 below I apply its completed Theorem B to the same exact-target family used for the fragmentation obstruction.

## 2. New theorem: keep the score whole and localize the core before Jensen

### Theorem 2.1 — `QFORM-PREJENSEN-RECEIVER-MIXTURE-v1`

Keep the partner setup but allow the conditional core budget to depend measurably on the driver:

    K(z)=||p_{T_z}||_p,

with no uniform bound assumed. Put

    alpha=r-1,
    S=2dW+2c^T Z+e.

If

    E K(Z)^p < infinity,                                          (2.1)

then

    boxed:
    ||p_Q||_infinity
      <= 2^{3 alpha/(2r)}(2-r)^{-1/r}
         R_0^{-alpha/r}
         [E K(Z)^p]^{1/p}.                                       (2.2)

Thus a positive localization of the driver into cells `C_j` of masses `m_j`, on which one only knows

    K(z)<=K_j,

costs at most

    boxed:
    [sum_j m_j K_j^p]^{1/p},                                     (2.3)

not `sup_j K_j`, not `sum_j K_j`, and no fragment-count or diameter parameter. The linear-score law is aggregated over the **whole** driver distribution before its reciprocal singularity is paid.

### Proof

For fixed `z` write

    F_z(w)=d w^2+(2c^Tz+e)w,
    A(z)=E_W |2dW+2c^Tz+e|^{-alpha}.

The partner's one-dimensional area calculation is pointwise in `z` and gives

    ||p_{F_z(W)}||_r
      <=2^{alpha/r} A(z)^{1/r}.                                  (2.4)

The core and receiver use disjoint original-coordinate source banks, so Young at the conjugate exponents `(p,r)` gives

    ||p_{Q|Z=z}||_infinity
      <= K(z) 2^{alpha/r} A(z)^{1/r}.                            (2.5)

Average in `z`, then use Holder in the **driver variable** with exponents `p` and `r`:

    ||p_Q||_infinity
      <=2^{alpha/r}[E K(Z)^p]^{1/p}
         [E A(Z)]^{1/r}.                                         (2.6)

No cellwise Jensen or normalization has occurred. The remaining expectation is exactly

    E A(Z)=E|S|^{-alpha}.                                        (2.7)

The partner's source-valid Rogozin--Ball projection cap gives

    ||p_S||_infinity<=1/(sqrt(2)R_0).                            (2.8)

For any probability density bounded by `M`, symmetric decreasing rearrangement gives, for `0<alpha<1`,

    sup_a int |x-a|^{-alpha}p(x)dx
      <=2^alpha M^alpha/(1-alpha).                               (2.9)

Hence

    E|S|^{-alpha}
      <=2^{alpha/2}(2-r)^{-1}R_0^{-alpha}.                       (2.10)

Substitution in (2.6) proves (2.2). For a cellwise bound `K(z)<=K_j`, (2.3) is immediate. No moments, support bounds, connectedness, centering or post-rotation independence occur. QED.

### Interpretation

This is a genuine localization/mixture rule for the full rough-law setting: one may localize whatever is needed to certify the core, but the active random score `S` must remain aggregated until after the Holder/Jensen step. Distant fragments and conditioning-generated affine shifts are harmless because they change only `e`, `s(z)`, and the measurable location of the core; (2.2) is uniform in all of them.

## 3. Exact subprobability homogeneity of the cellwise receiver certificate

The preceding theorem explains the safe order. The complementary calculation below quantifies exactly what happens if one insists on paying the score separately on each cell.

### Theorem 3.1 — `QFORM-RECEIVER-SCORE-SUBPROBABILITY-HOMOGENEITY-v1`

Let `nu` be a positive finite measure on driver values `z`, of total mass `m<=1`. Keep the receiver `W` whole and cap one. Assume

    ||p_{T_z}||_p<=K_r                                           (3.1)

for `nu`-a.e. `z`. Let `sigma` be the pushforward of `nu(dz) P_W(dw)` under

    S(z,w)=2d w+2c^Tz+e,                                         (3.2)

and suppose `sigma` has a density bounded by `L`. Let `eta` be the corresponding unnormalised output measure of

    T_z+s(z)+dW^2+(2c^Tz+e)W.                                   (3.3)

Then

    boxed:
    ||p_eta||_infinity
      <= K_r 2^{2 alpha/r}(2-r)^{-1/r}
             m^{1/r}L^{alpha/r}.                                (3.4)

### Proof

The area estimate (2.4) remains valid. Jensen for the finite measure `nu` gives

    int A(z)^{1/r} nu(dz)
      <=m^{1-1/r}
        [int |s|^{-alpha} sigma(ds)]^{1/r}.                      (3.5)

For a finite measure of mass `m` and density cap `L`, rearrangement gives the exact cap-only estimate

    int |s-a|^{-alpha} sigma(ds)
      <=[2^alpha/(1-alpha)]L^alpha m^{1-alpha}.                  (3.6)

Indeed the extremal cap profile is `L` on the centred interval of length `m/L`; no bounded support or attainment on an infinite-line bathtub problem is assumed. Combining (2.4), (3.5), (3.6), and `1-alpha=2-r` gives (3.4). QED.

The decisive homogeneity is therefore

    boxed: m^{1/r} L^{(r-1)/r}.                                  (3.7)

Consequently, for a positive decomposition into cells of masses `m_j` and score caps `L_j`, the cellwise certificate sums as

    K_r 2^{2 alpha/r}(2-r)^{-1/r}
    sum_j m_j^{1/r}L_j^{alpha/r}.                                (3.8)

If

    L_j<=H m_j                                                     (3.9)

for every cell, then the mass exponent restores exactly:

    m_j^{1/r}L_j^{alpha/r}<=H^{alpha/r}m_j,

so arbitrary countable mixing is zero-loss.

## 4. Whole-anchor localization: a zero-tax active fragmentation principle

Condition (3.9) has a simple original-coordinate mechanism.

### Corollary 4.1 — `QFORM-WHOLE-SCORE-ANCHOR-LOCALIZATION-v1`

If `d!=0` and the receiver `W` is kept whole, then **the entire driver law may be decomposed into arbitrary positive pieces**, with no product, diameter, location, separation or fragment-count restriction on the pieces. For a piece of mass `m_j`, conditioning on `z` shows that the score contains the scaled whole cap-one variable `2dW`; therefore

    L_j<=m_j/(2|d|).                                              (4.1)

Summing (3.4) gives

    boxed:
    ||p_Q||_infinity
      <=K_r 2^{alpha/r}(2-r)^{-1/r}|d|^{-alpha/r}.               (4.2)

Likewise, if a driver coordinate `Z_k` with `c_k!=0` is kept whole while the other driver variables are decomposed arbitrarily, then

    L_j<=m_j/(2|c_k|)                                             (4.3)

and (4.2) holds with `|c_k|` in place of `|d|`.

Translations of `W`, `Z_k`, or any fragmented variable only alter the score shift and hence cost zero. The result allows fragmented and unbounded supports and has no moment hypothesis.

### Application to the newest partner's exact-target family

Partner fleet03/B14 constructs

    Q_m=2X_0 V +(1/2)Y^2 + W^2+2(a_m^T Z)W,
    a_m=m^{-1/2}(1,...,1),                                       (4.4)

whose homogeneous matrix has target-scale eigenvalues

    1, -1, (1+sqrt(5))/2,                                       (4.5)

so it is a genuine full-target family. Its affine-uniform slice core and `r=12/7` calculation give the core `L^{12/5}` budget used in the partner report. Here

    d=1,  ||a_m||_2=1.                                           (4.6)

Now decompose the **entire Z-bank law** into any finite or countable positive pieces, however remote or irregular, and leave `W` whole. Equation (4.1) holds with `|d|=1`, so every cell pays linearly in its unnormalised mass. Summing reproduces exactly the partner's whole-law constant

    boxed:
    ||p_{Q_m}||_infinity
      <=2^{29/36}(63/2)^{7/12}
      =13.0770828465...                                          (4.7)

for every `m`, with no localization tax. In this family the whole-anchor cap `1/2` equals the partner's global Rogozin--Ball score cap because `sqrt(d^2+||a_m||^2)=sqrt2`; hence the numerical constant is literally unchanged.

This is a real localization statement, not merely the observation that a probability-level theorem happens not to mention supports.

## 5. Exact-target obstruction: normalising every active score fragment destroys the certificate

### Construction

Let `U_1,U_2,W` be independent cap-one variables, and for every `N>=1` let

    E_N=union_{j=1}^N [4^j,4^j+1/N],
    f_{Z_N}=1_{E_N}.                                              (5.1)

Thus `Z_N` is a legal probability law with cap one, total support length one, arbitrary fragment separation and unbounded location as `N` grows. Consider

    Q_N=U_1^2+U_2^2+2Z_NW.                                      (5.2)

Its quadratic matrix is

    diag(1,1) direct_sum [[0,1],[1,0]],                           (5.3)

with spectrum

    {1,1,1,-1}.                                                   (5.4)

Hence every `Q_N` lies squarely inside the exact target.

Take `r=12/7`, so

    p=12/5,  alpha=5/7,
    alpha/r=5/12,  1/r=7/12.                                    (5.5)

The two-square core has the standard cap

    ||p_{U_1^2+U_2^2}||_infinity<=pi,

therefore by interpolation with total mass one

    K_r:=||p_{U_1^2+U_2^2}||_{12/5}<=pi^{7/12}.                  (5.6)

### Whole-law payment is uniform

The score is simply

    S=2Z_N.                                                       (5.7)

Its density is bounded by `1/2`, independently of `N` and of every gap in `E_N`. Applying Theorem 3.1 once at mass one gives

    boxed:
    ||p_{Q_N}||_infinity
      <=pi^{7/12} 2^{5/12}(7/2)^{7/12}
      =5.4051317350...                                           (5.8)

for all `N`.

### Cellwise unnormalised cap payment already loses `N^{5/12}`

Let `nu_j=1_{[4^j,4^j+1/N]} dz`. Each cell has

    m_j=1/N,                                                      (5.9)

while the unnormalised score pushforward `2Z` has the **exact** density cap

    L_j=1/2,                                                      (5.10)

not `O(m_j)`. Therefore (3.8), even with the best exact cap data `(m_j,L_j)`, gives

    boxed:
    5.4051317350... N^{5/12}.                                   (5.11)

The full law is controlled by (5.8); the divergence in (5.11) is solely the consequence of paying a concave reciprocal certificate separately on each active score fragment.

### Normalise-and-rescale first: the newest partner theorem has the same structural loss

On the `j`th fragment, after normalisation write

    Z_N=4^j+Y/N,    Y~Uniform[0,1].                              (5.12)

Then

    2Z_NW=(2/N)YW+2(4^j)W.                                      (5.13)

The second term is exactly the arbitrary receiver-linear coefficient `eW`, which the partner theorem treats uniformly. But the cap-one active driver coefficient has shrunk from `c=1` to

    c_j=1/N.                                                      (5.14)

Applying the partner probability theorem (1.1) on every normalised cell therefore gives

    boxed:
    pi^{7/12}2^{5/8}(7/2)^{7/12} N^{5/12}
      =6.2448335270... N^{5/12}.                                (5.15)

Averaging the `N` equally weighted normalised conditional laws does not remove this factor. The translation `4^j` can be exponentially large and has no effect on the calculation.

This is `QFORM-ACTIVE-SCORE-FRAGMENT-NORMALIZATION-BARRIER-v1`. It refutes only the proof ordering

    active fragment -> normalise/rescale -> reciprocal score payment -> mix,

not QFORM and not the partner theorem.

A same-law bookkeeping variant takes `Z~Uniform[0,1]` and partitions `[0,1]` into `N` equal cells: the probability law of `Q` is then literally independent of `N`, while the same normalise-first certificate grows as `N^{5/12}`.

## 6. Required Claude result applied to the same obstruction

The completed Theorem B in

`e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

states, for a symmetric `A` with three eigenvalues of modulus at least one,

    ||p_Q||_infinity
      <=2 sqrt(2pi) sum_i |P e_i|,                               (6.1)

where `P` projects onto `range(A)`.

For the **same** matrix (5.3), `A` is invertible, so `P=I_4` and

    sum_i |Pe_i|=4.                                               (6.2)

Therefore Claude's theorem gives the independent source-valid inequality

    boxed:
    ||p_{Q_N}||_infinity
      <=8 sqrt(2pi)
      =20.0530261970...                                          (6.3)

uniformly in `N`, in every fragment location and gap, and indeed for arbitrary cap-one laws on all four coordinates. Equations (5.11) and (5.15) can therefore diverge while a completed theorem controls the true exact-target density by a fixed number. This proves that the divergence is a localization-interface artifact, not evidence for a counterexample.

For reference, the same e5f source also proves D' and the unrestricted fifth-volume estimate

    ||p_Q||_infinity<=5 sqrt(2e) e_5(M^TM)^{-1/10}

for any disjoint crossing block with positive fifth volume; those remain whole-law exits and should likewise be paid before active score fragmentation.

## 7. What this changes in the localization proof map

The safe hierarchy is now quantitative.

1. **Best:** keep the active score whole and localize only the core. Theorem 2.1 permits variable cellwise core budgets and combines them by the probability-weighted `L^p` norm `(sum m_j K_j^p)^{1/p}` while the score's fractional singularity is paid once globally.
2. **Still zero-loss:** if one insists on cellwise score payment, preserve one whole score anchor. Then its cap scales as `L_j=O(m_j)` and Theorem 3.1 restores a full power of the cell mass.
3. **Unsafe:** fragment every active score carrier and normalise before reciprocal payment. The exact target family (5.2) forces the black-box partner certificate to grow like `N^{5/12}` despite arbitrary translation-uniformity and despite a fixed whole-law density bound.

No fixed fragment count, bounded diameter, moment bound, log-concavity, centred support or post-rotation independence is used anywhere.

## 8. First unpaid implication

`QFORM-PREJENSEN-OVERLAPPING-CORE-OR-WHOLE-VOLUME-EXIT-v1`:

In each surviving no-pivot/N3 configuration, before active-law normalisation, force one of the following:

- a whole-law D'/D5/projected-crossing/ridge/mixed-hub/grouped-bank exit;
- a receiver representation to which Theorem 2.1 applies with a finite probability-weighted `L^p` core budget while the linear score is still the whole original-coordinate product projection;
- a whole score anchor satisfying the mass-homogeneous cap `L_j<=H m_j` through every localization step;
- or a new aggregate estimate for the genuinely overlapping case in which the receiver's score depends on the same original coordinates that supply the core smoothing, so fixed-`z` convolution independence is unavailable.

The last overlapping case is the actual new analytic debt. Replacing it by a worst conditional density, fragmentwise normalisation, bounded-diameter localization, or a small random perturbation argument would reintroduce already-refuted interfaces.

## 9. Source and arithmetic checks

At `r=12/7`, the exponents are exact:

    p=12/5,
    alpha/r=5/12,
    1/r=7/12.                                                     (9.1)

For the partner target family (4.4), the anchor cap is `1/2`, equal to the global projection cap `1/(sqrt2*sqrt2)`, so (4.7) exactly matches the partner's checked constant `13.0770828465...`.

For (5.2), the whole score cap `1/2` gives `5.4051317350...`; the normalised-cell partner coefficient is `6.2448335270... N^{5/12}`. These are certificate values, not numerical density estimates.

No use is made of the current Claude `(SP)` proposal or of the corrected unsupported arbitrary-rough-hub Borel-profile inference. The full unrestricted conjecture remains OPEN.
