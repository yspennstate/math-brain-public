SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T10:11:39Z.
attacking: the punctured zero-pivot collar after the newest fleet03/B03 r52 — use the pinned square peel plus the orientation-free rank-two half-Riesz theorem for every nonzero independent scalar pivot, and prove that the whole-copy negative-half time budget stays uniform as that pivot tends to zero.

# fleet02/B03 r54 — punctured-pivot density certificate and pivot-uniform collision time

Status: **NEW SUPPORTING SYNTHESIS / NEW PIVOT-UNIFORM COLLISION LEMMA / NEW EXPLICIT PUNCTURED-COLLAR MAP / LATEST PARTNER r52 APPLIED / REQUIRED PINNED RESULT APPLIED / FULL QFORM OPEN.** Full-target continuity remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and correction of the early direction

The same-run `EARLY.md` began to prove an arbitrary-baggage zero-pivot extension of fleet03/B03 r51. A fresh partner-history resolution showed that fleet03/B03 had already completed exactly that step in **r52**, `QFORM-SAMEBANK-SHEAR-BAGGAGE-HYPERBOLIC-v1` and `QFORM-2PLUS1-ZEROPIVOT-DETERMINANT-v1`. I therefore preserve the early note as an overlap/false start and change mechanism rather than relabeling it as new work.

The newest partner r52 pays every invertible 2+1 packet with a genuinely independent scalar source whose quadratic pivot is exactly zero. Its own stated next gap is a **small but nonzero independent scalar square**. This report attacks that punctured collar.

The resulting map is now precise. For a 2+1 scalar packet

    B = [[C,g],[g^T,c]],                                   (1.1)

with the two-dimensional mode `Y` coming from one original cap-one product bank and the scalar `V` coming from a source-disjoint bank:

* `c=0`: newest partner r52 gives a determinant-only density endpoint;
* `c!=0`: the pinned square peel plus the completed orientation-free rank-two half-Riesz theorem gives an explicit density endpoint, but it loses `|c|^{-1/4}`;
* for **all** `c`, including through `c=0`, a direct source-preserving Plancherel argument gives a pivot-independent bound on

      int |t|^(-1/2) |phi_Q(t)|^2 dt.

Thus the unresolved analytic collar is no longer a collision-energy problem. It is specifically the upgrade from a uniformly paid whole-copy half-Riesz budget to a one-copy `L^infinity` density bound when `0<|c|<<1` and no localized/spread aggregate receiver is available.

## 2. New nonzero-pivot density certificate

Let `X=(X_i)` be a bank of genuine independent scalar coordinates with densities at most one. Let `U` have two orthonormal columns and put

    Y = U^T X in R^2.

Let `V` be independent of `X`, with scalar density bounded by `N`. Let

    B = [[C,g],[g^T,c]]

be symmetric, `c!=0`, `det B!=0`, with `C` symmetric 2x2. Allow arbitrary affine terms in the `X`-bank and in `V`; source-disjoint outside variables may be conditioned first. Write the resulting scalar quadratic form as `Q`.

Complete the square in the actual independent scalar `V`:

    Q
      = c ( V + c^(-1) g^T Y + shift )^2
        + R(X),                                             (2.1)

where the quadratic part of `R` on the two-dimensional mode is the Schur matrix

    S = C - g g^T/c.                                       (2.2)

The determinant identity is exact:

    det B = c det S.                                       (2.3)

Because `B` is invertible, `S` is invertible.

For fixed `X`, the translated scalar `V+...` still has density cap `N`. The completed pinned square-peel argument therefore gives, at every target level `z`,

    p_Q(z)
      <= N |c|^(-1/2) E |R-z|^(-1/2).                     (2.4)

Now apply the completed orientation-free theorem

    QFORM-RANK2-AFFINE-HALF-RIESZ-v1

from `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`. It is uniform in arbitrary affine terms and gives

    sup_z E|R-z|^(-1/2)
      <= 128 |det S|^(-1/4).                              (2.5)

Combining (2.3)--(2.5),

    boxed:
    ||p_Q||_(infinity,ess)
      <= 128 N |c det B|^(-1/4).                          (2.6)

This is a genuine linear small-ball bound:

    boxed:
    P(Q in I)
      <= 128 N |c det B|^(-1/4) |I|.                     (2.7)

No post-rotation probabilistic independence is used. The only probabilistic separation is the actual source separation between the original `X` bank and the scalar `V` bank. The deterministic two-mode basis may be rotated because the rank-two half-Riesz theorem itself is orientation-free and was proved in original product coordinates.

