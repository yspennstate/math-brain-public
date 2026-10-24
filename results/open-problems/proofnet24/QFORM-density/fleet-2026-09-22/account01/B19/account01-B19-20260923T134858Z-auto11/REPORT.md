SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T13:48:58Z.
attacking: the STAR4 quantitative-rank-two branch; elevate the two hub-star vectors into literal selected third-volume packets, pay diffuse packets by the completed fractional-subvolume theorem, and isolate the true two-sided near-rank-two aligned core without deleting any tail.

# account01/B19 auto11 — STAR4 rank-two elevation to selected volume or aligned core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new selected-volume payment branch; full-target continuity remains OPEN.

The unrestricted theorem is still OPEN. All variables below are ORIGINAL-coordinate product variables. No spectral rotation is used as a probabilistic independence statement; no small matrix tail is discarded; no worst conditional projection-density bound, arbitrary-joint coarea lemma, single-minor extraction, or law-uniform pointwise quadratic Fresnel decay is used.

## 1. Fresh source graph

Fresh owner control immediately before publication remained QFORM-only at `yspennstate/math-research-brain@8791165743a5d252b8e6a7a753648589046ed2fa`, OWNER CONTROL revision `2026-09-22.15`; no later stop/pause for account01/B19 was present.

### 1.1 Designated partner account02/B19 actually used

The newest completed partner report used here is

