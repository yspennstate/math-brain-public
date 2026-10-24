SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-23T18:04:38Z.
attacking: remove the remaining projected one-volume heavy-row gate by promoting a heavy row to a literal second hub and spending the resulting exact-rank-two |t|^-1 envelope through the half-Riesz square peel.

# account02/B01 — one projected crossing direction needs no row-marginal hypothesis

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180438Z-auto11`  
Role: oscillatory replacement / complementary constructions  
Status: **PROVED SUPPORTING THEOREM; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Sources actually used

Control was resolved fresh from `yspennstate/math-research-brain/main`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no account02/B01 stop.

Required historical Fourier source, read at the owner-pinned commit:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

The exact completed facts used from that source are Lemma 4.1 and Lemma 4.2:

`H_{1/2}(Z) <= (2*pi)^(-1/2) integral |t|^(-1/2)|phi_Z(t)| dt`,

and after an original-coordinate scalar completion

`Q=a(X+h)^2+S`,  `||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(S)`.

The newer reviewed crossing theorem used in the proof is

- `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`
- `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

I use its `k=1, ell=1` grouped projected-crossing estimate and its exact-rank-two crossing estimate with arbitrary internal functions.

Newest designated partner result consumed:

- account03/B01, `yspennstate/math-open-problems@585b5a3ca7e887e5cd16f45ea49056d548361dfb`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`
- checks at `3e8c96175a9cb97e80365fc127ffd1c9b733588c`.

That theorem removes the row-marginal gate when the projected two-volume `Z2` is positive. Section 5 below applies it to an exact target family and finds `Z2=0`, so the partner theorem is genuinely unavailable there while the present theorem pays the same family uniformly.

## 2. Pointwise obstruction remains in force

For any prescribed `s>0` and small `eta>0`, the set

`E={x: dist(s x^2,2*pi*Z)<=eta}`

has infinite Lebesgue measure. A finite measurable subset of `E` of measure one is an admissible cap-one probability density and satisfies

`Re E exp(i s X^2) >= cos(eta)`.

Thus no positive law-uniform pointwise power decay for a scalar quadratic phase is used or recovered. The gain below comes from an averaged-frequency half-potential after preserving original-coordinate product structure.

## 3. Main theorem

Let `X_0`, `Y`, `(X_i)_{i in I}`, `(X_j)_{j in J}` be disjoint ORIGINAL coordinates of the product input. After completing `X_0`, suppose

`Q = a (X_0+h(Y,X_I,X_J))^2 + R(Y,X_I,X_J)`,                    (3.1)

where `a!=0`, and write the residual as

`R = F(Y)
     +2Y(<m_I,X_I>+<m_J,X_J>+beta)
     +X_{I union J}^T A_R X_{I union J}
     +affine terms`.                                                (3.2)

Here `F` may be arbitrary measurable; all same-bank quadratic terms and all affine terms are unrestricted. Assume

`m:=m_J !=0`.                                                       (3.3)

Let `P_m` be orthogonal projection in `R^J` onto `span(m)` and define

`C=A_R[I,J](I-P_m)`,  `F_C=||C||_F`.                               (3.4)

### Theorem 3.1 — `QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`

If `F_C>0`, then

`boxed: H_{1/2}(R) <= 8 (||m||_2 F_C)^(-1/4),`                     (3.5)

and therefore

`boxed: ||p_Q||_infinity <= 8 |a|^(-1/2)(||m||_2 F_C)^(-1/4).`     (3.6)

There is **no row-marginal hypothesis and no rank hypothesis on `C`**. The estimate allows arbitrary internal curvature in `I`, in `J`, and in the hub variable. It makes no continuity claim.

### Proof

Write the rows of `C` as `c_i` and normalize the one-volume weights

`alpha_i=||c_i||_2^2/F_C^2`,  `sum_i alpha_i=1`.                   (3.7)

#### Case A: every `alpha_i<=1/2`

Apply the reviewed grouped projected-crossing theorem with one original hub (`k=1`) and one projected crossing direction (`ell=1`). The hub projection is the literal original scalar `Y`, so its density cap is one. The hub-to-`J` singular product is `||m||`, and

`Z_1=e_1(CC^T)=F_C^2`.                                              (3.8)

The `ell=1` entropy factor cancels exactly. Hence

`|phi_R(t)| <= min(1, K_1 |t|^(-1)),`
`K_1=2*pi*(||m|| F_C)^(-1/2)`.                                     (3.9)

Now spend the REQUIRED fractional-potential result from the 20260922T211500Z Fourier report. Since

`int_R |t|^(-1/2) min(1,K/|t|) dt = 8 sqrt(K)`,                    (3.10)

Lemma 4.1 gives

`H_{1/2}(R)
 <=(2*pi)^(-1/2) * 8 sqrt(K_1)
 =8 (||m|| F_C)^(-1/4)`.                                           (3.11)

#### Case B: some `alpha_i>1/2`

Promote that **literal original coordinate** `X_i` to a second hub and condition all other original coordinates in `I\{i}`. No rotated random variable is declared independent.

Decompose the physical row

`a_i:=A_R[i,J]=lambda_i m+c_i`,  `c_i perpendicular m`.             (3.12)

Because `alpha_i>0`, `c_i!=0`. The two hub rows into the untouched original `J` bank form

`B_i=[m ; a_i]`.                                                     (3.13)

Its product of nonzero singular values is exactly

`S_i=sqrt(det(B_i B_i^T))=||m|| ||c_i||`.                          (3.14)

After conditioning `I\{i}`, every remaining term depending only on `(Y,X_i)` is an arbitrary hub function and every term depending only on `X_J` is an arbitrary `J`-function. Therefore the reviewed exact-rank-two crossing theorem applies exactly to the conditional form.

The two-dimensional hub is made of exactly two original coordinates, so its projection density is at most one. The two-dimensional orthogonal projection of the untouched product `J` bank has density at most `2`. Thus, uniformly in the conditioned coordinates,

`|phi_{R|cond}(t)|
 <= min(1, pi*sqrt(2)*S_i^(-1/2)|t|^(-1)).`                        (3.15)

Averaging over the conditioning preserves this envelope. Lemma 4.1 and (3.10) therefore give

`H_{1/2}(R)
 <= 8/sqrt(2*pi) * sqrt(pi*sqrt(2)) * S_i^(-1/4)
 =2^(11/4) S_i^(-1/4).`                                            (3.16)

But `alpha_i>1/2` means

`||c_i||>F_C/sqrt(2)`,                                              (3.17)

so

`H_{1/2}(R)
 <2^(11/4+1/8)(||m||F_C)^(-1/4)
 =2^(23/8)(||m||F_C)^(-1/4)
 <8 (||m||F_C)^(-1/4).`                                            (3.18)

This closes the heavy-row case.

Finally apply REQUIRED Lemma 4.2, the square peel,

`||p_Q||_infinity <= |a|^(-1/2)H_{1/2}(R)`,                       (3.19)

to obtain (3.6). QED.

### Interpretation

The previous B01 result left the rank-one projected crossing with a possible one-volume row marginal above `1/2`. That obstruction is now removed. More strongly, (3.5) pays **every nonzero projected crossing**, regardless of its rank or row concentration. The scalar-completion endpoint is therefore not `rank(C)=1`; it is the exact/quantitative collapse `C=0` or `||m||F_C` too small.

The estimate has the correct global scaling: under `A -> lambda A`, `a,m,C` each scale by `lambda`, so the right side of (3.6) scales by `|lambda|^(-1)`.

## 4. Strict-N3 target family with a maximally heavy projected row

Fix `0<epsilon<=1/2`, `0<nu<=1`, and an even `m`. Let `e,q in R^m` be orthonormal flat vectors:

`e_j=1/sqrt(m)`, `q_j in {+1/sqrt(m),-1/sqrt(m)}`, `sum_j q_j=0`.    (4.1)

Use original coordinates `(x,y,u,Z_1,...,Z_m)` and define the symmetric coefficient matrix by

`A_xx=epsilon`,
`A_yy=epsilon*nu`,
`A_yJ=epsilon^(-1)e^T`,
`A_uJ=epsilon^(-1)q^T`,                                             (4.2)

with all other indicated entries zero.

### Target spectrum

On the active orthonormal basis `(x,y,u,e,q)`, the matrix is

`diag(epsilon) direct_sum [[epsilon*nu,epsilon^(-1)],[epsilon^(-1),0]] direct_sum [[0,epsilon^(-1)],[epsilon^(-1),0]].`  (4.3)

Hence its nonzero eigenvalues are

`epsilon`,
`lambda_+=[epsilon*nu+sqrt(epsilon^2 nu^2+4 epsilon^(-2))]/2`,
`lambda_-=[epsilon*nu-sqrt(epsilon^2 nu^2+4 epsilon^(-2))]/2`,
`+epsilon^(-1)`, `-epsilon^(-1)`.                                  (4.4)

For `epsilon<=1/2`, both `|lambda_+|` and `|lambda_-|` exceed one, and `epsilon^(-1)>=2`; therefore there are at least four eigenvalues of modulus at least one.

### Strict N3

Every physical diagonal is at most `epsilon`. Every nonzero physical `2x2` principal determinant has magnitude at most

`epsilon^(-2)/m`.                                                    (4.5)

Thus for every fixed no-pivot threshold `tau in (0,1]`, choosing

`epsilon<min(tau,1/2)` and then `m>1/(tau epsilon^2)`               (4.6)

places the family in strict N3.

The physical pair `{x,y}` is genuinely nonzero and can be arbitrarily near singular:

`|det A_{xy,xy}|=epsilon^2 nu`,
`sigma_min(A_{xy,xy})=epsilon*min(1,nu)`.                           (4.7)

### New theorem on the family

Complete the original coordinate `x`. Here `a=epsilon` and `h=0`. In the residual take hub `Y=y`, `I={u}`, and `J={Z_1,...,Z_m}`. Then

`m_J=epsilon^(-1)e`,
`C=epsilon^(-1)q^T`,
`F_C=epsilon^(-1)`.                                                  (4.8)

The unique one-volume row marginal is exactly `1`, so the preceding spread-row theorem fails maximally. Nevertheless Theorem 3.1 gives

`||p_Q||_infinity <= 8`.                                            (4.9)

Because this family lies in the heavy-row case with `||c_u||=F_C`, the sharper branch (3.16) actually gives

`boxed: ||p_Q||_infinity <= 2^(11/4)=6.7271713220...`               (4.10)

uniformly in `epsilon`, `nu`, `m`, and all admissible cap-one product laws.

This is a full-target-valid strict-N3 family with an arbitrarily small nonzero physical-pair singular value and a maximally concentrated projected crossing.

## 5. Newest account03/B01 theorem applied at a concrete obstruction

For the same family, the projected crossing `C=epsilon^(-1)q^T` has rank exactly one. Consequently

`Z_2=e_2(CC^T)=0`.                                                   (5.1)

The newest designated-partner theorem `QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1` requires `Z2>0`, so its bound

`||p_R||_infinity <= 9.400 (||m||^2 Z2)^(-1/6)`                    (5.2)

is unavailable here. This is not a weakness in that theorem: the family lies exactly on its rank-one boundary. The present theorem spends `Z1=F_C^2=epsilon^(-2)` through the half-Riesz square peel and gives (4.10).

Thus the two results fit cleanly: account03/B01 removes concentration from positive projected two-volume, while this run removes concentration from the remaining projected one-volume endpoint.

## 6. What remains unpaid

The first unpaid implication is now

`QFORM-NEARNULL-PROJECTED-CROSS-ZERO-ROUTING-v1`.

After a scalar completion with a substantial random slope `m_J`, **every nonzero projected crossing**

`C=A_R[I,J](I-P_m)`

is paid by Theorem 3.1 before any reciprocal tiny physical-pair singular value is used. A surviving near-null configuration must therefore force `C=0` (or quantitatively tiny `||m|| ||C||_F`) on every useful product-preserving orientation. Algebraically, `C=0` means every relevant cross row lies in the one-dimensional span of the slope vector `m_J`: the crossing carries no transverse direction beyond the hub slope.

The next structural step should route that aligned state to one of the already-paid exact-singular random-slope, rank-one bilinear-plus-square, two-/three-hub, grouped-square, or physical-pair receivers. One must not infer independence after rotating the aligned bank, and one must not treat a small matrix residual as a small random quadratic perturbation without moments.

Full unrestricted QFORM remains OPEN. No counterexample was found. No continuity claim is made for Theorem 3.1.
