SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-24T11:00:39Z.
attacking: the exact borderline two-by-two physical cross packet: convert its nonintegrable |t|^{-1} envelope into all finite output L^p bounds, a sharp h log(1/h) small-ball estimate, and an L^r residual gluing theorem.

# fleet03/B01 — borderline cross-two finite-p and conditional L^r closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T110039Z-fleet03-B01-qform-auto11`  
Assignment: Oscillatory replacement / quantitative inequalities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW BORDERLINE FINITE-p / DISTRIBUTION-FUNCTION / CONDITIONAL-RESIDUAL THEOREMS; FULL QFORM OPEN**

## 1. Scope and correction boundary

The owner target remains open: for every n, independent original-coordinate real random variables with probability densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove that Q=X^TAX has a universally bounded density, or give a valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, identical-law, or diagonal-basis assumption is introduced. No independence after a spectral rotation is used.

The live corrections are retained. In particular:

- bounded density alone does not imply law-uniform pointwise quadratic-phase power decay;
- a nonsingular 2x2 physical cross block by itself does not force an L^infinity density (the known saddle example has a logarithmic singularity);
- no generic conditional projection-density cap or arbitrary-joint coarea theorem is used;
- the recently refuted mixed norm `int |t|^(-1/2)||G_t||_2 dt` is not used.

The run started by attempting to recover the missing phase-space dimension in the preceding ambiguity-cell route. A source search found that the most immediate 3x3 physical-cross Plancherel implication had already been proved by fleet01/B03 and fleet02/B07, with the exact density bound `m/(m-2)|det C|^(-1/m)` for m>=3. Per the owner duplicate-work rule I did not re-publish that result. The new work below attacks the **borderline m=2 endpoint**, which those reports explicitly leave nonintegrable in L^1_t.

## 2. Source-matched endpoint used as the starting line