`yspennstate/math-open-problems@db5c35db0ea104ee7e38d904c1a759ba46164f49`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T130709Z-account02-B19-QFORM-auto11/REPORT.md`,

with its exact-constant/check follow-ups through `b0628a95c0c4630d063fe8c5649416c804dbceea`.

It fixes

`tau=2^-20`,

and, after the completed global reduction/ridge exit and D5 exit, leaves a literal physical STAR4 packet

`h^c=J disjoint_union K`,

`u=A[J,h]`, `v=A[K,h]`, `N=A[J,K]`,

with

`||u||_2^2>beta`, `||v||_2^2>beta`,                         (1.1)

`beta=(1/12800-tau-2tau^2)/2
     =0.0000385856619323021732270717620849609375...`,       (1.2)

`E:=||N||_F^2>E0:=(1-tau)^2/4
  =0.24999952316306917055...`,                              (1.3)

and

`sum_(r<=4) s_r(N)^2 >(63/64)E`.                            (1.4)

Its first internal dichotomy says either

`(R2)  s_2>s_1/16`,                                         (1.5)

in which case

`rho:=s_1s_2>rho_*:=63(1-tau)^2/16384
                  =0.0038452075095882221056...`,            (1.6)

or the exact leaf cross is a Frobenius-relative rank-one tube

`(R1)  (sum_(r>=2)s_r^2)^(1/2)<=s_1/6`.                    (1.7)

This run attacks `(R2)` and does not claim `(R1)` is solved.

### 1.2 Completed peer analytic theorem actually applied

I apply account03/B09 r32,

`QFORM-FRACTIONAL-SUBVOLUME-BL-v1`,

canonical source

`yspennstate/math-open-problems@56d0211f2f04d74152032fd1914196673eb5c3e6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T124906Z-account03-B09-QFORM-r32/REPORT.md`.

At its exact scope: for an ACTUAL original-coordinate cross matrix `M`, choose any nonempty family `Omega` of actual physical `3 x 3` minors and put

`Z_Omega=sum_(R,C in Omega) det M[R,C]^2`.

Normalize these squared minors and let `alpha_i` be the row inclusion probabilities. If

`max_i alpha_i<=1/2`,                                            (1.8)

then the FULL quadratic-plus-affine form, with arbitrary same-bank phases and arbitrary outside couplings retained, satisfies

`||p_Q||_infinity <=3e Z_Omega^(-1/6)`,                          (1.9)

and `phi_Q in L^1`, so the density is continuous and vanishes at infinity.

The fact that only row marginals are constrained is important below: the selected family is allowed to contain the hub column in every minor.

## 2. New exact exterior identity for a star vector appended to an arbitrary cross block

Let

`N=sum_r s_r p_r q_r^T`, `x_r=s_r^2`,                            (2.1)

be any SVD, with `x_1>=x_2>=...>=0`. For an arbitrary vector `u in R^J`, define the literal selected third-volume

`Gamma_J(u;N)
 := sum_{R subset J, |R|=3}
    sum_{C subset K, |C|=2}
    det( [u,N[:,C]][R,:] )^2`.                                  (2.2)

This is not a spectral minor. It is exactly the squared volume of the actual physical `3 x 3` minors of the cross block

`M_J=A[J,{h} union K]=[u,N]`                                    (2.3)

whose three columns consist of the physical hub column `h` and two physical columns from `K`.

### Lemma 2.1 — `QFORM-STAR-APPENDED-SELECTED-VOLUME-IDENTITY-v1`

For every `N,u`, including singular `N` and repeated singular values,

`boxed:
 Gamma_J(u;N)
 =sum_(a<b) x_a x_b
   ( ||u||^2-|<u,p_a>|^2-|<u,p_b>|^2 ).`                        (2.4)

If `P_2` is the projection onto any fixed top-two left singular subspace and

`d_J^2=||(I-P_2)u||^2`,                                        (2.5)

then, with `x_3=0` when rank `N<=2`,

`boxed:
 Gamma_J(u;N)
 >=x_1x_2 d_J^2+x_2x_3 ||P_2u||^2
 =x_2x_3||u||^2+x_2(x_1-x_3)d_J^2.`                             (2.6)

The symmetric right-side identity holds for `v`:

`Gamma_K(v;N)
 :=sum_{R subset K, |R|=3}
   sum_{C subset J, |C|=2}
   det([v,N^T[:,C]][R,:])^2`,                                  (2.7)

and, for the top-two right projection `Q_2`,

`Gamma_K(v;N)
 >=x_1x_2 d_K^2+x_2x_3||Q_2v||^2`,
`d_K^2=||(I-Q_2)v||^2`.                                        (2.8)

#### Proof

Use exterior algebra only on deterministic coefficient spaces. The map `w -> u wedge (wedge^2 N)w` from `wedge^2 R^K` to `wedge^3 R^J` has Hilbert--Schmidt square exactly (2.2), because the physical coordinate wedge bases enumerate the minors in (2.2). Under the SVD,

`(wedge^2 N)(q_a wedge q_b)=s_as_b(p_a wedge p_b)`.

Therefore

`Gamma_J
 =sum_(a<b)s_a^2s_b^2 ||u wedge p_a wedge p_b||^2`,

and

`||u wedge p_a wedge p_b||^2
 =||u||^2-|<u,p_a>|^2-|<u,p_b>|^2`,

which proves (2.4).

For a component of `u` in `span(p_1,p_2)^perp`, the pair `(1,2)` alone contributes coefficient `x_1x_2`. For the `p_1` component, the pair `(2,3)` contributes `x_2x_3`; for the `p_2` component, `(1,3)` contributes `x_1x_3>=x_2x_3`. All omitted terms are nonnegative. This gives (2.6). The right-side formula is identical after transposition. QED.

This identity is useful because it spends an AGGREGATE of actual hub-bordered minors; it never asserts one physical `3 x 3` determinant is uniformly large.

## 3. New STAR4 rank-two elevation theorem

Define the universal selected-volume scale

`G_perp := rho_*^2 beta/4
 =1.4262824133284200880811666885790e-10`,                       (3.1)

and

`G_3 := beta E0^2/4096
 =5.8876823028402203887936092279362e-10`.                       (3.2)

Thus

`G_*:=min(G_perp,G_3)=G_perp`.                                  (3.3)

### Theorem 3.1 — `QFORM-STAR4-RANK2-SELECTEDVOLUME-OR-ALIGNEDCORE-v1`

Assume the partner STAR4 packet (1.1)--(1.6), i.e. the quantitative rank-two branch `(R2)`. Then at least one of the following holds.

**(A) Selected-volume Fourier payment.** The full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <=3e G_*^(-1/6)
 <356.765.`                                                       (3.4)

**(B) Literal selected-third-volume anchor.** On at least one side, there is an ORIGINAL physical leaf coordinate whose incident mass in the corresponding hub-bordered selected-minor family is larger than

