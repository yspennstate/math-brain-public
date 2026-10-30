SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-22T19:33:47Z.
attacking: O0 determinant-bank payment; replace single reciprocal minors by cross-rank fiber Plancherel, and stress-test the latest area-bank branch.

# fleet02/B07 — cross-rank fiber Plancherel and an aggregate-bank stress

**Run:** `20260922T193347Z-b07-639234ec`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / complementary constructions and source-valid counterexamples  
**Fresh owner control before the mathematical write:** revision `2026-09-22.15`; QFORM remains the sole target and no B07 stop was present.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED(intermediate single-packet extraction) / FULL TARGET OPEN`.

## 1. Exact target and corrections used

The target remains: for every finite `n`, every independent real `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal bound for the density of `Q=X^TAX`, or give a target-valid counterexample.

This report keeps the original coordinate product law throughout. It does not use post-rotation independence, the refuted arbitrary-joint rank-three coarea bound, a worst conditional fiber supremum, law-uniform pointwise Fresnel decay, or reciprocal payment of one arbitrarily small minor. The live correction ledger and CURRENT_RESEARCH were refreshed before the proof.

The latest complete designated-partner result consumed is fleet03/B07 r15, `QFORM-O0-EXCLUSION-PAIR-DICHOTOMY-v1`, canonical source

`yspennstate/math-open-problems@559e4be19d8f032bdae0392e7394bdcdca681a14:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T183653Z-fleet03-B07-qform-r15/REPORT.md`.

Its direct O0 dependency r13, `QFORM-O0-HEAVY-PACKET-ISOLATION-v1`, is at

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T173711Z-fleet03-B07-qform-r13/REPORT.md`.

I also use fleet02/B06's completed product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

Its needed statement is: if `R` has `k` orthonormal columns and `Y=R^T X` for independent cap-one coordinates, then `Y` has a density with

`||p_Y||_infinity <= exp(k/2)`.

## 2. New theorem: pay a rank-r cross interaction without choosing coordinates on both sides

### Theorem 2.1 — `QFORM-CROSS-FIBER-PLANCHEREL-v1`

Let `I,J` be disjoint sets of original coordinates and put `B=A[I,J]`. Assume `rank B=r>=3`, with nonzero singular values `s_1,...,s_r`, and write

`D=product_(nu=1)^r s_nu`.

Then the full quadratic form, with arbitrary self blocks, arbitrary outside couplings, arbitrary additional spectrum and arbitrary affine terms produced after conditioning, has a continuous density satisfying

`boxed( ||p_Q||_infinity <= e * r/(r-2) * D^(-1/r). )`          (2.1)

Equivalently, since `D^2=pdet_+(BB^T)`,

`||p_Q||_infinity <= e * r/(r-2) * pdet_+(BB^T)^(-1/(2r)).`    (2.2)

The bound deliberately uses the product of all nonzero singular values of this fixed physical cross block; it does not authorize discarding arbitrarily tiny extra singular values.

If in addition `|I|=r` and `B` has full row rank, the one-sided product structure improves the constant to

`boxed( ||p_Q||_infinity <= sqrt(e) * r/(r-2) * det(BB^T)^(-1/(2r)). )`  (2.3)

The symmetric full-column-rank version is identical.

### Proof

Condition on all original coordinates outside `I union J`. Independence of the coordinates in `I` and `J` is retained. The conditional phase is

`q(x,y)=x^T P x + 2 x^T B y + y^T R y + alpha dot x + beta dot y + c`,

with arbitrary symmetric `P,R` and arbitrary affine coefficients.

Take a thin singular-value decomposition

`B=U Sigma V^T`,

where `U,V` have `r` orthonormal columns and `Sigma=diag(s_1,...,s_r)`. For fixed frequency `t`, define the complex fiber amplitudes

`H_t(z)= integral_{U^T x=z} f_I(x) exp(i t[x^T P x+alpha dot x]) dH`,

`G_t(w)= integral_{V^T y=w} f_J(y) exp(i t[y^T R y+beta dot y]) dH`.

Because the maps have orthonormal rows, their coarea Jacobian is one. Taking absolute values before integrating along a fiber gives

`|H_t(z)| <= p_(U^T X_I)(z)`,
`|G_t(w)| <= p_(V^T X_J)(w)`.

Hence, by `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,

