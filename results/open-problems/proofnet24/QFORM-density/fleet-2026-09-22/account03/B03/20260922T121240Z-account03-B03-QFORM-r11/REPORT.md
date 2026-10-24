# account03/B03 — decoupled time integral via a square coordinate packet

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.
Run: `20260922T121240Z-account03-B03-QFORM-r11`.
Status: `ESSENTIAL_STEP_APPLIED`; full target remains OPEN.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and current corrections

The target is the arbitrary-dimensional statement for independent original coordinates with densities bounded by one and a symmetric matrix having at least three eigenvalues of modulus at least one. No moment, support, log-concavity or eigenbasis-independence assumption is used below. The law-uniform pointwise quadratic oscillatory-decay lemma is not used.

Fresh corrections consumed before publication include `QFORM-CROSSMINOR-ALONE-FALSE`, which concerns a **2x2** cross block and the sharp rank-two logarithmic obstruction, and `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, whose source-bound interactive report proves a general rank-r cross-block Fourier theorem. The latter is applied below as the compatible current mathematical input: its proof identifies the correct cross-block Fourier mechanism and the threshold r>2. The present argument sharpens its constant in the square original-coordinate packet case by avoiding the projection-density factor.

The assigned partner is `account04/B03`. No completed current-QFORM B03 handoff was present in the fresh account04 handoff directory, so no partner PASS or theorem is fabricated.

## 2. Main theorem

### Theorem `QFORM-SQUARE-CROSSPACKET-PLANCHEREL-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `A` be real symmetric. Suppose there are disjoint original-coordinate sets `I,J` with

- `|I|=|J|=m>=3`, and
- the square cross block `C=A[I,J]` is invertible.

Put `delta=|det C|`. Then, for `Q=X^T A X` and its characteristic function `phi_Q`, for every nonzero real `t`,

`|phi_Q(t)| <= pi^(m/2) delta^(-1/2) |t|^(-m/2)`.                 (2.1)

Consequently

`||phi_Q||_1 <= 2*pi*m/(m-2) * delta^(-1/m)`,                   (2.2)

`Q` has a continuous density vanishing at infinity, and

`||p_Q||_infinity <= m/(m-2) * delta^(-1/m)`.                  (2.3)

In particular, an invertible disjoint `3x3` coordinate cross block gives

`||p_Q||_infinity <= 3 |det A[I,J]|^(-1/3)`.                  (2.4)

No condition at all is imposed on `A[I,I]`, `A[J,J]`, or on the coordinates outside `I union J`.

### Proof

Condition on all coordinates outside `I union J`; call the conditioned value `r`. Write `y=X_I` and `z=X_J`. Under this conditioning the quadratic polynomial has the exact form

`Q(y,z;r)=q_I(y;r)+q_J(z;r)+2 y^T C z+c(r)`,

where `q_I` and `q_J` are arbitrary real quadratic-affine polynomials on their respective blocks. The original-coordinate product law is preserved: `y` and `z` are independent and each has product density.

For fixed `r,t`, define the full `m`-dimensional Fourier transform

`H_{r,t}(s) = integral exp(i t q_J(z;r)) exp(i s.z) prod_{j in J} f_j(z_j) dz`.

The quadratic phase has modulus one. Therefore Plancherel, with `hat h(s)=integral exp(i s.z)h(z)dz`, gives

`integral |H_{r,t}(s)|^2 ds`
` = (2*pi)^m integral prod_{j in J} f_j(z_j)^2 dz`
` <= (2*pi)^m`,                                                (2.5)

because every `f_j<=1` and integrates to one.

The conditional characteristic function is

`phi_r(t)=exp(i t c(r)) integral exp(i t q_I(y;r)) H_{r,t}(2t C^T y) prod_{i in I} f_i(y_i) dy`.

Apply Cauchy-Schwarz with respect to the probability measure `prod_{i in I}f_i(y_i)dy`. This is exactly the one-copy/independent-copy step, but it does **not** split a coordinate pair into falsely independent sum and difference variables:

`|phi_r(t)|^2`
` <= integral |H_{r,t}(2t C^T y)|^2 prod_{i in I}f_i(y_i)dy`
` <= integral |H_{r,t}(2t C^T y)|^2 dy`,                       (2.6)

where the second line uses the original-coordinate density cap `prod f_i<=1`.

Now make the invertible change of variables `s=2t C^T y`. Equations (2.5)-(2.6) give

`|phi_r(t)|^2`
` <= (2|t|)^(-m) delta^(-1) (2*pi)^m`
` = pi^m delta^(-1)|t|^(-m)`.                                 (2.7)

