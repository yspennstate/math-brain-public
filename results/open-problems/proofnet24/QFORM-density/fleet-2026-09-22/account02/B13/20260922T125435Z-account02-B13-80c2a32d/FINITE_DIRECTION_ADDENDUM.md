# account02/B13 late mathematical advance — finite-direction rank-three aggregation

This addendum strengthens the same run's three-bank theorem. Full QFORM remains **OPEN / NOT PROVED**.

## Theorem — `QFORM-RANK3-M-DIRECTION-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by one. Let

`A=R Lambda R^T`

have rank exactly three, with `R^T R=I_3` and `sigma_min(Lambda)>=1` (equivalently all three nonzero eigenvalues of `A` have absolute value at least one). Suppose the nonzero rows of `R` lie in at most `m` projective directions, where `m>=3` is finite.

Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 2 C_3 binom(m,3)`,  (1)

where

`C_3=2 pi+3 sqrt(3)`.

In particular, if there are at most four projective row directions,

`||p_Q||_infinity <= 8 C_3 = 16 pi+24 sqrt(3) < 92`.  (2)

### Proof

Partition the active physical coordinates into the distinct row-direction classes `G_1,...,G_m`. Write

`r_i=alpha_i w_k` for `i in G_k`,

set

`s_k=(sum_{i in G_k} alpha_i^2)^(1/2)`,

and define

`v_k=s_k w_k in R^3`.

Let `V` be the `3 x m` matrix with columns `v_k`. The Parseval frame identity gives

`V V^T = sum_k v_k v_k^T = R^T R = I_3`.  (3)

Define an `n x m` matrix `C` by

`C_{ik}=alpha_i/s_k` for `i in G_k`,

and zero otherwise. Its columns have disjoint supports and unit Euclidean norm, so

`C^T C=I_m`,

and

`R=C V^T`.  (4)

Hence

`A=C B C^T`,  `B=V^T Lambda V`.  (5)

Set `Y=C^T X`. Since the columns of `C` have disjoint physical supports, the scalar variables `Y_1,...,Y_m` are independent. Each is a normalized linear form in a disjoint subset of the original independent coordinates. By the Livshyts--Paouris--Pivovarov one-dimensional product-marginal theorem,

`||p_{Y_k}||_infinity <= sqrt(2)` for every `k`.  (6)

Also

`Q=Y^T B Y`.  (7)

Now use Cauchy--Binet on the `3 x m` Parseval frame `V`:

`sum_{I subset [m], |I|=3} det(V_I)^2 = det(V V^T)=1`.  (8)

Thus some triple `I` satisfies

`det(V_I)^2 >= 1/binom(m,3)`.  (9)

Because `V_I V_I^T <= V V^T=I_3`, every singular value of the square matrix `V_I` is at most one. Therefore

`sigma_min(V_I) >= |det(V_I)| >= binom(m,3)^(-1/2)`.  (10)

Let `B_I=B[I,I]=V_I^T Lambda V_I`. By the multiplicativity lower bound for least singular values,

`sigma_min(B_I)
 >= sigma_min(V_I)^2 sigma_min(Lambda)
 >= 1/binom(m,3)`.  (11)

Condition on all aggregate coordinates `Y_j` with `j notin I`. The conditional quadratic polynomial in the three remaining independent variables has the form

`Y_I^T B_I Y_I + 2 b^T Y_I + c`,

where `b,c` depend on the conditioned values but the principal matrix `B_I` does not.

Scale only these three variables by

`Z=sqrt(2) Y_I`.

The `Z` coordinates are independent with densities bounded by one, and the conditional quadratic becomes

`Z^T (B_I/2) Z + 2 b'^T Z + c`,

with

`sigma_min(B_I/2) >= 1/[2 binom(m,3)]`.  (12)

Apply the source-pinned three-variable affine quadratic theorem `QFORM-3VAR-AFFINE-PRINCIPAL-v1`, which gives conditional density at most

`C_3 / sigma_min(B_I/2)
 <= 2 C_3 binom(m,3)`.  (13)

The bound is uniform in the conditioned outside aggregate coordinates, so averaging preserves it. This proves (1). For `m=4`, `binom(4,3)=4`, giving (2). QED.

## Why this is stronger than local physical-triple selection

The selected triple is a triple of **independent aggregate banks**, not a triple of original physical coordinates. Each bank may contain arbitrarily many physical coordinates, and every physical `3 x 3` principal block may be badly conditioned. The only combinatorial loss is the number of distinct spectral row directions.

For `m=3`, (1) recovers the main report's `4 pi+6 sqrt(3)<23` theorem. For `m=4`, it newly closes every four-direction rank-three frame with constant `<92`.

## Partner theorem applied again

Combine (2) with the completed `account03/B13` rational strict-slack witness theorem at candidate constant `C=92`. If the full owner inequality with constant `92` fails, there is a strict rational finite-fragment witness with three eigenvalues satisfying `|lambda|>1`. Such a witness cannot have rank exactly three with at most four projective spectral-row directions, because (2) gives strict bound `<92`.

Hence every rational strict `92`-counterexample must either

1. have rank greater than three, or
2. have rank exactly three with at least five distinct projective row directions.

This is a genuine target-level reduction, not a finite census.

## Remaining implication

The rank-three aggregation debt is now:

`QFORM-RANK3-UNBOUNDED-DIRECTION-AGGREGATION-v1` — obtain a direction-count-independent bound from the Parseval frame identity and product structure, or construct a valid rational finite-fragment counterexample. The theorem above shows that every fixed number of row directions is harmless; any obstruction to this mechanism must use an unboundedly rich directional frame as dimension grows.
