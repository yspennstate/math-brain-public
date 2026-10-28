SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T02:51:41Z.
attacking: energy-collision routing in the zero-diagonal low-stable-rank/high-third-compound-overlap branch using product Fourier rearrangement.

# account01/B04 r27 — soft spectral-core stability for disjoint third-compound Fourier mass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement.  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / PARTNER APPLIED**.  
Continuity: proved on the new paid branch; full-target continuity remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. Every probabilistic conditioning below is on ORIGINAL physical coordinates. Spectral decompositions are used only for deterministic coefficient identities. No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, worst-fiber supremum, or law-uniform pointwise quadratic-phase decay assumption is introduced.

## 1. Fresh source boundary


The two analytic inputs are:

1. Previous same-slot theorem `QFORM-ENERGY-WEIGHTED-THIRDCOMPOUND-COLLISION-v1`, source
   `yspennstate/math-open-problems@32b0b659346aab1c840c81d677f75d5aef0654e3`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260924T014632Z-account01-B04-QFORM-auto11-r26/REPORT.md`.
   For a symmetric physical carrier `T`, with third-compound energy `E_T=e3(T^2)` and energy collision `chi_3(T)`, it proves

   `Delta3_disj(T) >= (1-chi_3(T)) E_T`,

   and `chi_3(T) <= sum_i ell_i(T)^2`, where `ell_i(T)` are physical range leverages.

2. Completed marginal-free physical cross-third-volume receiver `QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`, source
   `yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T215155Z-account03-B04-QFORM-auto11-r42/REPORT.md`.
   For every literal original-coordinate cross block `M`, with arbitrary same-bank quadratic terms and induced affine terms,

   `||p_Q||_infinity <= C_* E3(M)^(-1/6)`,

   `C_*=8.45302122552817687470491804598...`,

   and the characteristic function is in `L1`, hence the density has a `C_0` representative.

The designated account02/B04 theorem actually applied in Section 6 is `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`, pinned at
`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.
Its exact-rank-three branch gives `||p_Q||_infinity <=6 E3(M)^(-1/6)` with a continuous `C_0` density, while retaining arbitrary same-bank phases/curvature.

## 2. The new deterministic theorem

Let

`S=S^T=U diag(lambda_1,...,lambda_n) U^T`

be any real symmetric physical coefficient carrier (zero eigenvalues are allowed). Choose an arbitrary spectral index set `J` with at least three nonzero eigenvalues and define the spectral core

`S_J=U_J diag(lambda_j:j in J) U_J^T`.

Put

`E=e3(S^2)=||C3(S)||_F^2`,
`E_J=e3(S_J^2)=||C3(S_J)||_F^2>0`,
`R_J=E-E_J`.

For the core, let `chi_J=chi_3(S_J)` be the r26 energy-weighted collision. Equivalently one may use the computable coarser range collision

`tau_J=sum_i ell_i(S_J)^2`,

because `chi_J<=tau_J`.

### Theorem — `QFORM-SOFT-SPECTRAL-CORE-DISJOINT-E3-v1`

The full carrier satisfies

`boxed:
 Delta3_disj(S)
 >= [ sqrt((1-chi_J)_+ E_J) - sqrt(R_J) ]_+^2.`                 (2.1)

Consequently also

`boxed:
 Delta3_disj(S)
 >= [ sqrt((1-tau_J)_+ E_J) - sqrt(R_J) ]_+^2.`                 (2.2)

This is a stability theorem: a spectrally tiny full-rank tail is paid in **third-compound energy**, not by declaring it absent or perturbing the random quadratic form.

### Proof

Let `C3` denote the third compound in physical coordinates. Since `S` and `S_J` use the same orthonormal eigenbasis, on the exterior spectral basis

`C3(S)=W diag(lambda_a lambda_b lambda_c) W^T`,

while `C3(S_J)` is obtained by setting to zero exactly those spectral triples not wholly contained in `J`. Hence the two spectral pieces are Frobenius-orthogonal and

`boxed: ||C3(S)-C3(S_J)||_F^2=E-E_J=R_J.`                      (2.3)

