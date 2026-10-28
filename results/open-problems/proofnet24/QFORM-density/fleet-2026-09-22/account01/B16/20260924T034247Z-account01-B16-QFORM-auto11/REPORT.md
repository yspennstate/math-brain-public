SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-24T03:42:47.621071Z.
attacking: the innovation-free majority-sign physical-hub branch; keep the same original leaf sources through the hyperbolic discriminant and look for a TT*/Hilbert receiver uniform as the nonzero hub pivot tends to zero.

# account01/B16 — conditional pair-log + genuine square smoothing closes the authentic hyperbolic stress packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T034247Z-account01-B16-QFORM-auto11`  
**Role:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + AUTHENTIC MAJORITY-SIGN STRESS FAMILY CLOSED + NEWEST PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** essential boundedness and absolute continuity are proved on the new branch; continuity is not claimed by this argument and remains separate.

## 1. Fresh scope, corrections and source pins


The full statement remains OPEN: arbitrary independent original-coordinate inputs with probability densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, arbitrary signs and additional spectrum, no moment/support/iid/log-concavity assumptions, and no independence after spectral rotation.

The proof below preserves the live corrections:

- a bounded joint projection density is **not** used as an indefinite coarea bound;
- a conditional projection-height cap is **not** inferred from a marginal projection cap;
- no post-rotation coordinate independence is asserted;
- no law-uniform pointwise quadratic Fourier decay is used;
- the authentic account03/B16 r38 logarithmic divergence of the positive hub-first half-trace is accepted and explicitly bypassed rather than contradicted.

Source pins actually used:

1. Physical-pair logarithmic envelope, `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, full proof at
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
2. Newest completed designated partner account02/B16, `QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1`, report commit
   `390bf6a9ad30195ba4011927c8218245d0e014be`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260924T012413Z-account02-B16-QFORM-auto11/REPORT.md`.
3. Authentic majority-sign stress packet account03/B16 r38,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T005411Z-account03-B16-QFORM-r38/REPORT.md`.
4. The actual product-projection theorem used throughout B16: for a full-row-rank `k x n` coefficient matrix `T` and an independent cap-one product vector `X`,
   `||p_(TX)||_infinity <= 2^(k/2)/sqrt(det(TT^T))`.

The key new idea is to group the variables differently from the failed literal-hub half-trace. Instead of integrating the physical hub first and then facing the positive hyperbolic kernel `(4U^2-aV^2)_+^(-1/2)`, keep the fresh hub inside `Y=gamma H+S`, treat `(Y,U)` as an **indefinite physical pair**, retain its logarithmic singularity, and average that logarithm against a genuine third square `V^2`. The fresh hub supplies a valid conditional cap for `Y|V` even when `S` and `V` share sources.

## 2. Fresh-source conditional cap that survives dependence

Let the following three **original source blocks** be mutually independent:

- a scalar `H` with density cap `L_H`;
- a scalar receiver `U` with density cap `K_U`;
- an arbitrary source block producing a pair `(S,V)`, where `S` and `V` may be fully dependent, and the `V` marginal has density cap `K_V`.

Fix `gamma!=0` and put

`Y=gamma H+S`.                                                     (2.1)

Let `mu_v` be a regular conditional distribution of `S` given `V=v`. Because `H` is independent of the whole `(S,V)` source block, for almost every `v`,

`p_(Y|V=v)(y)
 = int |gamma|^(-1) f_H((y-s)/gamma) mu_v(ds)
 <= L_H/|gamma|.`                                                 (2.2)

Define

`A_0:=L_H/|gamma|`.                                                (2.3)

Equation (2.2) is the crucial dependence-safe interface. It is a convolution with a genuinely untouched source. It does **not** say that conditioning a generic projection preserves its marginal density cap. Moreover, because the entire `U` source block is disjoint from `(H,S,V)`, conditional on `V=v`, `U` remains independent of `Y` and retains its cap `K_U`.

## 3. New theorem: conditional pair-log plus square smoothing

Consider

`Q = aY^2+2 beta YU+rY+sU+lambda V^2+dV+c`,                       (3.1)

where

`beta!=0`, `lambda!=0`.                                           (3.2)

Set

`A=A_0`, `B=K_U`.                                                  (3.3)

For the pair scaling `x=AY`, `z=BU`, define

`M_0 = [[a/A^2, beta/(AB)], [beta/(AB),0]]`.                       (3.4)

This matrix is always invertible and indefinite. Put

`kappa_0:=sigma_min(M_0)
 = (sqrt((a/A^2)^2+4(beta/(AB))^2)-|a|/A^2)/2 >0`.                (3.5)

### `QFORM-FRESH-HUB-CONDITIONAL-PAIRLOG-SQUARE-v1`

Under the hypotheses above, `Q` has an absolutely continuous law and

`boxed:
 ||p_Q||_infinity
 <= 8 sqrt(2) K_V / sqrt(kappa_0 |lambda|)
    + 2 A B/|beta|.
