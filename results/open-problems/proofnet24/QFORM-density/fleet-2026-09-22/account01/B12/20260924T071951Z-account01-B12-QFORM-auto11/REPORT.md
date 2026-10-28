SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T07:19:51Z.
attacking: longitudinal-transverse principal-angle fusion — combine relative carrier survival with transverse spectral repair so fewer than five safe modes on either side can jointly yield a final five-mode original-coordinate carrier.

# account01/B12 — principal-angle fusion for arbitrary signed added spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T071951Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The owner target remains the unrestricted product-law problem: for every dimension, independent ORIGINAL coordinates with scalar densities at most one, and arbitrary real symmetric `A` with `s_3(A)>=1`, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No Gaussianity, moments, bounded/connected support, log-concavity, iid hypothesis, diagonal-basis independence, or post-rotation independence is used below.

The full conjecture remains open. The unresolved structural step is still to force, from bare `s_3(A)>=1`, one of the already-paid original-coordinate smoothing certificates. This report advances only the assigned **additional-eigenvalue stability** branch.

The mechanism is changed from the previous scalar/Pluecker update run. The key point is that after a large signed spectral addition, the exact carrier decomposition has two orthogonal codomain pieces:

1. a **longitudinal relative action** inside the old carrier range; and
2. a **transverse repair action** orthogonal to that range.

Earlier criteria paid either piece alone. Here I prove that fewer than five protected directions in each piece can fuse to produce five final carrier modes, provided their strong right-singular subspaces are quantitatively transverse in the ORIGINAL carrier domain.

## 2. Sources and corrections actually consumed


Designated partner source actually used:

`yspennstate/math-open-problems@572fa1f2bc3b1ab29018a426f414d21dce2b5504`

(account02/B12, theorem `QFORM-RELATIVE-NUMERICAL-RANGE-MODE-SHIELD-v1`). In its notation, for an original-coordinate carrier `M=A_0P`, `g=s_m(M)>0`, addition `N=SP`, and whitened relative action `K`, it proves for every `j`

` s_j((A_0+S)P) >= g [1+mu_j]_+ `

where `mu_j` is the `j`-th eigenvalue of the symmetric whitened relative action. I apply this below at `j=3` to an actual coefficient family.

Also reread the newer account02/B12 antipodal-skew theorem at

`yspennstate/math-open-problems@70aaef45400bbec56a6d6f4b0103c888e014d499`.

It confirms that the purely longitudinal obstruction is not just `Sym K=-I`: a skew component can rescue modes at exact antipodal symmetric resonance. The present theorem handles the complementary phenomenon where the rescue occurs **transversely to the old carrier range**, and only a few longitudinal plus a few transverse modes are separately available.

Density receiver used below: `D_5` from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

