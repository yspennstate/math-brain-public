# account01/B18 — one-sided curvature + all-rank cross-volume fusion

Run: `20260924T085723Z-account01-B18-qform-auto11-r51`  
Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Continuity: tracked separately; proved for the explicit target family, not claimed for the general ambient theorem.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Primary-source scope and non-novelty

The base all-rank bilinear-plus-affine mechanism is already present in Banks--Garza Vargas--Kulkarni--Srivastava, arXiv:2005.08930, Section 2 (Theorem 2.1 / Corollary 2.4 in the source version used by the fleet). I make **no novelty claim** for that qualitative geometric-mean singular-value packet.

The explicit cap-one constants below use two primary results at their literal hypotheses:

- Rudelson--Vershynin, arXiv:1402.4492, Theorem 1.2: a normalized linear combination of independent scalar variables with density caps at most one has density at most `sqrt(2)`;
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1: every `j`-dimensional orthogonal marginal of a genuine cap-one product density has joint density at most `2^(j/2)`.

No moment, iid, support, centering, symmetry, smoothness or log-concavity condition is inserted. LPP is used only as a joint marginal-density cap; no independence after projection is asserted.

The useful transfer this run is that the whole geometric-mean cross payment survives **arbitrary curvature on the opposite original-coordinate bank and a private original scalar whose coefficient may depend arbitrarily on that curved bank**. This is fused with a completed account02/B18 private-square receiver.

## 2. One-sided-curvature all-rank cross/private-square fusion

Let `X in R^m`, `Y in R^n`, and a scalar `W` be three pairwise-disjoint banks of ORIGINAL coordinates. All scalar coordinates are mutually independent and have densities bounded by one. Let `B` be an `m x n` real matrix of rank `r>=2`, with singular values

`sigma_1>=...>=sigma_r>0`.

Let `alpha in R^m`, let `G,rho:R^n->R` be arbitrary measurable functions, and let `a!=0`, `c in R`. Put

`T = 2 X^T B Y + alpha^T X + G(Y) + a W^2 + rho(Y)W + c`.          (2.1)

With `v_j=pi^(j/2)/Gamma(j/2+1)`, define

`C_j(B)=[j/(j-1)] v_j^(1/j)/(prod_{i=1}^j sigma_i)^(1/j)`.          (2.2)

Then `T` has a density and

`boxed: ||p_T||_infinity <= min{ min_{2<=j<=r} C_j(B),
                                 4sqrt(2)/sqrt(|a| sigma_1) }`.      (2.3)

The second branch is the literal-original-scalar specialization of the completed designated-partner theorem account02/B18 `QFORM-CONDITIONAL-CROSS-PRIVATEBANK-WEAKL2-v1`, scientific commit `fedbabc70c2245476d15532f38c5c2555a0d6c31`.

### All-rank cross branch

Condition on the genuine original-coordinate variables `(Y,W)=(y,w)`. The remaining random dependence on `X` is the linear form

`(2By+alpha)^T X`

plus a deterministic translation. Rudelson--Vershynin therefore gives conditional density cap

`sqrt(2)/||2By+alpha||_2`.                                         (2.4)

Fix `2<=j<=r`, write an SVD `B=U Sigma V^T`, and keep the top `j` singular directions. Then

`||2By+alpha|| >= ||2 Sigma_j V_j^T y + U_j^T alpha||`.             (2.5)

The vector `V_j^T Y` is a `j`-dimensional orthogonal marginal of the original product bank, so LPP gives joint density cap `<=2^(j/2)`. (If `j=n`, an orthogonal full-dimensional change preserves the original joint cap `<=1`, which is even stronger.) Therefore

`Z_j=2 Sigma_j V_j^T Y+U_j^T alpha`

has density cap

`L_j<=2^(-j/2)/(prod_{i=1}^j sigma_i)`.                             (2.6)

For every probability density `f` on `R^j`, `0<=f<=L`, the radial bathtub principle gives

`int ||z||^(-1) f(z) dz <= [j/(j-1)](L v_j)^(1/j)`.                 (2.7)

Indeed the extremizer under the mass and cap constraints is `L 1_{||z||<=R}`, with `L v_j R^j=1`. Direct radial integration proves (2.7). Averaging (2.4), using (2.5)--(2.7), cancels the `sqrt(2)` from Rudelson--Vershynin against the `2^(-1/2)` produced by (2.6), yielding exactly

`||p_T||_infinity<=C_j(B)`.                                        (2.8)

