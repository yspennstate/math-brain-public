SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T08:58:02Z.
attacking: true near-coloop noncollinear mixed bank: force a quantitative longitudinal-regression residual and disjoint original-coordinate directional packets, then localize the remaining two-sheet receiver.

# account01/B10 auto11 — true-collar disjoint-packet compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW PRODUCT-PRESERVING STRUCTURAL COMPILER / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not established by the new structural theorem; the one-sheet source theorem quoted below gives a bounded density on its stated half-line only.

The unrestricted target remains OPEN: arbitrary finite `n`, independent original-coordinate real variables with densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, identical-law, diagonal-basis, or post-rotation independence hypothesis is introduced.

## 1. Fresh live state and exact sources actually used


The newest completed designated-partner result actually used is account02/B10 auto11:

`yspennstate/math-open-problems@16ecbcc3f6d34d4195ff6e29066216df155d9530`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T064541Z-account02-B10-QFORM-auto11/REPORT.md`.

It consumes account03/B10 r24 and sharpens the true near-coloop survivor to

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`,

`r_0=sqrt(c)e`, `c>63/64`, `rho=1-c<1/64`,

`alpha=e^T Lambda e`, `|alpha|<1/16`,

with genuinely mixed complementary rows

`r_j=s_j e+w_j`, `w_j perp e`, `j in M`,

and

`rho_M=sum_(M)s_j^2`, `H_M=sum_(M)w_jw_j^T`, `eta=||H_M||op`.

The mixed bank satisfies the exact coefficient cancellation

`boxed: sum_(j in M) s_j w_j=0`,                                      (1.1)

and every state not already paid by the r24 mixed-row excision theorem obeys

`boxed: eta>7/8`,                                                     (1.2)

and, more sharply,

`boxed: 1-eta < 2(1-rho_M)|alpha| <=2|alpha|`.                       (1.3)

The partner also proves `QFORM-COLLINEAR-PRODUCT-BANK-COMPRESSION-v1`: collinear disjoint original-coordinate banks may be compressed to genuinely independent scalar product-source variables, and a three-bank aggregate squared determinant `w` gives

`||p_Q||infinity <=2 C_3 (|det Lambda| w)^(-1/3)`,

`C_3=16 sqrt(30) 2^(1/4)`.

I use that result below to remove the already-paid collinear stress family from the new obstruction.

I also use my preceding completed B10 result

`QFORM-REGRESSION-RESIDUAL-TRANSVERSE-SPLIT-v1`,

`yspennstate/math-open-problems@6e2925e1a210871b4cfe53f5731578d0a71cb6d4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T035230Z-account01-B10-QFORM-r25/REPORT.md`.

For a bank `r_i=t_i u+p_i` whose transverse Gram `G=sum p_ip_i^T` is positive definite and whose regression residuals `e_i` obey `sum e_i p_i=0`, it produces disjoint ORIGINAL-coordinate subsets `S,T` with

`boxed: (sum_(i in S)e_i^2) det(sum_(j in T)p_jp_j^T) >= rho det G/24`,    (1.4)

where `rho=sum e_i^2`.

Finally, I apply the required Claude ruled-level-set theorem at its exact scope. At

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C proves for an exact rank-three signature `(2,1)` form with eigenvalue magnitudes at least one

`boxed: ess sup_(t>=0) p_Q(t) <= pi sqrt(2)`,                         (1.5)

and the sign-reversed half-line for signature `(1,2)`. It uses line marginals of the actual product projection, not independence of spectral coordinates. Thus in the indefinite true collar the remaining density debt is only the minority/two-sheet side. This is an actual mathematical application of the current Claude package, not a copied activity label.

## 2. The mixed bank is maximally non-graph-like in its top transverse direction

Let `v` be a unit top eigenvector of `H_M`; put

`y_j=v dot w_j`.

Then (1.1) and the definition of `eta` give

`sum_j s_j^2=rho_M`,
`sum_j y_j^2=eta`,
`sum_j s_j y_j=0`.                                                  (2.1)

Consequently

`boxed: min_(a in R) sum_j (s_j-a y_j)^2 = rho_M`.                 (2.2)

Indeed the left side equals `rho_M+a^2 eta` by (2.1). Thus none of the positive longitudinal coefficient energy is explained by the top transverse coefficient sequence. In particular the genuine positive-`rho_M` survivor is the opposite of an approximate graph at the coefficient level; treating it as a small perturbation of the partner's exact graph endpoint would be structurally wrong on arbitrary unbounded input laws.

There is also a strong deterministic hub coupling. Write relative to `R e direct_sum e^perp`

