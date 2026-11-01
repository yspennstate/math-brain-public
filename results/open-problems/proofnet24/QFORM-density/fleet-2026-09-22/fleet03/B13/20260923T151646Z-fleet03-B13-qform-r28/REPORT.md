SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T15:16:46Z.
attacking: eliminate the rank-four cross-misalignment term in the diffuse retained-range branch by conditioning all outside original coordinates, then quantify the only surviving low-spectral obstruction directly under the bad slab.

# fleet03/B13 r28 — diffuse-range arbitrary-cross theorem and transverse slab anti-concentration

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATIONS / FULL QFORM OPEN / FULL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

Programme: `QFORM-DENSITY-3EIG-20260922`.  Role: extremal product laws.  No rotation of the random coordinates is used.

## 1. Source-pinned inputs actually used

### 1.1 Exact diffuse-range Fresnel/BL theorem

Source:

`yspennstate/math-open-problems@9d9e2369ad137664a48b1b7c6d682ddaed62bcad`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T125929Z-fleet01-B13-qform-auto23/FRESNEL_RANGE_ADDENDUM.md`.

Its Theorem B.1 says: if `R` is a symmetric physical leaf matrix of rank `d>=3`, its range projection `P_R` has maximum physical-coordinate leverage at most `1/2`, and every cross row lies in `range(R)`, then, allowing arbitrary physical diagonal twists and arbitrary affine leaf coefficients, the corresponding output has a continuous density and

`||p||_inf <= M(R) := [4d/(d-2)] |pdet(R)|^(-1/d)`.              (1.1)

The proof is uniform in every affine coefficient. In particular its `U`-bank may be empty.

### 1.2 Designated partner fleet04/B13

Source:

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T121154Z-fleet04-B13-nonattained-bathtub-r1/REPORT.md`.