`||H_t||_1, ||G_t||_1 <=1`,
`||H_t||_infinity, ||G_t||_infinity <= e^(r/2)`,

and interpolation yields

`||H_t||_2, ||G_t||_2 <= e^(r/4)`.                         (2.4)

The crucial point is that the cross interaction depends only on the projected variables:

`x^T B y=(U^T x)^T Sigma (V^T y)=z^T Sigma w`.

With Fourier convention `hat H(xi)=integral exp(-i xi dot z)H(z)dz`, the conditional characteristic function, up to a unit scalar phase, is

`phi(t)=integral G_t(w) hat H_t(-2t Sigma w) dw`.

Cauchy--Schwarz, the invertible change of variables `xi=-2t Sigma w`, and Plancherel give

`|phi(t)|
 <= ||G_t||_2 (2|t|)^(-r/2) D^(-1/2) ||hat H_t||_2
 <= e^(r/4)(2|t|)^(-r/2)D^(-1/2)(2pi)^(r/2)e^(r/4)
 = pi^(r/2)e^(r/2)D^(-1/2)|t|^(-r/2).`                    (2.5)

This is uniform in the conditioned outside coordinates, hence it holds for the unconditional characteristic function as well. Together with `|phi(t)|<=1`, set

`K=pi^(r/2)e^(r/2)D^(-1/2)`,
`t_0=K^(2/r)=pi e D^(-1/r)`.

For `r>2`, exact integration gives

`integral_R min(1,K|t|^(-r/2)) dt
 =2 t_0 r/(r-2).`                                           (2.6)

Fourier inversion therefore gives a continuous density vanishing at infinity and

`||p_Q||_infinity <=(2pi)^(-1) *2 t_0 r/(r-2)
 =e r/(r-2)D^(-1/r)`,

which proves (2.1).

For (2.3), `|I|=r` makes `U` square orthogonal, so the `U^T` fibers are points and the original product amplitude itself has `L^2` norm at most one:

`||H_t||_2=||prod_(i in I)f_i||_2<=1`.

Only the `J` side pays the projection factor `e^(r/4)`. Thus (2.5) improves to

`|phi(t)|<=pi^(r/2)e^(r/4)D^(-1/2)|t|^(-r/2)`.

Now `t_0=pi sqrt(e)D^(-1/r)` and the same integration gives (2.3). QED.

## 3. Actual partner application: the three-heavy-row O0 collar is paid directly

Fleet03/B07 r13 proves in the O0 effective-dimension-three branch that the third-volume resource satisfies `E>=1/256`, and when at least three calibrated row leverages are at least `3/4` it selects an ORIGINAL row triple `H` with

`det(B_H B_H^T)>=E/16>=1/4096`.                             (3.1)

No column triple is needed now. Apply (2.3) with `r=3`, `I=H` and `J` equal to the whole opposite physical side. The full ambient quadratic form therefore obeys

`||p_Q||_infinity
 <=3 sqrt(e) det(B_HB_H^T)^(-1/6)
 <=3 sqrt(e) *4096^(1/6)
 =12 sqrt(e)
 =19.7846552484... .`                                       (3.2)

This pays the entire r13 three-heavy-row collar in one step, including the formerly separate transpose-diffuse and transpose-heavy subbranches. It retains arbitrary self blocks, outside couplings, extra spectral components and signs. It is stronger structurally than the previous fleet02/B07 payment, which needed a second selected column triple in the transpose-heavy branch.

## 4. A source-valid target stress: the latest r15 area bank cannot be collapsed to one good packet

The latest complete partner r15 isolates, after a heavy row and an exclusion-heavy second row, an area branch `g=det K[{i,j}]>=1/16` carrying a universal determinant-law mass on bounded-cardinality packets. At the exact-rank-three endpoint all this mass lies on triples containing `{i,j}`.

A tempting next step would be to extract one such triple with a dimension-free determinant. That implication is false even inside the original QFORM target.

Fix `N>=1`. Define an `(N+4) x 3` matrix `U_N` by the rows

