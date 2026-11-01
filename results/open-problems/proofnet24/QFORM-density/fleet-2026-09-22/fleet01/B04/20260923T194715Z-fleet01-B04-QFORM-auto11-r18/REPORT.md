SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T19:47:15Z.
attacking: derive a marginal-free third-compound product-Fourier certificate and convert disjoint third-compound spectral energy into an original-coordinate partition with an explicit bound.

# fleet01/B04 r18 — marginal-free third-compound crossing and a disjoint-compound random-cut theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `SUPPORTING_THEOREM_PROVED / GLOBAL_DISJOINT-COMPOUND BRANCH PAID / PARTNER_APPLIED / FULL_TARGET_OPEN`  
Continuity in the new branch: **proved (`C_0`)**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The new theorem identifies a clean global spectral/product-space quantity which is sufficient, and isolates exactly why this crossing mechanism cannot alone finish the diagonal/overlap-dominated branch. No random variable is spectrally rotated. No pointwise quadratic-phase decay, arbitrary-joint coarea bound, conditional-density cap, moment assumption, compact support, connected support, Gaussianity, or log-concavity is used.

## 1. Source boundary


The analytic receiver is the independently checked arbitrary-rank projected-crossing theorem

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

together with this worker's preceding marginal-removal theorem

`QFORM-CANONICAL-COMPOUND-PROMOTION-v1`,

`yspennstate/math-open-problems@d5e114f4a9f515344575756615fce3a754195b13`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T185132Z-fleet01-B04-QFORM-auto11-r17/REPORT.md`.

The designated fleet02/B04 result applied below is its latest completed heavy-row report

`yspennstate/math-open-problems@beaf7fe9fb87fb81a13a35d5237793eb3b0dde14`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T182451Z-fleet02-B04-auto11-r12/REPORT.md`.

The current Claude continuation at `c4c23b784395630c094ba299a50712209921d1ae` was read as a source; its proposed single-hub conditional-adaptation estimate remains open and is not used below.

## 2. Marginal-free third-compound crossing theorem

Let `I,J` be disjoint sets of original independent coordinates and write

`B=A[I,J]`.

Define the physical third-compound energy

`E_3(B)=e_3(BB^T)`.

By Cauchy--Binet,

`E_3(B)=sum_(R subset I, |R|=3) det(B_R B_R^T)`

`       =sum_(R subset I, T subset J, |R|=|T|=3) det B[R,T]^2`.          (2.1)

Consider the **full** quadratic form, not only the crossing term,

`Q=F(X_I)+2 X_I^T B X_J+G(X_J)`,                                  (2.2)

where in the QFORM application `F` and `G` are the arbitrary same-bank quadratic terms (and the receiver permits the corresponding measurable internal phases).

### Theorem `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`

If `E_3(B)>0`, then for every independent cap-one product input law,

`boxed: ||p_Q||_infinity <= 6^(4/3) E_3(B)^(-1/6),`                (2.3)

and the density has a representative in `C_0(R)`. Equivalently,

`integral_R |phi_Q(t)| dt <= 2 pi 6^(4/3) E_3(B)^(-1/6)`.         (2.4)

There is **no physical row-marginal hypothesis**.

#### Proof

Apply `QFORM-CANONICAL-COMPOUND-PROMOTION-v1` with no initial hub: `k=0`, compound order `ell=3`, `d=k+ell=3`, zero-dimensional hub density cap `M_H=1`, empty singular product `S=1`, and projected crossing `C=B`. Then `Z_3=e_3(BB^T)=E_3(B)`. The theorem gives

`||p_Q||_infinity`

`<= [3/(3-2)] 2^((0+9)/6) (3^3/3!)^(1/6) E_3(B)^(-1/6)`

`=3*2^(3/2)*(9/2)^(1/6) E_3(B)^(-1/6)`

`=6^(4/3) E_3(B)^(-1/6)`.                                       (2.5)

The terminal Fourier estimate is integrable because the total smoothing count remains `d=3` through every physical promotion. Hence Fourier inversion gives a continuous density vanishing at infinity. QED.

The point of (2.3) is that a canonical third-volume law may be arbitrarily concentrated on a physical row: whenever its row marginal exceeds `1/2`, the promotion theorem converts that **original scalar coordinate** into a hub and lowers the residual compound order by one. No reciprocal tiny local minor is selected.

## 3. Exact adaptive certificate behind (2.3)

The coarse constant in (2.3) can be sharpened by retaining the actual promotion history.

Start with `Z_3=E_3(B)`. Suppose the promotion algorithm selects `p` physical rows, with canonical inclusion marginals

