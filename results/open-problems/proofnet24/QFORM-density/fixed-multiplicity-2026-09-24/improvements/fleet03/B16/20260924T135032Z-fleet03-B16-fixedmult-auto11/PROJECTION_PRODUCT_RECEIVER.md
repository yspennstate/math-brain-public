SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-24T13:50:32Z.
attacking: the fixed-multiplicity threshold through a dependence-safe projection-product receiver, then testing it against the rigid s_8 terminal chamber.

# fleet03/B16 — inverse-radius projection-product receiver

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T135032Z-fleet03-B16-fixedmult-auto11`.
Status: **proved supporting theorem; does not prove the general s_8 theorem or the unrestricted three-eigenvalue conjecture.**
Execution/memory status: `WITHOUT_VERIFIED_BRAIN`.

Pinned fixed-multiplicity baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, source `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## 1. The theorem

### `QFORM-PROJECTIONPRODUCT-INVERSE-RADIUS-v1`

Let `X_I` and `X_J` be disjoint original-coordinate product banks, all coordinate densities bounded by one. Let `U` have two orthonormal columns supported on bank `I`, and put

`W=U^T X_I in R^2`.

Let `Z=Z(X_J) in R^2` be an arbitrary measurable random vector whose law has a density `g_Z` satisfying

`||g_Z||_infinity <= M < infinity`.

Let `alpha:R^{|J|}->R^2` and `R:R^{|J|}->R` be arbitrary measurable functions. Then

`Q = 2 (W+alpha(X_J)) dot Z(X_J) + R(X_J)`

