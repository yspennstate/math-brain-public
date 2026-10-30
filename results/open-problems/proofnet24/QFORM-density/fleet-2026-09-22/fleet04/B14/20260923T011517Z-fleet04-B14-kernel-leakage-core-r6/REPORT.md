# QFORM B14 r6 — absorbing singular-core kernel leakage into a bounded physical enlargement

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B14, 2026-09-23T01:15:17Z.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T011517Z-fleet04-B14-kernel-leakage-core-r6`  
Status: `SUPPORTING TARGET-LEVEL THEOREM PROVED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and current source boundary

The owner target remains a dimension-free constant `C` such that

`P{X^T A X in J} <= C |J|`

for every interval `J`, all independent real original coordinates with probability densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one. No support, moment, identical-law, centering, Gaussian, or post-rotation-independence hypothesis is added.

Fresh owner control is revision `2026-09-22.15`; the active request blob is `165c570ecb4dcc6299c38fc3298771e4a8339dac`, the B14 assignment blob is `46b1d3db2ffb7759153a7209cd4cc34071e8c362`, the correction inbox blob is `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`, and the memory protocol blob is `0d902d56688f4b5c575f5b921ddf9f6709e88312`.

The newest required mathematical input is the volume-stability package at `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`. The still-active Claude source directory is read at the newer directory state `370534c8763da810a1b81945e0e44344feab0b75`; its current blobs are `RESULTS.md` `62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`, `FOURIER_ROUTE_REPORT.md` `9da148eed6cd43b1046a6f91d0f9329e12921cb4`, `GEOMETRIC_ROUTE_REPORT.md` `69d25fd6d4598bce258dee2f600090bf184df7ad`, and `COUNTEREXAMPLE_SEARCH.md` `ee721b237e206f31298b1871979faaab37a1bac2`. The Claude review at commit `9844891a9fbe96a65e37f71122bf0300b53dcc80` remains binding.

The completed designated partner actually used below is fleet01/B14 r23, report blob `7908503d72472b58359c14e5011bcd65c0ba6a05`. In particular, its zero-loss smooth-product/rough-product transfer is applied at equation (3.3), and its outside-lifted top-two-cross theorem is applied at equation (5.2).

## 2. Why the previous translation argument stops at a singular core

For an original-coordinate core `U` with quadratic matrix `B`, conditioning on all outside original coordinates `V=v` gives

`Q_v(U)=U^T B U + ell(v)^T U + r(v)`.

Writing `ell=ell_R+ell_K` according to `Range(B) direct-sum Ker(B)`, completion of the square gives

`Q_v(U)
 =(U+(1/2)B^dagger ell_R)^T B(U+(1/2)B^dagger ell_R)
   +ell_K^T U+r-(1/4)ell_R^T B^dagger ell_R`.                 (2.1)

Only `ell_R` is removable. The term `ell_K^T U` is genuine kernel leakage. Rotating `U` to make the kernel a coordinate would destroy product independence, so (2.1) cannot be finished by a spectral-coordinate argument.

The remedy below is different: retain original coordinates and enlarge the physical core by one actual leaking coordinate. The fixed-dimensional theorem is affine-uniform, so all still-outside coordinates can then be conditioned away at no cost.

## 3. Bounded physical-core localization compiler

Let `H` be a set of `m>=3` original coordinates and put `B_H=A[H,H]`. Suppose `B_H` has at least three eigenvalues of modulus at least `sigma>0`. The fixed-dimensional geometric theorem gives, for every affine vector `l`, scalar `c`, and every smooth cap-one product law on `R^m`,

`P{U^T B_H U+l^T U+c in J}
 <= [250 m(8+log m)/sigma] |J|`.                            (3.1)

For `m=3` and `sigma_min(B_H)>=sigma`, the sharper projected-gradient theorem gives

`P{U^T B_H U+l^T U+c in J}
 <= [6 sqrt(pi)/sigma] |J|`.                                (3.2)

Apply fleet01/B14's completed smooth-product transfer: mollification preserves the cap one, product total variation is bounded by the sum of marginal `L^1` errors, and pushforward contracts total variation. Therefore (3.1)-(3.2) hold for arbitrary cap-one product laws, including unbounded or arbitrarily fragmented supports. This is the promised actual application of the partner at an interval inequality; no bathtub optimizer or threshold set on the infinite line is asserted.

