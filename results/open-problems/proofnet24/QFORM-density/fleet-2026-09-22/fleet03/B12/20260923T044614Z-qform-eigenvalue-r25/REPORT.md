SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T04:46:14Z.
attacking: full nonseparable spectral tails at matrix level via the newest three-volume stability estimate plus the fleet04/B12 dependence-safe mixed-norm shear compiler.

# fleet03/B12 r25 — cross-footprint stability with an explicit continuity modulus

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN  
**Continuity:** proved in the stated branches below; full-target continuity remains open  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Scope and current correction boundary

Let `X=(X_1,...,X_n)` have independent real coordinates, each with a probability density bounded by one. No moments, bounded support, connected support, log-concavity, identical laws, centering or Gaussianity are assumed. Let `A=A^T` be arbitrary.

This report proves a matrix-level stability theorem for adding arbitrary further quadratic spectrum once a protected ORIGINAL-coordinate cross-volume certificate is present. It does **not** prove that the bare hypothesis `s_3(A)>=1` always supplies such a certificate, so the full conjecture remains open.

The proof uses no spectral-coordinate independence, no law-uniform pointwise van-der-Corput estimate, no arbitrary-joint rank-three coarea estimate, no worst conditional-fiber supremum, and no interpretation of a small matrix norm as a small random quadratic perturbation on unbounded inputs.

The two completed inputs actually used are:

1. **Newest three-volume stability package.**  
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,  
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md`.

   Its q=`4/3` Fourier proof gives, for a physical cross block `M`, a uniform characteristic-function envelope with exponent `9/8` whenever the volume-marginal gate holds. In the near-diffuse perturbative branch

       M=M0+E,
       s3(M0)>=a>0,
       max_i (P_Range(M0))_ii<=1/2,
       ||E||op<=a/16,                                           (1.1)

   it proves a continuous density `<23/a`, retaining arbitrary self blocks, outside couplings and affine terms. Its collective-tail extension replaces a third substantial singular value by the total squared tail `T2=sum_(j>=3)s_j(M)^2` under its stated projection gate.

2. **Designated partner fleet04/B12 mixed-norm shear compiler.**  
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260922T192552Z-fleet04-B12-mixed-shear-r1/REPORT.md`.

   For a joint density `h(u,z)`, define

       M(h)=int esssup_u h(u,z) dz,
       Omega_h(d)=int esssup_u |h(u+d,z)-h(u,z)| dz.             (1.2)

   Then every measurable shear `U+psi(Z)` satisfies

       ||p_(U+psi(Z))||inf <= M(h),                              (1.3)
       ||p_(U+psi(Z))(.+d)-p_(U+psi(Z))||inf <= Omega_h(d).      (1.4)

   No independence of `U` and `Z` is required.

The new contribution is an explicit, uniform `Omega_h` obtained from the newest volume theorem, and its conversion into a quantitative additional-eigenvalue theorem. The prior volume report proves continuity, but it does not record this dependence-safe uniform translation modulus or the matrix cross-footprint formulation below.

## 2. Fourier envelope and the intrinsic frequency scale

Take disjoint ORIGINAL coordinate sets `I,J`. Condition on all remaining original coordinates `Z=z`. Since this is conditioning in the product basis, the active coordinates in `I union J` retain their original independence and density caps. All `z`-dependence enters as affine terms and constants, while the physical cross block `M=A[I,J]` is unchanged.

Under (1.1), the newest volume theorem applies uniformly in `z`. Its q=`4/3` proof gives

    |phi_z(t)| <= min(1,K |t|^(-b)),
    b=9/8,                                                        (2.1)

where

    K=[e^3 q^(-3/2) pi^3 Z3^(-1/2)]^(1/(2q)),
    q=4/3,
    Z3=e3(M^T M).                                                 (2.2)

Introduce the natural crossover scale

    T:=K^(1/b)=K^(8/9)
      = e*pi/sqrt(q) * Z3^(-1/6)
      = (e*pi*sqrt(3)/2) Z3^(-1/6).                              (2.3)

The perturbation theorem gives

    kappa:=s3(M)>=15a/16,
    Z3^(1/6)>=kappa,                                              (2.4)