has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi M).`                                      (1)

No independence is asserted between the two coordinates of `W`, between the two coordinates of `Z`, or between `Z` and `R`. The only independence used is the original product-bank independence `X_I independent X_J`.

If moreover

`Z=L X_J`

for a real rank-two matrix `L`, with row Gram matrix `G=LL^T`, then the actual two-dimensional bounded-density projection theorem gives

`||g_Z||_infinity <= 2/sqrt(det G)`

and therefore

`boxed: ||p_Q||_infinity <= 2 sqrt(2 pi) (det G)^(-1/4).`                        (2)

The constant in (2) is

`2 sqrt(2 pi)=5.0132565492620005...`.

The theorem establishes essential boundedness. Continuity is not claimed from this argument alone.

## 2. Proof

Condition on `X_J=y`. Put `z=Z(y)`, `a=alpha(y)`, and `r=R(y)`. Since `U` has orthonormal columns,

`z dot W = (Uz) dot X_I`

is a one-dimensional linear projection of the cap-one product law on bank `I`, with coefficient-vector Euclidean norm

`||Uz||_2=||z||_2`.

The one-dimensional product-projection theorem therefore gives

`||p_{z dot W}||_infinity <= sqrt(2)/||z||_2`                                  (3)

for `z!=0`. Multiplication by two divides the density cap by two, while `2 a dot z+r` is merely a conditional translation. Hence, for almost every `y` with `z!=0`,

`||p_{Q | X_J=y}||_infinity <= 1/(sqrt(2)||z||_2).`                            (4)

Because `Z` has an absolutely continuous two-dimensional law, `P{Z=0}=0`. Averaging the conditional measure domination in (4) yields

`p_Q(t) <= (1/sqrt(2)) E ||Z||_2^(-1)`                                         (5)

for almost every `t`.

It remains to bound the inverse-radius moment using only the joint density cap `M` and total mass one. For every `r>0`,

`E ||Z||_2^(-1)
 <= M int_{||z||<=r} ||z||^(-1) dz + r^(-1) P{||Z||>r}
 <= 2 pi M r + 1/r.`                                                           (6)

Choose `r=(2 pi M)^(-1/2)`. Then

`E ||Z||_2^(-1) <= 2 sqrt(2 pi M).`                                             (7)

Combining (5) and (7) proves (1).

For the linear-image specialization, write

`U_J = G^(-1/2)L`.

Then `U_J U_J^T=I_2`, so `U_J X_J` is an orthogonal two-dimensional projection of the original product measure. The dimension-two projection theorem gives density cap at most two. The change of variables `Z=G^(1/2)(U_J X_J)` multiplies the density cap by `(det G)^(-1/2)`, proving

`M <= 2/sqrt(det G)`.

Substitution into (1) gives (2). QED.

## 3. Why this is a legitimate nonlinear use of the projection theorem

A bounded two-dimensional projected density by itself does **not** bound an arbitrary indefinite quadratic pushforward. Here the special pure-cross structure is essential. After conditioning on `X_J`, the remaining dependence enters through one **linear** functional of the source-valid projected bank `W`; the one-dimensional product-projection theorem supplies the exact inverse-radius factor `||Z||^-1`. Two dimensions are exactly enough to make that singularity integrable against a bounded joint density:

`int_{||z||<=r} ||z||^-1 dz = 2 pi r`.

Thus the proof keeps the original product provenance until after the nonlinear singular kernel has been exposed. It never replaces `W` or `Z` by independent rotated coordinates.

## 4. Strict-target control family

Let `W` and `Z` be orthonormal two-dimensional projections of two disjoint original-coordinate product banks and take

`Q_cross=2 W dot Z`.

The effective four-dimensional quadratic matrix is

`[[0,I_2],[I_2,0]]`,

whose spectrum is `{1,1,-1,-1}`. Equation (2) with `G=I_2` gives

`boxed: ||p_{Q_cross}||_infinity <= 2 sqrt(2 pi) < 5.014.`

This is a genuinely rotated/product-projection family with four unit-magnitude eigenvalues. It is a scoped theorem, not an `s_4` theorem for arbitrary matrices.

## 5. Application to the current s_8 terminal chamber — what closes and what does not

The current fleet03/B08 terminal theorem for an unpaid normalized `s_8(A)>=1` no-pivot state supplies:

- the unique failed interpolation ratio is `r=2`;
- `A=D+R+E` with `rank R<=6`, `rank R[L,L]<=2`;
- `s_2(D)>=77/80`, `s_3(D)<=519/1400`, and `s_6(R)>=1657/2800`;
- all three rank-two correction pieces are saturated;
- three disjoint physical two-banks `S,H,T` obey

`|det A[H,T]| |det A[S,H]|
 >= (857233/980000) |det A[S,T]|`;                                               (8)

- after every deletion of at most two physical coordinates, either the child window is paid by the diffuse-window theorem or a localized physical star survives.

The new receiver closes any such terminal packet **if** one can expose two disjoint product banks for which the surviving pure-cross coefficient matrix `L` has

`det(LL^T) >= delta >0`

uniformly: (2) then gives `2 sqrt(2 pi) delta^(-1/4)` even if the shift and the rest of the quadratic polynomial depend arbitrarily on the opposite bank.

However, (8) alone does not force such an absolute `delta`. The seed determinant `|det A[S,T]|` may be arbitrarily small, so the determinant-ratio certificate cannot be replaced by a lower bound for any one physical two-bank cross Gram determinant. Likewise, the three nested star norms need not be linearly independent. Therefore this run does **not** promote the current `s_8` terminal theorem to a density theorem.

This identifies the remaining projection-product obligation more sharply: a valid `9 -> 8` receiver must consume the **three-bank determinant ratio before local-minor inversion**, or turn simultaneous rank-two saturation into an absolute two-dimensional projected cross Gram without assuming independence after rotation.

## 6. Actual use of the designated fleet04/B16 result

The completed fleet04/B16 theorem `QFORM-PROJECTIONPRODUCT-DEFINITE-OR-PHASEALIGNED-EXIT-v1` states that if a two-dimensional orthogonal projection `Z` of a cap-one product bank enters, after conditioning on disjoint original coordinates, through a definite quadratic matrix `H`, then

`||p_Q||_infinity <= 2 pi / sqrt(|det H|).`                                     (9)

Apply it to the strict-target family

`Q_partner=-2R^2+4R Z_1+3Z_1^2+2Z_2^2`,                                        (10)

where `R` is one cap-one original coordinate and `Z` is an orthogonal two-dimensional projection of a disjoint product bank. Conditioning on `R` leaves the definite projected plane `H=diag(3,2)`, so (9) gives

`boxed: ||p_{Q_partner}||_infinity <= 2 pi/sqrt(6)
      =2.565099660323728... .`                                                   (11)

The effective three-dimensional matrix is

`[[-2,2,0],[2,3,0],[0,0,2]]`,

with eigenvalues

`(1-sqrt(41))/2, 2, (1+sqrt(41))/2`,

approximately `-2.701562, 2, 3.701562`. Hence all three have modulus at least one, so (11) is an actual target-level inequality and not a two-eigenvalue surrogate.

## 7. Status

- `QFORM-PROJECTIONPRODUCT-INVERSE-RADIUS-v1`: **PROVED**.
- Linear projected specialization (2): **PROVED**.
- Strict four-eigenvalue pure-cross family: **PROVED**, density height `<5.014`.
- Designated fleet04/B16 definite-plane theorem: **APPLIED** to the strict three-large-eigenvalue family (10), giving (11).
- General `s_8` fixed-multiplicity theorem: **OPEN**.
- General `s_9` candidate: separately audited in the sibling report for this run.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity for the fixed-multiplicity theorem: **OPEN/not claimed**.