`u_i=sqrt(3/4)e_1`,
`u_j=sqrt(1/2)e_2`,
`u_a=(1/2)e_1`,
`u_b=(1/sqrt(2))e_2`,
`u_{k}=N^(-1/2)e_3`,  k=1,...,N.`                           (4.1)

Then exactly `U_N^T U_N=I_3`, so `K=U_NU_N^T` is a rank-three projection with trace three. For the distinguished pair,

`ell=K_ii=3/4`, `K_jj=1/2`, `K_ij=0`,
`g=det K[{i,j}]=3/8`,                                       (4.2)

and the exclusion leverage in r15 is `m=1/2`. Thus this lies strictly in the partner's area-bank branch.

Every nonzero three-row packet containing `{i,j}` must use one of the `N` diffuse `e_3` rows. Its squared volume is

`det(U_S U_S^T)=3/(8N).`                                    (4.3)

The packets using `u_a` or `u_b` are rank deficient. Consequently

`max_(S superset {i,j}, |S|=3) det(U_SU_S^T)=3/(8N) ->0`,   (4.4)

while the aggregate volume-sampling mass is exactly

`sum_(S superset {i,j}, |S|=3) det(U_SU_S^T)
 =N*3/(8N)=3/8=g.`                                          (4.5)

So the constant aggregate r15 bank cannot be replaced by a single uniformly good row packet.

This is a **target-valid** structural stress, not merely an abstract DPP example. Form the symmetric matrix

`A_N = [[0,U_N],[U_N^T,0]].`                                (4.6)

Its nonzero eigenvalues are `+1,+1,+1,-1,-1,-1`, because all three singular values of `U_N` equal one. Hence every `A_N` satisfies the original spectral hypothesis with six unit-magnitude eigenvalues. Nevertheless the best pair-containing row triple decays as `1/N` in squared determinant.

This refutes only the intermediate implication

`constant r15 area-bank mass => one pair-containing coordinate packet with dimension-free determinant`.

It does **not** refute QFORM. In fact Theorem 2.1 pays this whole stress immediately: taking `B=U_N`, `r=3`, `D=1` gives

`||p_Q||_infinity <=3e=8.15484548538...`                    (4.7)

for arbitrary independent cap-one input laws and arbitrary additions in the allowed full-form theorem.

## 5. Conditional end-to-end position and first unpaid implication

A compact conditional route through the current B07 O0 state is now:

1. partner r13 isolates the third-volume resource and Theorem 2.1 pays its complete three-heavy-row branch by (3.2);
2. partner r14 pays an isolated heavy row after deletion unless there is a near-coloop or a second exclusion-heavy row;
3. partner r15 converts the latter into either a determinant-weighted bounded-cardinality area bank or a quantitative replacement pair;
4. **this report proves that the r15 area bank must be paid in aggregate**: selecting one pair-containing packet cannot work in general, even for a target-valid rank-three cross interaction;
5. if that aggregate bank and the replacement/near-coloop alternatives are paid product-preservingly, the O0 branch closes. O1/O2/O3 remain separate global debts from the current synthesis.

Therefore the first essential unpaid B07 implication is

`QFORM-O0-AREA-BANK-AGGREGATE-FIBER-PAYMENT-v1`:

> Starting from r15's constant determinant-law mass on size-3-to-5 packets containing a fixed replacement pair, obtain a dimension-free full-form density estimate by summing/averaging the packet currency **before reciprocal inversion**. It must cover the family (4.1)-(4.6), where every individual pair-containing packet tends to zero, and retain arbitrary self blocks/additional spectrum. A grouped partial-fiber Plancherel or regularized-ridge synthesis is admissible; worst-packet selection is not.

The r15 small-`g` replacement branch and the `ell>7/8` near-coloop branch remain sibling O0 obligations. Full QFORM is therefore OPEN.

## 6. Exact deterministic checks

The accompanying `CHECK.py` uses exact rational arithmetic for (4.2)-(4.5) and evaluates the two density constants. For `N=8,64,512,4096`, it verifies `N*(3/(8N))=3/8` while the individual packet tends to zero. It also records

`3e=8.154845485377136`,
`12sqrt(e)=19.78465524840154`.

Terminal marker: `STATUS=QFORM_CROSS_FIBER_PLANCHEREL_CHECK_PASS`.

The checker is a regression/calibration only; the universal proof is the analytic argument in Section 2.