Theorem 3.1 there proves, with no attainment assumption, that for every nonnegative measurable product kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 = sup_{|E_i|=1} int_{prod_i E_i} K`.                              (1.2)

The sets on the right may be approximated by bounded finite interval unions, but their diameter and fragment count are not uniformly bounded. This is the product-law purification used below at an actual slab inequality.

The same report also proves that a slab ratio `rho` forces every disjoint physical cross block to obey

`s_5(B) <= 10 sqrt(2e)/rho`.                                     (1.3)

I record (1.3) for compatibility, but the main theorem below shows that this rank-four cross compression is **not needed at all in the diffuse retained-range branch**.

### 1.3 New high-leverage complement available concurrently

Fleet02/B13 source:

`yspennstate/math-open-problems@6d77eb1e452afcd8c4f779344b5602118223d42a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T145505Z-fleet02-B13-leveragecascade-r29/REPORT.md`.

It proves that a five-deep leverage cascade at spectral scale `tau`, once `rho>16 sqrt(60 pi)/tau`, forces a physical third-volume row-column bi-hub; otherwise leverage peeling terminates after at most four physical centers or the residual retained rank drops below three. I use this only to state the final complement; it is not a premise of the diffuse proof.

## 2. First missing implication: the cross-row inclusion can be deleted by physical conditioning

The row-inclusion condition in (1.1) is unnecessary whenever the coefficients outside the selected leaf bank come from disjoint **original coordinates**, because those coordinates can simply be conditioned.

### Theorem 2.1 — `QFORM-DIFFUSE-RANGE-ARBITRARY-OUTSIDE-CROSS-v1`

Let `V=(V_1,...,V_m)` be independent real random variables with densities bounded by one. Let `W` be any random vector independent of `V` (in the QFORM application, `W` is the disjoint bank of all remaining original coordinates). Let

* `R` be a real symmetric `m x m` matrix of rank `d>=3`;
* `P` be the orthogonal projection onto `range(R)` and `max_j P_jj<=1/2`;
* `D` be an arbitrary real diagonal `m x m` matrix;
* `b(W)` be any measurable `R^m`-valued function;
* `F(W)` be any real measurable function.

Then

`Y = V^T(R+D)V + b(W)^T V + F(W)`                              (2.1)

has a **continuous** density and

`boxed: ||p_Y||_inf <= M(R)
 = [4d/(d-2)] |pdet(R)|^(-1/d).`                                (2.2)

In particular, an arbitrary physical cross matrix from `W` into `V` is allowed; no row-space alignment with `range(R)` is required.

#### Proof

Fix `W=w`. The conditional law is

`Y_w = V^T(R+D)V + b(w)^T V + F(w)`.                             (2.3)

Apply the pinned Theorem B.1 with its `U`-bank empty and with the affine coefficients equal to the fixed vector `b(w)`. Its proof gives not merely the density bound but the uniform characteristic-function estimate

`|phi_w(t)| <= psi_R(t)
 := min{1, (4 pi)^(d/2)|pdet(R)|^(-1/2)|t|^(-d/2)}`.             (2.4)

Crucially, the right side is independent of `w`, of `b(w)`, of `F(w)`, and of every diagonal twist in `D`.

Averaging the conditional characteristic functions,

`phi_Y(t)=E[phi_W(t)]`, hence `|phi_Y(t)|<=psi_R(t)`.             (2.5)

Because `d>=3`, `psi_R in L1(R)`. Fourier inversion therefore gives a continuous density. If `alpha=d/2` and

`K=(4 pi)^(d/2)|pdet(R)|^(-1/2)`,

then

`int_R min(1,K|t|^-alpha) dt
 = 2 alpha/(alpha-1) K^(1/alpha)`.                               (2.6)

Dividing by `2 pi` gives exactly

`||p_Y||_inf <= 4d/(d-2)|pdet(R)|^(-1/d)`.                      (2.7)

All conditioning is on disjoint original coordinates. No transformed coordinates are asserted independent. QED.

### Actual fleet04/B13 purification application

For fixed `R,D,b,F` and an interval `I`, take the nonnegative kernel

`K_I(v,w)=1_{ {v^T(R+D)v+b(w)^Tv+F(w) in I} }`.                 (2.8)

For unit product indicators, (2.2) gives

`int K_I prod_i 1_{E_i} <= M(R)|I|`.                             (2.9)

Apply the designated partner's exact no-attainment identity (1.2) to this **specific** slab kernel. It transfers (2.9), with zero constant loss, to every admissible cap-one product law. Thus no single interval, centered uniform law, optimizer, support diameter, or bounded fragment count is being assumed. Continuity in Theorem 2.1 comes from the uniform `L1` characteristic-function envelope, not from purification.

## 3. Spectral truncation: exact model with no cross leakage term

Now take any selected original-coordinate leaf bank `V` inside a full QFORM polynomial, condition all other original coordinates into `W`, and let its actual symmetric leaf block be `C`.

For `tau>0`, define the physical spectral projection and retained matrix

`P_tau = 1_{ {|C|>=tau} }`,
`R_tau = P_tau C P_tau`,
`E_tau = C-R_tau`.                                                (3.1)

These are deterministic matrices. We never replace the random variables by spectral coordinates. We have

`E_tau=P_tau^perp E_tau P_tau^perp`,
`||E_tau||_op <= tau`.                                           (3.2)

Let `d_tau=rank(P_tau)`. Assume

`d_tau>=3`, `max_j (P_tau)_jj<=1/2`.                             (3.3)

The earlier r27 compiler paid a term involving the outside cross leakage `||B(I-P_tau)||`. Theorem 2.1 shows that term was unnecessary: **all outside cross interactions can be retained exactly as conditional affine coefficients**.

For any `z in range(P_tau)^perp`, define the exact model polynomial

`Q_z := Q -(V-z)^T E_tau(V-z)`.                                  (3.4)

Expanding only the leaf terms, `Q_z` has retained quadratic curvature `R_tau`, while the removed residual contributes the affine term `2(E_tau z)^T V-z^TE_tau z`. Every outside cross term of `Q` is otherwise unchanged. Hence Theorem 2.1 applies to `Q_z` and gives a continuous density with

`||p_{Q_z}||_inf <= M_tau
 := [4d_tau/(d_tau-2)] |pdet(R_tau)|^(-1/d_tau).`                 (3.5)

Since every retained eigenvalue has modulus at least `tau`,

`|pdet(R_tau)|^(1/d_tau)>=tau`, and therefore

`M_tau <= [4d_tau/(d_tau-2)]/tau <= 12/tau`.                     (3.6)

This is an exact model theorem: there is no `rank<=4` cross approximation and no discarded cross residual.

## 4. Direct geometric slab inequality: transverse anti-concentration

Let `J` be any interval of length `L>0`, put

`S={Q in J}`, `rho=P(S)/L`.                                      (4.1)

For `r>=0` and `z in range(P_tau)^perp`, define the transverse physical event

`G(z,r)={ ||P_tau^perp V-z||_2 <= r }`.                          (4.2)

On `G(z,r)`, by (3.2),

`|Q-Q_z|
 = |(P_tau^perp V-z)^T E_tau(P_tau^perp V-z)|
 <= tau r^2`.                                                     (4.3)

Thus

`S cap G(z,r) subset {Q_z in J+[-tau r^2,tau r^2]}`.             (4.4)

The enlarged interval has length `L+2 tau r^2`. Applying (3.5) gives the following result.

### Theorem 4.1 — `QFORM-DIFFUSE-RANGE-SLAB-TRANSVERSE-ANTICONCENTRATION-v1`

Under (3.3), for every center `z in range(P_tau)^perp` and every `r>=0`,

`boxed:
 P(G(z,r) | S)
 <= [M_tau/rho] (1+2 tau r^2/L),`                                (4.5)

whenever `P(S)>0`.

Using only the retained eigenvalue threshold,

`boxed:
 sup_z P(||P_tau^perp V-z||<=r | Q in J)
 <= 12/(tau rho) + 24 r^2/(rho L).`                              (4.6)

This is a geometric sublevel-set inequality for the actual bad slab. It has no support radius, moment, compactness, connectedness, Gaussian/log-concavity, or fragment-count hypothesis.

#### Proof

By (4.4) and (3.5),

`P(S cap G(z,r)) <= M_tau(L+2tau r^2)`.                          (4.7)

Divide by `P(S)=rho L`. Then use (3.6). QED.

## 5. Quantile form and a target-level diffuse-branch obstruction

For `0<eta<1`, define the conditional transverse quantile radius

`r_{tau,eta}(S)
 := inf{ r>=0 : exists z in range(P_tau)^perp with
                  P(G(z,r)|S)>=1-eta }`.                         (5.1)

This is finite for every probability law: the conditional distribution of the finite-dimensional vector `P_tau^perp V` is tight. No finite moment is asserted or needed.

Apply (4.5) to any feasible `r>r_{tau,eta}(S)` and pass down to the infimum. Then

`boxed:
 rho <= [M_tau/(1-eta)]
        (1+2 tau r_{tau,eta}(S)^2/L).`                           (5.2)

At `eta=1/2`, using (3.6),

`boxed:
 rho <= 24/tau + 48 r_{tau,1/2}(S)^2/L.`                         (5.3)

Consequently,

`rho>24/tau
 => r_{tau,1/2}(S)^2 >= (L/48)(rho-24/tau)`,                     (5.4)

and in particular

`rho>48/tau
 => r_{tau,1/2}(S)^2 > rho L/96`.                               (5.5)

### Full-target specialization

Take `V=X` to be **all original coordinates**, `C=A`, and `tau=1`. The hypothesis of the conjecture guarantees `d_1>=3`. If the high-spectral projection

`P_1=1_{ {|A|>=1} }`                                             (5.6)

is coordinate-diffuse, `max_j(P_1)_jj<=1/2`, then every slab obeys

`boxed:
 rho <= 24 + 48 r_{1,1/2}(S)^2/L.`                              (5.7)

Thus a hypothetical counterexample sequence with `rho->infinity` in the diffuse high-spectral branch is forced into an explicit geometry:

`r_{1,1/2}(S)^2/L -> infinity`, in fact at least linearly in `rho`. (5.8)

This removes the previous `rank<=4 cross misalignment` obstruction from the diffuse branch entirely. The only surviving defect here is genuine slab-conditioned spread in the **low-spectral physical projection**.

## 6. Complementary high-leverage branch

If (5.6) is not diffuse, the new fleet02/B13 leverage cascade applies directly at `tau=1`: above slab ratio

`16 sqrt(60 pi)=219.669895887304...`,                            (6.1)

five unresolved high-leverage centers cannot survive without producing a physical third-volume row-column bi-hub. Otherwise the retained projection becomes diffuse after at most four physical centers or its retained rank falls below three.

Therefore the global obstruction can now be stated more sharply:

* **diffuse retained range:** no rank-four cross-misalignment payment is needed; high slab ratio forces the transverse anti-concentration (4.6)/(5.8);
* **high-leverage retained range:** leverage is localized into at most four physical centers, a rank-below-three endpoint, or a quantitative physical third-volume bi-hub.

The first B13 obligation after this run is

`QFORM-TRANSVERSE-SPREAD-TO-PHYSICAL-CERTIFICATE-v1`:

> Use the original product/extremal-set structure to turn the forced conditional low-spectral spread (4.6) into an already-paid square/pair/bordered/hub certificate, or prove a new dimension-free slab payment. Remote fragments are allowed and may pair with different regions of the other coordinates; no common-fiber overlap, finite moment, support diameter, or fixed fragment count may be assumed.

## 7. What is and is not proved

**Proved here:**

1. the exact diffuse-range continuous-density theorem tolerates arbitrary outside cross coupling after physical conditioning;
2. the spectral-truncation model therefore has no cross-row/rank-four misalignment error;
3. every bad slab in the diffuse branch satisfies the explicit transverse conditional anti-concentration inequalities (4.5)-(4.6) and quantile lower bounds (5.2)-(5.5);
4. fleet04/B13's no-attainment purification was applied to the actual model slab inequality with zero constant loss.

**Not proved:** the full QFORM conjecture. The transverse-spread alternative is not yet paid. Full continuity of the actual law is also not proved; continuity is proved only for the exact model `Q_z` and for Theorem 2.1's exact diffuse-range class.

No pointwise law-uniform van-der-Corput decay, post-rotation independence, arbitrary-joint coarea bound, conditional density cap, finite moment, bounded support, fixed fragment count, or interval extremality is used.