The source-matched report

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/B03-20260922T115130Z-qform-decoupled-time/REPORT.md`

proves, by conditioning every coordinate outside disjoint original-coordinate sets I,J of equal size m and then one Cauchy--Plancherel step, that for C=A[I,J]

`|phi_Q(t)| <= min(1, pi^(m/2)|det C|^(-1/2)|t|^(-m/2)).`       (2.1)

The published theorem uses m>=3 to integrate (2.1) in time. For the present run take **m=2** and write

`delta=|det C|>0`, `a=pi delta^(-1/2)`.                           (2.2)

Then the same already-proved calculation gives the exact borderline envelope

`boxed: |phi_Q(t)| <= min(1,a/|t|).`                              (2.3)

This retains every within-I term, every within-J term, every outside coordinate, every outside coupling, and all affine terms. It uses only original-coordinate conditioning. The new theorems begin from (2.3).

## 3. Main new theorem: every finite output L^p norm is controlled

### Theorem 3.1 — `QFORM-CROSS2-ALL-FINITE-LP-v1`

Assume there are disjoint original-coordinate pairs I,J with

`delta=|det A[I,J]|>0`.                                          (3.1)

Then the law of Q has a density p_Q belonging to L^p(R) for every finite `2<=p<infinity`, with

`boxed:
 ||p_Q||_p
 <= p^((p-1)/p) delta^(-(p-1)/(2p)).
}`                                                               (3.2)

In particular

`boxed: ||p_Q||_2 <= sqrt(2) delta^(-1/4).`                       (3.3)

No continuity conclusion is asserted from Theorem 3.1 alone.

### Proof

First integrate the square of (2.3):

`int_R |phi_Q(t)|^2 dt`
` <=2[int_0^a 1 dt + int_a^infinity a^2 t^(-2)dt]`
` =4a=4pi delta^(-1/2).`                                         (3.4)

A finite measure whose Fourier transform belongs to L^2 has an L^2 density; by Plancherel,

`||p_Q||_2^2=(1/(2pi))||phi_Q||_2^2 <=2 delta^(-1/2),`            (3.5)

which proves (3.3).

Now fix `2<=p<infinity` and put

`q=p/(p-1) in (1,2].`                                             (3.6)

Again from (2.3),

`||phi_Q||_q^q`
` <=2[int_0^a 1 dt + int_a^infinity (a/t)^q dt]`
` =2a[1+1/(q-1)]`
` =2a q/(q-1)`
` =2pi delta^(-1/2) p.`                                          (3.7)

Because p_Q already exists in L^2, inverse Hausdorff--Young applies to its Fourier transform:

`||p_Q||_p <=(2pi)^(-1/q)||phi_Q||_q.`                            (3.8)

Substituting (3.7), and using `1/q=(p-1)/p`, makes the Fourier-normalization constants cancel exactly:

`||p_Q||_p`
` <=(2pi)^(-1/q)[2pi p delta^(-1/2)]^(1/q)`
` =p^((p-1)/p) delta^(-(p-1)/(2p)).`                              (3.9)

This proves the theorem. QED.

### Interpretation

The 2x2 cross endpoint is therefore not merely “nonintegrable at t^{-1}.” It has a complete finite-p scale, with the correct density homogeneity. As `p->infinity`, the bound grows linearly like `p delta^(-1/2)`, which is compatible with the known logarithmic saddle singularity and explains why no L^infinity statement can be extracted from this resource alone.

## 4. Distribution-function replacement: h log(1/h) at the cross-two endpoint

### Corollary 4.1 — `QFORM-CROSS2-HLOGH-SMALLBALL-v1`

Let I_0 be any interval of length h and set

`x=h/sqrt(delta).`                                                (4.1)

If `0<x<=e^(-2)`, then

`boxed:
 P(Q in I_0)
 <= e x log(1/x)
 = e (h/sqrt(delta)) log(sqrt(delta)/h).
}`                                                               (4.2)

For larger h use the trivial probability bound one.

### Proof

Holder and Theorem 3.1 give, for every finite p>=2,

`P(Q in I_0)`
` <=h^(1-1/p)||p_Q||_p`
` <=(p h/sqrt(delta))^(1-1/p)`
` =(p x)^(1-1/p).`                                                (4.3)

For x<=e^(-2), choose

`p=L=log(1/x)>=2.`                                                (4.4)

Since x=e^(-L),

`(Lx)^(1-1/L)`
` =Lx exp(1-(log L)/L)`
` <=e Lx,`                                                        (4.5)

which is (4.2). QED.

Thus the false law-uniform pointwise Fresnel decay is replaced, on this critical coupled packet, by a near-linear **distribution-function** estimate. The logarithm is structurally natural: a nonsingular 2x2 cross block alone can have an actual logarithmic output-density singularity.

## 5. Exact signed-Fejer growth at the same endpoint

Define the normalized triangular Fejer mean

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)e^(-ity) phimu(t)dt.`    (5.1)

### Corollary 5.1 — `QFORM-CROSS2-FEJER-LOG-v1`

Under Theorem 3.1,

`boxed:
 sup_y D_T law(Q)(y)
 <= T/(2pi),                                  T<=a,
}`                                                               (5.2)

and for `T>=a=pi/sqrt(delta)`,

`boxed:
 sup_y D_T law(Q)(y)
 <= delta^(-1/2) log(T sqrt(delta)/pi)
    + pi/(2T delta).
}`                                                               (5.3)

### Proof

The Fejer kernel is positive, and absolute Fourier integration with (2.3) gives

`D_T(y) <=(1/pi)int_0^T(1-t/T)min(1,a/t)dt.`                     (5.4)

If T<=a this is `T/(2pi)`. If T>=a, split at a:

`int_0^a(1-t/T)dt + a int_a^T(1/t-1/T)dt`
` =a log(T/a)+a^2/(2T).`                                         (5.5)

Divide by pi and substitute a=pi/sqrt(delta). QED.

This gives an explicit signed/averaged-frequency replacement at the exact borderline where absolute L^1_t fails logarithmically.

A direct interval estimate can also be read from the positive Fejer kernel. Since

`K_T(z)=T/(2pi) [sin(Tz/2)/(Tz/2)]^2`,                           (5.6)

concavity of sin on [0,1/2] gives, for |Tz|<=1,

`K_T(z)>=T(1-cos 1)/pi.`                                         (5.7)

Taking T=2/h for an interval centered at y therefore yields

`P(Q in I_0) <= [pi h/(2(1-cos1))] D_(2/h)(y).`                  (5.8)

The prefactor is

`pi/[2(1-cos1)]=3.4170202436219475...`                           (5.9)

