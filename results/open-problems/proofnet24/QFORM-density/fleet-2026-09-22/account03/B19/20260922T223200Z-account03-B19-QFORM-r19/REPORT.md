SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-22T22:32:00Z.
attacking: internal-rank-two aggregate O3 routing: compress rank-one companion banks honestly, pay their scalar/pair Schur channels with the rank-two half-Riesz and pair-log theorems, and isolate the first genuinely unpaid near-singular state.

# account03/B19 r19 — rank-one-bank Schur pivots and aggregate-pair payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control consumed:** revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Scope and correction boundary

The unrestricted target remains open: for arbitrary independent real coordinates with marginal densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential-density bound for `X^T A X`, or give a valid counterexample. Full-target continuity also remains open.

This run does not use post-rotation independence, the refuted arbitrary-joint three-dimensional coarea estimate, positive moments of conditional projection heights, law-uniform pointwise quadratic-phase decay, a worst-fiber supremum, a fixed good physical minor, or perturbative deletion of small coefficients under unrestricted supports. In particular, the argument below never treats a bounded projected density as independence.

The immediate source boundary is account03/B19 r18: the B10 near-span aggregate O3 packet is already paid if all three resource banks are spectral-rank-one. Its first unpaid interface was `QFORM-O3-INTERNAL-RANK2-ROUTING-v1`, where at least one resource bank has genuine internal spectral rank at least two. The present run proves a nontrivial portion of that interface and replaces the exactly-one-internal-rank-two case by a quantitative near-singular/double-near-null remainder.

