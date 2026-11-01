SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T22:31:09Z.
attacking: aggregate-before-localize necessity — quantify a target-valid star-plus-rank-one-bank family where the new marginal-free Z3 and square-plus-Schur-Z2 receivers both vanish, while every physical 2+2 Plancherel certificate deteriorates but the grouped mixed-hub Fresnel estimate stays dimension-free.

# fleet02/B03 — local-certificate collapse versus grouped time integrability

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SHARPENED OBSTRUCTION / PINNED THEOREM APPLIED / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This run does not produce a counterexample to QFORM. It proves that three natural local structural receivers cannot replace grouped aggregation, even on a family for which a completed grouped theorem gives a uniform density bound and a uniform assigned half-Riesz time integral.

## 1. Sources and scope

The current owner programme is still `QFORM-DENSITY-3EIG-20260922`. The required pinned package is

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. I use its completed Theorem H at an actual matrix below. I also retain its corrections: no arbitrary-joint coarea cap, no law-uniform pointwise quadratic phase decay, and no independence after rotating the product law.

The newest compatible designated partner input read for this run is fleet03/B03 r41,

`math-open-problems@545738ea4ac5730dc20e6ed5f50315dfcf3322f1`,

which proves the physical two-bank local-phase Plancherel theorem. I apply that theorem below to every possible nondegenerate physical 2+2 crossing in the stress family.

## 2. The target-valid stress family

For integer `m>=2` and nonzero real `a,b`, split the physical coordinates as one hub `h`, a star-leaf bank `U` of size `m`, and a rank-one bank `V` of size `m`, and set

```text
A_m(a,b) = [ 0                    (a/sqrt(m)) 1^T     0
             (a/sqrt(m)) 1       0_m                 0
             0                    0                   (b/m) J_m ].
```

The star block has nonzero eigenvalues `+|a|,-|a|`; the `V` block has nonzero eigenvalue `b`. Hence the complete nonzero spectrum is

`{+|a|,-|a|,b}`.

In particular `|a|,|b|>=1` puts the family exactly inside the owner target for every `m`.

## 3. Every physical Z3 cut vanishes

For any disjoint physical coordinate sets `I,J`, the cross block `A_m[I,J]` is the sum of two matrices:

1. the star contribution, of rank at most one, because the unique hub belongs to at most one side of the cut;
2. the `V`-bank contribution, a submatrix of `(b/m)J_m`, also of rank at most one.

Therefore

`rank A_m[I,J] <= 2`

for **every** disjoint physical cut, and consequently

`Z3(I,J)=e3(A_m[I,J] A_m[I,J]^T)=0`.

Thus the marginal-free three-volume receiver proved in the preceding fleet02/B03 run is identically unavailable on this family. This is consistent with the existing correction forbidding a universal rank-three physical cut.

## 4. Every physical square peel kills Schur Z2 exactly

The only nonzero physical diagonal entries are the `V`-bank diagonals

`d = b/m`.

Take any `v in V`. The column `A_{-v,v}` is zero outside the other `V` coordinates and equals `(b/m) 1` on them. The Schur complement after completing the physical square at `v` is

`S_v = A_{-v,-v} - A_{-v,v} d^{-1} A_{v,-v}`.

On the remaining `V` bank,

`(b/m) J_{m-1} - ((b/m)1)((b/m)1)^T/(b/m) = 0`.

No star--`V` coupling is created because the original matrix is a direct sum across those two pieces. Hence

`S_v = (pure star on {h} union U) direct-sum 0_{m-1}`.

Every physical cross block of a pure star has rank at most one. Therefore, for every physical cut of every nonzero-diagonal Schur residual,

`Z2 = e2(MM^T) = 0`.

So the newest fleet02/B03 square receiver

`||p_Q||_infty <= 8 e^(1/4) (|d|^4 Z2)^(-1/8)`

has no admissible `Z2>0` cut here. More sharply, every candidate invariant `|d|^4 Z2` is **exactly zero**, not merely small.

This is the promised first unpaid implication: an exhaustive structural theorem cannot consist only of

`(uniform physical Z3) OR (physical square + uniform Schur Z2)`.

A grouped-hub/low-rank-carrier outcome is genuinely necessary.

## 5. Newest partner theorem: best physical 2+2 certificate still deteriorates

Fleet03/B03 r41 proves that if two genuine physical 2D product banks `X,Y` have cross term `X^T C Y`, with arbitrary same-bank phases retained, then

`sup_s E|S-s|^(-1/2) <= 8 |det C|^(-1/4)`

and

`int |t|^(-1/2)|phi_S(t)|^2 dt <= (16/3) sqrt(2 pi) |det C|^(-1/4)`.

Conditioning on every coordinate outside the selected two banks is legitimate because the remaining terms become same-bank functions or affine shifts, all explicitly allowed by the theorem.

For `A_m`, every physical `2 x 2` cross minor has absolute determinant either zero or

`|a b| / m^(3/2)`.

Indeed a nonzero determinant must use one star edge `a/sqrt(m)` and one independent `V`-bank edge `b/m`; both underlying contributions have rank one. The value is attained, for example, with