at `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. For any literal disjoint ORIGINAL-coordinate cross block `B=A[I,J]`,

` ||p_(X^T A X)||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10), `

with no row-marginal condition. In particular, if `s_5(B)>=r>0`, then

` ||p_(X^T A X)||_infinity <= 5 sqrt(2e)/r. `

This receiver gives a continuous `C_0(R)` density representative.

Corrections explicitly respected include:

- pointwise quadratic van-der-Corput decay is false uniformly over densities `<=1`;
- rotated eigen-coordinates are not independent;
- a bounded-density projection theorem alone does not control indefinite quadratic pushforward;
- naive fiber suprema can lose dimension;
- bi-independent spectral modes need not create aggregate physical cross volume;
- the three-large-eigenvalue hypothesis does not force a universal hub/star scale (`QFORM-GSTAR-SCALE-FORCING-FALSE-v1`).

No step below invokes any of these refuted interfaces.

## 3. Exact longitudinal/transverse carrier decomposition

Let `P:R^m -> R^n` be an ORIGINAL-coordinate embedding and let

` M=A_0P `

have full column rank. Put

` G=M^T M,    g=s_m(M)>0,    Pi=MM^dagger. `

Let `S=S^T` be an arbitrary signed addition and set

` N=SP. `

Define

` K=M^dagger N,    L=I+K,    Z=(I-Pi)N. `

Then exactly

` (A_0+S)P = ML+Z, `

with

` M^T Z=0. `

Therefore

` ((A_0+S)P)^T((A_0+S)P) = L^T G L + Z^T Z `

and hence

` boxed: ((A_0+S)P)^T((A_0+S)P) >= g^2 L^T L + Z^T Z. `      (3.1)

This identity is deterministic coefficient algebra. It does not rotate the random vector and does not treat any new quadratic remainder as an independent convolution.

## 4. Main theorem: principal-angle five-mode fusion

The next lemma is the new ingredient.

Let `E,F` be subspaces of the carrier domain `R^m`. Write `P_E,P_F` for orthogonal projections. Suppose

`dim E=r`, `dim F=s`, and `r+s=5`.

Assume `E cap F={0}` and define their largest principal-angle cosine

` c=||P_E P_F||op <1. `

For `a,b>0`, set

` mu(a,b,c)
   = ( a^2+b^2
       - sqrt((a^2-b^2)^2 + 4 a^2 b^2 c^2) )/2. `          (4.1)

### Theorem 4.1 — `QFORM-LONGITUDINAL-TRANSVERSE-ANGLE-FUSION-v1`

Assume the setup of Section 3. Suppose there is an `r`-dimensional right-singular spectral subspace `E` of `L` on which

` L^T L >= alpha^2 P_E `                                  (4.2)

and an `s`-dimensional right-singular spectral subspace `F` of `Z` on which

` Z^T Z >= beta^2 P_F, `                                   (4.3)

with `r+s=5` and `c=||P_E P_F||<1`.

Then

` boxed:
  s_5((A_0+S)P)^2
  >= mu(g alpha, beta, c). `                               (4.4)

Equivalently,

` boxed:
  s_5((A_0+S)P)
  >= sqrt(mu(g alpha,beta,c)). `                           (4.5)

The theorem remains true when `E,F` are subspaces of larger strong spectral spaces, provided one chooses subspaces `E_0,F_0` of dimensions summing to five and uses their principal-angle cosine.

### Proof

From (3.1), (4.2), and (4.3),

` H:=((A_0+S)P)^T((A_0+S)P)
    >= a^2 P_E+b^2 P_F, `

where

` a=g alpha`, `b=beta`.                                    (4.6)

It remains to compute the smallest positive eigenvalue of

` T=a^2 P_E+b^2 P_F. `                                     (4.7)

Because `E cap F={0}` and `dim E+dim F=5`, `T` has rank exactly five. Use the standard principal-angle decomposition of the pair `(E,F)`. Each paired two-dimensional principal-angle plane with cosine `sigma in [0,c]` contributes the two eigenvalues

` lambda_pm(sigma)
 = (a^2+b^2 +/- sqrt((a^2-b^2)^2+4a^2b^2 sigma^2))/2. `    (4.8)

Any unpaired direction contributes exactly `a^2` or `b^2`. Since

`lambda_-(sigma)` is decreasing in `sigma`

and

`lambda_-(sigma)<=min(a^2,b^2)`,                            (4.9)

the smallest nonzero eigenvalue of `T` is at least

`lambda_-(c)=mu(a,b,c)`.                                    (4.10)

By positive-semidefinite monotonicity and (4.6),

`lambda_5(H)>=lambda_5(T)>=mu(a,b,c)`.                       (4.11)

Since `lambda_5(H)=s_5((A_0+S)P)^2`, this proves (4.4)-(4.5). QED.

### Balanced-angle form

If `a=b`, then (4.1) simplifies to

` mu(a,a,c)=a^2(1-c), `

so

` boxed: s_5((A_0+S)P) >= a sqrt(1-c). `                    (4.12)

In particular, if the strong longitudinal and transverse domain subspaces are orthogonal (`c=0`), then

` boxed: s_5((A_0+S)P) >= min(g alpha,beta). `               (4.13)

This is the genuinely new fusion regime: neither piece needs five modes by itself.

## 5. Arbitrary small and large signed spectrum compiler

Write a full addition as

` A=A_0+S_hi+E_lo+T+S_spec, `

where:

- `S_hi=S_hi^T` is arbitrary in norm, sign and spectral magnitude and is handled by Theorem 4.1;
- `E_lo=E_lo^T` contains arbitrarily many eigenvalues of either sign but satisfies `||E_lo||op<=h`;
- `T=T^T` may have an arbitrarily large outside-outside block but satisfies only `||TP||op<=delta`;
- `S_spec=S_spec^T` is an arbitrary spectator satisfying `S_spec P=0`, with unrestricted dimension, signs and eigenvalue magnitudes.

Let

` r_* = sqrt(mu(g alpha,beta,c)). `

Then singular-value Weyl gives

` boxed: s_5(AP) >= [r_*-h-delta]_+. `                       (5.1)

Thus:

1. all small signed eigenvalues are paid **once** through their operator threshold `h`, independent of their number;
2. all spectator eigenvalues of arbitrary sign and size cost **zero**;
3. the active large packet is charged only through longitudinal strength, transverse strength, and the principal angle between their strong domain subspaces — not through the magnitude of its eigenvalues.

No claim is made that `X^T E_lo X` is a small random variable; (5.1) is a coefficient-matrix statement only.

## 6. Exact family where 3 longitudinal + 2 transverse modes fuse to five

This family is designed so that neither the longitudinal part nor the transverse part alone has five protected modes.

Take three disjoint ORIGINAL-coordinate banks

`H={h_1,...,h_5}`, `J={j_1,...,j_5}`, `K={k_4,k_5}`.

On `H union J union K`, define the baseline symmetric matrix

` A_0 = [[0,2I_5,0],
          [2I_5,0,0],
          [0,0,0]]. `                                       (6.1)

For `P=P_H`,

` M=A_0P `

has range equal to the `J` bank, `G=4I_5`, and `g=2`.

Let

` E=span(e_1,e_2,e_3),     F=span(e_4,e_5). `               (6.2)

For a real parameter `t`, define the symmetric high packet `S_t` by its only nonzero blocks

` S_t[J,H] = -2 P_F, `
` S_t[K,H] = t U_F, `                                      (6.3)

and transpose blocks, where `U_F:F -> R^K` is the coordinate isometry. Then

` N_t=S_tP = M(-P_F)+t U_F P_F. `                           (6.4)

Hence in the exact decomposition,

` K_rel=-P_F, `
` L=I+K_rel=P_E, `
` Z=t U_F P_F. `                                            (6.5)

Therefore

` L^T L=P_E, `
` Z^T Z=t^2 P_F, `
` P_E P_F=0. `                                              (6.6)

The longitudinal piece has rank three only. The transverse piece has rank two only. Neither can activate the fifth-volume receiver alone. Theorem 4.1 fuses them and gives

` boxed: s_5((A_0+S_t)P_H) >= min(2,|t|). `                 (6.7)

In fact equality holds because the five carrier columns are orthogonal with norms

`2,2,2,|t|,|t|`.

### The added eigenvalues are genuinely signed and unbounded

The high packet `S_t` itself is a symmetric off-diagonal dilation. On the two `F` directions its cross columns have norm

`sqrt(4+t^2)`,

so its nonzero eigenvalues are

` +sqrt(4+t^2), +sqrt(4+t^2),
  -sqrt(4+t^2), -sqrt(4+t^2). `                             (6.8)

Thus as `|t|->infinity`, the added spectrum contains arbitrarily large positive and negative eigenvalues. Any number of further arbitrarily large positive/negative spectator eigenvalues may be appended through `S_spec P_H=0` at zero carrier cost.

## 7. Explicit use of the designated account02/B12 result

For the family above, the whitened relative action of the in-range component is simply

`K_rel=-P_F`.

Its symmetric eigenvalues are

`0,0,0,-1,-1`.

Apply account02/B12 `QFORM-RELATIVE-NUMERICAL-RANGE-MODE-SHIELD-v1` at `j=3`. Since

`mu_3=0`,

its actual inequality gives

` boxed:
  s_3((A_0+S_t)P_H) >= g(1+mu_3)=2. `                       (7.1)

At the level of the relative factor, this supplies the three-dimensional longitudinal threshold

`alpha=1` on `E`.

The transverse defect is explicit and has

`beta=|t|` on the two-dimensional `F`, while

`c=||P_E P_F||=0`.

Substituting the partner-certified longitudinal threshold into the new fusion theorem gives

` s_5((A_0+S_t)P_H)
  >= sqrt(mu(2,|t|,0))
  = min(2,|t|), `                                           (7.2)

which is exactly the concrete inequality (6.7). Thus a completed designated-partner result is used at the equation level and then extended by the new transverse-fusion step.

## 8. Dense small signed tail and a final density bound

Assume now

`|t|>=2`.

Add any arbitrary-rank signed low-spectrum packet satisfying

`||E_lo||op<=1/8`,

and any further symmetric tail satisfying only

`||T P_H||op<=1/8`.

The outside-outside block of `T` is unrestricted. Also append any spectator symmetric matrix `S_spec` with `S_spec P_H=0`, arbitrary dimension and arbitrary positive/negative eigenvalues.

By (5.1) and (7.2), the actual final carrier obeys

` boxed:
  s_5(A P_H) >= 2-1/8-1/8 = 7/4. `                         (8.1)

Let

`J'=J union K`.