### Required pinned result used at an actual equation

Equation (2.4) is exactly the completed **square peel**, Lemma 4.2 of the required pinned

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

with the harmless extra factor `N` for a scalar source of density cap `N`. For `N=1` it is literally the pinned statement

    D(Q) <= |c|^(-1/2) H_(1/2)(Schur remainder).

Thus the required pinned package is used in the proof, not merely cited.

## 3. New pivot-uniform whole-copy collision estimate

The density certificate (2.6) deteriorates as `c -> 0`. The assigned decoupled-time quantity does **not**.

### Lemma `QFORM-TWISTED-HYPERBOLIC-COLLISION-v1`

Let `R` be a scalar random variable with density bounded by `L`. Let `V` be independent of the entire source containing `R`, with density bounded by `N`. Let `F` be any real random variable measurable with respect to the source containing `R`; it may retain arbitrary dependence on `R`. Let `beta!=0`, and let `c,d` be arbitrary reals. Define

    Q = F + 2 beta R V + c V^2 + d V.                      (3.1)

Then for every `t!=0`,

    boxed:
    |phi_Q(t)|^2
      <= min{ 1, pi L N / (|beta| |t|) }.                 (3.2)

Consequently

    boxed:
    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= 8 sqrt( pi L N / |beta| ),                       (3.3)

and for an independent copy `Q'` of the **whole scalar output**,

    boxed:
    E|Q-Q'|^(-1/2)
      <= 4 sqrt( 2 L N / |beta| ).                        (3.4)

#### Proof

Disintegrate only with respect to the genuine scalar `R`. Set

    A_t(r) = E[ exp(itF) | R=r ],

so `|A_t(r)|<=1`. Put

    h_t(v)=p_V(v) exp(it(c v^2+d v)).

The quadratic and affine terms in `V` are a **phase twist**, hence

    |h_t(v)| = p_V(v),
    integral |h_t|^2 <= N.                               (3.5)

With the Fourier convention `hat h(xi)=int e^{i xi v}h(v)dv`,

    phi_Q(t)
      = int p_R(r) A_t(r) hat(h_t)(2 beta t r) dr.         (3.6)

Cauchy-Schwarz in the probability measure `p_R(r)dr` gives

    |phi_Q(t)|^2
      <= int p_R(r)|hat(h_t)(2 beta t r)|^2 dr
      <= L int |hat(h_t)(2 beta t r)|^2 dr.               (3.7)

Plancherel and the change `xi=2 beta t r` yield

    int |hat(h_t)(2 beta t r)|^2 dr
      = pi/(|beta t|) int |h_t(v)|^2 dv
      <= pi N/(|beta t|).                                 (3.8)

This proves (3.2). If `K=pi L N/|beta|`, direct integration gives

    int_R |t|^(-1/2) min(1,K/|t|) dt
      = 8 sqrt(K),                                        (3.9)

