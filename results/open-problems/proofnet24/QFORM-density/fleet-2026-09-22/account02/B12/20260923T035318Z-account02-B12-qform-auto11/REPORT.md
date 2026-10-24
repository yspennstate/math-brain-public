SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T03:53:18Z.
attacking: a hybrid matrix-level stability theorem for arbitrary-magnitude added spectrum plus an arbitrary small dense tail: use fifth-volume rank reserve when no physical shielding is available, and a rank-plus-leakage decomposition when the added spectrum is only approximately shielded.

# account02/B12 auto11 — five-volume rank reserve and leaky-shield stability

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED_SUPPORTING_STABILITY / REQUIRED-e5f-RESULT-APPLIED / DESIGNATED-PARTNER-APPLIED / FULL_QFORM_OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and first unpaid implication

The full target remains OPEN: for arbitrary independent real ORIGINAL-coordinate inputs with densities at most one and arbitrary real symmetric A having at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X, or give a valid counterexample. No moment, bounded-support, connected-support, log-concavity, identical-law, diagonal-basis, or post-rotation independence assumption is introduced. Continuity is separate.

This run proves two complementary matrix-level exits for additional spectrum under an arbitrary dense operator-norm tail.

The first unpaid implication after them is structural:

> From only s_3(A)>=1, force either (i) an original-coordinate cross cut with enough rank reserve for the five-volume exit, (ii) a three-volume/collective-tail cut on which the added spectrum has small unshielded physical leakage, or (iii) an already-paid physical pair/triple, hub, ridge, grouped-bank, or scalar-pivot exit.

Neither theorem below asserts that the bare three-eigenvalue hypothesis automatically produces such a cut. They show exactly what additional eigenvalues and dense tails cost once a cut has been found.

## 2. Completed sources actually used

### Required newest-Claude source

At

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

the proved fifth-volume theorem D_5 states: for any ORIGINAL-coordinate cross block M=A_IJ,

`Z_5=e_5(M^T M)`,

with no row-marginal condition,

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`.                 (2.1)

All self blocks, outside couplings and affine terms are arbitrary. Its proof stays in original coordinates and uses no post-rotation independence.

The same source proves D': if the three-volume row marginals satisfy alpha_i<=h<3/4, then

`||p_Q||_infinity <= 6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) E_3(M^T M)^(-1/6)`.  (2.2)

### Current collective-tail marginal estimate

The current volume-tail package at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`,

supplies, for `T2(M)=sum_{j>=3}s_j(M)^2` and any row projection P,

`sqrt(alpha_i) <= sqrt(P_ii)
 + sqrt(3)|| (I-P)M ||op / sqrt(T2(M)) sqrt(1-P_ii)`.            (2.3)

Its sharper terminal coefficient under max P_ii<=1/2 and leakage<=sqrt(T2)/15 is

`C_tail=9 sqrt(3)e/2`.                                           (2.4)

### Designated partner account03/B12

The completed account03/B12 r23 scalar-Schur compiler is

`yspennstate/math-open-problems@4894ced504d555e84620c46029ed08a2af389d9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T024437Z-qform-eigenvalue-r23/REPORT.md`.

If a terminal Schur form has cap B/L, any preceding chain of ORIGINAL-coordinate scalar pivots with

`|a_j| >= (4/B)L`                                                (2.5)

preserves that same cap, with no independence assumption between completed squares and dependent remainders. Threshold-preserving physical Schur inheritance separately loses at most one >=L spectral direction per scalar pivot without degrading L.

## 3. A no-shield theorem from fifth-volume rank reserve

The previous B12 run controlled an arbitrary-magnitude rank-r addition when its row footprint was exactly shielded. The first theorem here removes the shielding condition entirely, at the cost of two extra cross-singular reserve directions.

Let I,J be disjoint original-coordinate banks. Write the final cross block as

`M = M0 + L + E`,                                                (3.1)

where

`rank L <= r`,          `||E||op <= delta`.                       (3.2)

Here L may have arbitrarily large operator norm. In the spectral-addition application it is the cross compression of an arbitrary rank-r symmetric added spectral block. E is allowed to be the cross compression of an arbitrary full-rank symmetric dense tail T with `||T||op<=delta`.

For j=1,...,5 define

`b_j = (s_{r+j}(M0)-delta)_+`.                                   (3.3)

### Theorem 3.1 — QFORM-FIVE-VOLUME-RANK-RESERVE-STABILITY-v1

