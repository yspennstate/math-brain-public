# F0012: signed-shear all-n extension

Runtime disclosure for the creating run: **GPT-5.6 Sol; reasoning level UNVERIFIED; not GPT-6 maximum.**

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.5. For the iid nonsymmetric Rademacher matrix `M_n`, let

`E_n = {all eigenvalues of M_n are Gaussian integers}`.

The preceding R7-07 run already refuted the source conjecture on the even subsequence using one fixed block shear. This note strengthens that construction to **every n** and counts a larger signed-shear union exactly.

## Theorem

For every integer `n >= 1`,

`P(E_n) >= 3^{floor(n/2)} 2^{-floor(n^2/2)}.`

Equivalently,

`-log_2 P(E_n) <= floor(n^2/2) - floor(n/2) log_2 3`.

In particular,

`limsup_{n->infinity} (-log_2 P(E_n))/n^2 <= 1/2`.

Thus the source asymptotic `P(E_n)=2^{-(1+o(1))n^2}` is contradicted along the full sequence, not merely along even `n`.

## 1. Even dimension: a signed diagonal shear and its Gaussian-unit endpoint

Let `n=2m`. Write a sign matrix in `m x m` blocks

`M = [[A,B],[C,D]]`.

For an `m x m` diagonal matrix `R`, set

`S_R = [[I,0],[R,I]]`,   `S_R^{-1} = [[I,0],[-R,I]]`.

A direct multiplication gives

`S_R^{-1} M S_R = [[A+BR, B], [C+DR-RA-RBR, D-RB]].`       (1)

We first take

`R = diag(epsilon_1,...,epsilon_{m-1},tau)`,

where each `epsilon_j` is in `{+1,-1}` and `tau` is a Gaussian unit in `{+1,-1,+i,-i}`. Impose

- `X:=A+BR` upper triangular;
- `Y:=C+DR-RA-RBR=0`;
- `Z:=D-RB` lower triangular.

Then (1) is block upper triangular and its two diagonal blocks are triangular. Hence its eigenvalues are the diagonal entries of `X` and `Z`.

For every index except the terminal diagonal coordinate, the constraints separate entrywise.

### Below the diagonal

For `i>j`, necessarily `j<m`, so `r_j=epsilon_j`. The condition `X_ij=0` is

`a_ij + b_ij epsilon_j = 0`.

Substituting this into `Y_ij=0` cancels the terms involving `r_i` and leaves

`c_ij + d_ij epsilon_j = 0`.

Thus `b_ij,d_ij` are free signs and `a_ij,c_ij` are forced: exactly `4` choices.

### Above the diagonal

For `i<j`, necessarily `i<m`, so `r_i=epsilon_i`. The condition `Z_ij=0` is

`d_ij - epsilon_i b_ij = 0`.

Substituting into `Y_ij=0` cancels the terms involving `r_j` and leaves

`c_ij - epsilon_i a_ij = 0`.

Thus `a_ij,b_ij` are free signs and `c_ij,d_ij` are forced: exactly `4` choices.

### Nonterminal diagonal coordinates

For `i=j<m`, with `epsilon=epsilon_i`, the single equation is

`c + epsilon(d-a) - b = 0`.

For each fixed `epsilon` there are exactly `6` sign quadruples `(a,b,c,d)`.

### Terminal diagonal coordinate and all possible Gaussian-integer parameters

At `i=j=m`, the equation is

`c + tau(d-a) - b tau^2 = 0`.                            (2)

For the two terminal diagonal eigenvalues `a+b tau` and `d-b tau` to be Gaussian integers, `tau` must be a Gaussian integer. If a Gaussian integer `tau` satisfies (2), then after division by `-b` it is a root of a monic quadratic over `Z` whose constant term is the unit `-c/b in {+1,-1}`. The other root is also a Gaussian integer, and the product of the two roots is a unit. Hence `tau` itself is a unit of `Z[i]`:

`tau in {+1,-1,+i,-i}`.

So the four parameters used above exhaust this local Gaussian-integer endpoint mechanism.

For `tau=+1` equation (2) is `c+d=a+b`, giving `6` sign quadruples. For `tau=-1` it is `a+c=b+d`, again giving `6`. Their intersection is exactly `a=d, c=b`, hence has `4` elements, so the real-unit union has size `8`.

For `tau=+i` or `-i`, equation (2) is equivalent to

`d=a, c=-b`.

Both imaginary units give the same `4` sign quadruples. This set is disjoint from the real-unit union. Therefore the terminal union has exactly

`8+4=12`

sign quadruples.

