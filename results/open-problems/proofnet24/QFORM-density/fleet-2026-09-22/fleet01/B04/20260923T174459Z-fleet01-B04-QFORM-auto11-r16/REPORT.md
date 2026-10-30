SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T17:44:59Z.
attacking: fractionalize the grouped projected-crossing product-Fourier argument so the one-hub/two-volume receiver survives row marginals above 1/2, and test it on a fully dense rotated indefinite form.

# fleet01/B04 r16 — fractional grouped projected-crossing Fourier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T174459Z-fleet01-B04-QFORM-auto11-r16`  
Status: `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture is **not proved** here. The new theorem proves a continuous `C_0` density in its stated original-coordinate grouped-crossing scope.

## 1. Fresh controls, corrections and the first attempted implication

Fresh owner control is `math-research-brain@72038b4bc2ab4c369014cff17eeb8efc17973188`, continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, revision `2026-09-22.15`: QFORM remains the sole target. The current claim ledger still marks the full density theorem and full-target continuity OPEN.

The current Claude continuation actually read is

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

at

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

Its newest open interface rewrites a small cross term as a "hub that sees P" and isolates the maximal functional `(SP)`. I attempted that first. The ordinary grouped-hub Plancherel step cannot simply be inserted there: after replacing `X_h` by `Y=X_h+eps P`, the conditional hub density is capped by one but depends on the light variables through `P`; the independence needed to push the hub phase to an `L^2` complex density is gone. The current source itself records that the corresponding maximal functional can grow on comb examples. I therefore do **not** use `(SP)` as a premise and do not claim that branch closed.

The mechanism change in this run stays on the same target: fractionalize the source-valid grouped projected-crossing theorem before any such dependent-hub replacement.

The theorem being extended is the complete written supporting result

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

at

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its q=1 weighted-subset lemma requires projected-crossing row marginals at most `1/2`. The new calculation below removes that fixed `1/2` threshold by combining finite-measure Jensen with the same exact product-space determinant identity.

The live corrections were refreshed. No post-rotation independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, positive conditional projection-cap moment, worst-fiber supremum, fixed good minor, or deletion of a nonzero small quadratic tail is used.

## 2. Setup

Use the grouped-crossing notation of the source theorem. Let `X_H` and `X'` be independent. Let `U` have `k` orthonormal columns in the hub coordinate space and put

`W=U^T X_H`,

with density cap `M_H`. The light vector `X'` has independent scalar coordinates with densities at most one. Consider

`Q=F(X_H)+2 <W, B X' + beta>+R(X')`,                         (2.1)

where `F` is arbitrary measurable and `R` is an arbitrary quadratic polynomial.

Split the light coordinates into disjoint original-coordinate banks `I,J`. Assume `B_J` has row rank `k`, and let

`S=product of the k singular values of B_J`.                    (2.2)

Let

`C=(A_R)_[I,J] (I-Pi_row(B_J))`.                               (2.3)

Fix an integer `ell>=1` with

`Z_ell=e_ell(CC^T)>0`.                                         (2.4)

For each physical `ell`-row set `T subset I` put

`d_T=det(C_T C_T^T)`,

and use the canonical volume law

`w_T=d_T/Z_ell`.                                                (2.5)

Let

`alpha_i=P_w(i in T)`,                                         (2.6)

and define the exact subset-entropy factor

`E(w)=exp{ [ H(w)+sum_i alpha_i log alpha_i ]/2 }`.             (2.7)

As usual `0 log 0=0`. Entropy subadditivity implies

`E(w) <= exp(ell/2)`,                                           (2.8)

but the exact factor will be retained.

## 3. New fractional weighted-subset estimate

Let `D=X_J-X_J*` be the independent-copy difference appearing in the source L2 decoupling, and let `kappa` be any nonnegative probability density on `R^k`. For the source row vectors `a_i`, define

`I_t=E[ kappa(B_J D) prod_i |psi_i(2t<a_i,D>)| ]`.              (3.1)

### Lemma 3.1 — `QFORM-FRACTIONAL-WEIGHTED-SUBSET-v1`

Let `q>=1` and suppose

