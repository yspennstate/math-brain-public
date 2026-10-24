SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T06:22:45Z.
attacking: literature-to-proof transfer for a product-preserving four-ray grouped-coordinate reduction, with the completed account02/B18 null-pivot theorem applied at the actual target inequality.

# account01/B18 r25 — four-ray grouped shear is uniformly paid by a source-valid null-pivot transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / DESIGNATED_PARTNER_APPLIED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed by the new full-line estimate; global continuity remains open.

## 1. Target and correction boundary

The owner target remains the unrestricted statement: for arbitrary independent real original-coordinate random variables with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite `L^infinity` bound for the density of `X^TAX`, or give a valid counterexample. No moment, support, iid, smoothness, log-concavity, or spectral-coordinate-independence hypothesis may be added.

This report does **not** use any of the live false interfaces: no arbitrary-joint 3D coarea estimate, no positive conditional projection-density moment, no independence after spectral rotation, no conditional-cap-as-independence substitution, no pointwise law-uniform Fresnel decay, no small-coefficient deletion, and no fixed-good-minor implication.

The branch proved below strictly enlarges the equal-weight Walsh--Hadamard stress family from the preceding account01/B18 run. It allows completely nonuniform coefficient magnitudes and arbitrary numbers of original coordinates in each source bank; only an exact four-ray Parseval structure is assumed.

## 2. Primary theorem matched at its exact hypotheses

The external input is:

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1; Israel J. Math. 216 (2016), 877--889.

If `f(x)=prod_j f_j(x_j)` is a product probability density with every `||f_j||_infinity<=1`, then every `k`-dimensional **orthogonal** marginal has density at most `2^(k/2)`. No moment, bounded-support, iid, log-concavity, or smoothness assumption is required. I use only the case `k=1`, after normalizing an actual coefficient vector to Euclidean norm one. No projected coordinates are declared independent unless they come from disjoint sets of original input coordinates.

The completed designated-partner analytic result applied below is account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, canonical source

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

It states: if a scalar `S` has density cap `K`, is genuinely independent of a possibly dependent pair `(C,D)` with joint density cap `M`, and

`T=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`,

with `beta,gamma!=0`, then

`||p_T||_infinity <= 3(2MK)^(2/3)|beta^2 gamma|^(-1/3).`      (2.1)

The latest account02/B18 report also proves for every exact-rank-three Schur-isotropic target form, after choosing the `(2+,1-)` sign, the one-sheet estimate

`p_Q(t)<=pi sqrt(2)` for a.e. `t>=0`.                            (2.2)

I retain (2.2) as the sharper majority-sign certificate, but the new argument below controls the entire real line.

## 3. Four-ray Parseval source class

Let `X_0,X_1,...,X_m` be arbitrary independent real variables with densities bounded by one. Let `V` be an `m x 3` matrix with

`V^T V=I_3`,                                                     (3.1)

and suppose every residual row has the form

`v_j = theta_j (1,a_j,b_j)`,

where `theta_j` is real and `(a_j,b_j) in {+1,-1}^2`.            (3.2)

For signs `a,b`, let

`G_ab={j:(a_j,b_j)=(a,b)}`,
`m_ab=sum_(j in G_ab) theta_j^2`.                                (3.3)

Taking the six entries of (3.1) gives

`sum_ab m_ab=1`,
`sum_ab a m_ab=0`,
`sum_ab b m_ab=0`,
`sum_ab ab m_ab=0`.                                              (3.4)

These are the four Walsh characters on `{+1,-1}^2`; inversion gives the exact bank-energy identity

`boxed: m_ab=1/4 for every (a,b).`                               (3.5)

Define the four disjoint-source aggregates

`Z_ab=sum_(j in G_ab) theta_j X_j`.                              (3.6)

The `Z_ab` are genuinely independent because their source sets `G_ab` are disjoint. By (3.5), the coefficient vector of `2Z_ab` has Euclidean norm one. Applying Livshyts--Paouris--Pivovarov at `k=1`,

`||p_(2Z_ab)||_infinity<=sqrt(2)`,

hence