`                                                                    (3.6)

In particular, the bound remains finite as `a ->0`; indeed

`kappa_0 -> |beta|/(AB)`.                                         (3.7)

Thus a vanishing nonzero physical-hub pivot is harmless on this branch even when the literal-hub discriminant is hyperbolic and even when the longitudinal shared variable `S` is dependent on the square smoother `V`.

## 4. Proof

Fix `v` outside a null set for the conditional law. By Section 2, `Y|V=v` and `U` are independent, with density caps `A` and `B`. Therefore

`X:=AY`, `Z:=BU`                                                   (4.1)

are independent and each has density cap one. Conditional on `V=v`, the `(Y,U)` part of (3.1) is a fixed affine perturbation of the indefinite pair with matrix `M_0`.

The completed physical-pair logarithmic theorem therefore gives, for every cutoff `R>0`, a conditional density representative

`p_(pair|V=v)(t)
 <= 2 sqrt(2)/R
    + |det M_0|^(-1/2)
      log_+(2R^2/(kappa_0 |t-t_0|)).`                              (4.2)

The critical value `t_0` depends only on the fixed affine pair coefficients in (3.1), not on `v`. Since

`|det M_0| = beta^2/(A^2B^2)`,                                    (4.3)

we have

`|det M_0|^(-1/2)=AB/|beta|`.                                     (4.4)

It remains to average the logarithmic singularity against the scalar quadratic in `V`.

### Scalar quadratic small-ball lemma

For every `lambda!=0`, every real `d,e,q`, and every `rho>0`,

`Leb{v: |lambda v^2+d v+e-q|<rho}
 <= 2 sqrt(2 rho/|lambda|).`                                      (4.5)

Proof: complete the square. It suffices to bound

`Leb{x: |x^2-q'|<eta}`.

If `q'<=-eta`, the set is empty. If `-eta<q'<eta`, it is contained in `|x|<sqrt(2eta)`, of length at most `2sqrt(2eta)`. If `q'>=eta`, its total length is

`2[sqrt(q'+eta)-sqrt(q'-eta)]
 =4eta/[sqrt(q'+eta)+sqrt(q'-eta)]
 <=2sqrt(2eta).`                                                   (4.6)

This proves (4.5).

Since `p_V<=K_V`, (4.5) gives

`P(|lambda V^2+dV+e-q|<rho)
 <= min(1, 2sqrt(2) K_V sqrt(rho/|lambda|)).`                      (4.7)

For `C>0`, layer cake yields

`E log_+(C/|lambda V^2+dV+e-q|)
 = int_0^infinity
   P(|lambda V^2+dV+e-q|<C exp(-u)) du`.                           (4.8)

Writing

`z=2sqrt(2)K_V sqrt(C/|lambda|)`,                                 (4.9)

the right side is at most

`J(z):=int_0^infinity min(1,z exp(-u/2)) du`,                      (4.10)

where explicitly

`J(z)=2z` for `0<=z<=1`,
`J(z)=2+2log z` for `z>=1`.                                       (4.11)

Now average (4.2) over `V`, with

`C=2R^2/kappa_0`.                                                  (4.12)

By (4.9),

`z = 4K_V R/sqrt(kappa_0 |lambda|).`                              (4.13)

Choose

`R_* = sqrt(kappa_0 |lambda|)/(4K_V)`.                            (4.14)

Then `z=1`, hence `J(z)=2`. Substitution into (4.2) gives, uniformly in the output level,

`p_Q(q)
 <= 2sqrt(2)/R_* + 2AB/|beta|`
` = 8sqrt(2)K_V/sqrt(kappa_0|lambda|)+2AB/|beta|`.                (4.15)

This proves (3.6). The conditional pair theorem already gives conditional absolute continuity, and averaging those conditional densities gives absolute continuity of `Q`. No continuity claim is made here. QED.

## 5. Why this is a genuine projection-product theorem

The proof uses three different pieces of source information at the correct stage:

1. **fresh original source:** the cap on `H` is retained inside the conditional convolution (2.2), producing a true cap on `Y|V` despite arbitrary dependence of `S` and `V`;
2. **bounded-density projection theorem:** `K_U` and `K_V` may be supplied by actual product projections, with no claim that any coordinates within a multidimensional projection are independent;
3. **nonlinear quadratic integration:** the indefinite `(Y,U)` pair is not bounded pointwise at its critical value; its logarithmic singularity is retained and only then integrated against the genuine square small-ball profile of `V`.

This directly avoids the correction that a bounded two-dimensional joint projection density alone does not control an indefinite half-level-set integral.

## 6. Strict target family with shared projection dependence

Let `H` and `U` be two literal independent original coordinates, each with density cap one. Let `W` be a disjoint independent product source block, and choose two orthonormal coefficient vectors `s,v` in that block. Put

`S=s^T W`, `V=v^T W`, `Y=H+S`.                                  (6.1)

No independence is assumed between `S` and `V`. The actual one-dimensional product-projection theorem gives

`K_V<=sqrt(2)`.                                                    (6.2)

For

`Q_a=aY^2+2YU+V^2`,                                               (6.3)

we have `A=B=1`, `beta=lambda=1`, and

`kappa_0=(sqrt(a^2+4)-|a|)/2`.                                   (6.4)

Therefore

`||p_(Q_a)||_infinity
 <= 16/sqrt(kappa_0)+2`.                                          (6.5)

For `0<=a<=1/2`,

`kappa_0 >= (sqrt(17)-1)/4 =0.7807764064...`,                     (6.6)

so

`boxed: ||p_(Q_a)||_infinity <20.108.`                            (6.7)

This is a strict owner-target family. In the orthonormal carrier basis

`y_hat=(H+S)/sqrt(2), U, V`,

the nonzero coefficient matrix is

`[[2a,sqrt(2),0],[sqrt(2),0,0],[0,0,1]]`.                         (6.8)

Its eigenvalues are

`a+sqrt(a^2+2)`, `a-sqrt(a^2+2)`, `1`.                            (6.9)

For `0<=a<=1/2`, the negative eigenvalue has modulus at least one because

`sqrt(a^2+2)-a>=1 <=> a<=1/2`,                                   (6.10)

and the positive one is larger than one. Thus all three displayed eigenvalues have modulus at least one. The family genuinely tests the intended interface: `S,V` can be highly dependent projections of the same product bank, yet the density stays uniformly bounded through `a=0` by the source-preserving argument above.

## 7. The authentic account03/B16 r38 majority-sign stress packet is now uniformly paid

The account03/B16 r38 family is

`Q_a=aY^2+4YU+V^2`,
`Y=sqrt(c)X_0+S`,
`c=127/128`, `0<a<2^-14`.                                        (7.1)

All physical inputs are independent cap-one uniforms, the matrix has exactly three eigenvalues of modulus at least one, the literal-hub discriminant is hyperbolic, and the positive hub-first half-trace diverges logarithmically as `a downarrow0`.

Apply the new theorem instead. The one-dimensional actual projection theorem gives

`K_U<=sqrt(2)`, `K_V<=sqrt(2)`.                                  (7.2)

Here

`A=c^(-1/2)`, `B=sqrt(2)`, `beta=2`, `lambda=1`.                  (7.3)

Consequently

`kappa_0
 = [sqrt((ac)^2+8c)-ac]/2`.                               (7.4)

Over `0<a<2^-14`,

`kappa_0>1.40864817`.                                             (7.5)

Substitution into (3.6) gives

`boxed: ||p_(Q_a)||_infinity <14.901`                             (7.6)

**uniformly through the entire punctured collar**.

This is an actual mathematical bridge across the partner's hyperbolic interface obstruction. The r38 logarithmic divergence remains correct: it is the divergence of the lossy **positive literal-hub root trace**. The new grouping keeps the fresh hub inside `Y`, retains the true indefinite pair logarithm rather than replacing it by a half-power kernel, and pays that logarithm with the genuine third square. Thus the obstruction is bypassed without claiming it was false.

The r38 source packet is therefore no longer a surviving B16 stress example for density height. The full QFORM problem is still open because a generic near-coloop survivor need not reduce to (3.1) with a quantitatively nonzero third-square coefficient after preserving all same-bank curvature and additional spectrum.

## 8. Newest designated partner account02/B16 applied to an actual inequality

The newest completed partner theorem at commit `390bf6a9ad30195ba4011927c8218245d0e014be` says: if `H` is a fresh cap-one hub, `Z=(U,V)` is an orthonormal two-dimensional product projection of a disjoint source block, and

`Q=(H,U,V)^T B(H,U,V)+affine`,

then whenever the literal hub diagonal `a=B_11` satisfies

`a det B>0`,                                                       (8.1)

one has

`||p_Q||_infinity <=2sqrt(2pi)(a det B)^(-1/4)`.                  (8.2)

Apply this to the actual matrix

`B_*=[[-1,1,0],[1,1,0],[0,0,1]].`                                (8.3)

Its spectrum is

`{-sqrt(2),sqrt(2),1}`,                                           (8.4)

so it is a strict target matrix. Moreover

`det B_*=-2`, `a=-1`, `a det B_*=2>0`.                            (8.5)

Therefore, for arbitrary cap-one physical input laws,

`boxed:
 ||p_(-H^2+2HU+U^2+V^2)||_infinity
 <=2sqrt(2pi) 2^(-1/4)
 =4.2156294611... .
`                                                                    (8.6)

This is a literal use of the completed designated-partner theorem at an actual target inequality. Any independent quadratic direct-sum block on additional original coordinates can be convolved afterward without increasing this height.

## 9. What remains open after this run

The first B16 obstruction is now narrower than `QFORM-PUNCTURED-MAJORITY-HUB-TTSTAR-v1`. The canonical source-authentic family used to demonstrate the hyperbolic positive-trace loss is actually bounded by `<14.901` once the variables are regrouped as an indefinite pair plus a genuine square.

The remaining implication is:

### `QFORM-GENERIC-MAJORITY-HUB-PAIRLOG-SQUARE-REDUCTION-v1` — OPEN

For every remaining majority-sign true-near-coloop configuration, force one of the already paid exits, or preserve original product provenance while reducing to an indefinite physical/source pair whose logarithmic critical singularity is smoothed by a scalar quadratic direction with a universal nonzero coefficient and a bounded marginal density. If generic same-bank curvature produces `YV`, `UV`, or nonseparable light-block quadratic terms, either complete them without destroying the fresh-source conditional cap or build the corresponding vector-valued pair-log receiver.

A generic bounded joint projection density is not enough. The new theorem works because the fresh physical hub yields the exact conditional cap (2.2) and the remaining scalar square retains a genuine one-dimensional small-ball profile. Arbitrary additional spectrum and generic nonseparable same-bank curvature remain the structural debt.

No full-solution claim is made. The full unrestricted QFORM theorem and global continuity remain OPEN.