hence

    T <= T_a:=8 e pi sqrt(3)/(15a)
       = 7.888668563629508.../a.                                 (2.5)

Integrating (2.1) gives the familiar density bound

    ||p_z||inf <= (1/pi)[T+K int_T^infinity t^(-9/8)dt]
               = 9T/pi
               <= 24 sqrt(3)e/(5a)
               = 22.59937073367501.../a
               <23/a.                                           (2.6)

The important point for B12 is that (2.1) is uniform over every affine perturbation generated by the outside coordinates. We now retain that uniformity quantitatively instead of merely averaging the cap.

## 3. New lemma: explicit Holder translation modulus from the 9/8 envelope

### Lemma 3.1

Suppose a real random variable has characteristic function satisfying

    |phi(t)|<=min(1,K|t|^(-9/8)),

and put `T=K^(8/9)`. Then its continuous density satisfies, for every real `d`,

    ||p(.+d)-p||inf
      <= [135/(7pi)] T min{1,(T|d|)^(1/8)}.                      (3.1)

### Proof

Fourier inversion and `|e^(-itd)-1|<=2 min(1,|t d|)` give

    ||p(.+d)-p||inf
      <= (2/pi) J(d),                                           (3.2)

where

    J(d)=int_0^infinity min(1,t|d|) min(1,Kt^(-b)) dt,
    b=9/8.                                                       (3.3)

First suppose `|d|T<=1`. Split the integral at `T` and `1/|d|`:

    J(d)
    <= |d|T^2/2
       +K|d| int_T^(1/|d|) t^(1-b)dt
       +K int_(1/|d|)^infinity t^(-b)dt.                         (3.4)

Since `K=T^b` and `|d|T<=1`,

    |d|T^2/2 <= (1/2)K |d|^(b-1).                               (3.5)

The other two terms are bounded by

    K |d|^(b-1)/(2-b),
    K |d|^(b-1)/(b-1).                                          (3.6)

At `b=9/8`,

    1/2 + 1/(2-b) + 1/(b-1)
      =1/2+8/7+8
      =135/14.                                                   (3.7)

Therefore

    J(d)<= (135/14)K |d|^(1/8)
         = (135/14)T(T|d|)^(1/8),                               (3.8)

which inserted in (3.2) proves (3.1) when `|d|T<=1`.

If `|d|T>=1`, then

    ||p(.+d)-p||inf<=2||p||inf<=18T/pi.                          (3.9)

Since `18<135/7`, (3.1) again follows. This proves the lemma. `square`

Applying (3.1) to every conditional density `p_z` and using (2.5) yields the uniform estimate

    boxed:
    ||p_z(.+d)-p_z||inf
      <= [72 e sqrt(3)/(7a)]
         min{1,[T_a |d|]^(1/8)},                                (3.10)

where

    72 e sqrt(3)/7=48.427223000732155... .                       (3.11)

Thus the near-diffuse three-volume branch carries a quantitative uniform Holder-`1/8` modulus, not merely an `L^infinity` cap.

## 4. Designated partner application: arbitrary dependent outside spectral remainder

Write the full quadratic form after the original-coordinate split as

    Q = U + psi(Z),                                              (4.1)

where `U` contains every term involving at least one active coordinate from `I union J`, including all `Z`-induced affine terms, while `psi(Z)` contains the outside-only part. For a quadratic form, `psi(Z)` includes the complete outside quadratic block, but the argument below allows **any measurable** `psi`.

Let `p_z(u)` be the conditional density of `U` given `Z=z`. The Fourier construction above gives a jointly measurable version; define

    h(u,z)=p_Z(z)p_z(u).                                         (4.2)

From (2.6),

    M(h)=int p_Z(z)||p_z||inf dz
        <=24 sqrt(3)e/(5a)<23/a.                                (4.3)

More importantly, (3.10) gives

    Omega_h(d)
      =int p_Z(z) esssup_u |p_z(u+d)-p_z(u)| dz
      <=[72 e sqrt(3)/(7a)]
        min{1,[T_a|d|]^(1/8)}.                                  (4.4)

