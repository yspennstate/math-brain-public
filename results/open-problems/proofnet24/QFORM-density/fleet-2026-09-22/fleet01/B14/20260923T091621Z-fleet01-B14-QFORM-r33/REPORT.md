SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T09:16:21Z.
attacking: critical-Fourier perspective localization—retain unnormalized fragment mass through the partner logarithmic kernel, then optimize the completed fleet02/B14 r32 inequality on a target-valid kernel-leakage family.

# QFORM B14 r33 — perspective localization for critical Fourier fragments

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** fleet01/B14  
**Run:** 20260923T091621Z-fleet01-B14-QFORM-r33  
**Status:** PROVED SUPPORTING LOCALIZATION THEOREM + SHARPENED TARGET-VALID PARTNER APPLICATION; FULL QFORM OPEN.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Purpose and exact scope

The completed fleet02/B14 r32 theorem converts a whole-bank critical Fourier estimate `|phi_R(t)| <= min(1,K/|t|)` into a logarithmic-potential bound, and then passes that through an indefinite physical pair. Its statement uses one uniform `K`. The localization issue is what happens when a law is decomposed into remote fragments or outside fibers whose normalized critical constants vary or blow up.

The result below shows that one must keep the fragments as unnormalized subprobabilities. The logarithmic compiler is the perspective of a concave function, so the only quantity paid after mixing is the sum of the unnormalized critical Fourier constants. Fragment count, support diameter, fragment separation, translations, and moments do not appear. This is a supporting proof interface, not a proof of the unrestricted conjecture.

## 2. Source-pinned completed partner theorem

Consumed completed fleet02/B14 r32: `yspennstate/math-open-problems@bce23e5a745fec8ac0f3b1c5e1eb2d917885c437`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T090605Z-fleet02-B14-QFORM-r32/REPORT.md`.

Its critical Fourier lemma defines

`c_E = 1/[2 sin^2(1/2)] = 2.175342649670021...`

and

`Omega(y) = c_E y [2+log(1/y)]`, `0<y<=1`,
`Omega(y) = log y + 2 c_E`, `y>=1`.

If a probability law `mu` satisfies `|hat mu(t)| <= min(1,K/|t|)`, then, for every `A>0`,

`sup_x int log_+(A/|x-r|) dmu(r) <= Omega(KA)`.                 (2.1)

After an invertible indefinite physical pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`, r32 gives

`||p_Q||_infinity <= inf_{y>0}{4 sqrt(K/(kappa y)) + D^(-1/2) Omega(y)}`.  (2.2)

For a diffuse rank-two Schur bank with nonzero eigenvalue product `P`, r32 has `K=4 pi/sqrt(P)`. No post-rotation independence is used in that source.

## 3. Concavity of the logarithmic compiler

### Lemma 3.1 — `QFORM-OMEGA-CONCAVE-v1`

`Omega` is increasing and concave on `(0,infinity)`.

For `0<y<1`, `Omega'(y)=c_E(1-log y)` and `Omega''(y)=-c_E/y<0`. For `y>1`, `Omega'(y)=1/y` and `Omega''(y)=-1/y^2<0`. At `y=1`, both pieces equal `2c_E`; the left derivative is `c_E` and the right derivative is `1`. Since `c_E>1`, the derivative has a downward jump. Hence the glued function is globally concave and increasing.

## 4. New subprobability perspective theorem

### Theorem 4.1 — `QFORM-CRITICAL-FOURIER-SUBPROB-PERSPECTIVE-v1`

Let `nu` be a finite positive measure on the line with mass `m in [0,1]`, and suppose

`|hat nu(t)| <= min{m,K/|t|}`                                      (4.1)

for every `t!=0`. Then for every `A>0`,

`sup_x int log_+(A/|x-r|) dnu(r) <= m Omega(AK/m)`             (4.2)

with the right side interpreted as zero for `m=0`.

Proof: for `m>0`, normalize `mu=nu/m`. Then `|hat mu(t)| <= min{1,(K/m)/|t|}`. Apply the completed partner lemma (2.1) with critical constant `K/m`, then multiply by `m`.

## 5. Exact mixture/localization theorem

### Theorem 5.1 — `QFORM-CRITICAL-FOURIER-MIXTURE-LOCALIZATION-v1`

Let `nu=sum_alpha nu_alpha` be a finite or countable sum of positive subprobability measures, with masses `m_alpha`, total mass `M=sum_alpha m_alpha<=1`, and suppose

`|hat nu_alpha(t)| <= min{m_alpha,K_alpha/|t|}`                    (5.1)

for every `alpha` and `t!=0`. Put `K_Sigma=sum_alpha K_alpha`. Then for every `A>0`,

`sup_x int log_+(A/|x-r|) dnu(r)
 <= M Omega(A K_Sigma/M).`                                         (5.2)

For a probability mixture `M=1`,

`sup_x int log_+(A/|x-r|) dnu(r) <= Omega(A K_Sigma).`             (5.3)

Proof: apply Theorem 4.1 componentwise and then Jensen to the concave `Omega` with weights `m_alpha/M`:

`sum m_alpha Omega(A K_alpha/m_alpha)
 <= M Omega(A sum K_alpha/M)`.

Countable sums follow by monotone convergence.

