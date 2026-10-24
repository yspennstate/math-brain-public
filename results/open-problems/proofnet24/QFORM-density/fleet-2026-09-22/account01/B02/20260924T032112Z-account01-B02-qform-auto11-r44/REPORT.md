SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T03:21:12Z.
attacking: turn the r43 finite-localized rank-42 carrier into a SPECTRALLY ACTIVE finite hub, by combining a finite-rank multiplicative spectral gap with the tunable r38 leverage split; spend the diffuse branch immediately through account02/B02 Fourier-E3.

# account01/B02 r44 — active spectral-gap hub or genuine Fourier-L1 exit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: continuous `C_0` density on the Fourier-L1 branches proved below; full-target continuity remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged. All random coordinates remain ORIGINAL coordinates. No post-rotation independence, Gaussianity, log-concavity, moments, compact support, connected support, conditional-density cap, arbitrary-joint coarea, pointwise van-der-Corput decay, or deletion of a small nonzero quadratic tail is used.

## 1. Source-pinned state actually used

Fresh control at invocation start was `yspennstate/math-research-brain@7afbaf67002a197b340cd34c244a8371147eb075`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. I read `AGENTS.md`, the owner message, `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, the live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, and this slot's assignment card.

Immediate predecessor:

- `yspennstate/math-open-problems@041bd053495db9b7e7c12d994501de10c059c459`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260924T022016Z-account01-B02-qform-auto11-r43/REPORT.md`.

The r43 survivor is an exact ORIGINAL-coordinate decomposition

`A = R + D + E`,                                                   (1.1)

with

`rank R <= 42`,
`D` diagonal, `||D||op < 1/8`,
`||E||F < eps_* := 7.888707199262311e-7`,
`s3(R) > gamma_* := 0.8749992111292801`.                           (1.2)

The designated account02/B02 result consumed at equation level is its newest completed full-cut exterior-propagation report:

- `yspennstate/math-open-problems@b34c3df7995a27f90540057d7dc1fcc33d6e7e39`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260924T023712Z-r11/REPORT.md`.

It contains the completed marginal-free physical-third-volume Fourier theorem

`E3(B)>0 => ||p_Q||inf <= C3 E3(B)^(-1/6)`,
`integral_R |phi_Q(t)|dt <= 2*pi*C3 E3(B)^(-1/6)`,
`C3=10.345083232147514...`,                                       (1.3)

for every literal disjoint ORIGINAL-coordinate cross block `B`, with continuous `C_0` density, and the full-cut exterior lift

`E3(B_C) >= E3(M)+x1*x2 delta_C^2`,
`E3(B_R) >= E3(M)+x1*x2 delta_R^2`.                               (1.4)

I also use the proved *tunable* form of my r38 leverage fork, source

- `yspennstate/math-open-problems@38ff5f34b3b87c21d44b8e6fd12646e496436234`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T212524Z-account01-B02-qform-auto11-r38/REPORT.md`.

For a rank-`k` carrier factor `V`, parameter `0<eta<=1`, and

`H_eta={i: ||v_i||^2 > eta^2/(4k)}`,                              (1.5)

it gives `|H_eta|<=4k^2/eta^2`, and either a carrier unit vector with more than `1-eta` of its squared mass on `H_eta`, or an ORIGINAL-coordinate cut with carrier crossing singular value

`s3 >= s3(K) sqrt[(eta/4)(1/2-eta/4)]`.                           (1.6)

The proof of r38 uses the perturbation only through the operator norm of the cross-block perturbation. I use precisely that proof below, with a spectral tail controlled in operator norm rather than Frobenius norm.

## 2. Main new theorem — active spectral gap before leverage splitting

### Theorem 2.1 — `QFORM-ACTIVE-SPECTRAL-HUB-OR-E3-L1-v1`

Assume (1.1)-(1.2), but for the moment write the parameters abstractly as

`rank R <= r <= 42`, `s3(R)>=gamma>0`, `||E||op<=eps`.             (2.1)

Take

`eta=1/4`,
`a=sqrt(1-eta)=sqrt(3)/2`,
`c_eta=sqrt[(eta/4)(1/2-eta/4)]=sqrt(7)/16`,                      (2.2)

and

`q = (39/38)/a = 39/(19 sqrt(3)) = 1.1850873946523899...`.        (2.3)

Define the top spectral scale

`T0=(c_eta gamma q)/2`,                                           (2.4)

and the forty disjoint multiplicative annuli

`I_m=(T0 q^(-(m+1)), T0 q^(-m)]`, `m=0,...,39`.                   (2.5)

Because `R` has rank at most `42` and already has at least three singular values at least `gamma>T0`, at most `39` singular values of `R` can lie in the union of the forty annuli. Hence at least one annulus is empty. Choose such an `m`, put

`tau=T0 q^(-m)`,                                                  (2.6)

and split `R` spectrally, as coefficient algebra only,

`R=R_hi+R_lo`,                                                     (2.7)