If b_5>0, then every independent cap-one product source satisfies

`boxed:
 ||p_Q||infinity
 <= 5 sqrt(2e) (prod_{j=1}^5 b_j)^(-1/5).`                       (3.4)

All final self blocks, all outside blocks, every affine term, and every sign and magnitude represented in L are unrestricted.

In particular, if

`s_{r+5}(M0) >= gamma > delta`,                                  (3.5)

then

`boxed: ||p_Q||infinity <= 5 sqrt(2e)/(gamma-delta).`            (3.6)

#### Proof

A rank-r singular-value interlacing inequality gives, for j>=1,

`s_j(M0+L) >= s_{j+r}(M0)`.                                     (3.7)

Weyl's operator-norm inequality then yields

`s_j(M) >= (s_j(M0+L)-delta)_+
         >= (s_{j+r}(M0)-delta)_+
         = b_j`,                                                 (3.8)

for j=1,...,5. Since

`e_5(M^T M)`

is the sum over all products of five squared singular values, it contains in particular the product of the five largest squared singular values. Therefore

`e_5(M^T M) >= prod_{j=1}^5 s_j(M)^2
             >= prod_{j=1}^5 b_j^2`.                            (3.9)

Apply the completed e5f D_5 theorem (2.1) to the ACTUAL final original-coordinate cross block M:

`||p_Q||infinity
 <=5 sqrt(2e) [prod b_j^2]^(-1/10)
 =5 sqrt(2e)(prod b_j)^(-1/5)`.                                 (3.10)

This proves (3.4). Under (3.5), every b_j>=gamma-delta, giving (3.6). QED.

### Spectral interpretation

Let the full symmetric perturbation be

`S=sum_{a=1}^r tau_a v_a v_a^T`,                                (3.11)

with arbitrary real tau_a, and let T be any symmetric matrix with `||T||op<=delta`. On the cut I|J,

`L=S[I,J]=sum_a tau_a (v_a)_I (v_a)_J^T`,                       (3.12)

so rank L<=r independently of the signs and magnitudes of all tau_a. Also `||T[I,J]||op<=delta`. Hence Theorem 3.1 controls arbitrary-magnitude additional eigenvalue changes with **no leverage, localization or shielding assumption on their physical footprint**, provided the baseline cut carries r+5 robust singular directions.

Nothing here says that the random variable `X^T T X` is small. The norm delta is used only in the deterministic inequality (3.8) for the final matrix.

## 4. Exact target-class application: 251 eigenvalues may change arbitrarily

Take m=256 and

`A0 = [[0, 2 I_m], [2 I_m, 0]]`.                                (4.1)

Its eigenvalues are +2 and -2, each with multiplicity m. For k=1,...,251 set

`z_k=(e_k,e_k)/sqrt(2)`,                                        (4.2)

which are orthonormal +2 eigenvectors of A0. For arbitrary real parameters tau_1,...,tau_251 define

`S=sum_{k=1}^{251} tau_k z_k z_k^T`,                             (4.3)

and add any symmetric dense T satisfying

`||T||op<=0.01`.                                                 (4.4)

Before T, (4.3) literally replaces 251 eigenvalues +2 by `2+tau_k`; each parameter can be arbitrarily small, arbitrarily large, positive or negative. At least 5 positive +2 eigenvalues and all 256 negative -2 eigenvalues remain untouched. After (4.4), at least 261 singular directions still have magnitude at least 1.99, so every member of the family remains in the exact QFORM target class.

Across the first-bank/second-bank cut,

`M0=2 I_256`, `rank S[I,J]<=251`, and `||T[I,J]||op<=0.01`.      (4.5)

Thus r=251, gamma=2, delta=0.01 in (3.6), and

`boxed:
 ||p_{X^T(A0+S+T)X}||infinity
 <= 5 sqrt(2e)/1.99
 = 5.85840196381187...`                                         (4.6)

uniformly over **all 251 arbitrary eigenvalue changes**, every such dense full-rank tail T, and every independent cap-one product law.

The enormous self blocks created when some |tau_k| is huge are retained exactly; theorem D_5 permits arbitrary self blocks and outside coupling.

## 5. Leaky shielding: interpolate between rank reserve and norm reserve

The five-volume theorem is deliberately coarse: it spends r+5 baseline cross directions. When only r+3 collective-tail reserve is available, exact shielding can be relaxed quantitatively.

Let again