`boxed: G_*/2
 =7.1314120666421004404e-11.`                                    (3.5)

Precisely, either there is `i in J` with

`sum_(R contains i, |R|=3; C subset K, |C|=2)
 det([u,N[:,C]][R,:])^2 >G_*/2`,                                (3.6)

or the symmetric statement holds for some `k in K` with `v,N^T`.

**(C) Two-sided near-rank-two aligned core.** For fixed top-two singular projections `P_2,Q_2`,

`boxed:
 sum_(r>=3)s_r(N)^2 <(3/64)E,`                                  (3.7)

and simultaneously

`boxed:
 ||P_2u||^2>3beta/4,
 ||Q_2v||^2>3beta/4.`                                           (3.8)

No term in the tail from (3.7) has been deleted from the random quadratic form. Alternative (C) is only a deterministic structural reduction.

#### Proof

Write `x_r=s_r^2` as above.

### Step 1: if the third cross direction is not tiny, both star elevations carry fixed selected volume

Suppose

`x_3>=E/64`.                                                     (3.9)

Since `x_2>=x_3`, Lemma 2.1 and (1.1) give

`Gamma_J>=x_2x_3||u||^2
          >=(E/64)^2 beta
          >G_3>G_*`,                                             (3.10)

and identically

`Gamma_K>G_3>G_*`.                                               (3.11)

Consider the selected family in (2.2) for the ACTUAL cross matrix `M_J=[u,N]`. If all normalized physical-row inclusion probabilities are at most `1/2`, apply the completed peer theorem (1.9) directly and obtain

`||p_Q||infinity<=3e Gamma_J^(-1/6)<3eG_*^(-1/6)`,              (3.12)

which is alternative (A). This application retains, on the opposite side `{h} union K`, the entire hub square, the whole `h--K` star, and arbitrary `K--K` curvature as same-side phase; on the `J` side it retains arbitrary `J--J` curvature. Hence no omitted coefficient or independence assertion is hidden in (3.12).

If the row-marginal gate fails, some original `i in J` has inclusion probability `>1/2`, so its incident selected volume is `>Gamma_J/2>G_*/2`, which is (B). The same argument may instead be applied to `Gamma_K`. Therefore (3.9) always yields (A) or (B).

### Step 2: if a hub star has fixed transverse mass to the top-two cross core, it is also paid or anchored

We may now suppose

`x_3<E/64`.                                                       (3.13)

If

`d_J^2=||(I-P_2)u||^2>=beta/4`,                                 (3.14)

then the `(1,2)` term in Lemma 2.1 and the partner product bound (1.6) give

`Gamma_J>=x_1x_2 d_J^2
          =rho^2 d_J^2
          >rho_*^2 beta/4=G_*`.                                  (3.15)

Again the completed selected-subvolume theorem gives (A) when the row marginals are diffuse, while failure of its gate gives the literal incident-mass alternative (B). The same reasoning applies to `d_K`.

Consequently, if neither (A) nor (B) occurs, then necessarily

`d_J^2<beta/4`, `d_K^2<beta/4`.                                  (3.16)

Using `||u||^2,||v||^2>beta` gives (3.8).

### Step 3: the exact tail is quantitatively near rank two

The partner STAR4 condition (1.4) says

`x_1+x_2+x_3+x_4>(63/64)E`.                                     (3.17)

Under (3.13), monotonicity gives `x_4<=x_3<E/64`. Hence

`x_1+x_2 >(63/64)E-2(E/64)=(61/64)E`,                            (3.18)

so

`sum_(r>=3)x_r=E-x_1-x_2<(3/64)E`.                              (3.19)

This is (3.7). Thus if neither the analytic payment nor the literal aggregate anchor occurs, the only possibility is the two-sided aligned near-rank-two core (C). QED.

### Constant check

With the exact partner constants,

`3e G_*^(-1/6)=356.7643758645407...`,                            (3.20)

and the higher-third-direction subcase alone has the sharper bound

`3e G_3^(-1/6)=281.6815111992349...`.                            (3.21)

These are large but universal. No effort is made here to optimize them.

## 4. Compact conditional proof assembly after the new splice

The current source-pinned graph can now be written in a short exhaustive form, conditional only on the already-pinned global reduction steps cited by the partner.

