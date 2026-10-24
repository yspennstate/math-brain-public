SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T03:15:35Z.
attacking: five-square-mode bounded-carrier compiler using the already-proved marginal-free physical E3 receiver, then spend the saved carrier mode on a larger hostile signed-spectrum budget.

# account03/B12 — five-mode E3/core compiler and a six-direction hostile-spectrum budget

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T031535Z-qform-eigenvalue-r47`  
Status: **NEW SUPPORTING COMPILER + STRONGER PARTNER STABILITY APPLICATION / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The exact owner target remains open: independent real ORIGINAL coordinates `X_i` with scalar densities `0<=f_i<=1`, arbitrary real symmetric `A`, and only the hypothesis that at least three eigenvalues of `A` have absolute value at least one.

No Gaussianity, log-concavity, moments, compact or connected support, iid law, diagonal-basis assumption, post-rotation independence, small-random-error approximation, or pointwise quadratic van-der-Corput estimate is used below.

This run deliberately changed mechanism after the recent spectral-budget sequence. A source search showed that the **marginal-free physical third-volume theorem is already completed** and therefore is not re-claimed here. I use it as an input:

- account03/B20 r34, recorded through `yspennstate/math-open-problems@a23ddf469392d77526db53d0811248a52a84d088`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T164400Z-account03-B20-QFORM-r34/REPORT.md`; the later r35 restatement at `9330f48315819c3a654652a884496c0c24e9bcbd` records the theorem explicitly. For a literal physical cross block `M=A[I,J]`,
  `Z_3=e_3(MM^T)>0` implies a continuous `C_0` density with
  `||p_Q||_infinity <= K_3 Z_3^(-1/6)`,
  where
  `K_3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.
  Arbitrary same-bank curvature, affine terms, outside couplings, signs, and extra spectrum are retained.

The second analytic input is the finite physical-core projected-gradient theorem:

- `yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`. On an actual `m`-coordinate ORIGINAL block with three singular values at least `a`, after arbitrary affine terms, the density is at most `2 sqrt(6 pi m)/a`.

For continuity I use the separately completed fixed-matrix theorem:

- `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`: every fixed real symmetric coefficient matrix of rank at least three gives a bounded density in `C_0(R)` for every cap-one product input. This is qualitative/instance-dependent regularity and is not a universal-height theorem.

The designated partner theorem actually used at an equation is account04/B12 r7:

- `yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md`.

Its hybrid square-defect inequality is recalled in Section 4.

## 2. The first implication: five physical square modes split into a three-mode self core or third cross volume

Let `H` be an actual set of `m>=5` ORIGINAL coordinates. In the final matrix write

`A = [[C,B],[B^T,D]]`

in the physical cut `H | H^c`, where `C=A[H,H]` and `B=A[H,H^c]`. Direct block multiplication gives

`(A^2)[H,H]=C^2+BB^T`.                                           (2.1)

Assume

`lambda_5((A^2)[H,H]) >= g^2>0`.                                (2.2)

Set

`a=s_3(C)`, `b=s_3(B)`.

For positive semidefinite matrices, Weyl's upper inequality gives

`lambda_5(C^2+BB^T) <= lambda_3(C^2)+lambda_3(BB^T)=a^2+b^2`.

Hence the exact deterministic spill relation is

`boxed: a^2+b^2 >= g^2.`                                        (2.3)

This is a statement about the **final coefficient matrix**. It neither rotates the random vector nor treats any added quadratic remainder as independent.

The two terms in (2.3) are both fully payable on a bounded physical carrier:

- Self-core receiver. If `a>0`, condition on every ORIGINAL coordinate outside `H`. The remaining `m` coordinates stay independent, while outside couplings become only affine terms. The finite-core theorem gives

  `||p_Q||_infinity <= A_m/a`,
  `A_m=2 sqrt(6 pi m)`.                                         (2.4)

- Cross-volume receiver. If `b>0`, put `Z_3=e_3(BB^T)`. Since the singular values decrease,

  `Z_3 >= s_1(B)^2 s_2(B)^2 s_3(B)^2 >= b^6`.                   (2.5)

  The completed marginal-free E3 theorem therefore gives

  `||p_Q||_infinity <= K_3/b`,                                  (2.6)

  and this exit has a continuous `C_0` density.

The source theorem (2.6), including its removal of all third-volume row-marginal gates, is **not** new in this run. The new step is to combine it with the bounded physical self-core receiver and optimize the exhaustive profile (2.3).

## 3. Main theorem — a closed five-square-mode bounded-carrier compiler

### Theorem 3.1 — `QFORM-FIVE-SQUARE-MODE-E3-CORE-COMPILER-v1`

Under (2.2), every cap-one independent product input has a density satisfying

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24 pi m + K_3^2)/g,
 K_3=3*2^(4/3)*exp(1/3).`                                       (3.1)