`M=M0+L+E`,                                                      (5.1)

and let P be a row-side orthogonal projection with

`max_i P_ii <= 1/2`.                                             (5.2)

Do **not** assume `(I-P)L=0`. Split exactly

`L_sh = P L`,          `L_leak=(I-P)L`.                          (5.3)

Set

`r >= rank(L_sh)`,
`eta = ||L_leak||op`,
`delta >= ||E||op`,
`rho = eta+delta`.                                               (5.4)

Then

`M=M0+L_sh+E'`,       `E'=L_leak+E`,                            (5.5)

with

`rank L_sh<=r`, `(I-P)L_sh=0`, `||E'||op<=rho`.                 (5.6)

Define

`a1=(s_{r+1}(M0)-rho)_+`,
`a2=(s_{r+2}(M0)-rho)_+`,
`B^2=sum_{k>=r+3}(s_k(M0)-rho)_+^2`,
`epsilon0=||(I-P)M0||op`.                                       (5.7)

### Theorem 5.1 — QFORM-LEAKY-SHIELD-RANK-NORM-SPLIT-STABILITY-v1

If a2>0, B>0, and

`epsilon0+rho <= B/15`,                                         (5.8)

then the required e5f D' result gives

`boxed:
 ||p_Q||infinity <= 9 sqrt(3e) (a1 a2 B)^(-1/3).`               (5.9)

Using the current sharpened collective-tail terminal gives the stronger coefficient

`boxed:
 ||p_Q||infinity <= (9 sqrt(3)e/2)(a1 a2 B)^(-1/3).`            (5.10)

The final Fourier terminal is continuous at this certificate.

#### Proof

Apply the rank-r singular-value inequality to M0+L_sh and Weyl with E'. Exactly as in Section 3,

`s1(M)>=a1`, `s2(M)>=a2`, and

`T2(M)=sum_{j>=3}s_j(M)^2 >= B^2`.                              (5.11)

The shielding of L_sh and (5.6) give

`||(I-P)M||op
 <=||(I-P)M0||op + ||(I-P)E'||op
 <=epsilon0+rho
 <=B/15
 <=sqrt(T2(M))/15`.                                              (5.12)

Use the current row-marginal inequality (2.3). For P_ii<=1/2, the right side is maximized at P_ii=1/2, hence

`alpha_i <= (1+sqrt(3)/15)^2/2
          =0.6221367205... < 2/3`.                               (5.13)

Therefore the **completed e5f theorem D'** applies with h=2/3 to the actual final M. Since

`E3(M^T M)>=s1(M)^2 s2(M)^2 T2(M)>=a1^2 a2^2 B^2`,             (5.14)

(2.2) gives exactly (5.9). The current sharpened collective-tail terminal applied to (5.11)-(5.12) gives (5.10). QED.

### Spectral-cloud leakage formula

For (3.11),

`eta=||(I-P)S[I,J]||op`

and the triangle inequality gives the explicit source-valid certificate

`eta <= sum_a |tau_a|
             ||(I-P)(v_a)_I||_2 ||(v_a)_J||_2`.                 (5.15)

Thus the protected component of an added eigendirection may have arbitrary amplitude for free; only its **unprotected physical cross-cut amplitude** is paid. An eigenvalue |tau_a| may tend to infinity provided the corresponding unprotected footprint shrinks fast enough. This is a deterministic matrix statement, not a claim about independence in a spectral basis.

## 6. Exact nonzero-leak target family

The new theorem is not merely the old exact-shield theorem with different notation. Here is a family with genuinely nonzero leakage.

Again take m=256 and A0 from (4.1). Let u1,u2 be two orthonormal vectors in R^m and let

`P=u1 u1^T`.                                                     (6.1)

Choose u1 flat, so `max_i P_ii=1/256`. Put c=0.02 and, for each tau in R,

`epsilon_tau = c/(1+|tau|)`,
`w_tau = sqrt(1-epsilon_tau^2) u1 + epsilon_tau u2`,
`z_tau=(w_tau,w_tau)/sqrt(2)`.                                  (6.2)

For every tau, z_tau is an exact +2 eigenvector of A0. Thus

`S_tau=tau z_tau z_tau^T`                                      (6.3)

literally replaces one eigenvalue +2 by 2+tau. Across the physical cut,

`L_tau=(tau/2) w_tau w_tau^T`.                                 (6.4)

