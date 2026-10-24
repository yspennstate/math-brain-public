SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T02:13:15Z.
attacking: optimize the admissible three-volume certificate by constrained KL reweighting, and test it on a full-rank genuinely rotated indefinite family where canonical volume sampling approaches the forbidden 3/4 marginal boundary.

# account01/B04 auto11 — entropy-weighted three-volume Fourier certificate

Programme: `QFORM-DENSITY-3EIG-20260922`. Fresh owner control at publication remained revision `2026-09-22.15`, QFORM only.  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver/ingestion was observed).

The full conjecture is NOT proved here, and full-target continuity is NOT proved here. The result below gives a new continuous-density exit for a cross-block class and converts the volume-marginal gate into an exact entropy/diagonal-scaling optimization. It uses no law-uniform pointwise quadratic-phase decay, no spectral-coordinate independence, no arbitrary-joint coarea estimate, no positive moment of a worst conditional projection-density cap, and no uniformly good physical minor.

## 1. Conditional end-to-end route and first missing implication

For an original-coordinate cut `I sqcup J`, write `M=A[I,J]`. The sharp three-volume Fourier theorem from

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

states that, with `Z=e_3(M^T M)>0`, if the canonical third-volume row marginals obey `alpha_i<=q/2`, `1<=q<3/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,

and the density is continuous. All within-bank terms, outside couplings and affine terms are retained.

The obstruction is that the canonical volume law can have a row marginal arbitrarily close to `3/4`, making the admissible `q` approach `3/2` and the constant blow up. The first question attacked here is:

> Can one redistribute the determinant mass among the SAME physical minors, paying only a controlled entropy price, so that all row marginals fall below the Fourier gate before any reciprocal local-minor cost is paid?

The answer is yes. The exact cost is a convex KL projection, and it has a closed diagonal-scaling dual.

## 2. Entropy-weighted sharp three-volume theorem

Let

`Omega={(S,T): |S|=|T|=3, det M[S,T] !=0}`,

`Z=sum_Omega det(M[S,T])^2=e_3(M^T M)`,

and let the canonical volume law be

`v_{S,T}=det(M[S,T])^2/Z`.

Let `w` be ANY probability law on `Omega`. Define

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`,

and

`K=KL(w||v)=sum_Omega w log(w/v)`.

### Theorem 2.1 — `QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1`

If `1<=q<3/2` and

`max_i alpha_i <= q/2`,

then the full original-coordinate quadratic-plus-affine form has a continuous density and

`||p_Q||_infinity
 <= [3e/((3-2q)sqrt(q))] Z^(-1/6) exp(K/6)`.                 (2.1)

Equivalently, define

`I_q(M)=inf{KL(w||v): w on Omega, alpha_i(w)<=q/2 for all i}`

and

`Z_eff(q;M)=Z exp(-I_q(M))`.

Then whenever the feasible set is nonempty,

`||p_Q||_infinity
 <= [3e/((3-2q)sqrt(q))] Z_eff(q;M)^(-1/6)`.                 (2.2)

Thus the correct currency is not merely raw third-volume `Z`; it is third-volume after the minimum entropy needed to flatten its row marginals.

### Proof

The source proof expands the Gaussian Brascamp--Lieb denominator as

`det(D_J+M^T D_I M)
 >= sum_Omega det(M[S,T])^2
        prod_(i in S) d_i prod_(j notin T)e_j`.

Put

`x_{S,T}=prod_(i in S)d_i prod_(j notin T)e_j`.

For arbitrary `w`, weighted AM--GM applied to `sum v x` gives

`sum_Omega v_omega x_omega
 =sum_Omega w_omega [(v_omega x_omega)/w_omega]
 >= exp(sum w log(vx/w))`

`=exp(-K) prod_i d_i^(alpha_i)
              prod_j e_j^(1-beta_j)`.

Hence