which is (3.3). Finally use only the whole-output identity

    |phi_Q(t)|^2 = E exp(it(Q-Q'))                         (3.10)

and the regularized one-dimensional Riesz identity used throughout the programme,

    int |t|^(-1/2)|phi_Q(t)|^2 dt
      = sqrt(2pi) E|Q-Q'|^(-1/2),                         (3.11)

which gives (3.4). No coordinatewise `X-X'` is separated from its conjugate `X+X'`. QED.

The important feature is that the bound is **independent of `c`**. A nonzero square on the independent scalar is harmless to the collision-time estimate because it is absorbed as a modulus-one Plancherel twist before any absolute-value loss.

## 4. Application to the full 2+1 coefficient matrix

Return to (1.1). Rotate only the deterministic two-dimensional mode basis so that

    g = (0,beta),   beta=||g||_2.                          (4.1)

Call the corresponding same-bank projections `(S,R)`. They are generally dependent; nothing here declares otherwise. All same-bank quadratic and affine terms are absorbed into `F(S,R)`. The independent scalar is `V`. Therefore Lemma 3 applies directly.

If `R` is a normalized one-dimensional projection of an original cap-one product bank, the standard scalar product-projection bound gives `L<=sqrt(2)`. If `V` is also a normalized projection of a disjoint product bank, `N<=sqrt(2)`. Hence

    boxed:
    int |t|^(-1/2)|phi_Q(t)|^2 dt
      <= 8 sqrt( 2pi/|beta| ),                            (4.2)

    boxed:
    E|Q-Q'|^(-1/2)
      <= 8 / sqrt(|beta|).                                (4.3)

For literal physical `R,V`, one has `L=N=1`, improving these to

    int |t|^(-1/2)|phi_Q(t)|^2 dt
      <= 8 sqrt(pi/|beta|),                               (4.4)

    E|Q-Q'|^(-1/2)
      <= 4 sqrt(2/|beta|).                                (4.5)

Thus the newest partner's zero-pivot height theorem and the nonzero-pivot square-peel theorem meet a collision estimate that does not notice the pivot crossing at all.

## 5. Strict exact-target collar family

Take the strict target matrix from newest partner r52,

    B_0 = [[3,2,0],
           [2,5,3],
           [0,3,0]].                                      (5.1)

Partner r52 proves its eigenvalues lie in

    (-2,-1), (2,3), (7,8),                               (5.2)

and `det B_0=-27`.

Scale by two and add a scalar pivot:

    B_epsilon
      = [[6,4,0],
         [4,10,6],
         [0,6,epsilon]],       |epsilon|<=1.              (5.3)

Since `2B_0` has eigenvalues in `(-4,-2),(4,6),(14,16)` and the perturbation `epsilon e_3e_3^T` has operator norm at most one, Weyl's inequality places the eigenvalues of `B_epsilon` inside

    (-5,-1), (3,7), (13,17).                              (5.4)

Hence every `B_epsilon` is a strict instance of the exact owner target. Its determinant is

    boxed: det B_epsilon = 44 epsilon - 216,              (5.5)

so throughout `|epsilon|<=1`,

    |det B_epsilon| >= 172.                               (5.6)

Let `X_1,X_2,X_3` be arbitrary independent cap-one inputs and

    Q_epsilon = X^T B_epsilon X.                          (5.7)

### Exact zero pivot: newest partner r52

At `epsilon=0`, the pair `(X_1,X_2)` has joint density cap `M<=1` and `X_3` has `N<=1`. Applying the newest fleet03/B03 r52 determinant theorem at the literal equation gives

    boxed:
    ||p_(Q_0)||_(infinity,ess)
      <= 6 |det B_0*2^3|^(-1/3)
      = 6 * 216^(-1/3)
      = 1.                                                (5.8)

Thus

    P(Q_0 in I) <= |I|.                                   (5.9)

This is the required current-partner application; the early same-run zero-pivot derivation is not counted as new.

### Punctured pivot: new square-peel certificate

For `epsilon!=0`, (2.6) gives

    boxed:
    ||p_(Q_epsilon)||_(infinity,ess)
      <= 128 [ |epsilon| |216-44epsilon| ]^(-1/4).        (5.10)

This is a valid density inequality for every punctured member of the collar. It behaves like

    O(|epsilon|^(-1/4))                                   (5.11)

as `epsilon ->0`, so it cannot be the final interpolation mechanism.

### Whole-copy time is uniform across the same collar

Here the hyperbolic coefficient in `2 beta R V` is `beta=6`, and `R=X_2`, `V=X_3` have `L=N=1`. Equation (4.4) gives for **every** `|epsilon|<=1`, including zero,

    boxed:
    int |t|^(-1/2)|phi_(Q_epsilon)(t)|^2 dt
      <= 8 sqrt(pi/6)
      = 5.788810036466141... ,                            (5.12)

and

    boxed:
    E|Q_epsilon-Q_epsilon'|^(-1/2)
      <= 4/sqrt(3)
      = 2.309401076758503... .                            (5.13)

This proves that the singular factor in (5.10) is not a deterioration of the assigned collision-energy resource.

## 6. A required pinned localized receiver proves the blow-up is an interface artifact

The completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A says that a literal physical `3x3` principal block whose three eigenvalues all have modulus at least `c` gives

    ||p_Q||_infinity <= 6 sqrt(pi)/c                         (6.1)

uniformly in all affine terms after conditioning outside coordinates.

By (5.4), `c=1` applies to every `B_epsilon` above. Therefore the same actual target family satisfies

    boxed:
    ||p_(Q_epsilon)||_infinity
      <= 6 sqrt(pi)
      = 10.634723105433096...                              (6.2)

uniformly for all `|epsilon|<=1`.

Hence the divergence in the punctured square-peel certificate (5.10) is demonstrably a **proof-interface loss**, not an output-density blow-up. The localized pinned theorem pays the physical three-coordinate collar uniformly, while the newest r52 theorem pays the exact zero pivot much more sharply.

## 7. Spread embedding: the other extreme is also already paid

The same conclusion holds after completely diffusing the three modes. Let `m>=4` be even. On one original product bank choose flat orthonormal vectors `r,t in R^m`, and on a disjoint bank choose a flat unit vector `v in R^m`. Set

    Y_1=<r,X>,  Y_2=<t,X>,  V=<v,Z>,
    Q_(m,epsilon) = (Y_1,Y_2,V)^T B_epsilon (Y_1,Y_2,V).  (7.1)

The embedding columns are orthonormal, so the three nonzero eigenvalues are exactly those of `B_epsilon`; the family remains a strict owner-target family. Physical leverage is `2/m` on the first bank and `1/m` on the second, hence at most `1/2` for `m>=4`.

Apply the required pinned **Theorem F** with the full coordinate set. Its Gram determinant is one and the product of the three nonzero eigenvalues has modulus `|det B_epsilon|`. Therefore

    boxed:
    ||p_(Q_(m,epsilon))||_infinity
      <= 12 |det B_epsilon|^(-1/3)
      <= 12 * 172^(-1/3)
      = 2.157769733575401... .                            (7.2)

The same pinned envelope gives

    boxed:
    int |t|^(-1/2)|phi_(Q_(m,epsilon))(t)|^2 dt
      <= (48/5)sqrt(pi) |det B_epsilon|^(-1/6)
      <= 7.215361502468649... ,                            (7.3)

and a continuous `C_0` density on this spread branch. Unrestricted continuity remains open.

In original coordinates, every fixed-size physical minor of this diffuse embedding tends to zero with `m`, while the aggregate three-mode determinant stays at least `172`. So the correct structural currency cannot require a uniformly good bounded physical minor before aggregation.

## 8. Structural conclusion

After consuming the newest partner r52, the 2+1 scalar picture is now:

1. **exact zero pivot `c=0`** — determinant-only density bound from r52;
2. **nonzero pivot bounded away from zero** — (2.6) gives an explicit density bound through the pinned square peel and rank-two half-Riesz theorem;
3. **all pivots, including `c ->0`** — the assigned whole-copy negative-half time integral is uniformly controlled by (3.3);
4. **localized physical triples** — pinned Theorem A pays the entire collar uniformly;
5. **spread three-mode frames** — pinned Theorem F pays the entire collar uniformly.

The first unpaid implication is therefore a genuinely narrower **high-leverage, unlocalized, punctured small-pivot bridge**: when `0<|c|<<1`, `|det B|` and the hyperbolic coupling stay quantitative, and neither a localized physical triple nor a spread aggregate receiver is available, convert the pivot-uniform collision resource into a one-copy linear small-ball bound **without** treating the small square `cV^2` as a uniformly small random perturbation. Small coefficient norm is not small random error for arbitrary unbounded cap-one inputs.

The unrestricted QFORM conjecture remains OPEN. The present argument does not assert that half-Riesz collision credit alone implies bounded density, and it does not use any refuted conditional projection-density moment, post-rotation independence, pointwise quadratic-phase decay, or arbitrary-joint 3D coarea bound.

## 9. Sources and integrity

Fresh control and live corrections were read from `math-research-brain` main during this invocation; owner revision remains `2026-09-22.15`, QFORM-only. The newest compatible partner is fleet03/B03 r52, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260924T095801Z-fleet03-B03-QFORM-auto11-r52/REPORT.md`, source commit chain containing `4edcae3a97a0de7376ea6f8149173bdf1c910999` / checks `cead39f2714d739dd5d00c7d3a537de4adba4732`. Required pinned source: `e5f71d79eff325201dd0274053d20268ce65b837`, RESULTS / FOURIER_ROUTE_REPORT / COUNTEREXAMPLE_SEARCH. Rank-two fractional source: `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`.

Changed-file scope is only this immutable fleet02/B03 run path plus the authorized fleet02/B03 handoff/memory/run records. No protected controls, peer artifacts, tasks, schedules, enablement, notifications, email, permissions, public release, cross-account authentication, paid calls or remote workflows are modified. Connector-only execution exposes no repository secret-scanner command; the generated mathematical text was manually reviewed for credentials, private non-mathematical content, signed URLs and machine paths. That is a limited fallback check, not a platform secret-scan attestation.