Let `D` be the orthogonal coordinate projection on compound-matrix entries `(R,T)` with `R cap T=empty`, `|R|=|T|=3`. Then

`||D C3(S)||_F^2=Delta3_disj(S)`,
`||D C3(S_J)||_F^2=Delta3_disj(S_J)`.                            (2.4)

The triangle inequality and contractivity of `D` give

`sqrt(Delta3_disj(S))
 >= sqrt(Delta3_disj(S_J)) - ||D(C3(S)-C3(S_J))||_F`
`>= sqrt(Delta3_disj(S_J)) - sqrt(R_J).`                         (2.5)

Apply the completed r26 theorem to the core:

`Delta3_disj(S_J)>=(1-chi_J)E_J`.                               (2.6)

Taking the positive part in (2.5) proves (2.1). Since `chi_J<=tau_J`, (2.2) follows. QED.

No random variable was rotated in this argument; exterior spectral coordinates are only a deterministic matrix representation used to prove (2.3).

## 3. Product-Fourier density consequence

For a random labelled Bernoulli partition of the ORIGINAL physical coordinates, every fixed ordered disjoint pair of triples lands across the cut with probability `2^-6=1/64`. Thus some physical cut `I disjoint-union K` satisfies

`E3(S[I,K])>=Delta3_disj(S)/64`.                                (3.1)

Define

`Lambda_J := [ sqrt((1-chi_J)_+ E_J) - sqrt(R_J) ]_+`.           (3.2)

Whenever `Lambda_J>0`, combine (2.1), (3.1), and the completed marginal-free cross-E3 receiver:

`boxed:
 ||p_Q||_infinity <= 2 C_* Lambda_J^(-1/3),`                    (3.3)

and

`boxed: p_Q in C_0(R).}`                                        (3.4)

Equivalently, if

`chi_J<=beta<1`, `R_J<=eta E_J`, `sqrt(eta)<sqrt(1-beta)`,

then

`boxed:
 ||p_Q||_infinity
 <=2 C_* E_J^(-1/6)
        (sqrt(1-beta)-sqrt(eta))^(-1/3).`                        (3.5)

The theorem retains arbitrary physical same-bank curvature because the final receiver is applied to a literal original-coordinate crossing. This is not a small-operator-norm perturbation argument on random variables.

## 4. Why this changes the r26 obstruction

If `S` is full rank, then its range projector is the identity. Hence every physical leverage is `ell_i=1`, while the canonical third-compound marginals satisfy `sum_i mu_i=3`. Therefore

`chi_3(S)=3`,                                                    (4.1)

so r26 applied directly to the **full** carrier gives no positive disjoint-mass certificate at all. The new theorem may nevertheless succeed by choosing a spectrally relevant head `S_J` and paying the omitted directions through the exact compound-tail norm `R_J`.

Thus “full physical range” is no longer an obstruction when almost all third-compound energy is carried by a diffuse three-or-more-dimensional spectral head.

The current unresolved structural implication is sharpened to

`QFORM-SMALLPAIR-NO-GOOD-SPECTRAL-CORE-ROUTING-v1`:

> In the localized overlap-two small-pair branch, after the completed pair exit and the forced complement-curvature packet, suppose every spectral core `J` with target-scale `E_J` either has core collision near one or leaves compound tail `R_J` at least comparable to `(1-chi_J)E_J`. Route that failure into the completed rank-two rough-curvature, grouped-hub, anchored-E4, projected-crossing, ridge, square-bank, or pair mechanisms without deleting a nonzero random quadratic tail.

This is strictly narrower than r26's previous “low stable rank or high full-range energy collision” remainder: an arbitrarily large collection of tiny nonzero eigenvalues is now harmless if its *third-compound* contribution is small.

## 5. Fully dense, full-rank, genuinely rotated indefinite stress matrix

Let `H_16` be the Sylvester Hadamard matrix and write its normalized columns as `u_1,...,u_16`, so every entry is `+-1/4` and the columns form an orthonormal basis. Define

`A_* = 2 u_1u_1^T +3u_2u_2^T -4u_3u_3^T
       + sum_(k=1)^13 (k/1000) u_(k+3)u_(k+3)^T.`                (5.1)

Its spectrum is exactly

