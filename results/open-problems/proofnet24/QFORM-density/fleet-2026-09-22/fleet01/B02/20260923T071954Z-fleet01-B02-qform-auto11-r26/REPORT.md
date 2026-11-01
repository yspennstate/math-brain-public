SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T07:19:54Z.
attacking: integrated Fourier estimate — replace the previous 1/2 rank-three-core leverage cutoff by the sharp 3/4 Fourier threshold, then identify the exact two-sided heavy-core packet left over.

# fleet01/B02 r26 — stability up to the three-quarter leverage threshold

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open. This run proves that the near-rank-three branch from the preceding B02 spectral-collapse theorem has an unweighted L1 characteristic-function estimate whenever the best physical rank-three core has a strict leverage gap below 3/4 on either the row side or the column side. Thus the prior perturbative cutoff 1/2 is not structural: after choosing the collapse scale sufficiently small, every one-sided core leverage `<3/4` is paid. The only near-rank-three leverage collar left by this mechanism has simultaneous row and column maxima at least 3/4. In that collar I derive an exact rank-three determinant-factorization identity and feed it into fleet02/B02's joint-star block compiler, obtaining a universal-scale anchored core resource.

No pointwise law-uniform oscillatory decay, post-rotation independence, arbitrary-joint coarea, fixed-good-minor selection, moment/support/log-concavity hypothesis, or generic matrix-perturbation continuity is used. The perturbation is retained inside the completed volume-stability Fourier theorem.

Continuity is proved on the L1 branches below. It is not asserted for the full target.

## 1. Inputs used at equations

The designated partner source is fleet02/B02,

- `yspennstate/math-open-problems@f7a221e0f40362a1ccad48cf81812f2143f3cc92`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T020523Z-fleet02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`.

I use two proved ingredients from that report.

### Partner input A: q-dependent third-volume Fourier theorem

For a physical cross block `M`, put `Z=e3(M^T M)>0` and let `alpha_i` be the actual determinant-squared third-volume row marginals. If

`1 <= q < 3/2`, `max_i alpha_i <= q/2`,

then the proof gives the genuine unweighted Fourier estimate

`int_R |phi_Q(t)| dt <= 2 pi C(q) Z^(-1/6)`,

where

`C(q)=3e/[(3-2q)sqrt(q)]`,

and hence

`||p_Q||_infinity <= C(q) Z^(-1/6)`.

All same-bank phases and outside couplings are retained.

### Partner input B: projection stability of actual volume marginals

If `M=M0+E`, `kappa=s3(M)>0`, and `P` is the orthogonal projection onto `range(M0)`, then the same source proves

`sqrt(alpha_i) <= sqrt(l_i) + d sqrt(1-l_i)`,

with

`l_i=P_ii`, `d=sqrt(3)||E||op/kappa`.

The source optimized the special case `max l_i<=1/2`, `||E||<=s3(M0)/16`. This run keeps the same proved inequality but optimizes it at the actual sharp-HY threshold `3/4`.

I also use my immediately preceding B02 theorem

- `yspennstate/math-open-problems@bf39ca0cbbb657e697d9b95f14ea17dd4f5118c2`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260923T065505Z-fleet01-B02-qform-auto11-r25/REPORT.md`,

which states that for every physical cross block with `Z=e3(M^TM)>0` and every `0<eps<=1`, either

`int |phi_Q| <= C_F eps^(-1/2) Z^(-1/6)`,
`C_F=9 pi sqrt(3)e 6^(1/6)<179.449`,

or

`s4(M)<eps^(1/6) Z^(1/6)`.

Finally I use fleet02/B02's deterministic `QFORM-JOINT-STAR-BLOCK-COMPILER-v1` from the designated partner report above in Section 5.

## 2. Main new perturbative theorem

### Theorem 2.1 — `QFORM-VOLUME-STABILITY-THREEQUARTER-GAP-v1`

Let `M=A[I,J]` be an ORIGINAL-coordinate physical cross block and suppose

`M=M0+E`, `rank(M0)=3`, `rho=s3(M0)>0`.

Fix `0<gamma<=1`. Assume that in one physical orientation the rank-three core range projection `P` satisfies

`max_i P_ii <= 3/4-gamma`.                                           (2.1)

Put

`tau_gamma = gamma/(4 sqrt(3)+gamma)`.                              (2.2)

If

`||E||op <= tau_gamma rho`,                                         (2.3)

then the full quadratic form has

`boxed{
 int_R |phi_Q(t)| dt
 <= [6 pi e]/[gamma sqrt((3-gamma)/2)(1-tau_gamma) rho].
}`                                                                    (2.4)

Consequently its density is continuous, vanishes at infinity, and