## 2. Inputs used at their proved scope

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`: if `U^T U=I_2`, `Lambda` is invertible symmetric, and `X` is an independent cap-one product source, then

   `sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2)`
   ` <=128 |det Lambda|^(-1/4)`,

   with the sharper constant `16 sqrt(30)` when the affine term lies in `Ran U`, in particular for zero affine term. Source snapshot: `yspennstate/math-open-problems@3034661243d00674dd35b8c9f0959e68d9379543`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

2. Rogozin--Ball scalar product-projection bound: a normalized linear form of independent cap-one variables has density at most `sqrt(2)`. This is already source-pinned inside the preceding theorem and in B19 r18.

3. `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`: for two independent cap-one scalars with fixed invertible indefinite quadratic block `B`, determinant magnitude `D`, smallest singular value `kappa`, and an independent remainder obeying `sup_t P(|R-t|<rho)<=H sqrt(rho)`,

   `||p_Q||_infinity <=4 sqrt(2H) (D kappa)^(-1/4)`.

   Source: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

These are used only as supporting theorems at their stated source status; neither is promoted here to an independently reviewed full solution.

## 3. First theorem: an entire rank-one original-coordinate bank is a valid Schur pivot

Let the exact-rank-three form be

`A=R M R^T`, `R^T R=I_3`,

with invertible symmetric `M`. Let `H` be a nonempty bank of original coordinates whose spectral rows are all collinear:

`u_i=c_i v`, `i in H`, `|v|=1`,

and put

`lambda=sum_(i in H)c_i^2 >0`.

Let `G=H^c`. Define the normalized bank scalar

`Z=lambda^(-1/2) sum_(i in H)c_i X_i`.

Then `Z` is independent of `X_G` and has density cap at most `sqrt(2)`. Put

`t=v^T M v`, `a=lambda t`.

### Theorem 3.1 — `QFORM-RANKONE-BANK-SCHUR-PIVOT-v1`

If `a!=0`, then `Q=X^TAX` has an essentially bounded density and

`boxed: ||p_Q||_infinity <=16 sqrt(60) [lambda |a| |det M|]^(-1/4).`  (3.1)

The estimate is valid for either sign of `a`, every sign pattern of `M`, arbitrary fragmented supports, and all independent cap-one marginal laws.

### Proof

The total spectral projection is

`R^T X = R_G^T X_G + sqrt(lambda) v Z`.

Expanding and completing the square in `Z` gives

`Q = a ( Z + L(X_G) )^2 + X_G^T R_G N R_G^T X_G`,               (3.2)

where

`N=M-(Mv)(Mv)^T/t`.                                               (3.3)

Since `Nv=0` and `M` is invertible, `N` has rank exactly two. Moreover

`R_G^T R_G=I_3-lambda vv^T`,                                    (3.4)

so the nonzero eigenvalues of `R_G N R_G^T` are exactly the nonzero eigenvalues of

`N R_G^T R_G=N(I-lambda vv^T)=N`.                               (3.5)

In an orthonormal basis beginning with `v`, the lower `2x2` block of `N` is the Schur complement of the scalar `t`; hence

`|pdet N|=|det M|/|t|=lambda |det M|/|a|`.                      (3.6)

Conditional on `X_G`, translating `Z` preserves its density cap `sqrt(2)`. The density of `a(Z+m)^2` is bounded by

`sqrt(2) |a|^(-1/2) |s|^(-1/2)`.                               (3.7)

Average (3.7) over the rank-two residual in (3.2), and apply the sharper zero-affine form of the rank-two half-Riesz theorem:

`sup_w E |X_G^T R_G N R_G^T X_G-w|^(-1/2)`
` <=16 sqrt(30) |pdet N|^(-1/4)`.                               (3.8)

Substituting (3.6) into (3.7)--(3.8) gives (3.1). No transformed random coordinates are declared independent. QED.

This is the aggregate-bank analogue of a physical scalar pivot. It is stronger than selecting one coordinate from `H`: the whole rank-one bank is used before any reciprocal atom cost.

## 4. Second theorem: two rank-one banks admit a dependence-safe aggregate pair payment

Let `H_1,H_2` be disjoint rank-one banks,

`u_i=c_i v_1` on `H_1`, `u_j=d_j v_2` on `H_2`,

where `v_1,v_2` are linearly independent unit vectors. Put

`lambda_1=sum c_i^2`, `lambda_2=sum d_j^2`,

and let `G=(H_1 union H_2)^c`. Define normalized independent bank scalars `Z_1,Z_2`; each has density cap `sqrt(2)`.

The compressed two-bank quadratic block is

`B = [[lambda_1 v_1^T M v_1,
       sqrt(lambda_1 lambda_2) v_1^T M v_2],
      [sqrt(lambda_1 lambda_2) v_2^T M v_1,
       lambda_2 v_2^T M v_2]]`.                                (4.1)

Let `kappa=sigma_min(B)`. Define the complete principal-triple determinant bank through the two rank-one banks by

`mu = sum_(i in G,j in H_1,k in H_2) |det A[{i,j,k},{i,j,k}]|`. (4.2)

### Lemma 4.1 — exact aggregate geometry

If `g^2=|v_1 cross v_2|^2`, then

`boxed: mu=|det M| lambda_1 lambda_2 g^2.`                       (4.3)

If `B` is invertible and its spectral Schur remainder is `eta w w^T`, where `w` is the unit normal to `span(v_1,v_2)`, then

`boxed: |eta| |det B| = mu.`                                    (4.4)

#### Proof

For a triple containing one row from each bank,

`|det A_I|=|det M| det(R_I)^2`.

Summing first over the two collinear banks gives the factor `lambda_1 lambda_2`. With `w_0=v_1 cross v_2`, the remaining sum is

`w_0^T (sum_(i in G)u_i u_i^T) w_0`.

But

`sum_(i in G)u_i u_i^T=I-lambda_1v_1v_1^T-lambda_2v_2v_2^T`,

and `w_0` is orthogonal to both `v_1,v_2`, so the last expression is `|w_0|^2=g^2`. This proves (4.3).

For (4.4), use the basis `P=[v_1,v_2,w]`. Its squared determinant is `g^2`. The upper `2x2` block of `P^T M P` has determinant `det B/(lambda_1 lambda_2)`. Therefore its scalar Schur complement is

`eta = det(P^T M P) / det(V^T M V)`,

so in absolute value

`|eta|=g^2 |det M| lambda_1 lambda_2 / |det B|=mu/|det B|`. QED.

### Theorem 4.2 — `QFORM-TWO-RANKONE-BANK-PAIRLOG-v1`

If `B` is invertible and indefinite, then

`boxed: ||p_Q||_infinity <= C_pair (mu kappa)^(-1/4),`           (4.5)

where

`C_pair=4 sqrt(20) 8^(1/4) <30.085`.                            (4.6)

### Proof

Rescale `Y_a=sqrt(2) Z_a`; then `Y_1,Y_2` are independent cap-one scalars. Their quadratic block is `B/2`, whose determinant magnitude and smallest singular value are respectively

`D'=|det B|/4`, `kappa'=kappa/2`.                               (4.7)

Completing this pair leaves, on the independent complement `X_G`, an exact rank-one quadratic-affine remainder with coefficient `eta` and a unit coefficient vector: indeed the spectral Schur remainder annihilates `span(v_1,v_2)`, while `||R_G w||=1` because `w` is orthogonal to both bank directions. The rank-one affine small-ball lemma used in the pair-log theorem therefore gives

`H=10 |eta|^(-1/2)`.                                             (4.8)

Apply the general pair-log smoothing inequality to `B/2`:

`||p_Q||_infinity`
` <=4 sqrt(2H) (D' kappa')^(-1/4)`
` =4 sqrt(20) 8^(1/4) (|eta| |det B| kappa)^(-1/4)`.            (4.9)

Use (4.4) to obtain (4.5). The small determinant of the pair cancels against the large rank-one Schur curvature; only `mu` and the pair's smallest singular value remain. QED.

For a definite `B`, direct ellipse integration after the same `sqrt(2)` rescaling gives instead

`||p_Q||_infinity <=2 pi / sqrt(|det B|) <=2 pi/kappa`.          (4.10)

## 5. Actual attack on B19 r18's first missing O3 implication

After the r18 random split, the B10 mixed O3 branch carries a three-bank principal-determinant packet of mass at least

`mu_packet>=1/512`.                                               (5.1)

Suppose **exactly one** of those three resource banks has internal spectral rank at least two. The other two banks are rank-one; call them `H_1,H_2`. The complete bank `mu` in (4.2) includes every triple counted by the packet, hence

`mu>=mu_packet>=1/512`.                                          (5.2)

Let `B` be their compressed `2x2` block.

If

`kappa(B)>=1/64`,                                                (5.3)

then the branch is fully paid:

- if `B` is definite, (4.10) gives
  `||p_Q||_infinity <=128 pi <403`;
- if `B` is indefinite, (4.5) and (5.2) give

  `||p_Q||_infinity`
  ` <= C_pair ((1/512)(1/64))^(-1/4)`
  ` <404.772 <405`.                                              (5.4)

Thus an unpaid exactly-one-internal-rank-two O3 state must satisfy

`boxed: sigma_min(B)<1/64.`                                     (5.5)

There is a second, independent exclusion from Theorem 3.1. For a rank-one bank `H_a`, put

`theta_a=lambda_a |a_a| |det M|`,
`a_a=lambda_a v_a^T M v_a`.                                     (5.6)

If `theta_a>=1/4096`, then

`||p_Q||_infinity <=16 sqrt(60) (1/4096)^(-1/4)`
` =128 sqrt(60)<992`.                                            (5.7)

Consequently an unpaid state also satisfies

`theta_1,theta_2<1/4096`.                                       (5.8)

Moreover (5.2) implies

`|det M| lambda_1 lambda_2>=mu>=1/512`,                         (5.9)

because the geometric factor in (4.3) is at most one. Therefore, writing `t_a=v_a^T M v_a`,

`theta_1 theta_2`
`=(|det M|lambda_1lambda_2)^2 |t_1t_2|`,                        (5.10)

and (5.8)--(5.9) force

`boxed: |t_1 t_2|<1/64.`                                       (5.11)

So the broad internal-rank-two debt has been replaced, in the exactly-one-internal-rank-two chamber, by a rigid simultaneous state:

`boxed: sigma_min(B)<1/64, theta_1<1/4096, theta_2<1/4096, |t_1t_2|<1/64.`  (5.12)

This is a genuine mechanism change from physical-minor selection: all payments occur after product-preserving bank compression.

## 6. Required designated-partner application

The current designated partner account04/B19 proved `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` in the residual-diffuse exact-rank-three null-coloop branch. For residual determinant `D_res` with `0<D_res<=1` and `|det M|>=1`, it gives the continuous-density estimate

`||p_Q||_infinity <34 sqrt(log(e/D_res))`.                       (6.1)

Apply this to the actual threshold subbranch

`D_res>=e^(-8)`.                                                 (6.2)

Then

`log(e/D_res)<=9`,

hence

`boxed: ||p_Q||_infinity <102.`                                 (6.3)

Together with the partner's exact singular endpoint `D_res=0`, where the completed Witt bound is `<3e^(2/3)<5.844`, and its `D_res>=1` fixed-exponent bound `<11.748`, the null-coloop branch is now explicitly paid on

`D_res in {0} union [e^(-8),infinity)`.                          (6.4)

Only the punctured interval `0<D_res<e^(-8)` retains the partner's logarithmic nonuniformity. This is an equation-level use of the completed designated-partner theorem, not a formal citation.

Partner source: `yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