and (5.3) then supplies another explicit h log(1/h) estimate. Corollary 4.1 has the cleaner leading constant e.

## 6. New conditional L^r gluing theorem

The preceding endpoint can be turned into an actual bounded continuous density as soon as an independent packet supplies an L^r residual budget. The useful point is that a **shared conditioning bank is allowed**.

### Theorem 6.1 — `QFORM-CROSS2-CONDITIONAL-LR-GLUE-v1`

Let the independent original coordinates be partitioned into four groups:

- a physical pair Y_I;
- a disjoint physical pair Y_J;
- a residual bank V;
- an arbitrary conditioning bank W.

Assume there are **no direct quadratic couplings between** `(Y_I,Y_J)` and V. Couplings from either packet to W are allowed. For almost every W=w write

`Q=q_w(Y_I,Y_J)+Z_w(V),`                                          (6.1)

where the cross matrix between Y_I and Y_J is the same fixed invertible 2x2 matrix C, `delta=|det C|`, while all same-bank quadratic terms and all w-dependent affine terms in q_w are arbitrary.

Suppose for some `1<r<=2` every conditional residual law `Z_w(V)` has a density z_w satisfying

`esssup_w ||z_w||_r <= M_r.`                                     (6.2)

Then Q has a continuous C_0 density and

`boxed:
 ||p_Q||_infinity
 <= [r/(r-1)]^(1/r) delta^(-1/(2r)) M_r.
}`                                                               (6.3)

### Proof

Let

`A_w(t)=E exp(it q_w(Y_I,Y_J)),`
`H_w(t)=E exp(it Z_w(V)).`                                        (6.4)

Conditional independence gives

`phi_Q(t)=E_W[A_W(t)H_W(t)].`                                    (6.5)

The source-matched 2x2 cross argument is uniform in every affine shift and every same-bank phase, hence

`|A_w(t)|<=g(t):=min(1,a/|t|),   a=pi delta^(-1/2)`              (6.6)

for every w. Therefore

`|phi_Q(t)|<=g(t) H_*(t),`
`H_*(t):=E_W |H_W(t)|.`                                           (6.7)

Write `r'=r/(r-1)`. Hausdorff--Young applied conditionally gives

`||H_w||_(r') <=(2pi)^(1/r') M_r.`                               (6.8)

Minkowski therefore gives

`||H_*||_(r') <=(2pi)^(1/r') M_r.`                               (6.9)

Meanwhile

`||g||_r^r=2a r/(r-1).`                                          (6.10)

Holders inequality in frequency gives

`||phi_Q||_1`
` <=[2a r/(r-1)]^(1/r)(2pi)^(1/r')M_r.`                          (6.11)

Fourier inversion and a=pi delta^(-1/2) yield the exact cancellation

`(1/(2pi))||phi_Q||_1`
` <=[r/(r-1)]^(1/r)delta^(-1/(2r))M_r,`                          (6.12)

which is (6.3). Since phi_Q belongs to L^1, the density is continuous and vanishes at infinity. QED.

The shared W bank is important: the theorem is stronger than a bare convolution statement. W may create arbitrary affine shifts in both packets and arbitrary same-bank curvature in the cross-two packet. The only separation required is the absence of direct edges between the cross-two packet and the residual V packet.

## 7. Designated partner fleet04/B01 applied at an actual inequality