`det(D_J+M^T D_I M)
 >= Z exp(-K) prod_i d_i^(alpha_i)
                  prod_j e_j^(1-beta_j)`.                     (2.3)

The endpoint convention is the same as in the source theorem: rows with zero exponent and columns with `beta_j=1` are dropped before the Gaussian optimization, so no inverse zero parameter is introduced.

Consequently the Brascamp--Lieb constant in the source proof acquires exactly the factor `exp(K/2)`. The sharp Hausdorff--Young/Jensen calculation is otherwise unchanged. Therefore

`E F_t^q
 <= exp(K/2) e^3 q^(-3/2)
      (pi/|t|)^3 Z^(-1/2)`.                                   (2.4)

From decoupling and Jensen,

`|phi_Q(t)|
 <= min{1,
    [exp(K/2)e^3 q^(-3/2)pi^3 Z^(-1/2)]^(1/(2q))
    |t|^(-3/(2q))}`.                                          (2.5)

Set `b=3/(2q)>1`. Integrating `min(1,C|t|^-b)` and applying Fourier inversion gives the source constant. The entropy multiplier is

`exp[(K/(4q))*(1/b)] = exp(K/6)`,

which proves (2.1). Since the characteristic function is integrable, the density has a continuous version vanishing at infinity. Taking the infimum over admissible `w` gives (2.2). QED.

## 3. Exact diagonal-scaling dual

The KL optimization in (2.2) is finite-dimensional and has an exact dual. Let `lambda_i>=0` and put

`D_lambda=diag(exp(-lambda_i/2))`.

### Proposition 3.1 — diagonal scaling formula

`Z_eff(q;M)
 = inf_(lambda_i>=0)
      exp[(q/2) sum_i lambda_i]
      e_3(M^T diag(exp(-lambda_i)) M)`.                         (3.1)

Moreover, any finite optimizer has Gibbs form

`w*_(S,T)
 proportional to v_(S,T)
 exp[-sum_(i in S)lambda_i]`,                                  (3.2)

with complementary slackness

`lambda_i(alpha_i(w*)-q/2)=0`.                                 (3.3)

### Proof

For `c=q/2`, the Lagrangian for the primal KL projection is

`KL(w||v)+sum_i lambda_i(alpha_i(w)-c)`.

Minimizing over probability laws `w` gives

`-log E_v exp[-sum_(i in S)lambda_i]-c sum_i lambda_i`.

But Cauchy--Binet gives exactly

`E_v exp[-sum_(i in S)lambda_i]
 = Z^(-1) e_3(M^T diag(exp(-lambda_i))M)`.                      (3.4)

Finite-dimensional convex duality therefore yields

`I_q(M)=sup_(lambda>=0)
 [log Z-log Z(lambda)-(q/2)sum lambda_i]`.

Exponentiating `log Z_eff=log Z-I_q` proves (3.1), and the Gibbs/KKT equations give (3.2)--(3.3). QED.

This is useful structurally: the volume-marginal obstruction is now an explicit diagonal row-scaling optimization. Failure of an entropy-weighted certificate means that every admissible flattening destroys a quantifiable amount of third exterior volume; it is no longer merely the statement that one canonical row is heavy.

## 4. A genuinely rotated full-rank family where the entropy repair removes the D' blow-up

Let `U` be the `7 x 7` orthogonal matrix with columns

`u1=e1`,

`u2=(e2+e3)/sqrt(2)`, `u3=(e4+e5)/sqrt(2)`, `u4=(e6+e7)/sqrt(2)`,

`u5=(e2-e3)/sqrt(2)`, `u6=(e4-e5)/sqrt(2)`, `u7=(e6-e7)/sqrt(2)`.

Let

`V=I-(2/7)11^T`,

which is a dense orthogonal Householder reflection. For `0<epsilon<=1/2`, set

`Sigma=diag(1,1,1,1,epsilon,epsilon,epsilon)`,

`M_epsilon=U Sigma V^T`,