`boxed{
 ||p_Q||infinity
 <= [3e]/[gamma sqrt((3-gamma)/2)(1-tau_gamma) rho].
}`                                                                    (2.5)

Exactly the same conclusion holds if (2.1) is true for the COLUMN range of `M0`, by applying the theorem to `M^T`, which is the same physical cross interaction with the two independent coordinate banks exchanged.

#### Proof

Let `kappa=s3(M)`. Weyl gives

`kappa >= (1-tau_gamma)rho`.                                        (2.6)

The partner projection inequality gives

`sqrt(alpha_i) <= sqrt(l_i)+d sqrt(1-l_i)`,
`d <= sqrt(3) tau_gamma/(1-tau_gamma)=gamma/4`.                      (2.7)

Squaring and using `2sqrt(l(1-l))<=1`, `1-l<=1` gives

`alpha_i <= l_i+d+d^2`.

Because `l_i<=3/4-gamma`, `d<=gamma/4`, and `gamma<=1`,

`alpha_i
 <=3/4-gamma+gamma/4+gamma^2/16
 <=3/4-11gamma/16
 < 3/4-gamma/2`.                                                     (2.8)

Choose

`q=(3-gamma)/2`.                                                     (2.9)

Then `1<=q<3/2` and

`q/2=3/4-gamma/4 > 3/4-gamma/2 >= max_i alpha_i`.                    (2.10)

Thus the designated partner's q-dependent sharp-Hausdorff--Young theorem applies to the ACTUAL block `M`:

`int |phi_Q|
 <=2pi C(q) Z^(-1/6)`                                               (2.11)

with `Z=e3(M^TM)`. Since

`Z>=s1(M)^2 s2(M)^2 s3(M)^2>=kappa^6`,                              (2.12)

we have `Z^(-1/6)<=kappa^(-1)`. Also `3-2q=gamma`. Substitution into (2.11), followed by (2.6), gives exactly (2.4); division by `2pi` gives (2.5). QED.

### Concrete scale

For example, if the core one-sided leverage is at most `1/2` then `gamma=1/4` is admissible. Here

`tau_(1/4)=0.034827657...`,

and (2.4)-(2.5) give

`int |phi_Q| <181.093/rho`, `||p_Q||infinity<28.822/rho`

whenever the tail is at most `0.03483 rho`. The point is not this numerical constant; it is that the allowable leverage can now be arbitrarily close to `3/4` provided the rank-three approximation is correspondingly accurate.

## 3. Collapse theorem + Theorem 2.1 closes every strict one-sided leverage gap below 3/4

### Theorem 3.1 — `QFORM-RANK3-COLLAPSE-ONE-SIDED-LEVERAGE-CLOSURE-v1`

Let `M=A[I,J]` be any physical cross block with

`Z=e3(M^TM)>0`, `rho=s3(M)>0`,

and let `M3` be its best rank-three approximation. Let

`L_row=max_i (P_range(M3))_ii`,
`L_col=max_j (P_range(M3^T))_jj`.

If

`min(L_row,L_col)<3/4`,                                             (3.1)

then

`boxed{ phi_Q in L1(R). }`                                          (3.2)

Hence the full quadratic form has a bounded continuous density vanishing at infinity.

More quantitatively, choose any `gamma>0` with

`min(L_row,L_col) <=3/4-gamma`,                                     (3.3)

put `tau=tau_gamma` from (2.2), and define

`eps = min{1, (tau rho/Z^(1/6))^6}`.                                (3.4)

Then

`boxed{
 int |phi_Q|
 <= max(
   C_F eps^(-1/2) Z^(-1/6),
   6pi e/[gamma sqrt((3-gamma)/2)(1-tau)rho]
 ).
}`                                                                    (3.5)

#### Proof

Apply the preceding B02 Fourier-or-rank-three-collapse theorem at the `eps` in (3.4).

If its direct Fourier branch occurs, the first term of (3.5) pays the form.

Otherwise

`||M-M3||op=s4(M)<eps^(1/6) Z^(1/6)<=tau rho`.                       (3.6)

Because `s3(M3)=s3(M)=rho`, condition (3.3) and (3.6) place the ACTUAL physical decomposition `M=M3+(M-M3)` exactly in Theorem 2.1, in whichever orientation realizes the minimum leverage. Its second bound in (3.5) therefore applies. QED.

### Consequence

The previous run left `ell>1/2` as a perturbative leverage residue. The actual threshold after optimizing the same partner Fourier theorem is `3/4`, not `1/2`. Qualitatively, every near-rank-three physical block whose core is not simultaneously three-quarter-heavy on both sides is now paid in unweighted `L1_t`.

This is a mechanism change rather than a repeated constant optimization: the collapse parameter is now chosen adaptively from the leverage gap, so the perturbative tail is made as small as needed to cross the sharp-HY `3/4` barrier.

