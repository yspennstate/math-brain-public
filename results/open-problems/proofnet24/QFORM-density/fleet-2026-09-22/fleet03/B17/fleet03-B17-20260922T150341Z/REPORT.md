# fleet03/B17 — first-order rigidity of the diffuse sharp witness

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `fleet03-B17-20260922T150341Z`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `NEW SUPPORTING THEOREM / EXACT ROTATED STRESS / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, sources, and correction state

The full target remains OPEN: for every dimension, every independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one dimension- and law-independent essential-density bound for `X^T A X`, or produce a valid counterexample. Continuity of the full target density is a separate desired conclusion and is not proved here.

Fresh control before publication: `yspennstate/math-research-brain` main commit `e2b4e19cfbe7aacd855df717036ffe0ab2a3d9b2`, owner revision `2026-09-22.5`. No later pause/stop for this worker was observed.

This derivation uses the live corrections, in particular: law-uniform pointwise quadratic-phase decay is false; rotation does not preserve coordinate independence; a single physical minor is not a universal closure; conditional density caps cannot replace product provenance; and the newest `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` correction shows that selecting one physical triple before paying reciprocal aggregate cost can diverge even on a target-admissible rank-three family.

The exact assigned partner `fleet04/B17` still had no completed QFORM handoff or canonical report visible at the final partner check. I therefore do not invent a partner result. I apply the compatible completed `fleet04/B18` Schur-pivot theorem, canonical report commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, to an explicit new rotated stress family in Section 7.

Two earlier completed sharp inputs are also used only in their stated scope:

- `fleet02/B17`, commit `cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`, proves the sharp centered-Gaussian three-mode envelope `||p||_infinity <= 1/(2 sqrt(2) s)` and the density-one variance floor `1/12`.
- this worker's preceding run, commit `3d0926c161ba4cbea4016bff63d89e34f87cb0e6`, proves the same envelope for arbitrary Gaussian mean shifts and supplies a fully mixed Walsh stress family.

The new mechanism here is neither another Gaussian calculation nor another finite minor enumeration. It computes the **first non-Gaussian correction** to the sharp diffuse witness for arbitrary fixed tight-frame rotations of independent density-one uniforms.

## 2. Fixed-frame repeated-uniform target family

Fix vectors `v_1,...,v_K in R^3` spanning `R^3` and satisfying the Parseval/tight-frame identity

`sum_(j=1)^K v_j v_j^T = I_3`.

For an integer `m>=1`, form the `(Km) x 3` matrix `R_m` by repeating the row `v_j/sqrt(m)` exactly `m` times for each `j`. Then

`R_m^T R_m = I_3`.

Let

`J = diag(1,1,-1),   A_m = R_m J R_m^T`.

Thus, for every `m`,

`spec(A_m) = {1,1,-1,0^(Km-3)}`,

so this is an exact target-admissible rotated family, not an approximate spectral construction.

Let the `Km` physical inputs be iid `Uniform[-1/2,1/2]`, each of density exactly one. Put

`Y_m = sqrt(12) R_m^T X`.

Then

`Q_m = X^T A_m X = (1/12) Y_m^T J Y_m`.

The central-limit limit is `G~N(0,I_3)`, whose indefinite quadratic density has

`p_((1/12) G^T J G)(0) = 3 sqrt(2)`.

The question attacked here is whether a genuinely rotated, finite, non-Gaussian density-one frame can approach this sharp stress from the dangerous side at first order.

## 3. Exact characteristic expansion

Let `xi` be uniform on `[-sqrt(3),sqrt(3)]`; its characteristic function is

`E exp(i s xi) = sinc(sqrt(3) s)`.

Therefore

`Phi_m(t) := E exp(i <t,Y_m>)
 = product_(j=1)^K sinc( sqrt(3) <v_j,t>/sqrt(m) )^m.`

For fixed `a`,

`m log sinc(sqrt(3) a/sqrt(m))
 = -a^2/2 - a^4/(20m) - a^6/(105m^2) + O_a(m^-3)`.

Using the tight-frame identity,

`sum_j <v_j,t>^2 = |t|^2`,

hence

`Phi_m(t)
 = exp(-|t|^2/2)
   [1 - (1/(20m)) sum_j <v_j,t>^4 + O(m^-2 P_8(t))]`

locally uniformly, with a fixed polynomial `P_8` depending only on the fixed frame.

For completeness, this expansion can be promoted to a weighted density expansion rather than merely a formal characteristic expansion. On `|t|<=m^(1/12)`, the displayed logarithmic Taylor remainder is bounded by a Gaussian times `O(m^-2(1+|t|^8))`. On the intermediate region `m^(1/12)<|t|<=c sqrt(m)`, the elementary inequality `|sinc x|<=exp(-c_0 x^2)` near zero together with `sum_j <v_j,t>^2=|t|^2` gives uniform Gaussian domination. Beyond `c sqrt(m)`, choose three linearly independent frame vectors and use `|sinc x|<=min(1,1/|x|)` after the corresponding invertible linear change of variables; because each selected factor is raised to the `m`th power, all fixed-order derivative tails are `o(m^-1)`. Fourier inversion and integration by parts therefore give, for any fixed sufficiently large `N`,

`sup_z (1+|z|)^N |
 f_m(z) - phi_3(z)
 + (1/(20m)) sum_j (v_j . grad)^4 phi_3(z)
 | = o(m^-1)`,

where `f_m` is the density of `Y_m` and `phi_3` the standard three-dimensional Gaussian density. The sign is important:

`f_m = phi_3 - (1/(20m)) sum_j (v_j . grad)^4 phi_3 + o(m^-1)`.

This weighted form is enough to integrate over the quadratic cone below.

## 4. Exact cone-Hermite factor

Write

`q(z)=z_1^2+z_2^2-z_3^2`.

The density of `q(Y_m)` at zero is

`p_(q(Y_m))(0)=int delta(q(z)) f_m(z) dz`.

Parameterize the two sheets of the zero cone by

`z=(r cos(theta), r sin(theta), epsilon r)`,
`r>=0`, `theta in [0,2pi)`, `epsilon in {+1,-1}`.

The delta Jacobian reduces the Gaussian cone measure to: `theta` uniform, `epsilon` uniform, and `r` with density proportional to `exp(-r^2)`. Under this normalized cone law,

`E r^2=1/2,   E r^4=3/4`.

For a nonzero frame vector `v`, let `u=v/|v|` and

`alpha = u_3^2 in [0,1]`.

Since

`(v . grad)^4 phi_3(z)
 = |v|^4 H_4(u.z) phi_3(z),`

with `H_4(s)=s^4-6s^2+3`, the relative cone contribution of this derivative is

`|v|^4 F(alpha)`,

where an elementary `theta,epsilon,r` calculation gives the exact polynomial

`F(alpha)
 = 3(19+2 alpha-13 alpha^2)/32
 = (57-33 alpha)/32 + (39/32) alpha(1-alpha).`

In particular,

`F(0)=57/32,   F(1)=3/4,`

and, because `F` is concave, its minimum on `[0,1]` is

`min F = 3/4 >0`.

The Gaussian reference cone integral is

`p_(q(G))(0)=1/(2 sqrt(2))`.

Consequently, defining

`S(v_1,...,v_K)
 := sum_j |v_j|^4 F( v_(j,3)^2/|v_j|^2 ),`

we obtain the main expansion.

## 5. Theorem: every fixed-frame uniform diffuse witness approaches the Gaussian zero stress from below

### Theorem 5.1

For every fixed spanning tight frame `v_1,...,v_K` as above,

`p_(Q_m)(0)
 = 3 sqrt(2) [1 - S(v_1,...,v_K)/(20m) + o(m^-1)]`,

with

`S(v_1,...,v_K) > 0`.

Therefore, for every such fixed frame, the zero-level density of the finite non-Gaussian density-one witness is strictly **below** `3 sqrt(2)` for all sufficiently large `m`.

### Proof

Insert the weighted density expansion of Section 3 into the cone integral. The Gaussian term gives `1/(2sqrt(2))`; the fourth-derivative terms give the normalized factors in Section 4. The weighted `o(m^-1)` remainder is integrable against the cone measure, because the latter grows only polynomially in `r`. Finally rescale from `q(Y_m)` to `Q_m=q(Y_m)/12`, multiplying the density at zero by `12`. Positivity follows from `F>=3/4` and from at least one nonzero frame vector. QED.

### Interpretation

This does **not** prove that `||p_(Q_m)||_infinity<=3sqrt(2)` for every finite `m`; a finite member could in principle have a larger maximum away from zero. What it proves is sharper than a CLT statement and narrower than a universal norm bound: the canonical zero-level sharp Gaussian stress cannot be exceeded at first non-Gaussian order by any fixed-frame repeated-uniform rotation.

Thus a lower-bound witness above `3sqrt(2)` cannot be obtained merely by taking a fixed finite rotation pattern, repeating it diffusely with density-one uniforms, and hoping the first Edgeworth correction raises the saddle peak.

## 6. Equal-leverage rigidity: sign-mixing has an exact positive first-order penalty

Assume now that the frame is equal leverage:

`|v_j|^2 = 3/K` for every `j`.

Put

`alpha_j = v_(j,3)^2/|v_j|^2`.

The tight-frame identity gives

`(1/K) sum_j alpha_j = 1/3`.

Using the second representation of `F`,

`(1/K) sum_j F(alpha_j)
 = 23/16 + (39/32) (1/K) sum_j alpha_j(1-alpha_j)`.

Since `n=Km`, Theorem 5.1 becomes the exact first-order law

`boxed(
 p_(Q_m)(0)
 = 3 sqrt(2) { 1 - (1/n)[
       207/320
       + (351/640) mean_j(alpha_j(1-alpha_j))
     ] + o(n^-1) }.
)`

Every summand `alpha_j(1-alpha_j)` is nonnegative. Therefore the smallest possible first-order deficit is

`207/(320 n)`,

and equality holds iff every `alpha_j` is `0` or `1`. Equivalently, every physical frame direction lies either entirely in the positive eigenspace of `J` or entirely on the negative eigenaxis. Any row that genuinely mixes the positive and negative spectral subspaces incurs a strictly larger negative first-order correction.

This gives a precise **rotation-penalty rigidity theorem** for this sharp-witness class: among equal-leverage fixed-frame density-one uniform stresses, sign-separated/block geometry is first-order extremal at the dangerous level zero. Rotation across the signature split makes the first correction safer, not worse.

Exact controls:

- three coordinate axes (`K=3`): `S=69/16`, relative deficit `69/(320m)=207/(320n)`;
- symmetric tetrahedral orientation with every `alpha_j=1/3`: `S=123/32`, deficit `123/(640m)=123/(160n)`;
- tetrahedron with one vertex on the negative eigenaxis and the other three having `alpha=1/9`: `S=55/16`, deficit `11/(64m)=11/(16n)`.

All rational identities are checked by the committed `CHECK.py`; no histogram or Monte Carlo evidence is used.

## 7. Applying the completed fleet04 Schur-pivot theorem to the same rotated family

Take the regular tetrahedral unit vectors in an orientation with

`u_1=(0,0,1)`

and the other three vertices having third coordinate `-1/3`; scale

`v_j=(sqrt(3)/2) u_j`.

Then `sum_j v_j v_j^T=I_3`, each `|v_j|^2=3/4`, and this is exactly the axial tetrahedral case above.

Choose one physical coordinate from each of row types `1,2,3`. The corresponding physical principal block is

`B_m = (1/m) V J V^T`.

The Euclidean Gram matrix of those three scaled tetrahedral rows has diagonal `3/4`, off-diagonal `-1/4`, and determinant exactly `1/4`. Hence

`det(B_m) = -1/(4m^3)`.

Because type `1` is the negative eigenaxis,

`a=(B_m)_(11)=-3/(4m)`.

The full block has inertia `(2,1)`, so this negative scalar pivot is the minority-sign pivot and its Schur complement is positive definite. The completed `fleet04/B18` theorem therefore applies and gives the actual target-level inequality

`||p_(X^T A_m X)||_infinity
 <= 2 sqrt(pi) / |a det(B_m)|^(1/4)
 = (4 sqrt(pi)/3^(1/4)) m
 = 5.3870947483... m.`

This is a correct all-law bound for this family, but it grows linearly in `m`, whereas the explicit density-one uniform witness has

`p_(Q_m)(0) -> 3sqrt(2)`.

So the partner mechanism is quantitatively nonsharp on this diffuse rotated stress. This is a concrete application, not a criticism of its stated scope: it proves that **selecting one eligible physical triple and then paying the determinant-sensitive Schur cost cannot by itself capture the sharp diffuse regime**. The proof architecture must aggregate frame/minor currency before reciprocal payment, matching the current correction state.

## 8. Optional perturbative extension: rare fragmented defects do not raise the first-order Gaussian saddle

The current target permits disconnected and far-separated supports, so it is important not to mistake the uniform-interval calculation for an extremality theorem. There is nevertheless one source-valid fragmented-support extension.

For each row type `j`, alter each unit interval density by moving a mass `tau_j/m^2` from a tiny symmetric neighborhood of zero to two tiny symmetric intervals centered at distance

`L_(j,m)= beta_j sqrt(m)/(sqrt(12)|v_j|)`.

The resulting density is still an indicator of a measurable set of total length one, hence is an admissible probability density bounded by one. Across the `m` copies of row type `j`, the tail event has total first-order intensity `tau_j/m`.

The characteristic expansion gains

`(tau_j/m)[cos(beta_j <u_j,t>)-1]`,

so the corresponding first-order correction to the zero-level quadratic density is

`(tau_j/m) [ g_(beta_j u_j)(0)-g_0(0) ]`,

where `g_h` denotes the density at zero of `(G+h)^T J(G+h)` and `g_0(0)=1/(2sqrt(2))`.

The preceding B17 noncentral-Gaussian theorem, sourced at commit `3d0926c161ba4cbea4016bff63d89e34f87cb0e6`, gives

`g_h(0) <= ||g_h||_infinity <= g_0(0)`

for every `h`. Hence every such `sqrt(m)`-scale sparse fragmented defect has a **nonpositive** first-order contribution to the dangerous Gaussian saddle. It cannot cancel the negative Edgeworth correction found above.

This perturbative statement does not rule out nonperturbative fragmentation, mesoscopic masses of a different scale, or maxima away from zero. It does show that one natural attempt to exploit the absence of support/moment hypotheses fails analytically rather than numerically.

## 9. What this changes for the sharp-constant search

The full QFORM conjecture remains **OPEN / NOT PROVED**, and continuity for the unrestricted target remains **OPEN**.

The sharp lower bound `C>=3sqrt(2)` remains the best proved lower bound in the source state. The new information is structural:

1. every fixed finite tight-frame repetition of density-one uniforms approaches the sharp Gaussian zero stress from below at order `1/m`;
2. in the equal-leverage class, cross-sign rotation incurs the explicit additional penalty `(351/640n) mean alpha(1-alpha)`;
3. sparse `sqrt(m)`-scale fragmented defects of total intensity `O(1/m)` cannot raise that zero stress at first order;
4. the compatible fleet04/B18 one-triple Schur bound applied to an exact tetrahedral rotated stress grows as `5.387... m`, demonstrating quantitatively why aggregate-before-inversion is necessary in the diffuse branch.

A genuine lower-bound witness above `3sqrt(2)` must therefore use a mechanism not covered here: for example a nonperturbative fragmented/mesoscopic array, a moving frame whose number of direction types grows with dimension in a way not captured by a fixed-frame Edgeworth expansion, or a mixed-leverage construction whose density maximum is created away from the Gaussian saddle.

The next B17 attack should target one of those three mechanisms rather than repeat a fixed-frame diffuse CLT perturbation.

## 10. Verification and provenance

`CHECK.py` and `CHECK_OUTPUT.txt` in this immutable run directory verify exactly, using rational arithmetic:

- the cone-Hermite polynomial values and its chord-plus-mixing decomposition;
- all three first-order stress coefficients above;
- the equal-leverage coefficient formula;
- the tetrahedral Gram determinant `1/4`;
- the principal determinant `-1/4`, minority pivot `-3/4`, and the resulting fleet04/B18 prefactor.

No numerical histogram is used as mathematical evidence. The only floating output in the checker is presentation of the exact Schur prefactor and `3sqrt(2)`.

Repository transport here is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`; no scheduler, notification, email, Drive, public-release, paid-model/API, Codex, workflow, permission, or cross-account mutation was performed.