### Exact union count for even n

For every `j<m`, any matrix satisfying the construction recovers `epsilon_j` uniquely from a below-diagonal entry, for example

`epsilon_j = -a_{j+1,j}/b_{j+1,j}`.

Thus distinct prefixes `(epsilon_1,...,epsilon_{m-1})` give disjoint matrix families. The terminal parameter has already been union-counted by the exact local count `12`. Therefore the number of distinct `2m x 2m` sign matrices in the construction is

`N_{2m} = 2^{m-1} 4^{m(m-1)} 6^{m-1} 12`

`        = 2^{2m^2} 3^m.`

Every matrix in this union has Gaussian-integer spectrum: all nonterminal diagonal eigenvalues are in `{-2,0,2}`, and the terminal pair is either integral or of the form `a +/- i b` with `a,b in {+1,-1}`.

Since there are `2^{4m^2}` Rademacher matrices of size `2m`,

`P(E_{2m}) >= 3^m 2^{-2m^2}.`                            (3)

This is exactly the theorem's bound for even `n`.

## 2. Odd dimension: rectangular shear

Let `n=2m+1`. Split the coordinates into blocks of sizes `m` and `m+1`:

`M = [[A,B],[C,D]]`,

where `A` is `m x m`, `B` is `m x (m+1)`, `C` is `(m+1) x m`, and `D` is `(m+1) x (m+1)`.

For `epsilon=(epsilon_1,...,epsilon_m) in {+1,-1}^m`, let `R_epsilon` be the `(m+1) x m` matrix whose top `m x m` block is `diag(epsilon)` and whose last row is zero. With

`S = [[I_m,0],[R_epsilon,I_{m+1}]]`,

the same multiplication as in (1) gives

`S^{-1} M S = [[A+B R_epsilon, B], [C+D R_epsilon-R_epsilon A-R_epsilon B R_epsilon, D-R_epsilon B]].`   (4)

Again impose that the upper-left block is upper triangular, the lower-left block is zero, and the lower-right block is lower triangular.

On the `m x m` core, the same entrywise calculation gives

`4^{m(m-1)}6^m`

choices.

There are three additional groups of entries:

1. For the extra column `j=m+1` and `i<=m`, lower-triangularity gives
   `d_{i,m+1}=epsilon_i b_{i,m+1}`, hence `2^m` choices.
2. For the extra bottom row `i=m+1` and `j<=m`, the zero lower-left condition gives
   `c_{m+1,j}+d_{m+1,j}epsilon_j=0`, hence `2^m` choices.
3. The bottom-right entry `d_{m+1,m+1}` is an arbitrary sign, hence `2` choices.

Thus for fixed `epsilon` there are

`4^{m(m-1)}6^m 2^{2m+1}`

matrices.

Moreover, the extra column recovers every sign parameter uniquely:

`epsilon_i = d_{i,m+1}/b_{i,m+1}`.

Hence the `2^m` parameter families are pairwise disjoint. The total number of distinct matrices is therefore

`N_{2m+1} = 2^m 4^{m(m-1)}6^m2^{2m+1}`

`          = 2^{2m^2+2m+1}3^m.`

All diagonal entries of the two triangular blocks in (4) are ordinary integers (`0,+/-2` on the paired coordinates and `+/-1` on the extra coordinate), so all eigenvalues are Gaussian integers. Since the ambient sign cube has size `2^{(2m+1)^2}`,

`P(E_{2m+1}) >= 3^m 2^{-(2m^2+2m)}`.                   (5)

Because `floor((2m+1)^2/2)=2m^2+2m`, (5) is exactly the theorem's odd bound.

## 3. Unified consequence

Equations (3) and (5) give, for every `n>=1`,

`P(E_n) >= 3^{floor(n/2)} 2^{-floor(n^2/2)}.`

Hence

`limsup_n [-log_2 P(E_n)]/n^2 <= 1/2`.

This strengthens the preceding even-subsequence refutation to a full-sequence lower bound of order

`2^{-(1/2+o(1))n^2}`.

It does **not** prove that `1/2` is the corrected sharp exponent; an upper bound of matching order remains a separate problem and is not claimed.

## 4. Exact finite check

A companion exact checker exhausts all sign matrices for `n=2,3,4`, tests membership in the signed/complex-unit shear union by direct matrix arithmetic, and compares the union cardinality with the closed formulas above. It also checks the terminal local union and intersection counts. The archived output ends with

`SIGNED_SHEAR_ALL_SMALL_CASES_PASS`.

This is a self-check, not either of the two independent audits required by the owner closure protocol.