where `R_hi` contains the eigencomponents with `|lambda|>tau`. Since the annulus `(tau/q,tau]` is empty,

`||R_lo||op <= tau/q`.                                            (2.8)

Also all three `>=gamma` singular directions belong to `R_hi`, hence

`s3(R_hi)>=gamma`.                                                (2.9)

Let `k=rank(R_hi)` and form the r38 tunable heavy set `H` from a spectral factor of `R_hi` with `eta=1/4`. Then exactly one of the following holds.

**(A) Fourier-L1 exit.** There is a literal ORIGINAL-coordinate cut `J|I` with

`s3(A[J,I]) >= sigma_act := (sqrt(7)/32) gamma - eps`.            (2.10)

Consequently

`E3(A[J,I])>=sigma_act^6`,                                        (2.11)

and the account02/B02 theorem gives

`||p_Q||inf <= C3/sigma_act`,                                     (2.12)

`integral |phi_Q| <= 2*pi*C3/sigma_act`,                          (2.13)

with continuous `C_0` density.

**(B) Spectrally active finite hub.** There is a set of ORIGINAL coordinates

`|H| <= 64 k^2 <= 112896`,                                       (2.14)

and a unit vector `z in range(R_hi)` such that

`||z_H||^2 > 3/4`.                                                (2.15)

Moreover the hub is coefficient-active after retaining the small tail: one has

`||P_H (A-D)||op >= nu(gamma,eps)>0`,                              (2.16)

where

`nu(gamma,eps)
 := [T0 q^(-39)]*(sqrt(3)/78) - eps`.                             (2.17)

In addition, some genuine eigenvector `v` of `R` with eigenvalue magnitude

`|lambda|>tau>=T0 q^(-39)`                                       (2.18)

has

`||v_H||^2 > 3/(4k) >= 1/56`.                                    (2.19)

Thus the finite-localized obstruction can no longer be an arbitrary almost-null direction of the rank-42 carrier.

### Proof

The spectral-gap selection (2.5)-(2.8) is the pigeonhole argument above. Apply the tunable r38 construction to `R_hi` with `eta=1/4`.

If its diffuse alternative holds, the carrier crossing produced by the same physical random split satisfies, by (1.6),

`s3(R_hi[J,I]) >= c_eta gamma`.                                   (2.20)

Across a literal physical cut the diagonal `D` vanishes. Weyl and (2.8) therefore give

`s3(A[J,I])
 >= c_eta gamma - ||R_lo||op - ||E||op
 >= c_eta gamma - tau/q - eps`.                                  (2.21)

Since `tau<=T0` and `T0/q=c_eta gamma/2`,

`s3(A[J,I]) >= c_eta gamma/2-eps
 = (sqrt(7)/32)gamma-eps`,                                       (2.22)

which is (2.10). Equations (2.11)-(2.13) follow immediately from the completed account02/B02 physical-`E3` theorem.

Now suppose the localized alternative holds. The r38 theorem gives (2.14)-(2.15). Because every nonzero singular value of `R_hi` is `>tau`, let `y=R_hi^dagger z`; then `||y||<1/tau`. For `u=y/||y||`,

`R_hi u = z/||y||`,

hence

`||P_H R_hi u|| > a tau`.                                        (2.23)

Using (2.8),

`||P_H R u|| > tau(a-1/q)`.                                      (2.24)

The choice (2.3) was made so that the margin is exact:

`a-1/q
 = sqrt(3)/2 - 19sqrt(3)/39
 = sqrt(3)/78`.                                                   (2.25)

Since `A-D=R+E`, (2.24) yields

`||P_H(A-D)||op
 >= tau sqrt(3)/78 - eps
 >= [T0 q^(-39)] sqrt(3)/78 - eps`,                              (2.26)

which is (2.16)-(2.17).

Finally, let `{v_j}` be an orthonormal eigenbasis of `range(R_hi)`. The operator norm statement (2.15) implies

`sum_j ||(v_j)_H||^2
 = trace(P_H restricted to range(R_hi))
 >= ||P_H restricted to range(R_hi)||op^2
 >3/4`.                                                          (2.27)

There are at most `k<=42` terms, so one eigenvector satisfies (2.19), and its eigenvalue belongs to `R_hi`, proving (2.18). QED.

## 3. Concrete r43 constants

Insert the actual r43 numbers

`gamma=gamma_*=0.8749992111292801`,
`eps=eps_*=7.888707199262311e-7`.                                 (3.1)

Then

`T0 = 0.08573478870780502...`,                                   (3.2)

`tau_min:=T0 q^(-39)=0.00011399670854814539...`,                 (3.3)

and

`sigma_act=(sqrt(7)/32)gamma_*-eps_*
          =0.07234390831758555...`.                              (3.4)

Therefore alternative (A) is paid at the actual inequality

`E3(A[J,I]) >= sigma_act^6`,                                     (3.5)

and the designated account02/B02 theorem gives

`boxed: ||p_Q||inf < 142.999,`                                   (3.6)