## 7. Updated compact proof map and exact remaining implication

The current source-valid assembly is now:

1. ridge/MSS-diffuse normalized-complement states are paid by the completed cross-rank-three route, including account02/B19 r20's `QFORM-NEARSPAN-NORMALIZED-COMPLEMENT-MSS-v1`;
2. B10 r19 converts the near-span structural singularity into a constant O3 aggregate packet;
3. B19 r18 pays the all-three-rank-one endpoint without selecting an atom;
4. this run pays every rank-one resource bank with a quantitative aggregate scalar Schur pivot, and pays the exactly-one-internal-rank-two O3 chamber whenever its two rank-one companion banks have a quantitatively nonsingular compressed pair;
5. account04/B19's adaptive theorem is applied above to close the quantitative null-coloop determinant range (6.4).

The full exact-rank-three problem is still open, as is the arbitrary-additional-spectrum theorem.

The first unpaid implication on the r18 O3 line is now:

### `QFORM-O3-NEARSINGULAR-DOUBLE-NEARNULL-COMPANIONS-v1` — OPEN

In the three-bank O3 packet with mass at least `1/512`, assume exactly one bank has internal spectral rank at least two and the two rank-one companion banks obey the simultaneous constraints (5.12). Prove a universal density bound by coupling the internal rank-two bank to the nearly singular companion pair, or route it to an already-paid cross-rank/ridge/grouped-square channel. The proof must remain uniform through exact zero scalar curvature and exact singularity of `B`; no coefficient-small perturbation argument is permitted.

A separate multi-rank chamber remains when at least two resource banks have internal spectral rank at least two. The arbitrary-extra-spectrum target also remains open.

## 8. Verification and status

`verify.py` checks the constants in (5.4), (5.7), (6.3), and randomized finite-dimensional instances of the exact determinant cancellation `|eta det B|=mu`. Its saved output terminates

`QFORM_B19_R19_BANK_PIVOT_CHECK_PASS`.

The numerical check is regression evidence only. The proof is the algebra above plus the pinned supporting theorems.

**New proved supporting claims:** `QFORM-RANKONE-BANK-SCHUR-PIVOT-v1`, `QFORM-TWO-RANKONE-BANK-PAIRLOG-v1`, and the quantitative O3 reduction (5.12).  
**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** partner branch (6.3) is continuous; Theorems 3.1 and 4.2 claim essential boundedness only.