`{2,3,-4,1/1000,2/1000,...,13/1000}`.                           (5.2)

Hence it is full rank, indefinite, and has exactly three eigenvalues of modulus at least one.

It is physically fully dense. For an off-diagonal entry, after multiplying by 16 the contribution of the first three directions is a signed sum `+-2 +-3 +-4`, hence an odd nonzero integer of magnitude at least one. The total absolute contribution of all thirteen tail eigenvalues is at most

`(1+...+13)/1000=91/1000<1`,

so no off-diagonal entry can vanish. The diagonal is

`(2+3-4+91/1000)/16=1091/16000>0`.                              (5.3)

The exact check finds the smallest absolute physical matrix entry to be `939/16000`.

Take the spectral core `J={1,2,3}`. Then

`E_J=4*9*16=576`.                                                (5.4)

Every physical core leverage is `3/16`, so

`tau_J=16*(3/16)^2=9/16`,                                       (5.5)

and therefore `chi_J<=9/16`.

For the thirteen tail squared eigenvalues `t_k=k^2/10^6`, put

`T1=sum t_k=819/10^6`,
`T2=e2(t_1,...,t_13)=58149/200000000000`,
`T3=e3(t_1,...,t_13)=11771331/200000000000000000`.

Since the head squared eigenvalues are `4,9,16`, with `e1=29`, `e2=244`, the exact compound tail is

`R_J=244 T1+29 T2+T3`
`   =39968886332771331/200000000000000000`
`   =0.199844431663856655...`.                                  (5.6)

Thus

`eta=R_J/576
 =13322962110923777/38400000000000000000
 =0.0003469521383053067...`,                                    (5.7)

and

`sqrt(1-9/16)-sqrt(eta)
 =sqrt(7/16)-sqrt(eta)
 =0.6428111764754485...>0`.                                     (5.8)

Equation (3.5) gives, for **every** independent cap-one product input law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=6.791156439005779...,
 p_(X^T A_* X) in C_0(R).}`                                     (5.9)

Direct r26 on the same full-rank matrix has `chi_3(A_*)=3` by (4.1), so its direct certificate is empty. The new soft-core theorem is therefore a strict extension, not merely a constant improvement.

## 6. Designated account02/B04 theorem applied at an actual inequality

To apply the designated partner on the **same matrix**, deliberately choose the literal physical three-row bank

`S={3,11,15}`

and let `T` be its thirteen-coordinate complement. The cross block

`M=A_*[S,T]`

has exactly three active row coordinates. Exact rational computation gives

`boxed:
 E3(M)=det(MM^T)
 =51073258907/819200000000000000000
 =6.234528675170898...*10^(-11)>0.}`                             (6.1)

Hence `rank(M)=3`, and account02/B04's completed exact-rank-three branch applies directly, retaining the same-bank quadratic blocks. It yields the actual inequality

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=6 E3(M)^(-1/6)
 =301.3126136164239...,
 p_(X^T A_* X) in C_0(R).}`                                     (6.2)

This is a deliberately local certificate on the same physical matrix. The new aggregate soft-core bound (5.9) is stronger by a factor

`301.3126136164239 / 6.791156439005779
 =44.368...`.                                                    (6.3)

The point is not that the partner theorem is weak; on a better specially chosen cut it can be far sharper. The comparison demonstrates the assignment's intended aggregate-before-local-inversion principle: a generic local three-row witness can carry only `~10^-10` third volume while the spectrally aggregated product-Fourier certificate stays `O(1)`.

## 7. Checks and status

A standard-library exact-rational check is committed beside this report as `checks.py`. It verifies:

- Sylvester orthogonality;
- every entry of `A_*` is nonzero;
- minimum absolute physical entry `939/16000`;
- exact compound-tail rational (5.6);
- exact `eta` (5.7);
- exact partner `E3` rational (6.1);
- numerical partner bound (6.2).

These computations support the proof but do not replace it.

The full QFORM conjecture remains **OPEN**. This run proves a new source-valid supporting theorem and a continuous-density branch, not a full solution. Independent review of `QFORM-SOFT-SPECTRAL-CORE-DISJOINT-E3-v1` is still pending.
