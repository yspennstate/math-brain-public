# QFORM B15 — algebraic genericization with no loss of the universal height constant

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control:** `yspennstate/math-research-brain@e94ef1e63c1ae9f377eec4c7149fb04fa4967f2a`, OWNER CONTROL revision `2026-09-22.8`  
**Worker:** `account03/B15`  
**Run:** `20260922T173720Z-account03-B15-r14`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-REDUCTION / FULL-CONJECTURE-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The full target remains open: for every dimension, every product law with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal finite bound on the density of `Q=X^TAX`.

The preceding B15 run supplied a candidate proof that every fixed rank-at-least-three instance has a bounded `C_0` density, but with a matrix-dependent constant. Thus the decisive unpaid issue is **uniformity of the height constant as the physical matrix becomes degenerate in the original coordinates**. In particular, exact zero pivots are less important than uniform control as pivots tend to zero.

This report proves a no-loss reduction making that distinction rigorous.

## 2. Completed partner result actually used

The assigned partner `account04/B15` proved in

- `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`

that the optimal target height constants satisfy

`C_all = C_C0 = C_sm`,

including the value `+infinity`, where `C_sm` is the supremum restricted to compactly supported smooth cap-one marginal densities.

I use this theorem below in an actual target inequality, not merely as background.

## 3. Generic-matrix closure theorem

For fixed `n`, let `P_n={P_1,...,P_m}` be any finite family of nonzero real polynomials on the vector space `Sym_n` of real symmetric matrices. Define the algebraically generic locus

`G_n(P)={B in Sym_n : P_j(B)!=0 for every j}`.

This is open and dense because the zero set of each nonzero polynomial has empty interior.

Let `C_gen(P)` denote the optimal density-height constant over all dimensions `n`, all independent compactly supported smooth marginal densities `f_i` with `0<=f_i<=1`, and all target matrices `B` satisfying

`at least three eigenvalues of B have absolute value >=1`

and `B in G_n(P_n)`.

### Theorem

For every choice of finite polynomial families `P_n`,

`boxed( C_gen(P) = C_sm = C_all )`

including `+infinity`.

Thus a universal proof may assume any finite list of purely algebraic nondegeneracy conditions on the matrix, provided the final constant is independent of how close the matrix is to the excluded algebraic set.

### Proof

The inclusion of classes gives immediately

`C_gen(P) <= C_sm`.

It remains to prove `C_sm <= C_gen(P)`. If `C_gen(P)=+infinity` there is nothing to prove, so assume it is finite and call it `C`.

Fix one smooth compactly supported target instance `(X,A)`. Let

`s_3(A)`

be the third largest singular value of `A`. Because `A` is symmetric and has at least three eigenvalues of absolute value at least one,

`s_3(A)>=1`.

Take any sequence `epsilon_k downarrow0`. Set

`A_k^0=(1+2 epsilon_k)A`.

Because `G_n(P)` is dense, choose `B_k in G_n(P)` with

`||B_k-A_k^0||_op < epsilon_k`.

Singular values are one-Lipschitz in operator norm, hence

`s_3(B_k) >= s_3(A_k^0)-epsilon_k`
`           = (1+2epsilon_k)s_3(A)-epsilon_k`
`           >= 1+epsilon_k >1`.

Therefore every `B_k` is still a target matrix. Also

`||B_k-A||_op <= 2epsilon_k ||A||_op + epsilon_k ->0`.

Because the product input is compactly supported, define the finite number

`R_X = sup{ ||x||_2^2 : x belongs to supp(X) }`.

For every support point `x`,

`|x^T(B_k-A)x| <= ||B_k-A||_op ||x||_2^2 <= delta_k R_X`,

where `delta_k=||B_k-A||_op`.

Hence, for every bounded interval `I=[u,v]`, writing `I^eta=[u-eta,v+eta]`,

`{X^TAX in I} subset {X^TB_kX in I^(delta_k R_X)}`.

By the definition of `C=C_gen(P)`,

`P(X^TAX in I)`
` <= P(X^TB_kX in I^(delta_k R_X))`
` <= C ( |I| + 2 delta_k R_X ).`

Letting `k->infinity` gives the exact linear small-ball inequality

`boxed( P(X^TAX in I) <= C |I| )`                                      (3.1)

for the original, possibly algebraically degenerate, smooth target instance. Therefore its output law has density bounded by `C`. Taking the supremum over all smooth target instances proves