Moreover the density has a representative in `C_0(R)`.

No restriction is imposed on any other eigenvalue of `A`: its sign, magnitude, multiplicity, or original-coordinate orientation may be arbitrary. No restriction is imposed on the outside dimension or on any same-bank/outside coupling.

### Proof

By (2.4)-(2.6), the law has either available cap `A_m/a` or available cap `K_3/b`, with `a^2+b^2>=g^2`.

Put

`M=sqrt(A_m^2+K_3^2)/g`.                                        (3.2)

If both `A_m/a>M` and `K_3/b>M`, then

`a<A_m/M`, `b<K_3/M`,

so

`a^2+b^2 < (A_m^2+K_3^2)/M^2=g^2`,

contradicting (2.3). Thus at least one receiver is at most `M`. Since `A_m^2=24 pi m`, (3.1) follows. The cases `a=0` or `b=0` are included automatically by using the other branch.

For regularity, (2.2) implies `rank(A)>=5`, because the compression `(A^2)[H,H]` has at least five positive eigenvalues. The completed fixed-matrix regularity theorem therefore gives a `C_0` representative. Its essential bound is (3.1); continuity then upgrades that essential bound to the same pointwise supremum bound. QED.

### Comparison with earlier B12 work

- r38 already observed the five-mode deterministic split and paid the cross alternative, but deliberately left the self-core branch unresolved when `|H|` was not bounded.
- r39 produced a seven-mode end-to-end compiler by a different ridge exit.
- Theorem 3.1 closes the **bounded** five-mode carrier end-to-end, with no volume-marginal hypothesis and a substantially smaller constant on the partner families below.

This is not a claim that the bare target hypothesis `s_3(A)>=1` always produces such a bounded five-mode carrier.

## 4. Partner composition: one more arbitrary hostile mode becomes free

Account04/B12 r7 considers

`A=B+D+L+T`, `B=A_0+C`,

where `C` commutes with `A_0`, `D` is arbitrary symmetric, `rank(L)<=r`, and `||T||op<=delta`. In a simultaneous eigenbasis for `A_0,B`, let

`d_j` be the decreasing rearrangement of the commuting square losses
`(lambda_j(A_0)^2-lambda_j(B)^2)_+`,

and let `nu_j` be the decreasing eigenvalues of the noncommuting destructive-square defect

`[B^2-(B+D)^2]_+`.

The partner theorem proves for any ORIGINAL-coordinate carrier `H` and integers `k,p,q>=0` with `k+r+p+q<=|H|` that

`sqrt(lambda_k((A^2)[H,H]))
 >= [ sqrt((lambda_(k+r+p+q)((A_0^2)[H,H])-d_(p+1)-nu_(q+1))_+) - delta ]_+.`  (4.1)

Taking `k=5` and feeding (4.1) into Theorem 3.1 gives a new density-level stability statement.

### Corollary 4.1 — `QFORM-HYBRID-FIVE-MODE-DENSITY-STABILITY-v1`

Define

`g_5=[ sqrt((lambda_(5+r+p+q)((A_0^2)[H,H])-d_(p+1)-nu_(q+1))_+) - delta ]_+.`  (4.2)

If `5+r+p+q<=m:=|H|` and `g_5>0`, then

`boxed:
 ||p_(X^TAX)||_infinity
 <= sqrt(24 pi m+K_3^2)/g_5,`                                    (4.3)

and the density belongs to `C_0(R)`.

Thus:

- arbitrarily large favorable commuting eigenvalue replacements are free;
- `p` arbitrarily severe commuting losses spend only `p` carrier modes;
- an arbitrary full-rank noncommuting packet spends only the tail `nu_(q+1)` of its actual destructive-square profile;
- a further arbitrary-magnitude rank-`r` signed packet spends only `r` modes;
- a dense coefficient tail spends only its deterministic operator norm `delta`;
- none of the corresponding quadratic random variables is treated as an independent convolution factor.

