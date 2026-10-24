SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T01:40:31Z.
attacking: the R1 transverse-absorption gate — convert the order-one same-side curvature forced by the current rank-one-tube compiler into aggregate third-minor currency, and make the nonzero cross tail pay explicitly if it cancels that currency.

# account02/B19 r24 — transverse compound compiler for the first N3 gap

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING REDUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open: for every dimension, every independent real input vector with marginal probability densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `Q=X^TAX`, or give a valid target counterexample. No moment, support, log-concavity, iid, diagonal-basis or post-rotation-independence hypothesis is added. Continuity is claimed only on branches where a source theorem proves it.

## 1. Fresh source boundary and proof graph

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. I reread the owner proof-first and Claude-latest requests, the live correction ledger, and the required interactive package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The source-valid global graph used here is:

1. The newest Claude synthesis reduces the full theorem to one fixed no-pivot class `N3(tau)`; the current account03/B19 compiler fixes `tau=2^-20`.
2. account03/B19 r21 chooses a physical cut `L|R`, with cross block `B=A[L,R]`, `||B||_F^2>2/3`.
3. If `E_3(B)>=2^-36` and at least one canonical three-volume orientation has maximal marginal at most `2/3`, the proved D' theorem pays the form.
4. Otherwise account03/B19 r21 leaves exactly the rank-one tube R1, rank-two tube R2, or concentrated-volume R3.
5. Own r23 sharpened R1: with

   `B=sigma q r^T+E`, `sigma>4/5`, `||E||_F<1/590`,

   on at least one corresponding same-side block `C` either

   `||P_(q^perp)Cq||>589/1180`

   or

   `||P_(q^perp)CP_(q^perp)||_op>589/1180`.

   It also paid R3 whenever a nonanchor row-pair or column-pair atom has mass at least `1/4`.

This run attacks item 5. R2 remains outside the result below.

Corrections enforced throughout: the `1/590` cross tail is never deleted as a perturbation of the random variable; no spectral coordinate is declared independent; no conditional projection-density cap is used; no single physical minor is selected and inverted; and the false law-uniform pointwise quadratic-phase decay is not used.

## 2. Exact exterior identity for the R1 transverse side

Let `q` be the unit R1 singular vector on the transverse side, let `C` be the corresponding physical same-side block, put

`P=I-qq^T`,
`b=PCq`,
`D=PCP|_(q^perp)`.

Thus relative to `span{q} direct_sum q^perp`,

`C=[[a,b^T],[b,D]]`.

Define the aggregate mixed two-column/one-direction volume

`Z_q(C)
 := sum_(|I|=3, |J|=2) det([C[I,J],q_I])^2`.                         (2.1)

### Theorem 2.1 — `QFORM-R1-TRANSVERSE-SECOND-COMPOUND-v1`

One has the exact identity

`boxed: Z_q(C)=e_2((PC)(PC)^T).`                                      (2.2)

Moreover, if `b!=0` and `bhat=b/||b||`, then

`boxed:
 Z_q(C)
 = e_2(D^2)+||b||^2 ||D P_(bhat^perp)||_F^2.
`                                                                         (2.3)

#### Proof

For each two-element physical column set `J={j,k}`, the vector of all three-row determinants in (2.1) is the coordinate vector of

`q wedge C e_j wedge C e_k`.

Wedge with `q` kills every `q` component of the other two factors, so

`q wedge C e_j wedge C e_k
 =q wedge PC e_j wedge PC e_k`.

Summing squared Euclidean norms over `j<k` is exactly the Hilbert--Schmidt norm squared of `wedge^2(PC)`, hence `e_2((PC)(PC)^T)`. This proves (2.2).

In the domain decomposition `span{q} direct_sum q^perp`, the map `PC` is the block row `[b,D]`; therefore

`(PC)(PC)^T=bb^T+D^2`.

For any PSD `S` and vector `b`,

`e_2(S+bb^T)=e_2(S)+(tr S)||b||^2-b^T S b`.

Taking `S=D^2` and using symmetry of `D` gives

`(tr D^2)||b||^2-b^T D^2b
 =||b||^2[||D||_F^2-||D bhat||^2]
 =||b||^2||D P_(bhat^perp)||_F^2`,

