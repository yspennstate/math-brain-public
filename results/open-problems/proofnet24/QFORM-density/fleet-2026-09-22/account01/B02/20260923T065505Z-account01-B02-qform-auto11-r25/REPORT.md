SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T06:55:05Z.
attacking: integrated Fourier estimate — turn the three-sample near-coloop obstruction into a quantitative operator-near-rank-three alternative, then apply the designated account02/B02 stability theorem.

# account01/B02 r25 — Fourier-or-rank-three spectral-collapse theorem

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains open. This run proves a new quantitative dichotomy for every ORIGINAL-coordinate physical cross block with positive third exterior volume: either the full characteristic function is already in unweighted `L^1`, or that physical cross block is quantitatively close in operator norm to rank at most three. The low-rank alternative is then fed into the completed account02/B02 perturbative Fourier theorem at an actual inequality. No law-uniform pointwise oscillatory decay, post-rotation independence, arbitrary-joint coarea, fixed-good-minor selection, compact support, moments, or log-concavity is used.

Continuity is proved on every branch where the `L^1_t` conclusion is obtained. It is not asserted for the full target.

## 1. Sources used at equations

Fresh owner control was resolved from `yspennstate/math-research-brain` main; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. I consumed the live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, `PROTOCOL.md`, and this B02 assignment before deriving the result, and refreshed control before this publication.

The designated partner result used first is account02/B02:

- `yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T050831Z-account02-B02-QFORM-auto11-f98b4bb5/REPORT.md`.

Its two inputs used below are:

1. `QFORM-TRIPLE-DISJOINT-VOLUME-COMPILER-v1`. For a physical cross block `M`, let `Z=E3(M)=e3(M^T M)>0`, let `mu` be its determinant-squared row-triple law, take iid `R1,R2,R3~mu`, and put

   `delta3=P(R1 cap R2 cap R3=empty)`.

   If `delta3>0`, then the full quadratic form has a continuous density and

   `||p_Q||inf <= (9 sqrt(3)e/2) delta3^(-1/6) Z^(-1/6)`.

   The proof is by an integrable characteristic-function envelope, so equivalently the explicit envelope integrates to

   `int_R |phi_Q(t)|dt <= 9 pi sqrt(3)e delta3^(-1/6) Z^(-1/6)`.

2. `QFORM-TRIPLE-INTERSECTION-STABILITY-v1`. For `0<eps<1`, put

   `eta=delta3/eps`, `tau=eta/[2(eps-eta)^2]`.

   If `eta<eps` and `tau<=1/2`, then either some physical row `i` satisfies

   `E3(M[-i,:])<eps Z`,

   or some physical row set `H`, `|H|<=4`, satisfies

   `E3(M[H,:]) >= (1-eta-5tau)Z`.

I also use the completed exact-rank-three physical-cross-block theorem

- `yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T230126Z-account03-B02-QFORM-r17/REPORT.md`,

which states that if a physical cross block has exact rank three and the product of its nonzero singular values is `Gamma`, then

`int |phi_Q| <=12 pi Gamma^(-1/3)`, `||p_Q||inf<=6 Gamma^(-1/3)`.

Finally, the designated account02/B02 perturbative result actually applied in Section 4 is

