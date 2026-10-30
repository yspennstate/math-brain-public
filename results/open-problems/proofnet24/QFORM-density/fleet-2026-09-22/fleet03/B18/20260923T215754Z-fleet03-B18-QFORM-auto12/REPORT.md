SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T21:57:54Z.
attacking: the punctured private-bank overlap by whitening a fresh-coordinate dependent pair and feeding its exact LPP density cap into the fleet04/B18 zero-pivot receiver.

# fleet03/B18 auto12 — fresh-coordinate wedge cancellation in the zero-pivot receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer  
Run: `20260923T215754Z-fleet03-B18-QFORM-auto12`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING TARGET-LEVEL THEOREM / PARTNER APPLIED / FULL QFORM OPEN`  
Regularity: continuous density on the theorem below; full-target continuity remains OPEN.

## 1. Exact scope

The owner target remains the unrestricted statement for arbitrary independent real original-coordinate inputs with probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, support, iid, symmetry, centering, Gaussian, log-concavity, smoothness, or diagonal-basis assumption is added here.

This run consumes the live corrections: no independence after a general rotation, no arbitrary-joint indefinite coarea theorem, no conditional-density-cap substitute for independence, no law-uniform pointwise quadratic-phase decay, no deletion of a small nonzero coefficient, and no assertion that a uniformly good physical minor is forced by the spectral hypothesis.

## 2. Primary source transfer: LPP for a nonorthogonal two-dimensional map

Primary source: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949.

Their theorem says that if `X` has product density `prod_j f_j` with every `||f_j||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`.

A deterministic whitening gives the exact full-row-rank form needed below. If `C` is a real `k x m` matrix of row rank `k`, then

`R=(C C^T)^(-1/2) C`

has orthonormal rows. Hence `R X` has density cap `2^(k/2)`, while

`C X=(C C^T)^(1/2) R X`.

Therefore

`boxed: ||p_(C X)||_infinity <= 2^(k/2) / sqrt(det(C C^T)).`       (2.1)

This is only a linear-projection statement. It does not declare the coordinates of `CX` independent.

Now let `X_i` be one fresh original coordinate and let `X_K` be a disjoint original-coordinate product bank. For deterministic `ell,beta in R^K`, with `beta!=0`, put

`W=X_i+ell dot X_K`,
`B=beta dot X_K`,
`rho=||beta||_2`,
`eta=||P_(beta^perp) ell||_2`.

The two coefficient rows on `{i} union K` are

`w=(1,ell)`, `b=(0,beta)`.

Their Gram matrix is

`G_2=[[1+||ell||^2, ell dot beta],[ell dot beta,rho^2]]`,

and its determinant is exactly

`det G_2
 =rho^2(1+||ell||^2)-(ell dot beta)^2
 =rho^2(1+eta^2).`                                             (2.2)

Applying (2.1) with `k=2` gives the joint density bound

`boxed: ||p_(W,B)||_infinity
 <= 2/[rho sqrt(1+eta^2)].`                                   (2.3)

The key point is the `+1`: even when `ell` is exactly or nearly parallel to `beta`, the fresh physical coordinate in `W` keeps the two-dimensional source map quantitatively nonsingular. This is a product-provenance fact, not an arbitrary-joint assumption.

## 3. Designated fleet04/B18 theorem applied at an actual inequality

The completed fleet04/B18 zero-pivot theorem is the result used in its r2 report, source path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

It states: if a cap-one scalar `U` is independent of a two-dimensional vector `Y` with arbitrary joint density cap `M`, and `H` is a nonsingular real symmetric `3x3` matrix with `H_11=0`, then

`||p_((U,Y)^T H (U,Y))||_infinity
 <= 6 M^(2/3)|det H|^(-1/3),`                                 (3.1)

and the output density is continuous.

The scalar-cap scaling of (3.1) is immediate. If instead `||p_U||_infinity<=N`, set `U'=N U`. Then `U'` is cap one and the transformed matrix has determinant `N^(-2) det H`. Thus

`boxed: ||p||_infinity
 <= 6 (N M)^(2/3)|det H|^(-1/3).`                             (3.2)

This scaling uses the completed partner theorem at an actual inequality; it does not alter its independence hypothesis.

## 4. New theorem: the fresh-wedge zero-pivot branch

### Theorem `QFORM-FRESH-WEDGE-ZEROPIVOT-v1`

Let the original coordinates split into pairwise disjoint sets

`J`, `{i}`, `K`.

Let `a in R^J` and `beta in R^K` be nonzero, and let `ell in R^K` be arbitrary. Define

`S=a dot X_J`,
`W=X_i+ell dot X_K`,
`B=beta dot X_K`.

Let `H` be any nonsingular real symmetric `3x3` matrix whose `S-S` entry is zero. Then

`Q=(S,W,B)^T H (S,W,B)`

has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= 12 [ ||a||_2^2 ||beta||_2^2
          (1+||P_(beta^perp)ell||_2^2)
          |det H| ]^(-1/3).`                                  (4.1)