For tau!=0, `(I-P)L_tau` is nonzero, so the preceding exact-shield theorem does not apply with this P. But

`rank(P L_tau)<=1`,
`eta_tau=||(I-P)L_tau||op
        =(|tau|/2) epsilon_tau
        <= c/2=0.01`.                                           (6.5)

Add any symmetric dense T with `||T||op<=delta=0.01`. Then rho<=0.02. For M0=2I_256 and r=1,

`a1=a2>=1.98`,
`B>=1.98 sqrt(253)=31.493827966761994...`,
`epsilon0=||(I-P)2I||op=2`.                                    (6.6)

The gate holds:

`epsilon0+rho <=2.02
 < B/15=2.099588531117466...`.                                  (6.7)

Therefore the source-completed e5f D' inequality (5.9) gives

`boxed: ||p_Q||infinity <=5.161371276818423...`,                (6.8)

and the sharpened tail coefficient gives

`boxed: ||p_Q||infinity <=4.254831305035606...`.                (6.9)

Both bounds are uniform for every real tau and every dense T of norm at most 0.01. Before T, all but one of the 512 eigenvalues still have modulus exactly 2; after T, at least 511 singular directions have modulus at least 1.99. Hence this is safely inside the exact target class for every tau.

This family demonstrates the intended new regime: the added eigenvalue is unbounded and the physical leakage is **not zero**, yet the large eigenvalue is stable because the product `|tau| times unshielded footprint` stays bounded.

## 7. Designated partner account03/B12 applied to the new terminal

Apply the account03/B12 one-sided scalar-Schur compiler to the concrete no-shield D_5 terminal (4.6). At scale L=1 its normalized cap is

`B5=5.85840196381187...`.                                       (7.1)

The partner threshold (2.5) is therefore

`4/B5=0.6827800524287226...`.                                   (7.2)

Consequently, any number of preceding ORIGINAL-coordinate scalar Schur extensions, with arbitrary signs and cross couplings, preserve the same cap (4.6) whenever every pivot satisfies

`boxed: |a_j|>=0.6827800524287226...`.                           (7.3)

No independence between a completed square and its dependent quadratic remainder is used. If these pivots are also peeling additional large spectral directions, the partner's threshold-preserving Schur inheritance performs the separate spectral bookkeeping without degrading the threshold scale.

For the sharper leaky terminal (6.9), the exact no-loss threshold is `4/4.254831305035606=0.9401077770735559...`; the looser e5f-only terminal (6.8) needs only `4/5.161371276818423=0.774987...` if one chooses to preserve that looser cap.

## 8. Why this does not use small matrix norm as a small random perturbation

A small dense matrix can generate an arbitrarily large quadratic random variable on admissible unbounded/translated cap-one inputs. For example, for `T=delta e_1 e_1^T` and `X_1` uniform on `[R,R+1]`,

`X^T T X = delta X_1^2 >= delta R^2` almost surely.              (8.1)

Accordingly, delta is used only in singular-value inequalities for the actual final cross block. No convolution with `X^T T X`, no probabilistic closeness, and no moment estimate appears anywhere above.

## 9. Relation between the two exits

The new results form a clean rank-versus-leakage tradeoff.

- **No shield at all:** spend five surviving cross singular directions after the arbitrary-rank addition; Theorem 3.1 is completely insensitive to the addition's magnitude, sign, and leverage.
- **Only three collective directions available:** protect most of the addition inside a low-leverage row subspace and pay the remainder by its actual unshielded operator norm; Theorem 5.1 interpolates continuously away from exact shielding.
- **Exact shield:** eta=0 recovers the previous account02/B12 rank-reserve theorem.

This identifies a concrete next structural target for the full proof: a bare three-large-eigenvalue N3 matrix that evades the known local/hub/ridge exits must be shown either to carry a five-direction cross reserve after the hostile added-spectrum rank is spent, or to have the hostile spectrum concentrated enough that its unshielded physical leakage is small on a three-volume cut. The global spectral hypothesis alone has not yet been proved to force that alternative.

## 10. Status and integrity

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. The present results are supporting stability theorems and exact target-class applications, not a full solution.

No Gaussianity, log-concavity, compact support, moments, centeredness, identical laws, post-rotation independence, law-uniform pointwise oscillatory decay, arbitrary-joint coarea bound, worst normalized conditional-fiber cap, or numerical inference is used. Finite numerical checks, if recorded separately, are only sanity checks of deterministic inequalities and constants.