`C_sm <= C_gen(P)`.

Thus `C_gen(P)=C_sm`. Applying the completed `account04/B15` theorem `C_sm=C_all` gives the claimed equality.

No moment assumption was used. Compact support entered only in the explicit pointwise comparison above; the partner theorem is what allows this smooth compactly supported reduction without changing the optimal target constant.

## 4. Concrete genericity that may now be assumed in a universal proof

For each fixed `n` one may take `P_n` to contain, for example,

1. every coordinate entry polynomial `A_ij`;
2. every principal-minor determinant `det A_I`;
3. the discriminant of the characteristic polynomial (simple spectrum);
4. any additional finite collection of determinant, Schur-pivot, or transversality polynomials required by a particular proof architecture.

Each listed polynomial is nonzero as a polynomial, so their simultaneous nonvanishing locus is dense.

Consequently a universal-height proof may work on matrices for which all of these exact degeneracies are absent. What it **may not** do is assume a quantitative lower bound such as

`|A_ii|>=c`, `|det A_I|>=c`, or `spectral gap>=c`

with a universal positive `c`. The approximating generic matrices can have these quantities arbitrarily close to zero. Therefore a bound such as `1/|A_ii|`, `1/sigma_min(A_I)`, or any reciprocal-minor cost still fails to close the target when passed to the limit.

This identifies the live obstruction more precisely:

`boxed( exact algebraic degeneracy is removable; near-degeneracy with a uniform constant is not. )`

In particular, the owner's "zero/near-isotropic physical-pivot branch" separates into two issues: the exact zero case can be recovered by closure once a uniform generic bound exists, whereas the near-zero case is genuinely part of the universal theorem.

## 5. Application to the target inequality

Combining (3.1) with the partner equality gives the following conditional end-to-end statement.

> If one proves a universal constant `C` for compactly supported smooth cap-one product inputs and algebraically generic target matrices, with `C` independent of every genericity gap, then for every rough target input allowed by the owner and every target matrix, degenerate or not,
>
> `boxed( P(X^TAX in I) <= C |I| )`
>
> for every interval `I`, and therefore `||p_Q||_infinity<=C`.

This is a no-loss reduction of the full target, not a new hypothesis on the theorem.

## 6. Separate continuity statement: rank two is genuinely different

The main `L^infinity` problem and continuity should remain distinct. There is a simple sharp control showing that bounded density alone need not give a continuous representative below rank three.

Let `X_1,X_2` be independent `Uniform[-1/2,1/2]` variables and

`Q=X_1^2+X_2^2`.

For `0<q<1/4`, the disk of radius `sqrt(q)` is contained in the unit square, so

`P(Q<=q)=pi q`,

and hence every density version satisfies

`p_Q(q)=pi` for almost every `q in (0,1/4)`,

while `p_Q(q)=0` for almost every `q<0`. Therefore no continuous representative can exist: continuity at zero would require simultaneously the left limit `0` and the right limit `pi`.

So rank two can have a bounded but discontinuous quadratic-form density. This does not touch the owner's rank-three target; it confirms that the separate continuity assertion genuinely uses the extra rank/curvature available there.

The preceding B15 rank-at-least-three `C_0` theorem is at

- `yspennstate/math-open-problems@4813f09ed4f518a1ee172b77a0f1d315989a84e1`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T162724Z-account03-B15-r13/REPORT.md`,

and remains a worker-scope candidate pending independent review. The genericization theorem in Sections 3--5 does not depend on accepting that continuity proof.

## 7. Implication for the full proof and next obligation

The full conjecture remains OPEN. This run removes only exact algebraic degeneracies from the universal-height proof architecture. The first unpaid implication is now correctly phrased as a **uniform near-degeneracy estimate** on the generic locus, not a separate treatment of exact zero pivots.

For proof assembly, the useful handoff is:

- workers may perturb away exact zero diagonal entries, vanishing physical minors, repeated eigenvalues, and finitely many other algebraic coincidences;
- the density constant must remain uniform as those quantities tend to zero;
- therefore any route whose final price contains an uncancelled reciprocal small pivot/minor remains insufficient;
- grouped-coordinate/ridge mechanisms should be tested specifically for whether they eliminate that reciprocal price before the closure step.

No rotation of the independent coordinates, no moment assumption, and no continuity assumption on the original marginal densities is used in the full-target reduction.
