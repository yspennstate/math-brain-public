SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T22:36:48Z.
attacking: compound-energy trichotomy after one literal scalar pivot; pay the disjoint two-volume branch through a post-Schur E2 cross receiver and signed-Fejer transfer.

# account03/B01 — scalar-pivot second-compound decomposition and disjoint-E2 payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T223648Z-auto11-compound`  
Assignment: oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM + EXACT PARTNER IDENTITY APPLICATION + AVERAGED-FREQUENCY CONSEQUENCE / FULL QFORM OPEN**

## 1. Target and correction boundary

The target is unchanged. The inputs are independent real ORIGINAL coordinates with probability densities bounded by one, and `A` is an arbitrary real symmetric matrix with `s_3(A)>=1`. No Gaussianity, log-concavity, moments, compact support, connected support, iid assumption, or independence after a rotation is used.

Fresh control was read from `yspennstate/math-research-brain@e71afbc43fbe0cfd51f86b10b0ad7fb3bd59d9e9`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and the full conjecture remains OPEN. The current correction boundary is retained: law-uniform pointwise quadratic Fresnel decay is false; arbitrary-joint coarea does not replace product provenance; small matrix tails cannot be deleted without moment assumptions; a bounded projection density alone does not control an indefinite quadratic pushforward.

This run attacks the first unpaid structural implication left by the preceding B01 high-diagonal reduction. The new point is to aggregate **all** physical two-minors of the exact scalar Schur complement before selecting any individual minor. The resulting second-compound energy splits into three geometrically distinct channels, one of which is paid uniformly by the existing aggregate-E2 receiver.

## 2. Source-pinned inputs used at equations

### 2.1 Designated partner account04/B01

Canonical source:

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

For a literal physical pair `S={i,j}`, with first scalar pivot `a=A_ii!=0`, let `H` be the scalar Schur complement after eliminating `i`. In the partner notation, for the second coordinate `j`,

`delta=H_jj`, `ell_k=H_jk`, `M_kl=H_kl` for `k,l!=j`,

and the partner proves the exact identity

`W_2({i,j})
 = a^2 sum_(k!=l; k,l!=j)
       (H_jj H_kl-H_jk H_jl)^2.`                                (2.1)

Equivalently,

`W_2({i,j})/a^2
 = sum_(k!=l; k,l!=j)
   det H[{j,k},{j,l}]^2.`                                       (2.2)

Only this exact identity is used below. In particular, this run does **not** use the partner report's subsequently corrected individual-bank conclusion from its Corollary 4.1.

### 2.2 Aggregate-E2 scalar-Schur receiver

Source:

`yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T102108Z-account03-B08-qform-diffuse-r32/REPORT.md`.

If one original coordinate with nonzero coefficient `a` is completed exactly and the resulting scalar Schur matrix contains a literal original-coordinate cross block `N` with

`E_2(N)=sum_(|R|=|C|=2) det N[R,C]^2 = Delta_2>0`,

then, retaining arbitrary same-bank curvature, arbitrary additional residual couplings and all additional spectrum,

`||p_Q||_infinity
 < C_E2 |a|^(-1/2) Delta_2^(-1/8),`                             (2.3)

where

`C_E2=2 sqrt(10) 7^(9/10)
     =36.44334493792993... .`                                    (2.4)

The source proves essential boundedness in this outer-square branch; continuity is not asserted there.

### 2.3 Scalar-Schur singular-value persistence

The immediate predecessor B01 report proves that if

`A=[[a,r^T],[r,C]]`, `a!=0`,

and

`H=C-a^(-1)rr^T`,                                                (2.5)

then

`s_(k+1)(A)<=s_k(H)` for every `k>=1`.                            (2.6)

In particular,

`s_3(A)>=1  =>  s_2(H)>=1`.                                     (2.7)

