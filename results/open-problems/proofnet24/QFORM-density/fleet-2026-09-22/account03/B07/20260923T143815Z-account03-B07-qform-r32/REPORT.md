SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T14:38:15Z.
attacking: the r30/r31 disjoint-bank survivors — convert cancellation of the selected matching products into determinant-weighted opposite-block rank-one tubes, without ever paying the reciprocal of one small physical minor.

# account03/B07 r32 — determinant-weighted bank-cycle pivot averaging

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T143815Z-account03-B07-qform-r32`  
Fresh main observed during work: `yspennstate/math-research-brain@8562b09b54674f8cafc89f0ee42819e5d3f983f3`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW DETERMINANT-WEIGHTED FOUR-BANK COMPILER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussian, moment, compact-support, log-concavity, connected-support, diagonal-basis, or post-rotation independence assumption is introduced. Every bank below is a subset of the original independent coordinates. No pointwise van-der-Corput envelope, fiber supremum, conditional projection-density moment, or uniformly good fixed physical minor is used.

## 1. Incoming B07 packets

The immediate source is

`yspennstate/math-open-problems@8c451bd5a80de0cee1aefcf6f4cca79766652bcc`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T140748Z-account03-B07-qform-r31/REPORT.md`.

Its small-anchor / aggregate-`E_2` branch gives four mutually disjoint ORIGINAL-coordinate banks `L_1,L_2,R_1,R_2` and, after relabeling the better matching,

`A=H[L_1,R_1]`, `D=H[L_2,R_2]`,

with

`P:=||A||_F ||D||_F > K a^2`,
`K=1.076074733e6`.                                             (1.1)

The crossed blocks

`B=H[L_1,R_2]`, `C=H[L_2,R_1]`                                (1.2)

remain present and may be arbitrarily large. The point of this run is to account for their possible cancellation rather than silently delete them.

The preceding r30 six-bank sibling is

`yspennstate/math-open-problems@0942d044043f3a73e2411cf2676af89bbf3853e6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T130749Z-account03-B07-qform-r30/REPORT.md`.

There, in addition to the same kind of four residual banks, two disjoint star banks have norms `S_L,S_R` and

`S_L S_R ||A||_F ||D||_F > a^4/(864 sqrt(6))`.                 (1.3)

## 2. Cross-rectangle determinant mass

For arbitrary real matrices with compatible sizes

`A in R^{p x r}`, `B in R^{p x s}`,
`C in R^{q x r}`, `D in R^{q x s}`,                            (2.1)

define the cross-rectangle determinant mass

`Omega(A,B,C,D)
 := sum_{i,k,j,l} (A_ij D_kl - B_il C_kj)^2`.                  (2.2)

For the physical bank decomposition (1.1)-(1.2), every summand is the square of a literal ORIGINAL-coordinate `2 x 2` minor of `H`, with one row from each `L` bank and one column from each `R` bank. Thus

`Omega <= E_2(H)`                                               (2.3)

with no basis rotation.

Write

`alpha=||A||_F`, `beta=||B||_F`,
`gamma=||C||_F`, `delta=||D||_F`.                              (2.4)

Expansion gives the exact identity

`Omega = alpha^2 delta^2 + beta^2 gamma^2 - 2 T`,              (2.5)

where

`T = sum A_ij D_kl B_il C_kj
   = <B, A C^T D>_F`.                                          (2.6)

By repeated Hilbert-Schmidt/operator Cauchy-Schwarz,

`|T| <= alpha beta gamma delta`.                                (2.7)

Therefore

`boxed: sqrt(Omega) >= |alpha delta - beta gamma|`.             (2.8)

This already shows that if the selected matching `alpha delta` is large but determinant mass is small, then the crossed matching `beta gamma` must be comparably large. More importantly, the same determinant weights yield a dimension-free *averaged pivot* statement below.

## 3. Main theorem: determinant-weighted bank-cycle pivot averaging

### Theorem 3.1 — `QFORM-BANKCYCLE-AVERAGED-PIVOT-v1`

Assume `alpha delta>0` and fix `0<eps<1`. Then one of the following holds.

**(I) Aggregate cross-minor branch**

`boxed: sqrt(Omega) >= eps alpha delta`.                        (3.1)

**(II) Four-block rank-one-tube branch**

