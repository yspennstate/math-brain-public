SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T14:23:52Z.
attacking: approximate invariant-subspace shielding for arbitrary-magnitude internal spectral updates plus a genuinely dense small tail.

# account02/B12 — approximate invariant spectral shield with arbitrary internal spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T142352Z-account02-B12-QFORM-auto11`.
Assignment: Additional eigenvalue control.
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**.
Execution-memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result and exact scope

The new result is `QFORM-APPROX-INVARIANT-SPECTRAL-SHIELD-v1`.

Let `P` be an orthogonal projection, `Q=I-P`, and let `B=B^T`. Put

`beta = ||Q B Q||op`,
`eta  = ||Q B P||op`.

Let `T=T^T` be an arbitrary, possibly full-rank, dense perturbation with

`||T||op <= delta`,

and set `A=B+T`. For a threshold `a>beta+delta`, let

`Pi = 1_{|A|>=a}`

be the spectral projection of the **actual final matrix**. Then

`||Q Pi||op <= sqrt(2) (eta+delta)/(a-beta-delta)`.                    (1.1)

Consequently, if `mu=max_i P_ii`, then every original coordinate obeys

`sqrt(Pi_ii) <= sqrt(P_ii) + sqrt(2)(eta+delta)/(a-beta-delta)`,       (1.2)

and hence

`max_i Pi_ii <= [sqrt(mu)+sqrt(2)(eta+delta)/(a-beta-delta)]^2`.      (1.3)

There is **no restriction at all on `P B P`**: arbitrary rank, arbitrary signs/inertia, arbitrary internal mixing, and arbitrarily large norm are allowed. In particular an arbitrary symmetric spectral update `S=P S P` costs zero in (1.1)-(1.3). The only non-shielded quantities are the complementary block `Q B Q`, the cross leakage `Q B P`, and the final dense matrix tail `T`.

This strictly extends the preceding exact-reducing shield theorem, which was the special case `eta=0`.

## 2. Proof of the shield theorem

Write the final matrix in the orthogonal decomposition `ran P direct_sum ran Q` as

`A = [[C,F^T],[F,D]]`,

so

`||D||op <= beta+delta =: b`,
`||F||op <= eta+delta =: eps`.

Assume `b<a`.

Let

`Pi_+ = 1_[a,infinity)(A)`,
`Pi_- = 1_(-infinity,-a](A)`.

On the positive high-spectral subspace `H_+=ran Pi_+`, let `A_+` denote the restriction of `A`; then `A_+>=a I`. For `X_+=Q Pi_+ : H_+ -> ran Q`, the eigen-subspace identity `A Pi_+=Pi_+ A` gives the exact Sylvester equation

`D X_+ - X_+ A_+ = - F P Pi_+`.                                    (2.1)

Because `spec(D) subset [-b,b]` and `A_+>=aI`, the separated-spectrum integral

`X_+ = integral_0^infinity e^{tD} F P Pi_+ e^{-tA_+} dt`

converges in operator norm and solves (2.1). Therefore

`||X_+||op <= integral_0^infinity e^{bt} eps e^{-at} dt
            = eps/(a-b)`.                                         (2.2)

Apply the same argument to `-A`; its positive high-spectral subspace is `ran Pi_-`, its complementary block is `-D`, and its cross block is `-F`. Hence

`||Q Pi_-||op <= eps/(a-b)`.                                      (2.3)

The domains `ran Pi_+` and `ran Pi_-` are orthogonal. For `x=x_++x_-+x_0` in the orthogonal spectral decomposition,

`||Q Pi x||
 <= [eps/(a-b)] (||x_+||+||x_-||)
 <= [sqrt(2) eps/(a-b)] sqrt(||x_+||^2+||x_-||^2)`.

Thus (1.1) follows.

For an original coordinate vector `e_i`,

`sqrt(Pi_ii)=||Pi e_i||
 <= ||Pi P e_i|| + ||Pi Q e_i||
 <= sqrt(P_ii) + ||Pi Q||op
 = sqrt(P_ii) + ||Q Pi||op`,

which proves (1.2)-(1.3). QED.

Important point: this is a deterministic matrix statement. No random variable is rotated, and no claim is made that a small matrix tail gives a small random quadratic error on unbounded inputs.

## 3. QFORM compiler through the completed spectral-window theorem

Use the completed ridge-window theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

It states: if a symmetric final matrix has at least three eigenvalues of modulus at least one, and the spectral projection `Pi=1_{|A|>=1/64}` satisfies