and form the physical `14 x 14` symmetric matrix

`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`.                    (4.1)

Its eigenvalues are exactly

`+1` four times, `-1` four times,
`+epsilon` three times, `-epsilon` three times.                 (4.2)

Hence every `A_epsilon` satisfies the original spectral hypothesis, is indefinite, and for every `epsilon>0` the active cross block is full rank. At `epsilon=0.05` all 49 entries of `M_epsilon` are nonzero (finite check below), so this is genuinely rotated in the original product coordinates.

Put `t=epsilon^2`. Since the squared singular values are four copies of `1` and three copies of `t`,

`Z=e_3(M_epsilon^T M_epsilon)
  =4+18t+12t^2+t^3`.                                           (4.3)

The spectral weights entering the canonical third-volume row marginals are

`p_H=(3+9t+3t^2)/Z` for each of the four unit singular directions,

`p_L=t(6+8t+t^2)/Z` for each of the three epsilon directions.   (4.4)

By the chosen `U`,

`alpha_1=p_H`,

`alpha_2=...=alpha_7=(p_H+p_L)/2`.                              (4.5)

As `epsilon->0`, `p_H->3/4`; more precisely

`p_H=3/4-(9/8)t+O(t^2)`.

Therefore the canonical D' choice `q=2p_H` approaches the nonintegrable endpoint `3/2`, and its explicit constant blows up like `epsilon^(-2)` even though the matrix family itself remains well controlled.

### 4.1 Exact q=1 entropy projection

Let `R={1 in S}` under the canonical volume law. Then `P_v(R)=p_H`. For `0<epsilon<=1/2`, `p_H>1/2` (indeed `2(3+9t+3t^2)-Z=2-6t^2-t^3>0` for `0<t<=1/4`).

Define `w*` by preserving the canonical conditional laws on `R` and `R^c` but setting

`P_w*(R)=P_w*(R^c)=1/2`.                                       (4.6)

The row-volume law is invariant under the permutations of the three pairs `(2,3),(4,5),(6,7)` and swaps inside each pair. Thus rows `2,...,7` remain equiprobable under the tilt. Since every sampled row triple has size three,

`alpha_1(w*)=1/2`,

`alpha_2(w*)=...=alpha_7(w*)=(3-1/2)/6=5/12`.                  (4.7)

So `w*` is admissible at the strongest Fourier choice `q=1`.

It is also the exact KL minimizer. For any q=1 feasible `w`, data processing through the indicator of `R` gives

`KL(w||v)>=D_Ber(P_w(R)||p_H)`.

Since `p_H>1/2`, the minimum over `P_w(R)<=1/2` is attained at `1/2`; the tilt (4.6) attains equality because the conditional laws were left unchanged. Therefore

`I_1(M_epsilon)
 =D_Ber(1/2||p_H)
 =(1/2) log[1/(4p_H(1-p_H))]`.                                 (4.8)

Theorem 2.1 now gives the all-law bound

`||p_(X^T A_epsilon X)||_infinity
 <=3e Z^(-1/6)
      [4p_H(1-p_H)]^(-1/12)`.                                 (4.9)

This density is continuous. As `epsilon->0`, the right side converges to

`3e 4^(-1/6)(4/3)^(1/12)
 =6.629548713390117...`,                                       (4.10)

so the entropy repair removes the canonical marginal singularity completely.

At `epsilon=0.05`,

`Z=4.045075015625`,

`p_H=0.747209566775610`,

`I_1=0.140154844106244`,

and (4.9) gives

`||p_(X^T A X)||_infinity <=6.613114657572972`.                (4.11)

For comparison, using the same raw canonical volume law at its minimum admissible `q=2p_H` gives the sharp D' bound

`3e Z^(-1/6)/[(3-4p_H)sqrt(2p_H)]
 =473.4710956054595...`.                                       (4.12)