Now apply the completed **fleet04/B12** theorem (1.3)-(1.4) to the actual joint density (4.2). For every measurable outside remainder `psi`, including an arbitrary dependent quadratic remainder,

    boxed:
    ||p_(U+psi(Z))||inf
       <=24 sqrt(3)e/(5a)<23/a,                                 (4.5)

and

    boxed:
    ||p_(U+psi(Z))(.+d)-p_(U+psi(Z))||inf
       <=[72 e sqrt(3)/(7a)]
          min{1,[(8e pi sqrt(3)/(15a))|d|]^(1/8)}.              (4.6)

In particular the final density is bounded and uniformly continuous, indeed globally Holder-`1/8` at small scales with the displayed modulus. This is an equation-level application of the designated partner result. No convolution and no independence between `U` and `psi(Z)` is asserted.

## 5. Matrix-level additional-eigenvalue theorem

The previous calculation has a useful formulation directly in terms of a final coefficient matrix.

### Theorem 5.1 — `QFORM-CROSS-FOOTPRINT-SHEAR-HOLDER-STABILITY-v1`

Let `I,J` be disjoint sets of original coordinates. Suppose there is a matrix `M0` such that

    s3(M0)>=a>0,
    max_i(P_Range(M0))_ii<=1/2,                                 (5.1)

and the **final** cross block of `A` obeys

    ||A[I,J]-M0||op<=a/16.                                      (5.2)

Then for every cap-one independent product input, the full quadratic form `X^T A X` has a bounded uniformly continuous density satisfying (4.5)-(4.6).

Every other entry of the final symmetric matrix is unrestricted. In particular:

- both active self blocks `A[I,I]` and `A[J,J]` are arbitrary;
- all couplings from `I,J` to the outside coordinates are arbitrary;
- the outside block `A[Z,Z]` is arbitrary;
- the number, signs, sizes, multiplicities and degeneracies of all additional eigenvalues are arbitrary.

Thus a full nonseparable spectral tail is charged **only through its actual footprint on the protected physical cross block**. There is no moment assumption and no claim that the extra quadratic form is a small random variable.

### Proof

Set `M=A[I,J]`, `E=M-M0`. Then (5.1)-(5.2) are exactly the newest volume-stability hypotheses. Condition on the outside original coordinates, apply Sections 2-3 uniformly, and then restore the entire outside-only remainder through the fleet04/B12 shear theorem as in Section 4. `square`

This formulation is stronger than a statement about a low-rank perturbation: one may alter the entire ambient matrix arbitrarily while keeping only the protected cross block within the stated tolerance.

## 6. Arbitrarily large signed added eigenvalues with small cross footprint

Let a baseline protected cross block be `M0`, and add an arbitrary symmetric spectral packet

    R=sum_r tau_r v_r v_r^T.                                    (6.1)

Its perturbation on the `I x J` cross block is

    R[I,J]=sum_r tau_r (v_r)_I (v_r)_J^T.                        (6.2)

Since a rank-one matrix `uv^T` has operator norm `||u||_2||v||_2`,

    ||R[I,J]||op
      <=sum_r |tau_r| ||(v_r)_I||_2 ||(v_r)_J||_2.               (6.3)

Therefore the sufficient condition

    sum_r |tau_r| ||(v_r)_I||_2 ||(v_r)_J||_2 <=a/16            (6.4)

preserves (4.5)-(4.6), regardless of the signs or individual magnitudes `|tau_r|`.

This is the requested large/small eigenvalue stability in a precise matrix-level sense: an added eigenvalue may be arbitrarily large if its cross-cut product leverage is correspondingly small. Any added direction supported wholly on one side of the protected cut, or wholly outside it, has zero cross footprint and costs exactly zero. More generally, an arbitrary symmetric perturbation `R` with `R[I,J]=0` costs zero even if its eigenvectors themselves are globally mixed and its spectral norm is arbitrarily large.

The theorem does **not** say that every arbitrary added matrix has small cross footprint. That would be false as a stability statement without a surviving certificate; the correct price is the final physical cross geometry, not the eigenvalue list alone.

## 7. Collective-tail version: two strong cross directions plus many weak ones