`Lambda=[[alpha,b^T],[b,C]]`.

Since `sigma_min(Lambda)>=1`,

`1 <= ||Lambda e||^2 = alpha^2+||b||^2`,

so using `|alpha|<1/16`,

`boxed: ||b||^2 >=1-alpha^2 >255/256`.                             (2.3)

Thus the remaining difficulty is not a lack of hyperbolic hub-to-transverse coefficient. It is preserving enough original-product provenance while spending that coefficient on the two-sheet side.

## 3. A sharp two-sequence disjoint split

### Lemma 3.1 — `QFORM-TRUECOLLAR-LONG-TOP-SPLIT-v1`

There is a partition of the ORIGINAL mixed-bank indices

`M=S disjoint_union T`

such that, with

`rho_S=sum_(i in S)s_i^2`,
`eta_T=sum_(j in T)y_j^2`,

one has

`boxed: rho_S eta_T >= rho_M eta/8 > 7 rho_M/64.`                 (3.1)

Consequently, whenever the displayed quantities are nonzero, the normalized scalar linear forms

`U_S=rho_S^(-1/2) sum_(i in S)s_i X_i`,
`V_T=eta_T^(-1/2) sum_(j in T)y_j X_j`                             (3.2)

are genuinely independent because they are functions of disjoint sets of ORIGINAL coordinates. Standard one-dimensional product-projection bounds give universal density caps for both. No rotated-coordinate independence is asserted.

### Proof

Normalize the deterministic coefficient pairs

`u_j=(s_j/sqrt(rho_M), y_j/sqrt(eta)) in R^2`.

Equation (2.1) says exactly

`sum_j u_j u_j^T=I_2`.                                             (3.3)

Set

`a_j=s_j^2/rho_M`, `b_j=y_j^2/eta`.

Then

`sum a_j=sum b_j=1`,

and because (3.3) is a Parseval frame,

`a_j+b_j=||u_j||^2<=1` for every `j`.                              (3.4)

Hence

`sum_j a_jb_j
 <=(1/4)sum_j(a_j+b_j)^2
 <=(1/4)sum_j(a_j+b_j)
 =1/2`.                                                            (3.5)

Now assign each original index independently to `S` or `T` with probability one half. Since an index cannot lie in both banks,

`E[rho_S eta_T]
 =(1/4) sum_(i!=j)s_i^2 y_j^2
 =(rho_M eta/4)(1-sum_j a_jb_j)
 >=rho_M eta/8`.                                                   (3.6)

At least one deterministic partition attains its expectation. The strict second inequality in (3.1) is (1.2). QED.

The constant `1/8` is the natural sharp endpoint of this proof: the normalized two-row frame with squared coordinate weights `a_j=b_j=1/2` has overlap sum `1/2`.

## 4. Exact compiler for the two partner Pluecker branches

Let the eigenvalues of `H_M` be

`eta>=xi>=0`,

with corresponding orthonormal transverse eigenvectors `(v,u)`. The partner's hub-Pluecker identity separates the hard packet into the cases `xi>=1/2` and `xi<1/2`. The following theorem upgrades both cases to disjoint original-product provenance.

### Theorem 4.1 — `QFORM-TRUECOLLAR-DISJOINT-PACKET-COMPILER-v1`

Under (1.1)--(1.3), one of the following holds.

**(A) Two-dimensional mixed packet (`xi>=1/2`).** There are disjoint original-coordinate subsets `S,T subset M` such that

`boxed:
 (sum_(i in S)s_i^2)
 det(sum_(j in T)w_jw_j^T)
 >= rho_M eta xi/24
 > 7 rho_M/384.
`                                                                    (4.1)

Thus one original source bank carries a longitudinal scalar coefficient packet while a disjoint original source bank carries a genuinely two-dimensional transverse determinant packet.

**(B) Mixed/pure-transverse three-direction packet (`xi<1/2`).** Let `P` be the pure-transverse original-coordinate class from the r24 decomposition. There are disjoint `S,T subset M`, also disjoint from `P`, such that

`boxed:
 (sum_(i in S)s_i^2)
 (sum_(j in T)(v dot w_j)^2)
 (sum_(k in P)(u dot w_k)^2)
 > 7 rho_M/128.
`                                                                    (4.2)

So the partner's large `P_MT` exterior packet can be refined into three mutually disjoint ORIGINAL-coordinate banks carrying the longitudinal direction, the top mixed transverse direction, and the complementary pure-transverse direction respectively.

### Proof of (A)

Here `H_M>0`. Apply the completed regression-residual split (1.4) to the mixed bank with

`t_j=s_j`, `p_j=w_j`, `G=H_M`.