`boxed: ||p_(Z_ab)||_infinity<=2sqrt(2).}`                       (3.7)

No equality of the coefficients inside a bank is assumed; (3.7) holds for arbitrary `theta_j` satisfying the Parseval identities.

## 4. Exact target family

Fix `r>=1`, put

`s=sqrt(1+r^2)`, `t=1/s`, `k=r/s=sqrt(1-t^2)`.                  (4.1)

Let

`u=r e_1`,
`D_r=[[0,1/s,0],[1/s,0,0],[0,0,1]]`,                            (4.2)

and, with `Y=V^T X_R`, define

`Q=(Y+uX_0)^T D_r (Y+uX_0)
  =2/s (Y_1+rX_0)Y_2 + Y_3^2.`                                  (4.3)

This is a genuine owner-target matrix. If `L=[u,V^T]`, then

`LL^T=diag(1+r^2,1,1)=diag(s^2,1,1)`.                           (4.4)

Therefore the nonzero eigenvalues of `A=L^T D_r L` equal those of

`diag(s,1,1) D_r diag(s,1,1)
 =[[0,1,0],[1,0,0],[0,0,1]],`                                   (4.5)

namely

`boxed: spectrum_nonzero(A)={-1,1,1}.}`                         (4.6)

Thus every member of the four-ray family lies exactly at the target spectral normalization.

## 5. Product-preserving conditioning and exact active matrix

The four aggregates satisfy

`Y_1=Z_+++Z_-+ + Z_+-+Z_--`,
`Y_2=Z_++-Z_-+ + Z_+--Z_--`,
`Y_3=Z_+++Z_-+ - Z_+--Z_--`.                                    (5.1)

Condition on the two original-coordinate banks `G_+-` and `G_--`, equivalently on the values of `Z_+-` and `Z_--`. The remaining variables

`X_0, P:=Z_++, N:=Z_-+`                                         (5.2)

are still genuinely independent. The conditioned polynomial is a quadratic form in `(X_0,P,N)` plus an arbitrary affine term and constant. Its quadratic matrix is

`H(t)=
 [[0, k, -k],
  [k, 1+2t, 1],
  [-k, 1, 1-2t]].`                                              (5.3)

Now make only an orthogonal change **inside the two-dimensional pair**, not across the independent scalar/pair split:

`C=(P-N)/sqrt(2)`,
`D=(P+N)/sqrt(2).`                                               (5.4)

Since `(P,N)` has joint density `p_P p_N`, (3.7) gives

`||p_(P,N)||_infinity <= (2sqrt(2))^2=8`.                       (5.5)

The rotation (5.4) has Jacobian one, so

`boxed: ||p_(C,D)||_infinity<=8.}`                               (5.6)

Also `X_0` remains independent of the whole pair `(C,D)` and has density cap one. No independence between `C` and `D` is needed or asserted.

In coordinates `(X_0,C,D)`, direct multiplication gives

`H'(t)=
 [[0, sqrt(2)k, 0],
  [sqrt(2)k, 0, 2t],
  [0, 2t, 2]].`                                                  (5.7)

Thus the partner notation (2.1) has

`K=1`, `M=8`,
`beta=sqrt(2)k`, `alpha=0`, `delta=2t`, `gamma=2`,               (5.8)

and hence

`boxed: |beta^2 gamma|=4k^2=4r^2/(1+r^2).}`                     (5.9)

The affine term created by the two conditioned banks causes no issue. Since

`det H'(t)=-4k^2 !=0`,                                           (5.10)

any affine term is removed by a deterministic translation of `(X_0,C,D)` for that conditioned value. Such translations preserve the scalar density cap, the pair density cap, and scalar/pair independence. Therefore the partner theorem applies uniformly for every conditioning value.

## 6. Full-line density bound

Substitute (5.8)--(5.9) into the completed account02/B18 theorem (2.1):

`||p_(Q | Z_+-,Z_--)||_infinity
 <=3(2*8*1)^(2/3)(4k^2)^(-1/3)
 =12 k^(-2/3)
 =12 ((1+r^2)/r^2)^(1/3).`                                      (6.1)

