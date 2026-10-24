SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T04:10:58Z.
attacking: weak-to-uniform closure of a paid density height after an independent original-coordinate smoothing block, with continuity proved only downstream of the central L-infinity estimate.

# account01/B15 — weak-height closure and a same-height C0 compactness compiler

Programme: `QFORM-DENSITY-3EIG-20260922` (programme revision `2026-09-22.5`).  
Owner-control revision consumed: `2026-09-22.15`.  
Status: `NEW_SUPPORTING_REGULARITY_THEOREM / PARTNER_APPLIED / FULL_QFORM_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and live corrections

The unrestricted owner target remains OPEN. This report proves a target-level regularity/closure lemma and applies the latest completed designated-partner result `account02/B15` at an actual owner-target inequality. It does not claim the missing universal height theorem.

All conditioning and independence statements below refer only to disjoint ORIGINAL-coordinate blocks. Nothing assumes independence after an orthogonal/spectral rotation. No law-uniform pointwise quadratic Fourier decay is used. No projection/X-ray-only argument is used to pay the full output height. Continuity is never used to manufacture an L-infinity estimate: the height is paid first, then an independent absolutely-continuous block upgrades regularity with the identical constant.

The designated partner result used below is source-pinned at

`yspennstate/math-open-problems@dbd7533d035ea02a097cf9ff573e9a5d65038f7a`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T030155Z-account02-B15-auto11-62cf32/REPORT.md`.

At the exact scope used here, it proves for arbitrary independent cap-one `X,Y,U,V`

`R = 4XY + U^2 + 2UV + (1/4)V^2`

that

`||p_R||_infinity <= M_* := 2+3 log 2 = 4.0794415416...`,                 (1.1)

and records the rough-input one-sheet tent inequality

`E[(epsilon-|R-y|)_+ 1_{R>=-(3/4)V^2}] <= pi epsilon^2`              (1.2)

for every `epsilon>0` and `y in R`. Its matrix eigenvalues are

`2, -2, (5+sqrt(73))/8, (5-sqrt(73))/8`,                            (1.3)

so exactly three have modulus at least one.

## 2. Height is weakly closed

For a probability measure `mu` on `R`, write `mu <= M dx` when `mu(E)<=M|E|` for every Borel set `E`.

### Lemma 2.1 — weak lower closure of a height certificate

Suppose `mu_n => mu` weakly and each `mu_n` has a density `p_n` with

`||p_n||_infinity <= M`.                                           (2.1)

Then `mu` is absolutely continuous, with a density `p` satisfying

`||p||_infinity <= M`.                                             (2.2)

Proof. For every bounded open interval `I`, Portmanteau gives

`mu(I) <= liminf_n mu_n(I) <= M |I|`.                              (2.3)

By countable disjoint decomposition this extends to open sets, and outer regularity extends it to all Borel sets. Hence `mu<=M dx`; Radon-Nikodym gives (2.2). QED.

This is an essential-height statement only. It does not imply uniform convergence of densities and does not imply a continuous representative.

## 3. New theorem: weak convergence becomes uniform after one fixed independent AC smoother

The following is the main new regularity lemma of this run.

### Theorem 3.1 — `QFORM-WEAK-HEIGHT-TO-UNIFORM-C0-v1`

Let `mu_n=>mu` be probability measures on `R`. Assume every `mu_n` has density `p_n` with the common height bound

`||p_n||_infinity <= M`.                                           (3.1)

Let `g` be any probability density in `L^1(R)`. Then Lemma 2.1 gives a density `p` of `mu` with `||p||_infinity<=M`, and

`boxed( ||p_n*g - p*g||_infinity -> 0. )`                          (3.2)

Moreover every `p_n*g` and `p*g` lies in `C_0(R)` and

`boxed( ||p_n*g||_infinity <= M,  ||p*g||_infinity <= M. )`        (3.3)

Thus a paid essential density height plus one genuinely independent absolutely-continuous additive resource converts mere weak convergence of the paid output laws into UNIFORM convergence of their continuous density representatives, with zero loss in the height constant.

There is also a quantitative approximation form. Define the bounded-Lipschitz metric by

`d_BL(mu,nu)=sup{|int h d(mu-nu)| : ||h||_infinity + Lip(h) <=1}`.   (3.4)

For every `phi in C_c^1(R)`,

`boxed(
 ||p_n*g-p*g||_infinity
 <= 2M ||g-phi||_1
    +( ||phi||_infinity+||phi'||_infinity ) d_BL(mu_n,mu).
)`                                                                   (3.5)

Since weak convergence of probability measures is equivalent to `d_BL->0`, and `C_c^1` is dense in `L^1`, (3.2) follows.

#### Proof

By Lemma 2.1, choose the Radon-Nikodym density `p` of `mu` with `||p||_infinity<=M`.

Fix `phi in C_c^1`. For every `x`, put