All four physical blocks lie in quantitative Frobenius tubes around rank-one matrices:

`dist_F(A,rank<=1) < eps alpha`,                                (3.2)
`dist_F(D,rank<=1) < eps delta`,                                (3.3)
`dist_F(B,rank<=1) < [eps/(1-eps)] beta`,                       (3.4)
`dist_F(C,rank<=1) < [eps/(1-eps)] gamma`.                      (3.5)

Moreover every approximant can be chosen from actual physical slices of the other three blocks. In particular, there is a nonzero physical entry `A_ij` such that

`boxed:
 ||D - C[:,j] B[i,:]/A_ij||_F <= sqrt(Omega)/alpha`.            (3.6)

There is likewise a nonzero `D_kl` with

`||A - B[:,l] C[k,:]/D_kl||_F <= sqrt(Omega)/delta`,            (3.7)

a nonzero `B_il` with

`||C - D[:,l] A[i,:]/B_il||_F <= sqrt(Omega)/beta`,             (3.8)

and a nonzero `C_kj` with the symmetric estimate for `B`.

Crucially, (3.6)-(3.8) are structural certificates only: no analytic step pays `1/|A_ij|`, `1/|B_il|`, etc. A selected pivot may be arbitrarily tiny. Its determinant weight is what cancels the reciprocal in the averaged residual estimate.

### Proof

For each `(i,j)`, let

`Omega_ij^A := sum_{k,l} (A_ij D_kl-B_il C_kj)^2`.              (3.9)

Then

`sum_{i,j} Omega_ij^A = Omega`.                                 (3.10)

For `A_ij !=0`,

`Omega_ij^A/A_ij^2
 = ||D-C[:,j]B[i,:]/A_ij||_F^2`.                               (3.11)

Choose a pivot at random with determinant weights

`P{(i,j)}=A_ij^2/alpha^2`.                                     (3.12)

Zero entries carry zero probability. Taking expectation in (3.11),

`E[Omega_ij^A/A_ij^2] = Omega/alpha^2`.                         (3.13)

Hence some nonzero actual physical pivot satisfies (3.6), and therefore

`dist_F(D,rank<=1) <= sqrt(Omega)/alpha`.                       (3.14)

The same argument weighted by `D_kl^2/delta^2` gives

`dist_F(A,rank<=1) <= sqrt(Omega)/delta`.                       (3.15)

If (I) fails, (3.14)-(3.15) imply (3.2)-(3.3). Also (2.8) gives

`beta gamma > (1-eps) alpha delta`.                             (3.16)

Now repeat the weighted-pivot argument with `B`. For `B_il !=0`,

`sum_{k,j}(A_ijD_kl-B_ilC_kj)^2/B_il^2
 = ||C-D[:,l]A[i,:]/B_il||_F^2`.                               (3.17)

Averaging with weights `B_il^2/beta^2` gives

`dist_F(C,rank<=1) <= sqrt(Omega)/beta
 < eps alpha delta/beta
 < [eps/(1-eps)] gamma`.                                       (3.18)

The `C`-weighted argument gives (3.4). This proves the theorem. No dimension enters.

## 4. Concrete `eps=1/8` compiler

Taking `eps=1/8`, every four-bank product `P=alpha delta` obeys the exhaustive alternative

`boxed: sqrt(Omega) >= P/8`,                                   (4.1)

or

`boxed:
 dist_F(A,R_1)<alpha/8,
 dist_F(D,R_1)<delta/8,
 dist_F(B,R_1)<beta/7,
 dist_F(C,R_1)<gamma/7`,                                       (4.2)

where `R_1` denotes matrices of rank at most one.

Thus cancellation of a large selected matching cannot simply erase determinant currency. It forces the entire `2 x 2` bank cycle into four simultaneous rank-one tubes.

## 5. Application to the r31 huge-`E_2` matching branch

Insert (1.1) into (4.1). Either

`boxed:
 sqrt(Omega) > (K/8) a^2
              = 134509.341625 a^2`,                            (5.1)

so an aggregate bank of literal physical `2 x 2` minors carries enormous mass, or all four physical subblocks satisfy the simultaneous tubes (4.2).

This is strictly stronger information than retaining only `B_1B_2`: it identifies the exact obstruction to converting the selected matching product into minors, namely coherent rank-one cancellation across the full four-block cycle.