The terms `G(Y)`, `rho(Y)W`, and `aW^2` are only translations after conditioning on `(Y,W)`, so arbitrary opposite-bank curvature costs nothing in this branch.

### Designated-partner branch

Apply account02/B18 commit `fedbabc70c2245476d15532f38c5c2555a0d6c31` with its bilinear matrix `M=2B` and private scalar equal to the literal original coordinate `W`. That theorem explicitly permits arbitrary `G(Y)` and arbitrary `Y`-dependent coefficient multiplying `W`. Its literal-scalar sharpening gives

`||p_T||_infinity <= 8/sqrt(|a| ||M||_op)
                   =4sqrt(2)/sqrt(|a| sigma_1)`.                    (2.9)

Taking the minimum proves (2.3). No continuity claim is imported in this fully `rho(Y)`-dependent scope.

## 3. Ambient original-coordinate corollary

Suppose an ORIGINAL-coordinate packet `R=I disjoint_union J disjoint_union {w}` has symmetric block

`A_RR=[[0,B,0],[B^T,C,h],[0,h^T,a]]`,                               (3.1)

where `rank B=r>=2`, `a!=0`, while `C` and `h` are completely arbitrary. All coefficients and couplings involving coordinates outside `R` may also be arbitrary.

Condition only on the outside ORIGINAL coordinates. Outside couplings create affine terms; `Y^T C Y` joins `G(Y)`; and the `J-w` plus conditioned outside-`w` couplings join `rho(Y)W`. Thus (2.3) applies uniformly and averaging gives

`boxed: ||p_{X^TAX}||_infinity
 <= min{ min_{2<=j<=r} C_j(B),4sqrt(2)/sqrt(|a|sigma_1(B)) }`.       (3.2)

This strictly relaxes the previous B18 geometric-mean ambient packet: only the `I-I` block and the `I-w` coupling are required to vanish; the entire `J-J` curvature and `J-w` coupling are retained.

## 4. Exact target-valid interpolation with arbitrary curved bank

Let `r>=2`, `t>0`, let `C` be an arbitrary real symmetric `r x r` matrix and `d in R^r` arbitrary. Take mutually independent cap-one scalar sources

`U_+,U_-,X_1,...,X_r,Y_1,...,Y_r,W`.

Set

`b=t/sqrt(r)`, `a=sqrt(r)/t=1/b`,

and

`Q_{r,t,C,d}=U_+^2-U_-^2
 +2b sum_{i=1}^r X_iY_i+Y^TCY+aW^2+2(d^TY)W`.                       (4.1)

### Target validity for every `C,d,t`

If `b<=1`, then `a>=1` and the physical principal block on `(U_+,U_-,W)` is `diag(1,-1,a)`: it has two eigenvalues `>=1` and one `<=-1`, hence so does the full matrix by Cauchy interlacing.

If `b>=1`, the physical principal block on `(U_+,U_-,X_1,Y_1)` is

`diag(1,-1) direct_sum [[0,b],[b,C_11]]`.                            (4.2)

The last block has determinant `-b^2`; its eigenvalues have opposite signs and absolute-value product `b^2>=1`, so at least one has modulus at least one. Together with `+1,-1`, the principal block has at least three eigenvalues of modulus at least one, with either signed count `(2+,1-)` or `(1+,2-)`. Interlacing transfers the corresponding signed count to the full matrix.

Thus (4.1) belongs to the owner's exact target class for **every** `r>=2`, `t>0`, and arbitrary `C,d`.

### Universal bound

Here `B=bI_r`. The `j=r` cross branch gives

`||p_Q||_infinity<=C_r/t`,

`C_r=[r/(r-1)]v_r^(1/r)sqrt(r)`.                                   (4.3)

The designated-partner branch has `|a|sigma_1(B)=ab=1`, so

`||p_Q||_infinity<=4sqrt(2)=5.656854249492381...`.                  (4.4)

Hence

`boxed: ||p_{Q_{r,t,C,d}}||_infinity
 <=min{C_r/t,4sqrt(2)}<=4sqrt(2)`.                                  (4.5)

This is uniform in dimension, `t`, the completely arbitrary same-bank curvature `C`, the coupling `d`, and every admissible rough product law. The individual crossings `b=t/sqrt(r)` may vanish with dimension; they are aggregated before inversion.