If `S` is itself one original physical coordinate rather than a general normalized bank, the constant `12` improves to

`6*2^(2/3)=9.524406311809196...`.                              (4.2)

#### Proof

The bank `S` is genuinely independent of the whole pair `(W,B)` because their underlying original-coordinate sets are disjoint.

By the one-dimensional LPP theorem,

`N:=||p_S||_infinity <= sqrt(2)/||a||_2.`                       (4.3)

Equation (2.3) gives

`M:=||p_(W,B)||_infinity
 <=2/[||beta||_2 sqrt(1+eta^2)],`

where `eta=||P_(beta^perp)ell||_2`.                             (4.4)

Insert (4.3)--(4.4) into the partner inequality (3.2):

`6(NM)^(2/3)|det H|^(-1/3)
 <=6[2sqrt(2)/(||a|| ||beta|| sqrt(1+eta^2))]^(2/3)
      |det H|^(-1/3)
 =12[||a||^2 ||beta||^2(1+eta^2)|det H|]^(-1/3).`

This proves (4.1), and continuity is inherited from the partner theorem. If `S` is an original physical coordinate, use its exact cap `N<=1` in place of the generic LPP bound (4.3), giving (4.2). QED.

## 5. Exact pseudodeterminant cancellation

Let `L` be the coefficient matrix whose three rows produce `(S,W,B)` from the original coordinates. The disjoint source supports give

`det(L L^T)
 =||a||_2^2 ||beta||_2^2(1+eta^2).`                            (5.1)

For

`A=L^T H L`,

`L` has full row rank and `H` is nonsingular, so `A` has exact rank three. The three nonzero eigenvalues of `A` are the eigenvalues of `H L L^T`; hence

`boxed: |pdet A|
 =|det H| det(L L^T)
 =||a||^2||beta||^2(1+eta^2)|det H|.`                         (5.2)

Consequently Theorem 4.1 has the invariant form

`boxed: ||p_(X^T A X)||_infinity <=12 |pdet A|^(-1/3).`        (5.3)

Therefore, throughout this exact-rank-three source geometry, if the three nonzero eigenvalues satisfy `|lambda_j(A)|>=s`, then

`boxed: ||p_(X^T A X)||_infinity <=12/s.`                     (5.4)

In particular the owner-normalized case `s>=1` is bounded by `12`, with a continuous density. The apparent reciprocal loss as `eta->0` is absent: the same Gram factor appearing in the LPP cap is exactly paid back by the physical pseudodeterminant.

This is the first essential implication of this run. It gives one uniform interpolation through the exact/near-parallel dependent-pair collar, but only when the compiler exposes the stated fresh-coordinate wedge and an independent scalar bank.

## 6. Target-valid overlapping-source stress family

Take four independent cap-one inputs and define, for arbitrary `t in R`,

`S=X_1`,
`W=X_0+t X_2+X_3`,
`B=X_2`.

The pair `(W,B)` shares the original coordinate `X_2` whenever `t!=0`; no independence between them is used. Its coefficient Gram is

`G_pair(t)=[[t^2+2,t],[t,1]],`

with