`X=(X_h,X_{v1})`, `Y=(X_{u1},X_{v2})`,

for which the quadratic cross term has

`C = diag(2a/sqrt(m), 2b/m)`

and

`|det C| = 4 |ab| m^(-3/2)`.

Therefore the **best** certificate available from the r41 theorem over all physical 2+2 choices is

`sup_s E|Q-s|^(-1/2)
 <= 4 sqrt(2) |ab|^(-1/4) m^(3/8),`

and the corresponding assigned whole-copy time certificate is

`int |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (16/3) sqrt(pi) |ab|^(-1/4) m^(3/8).`

These are valid inequalities, but their constants diverge like `m^(3/8)`. Thus the new two-bank theorem is behaving correctly; what fails is localization to a fixed physical 2+2 bank before aggregating the many weak edges.

No statement here says the actual half-potential diverges. The claim is precisely about the best certificate furnished by this local determinant mechanism.

## 6. Pinned Theorem H aggregates first and gives a uniform bound

Now apply the completed pinned Theorem H to the **same** `A_m`.

Take the genuine physical hub set `H={h}` and let `I=U union V`. Inside `I`, write the `V`-bank block as the rank-one term

`b v v^T`,  `v = m^(-1/2) 1_V`,

with zero diagonal remainder. The augmented frame rows (rank-one Fresnel direction first, hub coupling second) are

- for `u in U`: `(0, a/sqrt(m))`;
- for `v_j in V`: `(1/sqrt(m), 0)`.

Hence

`G_tilde = diag(1,a^2)`, `det G_tilde=a^2`,

and every normalized leverage is exactly `1/m <= 1/2`.

Theorem H therefore yields the explicit global envelope

`boxed:
 |phi_Q(t)| <= min{1, K |t|^(-3/2)},
 K = 4 pi^(3/2) |a|^(-1)|b|^(-1/2).
`

Fourier inversion gives

`boxed:
 ||p_Q||_infty
 <= 3 * 4^(2/3) |a|^(-2/3)|b|^(-1/3).
`

Thus for `|a|,|b|>=1`,

`||p_Q||_infty <= 3*4^(2/3) = 7.559526299...`.

This is an actual application of the required pinned package, and it uses only original-coordinate product structure. No post-rotation independence is invoked.

## 7. Assigned decoupled-time endpoint is also uniformly paid

The same global envelope directly controls the assigned integral. Since

`|phi_Q(t)|^2 <= min{1,K^2 |t|^(-3)}`

and the crossover is `T=K^(2/3)`, exact integration gives

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =< 2[ int_0^T t^(-1/2)dt + K^2 int_T^infty t^(-7/2)dt ]
 = (24/5) K^(1/3).`

Therefore

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (24/5) 4^(1/3) sqrt(pi)
    |a|^(-1/3)|b|^(-1/6).
`

At target scale `|a|,|b|>=1` this is at most

`13.505256516...`.

Using only the exact whole-independent-copy identity

`|phi_Q(t)|^2 = E exp(it(Q-Q'))`

and the positive-regularized half-Riesz identity used in the partner proof, this equivalently gives

`boxed:
 E|Q-Q'|^(-1/2)
 <= (24/5) 2^(1/6)
    |a|^(-1/3)|b|^(-1/6)
 < 5.388
`

at target scale. The sum/difference dependence of any coordinate pair is never split.

For completeness, the one-copy half-potential is also uniformly bounded by integrating `min(1,K|t|^-3/2)`:

`sup_s E|Q-s|^(-1/2)
 <= 3*2^(7/6)|a|^(-1/3)|b|^(-1/6)
 < 6.735`

at target scale.

## 8. Structural conclusion

This one explicit target family simultaneously has:

- `Z3=0` on every physical cross cut;
- after every possible nonzero physical square peel, `Z2=0` on every Schur-residual physical cut;
- best physical 2+2 determinant `4|ab|m^(-3/2)` in the quadratic cross matrix, so the newest local two-bank Plancherel certificate worsens as `m^(3/8)`;
- but a grouped mixed-hub certificate with density at most `7.560` and assigned whole-copy time integral at most `13.506`.

So **aggregate before localizing** is not a technical preference here; it is structurally necessary for any proof tree that aims to cover all target matrices with uniform constants.

This sharpens, rather than replaces, the existing corrections `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: those corrections rule out individual extraction lemmas, while the present calculation exhibits the simultaneous collapse of the latest `Z3`, square+`Z2`, and fixed physical 2+2 determinant certificates on the same target family and quantifies the separation from the grouped time-integral route.

The remaining full-target implication is therefore structural: prove that every remaining no-pivot/hub survivor admits either a quantitatively uniform grouped-hub/low-rank-carrier aggregation, or another already-paid global receiver. It is not enough to select a bounded-size physical bank or one physical square first.

Full QFORM remains OPEN. Unrestricted continuity remains OPEN; continuity does hold on this displayed family because the pinned `|t|^-3/2` envelope is integrable.
