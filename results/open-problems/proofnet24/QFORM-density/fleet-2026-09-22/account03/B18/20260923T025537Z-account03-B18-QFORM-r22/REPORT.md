SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T02:55:37Z.
attacking: the strict-N3 exact clique-factor survivor by a low-rank approximation argument, with a source-valid zero-pivot density transfer through account04/B18.

# account03/B18 r22 — exact cut-rank-one strict-N3 chamber cannot contain a target matrix

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `NEW TARGET-LEVEL STRUCTURAL CLOSURE / PARTNER RESULT APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Fresh owner-control revision:** `2026-09-22.15`  
**Prepublication control head observed:** `yspennstate/math-research-brain@57f4f3113a54fe762c63f00685350e15f927a128`

## 1. Exact target and correction boundary

The unrestricted target remains open: for every dimension, every independent real coordinate family with one-dimensional densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a valid counterexample. A continuous representative is a separate desired conclusion.

This run uses no Gaussianity, moments, compact support, connected support, log-concavity, or independence after a spectral rotation. It does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional projection-density moments, fixed-good-minor extraction, or the false principle that a conditional density cap supplies independence.

The new result is deterministic matrix geometry. It is specifically useful in the current strict no-pivot chamber, where one already has small physical diagonals and small `2x2` principal determinants.

## 2. Sources and exact hypothesis matching

### 2.1 Exact all-cut rank-one classification already proved in the fleet

Account01/B09 proved `QFORM-EXACT-CUTRANK1-CLASSIFICATION-v1`: if every disjoint physical cross block has rank at most one, then the off-diagonal support is exactly one of:

1. a star;
2. a triangle; or
3. a clique on a set `C`, with all outside vertices isolated and
   `A_ij = sigma u_i u_j` for all distinct `i,j in C`.

Canonical source used here:

`yspennstate/math-open-problems@77bd4ea475a11a505c6990630cbdfebdcce0fd8f`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T214429Z-r18/REPORT.md`.

I use only this exact classification, not any approximate gluing statement.

### 2.2 Low-rank approximation theorem

The matrix step below is the spectral-norm form of the Eckart--Young--Mirsky theorem:

` s_(k+1)(A) = inf_{rank R <= k} ||A-R||_op. `

The original low-rank approximation paper is C. Eckart and G. Young, *The Approximation of One Matrix by Another of Lower Rank*, Psychometrika 1 (1936), 211--218, DOI `10.1007/BF02288367`. Mirsky's extension to unitarily invariant norms, which includes the operator norm used here, is L. Mirsky, *Symmetric Gauge Functions and Unitarily Invariant Norms*, Q. J. Math. 11 (1960), 50--59, DOI `10.1093/qmath/11.1.50`.

No probabilistic premise is imported by this theorem.

### 2.3 Anti-concentration sources checked for the partner splice

I rechecked the primary statements used by the designated account04/B18 result:

- T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. It treats sums of independent bounded-density variables; no moment, support, symmetry, or log-concavity hypothesis is imposed.
- G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949. For a product density with each one-dimensional factor bounded by one, every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`.

These results concern genuine product inputs. They do not license post-rotation independence.

## 3. New theorem: clique-factor exclusion by a rank-two approximation

Put

`q(tau)=sqrt(tau+tau^2)`.

### Theorem 3.1 — `QFORM-STRICTN3-CLIQUE-FACTOR-IMPOSSIBLE-v1`

Let `A` be a real symmetric matrix. Assume there is a clique set `C` and numbers `sigma !=0`, `u_i !=0` for `i in C` such that

`A_ij = sigma u_i u_j` for all distinct `i,j in C`,

and every off-diagonal entry involving a vertex outside `C` is zero. Assume also

`|A_ii| < tau` for every `i`,                                             (3.1)

and

`|det A[{i,j},{i,j}]| < tau` for every `i != j`.                         (3.2)

Then

`boxed: s_3(A) < tau + sqrt(tau+tau^2).`                                 (3.3)

Consequently, if `tau<1/3`, no such clique-factor matrix can satisfy `s_3(A)>=1`.

#### Proof

For distinct `i,j in C`,

`det A[{i,j},{i,j}] = A_ii A_jj - A_ij^2`.

Using (3.1)--(3.2),

`|A_ij|^2 <= |A_ii A_jj| + |det A[{i,j},{i,j}]| < tau^2+tau`.

Thus

`|sigma| |u_i u_j| < q := sqrt(tau+tau^2)` for all distinct `i,j in C`.  (3.4)

Define

`r_i=|sigma| u_i^2 >=0`.

Then (3.4) is

`sqrt(r_i r_j)<q` for all `i != j`.                                      (3.5)

Hence **at most one** index `h` can satisfy `r_h>=q`: two such indices would give `sqrt(r_h r_j)>=q`, contradicting (3.5).

Extend `u` by zero outside `C` and write exactly

`A = sigma u u^T + D`,                                                    (3.6)

where `D` is diagonal and

`D_ii=A_ii-sigma u_i^2` on `C`,
`D_ii=A_ii` outside `C`.                                                   (3.7)

If an exceptional `h` with `r_h>=q` exists, set

`R = sigma u u^T + D_hh e_h e_h^T`;                                     (3.8)

otherwise set `R=sigma u u^T`. In either case `rank R<=2`.

For every `i != h` in `C`, (3.1) and `r_i<q` give

`|D_ii| <= |A_ii| + |sigma|u_i^2 < tau+q`.                              (3.9)

For vertices outside `C`, `|D_ii|<tau`; and the exceptional coordinate has been absorbed into `R`. Therefore

`||A-R||_op < tau+q`.                                                     (3.10)

The operator-norm Eckart--Young--Mirsky theorem now gives

`s_3(A) <= ||A-R||_op < tau+q`,

which is (3.3).

Finally, for `tau<1/3`,

`tau+sqrt(tau+tau^2)<1`

because, with `1-tau>0`, this is equivalent after squaring to

`tau+tau^2 < (1-tau)^2`, i.e. `3tau<1`. QED.

### Current strict-N3 threshold

At `tau=1/128`,

`q=sqrt(129)/128 = 0.088732942903129...`,

and

`tau+q=(1+sqrt(129))/128 = 0.096545442903129... <1`.                     (3.11)

So the exact clique-factor survivor listed in account03/B09 r22 is not merely payable: it **cannot occur** under the current strict-N3 spectral target.

The point of (3.8) is the cancellation that the previous star perturbation argument could not use safely. `D_hh` may be arbitrarily large. We do not call `D` a small perturbation. Instead, the pair-minor inequalities show that all but at most one of its potentially large cancellation entries are small; the single exceptional entry is absorbed into the rank-two approximant together with the global rank-one clique term.

## 4. Full exact cut-rank-one strict-N3 closure

The preceding theorem combines with the exact account01/B09 classification to eliminate the entire exact all-cut-rank-one chamber at the current threshold.

### Star branch

If the complete off-diagonal support is a star with center `h`, its off-diagonal matrix has the form

`e_h b^T + b e_h^T`

and hence rank at most two. The difference between `A` and this rank-two matrix is the physical diagonal, whose operator norm is `<tau`. Therefore

`s_3(A)<tau<1`.                                                         (4.1)

So a strict-N3 target cannot be an exact global star.

### Triangle branch

If the only nonzero off-diagonal entries lie on three vertices, the pair-minor estimate above gives every edge magnitude `<q`. The active `3x3` block has maximum absolute row sum `<tau+2q`; every outside coordinate is isolated with diagonal magnitude `<tau`. Hence

`||A||_op < tau+2q`.                                                     (4.2)

At `tau=1/128`,

`tau+2q = 0.185278385806258... <1`,                                    (4.3)

contradicting `s_3(A)>=1`.

More generally, `tau+2sqrt(tau+tau^2)<1` whenever

`tau < (2sqrt(3)-3)/3 = 0.154700538...`.

### Clique-factor branch

Theorem 3.1 gives `s_3(A)<tau+q<1` already for every `tau<1/3`.

We therefore obtain:

### Corollary 4.1 — `QFORM-STRICTN3-EXACT-CUTRANK1-IMPOSSIBLE-v1`

At the current strict threshold `tau=1/128`, if

`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau` for all `i!=j`,

and `s_3(A)>=1`, then it is impossible that every disjoint physical cross block has rank at most one.

Equivalently, **some disjoint physical cut has cross rank at least two.**

This is a structural conclusion only; it does not claim a dimension-free lower bound on that cut's second singular value. It therefore does not conflict with the live corrections showing that one uniformly good physical minor/cross cut need not exist.

## 5. Stress test for the cancellation mechanism

The theorem allows one clique coordinate to carry an arbitrarily large cancellation diagonal. For example, take

`sigma=100`,
`u=(1,0.0005,...,0.0005)` in dimension eight,

and choose all physical diagonals equal to zero. Then the largest pair determinant magnitude is `0.0025<1/128`, even though the hidden diagonal term `-sigma u_1^2` in (3.7) has magnitude `100`. The matrix's singular values begin

`0.132362587..., 0.132212587..., 0.000025,...`,

so `s_3=0.000025`, fully consistent with (3.11).

This example is only a finite check of the exact algebra; it is not used as evidence for the theorem.

## 6. Required account04/B18 partner application

The designated completed account04/B18 result is

`QFORM-SHARP-DISJOINT-TWOBANK-ZEROPIVOT-v1`,

canonical source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its analytic core is: if a cap-one scalar `X` is independent of a two-dimensional vector `Y` with joint density cap `M`, and

`K=[[0,ell^T],[ell,B]]`

is nonsingular symmetric, then `(X,Y)^T K(X,Y)` has a continuous density and

`||p||_infinity <= 6 M^(2/3)|det K|^(-1/3)`.                         (6.1)

Apply it to the genuine three-coordinate zero-diagonal clique core

`K_0=[[0,1,1],[1,0,1],[1,1,0]]`,                                    (6.2)

with three independent arbitrary cap-one scalar inputs. Take the first scalar as `X` and the other two as `Y`; their joint density cap is `M<=1` by genuine original-coordinate independence. Since

`det K_0=2`,

(6.1) gives the actual inequality

`boxed: ||p_(X^T K_0 X)||_infinity <= 6/2^(1/3)
      = 4.762203155904598... .`                                    (6.3)

The density is continuous. The matrix has eigenvalues `{2,-1,-1}`, so (6.3) is itself a target-normalized indefinite control example.

More generally, for the zero-diagonal triangle

`K=[[0,a,b],[a,0,c],[b,c,0]]`, `abc!=0`,

one gets

`boxed: ||p||_infinity <= 6 |2abc|^(-1/3).`                         (6.4)

For disjoint scalar banks instead of singleton coordinates, the Juškevičius--Lee sharp rearrangement caps used in the partner report may be inserted in (6.1) exactly as stated there. No claim is made that this zero-pivot theorem handles nonzero clique diagonals; the strict-N3 exclusion above is what removes that structural chamber at the current threshold.

## 7. What changed in the collective proof map

Before this run, account03/B09 r22 had paid the strict-N3 global-star geometry but explicitly left the exact clique-factor branch unresolved because the representation

`A = diag(A_ii-sigma u_i^2) + sigma u u^T`

can have a large diagonal cancellation term even though the *physical* diagonal `A_ii` is tiny.

Theorem 3.1 resolves exactly that issue without treating the cancelling diagonal as small. The pair-minor gate implies that at most one cancellation entry can be large; rank-one clique curvature plus that one entry is rank at most two; the remaining operator-norm error is `<tau+q`. Thus the target's third singular value rules the branch out.

Together with the star and triangle observations, the **exact** all-cut-rank-one strict-N3 chamber is now empty. The next structural obligation is the robust/approximate version already isolated elsewhere in the fleet: convert a near-rank-one all-cut state into a quantitatively payable rank-two product-preserving packet, or route it to an existing ridge/grouped/pair branch. This result supplies the exact endpoint that such a stability theorem should approach.

It does **not** prove that the rank-two cut forced by Corollary 4.1 has a uniform second singular value. It therefore does not resurrect the refuted fixed-good-minor or fixed-good-cross-cut mechanisms.

## 8. Continuity and full-target status

- The new strict-N3 clique/cut-rank-one result is a deterministic **exclusion theorem**; no output law exists in that chamber under the target spectral hypothesis, so there is no separate continuity assertion to prove there.
- The actual account04/B18 application (6.3)--(6.4) gives a continuous density in its zero-pivot scope.
- The unrestricted QFORM conjecture remains **OPEN / NOT PROVED**.
- Unrestricted continuity remains **OPEN**.

No claim of external novelty is made.

## 9. Source pins

- Current owner/control repository prepublication head: `yspennstate/math-research-brain@57f4f3113a54fe762c63f00685350e15f927a128`.
- Exact cut-rank-one classification: `yspennstate/math-open-problems@77bd4ea475a11a505c6990630cbdfebdcce0fd8f`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T214429Z-r18/REPORT.md`.
- Designated account04/B18 theorem: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.
- Eckart--Young original: DOI `10.1007/BF02288367`.
- Mirsky unitarily invariant norm extension: DOI `10.1093/qmath/11.1.50`.
- Juškevičius--Lee: `https://arxiv.org/abs/1503.09190`.
- Livshyts--Paouris--Pivovarov: `https://arxiv.org/abs/1507.07949`.

Repository synchronization is not native learned-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