`alpha_i <= q/2` for every active row.                          (3.2)

Then for `t!=0`,

`I_t <= 2^(k/2+ell/(2q)) (2pi)^(ell/q)
        * q^(-ell/(2q)) S^(-1) Z_ell^(-1/(2q))
        * E(w)^(1/q) |t|^(-ell/q).`                             (3.3)

#### Proof

Put

`m=E kappa(B_J D)`.

Every coordinate of `D` has a density bounded by one. The orthogonal product-projection theorem followed by the singular-value scaling of `B_J` gives

`m <= 2^(k/2)/S`.                                               (3.4)

Finite-measure Jensen/Hölder gives

`I_t^q <= m^(q-1)
          E[kappa(B_JD) prod_i |psi_i(2t<a_i,D>)|^q].`           (3.5)

Apply weighted Holder with the canonical subset weights `w_T`. Since

`sum_(T contains i) w_T = alpha_i`,

we get

`E[kappa prod_i |psi_i|^q]
 <= prod_T K_T^(w_T)`,                                         (3.6)

where

`K_T=E[kappa(B_JD)
       prod_(i in T)|psi_i(2t<a_i,D>)|^(q/alpha_i)].`            (3.7)

Condition (3.2) says `q/alpha_i>=2`, precisely the range of the sharp scalar Fourier integral. Write each source row as

`a_i=c_i+lambda_i B_J`,

with `c_i` in the orthogonal complement of `row(B_J)`. The joint vector

`(B_JD,(<c_i,D>)_(i in T))`

has density at most

`2^((k+ell)/2)/(S sqrt(d_T))`.                                  (3.8)

This is the same determinant product-projection identity as in the source theorem. Shift the last `ell` coordinates by the `lambda_i` terms, integrate `kappa`, and use

`int_R |psi_i(2ty)|^(q/alpha_i) dy
 <= (2pi/|t|) sqrt(alpha_i/q)`.                                 (3.9)

Therefore

`K_T <= [2^((k+ell)/2)(2pi)^ell]
        /[S |t|^ell q^(ell/2) sqrt(d_T)]
        * prod_(i in T) sqrt(alpha_i).`                          (3.10)

Taking the weighted geometric mean gives the exact canonical determinant/entropy identity

`prod_T d_T^(-w_T/2) prod_i alpha_i^(alpha_i/2)
 = Z_ell^(-1/2) E(w)`.                                         (3.11)

Thus

`E[kappa prod |psi_i|^q]
 <= [2^((k+ell)/2)(2pi)^ell]
    /[S |t|^ell q^(ell/2) sqrt(Z_ell)] * E(w).`                 (3.12)

Combine (3.4), (3.5), and (3.12), then take the q-th root. The powers of `S` collapse exactly to `S^(-1)`, and the powers of two collapse to `2^(k/2+ell/(2q))`. This is (3.3). QED.

The point of (3.5) is structural: it spends some decay exponent in exchange for a larger admissible marginal window, without ever changing to dependent spectral coordinates.

## 4. Fractional grouped projected-crossing theorem