Canonical source:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T212842Z-auto11/REPORT.md`.

The proof is the exact rank-one decomposition

`A=diag(0,H)+a(1,r/a)^T(1,r/a)`

followed by rank-one singular-value interlacing. No probabilistic rotation is involved.

### 2.4 Designated partner signed-Fejer equivalence

Source:

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a law with bounded density,

`||p||_infinity = sup_(T>0,y) D_T mu(y)`,                        (2.8)

where `D_T` is the signed triangular Fejer average used throughout this programme. This transfers every density estimate below into a genuine averaged-frequency statement without asserting absolute Fourier `L^1` integrability.

## 3. The second-compound decomposition after one literal scalar pivot

Fix an ORIGINAL coordinate `i` with

`a=A_ii!=0`,                                                     (3.1)

let `K` be the remaining coordinate set, and let `H` be the exact scalar Schur complement (2.5), indexed by `K`.

For unordered two-subsets `R,C subset K`, define the squared minor

`m_(R,C)^2 := det H[R,C]^2`.                                     (3.2)

Partition all ordered pairs `(R,C)` of two-subsets according to their intersection size:

`P_2(H)=sum_(R=C) m_(R,C)^2`,                                    (3.3)

`O_2(H)=sum_(|R intersect C|=1) m_(R,C)^2`,                      (3.4)

`D_2(H)=sum_(R intersect C=empty) m_(R,C)^2`.                    (3.5)

Here `P` means principal, `O` overlap-one, and `D` disjoint.

### Theorem 3.1 — `QFORM-SCALARPIVOT-COMPOUND-DECOMPOSITION-v1`

For every real symmetric `A` with the pivot (3.1),

`boxed:
 ||wedge^2 H||_F^2 = P_2(H)+O_2(H)+D_2(H).`                      (3.6)

Moreover the three terms have exact pre-Schur interpretations:

`boxed:
 a^2 P_2(H)
 = sum_(R subset K, |R|=2)
     det A[{i} union R,{i} union R]^2,`                           (3.7)

`boxed:
 a^2 O_2(H)
 = sum_(j in K) W_2({i,j}),`                                     (3.8)

and

`boxed:
 a^2 D_2(H)
 = sum_(R,C subset K, |R|=|C|=2, R intersect C=empty)
     det A[{i} union R,{i} union C]^2.`                           (3.9)

If additionally `s_3(A)>=1`, then

`boxed:
 P_2(H)+O_2(H)+D_2(H)>=1.`                                      (3.10)

Hence at least one of the three nonnegative channels is at least `1/3`.

#### Proof

The compound-matrix Cauchy--Binet identity gives

`||wedge^2 H||_F^2
 = sum_(|R|=|C|=2) det H[R,C]^2
 = e_2(H^T H)
 = sum_(p<q) s_p(H)^2 s_q(H)^2.`                                (3.11)

Partitioning the sum according to `|R intersect C|=2,1,0` proves (3.6).

Scalar block elimination gives, for every two-subsets `R,C subset K`,

`det A[{i} union R,{i} union C]
 = a det H[R,C].`                                                (3.12)

Taking `R=C` and summing proves (3.7). Taking disjoint `R,C` and summing proves (3.9).

For the overlap-one part, every ordered pair of two-subsets with intersection one has a unique shared coordinate `j` and a unique representation

`R={j,k}`, `C={j,l}`, `k!=l`, `k,l!=j`.                         (3.13)

Its minor is

`det H[{j,k},{j,l}]
 = H_jj H_kl-H_jk H_jl.`                                       (3.14)

The designated partner identity (2.1)-(2.2) therefore gives

`sum_(k!=l; k,l!=j) det H[{j,k},{j,l}]^2
 = W_2({i,j})/a^2.`                                             (3.15)

Summing over the unique shared coordinate `j` proves (3.8). This is the actual equation-level application of the designated partner result.

Finally, (2.7) gives `s_2(H)>=1`; hence also `s_1(H)>=1`. The single term `s_1(H)^2s_2(H)^2` in (3.11) is at least one, proving (3.10). QED.

### Interpretation

Equation (3.8) identifies the entire overlap-one second-compound mass with the **sum of the partner's physical overlap-two exterior-three stars**. No individual `W_2({i,j})` is selected, so there is no hidden factor depending on dimension.

Equation (3.9) identifies the disjoint part with three-by-three minors of the original matrix whose row and column triples share only the pivot `i`. This is precisely the part that can be converted into a literal post-Schur cross packet without inverting a small minor.

## 4. The disjoint compound channel is paid uniformly

### Theorem 4.1 — `QFORM-SCALARPIVOT-DISJOINT-E2-v1`

Under the hypotheses above, if

`D_2(H)>0`,                                                      (4.1)

then `Q=X^TAX` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 < C_E2 sqrt(2) |a|^(-1/2) D_2(H)^(-1/8).`                       (4.2)

