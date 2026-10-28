SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T05:18:47Z.
attacking: sharpen the multicarrier volume branch by promoting a physical E3 pair, then compare the optimized D/D' weights, pair-E4 partner receiver and direct ridge gate on one rank-four rotated crossing.

# account02/B04 r20 — pair-anchored E3 promotion and critical-volume separation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions.
Status: **PROVED SUPPORTING THEOREM / GLOBAL SAME-CROSSING WEIGHT OPTIMIZATION / PINNED D,D' APPLIED / DESIGNATED PARTNER r48 APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full unrestricted theorem remains open. This run does not infer a target-scale physical E3 crossing from the bare spectral hypothesis. It proves a sharper pair-localized Fourier receiver, identifies exactly what pair-E4 collapse means in coefficient geometry, and gives a genuinely rotated target-valid family where the pair receiver stays uniform while the pair-E4 and entropy-critical ambient routes deteriorate.

A completed marginal-free aggregate-E3 compiler already exists (account03/B02 r35). The theorem below is therefore not advertised as the first removal of all E3 marginal gates; it is a sharper **pair-anchored** receiver and a useful exact bridge for the multicarrier face analysis from B04 r19.

## 1. Source-pinned inputs and live corrections


Pinned source required by the owner:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` all read. I use its arbitrary-weight Theorem D and D' at explicit inequalities in Section 5 and its D5 theorem as a same-crossing obstruction check.

The physical grouped-crossing theorem used below is the checked checkpoint

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The exact-cross-rank Plancherel theorem is account03/B04 r32,

`yspennstate/math-open-problems@ae6229183a1be7e7a31df596e0710d4702b84649`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T105123Z-account03-B04-qform-auto11-r32/REPORT.md`.

The newest completed designated-partner result available during this run is account03/B04 r48,

`yspennstate/math-open-problems@085560dcfb3b90238f3e84dd2de7d0e09bfa7525`,

which proves `QFORM-PAIR-ANCHORED-E4-PROMOTION-v1`:

`||p_Q||_infinity <= 2^(17/8) H_ab^(-1/8)`.