The gain over the partner's six-mode compiler is exactly one reserve direction: a fixed carrier of size `m` can now tolerate `m-5` hostile rank/profile directions rather than `m-6`.

## 5. Concrete account04/B12 application: destructive budget six instead of five

Use the partner's sixteen-dimensional Walsh-Hadamard baseline

`A_0=V diag(+/-2) V^T`, so `A_0^2=4 I_16`.                       (5.1)

Let `B=V diag(mu_1,...,mu_16)V^T` be an arbitrary commuting replacement with at most `p` indices satisfying `|mu_j|<2`; all other replacements may reverse sign and have arbitrarily large magnitude. Then

`d_(p+1)=0`.                                                      (5.2)

Let `D` be any real symmetric matrix, of arbitrary rank and operator norm, satisfying

`rank [B^2-(B+D)^2]_+ <=q`,                                      (5.3)

so `nu_(q+1)=0`. Let `L` be any symmetric matrix of rank at most `r`, with unrestricted eigenvalues, and let

`||T||op<=1/4`.                                                   (5.4)

Assume only the **total hostile mode budget**

`p+q+r<=6`.                                                       (5.5)

Choose any eleven ORIGINAL coordinates `H`. Since

`5+p+q+r<=11`,

(4.1) at `k=5` gives the actual final-matrix inequality

`boxed:
 sqrt(lambda_5((A^2)[H,H])) >=2-1/4=7/4.`                        (5.6)

This is the required equation-level use of the completed account04/B12 result.

Theorem 3.1 with `m=11`, `g=7/4` now gives

`boxed:
 ||p_Q||_infinity
 <= (4/7) sqrt(264 pi + K_3^2)
 =17.526064768154967... <17.527.`                                 (5.7)

The density is continuous and vanishes at infinity.

The family genuinely remains inside the owner target. Apply the same partner inequality on the full sixteen-coordinate space with `k=3`. From `3+p+q+r<=9<=16`, (5.1)-(5.5) give

`boxed: s_3(A)>=7/4>1.`                                          (5.8)

A particularly transparent new member takes

`p=q=r=2`.

Then:

- fourteen commuting replacements may have arbitrary sign and magnitude subject only to `|mu_j|>=2`;
- two commuting eigenmodes may be arbitrarily severely reduced or cancelled;
- `D` may be full rank and arbitrarily large, constrained only by a rank-two destructive-square defect;
- `L` is now an arbitrary-magnitude **rank-two** signed packet;
- the dense tail has norm at most `1/4`.

The partner's previous concrete density application had `p=2,q=2,r=1` and a six-mode receiver with bound `<1198`. The new compiler permits the extra hostile rank direction (`r=2`) and simultaneously improves the displayed cap to `<17.527` for this enlarged family. This comparison concerns proved bounds, not sharp constants.

## 6. Deterministic consistency checks

A seeded checker generated 10,000 random physical block pairs `(C,B)` with `m` between five and nine and verified

`s_3(C)^2+s_3(B)^2 >= lambda_5(C^2+BB^T)`                         (6.1)

with zero violations. The minimum numerical margin was

`0.17923912780958395`.

It also checked

`e_3(BB^T)>=s_3(B)^6`                                             (6.2)

with zero violations; the minimum observed ratio was

`1.4570532697315999`.

A separate 10,000-instance scalar check of the optimization step in (3.2) found zero violations and minimum numerical slack `0.008593114425447967`.

These are sanity checks only. The proofs are Weyl's inequality, the elementary-symmetric singular-value identity, and the two source-valid analytic receivers.

## 7. Exact remaining gap

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem closes every bounded physical carrier with five quantitative square-energy modes and improves the partner hostile-spectrum budget. It does **not** show that the bare hypothesis `s_3(A)>=1` forces such a carrier.

Combined with the immediately preceding r47 spectral-window reduction, the next B12 edge is sharper:

1. the diffuse spectral-window branch is already continuously bounded by `<64`;
2. otherwise there is a universal ORIGINAL-coordinate physical pivot or cross-row hub;
3. the present theorem says that if, after resolving that hub geometry, any bounded bank retains five square-energy modes, the branch is completely paid with a continuous quantitative bound;
4. what remains is to prove that the heavy-window branch either produces such a five-mode bank, or routes the remaining two spectral resources into an already-proved grouped-hub, projected-crossing, pair, ridge, or common-plane receiver.

A small coefficient remainder is never discarded as a small random quadratic error, and general eigen-coordinate rotations are never used to infer independence.