`det G_pair(t)=2`                                               (6.1)

for every `t`. Let

`G_t=diag(1,G_pair(t))`,
`D_0=[[0,1,0],[1,0,0],[0,0,1]],`
`H_t=G_t^(-1/2) D_0 G_t^(-1/2).`                               (6.2)

Because `G_t` is block diagonal at the scalar `S`, `H_t` still has zero `S-S` pivot. Let `L_t` be the coefficient map `(X_1,X_0,X_2,X_3)->(S,W,B)` and put

`A_t=L_t^T H_t L_t.`                                           (6.3)

The nonzero spectrum of `A_t` is exactly the spectrum of

`G_t^(1/2) H_t G_t^(1/2)=D_0`,

namely

`{1,-1,1}`.                                                     (6.4)

Thus every `A_t` is an exact target matrix. Since `S=X_1` is a physical coordinate, (4.2) and `|pdet A_t|=1` give, for every `t` and every admissible product input law,

`boxed: ||p_(X^T A_t X)||_infinity
 <=6*2^(2/3)
 =9.524406311809196... .`                                      (6.5)

The density is continuous. This family remains uniformly paid even as the overlap coefficient `t` becomes arbitrarily large; the determinant identity (6.1) is exactly the source-space reason.

## 7. Null-hub corollary and relation to prior B18 work

A useful direct corollary is the exact-rank-three form

`Q=2 (g dot X_J)(X_i+ell dot X_K)
   + d (beta dot X_K)^2`,                                      (7.1)

where `J,{i},K` are pairwise disjoint and `g,beta` are nonzero. This is Theorem 4.1 with

`S=g dot X_J`, `W=X_i+ell dot X_K`, `B=beta dot X_K`,
`H=[[0,1,0],[1,0,0],[0,0,d]].`

Hence

`||p_Q||_infinity
 <=12[|d| ||g||^2 ||beta||^2
       (1+||P_(beta^perp)ell||^2)]^(-1/3),`                    (7.2)

continuously.

The earlier B18 private-square theorem paid the exactly aligned `ell_K parallel beta_K` endpoint by a square smoother, and the later private-cross theorem paid a different transverse geometry by a rank-two cross determinant. Formula (7.2) is a uniform all-`ell` receiver for this stricter source-separated null-hub packet: the fresh coordinate is kept inside the two-dimensional LPP projection instead of being conditioned away. It therefore does not divide by the transverse component and does not delete it when small.

## 8. Literature boundary

The LPP theorem is used exactly within its published product-marginal hypotheses, followed only by deterministic whitening. The nonlinear step is not inferred from a projection-density cap alone; it is supplied by the completed fleet04/B18 zero-pivot theorem, whose required scalar-versus-vector independence is genuine here.

A targeted source check also revisited Juškevičius--Lee, arXiv:1503.09190, which gives sharp maximum-density/small-ball rearrangement for sums of independent bounded-density variables. It is useful for scalar banks but does not by itself replace the nonlinear zero-pivot receiver. No primary theorem located in this check matches the full unrestricted owner target. This is a scope statement, not a novelty claim.

## 9. What remains

The unrestricted QFORM conjecture is still OPEN / NOT PROVED, and unrestricted continuity remains OPEN. The theorem above requires a product-preserving compiler to expose an independent scalar bank and a two-dimensional dependent bank with one fresh original-coordinate component. The bare hypothesis `s_3(A)>=1` does not currently force that representation, and arbitrary additional spectrum remains unresolved.

The next structural implication is therefore to route the fully source-entangled states that admit no such fresh wedge into the already-paid ridge, grouped-cross, common-plane, hub, or pair-log receivers without forcing a vanishing local minor. In the null-hub language, arbitrary `J`-side shear/transverse curvature can still couple the scalar bank to the dependent pair and destroy the genuine independence needed by the zero-pivot theorem; the live conditional-cap counterexample shows why that dependence cannot be discarded.

No scheduler/task state, email/push setting, cross-account authentication, permission, public-release, remote-workflow, paid model/API/Codex, or installation change is made by this mathematical result.