which proves (2.3). QED.

## 3. The old slope/compression dichotomy becomes a low-rank-or-compound dichotomy

Put

`g=589/1180=0.4991525423...`,
`kappa=1/64`.

Every R1 state has, on the side selected by r23, either `||b||>g` or `||D||_op>g`.

### Corollary 3.1 — `QFORM-R1-LOWCOMPOUND-GEOMETRY-v1`

Either

`boxed: Z_q(C)>=g^2 kappa^2,}`                                      (3.1)

or the selected transverse side is quantitatively near low rank in the following exact sense.

* If `||D||_op>g`, then `s_2(D)<kappa`; hence `D` is within operator norm `<1/64` of a rank-one symmetric matrix.
* If `||b||>g`, then

  `||D P_(bhat^perp)||_F<kappa`,                                    (3.2)

  and, with `alpha=bhat^T D bhat`,

  `boxed: ||D-alpha bhat bhat^T||_F<sqrt(2)/64.}`                   (3.3)

  Consequently `C` is within Frobenius distance `<sqrt(2)/64` of a matrix supported on the two-dimensional deterministic span `span{q,b}`.

#### Proof

If `||D||>g` and `s_2(D)>=kappa`, then `e_2(D^2)>=s_1(D)^2s_2(D)^2>=g^2kappa^2`, and (2.3) gives (3.1). Thus failure of (3.1) forces `s_2(D)<kappa`.

If instead `||b||>g`, (2.3) and failure of (3.1) give (3.2). In the basis `bhat direct_sum bhat^perp`, write

`D=[[alpha,d^T],[d,F]]`.

Then `||D P_(bhat^perp)||_F^2=||d||^2+||F||_F^2<kappa^2`, while

`||D-alpha bhat bhat^T||_F^2=2||d||^2+||F||_F^2<2kappa^2`.

This is (3.3). QED.

This is already a strict sharpening of the first R1 gap. Low compound mass is no longer an unspecified order-one transverse operator: it is a near-rank-one transverse compression or a near-two-dimensional slope block. The nonzero remainder is retained, not discarded.

## 4. High compound mass: the rank-one cross channel creates a mixed third-minor tensor

Assume now (3.1). Write the actual R1 cross block

`B=sigma q r^T+E`, `||r||=1`, `sigma>4/5`, `||E||_F<1/590`.

For `I subset L`, `|I|=3`, `J subset L`, `|J|=2`, and `k in R`, define

`d_(I,J)=det([C[I,J],q_I])`,
`M_(I,J,k)=det A[I,J union {k}]`,
`F_(I,J,k)=det([C[I,J],E[I,k]]).`

Linearity of the determinant in its last column gives the exact tensor identity

`M_(I,J,k)=sigma r_k d_(I,J)+F_(I,J,k).`                           (4.1)

Let `Z_M=sum M^2` and `Z_E=sum F^2`. Reverse triangle in the full `ell_2(I,J,k)` tensor yields

`sqrt(Z_M)+sqrt(Z_E)>=sigma sqrt(Z_q(C)).`                           (4.2)

Therefore

`boxed: max(Z_M,Z_E)>=z_*}`,                                        (4.3)

where

`z_*=(1/4)(4/5)^2 g^2 kappa^2
    =346921/35645440000
    =9.7325492405...*10^-6.`                                        (4.4)

This is the key nonperturbative point: the small tail `E` is not thrown away. If it destroys the leading mixed determinant tensor, it must itself carry comparable determinant energy.

### Tail-cancellation alternative

For every `j<l,k`,

`||C e_j wedge C e_l wedge E e_k||^2
 <=||C e_j wedge C e_l||^2 ||E e_k||^2`.

Summing gives

`Z_E<=||E||_F^2 e_2(C^T C).`                                      (4.5)

Consequently, if `Z_E>=z_*`, then

`boxed:
 e_2(C^2)> z_* (590)^2
          =346921/102400
          =3.387900390625.
}`                                                                    (4.6)

Thus cancellation by the nominally tiny R1 tail is expensive: it forces a large same-side second compound. This is a new quantitative replacement for the forbidden inference that `E` can simply be deleted.