The right side is independent of the conditioned values. Averaging the conditional densities therefore gives

`boxed:
 ||p_Q||_infinity
 <=12 ((1+r^2)/r^2)^(1/3)
 <=12*2^(1/3)
 =15.1190525987385... ,  r>=1.`                                 (6.2)

This proves essential boundedness on the **entire real line** for the four-ray grouped family.

The latest account02/B18 one-sheet theorem is simultaneously applicable to the same target form and gives the sharper half-line estimate

`boxed: p_Q(t)<=pi sqrt(2)=4.442882938... for a.e. t>=0.}`       (6.3)

Thus any possible large value in this family can only occur on the two-sheet half-line, where (6.2) supplies the new uniform bound.

## 7. Strict extension and improvement over the preceding Hadamard packet

The preceding account01/B18 run treated the special Walsh--Hadamard case in which, after a sign normalization, every nonzero `theta_j` has the same magnitude. Its three-independent-scalar route gave the full-line bound `<630`.

The present theorem allows arbitrary magnitudes `theta_j`, arbitrary bank cardinalities, and arbitrary fragmented cap-one laws. The Parseval condition alone forces only the **total squared mass** `1/4` in each sign bank. On the old equal-weight family, (6.2) improves the full-line certificate from `630` to

`12*2^(1/3)=15.1190525987...`                                    (7.1)

while retaining (6.3) on the majority-sign half-line.

The mechanism is materially different from the old proof: the exact two-bank grouping produces a genuinely independent scalar/pair split, and the designated partner's null-pivot kernel handles arbitrary dependence created by the orthogonal rotation inside the pair.

## 8. Correction audit

The proof is compatible with the current correction ledger.

- **No post-rotation independence:** the only independence assertion is `X_0` versus the pair generated by disjoint residual source banks. The rotation `(P,N)->(C,D)` is allowed because the partner theorem requires only a joint density cap for the pair.
- **No conditional-cap-as-independence:** the partner theorem starts from genuine scalar/pair independence. We do not infer independence from a conditional density bound.
- **No arbitrary-joint coarea:** the nonlinear density estimate is the pinned null-scalar kernel, whose proof integrates the genuine independent scalar first and uses curvature in the dependent pair.
- **No fixed minor / coefficient deletion:** the bank identity (3.5) is exact and uses the whole four-ray frame.
- **No pointwise Fresnel decay:** none is used.

## 9. Remaining connection to the full target

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED**. The new theorem pays a substantially larger structured portion of the account02/B18 diffuse-star/two-sheet obstruction, but an arbitrary N3 diffuse star does not have to lie on four exact Walsh rays.

The next structural implication suggested by this proof is therefore:

`QFORM-DIFFUSE-STAR-FOURBANK-OR-PAID-v1`:

> Starting from the account02/B18 N3 identities `sum q_j^2=1` and `max q_j^2<2 tau`, construct a bounded number of disjoint original-coordinate banks whose three coefficient vectors form a quantitatively nondegenerate null-pivot scalar/pair packet, or prove that failure enters an already-paid physical-pair/ridge/volume branch.

Approximate replacement of a general row by a four-ray row is **not** licensed: the live coefficient-perturbation corrections forbid treating small row errors as harmless without a new uniform argument.

A separate exact-rank-three near-coloop collar and the arbitrary-additional-spectrum interaction also remain open elsewhere in the fleet.

## 10. Source pins and status

- Primary marginal theorem: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.
- Designated partner payoff: account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, report blob `7d4e66d4305ec7e63418078b4c8f8a274db16dd1`.
- Latest partner one-sheet reduction: account02/B18 `20260923T040922Z-account02-B18-QFORM-auto11`, canonical math `yspennstate/math-open-problems@826920faef301e7d6880266805e11a0a7350076f`, report blob `7a8aa858eb243f3165c4bc42fea030be34d3f286`.
- Preceding account01/B18 equal-weight Hadamard packet: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T045524Z-account01-B18-qform-r24/REPORT.md`.

Independent end-to-end review: **not performed**. This is a supporting target-level branch, not a claim of the full theorem.