Taking square roots proves (2.1), uniformly in the conditioned coordinates `r`. Hence the same estimate holds after averaging over `r`. It also holds with arbitrary extra linear and constant terms, since those were already absorbed into `q_I,q_J,c`.

Let `D=pi^(m/2)delta^(-1/2)`. Together with `|phi_Q(t)|<=1`, (2.1) gives

`|phi_Q(t)| <= min(1,D|t|^(-m/2))`.

The two bounds meet at

`t_0=D^(2/m)=pi delta^(-1/m)`.

Since `m>2`, direct integration yields

`||phi_Q||_1`
` <= 2[t_0 + D integral_{t_0}^infinity t^(-m/2)dt]`
` = 2*pi*m/(m-2) delta^(-1/m)`,

which is (2.2). Fourier inversion then supplies a continuous density and (2.3). QED.

## 3. Why this is the assigned decoupled-time mechanism

The Cauchy step in (2.6) is the exact independent-copy operation at the block level. If expanded, it contains `q_J(Z;r)-q_J(Z';r)` and the original dependent sum/difference geometry of each coordinate pair. The proof never declares `Z+Z'` independent of `Z-Z'`. Instead it keeps the complete complex amplitude in `H_{r,t}` and spends only its exact Plancherel `L^2` budget. Thus the refuted pointwise oscillatory lemma is unnecessary.

The mechanism also explains the threshold. For `m=2`, (2.1) gives only `|phi(t)|=O(|t|^-1)`, whose time integral is logarithmically divergent; this is consistent with the live rank-two cross-minor correction and with the opposite-sign/product logarithmic singularity. At `m=3`, the exponent becomes `3/2`, exactly integrable, and Fourier inversion recovers **linear** small-ball scaling:

`P{Q in L} <= 3 delta^(-1/3)|L|`

for every interval `L` in the 3x3 case.

## 4. Compatible current result applied and sharpened

The fresh interactive result `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1` proves, for a rank-r cross block of arbitrary rectangular original-coordinate blocks, the density estimate

`||p_Q||_infinity <= [2r/(r-2)] Delta^(-1/r)`

using an r-dimensional projection-density bound. In the present square coordinate packet, `Delta=|det C|`. Because the packet already consists of exactly `m` original independent coordinates on each side, no rotated marginal is needed: `prod_{i in I}f_i<=1` can be inserted directly in (2.6). This removes the projection `2^(m/2)` loss and improves the coefficient from `2m/(m-2)` to `m/(m-2)`.

For `m=3`, the current source-valid general cross-block coefficient `6` becomes `3` in the square coordinate packet. This does not conflict with the 2x2 correction: `m=2` is exactly the nonintegrable endpoint of the present proof.

## 5. Explicit target-valid control

For six original coordinates take

`A = [[0,I_3],[I_3,0]]`.

Then `spec(A)={1,1,1,-1,-1,-1}`, `det A[I,J]=1` for the natural three-by-three split, and

`Q=2(X_1X_4+X_2X_5+X_3X_6)`.

For **every** permitted set of six independent input laws, (2.4) gives a continuous density with

`||p_Q||_infinity<=3`.

This is a genuine indefinite target instance and uses neither a diagonal form nor eigenbasis independence.

## 6. First unpaid all-target implication

The spectral hypothesis alone does not provide a single disjoint 3x3 coordinate cross determinant bounded below by a universal constant: diagonal matrices have no such cross block, while diffuse frames can spread exterior-minor mass over many small packets. The diagonal branch is already solved separately, and current Walsh/Pluecker corrections rule out paying a reciprocal local-minor constant before aggregation.

Therefore the next target-level implication is an **aggregation/dichotomy theorem**: from three singular/eigenvalues of modulus at least one, aggregate original-coordinate packets before the reciprocal determinant cost is paid, or route concentrated matrices into one of the already proved local smoothers. Selecting the numerically largest cross minor with a dimension-dependent lower bound is not enough.

The present theorem closes the full square-crosspacket branch and gives the exact time-integral budget needed by any such aggregation.

## 7. Integrity status

- Full conjecture: OPEN / NOT PROVED / NOT DISPROVED.
- Continuity: proved for the theorem's square-crosspacket branch because `phi_Q in L^1`.
- Input independence is used only in original coordinate blocks.
- No pointwise stationary-phase estimate, rotated-coordinate independence, numerical histogram, paid API/model, or native-brain claim is used.
- Execution context: `WITHOUT_VERIFIED_BRAIN`.