The source grouped-hub Plancherel step is unchanged:

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k I_t`.                           (4.1)

Put

`D_q=kq+ell`.                                                    (4.2)

Then (3.3) gives

`|phi_Q(t)| <= min(1,K_q |t|^(-D_q/(2q)))`,                     (4.3)

where the coefficient is the exact product of the factors above. If

`D_q>2q`,                                                        (4.4)

the power is integrable.

### Theorem 4.1 — `QFORM-FRACTIONAL-GROUPED-PROJECTED-CROSSING-v1`

Under (2.1)--(2.7), let `q>=1` satisfy (3.2) and (4.4). Then the full ambient quadratic form has a continuous density vanishing at infinity, and

`boxed:
||p_Q||_infinity
 <= [D_q/(D_q-2q)]
    2^((kq+3ell)/(2D_q)) q^(-ell/(2D_q))
    M_H^(q/D_q) S^(-q/D_q)
    Z_ell^(-1/(2D_q)) E(w)^(1/D_q).`                            (4.5)

Moreover

`boxed: integral_R |phi_Q(t)|dt <= 2pi * RHS(4.5).`             (4.6)

#### Proof

From (3.3) and (4.1), before the `|t|` power,

`K_q = M_H^(1/2) pi^(k/2)
       2^(k/4+ell/(4q)) (2pi)^(ell/(2q))
       q^(-ell/(4q)) S^(-1/2)
       Z_ell^(-1/(4q)) E(w)^(1/(2q)).`                          (4.7)

Let `b=D_q/(2q)>1`. Exact integration gives

`int_R min(1,K_q |t|^-b)dt
 = 2b/(b-1) K_q^(1/b).`                                        (4.8)

Fourier inversion divides by `2pi`. The power of `pi` in `K_q^(1/b)` is exactly one and cancels. Collecting the remaining exponents gives (4.5). The same integrable envelope proves (4.6) and the `C_0` representative. QED.

### Checks against the source theorem

At `q=1`, `D_q=k+ell`. Replacing the exact `E(w)` by (2.8) turns (4.5) into

`[(k+ell)/(k+ell-2)]
 2^((k+3ell)/(2(k+ell))) exp(ell/(2(k+ell)))
 M_H^(1/(k+ell)) S^(-1/(k+ell)) Z_ell^(-1/(2(k+ell))),`

which is exactly the current grouped-crossing theorem `(GC)`.

For one hub and two projected crossing directions (`k=1,ell=2`), condition (4.4) becomes simply

`q<2`.                                                          (4.9)

Thus **every non-coloop canonical two-volume law** (`alpha_*<1`) is admissible: choose

`max(1,2 alpha_*) <= q <2`.                                    (4.10)

The old fixed `alpha_*<=1/2` gate is therefore not structural. An exact coloop remains an endpoint, naturally routed by promoting that row to the hub bank and using the two-hub/one-crossing theorem.

## 5. Explicit genuinely rotated indefinite stress matrix

Take four left-bank and four right-bank original coordinates and the physical cross block

`M = [[ 1,   1,   1,   1],
      [3/2, 3/2,-1/2,-1/2],
      [3/2,-1/2, 3/2,-1/2],
      [3/2,-1/2,-1/2, 3/2]].`                                  (5.1)

Every cross coefficient is nonzero. Use the first left coordinate as the one-dimensional hub. Its row is

`w=(1,1,1,1)`, so `S=||w||=2`.                                 (5.2)

For the other three rows, projection away from `span(w)` gives

`c_1=(1,1,-1,-1)`,
`c_2=(1,-1,1,-1)`,
`c_3=(1,-1,-1,1)`.                                              (5.3)

These are pairwise orthogonal with squared norm four. Therefore

`CC^T=4 I_3`,
`Z_2=e_2(CC^T)=48`.                                             (5.4)

The three two-row squared volumes are all `16`, so the canonical two-volume law is uniform on the three pairs. Hence

`alpha_1=alpha_2=alpha_3=2/3`.                                 (5.5)

The source q=1 projected-crossing theorem is unavailable, because `2/3>1/2`. The new theorem applies at the sharp endpoint

`q=4/3`.                                                        (5.6)

Here

`H(w)=log 3`,
`sum_i alpha_i log alpha_i =2 log(2/3)`,

so

`E(w)=2/sqrt(3)`.                                               (5.7)

Substituting `k=1`, `ell=2`, `q=4/3`, `S=2`, `Z_2=48`, `M_H=1`, and (5.7) into (4.5) simplifies exactly to

`boxed: ||p_Q||_infinity <= 5 / 2^(1/5)
       =4.3527528164806206956... .`                             (5.8)

Also

`boxed: integral |phi_Q(t)|dt <= 10 pi / 2^(1/5)
       =27.3491525422956... .`                                  (5.9)

Thus this branch gives a continuous `C_0` density for every admissible product input law.

### Full target-valid dense symmetric matrix

Put

`A_* = [[J_4/100, M],
        [M^T,     J_4/100]].`                                   (5.10)

Every physical entry of `A_*` is nonzero. It is indefinite and non-diagonal in the independent coordinates.

For the cross block, the row Gram matrix is

`MM^T = [[4,2,2,2],
         [2,5,1,1],
         [2,1,5,1],
         [2,1,1,5]].`                                          (5.11)

Two eigenvalues are `4`; the remaining two are the eigenvalues of

`[[4,2 sqrt(3)],[2 sqrt(3),7]]`,

namely

`(11+sqrt(57))/2`, `(11-sqrt(57))/2`.                           (5.12)

Since `sqrt(57)<8`, every singular value of `M` is strictly larger than `sqrt(3/2)`. Therefore the zero-self-block symmetric matrix has four positive and four negative eigenvalues of modulus greater than `sqrt(3/2)`. The perturbation in (5.10) has operator norm `1/25`, so Weyl gives four positive and four negative eigenvalues with modulus at least

`sqrt(3/2)-1/25 >1`.                                           (5.13)

Hence (5.10) satisfies the owner's exact three-large-eigenvalue hypothesis with substantial room. The within-bank blocks are retained by Theorem 4.1, not discarded as convolution noise. Equations (5.8)--(5.9) therefore apply directly to `X^T A_* X`.

## 6. Designated partner fleet02/B04 applied to an actual inequality

The latest completed designated-partner theorem available at publication refresh is

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

from

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`.