`alpha_1,...,alpha_p > 1/2`,

and terminates at residual compound order

`r=3-p`.

At each step the exact base-times-height recursion from the preceding theorem is

`S_(j+1)^2 Z_(ell_j-1)^(j+1)=alpha_(j+1) S_j^2 Z_(ell_j)^j`.     (3.1)

Therefore after `p` promotions,

`boxed: S_p^2 Z_r = E_3(B) product_(j=1)^p alpha_j.`             (3.2)

Let `w_r` be the terminal canonical `r`-subset law and let

`F_r^2=exp(H(w_r)+sum_i alpha_i^(r) log alpha_i^(r))`,           (3.3)

with `F_0=F_1=1`. The exact fixed-cardinality entropy identity from r17 is

`F_r^2=(r^r/r!) exp[-TC(I_1,...,I_r)]`,                          (3.4)

where `(I_1,...,I_r)` is a uniformly ordered version of the random subset. Thus

`F_r^2<=r^r/r!`.                                                 (3.5)

Keeping (3.2)--(3.4) rather than the worst-case relaxations yields the adaptive certificate

`boxed:
 ||p_Q||_infinity
 <=3 * 2^((p+3r)/6) * F_r^(1/3)
   * [E_3(B) product_(j=1)^p alpha_j]^(-1/6).`                   (3.6)

Because every promoted `alpha_j>1/2` and (3.5) holds, (3.6) implies (2.3). Formula (3.6) is useful when one or two heavy physical rows are visible: their volume is retained rather than discarded.

## 4. Random-cut conversion from a global disjoint compound

For a real symmetric `n x n` matrix `A`, define the **disjoint third-compound energy**

`Delta_3^disj(A)`

`=sum_{R,T subset [n], |R|=|T|=3, R intersect T=empty} det A[R,T]^2`.   (4.1)

The row and column triples in (4.1) are labelled/ordered as roles (`R` is the row triple, `T` the column triple), although each subset itself is unordered.

### Theorem `QFORM-DISJOINT-THIRDCOMPOUND-RANDOMCUT-v1`