`boxed: integral_R |phi_Q(t)|dt < 898.488.`                      (3.7)

This branch has a continuous `C_0` density.

On alternative (B), the coefficient-active hub constant is

`nu_*
 = tau_min*(sqrt(3)/78)-eps_*
 =1.7425150634200468e-6`.                                        (3.8)

Thus the still-unpaid branch now contains a universal finite physical set `H`, `|H|<=112896`, satisfying

`boxed: ||P_H(A-D)||op >=1.7425e-6,`                              (3.9)

and a genuine carrier eigenvector with

`boxed: |lambda|>1.13996e-4,  ||v_H||^2>1/56.}`                  (3.10)

For bookkeeping, since `sqrt(|H|)<=336`, (3.9) also implies that some physical row in `H` has `(A-D)` row `l2` norm at least

`1.7425e-6/336 >5.18e-9`.                                        (3.11)

This tiny number is not presented as a density constant; it is a universal coefficient certificate for the next grouped-hub step.

## 4. Actual use of the newest account02/B02 exterior lift

Return to the r42/r43 ultra-rank-two parent block `M=A[R,C]`. In the r43 full-cut survivor,

`x1*x2 > P_*:=0.4444444444298925...`,
`E3(M)<zeta:=2^-48`.                                             (4.1)

The newest account02/B02 theorem (1.4) says that if either one-sided full-cut lift reaches `E3>=zeta`, the same physical-`E3` Fourier theorem pays the ambient law (the r43 bound `<2648.342` for the density and `<16640.020` for the Fourier integral). Hence the still-unpaid branch may also assume both full-cut lifts remain below `zeta`, and then (1.4) forces

`delta_C^2,delta_R^2 < zeta/P_*
 =7.993605777562852e-15`,                                       (4.2)

so

`boxed: delta_C,delta_R < 8.940696716454961e-8.}`                 (4.3)

This is an equation-level application of the newest designated partner result. It says that, simultaneously with the active-hub certificate (3.9), genuinely transverse leakage out of the inherited two-mode crossing is two orders of magnitude smaller. Therefore the next obstruction is not a diffuse third direction hiding outside the old banks: after the Fourier exits, the active hub must be reconciled with the aligned rank-two crossing and/or same-bank curvature.

I do **not** infer from (4.3) that the full hub is transverse, nor that a single good minor exists. Those would be invalid strengthenings.

## 5. What changed and first unpaid implication

The r43 obstruction was only:

> some carrier-range unit vector is mostly supported on a finite physical set.

That vector could, in principle, have belonged almost entirely to a tiny singular-value direction of the rank-42 carrier, making it useless for quantitative smoothing. The multiplicative spectral-gap compiler above removes that ambiguity.

After the new theorem, every survivor has a finite set `H` of at most `112896` original coordinates which simultaneously carries:

1. a genuine eigenvector of `R` at eigenvalue scale `>1.13996e-4` with at least `1/56` of its squared mass on `H`;
2. an actual coefficient operator `P_H(A-D)` of norm at least `1.7425e-6` after the full small Frobenius tail is retained;
3. the r42/r43 robust rank-two crossing with `E2>4/9` and ultra-small third volume;
4. the account02/B02 conclusion that all still-unpaid outside crossing leakage transverse to the two-mode carrier is `<8.95e-8` in Frobenius norm.

The new first B02 interface is therefore

`QFORM-ACTIVE-HUB-ALIGNED-RANK2-OR-SAMEBANK-L1-v1`:

> On the above exact survivor, split the active finite hub relative to the two sides of the robust full cut. Use (4.3) to discard only the *coefficient estimate* on transverse leakage (not the random term), and prove that either (i) enough of the hub operator lies in same-bank curvature to trigger a finite-coordinate pair-log / principal-block receiver, or (ii) enough lies in the aligned two-mode crossing to trigger a phase-sensitive rank-two bilinear Fourier receiver. The rank-two receiver must be integrated in time; the critical pointwise `|t|^-1` estimate is not enough.

This is a stricter and more quantitative endpoint than the previous finite-localization statement. No exact-target counterexample to a universal unweighted `integral |phi_Q|` bound was found. The target-wide Fourier criterion remains `OPEN_NOT_REFUTED`; full bounded density and full-target continuity remain OPEN.

## 6. Arithmetic checks

With `eta=1/4`,

`a=sqrt(3)/2`, `c_eta=sqrt(7)/16`,
`q=39/(19sqrt(3))`,
`a-1/q=sqrt(3)/78` exactly.

For the r43 constants:

`T0=0.08573478870780502`,
`tau_min=0.00011399670854814539`,
`sigma_act=0.07234390831758555`,
`C3/sigma_act=142.99867774261241`,
`2pi C3/sigma_act=898.4871909384908`,
`nu_*=1.7425150634200468e-6`,
`64*42^2=112896`,
`(3/4)/42=1/56`.

These computations normalize constants only; the proof is the exact argument above.