Because of the exact cancellation (1.1), its regression vector is zero and the regression residual is exactly `e_j=s_j`; hence `rho=rho_M`. Therefore (1.4) becomes

`rho_S det(H_T) >= rho_M det(H_M)/24
                  =rho_M eta xi/24`.                              (4.3)

By `eta>7/8` and `xi>=1/2`, the right side is strictly larger than `7rho_M/384`. QED.

### Proof of (B)

Lemma 3.1 produces disjoint `S,T subset M` with

`rho_S eta_T >7rho_M/64`,                                        (4.4)

where `eta_T=sum_(j in T)(v dot w_j)^2`.

The total transverse Parseval ledger is `I_2`. The pure-longitudinal class has no transverse component, and `H_M` is the mixed transverse Gram. Hence the pure-transverse class `P` has Gram

`H_P=I_2-H_M`.                                                     (4.5)

Along the second eigenvector `u`,

`sum_(k in P)(u dot w_k)^2=1-xi>1/2`.                             (4.6)

Multiply (4.4) and (4.6) to obtain (4.2). QED.

This theorem is strictly stronger than merely knowing that the aggregate hub Pluecker packet is constant: it places the directional resources into disjoint source banks. It still does **not** make each bank scalar-sufficient. The `S` mixed rows also carry transverse components and the `T` mixed rows also carry longitudinal components. Those nuisance components are exactly why a conditional projection-density cap cannot be substituted for independence.

## 5. Actual designated-partner application

The latest account02/B10 report gives a target-valid true-collar stress family for every even `m>=64` with

`spec Lambda={1,1,-1}`,
`rho_M=1/256`,
`eta=1-1/(4m)`,
`xi=0`,
`alpha=-1/m`.

It lies in the genuine r24 survivor, while every individual physical pivot/pair/triple certificate tends to zero. The partner then pays it by collinear-bank compression with

`||p_Q||infinity<263.642`.                                        (5.1)

This completed partner result is therefore consumed as an actual branch payment, not re-proved.

The same family falls into Theorem 4.1(B). Since `m>=64`,

`eta>=255/256`,

and (4.2) can be sharpened directly from Lemma 3.1 to

`rho_S eta_T(1-xi)
 >=rho_M eta/8
 >=255/524288
 =0.0004863739... .`                                              (5.2)

Thus even the partner family that defeats every local scalar/pair/triple certificate has a fixed disjoint longitudinal/top-transverse/pure-transverse product packet. Its density is already paid by (5.1); equation (5.2) identifies the structure that a general noncollinear receiver should preserve.

## 6. What remains genuinely unpaid

The new compiler exhausts the two deterministic partner packet branches but does not yet produce an end-to-end density bound. The first unpaid implication is now

`QFORM-TRUECOLLAR-DISJOINT-PACKET-NUISANCE-RECEIVER-v1`:

> In the exact-rank-three near-null collar (1.1)--(1.3), use either the disjoint scalar/2D packet (4.1) or the disjoint three-direction packet (4.2), together with the strong hub coupling (2.3), to control the minority/two-sheet output density while allowing the mixed source banks to retain their same-bank longitudinal/transverse nuisance components.

The receiver must be scale-homogeneous as `rho_M->0`; neither (4.1) nor (4.2) has a positive lower bound independent of `rho_M`. It must therefore interpolate the shrinking packet with the near-null spectral data rather than divide by `rho_M` in isolation. Equation (1.3) says the missing pure-transverse top-direction mass `1-eta` is at most `O(|alpha|)`, while (2.3) says the hub cross coupling stays order one. A correct completion should spend these resources jointly.

The following shortcuts remain invalid and are not used:

- conditioning on a spectral projection and asserting a bounded conditional density;
- treating small longitudinal coefficients as a small random perturbation on unbounded inputs;
- selecting one local physical minor from the constant aggregate Pluecker packet;
- invoking law-uniform pointwise stationary-phase decay.

For indefinite signature, Claude Theorem C already pays the majority-sign one-sheet half-line by (1.5), so this receiver only needs the two-sheet side. Definite exact-rank-three forms are outside that ruled theorem and remain separately governed by the global proof map.

## 7. Status

`QFORM-TRUECOLLAR-DISJOINT-PACKET-COMPILER-v1` is a proved supporting structural theorem. It does not prove the arbitrary exact-rank-three theorem, does not prove the full arbitrary-spectrum QFORM conjecture, and does not prove a continuous density for the surviving branch. No independent end-to-end review has been performed for this new lemma. The full target remains `OPEN / NOT PROVED / NOT DISPROVED`.
