SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T00:21:08Z.
attacking: Schur-reserve transport for arbitrary signed spectral packets, with a high/low spectral split and a partner rank-one-self receiver on the actual final matrix.

# account01/B12 — Schur-reserve transport for arbitrary signed eigenvalue additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T002108Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **not proved in this branch**; the conclusion obtained below is essential boundedness only.

## 1. What this run changes

The previous B12 runs paid several special geometries (polar cones, square-energy carriers, hard low-rank footprints, Gram defects, commuting replacements, carrier-relative gains, Schur gauge directions, and hub-aligned packets). This run changes mechanism. It uses an exact **Schur-complement transport identity** for an arbitrary signed spectral packet and shows that, after a fixed original-coordinate pivot is eliminated, the packet is charged only by the rank of its **Schur graph residual**. Its eigenvalue magnitudes do not enter the singular-value reserve loss at all.

The same identity yields a high/low spectral reduction: all spectral modes above a threshold are paid by Schur-residual rank, while all modes below the threshold are paid simultaneously by one operator-norm tail. No rotated random coordinates are used and no quadratic remainder is convolved independently.

The first unpaid implication remains structural: the bare hypothesis `s_3(A)>=1` does not yet force a pivot/bank decomposition with enough Schur singular-value reserve and controlled residual rank (or one of the other completed exits).

## 2. Exact signed spectral-packet identity

Let `I` be a set of ORIGINAL coordinates and write a symmetric matrix in the physical decomposition `I | I^c` as

`A_0 = [[C,B],[B^T,D]]`,                                         (2.1)

where `C` is invertible. Let an arbitrary symmetric spectral packet be

`E=U Theta U^T`,                                                  (2.2)

where `Theta=Theta^T` may be indefinite and may have eigenvalues of arbitrary magnitude. Split the rows of `U` as

`U=[U_0;U_1]`,                                                    (2.3)

according to `I | I^c`, and assume only that the updated physical pivot

`C_1=C+U_0 Theta U_0^T`                                          (2.4)

is invertible. Define

`S_0 = D-B^T C^{-1}B`,                                           (2.5)

`Z = U_1-B^T C^{-1}U_0`,                                        (2.6)

and

`K_Theta = Theta-Theta U_0^T C_1^{-1}U_0 Theta`.                 (2.7)

### Theorem 2.1 — `QFORM-SCHUR-SPECTRAL-PACKET-RESERVE-v1`

The Schur complement after the arbitrary signed packet is exactly

`boxed:
 Schur_I(A_0+E)=S_0+Z K_Theta Z^T.`                               (2.8)

If `Theta` is invertible, then equivalently

`K_Theta=(Theta^{-1}+U_0^T C^{-1}U_0)^{-1}`.                     (2.9)

The representation (2.7), unlike (2.9), does **not** require `Theta` to be invertible.

Now partition the physical complement into two disjoint original-coordinate banks `K` and `J`, and let

`M_0=S_0[K,J]`,                                                   (2.10)

`M_1=Schur_I(A_0+E)[K,J]`.                                       (2.11)

Then

`M_1-M_0=Z_K K_Theta Z_J^T`,                                    (2.12)

so

`rho:=rank(M_1-M_0)
 <= min{rank Z_K, rank K_Theta, rank Z_J}
 <= rank(E)`.                                                     (2.13)

For every `q` with `q+rho<=min{|K|,|J|}`,

`boxed: s_q(M_1)>=s_{q+rho}(M_0).`                               (2.14)

Thus an arbitrarily large positive/negative spectral packet costs only `rho` Schur reserve directions. The coefficient `K_Theta` is permitted to be arbitrarily large; its magnitude never appears in (2.14). Near a pivot resonance the theorem remains valid until the physical pivot actually becomes singular.

### Proof

Introduce the baseline physical shear

`T=[[I,-C^{-1}B],[0,I]]`.                                        (2.15)

Direct multiplication gives

`T^T A_0 T = diag(C,S_0)`.                                       (2.16)

Moreover

`T^T U = [U_0; Z]`.                                              (2.17)

Hence

`T^T(A_0+E)T
 = [[C_1, U_0 Theta Z^T],
    [Z Theta U_0^T, S_0+Z Theta Z^T]]`.                          (2.18)