Equivalently, with the pre-Schur disjoint triple currency

`mathcal D_i
 :=a^2D_2(H)
 =sum_(R intersect C=empty) det A[{i} union R,{i} union C]^2,`    (4.3)

one has

`boxed:
 ||p_Q||_infinity
 < C_E2 sqrt(2) |a|^(-1/4) mathcal D_i^(-1/8).`                  (4.4)

Numerically,

`C_E2 sqrt(2)=51.53867266946139... .`                            (4.5)

#### Proof

Independently color every coordinate of `K` red or blue with probability one half, and write the resulting disjoint ORIGINAL-coordinate banks as `I,J`.

For a fixed ordered disjoint pair of two-subsets `(R,C)`, the event

`R subset I`, `C subset J`                                      (4.6)

has probability `2^(-4)=1/16`. Therefore, for the literal cross block `H[I,J]`,

`E E_2(H[I,J])
 = D_2(H)/16.`                                                   (4.7)

Thus some deterministic original-coordinate cut satisfies

`Delta_2:=E_2(H[I,J]) >=D_2(H)/16.`                              (4.8)

Now apply the source-valid scalar-Schur E2 receiver (2.3) to the actual outer pivot `a` and this exact post-Schur cross block. It retains every same-bank quadratic term and every other residual coupling, so no part of `H` is deleted. We obtain

`||p_Q||_infinity
 < C_E2 |a|^(-1/2) [D_2(H)/16]^(-1/8)`
` = C_E2 sqrt(2) |a|^(-1/2)D_2(H)^(-1/8),`                       (4.9)

which is (4.2). Substituting `D_2(H)=mathcal D_i/a^2` gives (4.4). QED.

The homogeneity is correct: under `A -> lambda A`, `a -> lambda a` and `mathcal D_i -> lambda^6 mathcal D_i`, so (4.4) scales as `|lambda|^-1`.

### Corollary 4.2 — paid one-third branch

If the disjoint channel wins the compound trichotomy,

`D_2(H)>=1/3`,                                                   (4.10)

then

`boxed:
 ||p_Q||_infinity
 < C_E2 sqrt(2) 3^(1/8)|a|^(-1/2)
 =59.12530394810627... |a|^(-1/2).`                              (4.11)

In the high-physical-diagonal chamber of the preceding B01 run,

`|a|>=1/64`,                                                     (4.12)

this gives the universal numerical payment

`boxed: ||p_Q||_infinity <473.0024315848501.`                    (4.13)

This branch is dimension-free, sign-free, and does not select a single small physical minor.

## 5. A sharper high-pivot structural survivor

Combine Theorems 3.1 and 4.1. Whenever `s_3(A)>=1` and an original scalar pivot `a!=0` has been selected, exactly one of the following sufficient alternatives occurs:

1. **Disjoint compound payment:** `D_2(H)>=1/3`, in which case (4.11) pays the full form.
2. **Principal-triple aggregate:**

   `P_2(H)>=1/3`, equivalently

   `sum_(j<k) det A[{i,j,k},{i,j,k}]^2 >=a^2/3.`                 (5.1)

3. **Partner overlap-star aggregate:**

   `O_2(H)>=1/3`, equivalently

   `boxed:
   sum_(j in K) W_2({i,j}) >=a^2/3.`                             (5.2)

The point of (5.2) is that it uses the completed account04/B01 `W_2` currency **in aggregate**. The existing single-pair quarter-Riesz theorem may deteriorate if this mass is spread over many `j`; this run does not hide that remaining issue by choosing a maximum and paying a dimension factor.

Thus, inside the previous high-diagonal chamber `|a|>=1/64`, the former fixed-energy rank-two-tube obstruction has a new exact refinement: either it exposes a disjoint second-compound packet and is already paid by (4.13), or at least one half of the remaining exterior mechanism is concentrated in the principal-triple aggregate (5.1) or the partner overlap-star aggregate (5.2). Both survivors are now explicit nonnegative aggregate currencies in the original basis.