The same continuity compiler applies to the newest collective-tail theorem. Let

    T2=sum_(j>=3)s_j(M)^2,
    G=[s1(M)^2 s2(M)^2 T2]^(1/6).                               (7.1)

Suppose there is an orthogonal row-space projection `P` satisfying

    max_i P_ii<=1/2,
    ||(I-P)M||op<=sqrt(T2)/15.                                  (7.2)

The tail extension proves the same q=`4/3`, b=`9/8` envelope with

    Z3^(1/6)>=G.                                                 (7.3)

Hence the crossover frequency obeys

    T<=T_G:=e*pi*sqrt(3)/(2G)
          =7.395626778402664.../G.                              (7.4)

The density cap is

    boxed:
    ||p_Q||inf <=(9sqrt(3)e)/(2G)
                =21.186910062820317.../G,                       (7.5)

and the same argument plus fleet04/B12 yields, after every measurable dependent outside shear,

    boxed:
    ||p_Q(.+d)-p_Q||inf
      <=[135 e sqrt(3)/(14G)]
        min{1,[(e*pi*sqrt(3)/(2G))|d|]^(1/8)},                  (7.6)

where

    135 e sqrt(3)/14=45.400521563186395... .                     (7.7)

This version is especially relevant to "additional eigenvalues": the third smoothing scale may be the **collective energy of arbitrarily many individually vanishing singular directions**, rather than one separately large third cross singular value. The proof pays the matrix tail before any reciprocal single-direction cost.

## 8. Relation to the preceding B12 reduction

The preceding B12 run proved that a target with at least four eigenvalues beyond a scale `L` either exits through a physical pair/ridge branch or reduces after at most one original-coordinate scalar Schur step to a residual with

    N_abs(S;L)>=3,
    |S_jj|<0.17L,
    |det S[{i,j}]|<0.0289L^2,

and a concentrated `L/256` spectral window.

The present theorem supplies a **continuous-density exit** from that residual whenever an original-coordinate cut admits either:

1. a near-diffuse rank-three cross packet satisfying (5.1)-(5.2); or
2. a two-direction-plus-collective-tail packet satisfying (7.1)-(7.2).

All remaining spectrum is retained exactly. What is still missing is an exhaustive theorem proving that every residual outside these exits must fall into one of the other already-paid grouped-bank/hub mechanisms. The singleton-plus-two-banks family and the known low-cross-rank examples show why one cannot simply assert a universal well-conditioned rank-three cross cut.

## 9. Computation and exact constants

`CHECK.py` verifies the exact exponent arithmetic

    b=9/8,
    1/2+1/(2-b)+1/(b-1)=135/14,                                 (9.1)

and checks that the large-translation estimate `18T/pi` is dominated by `135T/(7pi)`. The numerical constants are recorded in `CHECK_RESULT.json`:

    T_a coefficient                  7.888668563629508
    near-diffuse density /a         22.59937073367501
    near-diffuse modulus /a         48.427223000732155
    T_G coefficient                  7.395626778402664
    collective-tail density /G      21.186910062820317
    collective-tail modulus /G      45.400521563186395.          (9.2)

These computations are sanity checks. The proof is the exact Fourier integral calculation in Section 3.

## 10. Status, continuity, and remaining full-target implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The bare condition of three eigenvalues of modulus at least one has not yet been shown to force the protected cross-volume or collective-tail certificate used here.

Within the precise scopes of Theorem 5.1 and Section 7, however, this run proves more than essential boundedness: the final density remains bounded and uniformly continuous after arbitrary dependent outside quadratic completion, with an explicit uniform Holder-`1/8` modulus. This directly closes the continuity debt for these added-spectrum branches.

The next B12 implication is structural rather than a new perturbative estimate: in the surviving low-pivot/high-leverage class, prove an exhaustive grouped-coordinate alternative that either produces a protected cross-volume/collective-tail certificate of the present type or lands in a completed low-cross-rank/hub/bank theorem, without selecting one tiny physical minor and without discarding the nonseparable tail.

## Provenance


Repository access and native learned-memory ingestion are separate. This run remains `WITHOUT_VERIFIED_BRAIN`.