### 5.1 Designated partner account04/B07 applied to an actual inequality

The completed designated partner is

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T091740Z-account04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

It supplies

`h=(2sqrt(2)-1)/1572864`,                                      (5.2)

and in the same strict-N3 chamber the physical coefficient cap

`|A_uv| <= h/8` for off-diagonal original-coordinate entries.  (5.3)

The inherited B07 scale floor is

`a/h > r0=16 sqrt((sqrt(63)/16)/4617)
          =0.1658498913771345...`.                             (5.4)

Therefore (1.1) becomes the actual partner-scale inequality

`boxed: P > 29598.7122613461 h^2`.                             (5.5)

On the determinant branch (5.1),

`boxed: sqrt(Omega) >3699.83903266826 h^2`,                    (5.6)

hence

`Omega >1.36888088676555e7 h^4`.                              (5.7)

Every determinant in (2.2) has modulus at most

`2(h/8)^2=h^2/32`,                                             (5.8)

so each squared term is at most `h^4/1024`. Consequently the physical determinant branch contains at least

`boxed: 14,017,340,281`

nonzero cross-rectangle `2 x 2` minors.                         (5.9)

This count is not used as a Monte Carlo or interval-extremality argument. It is a deterministic consequence of the partner's physical coefficient cap and the aggregate determinant mass. It shows that this branch is necessarily genuinely diffuse rather than supported by one exceptional coordinate minor.

## 6. Application to the r30 six-bank sibling

In the six-bank packet (1.3), let `P=alpha delta` denote the matched residual-block product. Applying (4.1) gives either

`S_L S_R sqrt(Omega)
 > a^4/(6912 sqrt(6))`,                                        (6.1)

which is now a **star-star times aggregate physical second-minor** packet, or all four residual bank blocks satisfy the simultaneous rank-one tubes (4.2).

Thus the r30 six-bank branch has been reduced without selecting an individual determinant to:

`aggregate 2x2-minor bank + two independent star banks`

or

`two star banks + a four-block coherent rank-one cycle`.        (6.2)

The latter is the only cancellation geometry left by this compiler.

## 7. Why this respects the source corrections

The theorem never claims that a bounded projection density controls an arbitrary indefinite quadratic pushforward. It never rotates random coordinates. It never conditions on a variable and then reuses an unconditional density cap. It does not infer a universal pointwise oscillatory envelope. Most importantly, it does not select a tiny minor and pay its reciprocal: the only divisions in (3.6)-(3.8) define rank-one approximants, and the determinant-weighted average makes the residual bounds independent of the selected pivot magnitude.

The strict-N3 partner coefficient cap is used only in the deterministic count (5.9), not as an analytic density receiver.

## 8. Exact remaining implication

The first B07 debt is now

`QFORM-BANKCYCLE-R1-OR-AGGREGATE-E2-CURVATURE-RECEIVER-v1`:

1. consume the aggregate determinant branch (5.1) or (6.1) while retaining arbitrary same-bank curvature and the true ambient remainder; or
2. consume the simultaneous four-block rank-one tubes (4.2), using their common physical slice provenance rather than replacing the blocks by their rank-one approximants and deleting the nonzero tails.

The r31 star/core and punctured-hub siblings remain separate. A promising interface is the fresh global low-rank / one-hub machinery from account03/B01, but no claim is made here that four local bank tubes already satisfy its global diagonal-plus-low-rank hypothesis.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** No continuity statement is obtained by Theorem 3.1 itself.

## 9. Source pins

- fresh research-brain main consumed during the run: `8562b09b54674f8cafc89f0ee42819e5d3f983f3`;
- prior B07 r31: `math-open-problems@8c451bd5a80de0cee1aefcf6f4cca79766652bcc`;
- prior B07 r30: `math-open-problems@0942d044043f3a73e2411cf2676af89bbf3853e6`;
- designated partner account04/B07: `math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`;
- fresh account03/B01 global low-rank handoff observed at research-brain main `8562b09b54674f8cafc89f0ee42819e5d3f983f3`, canonical math source `math-open-problems@ed79f4a518a9f683a679d70193d6a2a72fb05ff2`.

A deterministic checker accompanies this report. It verifies the exact expansion, Cauchy lower bound, weighted-pivot residual inequalities on random finite matrices, and all numerical constants. The checker is regression evidence only; the proof above is algebraic.