Now condition on all original coordinates outside `H`. The cross couplings create only an arbitrary affine vector `l(v)` and scalar `c(v)` while `B_H` stays fixed. Equations (3.1)-(3.2) are uniform in these parameters, hence averaging gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= 250 m(8+log m)/sigma,`                                  (3.3)

and, for a protected triple,

`boxed:
 ||p_(X^T A X)||_infinity <= 6 sqrt(pi)/sigma.`              (3.4)

All additional spectrum, outside couplings, translations, tails and fragments are arbitrary. This compiler is useful precisely because the physical core theorem already includes every affine term, including any affine component lying in a kernel of a smaller subcore.

## 4. One-coordinate absorption of rank-two kernel leakage

Let `S` consist of three original coordinates and suppose the symmetric block `B=A[S,S]` has rank two. Let its two nonzero singular values be `nu_1>=nu_2>0`, and let `k` be a unit vector spanning `Ker(B)`. Choose one further original coordinate `j`, put

`c=A[S,j]`, `d=A[j,j]`, and

`H=A[S union {j},S union {j}]
   =[[B,c],[c^T,d]].`                                       (4.1)

Set `a=k^T c`. This is the exact coupling of the added physical coordinate into the old kernel. Let `s_1(H)>=s_2(H)>=s_3(H)>=s_4(H)` denote the singular values of `H`.

### Lemma 4.1 — exact determinant and third-singular-value gate

If `a!=0`, then

`|det H|=nu_1 nu_2 a^2`,                                   (4.2)

and

`s_3(H)
 >= |a| sqrt(nu_1 nu_2)/sqrt(s_1(H)s_2(H)).`                (4.3)

#### Proof

Use an orthogonal basis of the deterministic coefficient space whose first two vectors span `Range(B)` and whose third vector is `k`. This is only matrix algebra; no random variable is rotated. In that basis,

`B=diag(lambda_1,lambda_2,0)`,
`c=(b_1,b_2,a)`.

Taking the Schur complement of the invertible two-dimensional range block gives

`det H=lambda_1 lambda_2 det([[0,a],[a,d-b^T diag(lambda_1,lambda_2)^(-1)b]])
      =-lambda_1 lambda_2 a^2`.

Taking absolute values proves (4.2). Moreover

`|det H|=s_1(H)s_2(H)s_3(H)s_4(H)
        <=s_1(H)s_2(H)s_3(H)^2`,

because `s_4(H)<=s_3(H)`. Rearranging and using (4.2) proves (4.3). QED.

### Theorem 4.2 — kernel-leakage physical-enlargement inequality

Under the hypotheses above, for arbitrary independent cap-one input laws in every ambient dimension,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 1000(8+log 4)
    sqrt(s_1(H)s_2(H))
    /[|k^T c| sqrt(nu_1 nu_2)].`                            (4.4)

#### Proof

The four-coordinate block `H` has at least three eigenvalues of modulus at least the right side of (4.3). Apply (3.3) with `m=4` and

`sigma=|k^T c| sqrt(nu_1 nu_2)/sqrt(s_1(H)s_2(H))`.

Conditioning on every coordinate outside this actual four-coordinate core retains arbitrary affine terms, to which (3.3) is uniform. QED.

Equation (4.4) is a full-target density inequality on its stated structural branch. It neither removes nor hides kernel leakage: the price is the reciprocal of the actual kernel coupling `|k^T c|`. It also exposes the next structural issue exactly. The bare global hypothesis `s_3(A)>=1` does not force the dimensionless ratio

`|k^T c| sqrt(nu_1 nu_2)/sqrt(s_1(H)s_2(H))`

to be uniformly positive for any one coordinate `j`.

## 5. Other paid localization branches and an actual fleet01/B14 inequality

The same conditioning compiler preserves the latest ruled and cross estimates.

1. If a three-coordinate physical block is invertible of signature `(2,1)` with every eigenvalue magnitude at least `sigma`, then with its moving critical value `tau(V)`,

   `P{Q in J, Q>=tau(V)} <= (pi sqrt(2)/sigma)|J|`.          (5.1)

   For signature `(1,2)` the reflected gate is paid. This remains only the one-sheet contribution.

2. If disjoint original-coordinate banks `I,J` satisfy `A[I,I]=0` and `C=A[I,J]` has `s_2(C)>0`, the completed fleet01/B14 outside-lifted theorem gives, after conditioning on every remaining original coordinate,

   `boxed:
    ||p_(X^TAX+b^TX+c)||_infinity
    <= e sqrt(pi)/sqrt(s_1(C)s_2(C)).`                      (5.2)

   All `J`-self terms, outside quadratic terms, outside couplings, translations and rough supports remain arbitrary.

3. If an original-coordinate cross block satisfies the current volume-stability gate `M=M_0+E`, `s_3(M_0)>=a`, maximum row leverage of `Range(M_0)` at most `1/2`, and `||E||op<=a/16`, then the new continuation gives

   `||p_Q||_infinity <23/a`,                                (5.3)

   again with arbitrary self blocks, affine terms and outside completion.

When several gates hold, the minimum of (3.3), (3.4), (4.4), (5.2), and (5.3) is valid. Equation (5.1) may improve the one-sheet part but is not inserted into a full-density minimum.

## 6. What changed and what remains

The substantive new point is Theorem 4.2. The previous B14 report correctly left `P_Ker(B)ell` as an obstruction. This run proves that a nonzero physical leakage coupling can be absorbed by one additional original coordinate, with an exact determinant identity and an explicit target-level density bound. No random-variable rotation, support truncation, moment estimate, interval extremizer, or small-quadratic-error argument is used.

This does not finish the conjecture. A diffuse or near-null matrix may have no uniformly good single leakage coordinate; the ratio in (4.4) can tend to zero even when the full matrix has three large eigenvalues. The next obligation is therefore collective: aggregate many small kernel couplings into a product-preserving cross/volume certificate, or combine the new two-direction-plus-tail theorem with the bounded physical enlargement. The convex/two-sheet contribution also remains unpaid outside the protected/full-core branches.

Continuity remains separate. Equations (3.3), (4.4), and (5.2) establish essential boundedness. The current volume estimate (5.3) additionally gives a continuous `C_0` version; no general continuity conclusion is inferred here.

## 7. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved supporting theorem: one-coordinate absorption of rank-two physical-core kernel leakage, (4.4).
- Completed partner actually used: fleet01/B14 r23, blob `7908503d72472b58359c14e5011bcd65c0ba6a05`, at (3.3) and (5.2).
- New continuation actually used: volume stability at `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, at (5.3).
- Repository transport is not native brain ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