For (5.1), the squared singular values are

`4,4,(11+sqrt(57))/2,(11-sqrt(57))/2`,

and the last two have sum `11` and product `16`. Therefore

`E_3(M)=16*11 + 8*16 =304`.                                    (6.1)

There are only four physical rows. Every probability law on three-row sets has row-marginal sum three, so at least one row marginal is at least `3/4`. Thus no supported third-volume law has all row marginals strictly below `3/4`, exactly the partner theorem's support-defect hypothesis. Its rank-four/four-row branch gives, for the same ambient matrix,

`boxed: ||p_(X^T A_* X)||_infinity
 <= 6 * 4^(1/6) * 304^(-1/6)
 = 6 * 76^(-1/6)
 =2.9152937283842089... .`                                     (6.2)

The partner certificate is numerically stronger on this particular four-row form. That does not duplicate the new theorem: (4.5) removes the `1/2` marginal barrier inside the arbitrary-rank grouped projected-crossing mechanism, whereas (6.2) pays the special exact four-row third-volume support defect by conditioning/exact-rank exits. Equation (6.2) is the required actual use of the designated partner result.

## 7. Structural consequence and remaining implication

For `k=1,ell=2`, the current grouped-crossing route formerly split at `alpha_*=1/2`. The new theorem moves that analytic endpoint all the way to the true integrability boundary `alpha_*=1`:

- if `alpha_*<1`, choose `q<2` with `alpha_*<=q/2` and use (4.5);
- if `alpha_*=1`, the two-volume row matroid has a coloop, and that physical row can be promoted to a second hub, entering the already completed two-hub/one-crossing cascade.

The quantitative near-coloop constant still deteriorates as `q ->2`, so the next useful optimization is not another support theorem. It is

`QFORM-FRACTIONAL-PROJECTED-CROSSING-NEARCOLOOP-SPLICE-v1`:

choose the switch point between (4.5) and physical promotion to a second hub so that both the determinant currency and the marginal-gap cost remain uniformly controlled under the actual compound-hub geometry supplied by the global routing workers. This must retain arbitrary same-bank curvature, outside couplings and all nonzero cross tails.

Separately, the dependent "hub that sees P" statement `(SP)` from the current Claude continuation remains open. The present theorem does not silently treat that dependent hub as independent.

The full QFORM conjecture and the full-target continuity statement remain **OPEN**.

## 8. Integrity

No Gaussianity, moments, log-concavity, compact support, connected support, spectral-coordinate independence, pointwise oscillatory decay, arbitrary-joint coarea estimate, conditional-density positive moment, histogram extremality, or deletion of a nonzero quadratic tail is used. The only numerical decimals evaluate exact closed forms. Scheduler/task state, email/push settings, public visibility, paid model/API use, cross-account authentication and permissions were not changed. Repository transport remains distinct from verified native learned-memory ingestion; status is `WITHOUT_VERIFIED_BRAIN`.