The literal original-coordinate cross block `B=A[J',H]` has the same five singular values as the carrier rows used above up to additional rows, and the two small/tail perturbations together cost at most `1/4`. Hence directly

` boxed: s_5(B)>=7/4. `                                      (8.2)

Therefore

` e_5(B^T B) >= s_5(B)^10 >= (7/4)^10. `                    (8.3)

Apply the completed `D_5` theorem to this **actual final original-coordinate cross block**:

` boxed:
  ||p_(X^T A X)||_infinity
  <= 5 sqrt(2e)/(7/4)
  = 6.661839947420355... < 6.662. `                          (8.4)

This branch has a continuous `C_0(R)` density representative.

The full matrix also lies literally in the owner's target class, because

` s_3(A) >= s_5(A P_H) >= 7/4 >1. `                         (8.5)

So the example is not merely a toy outside the target: it is an exact-target family with unbounded signed added spectrum, arbitrary-rank small signed spectrum, arbitrary spectator spectrum, and a final universal density bound.

## 9. Why this is not covered by a one-piece five-mode criterion

Before fusion,

`rank(ML)=3`,

and

`rank(Z)=2`.

Therefore neither

` s_5(ML)>0 `

nor

` s_5(Z)>0 `

holds. A criterion demanding five protected longitudinal modes or five protected transverse modes separately gives nothing.

