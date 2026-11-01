SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T18:25:10Z.
attacking: a quantitative rough-law regularity obstruction: can the new full Gaussian-component-mixture theorem be closed to arbitrary cap-one marginals by weak/L1 approximation while preserving its inverse-scale hypothesis?

# fleet03/B15 auto25 — Gaussian-mixture approximation obstruction and rough-law separation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T182510Z-fleet03-B15-qform-auto25`  
Status: `PROVED ROUTE OBSTRUCTION / PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. This report proves an exact one-dimensional separation theorem showing that the newly proved full-matrix Gaussian-component-mixture branch cannot be extended to arbitrary rough cap-one inputs by weak, total-variation, or L1 approximation while preserving the branch's average-component-peak hypothesis. This is not a counterexample to QFORM; it removes one tempting regularity/closure shortcut.

## 1. Source theorem being tested

The completed interactive theorem

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_GAUSSIAN_MIXTURE_FULL_THEOREM.md`

proves the full arbitrary-rank/sign/affine QFORM estimate for independent coordinates of the form

    X_i = M_i + sqrt(T_i) G_i,

provided

    E T_i^(-1/2) <= sqrt(2*pi).                         (1.1)

For k=3 it yields `||p_Q||_infinity < 3` whenever `s_3(A)>=1`. For random component centers, (1.1) is stronger than merely requiring the final marginal density to be <=1. The open question addressed here is whether arbitrary cap-one laws could nevertheless be approximated by such mixture laws while retaining (1.1), allowing the theorem to pass to rough inputs by weak closure.

The answer is quantitatively no, already for `Uniform[0,1]`.

## 2. Exact separation theorem

Let `G~N(0,1)` be independent of a pair `(M,T)` with `0<T<infinity` almost surely, and put

    Y = M + sqrt(T) G.

Assume the exact Gaussian-mixture hypothesis

    E T^(-1/2) <= sqrt(2*pi).                            (2.1)

Let `mu=L(Y)` and let `U` denote `Uniform[0,1]`. Define

    alpha_* = 2 Phi(sqrt(pi/2)) - 1
            = 0.7899085945560627... .                   (2.2)

### Theorem 2.1 — `QFORM-GAUSSIAN-MIXTURE-CLASS-NOT-WEAK-DENSE-v1`

Every such `mu` satisfies

    boxed( mu([0,1]) <= alpha_* ).                       (2.3)

The constant is sharp. Consequently,

    boxed( d_TV(mu,U) >= 1-alpha_*
                         =0.2100914054439373... ),       (2.4)

and, writing `g` for the smooth density of `mu`,

    boxed( ||g-1_[0,1]||_1
             >= 2(1-alpha_*)
             =0.4201828108878747... ).                  (2.5)

In particular, **no sequence satisfying (2.1) can converge weakly to `Uniform[0,1]`**.

### Proof

Write `sigma=sqrt(T)` and `X=1/sigma=T^(-1/2)`. Conditional on `(M,T)=(m,sigma^2)`, `Y` is Gaussian `N(m,sigma^2)`. For a fixed `sigma`, among all centers `m` the probability of an interval of length one is maximized by centering the Gaussian at the interval midpoint. Thus

    P(m+sigma G in [0,1])
      <= 2 Phi(1/(2 sigma)) - 1.

For completeness, if

    F_sigma(m)=Phi((1-m)/sigma)-Phi(-m/sigma),

then symmetry gives `F_sigma(1-m)=F_sigma(m)`, and strict unimodality of the Gaussian density gives the unique maximum at `m=1/2`.

Define for `x>=0`

    a(x)=2 Phi(x/2)-1.

Then

    a'(x)=phi(x/2) > 0,
    a''(x)=-(x/4) phi(x/2) <=0,                          (2.6)

so `a` is increasing and concave. Averaging the component bound and applying Jensen gives

    mu([0,1])
      <= E a(X)
      <= a(E X)
      <= a(sqrt(2*pi))
      = 2 Phi(sqrt(pi/2))-1
      = alpha_*.

This proves (2.3).

Sharpness is attained by the single Gaussian

    M=1/2,    T=1/(2*pi).

It saturates (2.1), because `T^(-1/2)=sqrt(2*pi)`, and its `[0,1]` mass is exactly `alpha_*`.

Since `U([0,1])=1`, the defining event `[0,1]` gives

    d_TV(mu,U) >= |mu([0,1])-U([0,1])| >=1-alpha_*.

For absolutely continuous laws, `||g-u||_1=2 d_TV(g dx,u dx)`, proving (2.5). Finally, `[0,1]` is a continuity set for `U`; if `mu_n=>U` weakly, then `mu_n([0,1])->1`, contradicting the uniform bound (2.3). QED.

## 3. Product strengthening: the approximation gap gets worse with dimension

Let `mu_i` be arbitrary Gaussian component-mixture laws satisfying (2.1), independently across coordinates, and let

    nu_n = mu_1 tensor ... tensor mu_n,
    U_n  = Uniform([0,1]^n).

Then by independence and (2.3),

    nu_n([0,1]^n)
       = product_i mu_i([0,1])
       <= alpha_*^n.

Therefore

    boxed( d_TV(nu_n,U_n) >= 1-alpha_*^n ),              (3.1)

and the joint-density L1 distance is at least

    boxed( 2(1-alpha_*^n) ).                             (3.2)