`max_i Pi_ii <= 1/32`,

then for arbitrary independent cap-one input densities the quadratic form has a continuous `C_0` density with

`||p_Q||infinity <= 288 sqrt(3e)/13 < 64`.                         (3.1)

Therefore the new shield theorem gives the following direct compiler. If

`beta+delta < 1/64`,

`[sqrt(mu)+sqrt(2)(eta+delta)/(1/64-beta-delta)]^2 <= 1/32`,        (3.2)

and the **actual final matrix** has at least three eigenvalues of modulus at least one, then (3.1) holds.

The arbitrarily large block `PBP` never enters (3.2).

## 4. Exact target-class family with only three protected directions

This family shows that the theorem handles genuinely arbitrary added spectrum and nonzero cross leakage even when a five-volume exit can disappear.

Let `m` be a Sylvester-Hadamard order, let `h_1,...,h_d` be orthonormal Hadamard columns in `R^m`, and assume

`m >= 64 d`.

On the two original-coordinate banks `R^m direct_sum R^m`, define

`g_k = (h_k,h_k)/sqrt(2)`,
`P = projection onto span{g_1,...,g_d}`.

Every original coordinate has

`P_ii = d/(2m) <= 1/128`.                                        (4.1)

Protect only the first three modes and let

`E = span{g_1,g_2,g_3}`,
`W = span{g_4,...,g_d}`,

`A_0 = 4 P_E + 2 P_W`.

Now take an **arbitrary** symmetric operator `Theta` on `W` and put

`S = P_W Theta P_W`.

Before any leakage is introduced, this literally replaces all `d-3` baseline eigenvalues `2` on `W` by the completely arbitrary eigenvalues of `2I_W+Theta`; they may have either sign, cross zero, mix, and have unbounded magnitude.

Choose unit vectors `w in W`, `q in ran(P)^perp`, and add a nonzero nonseparable leakage

`H = eta (w q^T + q w^T)`,
`eta = 1/4096`.

Finally add **any** symmetric dense matrix `T` with

`||T||op <= delta = 1/4096`.

Set `B=A_0+S+H`, `A=B+T`. Then

`Q B Q = 0`,
`||Q B P||op = eta`,

while `g_1,g_2,g_3` remain exact `+4` eigenvectors of `B`. Hence Weyl gives

`lambda_3^downarrow(A) >= 4-delta > 1`,                            (4.2)

so every member is in the exact owner target class.

At `a=1/64`, (1.3) gives

`max_i Pi_ii
 <= [1/sqrt(128) + sqrt(2)*(2/4096)/(1/64-1/4096)]^2
 = [sqrt(2)/16 + 2sqrt(2)/63]^2
 = 9025/508032
 = 0.0177646289997... < 1/32`.                                  (4.3)

Therefore

`||p_{X^T A X}||infinity
 <= 288 sqrt(3e)/13
 = 63.2640518778...`                                             (4.4)

uniformly over every `Theta`, every cap-one product source, and every allowed dense `T`.

This family can have only the three protected cross singular directions: taking `Theta=-2I_W` removes the entire baseline `W` cross block. Thus a fixed five-volume lower bound is not present, whereas the approximate spectral shield remains valid.

## 5. Required e5f71d79... application: a real D5 inequality

The pinned source package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed `D_5` theorem in the Fourier report says that for an actual original-coordinate cross block `M`, with

`Z_5=e_5(M^T M)`, one has

`||p_Q||infinity <= 5 sqrt(2e) Z_5^(-1/10)`                       (5.1)

with **no marginal condition**, while all self blocks and outside couplings remain arbitrary.

Apply it to the sibling of Section 4 with five protected modes: use

`E_5=span{g_1,...,g_5}`,
`W=span{g_6,...,g_d}`,
`A_0=4P_{E_5}+2P_W`,

and retain the same arbitrary `Theta` on `W`, the same `eta=1/4096` off-shield leakage, and the same arbitrary dense `||T||op<=1/4096`.

Across the two physical banks, before `H+T` the five protected Hadamard directions give five orthogonal cross singular directions of size exactly `2`; the arbitrary `Theta` packet is supported on the orthogonal `W` modes and cannot cancel them. The cross compression of `H+T` has norm at most `eta+delta=1/2048`. Hence

`s_5(M_final) >= 2-1/2048`,

so

`Z_5 >= (2-1/2048)^10`.                                          (5.2)