- `yspennstate/math-open-problems@f7a221e0f40362a1ccad48cf81812f2143f3cc92`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T020523Z-account02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`.

Its theorem `QFORM-VOLUME-STABILITY-OPTIMAL-Q-v1` says: if a physical cross block decomposes as `M=M0+E`, with `s3(M0)>=rho>0`, maximum row-range leverage of `M0` at most `1/2`, and `||E||op<=rho/16`, then

`||p_Q||inf <15.247/rho`,

and the proof gives

`int |phi_Q| <95.799/rho`.

All same-bank quadratic phases and outside couplings are retained in those source theorems.

## 2. New spectral-collapse lemma

### Lemma 2.1 — `QFORM-ROW-DELETION-E3-SPECTRAL-COLLAPSE-v1`

Let `M` be any real matrix and let `N=M[-i,:]` be obtained by deleting one row. If

`E3(N)=e3(N^T N) <= delta`,

then

`boxed{ s4(M) <= s3(N) <= delta^(1/6). }`                                  (2.1)

In particular, if `E3(N)<eps E3(M)` and `Z=E3(M)>0`, then

`boxed{ dist_op(M,{rank<=3})=s4(M)<eps^(1/6) Z^(1/6). }`                    (2.2)

#### Proof

Write the singular values of `N` as `u1>=u2>=u3>=...>=0`. Cauchy--Binet / the elementary symmetric singular-value identity gives

`E3(N)=sum_(a<b<c) ua^2 ub^2 uc^2 >= u1^2 u2^2 u3^2 >= u3^6`,

because `u1,u2>=u3`. Hence `s3(N)=u3<=delta^(1/6)`.

Deleting one row is a codimension-one compression of `MM^T`. Cauchy interlacing therefore gives

`s4(M)^2 <= s3(N)^2`.

This proves (2.1). Eckart--Young gives `dist_op(M,{rank<=3})=s4(M)`, proving (2.2). No coordinate change is made to the random variables. QED.

This elementary observation is the key new bridge: a near-coloop statement expressed in third exterior volume is automatically a quantitative operator-near-rank-three statement, with the scale-correct exponent `1/6`.

## 3. Main theorem: Fourier or operator-near-rank-three

### Theorem 3.1 — `QFORM-E3-FOURIER-OR-RANK3-COLLAPSE-v1`

Let `M=A[I,J]` be any ORIGINAL-coordinate physical cross block of the full quadratic form, with

`Z=E3(M)>0`.

All self blocks, outside couplings and affine terms may be arbitrary. For every `0<eps<=1`, at least one of the following holds:

**(F) Integrated-Fourier exit**

`boxed{
 int_R |phi_Q(t)|dt
 <= C_F eps^(-1/2) Z^(-1/6),
}`                                                                    (3.1)

where

`C_F=9 pi sqrt(3)e 6^(1/6)=179.448307459...<179.449`.

Hence this branch has a continuous density vanishing at infinity and

`||p_Q||inf <= C_F/(2pi) eps^(-1/2)Z^(-1/6)
             <28.561 eps^(-1/2)Z^(-1/6)`.

**(R3) Spectral-collapse exit**

`boxed{
 s4(M)<eps^(1/6) Z^(1/6).
}`                                                                    (3.2)

Equivalently, there exists a rank-at-most-three coefficient matrix `M3` in the same physical row/column coordinates such that

`||M-M3||op<eps^(1/6)Z^(1/6)`.

#### Proof

Let `delta3` be the partner's three-sample common-intersection failure probability.

### Case 1: `delta3 >= eps^3/6`

Apply the account02/B02 three-sample compiler directly:

`int |phi_Q|
 <=9 pi sqrt(3)e delta3^(-1/6)Z^(-1/6)
 <=9 pi sqrt(3)e 6^(1/6)eps^(-1/2)Z^(-1/6)`.

This is (F).

### Case 2: `delta3 < eps^3/6`

Use the partner stability theorem with the same parameter `eps`. Then

`eta=delta3/eps <eps^2/6<eps`.

Moreover

`eps-eta > eps(1-eps/6) >=(5/6)eps`,

so

`tau=eta/[2(eps-eta)^2]
    <(eps^2/6)/(2*(25/36)eps^2)=3/25<1/2`.

Thus the stability theorem applies. There are two subcases.

#### Case 2a: near coloop

Some row deletion `N=M[-i,:]` obeys

`E3(N)<eps Z`.

Lemma 2.1 gives immediately

`s4(M)<eps^(1/6)Z^(1/6)`,

which is (R3).

#### Case 2b: four-row concentration

Some `H`, `|H|<=4`, obeys

`E3(M[H,:]) >=(1-eta-5tau)Z`.

The estimates above give

`eta<1/6`, `tau<3/25`, hence

`1-eta-5tau >1-1/6-3/5=7/30`.

By Cauchy--Binet,

`E3(M[H,:])
 =sum_(R subset H, |R|=3) det(M[R,:]M[R,:]^T)`.

There are at most four row triples. Therefore some physical triple `R` has

`det(M[R,:]M[R,:]^T) > (7/120)Z`.                                  (3.3)

The physical block `M[R,:]` has exactly three rows and rank three. If `Gamma_R` is the product of its three nonzero singular values, then

`Gamma_R^2=det(M[R,:]M[R,:]^T)>(7/120)Z`.

Apply the exact-rank-three cross-block theorem:

`int |phi_Q|
 <12pi(120/7)^(1/6)Z^(-1/6)
 =60.535711760... Z^(-1/6)`.

Since `eps<=1`, this is strictly below `C_F eps^(-1/2)Z^(-1/6)`. Hence (F) holds. QED.

### What the theorem changes

The preceding non-coloop estimate deteriorated like `(1-h)^(-1/2)` as a third-volume row marginal `h` approached one. The new theorem identifies the exact geometric meaning of that deterioration: if the Fourier compiler cannot pay at a chosen scale `eps`, the physical cross block must be within operator distance `eps^(1/6) Z^(1/6)` of rank three. Thus the near-coloop collar is no longer merely a combinatorial high-marginal state; it is a quantitative spectral-collapse state in the original physical coordinates.

The theorem is deliberately scale-parametric. Sending `eps` downward improves the rank-three approximation; the only cost is the explicit `eps^(-1/2)` on the alternative Fourier exit.

## 4. Actual application of the designated account02/B02 stability theorem

Let `M3` be a best rank-three approximation to `M` and write

`M=M3+E`, `||E||op=s4(M)`.

Put

`rho=s3(M3)=s3(M)>0`,
`ell=max_i (P_range(M3))_ii`.

Assume the rank-three core is physically diffuse,

`ell<=1/2`,                                                                  (4.1)

and choose `eps` so that

`16 eps^(1/6) Z^(1/6) <=rho`.                                                (4.2)

Apply Theorem 3.1.

- If (F) occurs, we already have the explicit unweighted Fourier bound (3.1).
- If (R3) occurs, then

  `||E||op=s4(M)<eps^(1/6)Z^(1/6)<=rho/16`.

  Conditions (4.1)--(4.2) therefore place the *actual physical decomposition* `M=M3+E` exactly inside account02/B02's `QFORM-VOLUME-STABILITY-OPTIMAL-Q-v1`. Hence

  `boxed{ int |phi_Q(t)|dt <95.799/rho, }`                            (4.3)

  and

  `boxed{ ||p_Q||inf <15.247/rho. }`                                 (4.4)

This is the required application of a completed designated-partner result to an actual inequality. The small tail is not discarded; it is retained and paid by the partner perturbative theorem.

Consequently, for every physical cross block with `Z>0`, the only part not covered by this Fourier-or-stability synthesis at a chosen scale `eps` is quantitatively explicit:

`ell>1/2` (a high-coordinate-leverage rank-three core), or

`rho<16 eps^(1/6)Z^(1/6)` (the third core singular direction is itself at the collapse scale).

These are structural, not analytic, residues.

## 5. Relation to the exact target

This theorem does not prove that the bare hypothesis `s3(A)>=1` supplies a physical cross block with `Z`, `rho`, and leverage satisfying a universal lower/upper package. Existing source-valid counterexamples forbid simply choosing one uniformly conditioned minor or asserting a rank-three cross cut.

It does, however, remove a full layer of the integrated-Fourier obstruction: **for a live physical cross block, arbitrary near-coloop concentration is now either paid directly in `L1_t` or converted to a quantitative near-rank-three matrix to which the existing stability theorem applies whenever its core is diffuse.** No fifth compound, no single local minor, and no pointwise oscillatory estimate are required for this reduction.

The first unpaid implication is therefore

`QFORM-HIGH-LEVERAGE-OR-THIRD-SINGULAR-COLLAPSE-ROUTING-v1`:

starting from a physical cross block produced by the global aggregate geometry, route the surviving high-leverage core (`ell>1/2`) or the small-third-singular core (`rho<16 eps^(1/6)Z^(1/6)`) into the proved original-coordinate rank-two-affine, strong-star/mixed-hub, scalar-square, grouped-bank, pair-log, or ridge mechanisms, without paying a vanishing fixed minor. The new determinant-area receiver from account03/B01 is potentially compatible with the rank-two-dominant side, but its one-sided-affine hypotheses must be checked before use; it is not silently applied here.

## 6. Stronger global Fourier criterion

I found no target-valid counterexample to

`int_R |E exp(it X^T A X)|dt <= C`

under the full three-large-eigenvalue assumptions. The theorem above gives a new quantitative reason the counterexample search is difficult: every physical third-volume packet either has an explicit `L1_t` certificate or collapses spectrally toward the already-paid exact-rank-three endpoint. The target-wide universal `L1_t` statement therefore remains `OPEN_NOT_REFUTED`.

Full bounded density remains OPEN. Full continuity remains OPEN. Continuity is proved only on the explicit Fourier branches above.

## 7. Verification status

The proof of Lemma 2.1 and Theorem 3.1 is symbolic. Numerical computation was used only to evaluate displayed constants:

`C_F=179.448307459...`,
`12pi(120/7)^(1/6)=60.535711760...`.

No numerical experiment is used as proof. Independent end-to-end review of this new theorem has not yet been performed.

MODEL: GPT-5.6 Sol. THINKING LEVEL: UNKNOWN / not exposed; maximum supported was requested by owner control. Provider reasoning-token and thinking-time counters are not exposed.