The direct ridge comparison uses the completed ridge-window theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`.

## 2. Pair-anchored E3 is already a complete physical receiver

Let `I,J` be disjoint original-coordinate banks and

`M=A[I,J]`.

Write its physical rows as `m_r`. Fix distinct rows `a,b in I` and define

`D_2 = det Gram(m_a,m_b)`.

Assume the pair-anchored third-volume mass

`W_ab := sum_{r notin {a,b}} det Gram(m_a,m_b,m_r)`               (2.1)

is positive. Then `D_2>0`. Let `P_2` be orthogonal projection in coefficient space onto `span(m_a,m_b)` and put

`c_r=m_r(I-P_2)`, `C=(c_r)_{r notin {a,b}}`.

The Gram-Schur identity gives the exact aggregate factorization

`boxed: W_ab = D_2 E_1(C),   E_1(C)=sum_r ||c_r||^2.`             (2.2)

Define the residual one-volume row marginals

`alpha_r=||c_r||^2/E_1(C)`.

### Theorem 2.1 — `QFORM-PAIR-ANCHORED-E3-PROMOTION-v1`

For every independent cap-one product input and every ambient quadratic-plus-affine form carrying the literal crossing above,

`boxed: ||p_Q||_infinity <= 3*2^(5/6) W_ab^(-1/6).`              (2.3)

The branch has an integrable characteristic-function envelope, hence a continuous `C_0` density.

### Proof

Condition only original coordinates outside the displayed banks. This preserves independence and the density cap of all remaining source coordinates; all conditioned interactions become affine terms allowed by the cited receivers.

**Diffuse residual.** If every `alpha_r<=1/2`, keep the literal original coordinates `a,b` as two hubs. Their joint density cap is at most one. The hub-to-right-bank singular-value product is `sqrt(D_2)`. The projected light crossing is exactly `C`, its `ell=1` volume is `E_1(C)`, and its row marginals are the `alpha_r`. Apply the grouped projected-crossing theorem with `(k,ell,d)=(2,1,3)`. For `ell=1` its entropy factor cancels exactly:

`||p_Q||_infinity
 <= 3*2^(5/6) D_2^(-1/6) E_1(C)^(-1/6)
 = 3*2^(5/6) W_ab^(-1/6).`                                     (2.4)

**Heavy residual.** Otherwise choose `c` with `alpha_c>1/2`. The literal three-row Gram determinant is

`D_3=det Gram(m_a,m_b,m_c)=D_2||c_c||^2=alpha_c W_ab>W_ab/2`.    (2.5)

Condition the other left-bank source coordinates. The retained three literal rows form an exact-rank-three crossing to the right bank. On the three-coordinate side the projected density cap is one; on the other side the three-dimensional orthogonal projection of a cap-one product law has density cap at most `2^(3/2)`. Account03/B04 r32 therefore gives

`||p_Q||_infinity
 <=3 sqrt(2) D_3^(-1/6)
 <3*2^(2/3) W_ab^(-1/6)
 <3*2^(5/6) W_ab^(-1/6).`                                      (2.6)

Both source receivers have genuine Fourier `L^1` envelopes. QED.

This proof uses only literal original coordinates as promoted variables. No rotated random coordinate is called independent and no pointwise quadratic stationary-phase decay is used.

### Canonical-volume corollary

Let

`z_S=det Gram(m_r:r in S)`, `Z=sum_{|S|=3}z_S=e_3(M^TM)`

and let `alpha_i=P(i in S)` under the canonical law `z_S/Z`. Then

`W_ab/Z=P(a,b in S)>=alpha_a+alpha_b-1`.                         (2.7)

Hence whenever `alpha_a+alpha_b>1`,

`||p_Q||_infinity
 <=3*2^(5/6)[(alpha_a+alpha_b-1)Z]^(-1/6).`                     (2.8)

In particular, if two canonical row marginals are at least `3/4`,

`boxed: ||p_Q||_infinity <= 6 Z^(-1/6).`                         (2.9)

Thus, within the older D/D' carrier analysis, two simultaneous `3/4`-heavy rows are not an entropy obstruction at all: promote the pair physically and pay their incident aggregate before any reciprocal local minor is chosen.

For context, account03/B02 r35 already gives a marginal-free global estimate `10.5501688312... Z^(-1/6)` for every `Z>0`. Equation (2.9) is a sharper concentrated-pair specialization, not a replacement for that global theorem.

## 3. What collapse of pair-E4 actually implies

Let

`H_ab := sum_{R: |R|=4, {a,b} subset R} det Gram(m_r:r in R)`.

The same Gram-Schur factorization used by partner r48 gives

`H_ab=D_2 E_2(C)`.                                               (3.1)

Let `mu_1>=mu_2>=...>=0` be the squared singular values of `C`. Then

`S=sum mu_j=W_ab/D_2`,
`T=sum_{i<j}mu_i mu_j=H_ab/D_2`.                                 (3.2)

### Lemma 3.1 — `QFORM-PAIR-E4-COLLAPSE-RANK3-SKELETON-v1`

If

`4D_2 H_ab < W_ab^2`,                                            (3.3)

then the squared Frobenius tail after the largest residual singular direction satisfies

`boxed:
 sum_{j>=2} mu_j
 <= [W_ab-sqrt(W_ab^2-4D_2H_ab)]/(2D_2)
 <= 2H_ab/W_ab.`                                                 (3.4)

In particular, `H_ab=0<W_ab` forces `rank C=1` and hence `rank M=3`.

**Proof.** If `mu_1<=S/2`, then `sum mu_j^2<=mu_1 S<=S^2/2`, so `T=(S^2-sum mu_j^2)/2>=S^2/4`, contradicting (3.3). Thus `tau=S-mu_1<S/2`. Since

`T>=mu_1 tau=tau(S-tau)`

and the right side increases on `[0,S/2]`, solve the quadratic inequality for `tau`. The second inequality uses `1-sqrt(1-x)<=x`. QED.

This is a coefficient-matrix statement only. It is **not** used as a small-random-perturbation argument; arbitrary cap-one product inputs have no moments, so a small Frobenius tail cannot simply be deleted. The value of the lemma is structural: simultaneous large pair-E3 and tiny pair-E4 means “rank three plus a quantitatively small coefficient tail,” exactly identifying where a new rough-law stability mechanism would have to act. Theorem 2.1 avoids that stability debt whenever `W_ab` itself is large enough.

## 4. A dense rank-four stress family

Let `m=8`, choose four signs `s_r=+1` and four signs `s_r=-1`, and set

`R_{L,eps}` to have rows

`L e_1`, `L e_2`, and `m^(-1/2)(e_3+eps s_r e_4)`, `r=1,...,m`.

Right-multiply by the fixed dense orthogonal matrix

`V=(1/15)*[[14,-2,-3,-4],
           [-2,11,-6,-8],
           [-3,-6,6,-12],
           [-4,-8,-12,-1]]`,                                    (4.1)

and put

`M_{L,eps}=R_{L,eps} V^T`,
`A_{L,eps}=[[0,M_{L,eps}],[M_{L,eps}^T,0]]`.                     (4.2)

The integer matrix in (4.1) squares to `225 I`, so `V` is orthogonal. At the stress values

`L=64`, `eps=1/64`,                                                     (4.3)

all physical entries of `M` are nonzero: the two carrier rows use the first two dense rows of `V`, while each residual row is proportional to row 3 plus or minus `(1/64)` row 4, whose four coordinates are all nonzero.

Because the residual signs sum to zero,

`M^T M` is orthogonally similar to

`diag(L^2,L^2,1,eps^2)`.                                        (4.4)

Thus the singular values are

`L,L,1,eps`,                                                     (4.5)

and the symmetric pure-cross matrix has nonzero spectrum

`{+L,+L,+1,+eps,-eps,-1,-L,-L}`.                                (4.6)

For every `L>=1` this has six eigenvalues of modulus at least one. It is dense across the physical banks, non-diagonal in the independent coordinates, and indefinite.

## 5. Exact global optimization of every proved D/D' physical weight on this crossing

For a row triple `S`, put

`z_S=sum_{|T|=3} det(M_{S,T})^2=det Gram(M_S)`.

Classify a row triple by whether it contains carrier `a`, carrier `b`. Cauchy-Binet and the two residual directions give the exact face masses

`W_11=L^4(1+eps^2)`,
`W_10=W_01=L^2 eps^2`,
`W_00=0`.                                                        (5.1)

For (4.3),

`boxed: W_11=16781312, W_10=W_01=1, Z_3=16781314.`               (5.2)

The canonical carrier marginals are

`alpha_a=alpha_b=(W_11+W_10)/Z_3=0.9999999404099...`,            (5.3)

so the natural pinned D and D' laws are far beyond either marginal gate.

Now optimize **all supported physical 3x3-minor weights**, not merely the canonical law. Conditional on a row triple, Gibbs/log-sum optimization over the physical column triples replaces the individual determinants by `z_S`. Conditional on one of the three nonempty carrier faces, a second Gibbs/log-sum optimization replaces its row triples by the face mass `W_above`. Therefore only the three face probabilities remain.

For a proved D' row cap `h in [1/2,3/4)`, symmetry makes `q_10=q_01`. The two carrier caps imply

`q_11<=2h-1`.                                                    (5.4)

Here the unconstrained Gibbs mass of face 11 exceeds `1/2`, while `2h-1<1/2`, so strict concavity forces both carrier caps to saturate:

`q_11=2h-1`, `q_10=q_01=1-h`.                                   (5.5)

Inside face 11 each residual row is used with conditional marginal `1/m`; inside either one-carrier face it is used with conditional marginal `2/m`. Hence every residual physical row has final marginal

`alpha_res=(3-2h)/m<=1/4<h`,                                    (5.6)

so no hidden row constraint is active.

The exact global determinant-entropy currency at cap `h` is therefore

`boxed:
 G_h=
 (W_11/(2h-1))^(2h-1)
 (W_10/(1-h))^(2(1-h)),`                                       (5.7)

with the first factor interpreted by continuity at `h=1/2`.

Applying the pinned e5 D' theorem gives

`B_D'(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) G_h^(-1/6).`           (5.8)