## 5. Actual mixed mass: split by physical overlap

Assume instead `Z_M>=z_*`. Split it according to

`h=|I cap J| in {0,1,2}`.

For some `h`, the corresponding mass `Z_M^(h)` is at least `z_*/3`.

### 5.1 `h=0`: genuine disjoint cross volume and a target-level payment

If `Z_M^(0)>=z_*/3`, independently two-colour the physical indices of `L`. A fixed disjoint configuration has probability `2^-5=1/32` that all three row indices land in the row colour and both same-side column indices land in the column colour. Hence some physical partition `L=P disjoint_union Q` gives the actual cross block

`N=A[P,Q union R]`

with

`E_3(N)>=z_*/96
       =1.01380721255...*10^-7.`                                    (5.1)

Now apply the **required owner source** D' theorem from `math-open-problems@e5f71d79.../FOURIER_ROUTE_REPORT.md` at an actual inequality. If either canonical three-volume orientation of `N` has maximum row marginal at most `2/3` (transpose if needed), then

`||p_Q||_infinity
 <=9 sqrt(3e) E_3(N)^(-1/6)
 <376.379.`                                                          (5.2)

This retains arbitrary same-side quadratic blocks and all outside couplings. It is a genuine full-ambient payment, not a density bound for a rotated surrogate. The D' branch also gives continuity.

If both orientations are concentrated, the account03/B19 r21 anchor argument applies verbatim to this physical cross block: an anchored four-colour packet has mass `>E_3(N)/12`. Combining it with own r23 pair-atom theorem, any nonanchor row-pair or column-pair atom of mass at least `1/4` is paid by

`||p_Q||_infinity
 <3 sqrt(e) (z_*/4608)^(-1/6)
 <138.086.`                                                          (5.3)

So the only unclosed `h=0` state is again an explicitly pair-diffuse anchored packet, now arising inside R1 with the much larger fixed cross-volume (5.1).

### 5.2 `h=1`: feed the completed q=1 overlap compiler

Suppose `Z_M^(1)>=z_*/3`. A term has row triple `{h,r1,r2}` and column triple `{h,c,k}`, with `k in R` and the four `L`-indices distinct. Randomly four-colour `L` into `H,R1,R2,C1`. The probability that `h` receives `H`, `c` receives `C1`, and the two residual rows split between `R1,R2` is `1/128`. Thus some deterministic colouring produces a q=1 packet of mass

`P1>=z_*/384.`                                                       (5.4)

Apply the completed account03/B08 r26 theorem `QFORM-Q1-AGGREGATE-DESHEAR-COMPILER-v1` to this **actual** packet. It yields one of

`boxed: B2*C2split >= z_*/1536
       =6.33629507846...*10^-9,}`                                   (5.5)

or a disjoint aggregate star-star-core packet

`boxed: F_core^2 sum_h K_h^2 R_h^2 >= z_*/24576
       =3.96018442404...*10^-10.}`                                  (5.6)

No shared coordinate is selected reciprocally; the whole q=1 mass is retained before the compiler fires.

### 5.3 `h=2`: feed the completed q=2 overlap compiler

Suppose `Z_M^(2)>=z_*/3`. A term is

`det A[{h1,h2,r},{h1,h2,k}]`.

Randomly three-colour `L` into `H1,H2,R`. The probability that the shared pair splits into `H1,H2` and the third row enters `R` is `2/27`. Hence some colouring has q=2 packet mass

`P2>=2z_*/81.`                                                       (5.7)

Apply account03/B08 r26 `QFORM-Q2-MONOMIAL-PACKET-COMPILER-v1`. One of its five fully original-coordinate aggregate energies satisfies

`boxed: E2j>=2z_*/2025
       =9.61239431162...*10^-9.}`                                   (5.8)

This is again a quantitative aggregate packet, not one tiny local minor.

## 6. Exact low-rank endpoint stress and why it does not license perturbative deletion

The low-compound alternative is real, not an artifact. Let `L,R` be disjoint original-coordinate banks, choose orthonormal `q,w` on `L` and a unit `r` on `R`, and set