Exact values: `C_2=5.013256549262001`, `C_3=4.188077948623138`, `C_4=3.974533571810907`. The elementary Gamma lower bound gives `C_r<=2sqrt(2pi e)<8.266` for all `r>=2`.

## 5. Newest account02/B18 theorem applied too

The newest completed account02/B18 report consumed this run is scientific commit `fd7c768025320fbb5e54e13a1acd00d329e8f8dd`, theorem `QFORM-HS-MOVING-DIFFUSE-SQUARE-v1`. For disjoint original banks it treats

`X^T M Y+a(beta^TZ+H(Y))^2+c`

and proves

`||p||_infinity <= K_beta/sqrt(|a|)
 *min{K_HP/sqrt(||M||_HS),8/sqrt(||M||_op)}`,                       (5.1)

with a `C_0` density. Its Hilbert--Schmidt branch is source-pinned to Hu--Paouris tensor small-ball estimates and the partner keeps `K_HP` symbolic rather than inventing a numerical value.

Apply it to the target-valid completed-square subfamily

`Q^sq_{r,t,h}=U_+^2-U_-^2+2b sum_iX_iY_i+a(W+h^TY)^2`,              (5.2)

with arbitrary `h`, the same `a=1/b`, and literal original scalar `W`. Section 4 applies with `C=a h h^T`, `d=a h`. Here

`M=2bI_r`, `||M||_HS=2t`, `||M||_op=2t/sqrt(r)`, `K_beta<=1`.

Therefore the **actual newest-partner inequality** is

`||p_{Q^sq_{r,t,h}}||_infinity
 <=min{K_HP/(sqrt(2)r^(1/4)),4sqrt(2)}`.                             (5.3)

Combining with the cross branch gives

`boxed: ||p_{Q^sq_{r,t,h}}||_infinity
 <=min{C_r/t,K_HP/(sqrt(2)r^(1/4)),4sqrt(2)}`.                       (5.4)

No extension of the newest partner's HS theorem to arbitrary additive `Y^TCY` is asserted.

## 6. Continuity, separately

The general ambient theorem (3.2) asserts essential boundedness only.

For the explicit family (4.1), let `R` be the part excluding `U_+^2-U_-^2`. By (2.3), `R` has a probability density `f_R in L^1 cap L^infinity`. Let `S=U_+^2-U_-^2`. Because each input is absolutely continuous, each square has an `L^1` density, hence `S` has some probability density `g_S in L^1`; **no boundedness or continuity of `g_S` is claimed** (indeed an opposite-sign rank-two square can have a logarithmic singularity).

Independence gives `p_Q=f_R*g_S`. This convolution is nevertheless `C_0` because `f_R in L^1 cap L^infinity` and `g_S in L^1`: translation continuity of `g_S` in `L^1` gives

`sup_x |p_Q(x+h)-p_Q(x)| <= ||f_R||_infinity ||tau_h g_S-g_S||_1 ->0`,

and approximating `g_S` in `L^1` by continuous compactly supported functions shows vanishing at infinity, with uniform error at most `||f_R||_infinity` times the `L^1` approximation error. Young's inequality also gives

`||p_Q||_infinity<=||f_R||_infinity||g_S||_1=||f_R||_infinity`.

Thus the explicit family (4.1) has a continuous `C_0` representative with the same universal bound `4sqrt(2)`. This continuity argument is intentionally not promoted to the unrestricted ambient theorem.

## 7. Remaining full-target debt

The unrestricted QFORM theorem remains OPEN. The bare spectral condition `s_3(A)>=1` is not known to force a product-preserving packet of the form (3.1) with either

`(prod_{i=1}^j sigma_i(B))^(1/j)>=c` for some `j>=2`,

or

`|a|sigma_1(B)>=c`.

Live corrections already refute several naive single-minor and single-Schur extraction statements; small nonzero same-side curvature/crossing tails cannot be deleted under arbitrary rough unbounded-support inputs.

The sharpened compiler target is: from `s_3(A)>=1`, either extract a source-preserving one-zero-self-side packet with payable geometric-mean cross volume or private-square currency **while retaining the opposite-bank curvature**, or route failure into an already paid ridge/grouped-hub/projected-crossing/physical-pair branch.

## 8. Corrections preserved

No step uses post-rotation independence, conditional density caps as independence, arbitrary-joint rank-three coarea, positive conditional projected-density moments, uniform pointwise quadratic-phase decay, deletion of a small nonzero remainder, or a uniformly good single physical minor. All conditioning is on ORIGINAL coordinate banks.