Its logarithmic derivative is

`-1/(2h)+4/(3-4h)
 -(1/3) log[W_11(1-h)/(W_10(2h-1))]`,                           (5.9)

and the second derivative is

`1/(2h^2)+16/(3-4h)^2
 +(1/3)[1/(1-h)+2/(2h-1)]>0`.                                  (5.10)

So the minimizer is unique and global. At (4.3),

`boxed: h_*=0.5988522195374297...`,
`boxed: G_*=76.8825814570228...`,                               (5.11)

and the required pinned completed D' result yields the actual inequality

`boxed: ||p_Q||_infinity <= 7.250321030967945... .}`             (5.12)

At the original pinned Theorem-D cap `h=1/2`, the exact global physical weight has `q_11=0`, `q_10=q_01=1/2`, hence

`G_D=2`

and

`boxed: ||p_Q||_infinity <= 8.813061999824733... .}`             (5.13)

The pinned D5 theorem has `Z_5=0` on this same natural crossing because `rank M=4`; therefore it supplies no finite certificate on this crossing. This is a route obstruction on the displayed crossing, not a claim about every other cut of the ambient symmetric matrix.

Equations (5.12)-(5.13) are the required equation-level application of the pinned `e5f71d...` source.

## 6. Pair promotion, partner r48, and marginal-free E3 on the identical crossing

For the physical carrier pair,