Thus the direct coordinatewise approximation route is not merely non-dense: as dimension grows, the target cube law becomes asymptotically maximally separated in total variation from the product mixture class satisfying the hypothesis used by the `<3` theorem.

This strengthens the release warning that arbitrary rough densities cannot simply be inserted by Gaussian-mixture approximation. The obstruction persists even in weak topology, so the previous weak-limit/height-closure compilers cannot bridge this gap.

## 4. Scale-invariant cap version

The same constant is intrinsic to matching the density cap. For any `L>0`, let

    u_L(x)=L 1_[0,1/L](x)

be the height-`L` uniform density. Suppose

    E[(2*pi*T)^(-1/2)] <= L.                             (4.1)

After scaling `x -> Lx`, Theorem 2.1 gives

    d_TV(L(Y), Uniform[0,1]) >= 1-alpha_*.

Equivalently, a height-`L` interval law stays the same fixed positive distance from every Gaussian location-scale mixture whose **average component peak** is at most `L`. Therefore the phenomenon is not an artifact of the normalization `f<=1`.

## 5. Application of completed partner fleet04/B15 to an actual target inequality

Completed partner source:

`yspennstate/math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T151702Z-fleet04-B15-pivoted-convolution-r6/REPORT.md`.

It proves that for independent cap-one `X,Y,Z`,

    T=aX^2+2bXY+2uX+2vY+c,
    ||p_T||_3 <= 3 |b|^(-2/3),                          (5.1)

and for the disjoint square receiver

    S=gamma Z^2+2wZ,
    ||p_S||_(3/2) <= 2 |gamma|^(-1/3).                 (5.2)

Hence Young-Hoelder gives

    ||p_(T+S)||_infinity
      <= 6 |b|^(-2/3)|gamma|^(-1/3),                   (5.3)

with a `C_0` density.

Apply this to the explicit rough target instance

    X,Y,Z iid Uniform[0,1],
    Q = 2XY + Z^2,
    A = [[0,1,0],[1,0,0],[0,0,1]].                     (5.4)

The eigenvalues of `A` are exactly `1,-1,1`, so this is a genuine normalized three-large-eigenvalue target instance. Equations (5.1)-(5.3) give

    boxed( p_Q in C_0(R),   ||p_Q||_infinity <= 6 ).    (5.5)

At the same time, Theorem 2.1 says **each of its three marginals** is at total-variation distance at least `1-alpha_*` from every marginal in the Gaussian-component-mixture class satisfying (2.1), while (3.1) gives for the three-dimensional source law

    d_TV( U_[0,1]^3, nu_3 )
       >= 1-alpha_*^3
       = 0.507...                                      (5.6)

for every admissible product Gaussian-mixture source `nu_3` of the full-mixture theorem. Thus the partner's direct rough-law `L^p` mechanism genuinely reaches a target source that cannot be recovered as a weak or TV limit of the `<3` Gaussian-mixture branch under its preserved hypothesis.

This is an actual equation-level application of the designated partner result, not a citation-only use.

## 6. Consequence for the full programme

The new full Gaussian-mixture theorem is very strong on its exact input class, but **weak-limit closure cannot by itself remove its inverse-scale/average-component-peak hypothesis**. The cap-one rough class contains laws, beginning with the extremal interval density, that lie a fixed positive distance from that class even in weak topology.

Therefore a full proof for arbitrary cap-one inputs needs at least one genuinely rough-law ingredient: for example the partner's physical `L^p` conditioning, a product-preserving Fourier/volume estimate, or another mechanism that uses the final density cap directly rather than an average bound on hidden Gaussian component peaks.

This obstruction is compatible with all current source corrections. It does not assert that Gaussian mixtures are useless, does not refute their `<3` QFORM theorem, and does not produce a large-density QFORM counterexample. It precisely blocks the inference

    Gaussian-mixture theorem + approximation + weak closure
      => arbitrary cap-one theorem

when the approximants are required to retain the mixture theorem's inverse-half-scale hypothesis.

## 7. Regularity ledger

- **Absolute continuity:** unchanged; every nonconstant quadratic pushforward of an absolutely continuous joint law is absolutely continuous by the coarea argument away from the critical affine set.
- **Fixed-instance continuity:** the current checked manuscript reports a fixed-matrix `C_0` theorem under the target product hypotheses; this run does not redo that proof.
- **Universal height:** still OPEN for arbitrary cap-one product laws.
- **Gaussian component mixtures:** bounded continuous density with constant `<3` when `s_3(A)>=1`, under (2.1), complete and independently checked in the source release.
- **Approximation bridge from that class to arbitrary rough laws:** quantitatively impossible under the preserved hypothesis, by Theorem 2.1.

## 8. Exact remaining implication

The useful successor question is no longer whether one can smooth every cap-one marginal into the proven Gaussian-component-mixture class while keeping its average component peak bounded: Theorem 2.1 rules that out.

The remaining full-target problem is to prove a rough-law estimate that is stable under fragmented supports directly. From this B15 perspective, a productive interface is still a conditional `L^p * L^{p'}` or expected conditional-height certificate using original-coordinate independence, because those mechanisms apply to `Uniform[0,1]` and arbitrary fragmented cap-one marginals without hidden mixture moments.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or centered-input assumption is added to the owner target. No schedule/task/notification/email/permission/model/API setting is changed by this report.