If each component is only an outside fragment of mass `m_alpha`, while the active whole-bank theorem has the same normalized critical constant `K_0` on every outside realization, then `K_alpha=m_alpha K_0` and therefore `K_Sigma=K_0`. Thus arbitrary outside fragmenting is exactly zero-loss. More generally, the compiler pays only `sum K_alpha`, not `sup(K_alpha/m_alpha)` and not the number of fragments.

## 6. Physical-pair compiler with averaged critical cost

Combine Theorem 5.1 with r32. If the full remainder probability law admits a decomposition satisfying (5.1) with total critical cost `K_Sigma`, then

`||p_Q||_infinity
 <= inf_{y>0}{4 sqrt(K_Sigma/(kappa y)) + D^(-1/2) Omega(y)}`.       (6.1)

Indeed take `A=2r^2/kappa` in (5.3), insert it into the physical-pair envelope, and set `y=2 K_Sigma r^2/kappa`.

This is the same functional form as r32, but the required input is now an additive unnormalized critical budget over arbitrary localization pieces rather than one worst normalized fiber constant.

## 7. Exact optimization in the logarithmic branch

For r32's diffuse rank-two bank, put

`P=|lambda_1 lambda_2|`,
`beta = 8 sqrt(pi D/kappa) P^(-1/4)`.                              (7.1)

Then

`||p_Q||_infinity
 <= D^(-1/2) inf_{y>0}{ beta y^(-1/2)+Omega(y) }`.                 (7.2)

When `beta>=2`, equivalently `16 pi D/(kappa sqrt(P))>=1`, the stationary point in the branch `y>=1` is

`y_*=(beta/2)^2=16 pi D/(kappa sqrt(P))`.                          (7.3)

At that point the first term equals `2`, so

`||p_Q||_infinity
 <= D^(-1/2)[2+2c_E+log(16 pi D/(kappa sqrt(P)))]`.                (7.4)

This is a direct optimization of the completed partner theorem and improves the convenient nonoptimized choice `y=1` used in its displayed corollary.

## 8. Actual target-valid inequality: kernel leakage with arbitrary remote outside fragments

For `m>=2`, let `a_m,b_m,c_m` be mutually orthonormal block-constant vectors on three disjoint `m`-coordinate banks. Let `U=(U_1,U_2)` be an original physical pair and `Z` an independent scalar. Consider

`Q_(m,gamma)
 = 2 U_1 U_2
   +(a_m^T V)^2 +(b_m^T V)^2
   +2 gamma (c_m^T V) Z.`                                       (8.1)

All original coordinates are independent with density caps at most one. The physical pair has `B=[[0,1],[1,0]]`, so `D=kappa=1`. The rank-two Schur curvature has `P=1` and leverage `1/m<=1/2`. Conditioning on `Z=z` produces an affine vector in the kernel direction `c_m`; completed r32 handles it uniformly and gives `K_0=4 pi`.

Now decompose the law of `Z` into any finite or countable collection of unnormalized fragments `nu_alpha`, of masses `m_alpha`, with arbitrary locations and separations and no bounded-support assumption. On fragment `alpha`, uniformity of the r32 bank estimate gives

`|hat nu_alpha^R(t)|
 <= m_alpha min{1,4pi/|t|}
 <= min{m_alpha,(4pi m_alpha)/|t|}`.                               (8.2)

Thus `K_alpha=4pi m_alpha` and `sum K_alpha=4pi`. Theorem 5.1 restores exactly the same whole-law critical budget. Applying (7.4), with `D=kappa=P=1`, yields

`||p_(Q_(m,gamma))||_infinity
 <= 2 + [sin(1/2)]^(-2) + log(16 pi)
 = 10.268003907429... .`                                          (8.3)

This is uniform in `m>=2`, every real `gamma`, every admissible cap-one product input law, every choice and number of outside fragments, arbitrarily distant fragment locations and unbounded support, all conditioning-generated translations, and all moments (none are assumed).

It improves the same partner branch's displayed nonoptimized bound `8 sqrt(pi)+[sin(1/2)]^(-2)=18.530316...` on this family.

The coefficient matrix of (8.1) has nonzero spectrum `{1,-1,1,1,|gamma|,-|gamma|}` (with the last pair absent when `gamma=0`), so this is genuinely inside the exact three-large-eigenvalue target for every `gamma`.

## 9. Localization conclusion and remaining gap

The decisive order is: keep each fragment unnormalized, prove or inherit its critical Fourier budget `K_alpha`, sum those budgets, use concavity of the logarithmic compiler, and only then pay the reciprocal physical-pair singularity. Rare bad fibers are allowed if their unnormalized critical costs are summable. No support, moment, translation, diameter, or fragment-count penalty is introduced.

This does not repair active-bank fragmentation when `sum K_alpha` itself diverges, and it does not manufacture a useful physical pair or a diffuse rank-two Schur frame from the bare spectral hypothesis. The next localization question is whether the surviving high-leverage/mixed-hub structural reductions can be organized so their fiberwise critical constants form a summable unnormalized budget.

No law-uniform pointwise scalar quadratic Fourier decay, arbitrary-joint coarea, post-rotation independence, positive conditional projection-cap moment, bounded-diameter localization, or fixed fragment-count reduction is used.

Full QFORM remains OPEN. Continuity for the unrestricted rough-law target remains separate.