A block upper-triangular pivot shear with identity on the complement leaves the Schur complement invariant. Taking the Schur complement of `C_1` in (2.18) therefore gives

`S_0+Z Theta Z^T
 -Z Theta U_0^T C_1^{-1}U_0 Theta Z^T
 =S_0+Z K_Theta Z^T`,                                            (2.19)

which proves (2.8). If `Theta` is invertible, the Woodbury identity gives (2.9).

Equation (2.12) is the `K x J` block of (2.8). Its rank is bounded by (2.13). The standard rank-`rho` singular-value interlacing inequality

`s_{q+rho}(M_0)<=s_q(M_0+(M_1-M_0))+s_{rho+1}(M_1-M_0)`           (2.20)

has final term zero, proving (2.14). No probability statement is used.

## 3. High/low spectral split, including arbitrary small eigenvalues

The preceding theorem pays the large packet without any bound on the large eigenvalues. The remaining small spectrum can be paid deterministically on the coefficient matrix.

Let the full added matrix be spectrally split at `h>0` as

`F=E_>+T`,                                                        (3.1)

where `E_>` contains all selected modes with `|theta|>h` and `T` contains the remaining modes. Since `T` is symmetric,

`||T||op<=h`,                                                     (3.2)

regardless of its rank, signs, multiplicities, orientation, or dimension.

Apply Theorem 2.1 to `E_>` and call the resulting matrix `A_1=A_0+E_>`. Write its pivot/complement blocks as

`A_1=[[C_1,B_1],[B_1^T,D_1]]`,                                  (3.3)

and assume

`mu:=s_min(C_1)>h`, `R:=||B_1||op`.                              (3.4)

Let `S_1=Schur_I(A_1)` and `S_f=Schur_I(A_1+T)`. Then

`boxed:
 ||S_f-S_1||op <= eps_h`,                                        (3.5)

where

`eps_h
 = h
 + R^2 h/[mu(mu-h)]
 + (2Rh+h^2)/(mu-h).`                                             (3.6)

Indeed, write the blocks of `T` as `[[F,G],[G^T,H]]`. Each has operator norm at most `h`, while

`||(C_1+F)^{-1}|| <=1/(mu-h)`,                                   (3.7)

`||(C_1+F)^{-1}-C_1^{-1}||
 <=h/[mu(mu-h)]`.                                                 (3.8)

Expanding the two Schur complements and applying (3.7)-(3.8) gives (3.5)-(3.6).

Consequently, if `M_f=S_f[K,J]`, then

`boxed:
 s_q(M_f)>=s_{q+rho}(M_0)-eps_h.`                                (3.9)

This is a valid deterministic reduction for simultaneously adding arbitrary **large** and **small** signed eigenvalues. The large packet is charged by Schur-residual rank; the entire small packet is charged once by its spectral threshold. The price is an explicit physical-pivot conditioning requirement. There is no claim that `X^T T X` is small.

## 4. Useful corollary: arbitrary complement spectrum and an unbounded low-rank cross packet

For a scalar physical pivot `I={i}`, suppose an addition `S=S^T` satisfies

`S[i,*]=0`.                                                       (4.1)

Then the pivot and its row are unchanged, while

`Schur_i(A_0+S)-Schur_i(A_0)=S[I^c,I^c]`.                         (4.2)

If `I^c=K union J` and

`rank S[K,J]<=rho`,                                               (4.3)

then

`boxed:
 s_q(Schur_i(A_0+S)[K,J])
 >=s_{q+rho}(Schur_i(A_0)[K,J]).`                                (4.4)

All same-bank blocks `S[K,K]`, `S[J,J]` are completely free for this certificate. In particular `S[J,J]` may have arbitrarily many positive or negative eigenvalues of arbitrarily large magnitude, while the physical cross addition may itself have arbitrary norm.

This corollary is not a convolution statement; it is an exact coefficient identity in the original coordinates.

## 5. Actual application of completed account02/B12 theorem

Dependency actually read and applied:

- repository: `yspennstate/math-open-problems`
- commit: `894dfe1e6cc4817c2b3e0bbe46036e4839f10dbf`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T215456Z-account02-B12-QFORM-auto11b/REPORT.md`
- theorem: `QFORM-RANKONE-SELF-CARRIER-RETENTION-v1`.

That theorem states for an actual final matrix `A=[[C,B],[B^T,D]]` on an original-coordinate carrier `H`, `|H|=m>=3`, if

`lambda_3(C^2+BB^T)>=g^2`,                                      (5.1)

and `C=lambda uu^T+E` with

`c=|lambda|=s_1(C)`, `b=||E||op=s_2(C)`, `c>mb`,                 (5.2)

then for a literal coordinate `i` with `|u_i|>=m^{-1/2}`, putting

`alpha=c/m-b`, `h_i=||B_i||`,                                   (5.3)

one has

`s_2(B#)>=Delta_R1`,                                              (5.4)

`Delta_R1=g-b-[(1+sqrt(m-1))b/alpha]h_i`,                        (5.5)

and if `Delta_R1>0`,

`||p_Q||_(infinity,ess)
 <=2^(11/4) binom(m-1,2)^(1/8)/sqrt(alpha Delta_R1)`.             (5.6)

I now apply it to a family for which the new Schur-reserve theorem supplies the crucial final-matrix carrier inequality.

### 5.1 Baseline

Take `H={1,...,7}` and at least six complementary original coordinates `J_0={j_1,...,j_6}`. Let

`C_0=4 e_1e_1^T`,                                                (5.7)

and let the physical cross block `B_0=A_0[H,J]` have row 1 zero and

`B_0[e_{k+1},j_k]=2`, `k=1,...,6`,                               (5.8)

with all other displayed entries zero. Thus after eliminating the scalar pivot `i=1`,

`M_0=B_0[H\{1},J]=2 I_6`                                        (5.9)

(on the six active complement columns), so every one of its six singular values is `2`.

The complementary self block of `A_0` is arbitrary and plays no role below.

### 5.2 Arbitrary large signed additions

Add an arbitrary symmetric matrix `S` satisfying only

`S[H,H]=0`,                                                       (5.10)

`S[1,J]=0`,                                                       (5.11)

`rank L<=2`, where `L:=S[H\{1},J]`.                              (5.12)

There is **no norm bound** on `L`, and the entire complementary block `S[J,J]` is arbitrary in dimension, sign, rank and magnitude.

The scalar pivot `4` and its cross row remain unchanged. Corollary 4 gives

`s_3(M_0+L)>=s_5(M_0)=2`.                                       (5.13)

This is the first actual inequality supplied by the new theorem. Since row 1 of the full cross block is zero,

`s_3(B_0+S[H,J])>=2`.                                            (5.14)

Therefore for the pre-small-tail matrix `A_*=A_0+S`,

`s_3([C_*,B_*])>=2`,                                             (5.15)

or equivalently

`lambda_3(C_*^2+B_*B_*^T)>=4`.                                  (5.16)

The allowed `S` genuinely contains arbitrary large signed eigenvalues. For example, take `L` of rank two with singular values `tau_1,tau_2`: its symmetric cross dilation contributes eigenvalues `+tau_1,-tau_1,+tau_2,-tau_2`. Independently, a decoupled part of `S[J,J]` may be any diagonal or mixed symmetric spectator block with arbitrarily many prescribed positive and negative eigenvalues of unbounded magnitude.

### 5.3 Arbitrary small signed spectrum

Now add **any** symmetric matrix `T` satisfying

`||T||op<=eta:=1/100`.                                           (5.17)

Equivalently, all eigenvalues of this small packet lie in `[-1/100,1/100]`; its rank, signs, orientation and support are unrestricted. Let

`A=A_*+T`                                                        (5.18)

be the actual final matrix.

On the physical row carrier,

`[C,B]=[C_*,B_*]+P_H T`,                                         (5.19)

so (5.15) and singular-value Weyl give

`g:=s_3([C,B])>=2-eta=1.99`.                                    (5.20)

Also, because `C_*=4e_1e_1^T`,

`c=s_1(C)>=4-eta=3.99`,                                          (5.21)

`b=s_2(C)<=eta=0.01`.                                            (5.22)

Let `u` be the top eigenvector of `C`. Since its top eigenvalue is at least `4-eta`, projection of `Cu=lambda u` onto `e_1^perp` gives

`||u_{e_1^perp}||<=eta/(4-eta)<0.00251`,                         (5.23)

hence `|u_1|>0.99999>1/sqrt(7)`. Thus the partner theorem permits the literal pivot `i=1`. The pre-tail pivot cross row is zero, so

`h_1=||B[1,J]||<=eta=0.01`.                                     (5.24)

Therefore

`alpha=c/7-b
 >=(4-eta)/7-eta
 =0.56`.                                                         (5.25)

Using (5.20)-(5.25) in the completed account02/B12 theorem gives

`Delta_R1
 >=1.99-0.01-(1+sqrt(6))(0.01)^2/0.56
 =1.9793840196887886...`.                                        (5.26)

Hence the **actual final quadratic form**, for every independent product input with scalar densities bounded by one, satisfies

`boxed:
 ||p_(X^T A X)||_(infinity,ess)
 <= 2^(11/4) binom(6,2)^(1/8)
    /sqrt(0.56*1.9793840196887886...)
 =8.963649207866878... <8.964.`                                  (5.27)

This is a genuine equation-level application of the designated partner result after the new Schur-reserve inequality (5.13).

### 5.4 Exact target-class check

Equation (5.20) also gives

`s_3(P_H A)>=1.99`.                                               (5.28)

Since left multiplication by the coordinate projection cannot increase singular values,

`s_3(P_H A)<=s_3(A)`.                                             (5.29)

Thus

`boxed: s_3(A)>=1.99>1`.                                         (5.30)

Because `A` is symmetric, this means the actual final matrix has at least three eigenvalues of absolute value at least `1.99`. Every member of the family lies literally inside the owner's target class.

## 6. Why this does not solve unrestricted QFORM

Theorem 2.1 is an exact stability compiler, not the missing global structural theorem. From only

`s_3(A)>=1`,                                                      (6.1)

we do not yet know how to force an original-coordinate pivot `I` and banks `K,J` for which

1. the pivot survives (`C_1` invertible and quantitatively usable), and
2. the large spectral packet has low Schur residual rank `rho`, and
3. the baseline Schur cross block has `rho` spare singular directions,

or else force one of the already completed diffuse-bank / D5 / ridge / hub / physical-pair / half-Riesz / Schur alternatives.

There is also a genuine resonance warning: if the large packet makes the chosen physical pivot singular, the Schur identity must be re-pivoted; one cannot divide through that singularity. Likewise the small-tail estimate (3.6) can be large when the post-large-packet pivot is poorly conditioned or its pivot-to-complement block is huge. These are deterministic structural debts, not probabilistic independence issues.

The full conjecture therefore remains **OPEN**. The present branch proves essential boundedness only; no unrestricted continuity conclusion is claimed.

## 7. Correction discipline

This proof does not use any of the invalidated mechanisms in the live correction inbox:

- no pointwise van-der-Corput decay from a density cap;
- no arbitrary-joint coarea theorem;
- no conditional-cap-implies-independence step;
- no fiber-supremum bound growing secretly with dimension;
- no rotated-coordinate independence;
- no assertion that small `||T||op` makes `X^T T X` a small random variable;
- no Monte Carlo evidence as proof.

All perturbation estimates are deterministic identities or singular-value inequalities on the actual coefficient matrix in original coordinates.

## 8. Status and next step

**New proved result:** `QFORM-SCHUR-SPECTRAL-PACKET-RESERVE-v1`, equations (2.8)-(2.14), plus the high/low spectral extension (3.9).

**Partner result actually applied:** `QFORM-RANKONE-SELF-CARRIER-RETENTION-v1`, `yspennstate/math-open-problems@894dfe1e6cc4817c2b3e0bbe46036e4839f10dbf`, exact path stated above.

**Concrete output:** a target-class family with arbitrarily many unbounded positive/negative complementary eigenvalues, an unbounded rank-two physical cross packet, and an arbitrary full-rank signed small spectral tail of norm `<=0.01`, for which

`||p_Q||_(infinity,ess)<8.964` and `s_3(A)>=1.99`.

**First unpaid implication:** prove a pivot-selection / Schur-residual-rank dichotomy from the bare three-large-eigenvalue hypothesis, with failure routed into a completed non-Schur branch. A promising formulation is: either some physical pivot produces a Schur cross block with enough reserve beyond the graph-residual dimension, or the collection of graph residuals has enough transverse volume to trigger an existing projected-crossing or diffuse-bank receiver.

Execution status: `WITHOUT_VERIFIED_BRAIN`.