## 4. Exact determinant-factorization in the remaining two-sided heavy core

Suppose now the rank-three core itself has

`L_row>=3/4`, `L_col>=3/4`.                                         (4.1)

Write its thin SVD

`M3=U Sigma V^T`, `U^T U=V^T V=I_3`,

and let

`Gamma=det Sigma=s1(M3)s2(M3)s3(M3)>=rho^3`.                        (4.2)

Choose physical row `i` and physical column `j` with leverages

`ell_i=||U_i||^2>=3/4`, `m_j=||V_j||^2>=3/4`.                       (4.3)

For physical triples `S,T`, exact rank three gives

`det M3[S,T]=det(U_S) Gamma det(V_T)`.                              (4.4)

Therefore the determinant-squared third-minor law FACTORIZES into independent row and column projection-DPP laws:

`w_ST=det(U_S)^2 det(V_T)^2`.                                       (4.5)

In particular

`P(i in S)=ell_i`, `P(j in T)=m_j`,

and, more strongly than the generic union-bound estimate,

`P(i in S, j in T)=ell_i m_j >=9/16`.                               (4.6)

Thus the anchored third-minor mass of the core obeys

`boxed{ J_ij(M3) >= (9/16) Gamma^2 >= (9/16)rho^6. }`               (4.7)

This is an exact structural identity in the ORIGINAL physical coordinates. No random variables are rotated.

## 5. Apply the designated partner joint-star compiler to the heavy core

Write the selected-row/selected-column decomposition of the rank-three core as

`M3 = [ a0   r0^T ]
      [ c0    N0  ]`.                                               (5.1)

The designated fleet02/B02 `QFORM-JOINT-STAR-BLOCK-COMPILER-v1` gives

`sqrt(J_ij(M3))
 <= |a0| sqrt(E2(N0))
    +||c0||||r0|| ||P_(c0^perp) N0 P_(r0^perp)||F`.                 (5.2)

Hence one of the two terms on the right is at least half of `sqrt(J_ij)`. Combining with (4.7) yields the universal-scale rank-three-core dichotomy

`boxed{
 a0^2 E2(N0) >= 9 rho^6/64
}`                                                                    (5.3)

or

`boxed{
 ||c0||^2 ||r0||^2
 ||P_(c0^perp) N0 P_(r0^perp)||F^2
 >=9 rho^6/64.
}`                                                                    (5.4)

This is the required application of a completed designated-partner result to an actual inequality in the surviving branch.

Equation (5.3) is a physical-edge times aggregate residual two-volume resource. Equation (5.4) is a two-physical-stars times transverse Frobenius resource. Importantly, neither chooses or inverts one small local minor.

The core is only a deterministic approximation to the actual cross block, so (5.3)-(5.4) are NOT by themselves promoted to a probability-density theorem. The live correction against generic operator-norm perturbation continuity is exactly why the remaining step must retain the actual tail inside a proved Fourier/small-ball transducer rather than simply erase it.

## 6. First unpaid implication after this run

The first unpaid interface is now

`QFORM-TWOSIDED-THREEQUARTER-CORE-RESOURCE-ROBUSTIFICATION-v1`:

> In the collapse branch, where the best rank-three physical core has both a row and a column leverage at least 3/4, use either the core resource (5.3) or (5.4), together with the actual small operator tail, inside a source-valid physical-edge + aggregate-E2 or mixed-hub/two-star transducer. The tail must be retained; no generic distributional continuity in matrix norm and no fixed-good-minor payment is allowed.

A second acceptable exit is to show that the actual block itself returns to a paid D'/D5/three-sample volume branch before this robustification is needed.

This is strictly narrower than the preceding `high-leverage or small-third-singular` residue. The small-third-singular part is absorbed by choosing the collapse parameter adaptively; only simultaneous two-sided 3/4-heavy core geometry survives.

## 7. Stronger global Fourier criterion

No target-valid counterexample to

`int_R |E exp(it X^T A X)| dt <= C`

was found. The target-wide universal L1 bound therefore remains `OPEN_NOT_REFUTED`. The present theorem proves qualitative `L1_t` for a substantially larger near-rank-three region, with explicit geometry-dependent constants, but it does not derive a universal lower bound for `rho` or a universal leverage gap from the bare three-large-eigenvalue hypothesis.

Full bounded density remains OPEN. Full continuity remains OPEN. Continuity is proved on all branches in Sections 2-3.

## 8. Verification status

All arguments above are symbolic. The only numerical values quoted are evaluations of exact elementary constants. Independent end-to-end review of Theorems 2.1 and 3.1 has not yet been performed.

MODEL: GPT-5.6 Sol. THINKING LEVEL: UNKNOWN / not exposed. Provider reasoning-token and thinking-time counters: NOT_EXPOSED.