`h_x(y)=phi(x-y)`.

Uniformly in `x`,

`||h_x||_infinity + Lip(h_x)
 <= ||phi||_infinity+||phi'||_infinity.`                           (3.6)

Therefore

`sup_x |int phi(x-y) d(mu_n-mu)(y)|`

`<= (||phi||_infinity+||phi'||_infinity)d_BL(mu_n,mu).`            (3.7)

For the approximation error, both densities are bounded by `M`, hence

`||(p_n-p)*(g-phi)||_infinity`

`<= ||p_n-p||_infinity ||g-phi||_1`

`<=2M||g-phi||_1.`                                                 (3.8)

Adding (3.7) and (3.8) proves (3.5). Given `eta>0`, first choose `phi` so that the first term is below `eta/2`; then use `d_BL(mu_n,mu)->0` to make the second below `eta/2`. This proves (3.2).

Because `p_n,p,g` all lie in `L^1`, the standard `L^1*L^1 subset C_0` theorem yields the continuity and vanishing at infinity. Finally Young's `L^infinity*L^1` inequality gives

`||p_n*g||_infinity <= ||p_n||_infinity ||g||_1 <=M`,             (3.9)

and likewise for `p*g`. QED.

### Corollary 3.2 — varying smoothing law

Under the assumptions of Theorem 3.1, let `g_n` be probability densities with

`||g_n-g||_1 ->0`.                                                 (3.10)

Then

`boxed( ||p_n*g_n-p*g||_infinity ->0, )`                           (3.11)

and every density in (3.11) lies in `C_0` with height at most `M`.

Indeed,

`||p_n*g_n-p*g||_infinity`

`<= M||g_n-g||_1 + ||p_n*g-p*g||_infinity`.                       (3.12)

This is useful when the independent smoothing coordinate itself is regularized.

### Corollary 3.3 — a compactness compiler for an independent original-coordinate block

Let `R_n=>R` be any sequence of real random variables whose laws have densities bounded by one common `M`. Let `H` be independent of every `R_n` and of `R`, with any absolutely continuous law having probability density `g` (no boundedness or continuity of `g` is assumed). Then

`p_{R_n+H} -> p_{R+H}` uniformly,                                  (3.13)

all these densities are in `C_0`, and all have height at most `M`.

For quadratic forms this is product-structure safe whenever `R_n` and `H` are functions of disjoint ORIGINAL-coordinate blocks.

## 4. Why the independent smoother is doing real work

Weak convergence plus a common density cap does NOT imply uniform convergence of densities.

For integer `n>=1`, set

`p_n(x) = [1/2 + (1/4) sin(pi n x)] 1_[0,2](x)`.                  (4.1)

Then every `p_n` is a probability density and

`1/4 <= p_n <=3/4`.                                                (4.2)

By the Riemann-Lebesgue lemma,

`p_n(x)dx => (1/2)1_[0,2](x)dx =:p(x)dx`,                         (4.3)

but

`boxed( ||p_n-p||_infinity =1/4 for every n. )`                    (4.4)

Thus one may pass a height certificate through weak convergence, but one cannot pass pointwise or uniform density information for free. Theorem 3.1 identifies a clean sufficient additional resource: a fixed independent `L^1` smoothing law. This is a regularity-interface obstruction, not a counterexample to QFORM.

The theorem also deliberately gives no law-uniform modulus of continuity: for each fixed `g`,

`||tau_h(p*g)-p*g||_infinity <= M ||tau_h g-g||_1 ->0,`           (4.5)

but cap-one quadratic pushforwards `g` can themselves have arbitrarily fine rough structure, so no universal rate is asserted.

## 5. An exact tent certificate for bounded density

The partner's rough-input estimate (1.2) naturally fits the following exact characterization, which is useful because every test function is bounded and continuous and hence survives weak limits without assuming output continuity.

Let

`T_epsilon(u)=(epsilon-|u|)_+`,

so

`int_R T_epsilon(u)du=epsilon^2`.                                  (5.1)

### Lemma 5.1 — `QFORM-TENT-HEIGHT-CERTIFICATE-v1`

For a finite positive Borel measure `nu`, the following are equivalent:

(i) `nu<=M dx`;

(ii) for every `y in R` and `epsilon>0`,

`int T_epsilon(x-y) dnu(x) <= M epsilon^2`.                       (5.2)

Proof. `(i)=>(ii)` follows immediately from (5.1). Conversely let

`k_epsilon=T_epsilon/epsilon^2`.

Then `k_epsilon` is a probability approximate identity and (5.2) says

`nu*k_epsilon <=M` pointwise. For every nonnegative `psi in C_c(R)`,

`int psi(y)(nu*k_epsilon)(y)dy <= M int psi(y)dy`.                 (5.3)

Fubini rewrites the left side as

`int (psi*k_epsilon)(x)dnu(x)`,