`W_ab=W_11=L^4(1+eps^2)=16781312`.                              (6.1)

The new Theorem 2.1 therefore gives

`boxed: ||p_Q||_infinity <= 0.3340734272026694... .}`            (6.2)

For comparison, the completed marginal-free aggregate-E3 theorem of account03/B02 r35 gives, with `Z_3=16781314`,

`||p_Q||_infinity <=0.6593587122043184...`.                     (6.3)

The newest completed designated partner account03/B04 r48 applies positively on this same matrix. Its pair-anchored fourth-volume mass is

`H_ab=L^4 eps^2=4096`,                                          (6.4)

so

`boxed: ||p_Q||_infinity
 <=2^(17/8) 4096^(-1/8)
 =1.542210825407941... .}`                                      (6.5)

This is an actual use of the designated partner theorem, not only a citation.

As `eps->0`, (6.2) stays at scale `L^(-2/3)`, while (6.5) deteriorates like `eps^(-1/4)` and the ambient D/D' optimization becomes critical/infeasible because every supported E3 triple eventually contains both carrier rows. At the exact `eps=0` limit the crossing has rank three, and account03/B04 r32 sharpens the bound further to

`3 sqrt(2) L^(-2/3)`.                                           (6.6)

Thus physical pair promotion bridges the near-rank-three limit without using a rough-input perturbation argument.

## 7. Direct ridge is impossible at every scale on this same crossing

Write `g=gamma^2`. The ridge eigenvalues associated with (4.5) are

`k_L=L^2/(L^2+g)` twice,
`k_1=1/(1+g)`,
`k_eps=eps^2/(eps^2+g)`.                                        (7.1)

The two physical carrier rows have ridge leverage exactly `k_L`. Every residual row has leverage `(k_1+k_eps)/m`. Since `L>=1`, `eps<=1`, and `m=8`, the maximum physical ridge leverage is `k_L`. The ridge trace is

`theta=2k_L+k_1+k_eps<=4k_L`.                                  (7.2)

The completed direct ridge theorem requires `q>=1`, leverage `<=q/2`, and the strict integrability gate

`theta>2q`.                                                      (7.3)

But leverage forces `q>=2k_L`. If `k_L>=1/2`, then

`2q>=4k_L>=theta`.

If `k_L<1/2`, then `q>=1` gives

`2q>=2>4k_L>=theta`.

So (7.3) is impossible for every `gamma>0` and every admissible `q`. This is an exact same-crossing ridge obstruction, not a numerical failure to find a scale.

At the stress value (4.3), the certified hierarchy on this physical crossing is therefore

`boxed:
 0.334074  pair-anchored E3 promotion
 <0.659359 generic marginal-free E3
 <1.542211 partner pair-anchored E4
 <7.250322 globally optimized pinned D'
 <8.813062 globally optimized pinned D,
 while direct ridge has no admissible scale and D5 has Z5=0 on this crossing.`

## 8. What this actually changes and what remains unpaid

The run changes mechanism from the preceding three-carrier entropy dual. A concentrated pair should not be entropy-balanced if its incident E3 aggregate is available: promote the two literal coordinates and spend `W_ab` directly. The same calculation shows exactly why pair-E4 is secondary in the near-rank-three collar: `H_ab/W_ab` controls the residual coefficient tail, while the pair-E3 receiver does not divide by that tail.

The bare three-large-eigenvalue condition still does **not** force a target-scale literal cross `E3`; the live correction ledger contains explicit families where every coordinate cut has cross rank at most two. Therefore the first genuinely unpaid B04 implication is now:

`QFORM-LOW-E3-TO-RANK2-HUBSTAR-OR-OTHER-PAID-ENDPOINT-v1` — starting from the actual low-cross-E3 funnel left by the marginal-free compiler, use original-coordinate product geometry to obtain either (i) a target-scale pair-incident E3 packet paid by Theorem 2.1, or (ii) an actual rank-at-most-two / hub-star / square-bank / fixed-pair receiver. A merely small coefficient tail cannot be dropped under arbitrary rough unbounded inputs.

This is compatible with the current fleet synthesis, which has also narrowed the hard state toward low-rank crossings plus exceptional physical hub stars. Full QFORM remains open; continuity is proved only on the displayed Fourier branches.

## 9. Deterministic audit

`CHECKS.py` verifies exactly that the integer matrix in (4.1) is orthogonal after division by 15, that the stress matrix is physically dense, the face masses (5.2), the unique D' optimum and constants, the pair-E3/E4 comparison, and the all-scale ridge contradiction. Executed output marker:

`QFORM_B04_R20_PAIR_E3_CHECK_PASS`.