If `Delta_3^disj(A)>0`, then for every independent cap-one input law,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 2*6^(4/3) [Delta_3^disj(A)]^(-1/6),`                         (4.2)

and `p_(X^TAX) in C_0(R)`.

#### Proof

Choose a labelled Bernoulli half-partition `[n]=I sqcup J`, independently assigning each physical coordinate to `I` or `J` with probability `1/2`. By (2.1),

`E_3(A[I,J])`

`=sum_(R subset I, T subset J, |R|=|T|=3) det A[R,T]^2`.         (4.3)

For a fixed pair of **disjoint** triples `(R,T)`, the event `R subset I` and `T subset J` has probability exactly `2^-6=1/64`. If the triples overlap, that event is impossible. Linearity of expectation therefore gives the exact identity

`boxed:
 E_partition E_3(A[I,J]) = Delta_3^disj(A)/64.`                  (4.4)

Hence some original-coordinate partition satisfies

`E_3(A[I,J]) >= Delta_3^disj(A)/64`.                             (4.5)

For this fixed partition the full quadratic form decomposes as

`X^TAX=X_I^T A_II X_I +2X_I^T A_IJ X_J+X_J^T A_JJ X_J`,        (4.6)

so Theorem (2.3) applies with `B=A[I,J]`, while retaining both arbitrary same-bank quadratic blocks. Thus

`||p||_infinity`

`<=6^(4/3) (Delta_3^disj/64)^(-1/6)`

`=2*6^(4/3) (Delta_3^disj)^(-1/6)`,                              (4.7)

and the same Fourier argument gives `C_0` regularity. QED.

Numerically the coefficient in (4.2) is

`2*6^(4/3)=21.80544711398567...`.                                (4.8)

## 5. Relation to the spectral hypothesis and the exact remaining debt

The total squared third-compound energy is

`E_3^tot(A)=sum_(|R|=|T|=3) det A[R,T]^2`

`          =e_3(A^2)`

`          =sum_(i<j<k) s_i(A)^2 s_j(A)^2 s_k(A)^2`,             (5.1)

where `s_i(A)` are singular values. Therefore the owner's hypothesis `s_3(A)>=1` implies

`E_3^tot(A)>=1`.                                                  (5.2)

Consequently, for any `theta>0`, the branch

`Delta_3^disj(A)>=theta E_3^tot(A)`                              (5.3)

is completely paid by

`boxed: ||p_(X^TAX)||_infinity <=2*6^(4/3) theta^(-1/6),`        (5.4)

with a `C_0` density.

But no universal positive `theta` follows from the bare spectral assumption. For a diagonal matrix with three diagonal entries of modulus at least one, every disjoint off-diagonal `3x3` minor vanishes, so

`Delta_3^disj(A)=0`,                                             (5.5)

while the diagonal form is separately controlled by the elementary `pi` theorem. Thus (4.2) is not being mislabeled as a full solution.

The new structural gap is precise:

`QFORM-OVERLAP-THIRDCOMPOUND-ROUTING-v1`:

when `e_3(A^2)>=1` but `Delta_3^disj(A)` is small, exploit the third-compound energy carried by pairs `(R,T)` with `|R intersect T|=1,2,3` and route it into an already-paid physical principal/diagonal, compound-hub, pair-log, aggregate-square, ridge, or exact-rank endpoint, without inserting a reciprocal tiny coefficient or rotating the independent inputs.

This is strictly more specific than the previous generic `target-scale grouped packet` debt: the entire disjoint-compound sector is now quantitatively finished.

## 6. Designated partner applied on the same dense rotated target

Use the fleet02/B04 family

`V=I_5-(2/5)11^T`,

`M_L=diag(L,1,1,1,1)V`,

`A_L=[[0,M_L],[M_L^T,0]]`,                                      (6.1)

with `L>=1`. The partner report proves `V` is orthogonal with every physical entry nonzero, the singular values of `M_L` are `L,1,1,1,1`, and

`spec(A_L)={+/-L,+/-1,+/-1,+/-1,+/-1}`.                         (6.2)

Hence this is genuinely rotated, indefinite, and target-valid.

For the natural physical left/right partition,

`E_3(M_L)=e_3(diag(L^2,1,1,1,1))=6L^2+4`.                      (6.3)

The new marginal-free theorem therefore gives the actual inequality

`boxed:
 ||p_(X^T A_L X)||_infinity
 <=6^(4/3)(6L^2+4)^(-1/6),
 p in C_0.`                                                       (6.4)

The exact adaptive certificate explains the partner's superior hub exponent without an extra theorem. Under canonical third-volume sampling the heavy first physical row has marginal

`alpha=6L^2/(6L^2+4)`.                                         (6.5)

Promoting it leaves four orthonormal residual rows, so `Z_2=6`; the terminal canonical pair law is uniform on six pairs and

`F_2^2=3/2`.                                                     (6.6)

Substitution in (3.6) gives exactly

`boxed:
 ||p_(X^T A_L X)||_infinity
 <=3*2^(5/6)L^(-1/3).`                                          (6.7)

Thus the partner's one-heavy-row hub certificate is precisely the first physical promotion of the general third-compound compiler.

The **completed fleet02/B04 result actually applied for comparison** is its global ambient D-prime optimization. For

`sqrt(2)<=L<=exp(35/2)`,

it proves

`||p_(X^T A_L X)||_infinity`

`<=10^(5/6) sqrt(5e/6) L^(-1/5)`.                              (6.8)

At `L=4096`, the three source-backed bounds on the same matrix are

`new coarse E3 crossing:          0.5055023046261697`,

`new exact adaptive promotion:    0.3340870193026273`,

`fleet02/B04 global D-prime:     1.9427546703383625`.          (6.9)

Hence even the coarse new theorem improves the designated partner's completed ambient-volume inequality by the explicit factor

`1.9427546703383625 / 0.5055023046261697`

`=3.8432162475996483...`,                                       (6.10)

while the exact adaptive formula reproduces the stronger `L^(-1/3)` physical-hub mechanism.

## 7. Integrity and scope

The proof uses only original-coordinate independence, Cauchy--Binet, a random **coordinate partition**, and the already proved product-Fourier compound-promotion receiver. It does not infer independence after a spectral rotation. It does not require a pointwise oscillatory decay estimate. It does not assert that disjoint compound energy is automatically large under the target spectral hypothesis. It also does not use Monte Carlo evidence.

The current result proves an essentially bounded density and, in its exact scope, the stronger continuous `C_0` representative. The full universal target and full-target continuity statement remain open pending the overlap-compound routing implication above and independent review of this new theorem.

## 8. Publication record

Run: `20260923T194715Z-fleet01-B04-QFORM-auto11-r18`.

Canonical directory:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T194715Z-fleet01-B04-QFORM-auto11-r18/`.

Changed-file allowlist for the math repository is restricted to this immutable run directory. No credentials, private nonmathematical data, account secrets, scheduler IDs, signed URLs, or unrelated material are included. Repository publication is file transport only and is not native learned-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