Substituting (5.2) into the completed e5f theorem gives the actual final-matrix inequality

`||p_Q||infinity
 <= 5 sqrt(2e)/(2-1/2048)
 = 5.83053342407...`.                                            (5.3)

No post-rotation independence is used. This D5 branch is stronger on the deliberately five-protected sibling; Section 4 explains why the new shield remains useful when only three protected directions survive.

## 6. Required latest account03/B12 partner application

The latest designated partner result read this run is

`yspennstate/math-open-problems@c09e907f60e1c8819becc9254f8f512c3d3e6ff2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T134701Z-qform-eigenvalue-r34/REPORT.md`.

Its `QFORM-ERODED-SPECTRAL-PROFILE-STABILITY-v1` theorem says that if an original-coordinate reference cross block `B_0` is perturbed by `E`, the first `r` singular directions of `E` may be completely arbitrary, while the residual threshold `beta=s_{r+1}(E)` erodes the baseline profile by

`u_j=(s_{r+j}(B_0)-beta)_+`.

Its participation-rank corollary gives, with

`S_2=sum u_j^2`, `S_4=sum u_j^4`, `S_2^2>4S_4`,

`||p_Q||infinity
 <= (3sqrt(3e)/2) S_2^(5/2)/(S_2^2-4S_4)^(3/2)`.                (6.1)

Apply this to a separate exact target-class stress family. Let `I,J` each have `m=r+10` original coordinates and take

`A_0 = [[0,2I_m],[2I_m,0]]`.

Add **any** symmetric rank-`r` matrix `S` of arbitrary signs and arbitrarily large norm, then any symmetric dense `T` with

`||T||op <= 1/4`.

For the final cross update `E=(S+T)[I,J]`, the rank-`r` part can be removed exactly, so

`s_{r+1}(E) <= 1/4`.                                             (6.2)

Since `s_j(B_0)=2`, the ten certified eroded singular values are

`u_1=...=u_10=7/4`.                                             (6.3)

Substitution into (6.1), or equivalently the partner's flat-profile specialization with `k=10`, gives

`||p_Q||infinity
 <= 3*10*sqrt(3e)/(2*6^(3/2)*(7/4))
 = (10/7) sqrt(e/2)
 = 1.66545998686...`.                                           (6.4)

This family is also inside the exact global target: rank-`r` interlacing gives

`s_3(A_0+S) >= s_{r+3}(A_0)=2`,

and the dense tail gives

`s_3(A_0+S+T) >= 7/4 > 1`.                                     (6.5)

Thus (6.4) is a genuine partner theorem application to arbitrary-magnitude added spectrum plus a dense tail, not a copied citation.

## 7. Why the dense-tail step is matrix-level only

Nothing above treats `X^T T X` as a uniformly small random error. That principle is false for the allowed unbounded product laws: even for `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`,

`X^T T X = delta X_1^2 >= delta R^2`

almost surely. The new theorem instead controls the spectral projector of the **actual final matrix** through block geometry, and the probabilistic receiver remains in original coordinates.

## 8. First unpaid implication

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem pays a substantially larger stability class than the exact-shield result: arbitrary internal spectrum is still magnitude-free even when the shield is only approximately invariant and is then hit by an arbitrary dense tail. What remains unpaid is structural:

> From bare `s_3(A)>=1` in the no-pivot survivor, force either (i) a diffuse approximate spectral shield with universal `mu,beta,eta` satisfying (3.2), (ii) an eroded cross profile with participation rank `>4` as in account03/B12, (iii) an actual D5/three-volume/collective-tail certificate, or (iv) an already-paid hub/ridge/grouped-bank/physical-pair/physical-triple/Schur exit.

The known singleton-plus-two-bank and diffuse exact-rank-three corrections prevent simply asserting one uniformly good bounded physical core or one rank-three cross cut. This run does not claim that final extraction.

## 9. Sources and correction discipline


Corrections preserved: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint three-dimensional coarea bound; no dimension-free worst fiber-supremum step; no positive moment of the worst conditional projection cap; no universal single good physical minor/cross-rank-three extraction; and no small-matrix-norm-to-small-random-quadratic-error inference. None is used here.

A local deterministic sanity check sampled 1000 random symmetric block matrices with `||D||op<=0.2`, `||F||op=0.05`, threshold `a=0.5`; it found zero violations of (1.1). This is only a check of the proved algebra, not proof evidence for the conjecture.