The completed designated partner result is

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260924T012155Z-fleet04-B01-lr-residual-r1/REPORT.md`.

For independent cap-one U,V and every `1<r<=2`, it proves, uniformly over affine coefficients,

`Z=2cUV+beta U+gamma V+delta0`, `c!=0`,

`boxed:
 ||p_Z||_r <=2^((r-1)/r)|c|^(-(r-1)/r).
}`                                                               (7.1)

Apply this pointwise in the shared bank W to

`Z_w=2cUV+beta(w)U+gamma(w)V+delta0(w).`                          (7.2)

Then Theorem 6.1 gives the actual new inequality

`boxed:
 ||p_Q||_infinity
 <= [r/(r-1)]^(1/r)
    2^((r-1)/r)
    delta^(-1/(2r))
    |c|^(-(r-1)/r).
}`                                                               (7.3)

At r=2 this is especially simple:

`boxed:
 ||p_Q||_infinity <=2 delta^(-1/4)|c|^(-1/2).
}`                                                               (7.4)

The density is continuous C_0. This applies with arbitrary same-bank quadratic terms in the physical cross-two packet and arbitrary W-dependent affine coefficients in both packets. No scalar pointwise quadratic-phase decay is used.

### Reciprocal-scale cancellation

If the physical cross matrix is

`C=k I_2`, so `delta=k^2`,                                      (7.5)

and the hyperbolic coefficient is

`c=k^(-q0)`, `q0>=1`,                                            (7.6)

choose

`r=1+1/q0.`                                                      (7.7)

Then the complete k exponent in (7.3) is

`[-1+q0(r-1)]/r=0.`                                              (7.8)

Hence the density bound is uniform in k:

`boxed:
 ||p_Q||_infinity
 <= (q0+1)^(q0/(q0+1)) 2^(1/(q0+1)).
}`                                                               (7.9)

For q0=1,2,3,4 these constants are respectively

`2.0000000000, 2.6207413942, 3.3635856610, 4.1627660370.`        (7.10)

This is a concrete scale-exact application of the partner theorem.

## 8. Phase-aligned fragmented-support obstruction preserved

Fix any prescribed `s!=0` and any `eta>0`. The set

`E={x: dist(sx^2,2pi Z)<=eta}`                                   (8.1)

has infinite Lebesgue measure, because the large-radius admissible components have lengths comparable to a constant times k^(-1/2), whose sum diverges. Choose a finite union, trimming one component if needed, of total measure one and put `f=1_E0`. Then f is an admissible cap-one probability density and

`Re E exp(isX^2)>=cos eta.`                                      (8.2)

Thus the new finite-p, h log h, Fejer-log, and residual-gluing theorems do **not** restore any law-uniform positive-power pointwise quadratic-phase decay. They replace it by integrated-frequency and distribution-function information at a genuinely coupled critical packet.

## 9. Relation to the aggregate two-volume route

Fleet01/B02 proved an aggregate `e_2` Fourier/L^p theorem when the natural squared-two-minor row marginals stay below a non-coloop threshold. That theorem explicitly deteriorates as a row marginal tends to one. Theorem 3.1 above supplies the exact local **coloop endpoint**: a fixed nonsingular physical 2x2 cross packet still gives all finite L^p norms, even though L^infinity can fail.

This suggests the next B01 implication:

`QFORM-E2-NEARCOLOOP-FINITEP-AGGREGATION-v1`:
combine the aggregate non-coloop e_2 compiler with the new cross-two finite-p endpoint in the near-coloop regime, without selecting one dimension-losing tiny minor, and then feed the resulting finite-p packet into an already-paid square/hyperbolic/third-curvature smoother.

That structural aggregation is **not proved in this run**. The unrestricted full QFORM theorem remains open.

## 10. Deterministic checks

The sibling `checks.py` and `CHECKS.txt` verify:

- the exact cancellation in (3.9) for p=2,3,4,10,100;
- the L^2 endpoint constant sqrt(2);
- the Fejer kernel interval prefactor `pi/[2(1-cos1)]`;
- the partner-gluing r=2 constant exactly 2;
- the reciprocal-scale exponent cancellation and constants for q0=1,2,3,4,10;
- density homogeneity: delta has quadratic coefficient scale 2, c has scale 1, and the exponents in (7.3) sum to one.

These are regression checks. The proofs above are analytic.

## 11. Status

- `QFORM-FULL`: **OPEN**.
- `QFORM-CROSS2-ALL-FINITE-LP-v1`: **PROVED in stated scope**.
- `QFORM-CROSS2-HLOGH-SMALLBALL-v1`: **PROVED in stated scope**.
- `QFORM-CROSS2-FEJER-LOG-v1`: **PROVED in stated scope**.
- `QFORM-CROSS2-CONDITIONAL-LR-GLUE-v1`: **PROVED in stated scope**.
- fleet04/B01 `L^r` hyperbolic residual theorem: **APPLIED at (7.3)**.
- Continuity: **not proved** for the bare cross-two finite-p theorem; **proved C_0** for the conditional-L^r glued theorem.
- Native brain status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval/writeback is separate and does not establish native learned-memory ingestion.