The enormous gap is not a change in the matrix or input law: it is entirely the cost of insisting on canonical volume marginals instead of reweighting the same physical minors.

## 5. Designated account02/B04 result applied on the SAME matrix

I now consume the completed OTHER-account theorem from account02/B04:

`QFORM-RANKR-TWOSIDED-CONTAMINATION-FOURIER-v1`,

`yspennstate/math-open-problems@8f8913581643a7e7bcbe7d8c178a2255194dfc3d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260922T233213Z-account02-B04-QFORM-r22/REPORT.md`.

For an exact-rank `r>=3` original-coordinate cross block with nonzero singular values `sigma_1,...,sigma_r`, it retains arbitrary measurable self-contamination on both product banks and gives

`||p_Q||_infinity
 <= e r/(r-2) (prod sigma_j)^(-1/r)`.                           (5.1)

On the SAME `M_epsilon`, `r=7` and

`prod sigma_j=epsilon^3`.

Therefore the partner theorem gives the actual inequality

`||p_(X^T A_epsilon X)||_infinity
 <=(7e/5) epsilon^(-3/7)`.                                     (5.2)

At `epsilon=0.05`, this is

`13.740634938992596...`.                                       (5.3)

It diverges as `epsilon->0`, because that exact-rank theorem pays the product of all seven nonzero singular values. The new entropy-weighted third-volume certificate instead stays below `6.630` along the entire small-tail limit. This is a direct partner-result application at its exact scope, and it exhibits a genuine division of labor:

- exact-rank product-Fourier rearrangement is strong when the whole nonzero cross spectrum is robust;
- entropy-weighted three-volume ignores arbitrarily small extra directions while retaining them in the full characteristic function and pays only the entropy required to flatten the active third-volume.

No singular direction is discarded by rotating the random inputs.

## 6. Finite exact/numerical checks

For `epsilon=0.05`, direct matrix checks give

`||U^T U-I||max <2.3e-16`,

`||V^T V-I||max <1.2e-16`,

`singular_values(M)=(1,1,1,1,0.05,0.05,0.05)`,

`min_ij |M_ij|=0.17677669529663684`,

`max_ij |M_ij|=0.7142857142857143`.

The attached finite checker records the formula values at `epsilon=0.5,0.1,0.05,0.01` and the limiting constant. These checks are arithmetic validation only; the proof is the analytic argument above.

## 7. What changed and what remains

Paid here:

1. a general entropy-weighted extension of the sharp three-volume Fourier theorem, with explicit factor `exp(KL/6)`;
2. an exact convex dual identifying the optimal volume-weight certificate with a diagonal row-scaling problem;
3. an explicit full-rank genuinely rotated indefinite target family on which the canonical D' constant diverges while the optimal entropy-weighted q=1 certificate remains `<=6.630` in the small-tail limit;
4. a direct application of the designated account02/B04 rank-r theorem on the same matrix, showing why exact-rank product-of-singular-values currency can deteriorate while entropy-weighted exterior volume remains stable.

Not paid:

- a universal lower bound on `Z_eff(q;A[I,J])` for some physical cut from only `s_3(A)>=1`;
- a proof that failure of every entropy-weighted cut forces a completed hub/ridge/grouped-coordinate branch;
- the full N3 theorem;
- the full QFORM conjecture;
- full-target continuity.

The next sharply defined implication is therefore

**`QFORM-ENTROPY-VOLUME-OR-HUB-ROUTING-v1` (OPEN):** starting only from the three-large-eigenvalue hypothesis, prove that some original-coordinate cut has `Z_eff(q;M)` bounded below at a universal scale for some `1<=q<3/2`, OR show from the diagonal-scaling dual (3.1) that every failure forces the matrix into an already-paid high-leverage hub, ridge, square-pivot, or grouped-coordinate branch. This is now an optimization/routing question rather than a local-minor selection problem.

Independent end-to-end review of this new theorem has not yet been recorded. Full target remains OPEN.