which tends to `int psi dnu` as `epsilon downarrow0`. Thus

`int psi dnu <=M int psi dx`

for every nonnegative compactly supported continuous `psi`, hence `nu<=M dx`. QED.

Consequently the height property is encoded by a family of weakly continuous tests. Again, this certifies an essential `L^infinity` bound, not continuity.

## 6. Designated partner result applied at an actual inequality

Take independent cap-one variables `X,Y,U,V,W` and define

`R=4XY+U^2+2UV+(1/4)V^2`,

`Q=R+W^2`.                                                         (6.1)

The latest completed account02/B15 theorem gives the actual height inequality (1.1):

`||p_R||_infinity <= M_*=2+3log2`.                                (6.2)

Because `W` has an absolutely continuous law and the critical point of `w->w^2` is a one-point null set, `W^2` has an `L^1` probability density `g_W`. The variables in `R` and `W` are disjoint original coordinates and therefore genuinely independent. Applying Theorem 3.1 / Young's inequality gives

`boxed(
 p_Q in C_0(R),
 ||p_Q||_infinity <=2+3log2=4.0794415416... .
)`                                                                   (6.3)

No fixed-matrix continuity theorem is needed for this particular extension: the new independent coordinate supplies the entire `C_0` upgrade after the partner has paid the height.

The matrix of `Q` is the partner's four-dimensional block direct-summed with `[1]`; hence its spectrum is

`2, -2, (5+sqrt73)/8, (5-sqrt73)/8, 1`.                           (6.4)

Thus (6.3) is an actual owner-target inequality (indeed four eigenvalues have modulus at least one).

The new stability content is stronger than (6.3). Suppose cap-one product inputs `(X_n,Y_n,U_n,V_n)` converge coordinatewise weakly to cap-one limits `(X,Y,U,V)`. Independence passes to the product limit, and the polynomial map is continuous, so

`R_n=>R`.                                                          (6.5)

The partner theorem pays every `R_n` by the SAME `M_*`. Keeping one fixed independent cap-one `W`, Theorem 3.1 yields

`boxed(
 ||p_{R_n+W^2}-p_{R+W^2}||_infinity ->0,
 \quad
 sup_n ||p_{R_n+W^2}||_infinity <=2+3log2.
)`                                                                   (6.6)

So this owner-target chamber is closed under arbitrary weak cap-one source approximation in a genuinely uniform density topology once the independent square is retained.

The partner's one-sheet tent estimate is also an exact application of Lemma 5.1. If

`nu(E)=P{R in E, R>=-(3/4)V^2}`,                                   (6.7)

then (1.2) and Lemma 5.1 give directly

`boxed( nu<=pi dx. )`                                              (6.8)

This conclusion uses neither output continuity nor a smooth-input approximation. If an independent AC block is subsequently convolved with this submeasure, the resulting subdensity is in `C_0` and retains height `pi`.

## 7. Absolute continuity, bounded density, and continuous density are distinct layers

The exact logical hierarchy for this assignment is now:

- Qualitative absolute continuity: if the joint input law is absolutely continuous and `A!=0`, then `X^TAX` is absolutely continuous. The critical set `ker A` is a proper null subspace, and coarea away from it sends one-dimensional null target sets to null preimages. This needs neither rank three nor the cap-one condition.

- Essential boundedness: this is the hard quantitative layer. It must be paid by a valid interval/tent/coarea/Schur/grouped receiver. Weak limits preserve a common paid height by Lemma 2.1 or, equivalently, by the tent certificates in Lemma 5.1.

- Continuous density: a bounded density need not be continuous. But if a paid bounded component is convolved with any genuinely independent AC original-coordinate block, the full density lies in `C_0` with the identical height. Theorem 3.1 strengthens this to uniform `C_0` stability under weak perturbations of the paid component.

No implication in the reverse direction is being assumed.

## 8. Remaining connection to full QFORM

The new compiler does not solve the global owner target because a general symmetric matrix with `s_3(A)>=1` need not split in original coordinates into a dimension-free paid component plus an independent additive AC block. Cross-couplings between the potential smoothing coordinates and the receiver prevent the direct convolution representation. Conditioning those couplings away and then taking a worst-fibre supremum would run into the live conditional-cap and projection/X-ray corrections.

The missing global step therefore remains structural: aggregate the diffuse/high-dimensional spectral resource in original product coordinates before reciprocal local-minor payment, or produce a coupled receiver whose height is uniform under `s_3(A)>=1`. Once such a universal height receiver is paid, the regularity layer is substantially easier: weak lower closure preserves the height, and any genuine independent AC residue produces a same-height `C_0` density and even uniform stability under weak approximation.

This run therefore narrows B15's role: continuity and weak-source closure are not the obstruction. The obstruction remains the universal L-infinity payment itself in the fully coupled aggregate regime.
