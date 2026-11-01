SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T11:00:22Z.
attacking: the punctured diffuse Schur-star endpoint by forcing the inherited second direction into a literal leaf spectral window, then paying its diffuse branch by half-Riesz and isolating the remaining self-similar physical obstruction.

# fleet03/B02 r51 — punctured-star leaf spectral halving compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING COMPILER / PUNCTURED SCHUR STAR REDUCED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new terminal half-Riesz exits prove essential boundedness. Continuity is claimed only on the separately cited fleet04/B02 overlap.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one; arbitrary real symmetric coefficient matrix; at least three eigenvalues of modulus at least one. No moments, compact support, connected support, log-concavity, iid assumption, Gaussianity, post-rotation independence, arbitrary conditional density cap, coefficient deletion, or pointwise law-uniform van der Corput bound is used.


## 1. Source boundary and the exact live frontier

Immediate own predecessor:

`yspennstate/math-open-problems@502f6502f0628f959a13e46b8bdce58a3d75be80`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T100402Z-fleet03-B02-qform-r50/REPORT.md`.

It starts from an ORIGINAL physical outer pivot `a=A_hh!=0`, writes

`A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`,

and uses the exact rank-one identity

`A-diag(0,S)=a^(-1)[a;b][a,b^T]`

to obtain

`boxed: s_2(S)>=s_3(A)>=1`.                                      (1.1)

On the live fixed-scale outer branch `|a|>1/228`, r50 pays the diffuse residual spectral window, every second non-small scalar pivot, localized residual stars, and the exact-zero residual hub. The true remaining residual geometry is therefore

`0<|c|:=|S_jj|<=1/228`,
`r:=||S[j,j^c]||_2>1/228`,
`max_(k!=j) S_jk^2 <= r^2/2`,
`s_2(S)>=1`.                                                     (1.2)

The current correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` is essential here: a small nonzero diagonal plus a row norm alone cannot be treated by continuity from the exact-zero theorem. The rank-one family

`[[eps,1],[1,eps^(-1)]]`

has row norm one but infinite half-Riesz potential for centered uniform inputs. This does not contradict (1.2), because that family has only one nonzero singular direction. The whole point of this run is to spend the *second* direction in (1.2) quantitatively.

Completed inputs actually used below are:

1. fleet01/B02 r48,
   `yspennstate/math-open-problems@4f9513fc5f561ab1db4ee87ecf55eea90644ecb2`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T093207Z-fleet01-B02-qform-auto11-r48/REPORT.md`.
   Its `QFORM-TWOEIG-1OVER19-DIFFUSE-HALFRIESZ-v1` says: if a symmetric coefficient `D` has `s_2(D)>=sigma>0` and
   `P=1_{|D|>=sigma/19}` satisfies `max_i P_ii<=1/72`, then for arbitrary affine terms in the ORIGINAL independent coordinates,

   `H_(1/2)(Z^T D Z+affine) <= C_2 sigma^(-1/2)`,
   `C_2=23.34314135471538...`.                                  (1.3)

2. fleet02/B01 r50,
   `yspennstate/math-open-problems@f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T091804Z-fleet02-B01-qform-auto11/REPORT.md`.
   Its two-level scalar compiler gives, when `s_2(D)>=rho` and `u=D_kk!=0`,

   `H_(1/2) <= 8|u|^(-1/2)
      +32 sqrt(5) 4^(-1/8) rho^(-1/8)|u|^(-3/8)`.              (1.4)

   The same report proves the exact-zero row endpoint

   `D_kk=0, q_k=||D[k,k^c]||_2>0
    => H_(1/2) <=2^(11/4) q_k^(-1/2)`                           (1.5)

   with arbitrary remaining curvature and affine terms.

3. fleet03/B11,
   `yspennstate/math-open-problems@0e0a0ab9b2a27d7a647567690e2c7f79c05341b0`,
   whose earlier binary theorem (source pinned there to commit `860d849b7f2e0198bf7c3531a71b14e59f03e430`) gives, for a literal indefinite physical pair with `Delta=e^2-uf>0`,

   `H_(1/2) <=16 Delta^(-1/4)`                                  (1.6)

   after conditioning every other ORIGINAL coordinate.

4. designated partner fleet04/B02,
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.
   On a nonsingular physical principal triple `H_0` with one exact zero diagonal it proves continuity and

   `integral_R |phi_Q(t)|^2 dt
      <=6*pi*2^(2/3)|det H_0|^(-1/3)`.                          (1.7)

No source above is promoted beyond its stated scope.

## 2. Compact conditional end-to-end argument

Write the residual coefficient in the current physical coordinate `j` as

`S=[[c,d^T],[d,D]]`,                                               (2.1)

where `D=S[j^c,j^c]` is a literal principal block on the remaining ORIGINAL variables and `r=||d||_2`.

The first missing implication is whether the second singular direction in `s_2(S)>=1` can be forced into `D` when the punctured star itself is not already very large. The answer is yes with an exact half-scale constant.

Define

`tau_* := sqrt(113/456)=0.497802187162591...`.                    (2.2)

If `r>tau_*`, this run labels the state a **strong punctured star** and does not claim it is paid. If `r<=tau_*`, the theorem below proves `s_2(D)>=1/2`. Then either the leaf spectral window is diffuse, in which case the full residual half-Riesz potential is uniformly paid, or one obtains a new ORIGINAL physical leaf hub at scale `1/456`. Existing scalar/zero/concentrated-hub receivers pay all but a scaled copy of the same diffuse punctured obstruction.

## 3. Main theorem — leaf spectral halving

### Theorem 3.1 — `QFORM-PUNCTURED-STAR-LEAF-HALVING-v1`

Let `S=S^T` be a real symmetric coefficient matrix on ORIGINAL independent cap-one coordinates and suppose

`s_2(S)>=rho>0`.                                                   (3.1)

Choose a physical coordinate `j`, write (2.1), and assume

`|c|<=rho/228`,
`r=||d||_2<=tau_* rho`,
`tau_*=sqrt(113/456)`.                                             (3.2)

Then:

**(A) Exact inherited leaf scale.** With singular values padded by zeros when needed,

`boxed: s_2(D)>=rho/2.`                                           (3.3)

**(B) Diffuse leaf spectral window is a half-Riesz exit.** Let

`P_D = 1_{|D|>=rho/38}`.                                          (3.4)

If

`max_k (P_D)_kk <=1/72`,                                         (3.5)

then for every arbitrary affine term and every real center,

`boxed:
 H_(1/2)(X^T S X+affine)
 <= C_2 sqrt(2/rho).`                                             (3.6)

In particular this estimate is uniform in the value of the physical coordinate `X_j`; no conditional density cap is used.

**(C) Failure of the diffuse leaf window creates a literal second hub.** If (3.5) fails, some ORIGINAL leaf coordinate `k` satisfies

`boxed:
 |D_kk|>rho/456
 OR
 ||D[k,k^c]||_2>rho/456.`                                        (3.7)

### Proof of (A)

Split

`S = B+E`,
`B=diag(0,D)`,
`E=[[c,d^T],[d,0]]`.                                              (3.8)

The star matrix `E` vanishes on the codimension-two subspace perpendicular to both `e_j` and `d`, while on their span its two eigenvalues are

`lambda_+- = (c +- sqrt(c^2+4r^2))/2`.

Therefore

`||E||_op = (|c|+sqrt(c^2+4r^2))/2`.                             (3.9)

The chosen constants are exact. At the corner of (3.2),

`(1/228)^2 + 4(113/456)
 = (227/228)^2`,                                                   (3.10)

so monotonicity of (3.9) gives

`||E||_op <= rho/2`.                                              (3.11)

Singular values are 1-Lipschitz under operator-norm perturbation. Hence

`s_2(B) >= s_2(S)-||E||_op >= rho/2`.                             (3.12)

Since adjoining one zero coordinate does not change the nonzero singular values, `s_2(B)=s_2(D)` with zero padding. This proves (3.3). Notice that when `D` is too small to possess two nonzero singular values, (3.3) simply says the branch (3.2) is impossible.

### Proof of (B)

Condition only on the ORIGINAL coordinate `X_j=x`. The remaining quadratic-plus-affine form is

`Z^T D Z + (ell+2x d)^T Z + constant(x)`.                        (3.13)

By (3.3), `D` has two singular directions at scale `sigma=rho/2`. The cutoff `sigma/19` is exactly `rho/38`. Under (3.5), fleet01/B02 r48 applies uniformly for **every** affine vector, hence uniformly in `x`:

`sup_t E_Z |Z^T D Z+(ell+2x d)^T Z-t|^(-1/2)
 <= C_2 (rho/2)^(-1/2).`                                         (3.14)

The additive scalar `constant(x)` merely shifts the center `t`. Average (3.14) over `X_j`. This gives (3.6). No rotation of the random variables occurs.

### Proof of (C)

If (3.5) fails, choose `k` with `(P_D)_kk>1/72`. Then

`||D e_k||_2^2=(D^2)_kk
 >=(rho/38)^2(P_D)_kk
 >rho^2/(38^2*72).`                                               (3.15)

But

`||D e_k||_2^2=D_kk^2+||D[k,k^c]||_2^2`.                         (3.16)

If both terms on the right had square roots at most `rho/456`, then

`||D e_k||_2
 <=sqrt(2) rho/456
 =rho/(38 sqrt(72)),`                                             (3.17)

contradicting (3.15). This proves (3.7). QED.

## 4. Application to the live r50 punctured star

Take `rho=1` in Theorem 3.1. The r50 survivor (1.2) now has the following exhaustive refinement.

### 4.1 Strong-star exit from this compiler

If

`r>tau_*=0.497802187162591...`,                                  (4.1)

the physical punctured star itself carries fixed order-one row energy. This branch is **not** claimed paid here; it is one of the two exact remaining mechanisms after r51.

### 4.2 Modest star + diffuse leaf window is paid

If `r<=tau_*` and the leaf window (3.4) is diffuse, (3.6) gives

`H_(1/2)(residual) <= C_2 sqrt(2)
 =33.01218709223076...`.                                         (4.2)

The already-present outer ORIGINAL square `|a|>1/228` has the standard conditional density kernel

`p_Q(t) <= |a|^(-1/2)
          E|residual-t|^(-1/2)`.                                 (4.3)

Therefore

`boxed:
 ||p_Q||_infinity
 <= C_2 sqrt(2)|a|^(-1/2)
 < C_2 sqrt(456)
 =498.473093785049.`                                             (4.4)

This is essential boundedness. The half-Riesz route alone does not prove continuity.

### 4.3 Modest star + nondiffuse leaf window creates a scale-1/456 hub

If the leaf window is nondiffuse, (3.7) gives a physical leaf coordinate `k` with

`|D_kk|>1/456`

or

`q_k:=||D[k,k^c]||_2>1/456`.                                    (4.5)

Because `s_2(D)>=1/2`, the first alternative is terminal by the fleet02/B01 two-level theorem. Substituting `rho=1/2`, `|D_kk|>=1/456` into (1.4) gives

`H_(1/2)(leaf form) <822.638791451`,                              (4.6)

uniformly in the affine term created by conditioning `X_j`. Thus the full outer law obeys

`boxed: ||p_Q||_infinity <12421.57335097.`                        (4.7)

For the row alternative in (4.5), if `D_kk=0`, (1.5) gives

`H_(1/2)(leaf form) <143.653069241`,
`boxed: ||p_Q||_infinity <2169.113777765.`                        (4.8)

If instead `0<|D_kk|<=1/456` and the row is concentrated, choose `l` with

`|e|:=|D_kl|>q_k/sqrt(2)>1/(456 sqrt(2))`.                        (4.9)

Put `f=D_ll`. If `|f|>=|e|/2`, then `|f|>1/(912 sqrt(2))`; applying (1.4) at residual scale `rho=1/2` gives

`H_(1/2)(leaf form)<1249.909601162`,
`||p_Q||_infinity<18873.221095653`.                               (4.10)

If `|f|<|e|/2`, then the literal physical pair `{k,l}` is quantitatively indefinite. Indeed

`Delta=e^2-D_kk f
 > (1-1/sqrt(2))e^2
 > (1-1/sqrt(2))/(2*456^2).`                                     (4.11)

By (1.6),

`H_(1/2)(leaf form)<552.309576720`,
`||p_Q||_infinity<8339.691722488`.                                (4.12)

Again these are essential-density bounds; no continuity is inferred from these fractional-potential payments.

## 5. The exact self-similar obstruction left by r51

After the terminal branches in Section 4, the only nondiffuse-leaf survivor is

`0<|D_kk|<=1/456`,
`q_k=||D[k,k^c]||_2>1/456`,
`max_(l!=k) D_kl^2 <=q_k^2/2`,
`s_2(D)>=1/2`.                                                     (5.1)

This is exactly the r50 punctured diffuse-star geometry rescaled from spectral scale `rho=1` to `rho=1/2`:

`1/456=(1/2)/228`.                                                (5.2)

Hence Theorem 3.1 can be iterated *as a compiler* without changing hypotheses. At a general inherited scale `rho_m=2^(-m)`, a nonterminal non-strong step produces a literal principal leaf block with

`s_2>=rho_(m+1)=rho_m/2`,                                        (5.3)

and either a half-Riesz terminal branch or a new physical hub at exactly

`rho_(m+1)/228`.                                                  (5.4)

If the new punctured row exceeds `tau_* rho_(m+1)`, it is a strong-star state at its inherited scale; otherwise the compiler repeats. In finite dimension this descent must eventually hit a terminal or a relative strong-star state, because a one-dimensional final leaf block cannot satisfy `s_2>=rho/2`.

This does **not** prove the owner theorem: after `m` descents the absolute inherited scale is `2^(-m)`, so naively spending the eventual strong star would reintroduce dimension-dependent loss. The genuine remaining B02 problem is therefore now sharply identified as follows:

`QFORM-SCALE-INVARIANT-STRONG-PUNCTURED-STAR-AGGREGATION-v1`:

> retain the entire preceding nested chain and pay a punctured diffuse physical row of norm `>tau_* rho` together with `s_2>=rho` by a scale-covariant grouped Fourier/half-Riesz receiver whose cost does not accumulate as `rho=2^(-m)` decreases.

A row-only continuity argument is forbidden by `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`; the inherited second direction or the stored chain must enter the estimate.

## 6. Required fleet04/B02 result applied at a new inequality

On the exact overlap where the designated partner's nonsingular zero-diagonal physical triple `H_0` is present, (1.7) and Plancherel give

`||p_Q||_2
 <=sqrt(3) 2^(1/3)|det H_0|^(-1/6)
 =2.18224727194344... |det H_0|^(-1/6).`                          (6.1)

The new leaf-diffuse branch (4.4), before inserting the outer threshold, is

`||p_Q||_infinity
 <=C_2 sqrt(2)|a|^(-1/2).`                                      (6.2)

Density-space interpolation therefore yields the genuinely new overlap estimate

`boxed:
 ||p_Q||_4
 <= [sqrt(3)2^(1/3) C_2 sqrt(2)]^(1/2)
    |a|^(-1/4)|det H_0|^(-1/12)
 =8.487682559033
    |a|^(-1/4)|det H_0|^(-1/12).`                               (6.3)

At the live outer scale `|a|>1/228`,

`boxed:
 ||p_Q||_4
 <32.9816850548 |det H_0|^(-1/12).`                             (6.4)

This is an equation-level use of fleet04/B02, not a citation-only dependency. The partner theorem separately supplies a continuous representative on this exact overlap. Equation (6.4) is not promoted to target-wide Fourier `L^1`.

## 7. Deterministic verification

The run checker tests the deterministic compiler only; it is not evidence for the probabilistic conjecture. It uses seed `2026092411`, dimensions 4 through 10, and 4,200 constructed random symmetric matrices satisfying the small-star collar and `s_2(S)>=1`.

Observed:

- spectral-halving violations: `0`;
- high-leverage-to-physical-hub violations: `0`;
- maximum sampled `||E||/(rho/2)`: `0.999228553714693`;
- minimum sampled Weyl margin `s_2(D)-[s_2(S)-||E||]`: `3.801497170992096e-04`;
- minimum sampled high-leverage hub margin above `rho/456`: `2.749023123532002e-01`.

The exact proof is Sections 3.1–3.3; the numerical regression is only a consistency check. Checker source and output are saved beside this report.

## 8. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. The target-wide universal unweighted

`integral |E exp(it X^T A X)| dt`

bound remains **OPEN / not refuted**. This run does not manufacture a counterexample to it.

The mathematical gain is a dimension-free, original-coordinate, exact-scale structural/analytic implication on the first r50 obstruction: every modest punctured Schur star necessarily transfers the second singular direction to its literal leaf block at half scale, after which a diffuse leaf spectral window is uniformly paid and every nondiffuse leaf state produces a fixed relative physical hub. The only recursive obstruction is a relative strong punctured star or a scaled copy of the same punctured diffuse geometry.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval/writeback is real, but authenticated native learned-memory receiver ingestion was not exposed or verified. No task identity, cadence, enabled/paused state, notification, email, public release, paid model/API call, installation, permission, or cross-account authentication was changed.