`A=q r^T+r q^T+w w^T`                                                (6.1)

in block notation. Its nonzero spectrum is exactly `{-1,1,1}`. Taking diffuse Walsh-type `q,w,r` over large physical banks makes every physical coefficient arbitrarily small, so the family lies in any fixed N3 threshold once the banks are large enough. Here the R1 tail is exactly zero and

`b=0`, `D=ww^T`, `Z_q(C)=0`.

The completed account03/B09 theorem `QFORM-TWO-BANK-TRANSVERSE-RANKONE-CURVATURE-v1` applies directly to the actual quadratic variable

`Q=2(q^T X_L)(r^T X_R)+(w^T X_L)^2`

because the `R`-bank scalar is genuinely independent of the `(q,w)` pair from `L`; it gives

`boxed: ||p_Q||_infinity<17.086.}`                                  (6.2)

Thus the exact rank-one-compression endpoint is paid. What remains in Corollary 3.1 is a **nonzero** low-rank residual together with the actual R1 tail and arbitrary self curvature. The live correction against law-uniform coefficient perturbation prevents inferring a uniform bound merely by saying these matrices are close to (6.1).

## 7. Updated conditional end-to-end graph

The strongest correction-safe graph is now:

1. full target -> fixed `N3(2^-20)` by the completed Claude no-pivot reduction;
2. account03/B19 r21 -> D'-paid diffuse branch or R1/R2/R3;
3. r23 -> R1 has order-one transverse slope/compression; R3 pair-atomic endpoint paid;
4. **new r24 R1 compiler:** on the transverse R1 side, either
   - `Z_q(C)<g^2/4096`, which forces the explicit near-rank-one / near-two-dimensional geometry of Corollary 3.1; or
   - `Z_q(C)>=g^2/4096`, in which case the actual cross tail either forces `e_2(C^2)>3.38790039`, or an actual mixed third-minor tensor of mass `>=z_*` survives;
5. surviving mixed mass is then forced into exactly:
   - a genuine disjoint cross-volume branch, paid by D' unless it becomes the already-recognized pair-diffuse anchored state;
   - the q=1 aggregate currencies (5.5)-(5.6); or
   - one of the q=2 aggregate currencies (5.8).
6. R2 from account03/B19 r21 remains an independent branch.

No full-proof claim is made. The graph still has multiple conditional receivers, and there are not two independent end-to-end reviews.

## 8. First unpaid implication after this run

The first R1 gap can now be stated more sharply as

`QFORM-N3-R1-LOWCOMPOUND-ABSORPTION-v1`:

> Fix `tau=2^-20`, `g=589/1180`, `kappa=1/64`. There exists a universal finite `C` such that for every dimension, every `A in N3(tau)` with `s_3(A)>=1`, and every account03/B19-r21 R1 cut
> 
> `A[L,R]=sigma q r^T+E`, `sigma>4/5`, `||E||_F<1/590`,
> 
> if on an r23 transverse side `C` one has
> 
> `Z_q(C)=e_2((P_(q^perp)C)(P_(q^perp)C)^T)<g^2/4096`,
> 
> then `X^TAX` has density cap at most `C` for every independent cap-one product input law, with the nonzero cross tail `E`, all same-side curvature, all signs and all extra spectrum retained.

By Corollary 3.1, the hypothesis has only two source-valid geometries: a compression within operator distance `1/64` of rank one, or a slope block whose transverse compression is within Frobenius distance `sqrt(2)/64` of a rank-one matrix aligned with the slope. The exact rank-one-square boundary is paid by (6.2); the missing step is a nonperturbative receiver for the nonzero residual.

If this low-compound implication is paid, the next R1 debts are exactly the tail-cancellation second-compound branch (4.6), the q=1/q=2 aggregate packets, and the pair-diffuse anchored cross packet; R2 and residual R3 still remain afterward.

## 9. Verification

`VERIFY.py` checks the exterior identity exactly on a rational deterministic matrix and checks every displayed numerical threshold. The saved output ends

`QFORM_B19_R24_TRANSVERSE_COMPOUND_CHECK_PASS`.

The verification is only a regression; the proofs above are exact.