The new theorem pays the **domain geometry** between the two strong subspaces. In the example the subspaces are exactly orthogonal, so the five directions combine with no loss. For nonorthogonal `E,F`, the exact loss is the principal-angle factor in (4.1).

This is the useful new stability principle for additional signed eigenvalues:

> a destructive large spectral packet must simultaneously erase longitudinal carrier directions **and** align the surviving transverse-repair directions with those same weak domain directions. Merely having fewer than five modes in either component is not enough.

## 10. Structural limitation and next implication

This report does **not** prove that bare `s_3(A)>=1` forces the hypotheses of Theorem 4.1 with a universal quantitative angle, nor does it prove a universal fifth cross-volume. The live corrections show that several tempting local-minor, cross-rank, and hub-scale implications are false.

The precise next structural target suggested by the theorem is a cancellation-aware domain decomposition:

- choose an original-coordinate carrier `P`;
- decompose every dangerous added spectral packet into its longitudinal relative action `L` and transverse repair `Z`;
- prove that either five protected modes exist in one piece, or there are smaller strong subspaces `E,F` with dimensions summing to five and `||P_E P_F||<=1-c_0` for a universal `c_0>0`, or else the common near-bad domain forces one of the already-paid grouped-bank / physical-pair / Schur / ridge / common-plane / Pluecker exits.

The unresolved content is exactly that final forcing statement. No claim of a full solution is made.

## 11. Finite sanity check

I separately checked the principal-angle spectral formula on 500 random pairs of subspaces with dimensions `3+2` in `R^7`, random positive `a,b`, and compared the fifth eigenvalue of

`a^2 P_E+b^2 P_F`

against (4.1). No violation occurred; the minimum numerical slack was `-3.1e-14`, consistent with floating-point roundoff. This is only a sanity check. The proof is the exact principal-angle calculation above.

## 12. Status

- New theorem proved: `QFORM-LONGITUDINAL-TRANSVERSE-ANGLE-FUSION-v1`.
- Arbitrary large eigenvalues: handled in the stated longitudinal/transverse geometric scope, with either sign and unbounded magnitude.
- Arbitrarily many small eigenvalues: handled at once by one operator threshold.
- Partner result: account02/B12 `QFORM-RELATIVE-NUMERICAL-RANGE-MODE-SHIELD-v1` applied to (7.1)-(7.2).
- Density receiver: completed `D_5` theorem applied to the actual final original-coordinate cross block.
- Essential boundedness: proved in the stated family/scope.
- Continuity: proved only in the final `D_5` branch above (`C_0` representative).
- Full conjecture: **OPEN**.
- Brain ingestion: `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion.