This reduction is compatible with the global exterior-three decomposition used elsewhere in the fleet, but it is sharper **after a chosen scalar pivot** because it identifies the overlap-one channel exactly with the partner's `W_2` stars and makes the disjoint channel immediately consumable by the E2 receiver.

## 6. Signed-Fejer / averaged-frequency consequence

Apply the designated account04/B01 signed-Fejer identity (2.8) to Theorem 4.1. For every `T>0` and `y in R`,

`boxed:
 D_T law(Q)(y)
 < C_E2 sqrt(2)|a|^(-1/2)D_2(H)^(-1/8).`                        (6.1)

In particular, on the one-third disjoint branch,

`boxed:
 sup_(T>0,y)D_T law(Q)(y)
 <59.12530394810627... |a|^(-1/2).`                              (6.2)

At `|a|>=1/64`, the right side is below `473.003`.

This is the assignment's requested kind of oscillatory replacement: it is an **averaged-frequency/distributional** estimate assembled from aggregate minors and product structure. It does not require or imply a law-uniform pointwise quadratic-phase power bound, and it does not require `hat mu in L^1`.

## 7. The phase-aligned pointwise obstruction is preserved

Fix any frequency `s>0` and `0<eta<pi/6`. The set

`E_(s,eta)={x: dist(sx^2,2pi Z)<=eta}`                           (7.1)

has infinite Lebesgue measure. Choose a finite union of its interval components of total measure one and let its indicator be the density `f`. Then

`Re E exp(isX^2)>=cos eta`,                                     (7.2)

so in particular

`|E exp(isX^2)|>=cos eta`.                                      (7.3)

For three independent coordinates one may choose the three cap-one laws separately, phase-aligned at the respective signed frequencies `s lambda_j`. The product characteristic function at that prescribed frequency has modulus at least `(cos eta)^3`, even for a diagonal rank-three form. Hence no positive law-uniform pointwise power decay in `s` can be recovered from the target assumptions.

Theorem 4.1 avoids this obstruction by spending aggregate physical two-volume and then using a density/signed-Fejer compiler, rather than bounding a scalar oscillatory factor pointwise.

## 8. Deterministic checks

The sibling `checks.py` verifies on seeded symmetric matrices of sizes four through eight:

- the exact second-compound decomposition (3.6);
- the partner overlap identity `O_2=sum_j W_2/a^2` after scalar completion;
- the scalar-Schur three-by-three minor lift (3.12);
- the fair-cut identity `E E_2(H[I,J])=D_2/16` by exhaustive enumeration of all colorings at the tested sizes;
- numerical rank-one singular-value interlacing;
- all displayed constants and scale exponents.

The committed `CHECKS.txt` records

`max_compound_decomposition_error=6.821e-13`,

`max_partner_overlap_identity_error=4.547e-13`,

`max_scalar_schur_minor_lift_error=1.776e-15`,

`max_random_cut_expectation_error=3.553e-15`,

and ends `STATUS=PASS`.

These are diagnostics only; the proof above is exact.

## 9. Remaining implication

The disjoint second-compound channel is now paid without a reciprocal single-minor loss. The first unpaid B01 implication is therefore

`QFORM-SCALARPIVOT-PRINCIPAL-OR-OVERLAP-AGGREGATE-v1`:

> Under `s_3(A)>=1` and a quantitatively useful original scalar pivot `a`, when `D_2(H)<1/3`, exploit the forced aggregate
> `P_2(H)+O_2(H)>2/3` while retaining arbitrary small spectrum and same-bank curvature. Either turn the principal-triple mass into a grouped square/physical-pair receiver, or turn the aggregate partner currency `sum_j W_2({i,j})` into a dimension-free averaged-frequency estimate without choosing one `j` and losing a factor depending on dimension.

This is a genuine aggregate-before-inversion problem. A proof may not replace `sum_j W_2` by a dimension-free lower bound on `max_j W_2`; such a statement is false in diffuse configurations. Likewise, small operator or Frobenius tails cannot simply be deleted because the input laws have no moment assumptions.

The unrestricted QFORM conjecture remains **OPEN**. This run proves essential boundedness only in the stated disjoint-compound branch. Full-target continuity remains open, and continuity is not claimed from Theorem 4.1.