1. **Full target -> strict `N3(2^-20)`.** The geometric physical-pivot synthesis used by account02/B19 allows one fixed universal no-pivot scale.
2. **Spectral-window diffuse exit.** If `max_i (1_{|A|>=1/16})_ii<=1/50`, the completed ridge/window theorem gives `||p_Q||infinity<217.085` and continuity.
3. **Every window failure -> literal STAR cut.** The partner constructs one physical `h|J|K` with both star energies `>beta` and leaf cross energy `E>E0`.
4. **Diffuse fifth-volume exit.** If the first four leaf-cross singular directions contain at most `63/64` of `E`, D5 gives `||p_Q||infinity<198.634` and continuity.
5. **STAR4 dichotomy.** The partner leaves either the relative-rank-one tube (1.7) or quantitative-rank-two branch (1.5)--(1.6).
6. **New quantitative-rank-two splice.** Theorem 3.1 pays that branch by `<356.765` whenever one of the two natural hub-bordered selected-volume laws is row-diffuse. Every unpaid quantitative-rank-two state is now either an explicit physical selected-third-volume anchor (3.5)--(3.6), or the exact two-sided aligned near-rank-two core (3.7)--(3.8).
7. **Existing exact-rank-three TRIANGLE splice.** When its separate hypotheses genuinely hold, the partner's pinned TRIANGLE receiver gives its existing `<65` bound. I do not infer those hypotheses from STAR4.

Therefore the first compatible global debt on this proof route is no longer the raw STAR4 packet. It is the union

`QFORM-STAR4-ALIGNED-RANK2-OR-AGGREGATE-ANCHOR-v1`:

- the relative-rank-one tube (1.7), still with its entire nonzero tail;
- the two-sided aligned near-rank-two core (3.7)--(3.8), with arbitrary same-side curvature and all tail coefficients retained;
- the literal aggregate selected-volume anchor (B), to be routed through a second-anchor / grouped-Schur receiver without choosing a tiny single minor.

This is a product-preserving finite-core/aggregate-anchor frontier. The new proof has removed every quantitative-rank-two STAR4 state in which either star supplies fixed transverse third-volume and that selected volume is physically diffuse.

## 5. Signs, degeneracies, and law scope

- `N` may be rectangular, singular, have repeated singular values, or have arbitrary rank. The selected-volume identities use squared singular values only.
- No sign condition is imposed on `A`, its hub diagonal, same-side leaf blocks, or any extra spectral component.
- Every input coordinate may have an arbitrary, fragmented, unbounded-support probability density satisfying only `0<=f_i<=1`; the inputs need not be centered, iid, continuous, symmetric, log-concave, or compactly supported.
- The random input is never rotated. `P_2,Q_2` occur only in deterministic coefficient identities. The analytic theorem is applied to literal physical cross matrices `[u,N]` and `[v,N^T]`.
- Alternative (B) is an aggregate physical-anchor statement, not a claim that one physical minor is large.
- Alternative (C) does not perturbatively remove the `3E/64` tail; it records its exact norm and keeps it in the remaining theorem.
- Continuity follows only in alternative (A) from the peer theorem's `L^1` characteristic-function conclusion. Full-target continuity remains open.

## 6. Next inequality

The strongest next target exposed by this run is a three-block, product-preserving core inequality:

`QFORM-STAR4-ALIGNED-2x2-CORE-WITH-TAIL-v1`.

Given independent original-coordinate blocks `{h}`, `J`, `K`, arbitrary cap-one laws, an exact leaf cross `N` with

`sum_(r>=3)s_r(N)^2<3||N||_F^2/64`,

and star vectors whose squared projections onto the top-two left/right singular spaces are each `>3beta/4`, prove a universal density bound while retaining the cross tail and arbitrary `J--J`, `K--K`, hub and affine curvature. A valid proof may use the two block-projection densities as complex amplitudes, but must not assert independence of singular coordinates or take a worst conditional fiber. The alternative aggregate-anchor state should be attacked by the current second-anchor/grouped-Schur machinery before any reciprocal local-minor selection.

No full-solution claim is made. The target remains OPEN / NOT PROVED / NOT DISPROVED.
