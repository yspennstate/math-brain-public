SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T19:47:42Z.
attacking: reduce the physical square-energy requirement from six/seven protected modes to four by paying the rank-one self-block survivor with a scalar square peel plus a rank-two literal crossing.

# fleet03/B12 r40 — four-mode spectral-square carrier and signed-spectrum stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T194742Z-qform-eigenvalue-r40`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for the compiler as a whole**. The rank-three crossing exit is continuous `C_0`; the finite-core, physical-pair and square-peel exits used below establish essential boundedness only.

## 1. Target, corrections and source pins

The target remains: for independent real original coordinates with scalar probability densities bounded by one and an arbitrary real symmetric matrix `A` with `s_3(A)>=1`, prove a universal density cap for `X^T A X`, or produce a counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, post-rotation independence, or diagonal-basis assumption is made.

Fresh owner control was read on `math-research-brain/main`: programme `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.15`, no fleet03/B12 stop. The live correction inbox blob before publication is `6bdbd9987a4eefeba79d53915cfe7e232263f8ec`. In particular, this proof does not use law-uniform pointwise quadratic-phase decay, unrestricted joint-density coarea, a uniformly good single physical minor, or independence after rotating to eigen-coordinates.

Analytic inputs, at their proved scopes:

1. Projected-gradient finite-core receiver: `yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`. For an `m`-coordinate physical quadratic-plus-affine form with three actual singular values at least `sigma`, the conditional density cap is `2 sqrt(6 pi m)/sigma`.
2. Full-matrix physical-pair receiver used by fleet02/B12: `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`. For an invertible indefinite physical pair with determinant magnitude `D`, smallest singular value `kappa`, and global `s_3(A)>=s`, the density cap is `3*400^(1/3)*(D^2*kappa*s)^(-1/6)`.
3. Exact-rank crossing theorem: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. For a literal rank-`r>2` cross block of singular-product `S`, arbitrary same-side functions are allowed; with one side exactly `r` original coordinates the `r=3` cap is `3 sqrt(2) S^(-1/3)`.
4. Half-Riesz and outer-square peel, source-pinned through the current Fourier package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`: if `Q=a(X+h(V))^2+R(V)`, with `X` an original scalar independent of `V`, then `||p_Q||_infty <= |a|^(-1/2) H_{1/2}(R)`, and `H_{1/2}(R) <= (2 pi)^(-1/2) integral |t|^(-1/2)|phi_R(t)|dt`.
5. Designated partner fleet04/B12: `yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260923T191531Z-fleet04-B12-hybrid-square-defect-r7/REPORT.md`. Its hybrid two-profile theorem permits simultaneous commuting square losses, an arbitrary noncommuting destructive-square packet, a rank packet and a dense tail.

A fresh master-head check also found fleet02/B09's distinct `weak-fourth-mode stability` report at commit `9e1e4143471b51c63460be8d1f536c3da0b4d8c5`. That theorem concerns a diagonal-plus-strong-three-plus-weak-four decomposition. The theorem below is different: it starts from an **actual four-mode square-Gram carrier** and compiles it by an exhaustive self-rank/crossing split.

## 2. Deterministic square-energy spill

Let `H` be an ORIGINAL-coordinate set of size `m`, and write the actual final matrix in the physical split

`A = [[C,B],[B^T,D]]`,

where `C=A[H,H]` and `B=A[H,H^c]`. Then

`(A^2)[H,H] = C^2 + B B^T`.                                      (2.1)

Let `0<=G<=A^2` and suppose

`lambda_k(G[H,H]) >= g^2`.                                       (2.2)

If `c=s_{r+1}(C)<g`, then

`boxed: s_{k-r}(B) >= sqrt(g^2-c^2).`                            (2.3)

### Proof

Spectrally truncate the symmetric matrix `C` as `C=C_r+E`, where `rank C_r<=r`, `C_r E=0`, and `||E||op=c`. Hence

`C^2=C_r^2+E^2`, `0<=E^2<=c^2 I`.

By (2.1)-(2.2),

`B B^T + C_r^2 = (A^2)[H,H]-E^2 >= G[H,H]-c^2 I`.

Therefore its `k`-th eigenvalue is at least `g^2-c^2`. A positive rank-`r` update can move at most `r` eigenvalues past a threshold, so

`lambda_{k-r}(BB^T) >= lambda_k(BB^T+C_r^2) >= g^2-c^2`.

Taking square roots proves (2.3). QED.

This identity is entirely in the final deterministic matrix. It does not regard any added quadratic part as an independent random convolution.

## 3. A new rank-one self-block shear lemma

The six-mode compiler previously paid a nearly rank-one self block by preserving five cross singular directions. The new point is that **three** cross singular directions suffice before one scalar square peel: after eliminating the scalar pivot, two cross directions survive and can be spent by the exact-rank-two crossing plus half-Riesz estimate.

Let `C=C^T` satisfy

`s_1(C)>=c`, `s_2(C)<b`,                                         (3.1)

where

`0<b<c/m`.                                                       (3.2)

Write

`C=lambda u u^T+E`, `|lambda|=s_1(C)`, `||E||op=s_2(C)<b`,      (3.3)

with `u` unit. Choose an ORIGINAL coordinate `i in H` with

`|u_i|>=1/sqrt(m)`.                                               (3.4)

Put

`a_0=C_ii`, `K=H\{i}`.                                           (3.5)

Then

`boxed: |a_0| >= alpha:=c/m-b>0.`                                (3.6)

Indeed `|a_0|>=|lambda|u_i^2-b>=c/m-b`.

For the cross block `B`, let `B_i` be row `i` and `B_K` the remaining rows. Completing the square in the literal original scalar `X_i` replaces the residual `K`-to-`H^c` cross block by

`B' = B_K - eta B_i`,
`eta = C_{K,i}/a_0`.                                              (3.7)

The shear parameter obeys

`boxed: ||eta|| <= L := (c/sqrt(m)+b)/(c/m-b).}`                 (3.8)

### Proof of (3.8)

Put `t=|lambda|>=c` and `r=|u_i|>=1/sqrt(m)`. From (3.3),

`||C_{K,i}|| <= t r + b`,
`|a_0| >= t r^2-b`.

Thus

`||eta|| <= (tr+b)/(tr^2-b)`.                                    (3.9)

On the domain `t>=c`, `r>=1/sqrt(m)`, `tr^2>b`, the right side decreases in both `t` and `r`: its `t`-derivative has numerator `-b r(1+r)`, and its `r`-derivative has numerator `-t^2 r^2-tb(1+2r)`. Therefore its maximum occurs at `t=c`, `r=1/sqrt(m)`, giving (3.8). QED.

Define

`ell(rho)=(sqrt(rho^2+4)-rho)/2`.                                (3.10)

After permuting row `i` first, the shear matrix

`T_eta=[[1,0],[-eta,I]]`                                         (3.11)

satisfies

`T_eta B = [B_i ; B']`,
`sigma_min(T_eta)=ell(||eta||)>=ell(L)`.                         (3.12)

Hence for every `j`,

`s_j(T_eta B)>=ell(L)s_j(B)`.                                    (3.13)

Deleting the first row and using singular-value interlacing gives the key estimate

`boxed: s_2(B') >= s_3(T_eta B) >= ell(L) s_3(B).}`              (3.14)

This is the missing rank budget: a scalar Schur elimination consumes exactly one cross singular direction, with an explicit shear loss but no stochastic approximation.

## 4. Two volume-extraction identities

We will use Cauchy-Binet only on literal row subsets.

### Three rows

If `s_3(B)>=d`, then

`e_3(BB^T) >= s_1(B)^2 s_2(B)^2 s_3(B)^2 >= d^6`.

Since

`e_3(BB^T)=sum_{|I|=3} det(B_I B_I^T)`,                           (4.1)

for `N_3=binom(m,3)` some ORIGINAL triple `I` satisfies

`S_3(B_I):=sqrt(det(B_I B_I^T)) >= d^3/sqrt(N_3).`              (4.2)

### Two rows after the scalar peel

If `s_2(B')>=d'`, then with `N'=binom(m-1,2)`,

`e_2(B'B'^T)>=d'^4`,

so some ORIGINAL pair `I subset K` satisfies

`S_2(B'_I):=sqrt(det(B'_I B'_I^T)) >= d'^2/sqrt(N').`           (4.3)

No assertion about independence of singular coordinates is made: the row subsets are original physical coordinates.

## 5. Main theorem — four square modes suffice on a bounded physical carrier

Let `A=A^T` satisfy

`s_3(A)>=s>0`.                                                    (5.1)

Let `H` be an ORIGINAL-coordinate set of size `m>=4`, write `C=A[H,H]`, `B=A[H,H^c]`, and suppose there is a PSD certificate

`0<=G<=A^2`, `lambda_4(G[H,H])>=g^2`                             (5.2)

for some `g>0`.

Put

`N_2=binom(m,2)`, `N_3=binom(m,3)`, `N'=binom(m-1,2)`.          (5.3)

Choose parameters

`0<a<b/N_2`, `0<b<c/m`, `0<c<g`.                                (5.4)

Define

`kappa=b/N_2-a`, `alpha=c/m-b`,                                 (5.5)

`L=(c/sqrt(m)+b)/alpha`, `l=ell(L)`,                            (5.6)

`d_0=sqrt(g^2-c^2)`, `d_1=sqrt(g^2-b^2)`.                       (5.7)

### Theorem 5.1 — `QFORM-FOUR-MODE-SPECTRAL-SQUARE-CARRIER-v1`

Under (5.1)-(5.7), for every independent cap-one product input and arbitrary affine terms,

`boxed:
||p_(X^TAX+linear)||_(infinity,ess)
 <= max{
   2 sqrt(6 pi m)/a,
   pi/kappa,
   3*400^(1/3) kappa^(-5/6) s^(-1/6),
   3 sqrt(2) N_3^(1/6)/d_0,
   2^(11/4) N'^(1/8) / sqrt(alpha*l*d_1)
 }.`                                                             (5.8)

Every additional eigenvalue of the final matrix, of either sign and arbitrary magnitude, remains present. The theorem assumes no decomposition of the law into an independent `main form + remainder`.

### Proof

There are four exhaustive regimes.

#### Case I: three self modes

If

`s_3(C)>=a`,                                                      (5.9)

condition on all ORIGINAL coordinates outside `H`. Exterior couplings become arbitrary affine terms in the `m` untouched independent coordinates. The finite-core projected-gradient theorem gives

`||p_Q||_infinity <= 2 sqrt(6 pi m)/a`.                           (5.10)

#### Case II: approximate rank two self block

Suppose

`s_3(C)<a`, `s_2(C)>=b`.                                         (5.11)

The rank-two Pluecker extraction used in the six-mode compiler is recalled briefly. Let `C_2=lambda_1 uu^T+lambda_2 vv^T` contain the two largest absolute eigenvalues. The residual has operator norm `<a`. Since

`sum_{i<j}(u_i v_j-u_j v_i)^2=1`,

some ORIGINAL pair has squared Pluecker coordinate at least `1/N_2`. Its rank-two compression has smallest singular value at least `b/N_2`; after the residual is restored, the actual physical pair has

`sigma_min >= kappa=b/N_2-a`.                                    (5.12)

If that pair is definite, conditioning all other coordinates and completing its center gives

`||p_Q||_infinity <= pi/kappa`.                                  (5.13)

If it is indefinite, `D=|det pair|>=kappa^2`; the full-matrix physical-pair theorem and (5.1) give

`||p_Q||_infinity
 <=3*400^(1/3)(D^2*kappa*s)^(-1/6)
 <=3*400^(1/3) kappa^(-5/6)s^(-1/6).`                            (5.14)

All other spectrum and couplings are retained by that receiver.

#### Case III: small self norm

Suppose

`s_1(C)<c`.                                                       (5.15)

Apply (2.3) with `k=4,r=0`. From (5.2),

`s_4(B)>=d_0`, hence `s_3(B)>=d_0`.                              (5.16)

By (4.2), some literal three-row cross block has singular product

`S_3>=d_0^3/sqrt(N_3)`.                                          (5.17)

Condition only on the other `H` coordinates. The exact-rank-three crossing theorem allows arbitrary functions on both sides and gives an integrable characteristic-function envelope. Since the three-row side consists of exactly three original coordinates, its full three-dimensional density cap is one; the orthogonal three-dimensional projection of the untouched product bank has density cap at most `2^(3/2)`. Consequently

`||p_Q||_infinity
 <=3 sqrt(2) S_3^(-1/3)
 <=3 sqrt(2) N_3^(1/6)/d_0`.                                    (5.18)

This branch has a continuous `C_0` density.

#### Case IV: rank-one self survivor

The only remaining regime is

`s_1(C)>=c`, `s_2(C)<b`.                                         (5.19)

Use Section 3. There is an ORIGINAL scalar pivot `i` with

`|a_0|>=alpha`, `||eta||<=L`.                                   (5.20)

Because `s_2(C)<b`, apply (2.3) with `k=4,r=1`:

`s_3(B)>=d_1`.                                                    (5.21)

Equation (3.14) then gives, for the Schur cross block after completing `X_i`,

`s_2(B')>=l d_1=:d'`.                                            (5.22)

By (4.3), some literal pair `I subset H\{i}` has rank-two cross singular product

`S_2>=d'^2/sqrt(N')`.                                            (5.23)

Condition all other coordinates of `H\{i}` but keep the outside bank untouched. The residual `R` after the scalar square completion has arbitrary same-side quadratic and affine terms, plus the literal rank-two crossing `B'_I`. The exact-rank-two crossing theorem gives

`|phi_R(t)| <= min(1, pi sqrt(2) S_2^(-1/2) |t|^(-1)).`          (5.24)

Using the half-Riesz identity,

`integral_R |t|^(-1/2) min(1,K/|t|) dt = 8 sqrt(K)`,             (5.25)

we obtain

`H_(1/2)(R) <= 2^(11/4) S_2^(-1/4)
              <=2^(11/4) N'^(1/8) (d')^(-1/2).`                 (5.26)

Finally the ORIGINAL-coordinate square peel

`Q=a_0(X_i+h)^2+R`                                               (5.27)

gives

`||p_Q||_infinity
 <= |a_0|^(-1/2) H_(1/2)(R)
 <= 2^(11/4) N'^(1/8)/sqrt(alpha*l*d_1).`                        (5.28)

No independence between `h` and `R` is required; only `X_i` remains independent of all other original coordinates. This is exactly why the Schur step is performed in a physical coordinate instead of an eigen-coordinate.

Cases I-IV exhaust the possibilities for `s_3(C),s_2(C),s_1(C)`, proving (5.8). QED.

## 6. Why this mechanism stops at four square modes

The reduction from six/seven carrier modes to four is real, but the same argument does **not** automatically reach the owner's three-mode hypothesis.

In the rank-one self survivor, a four-mode square certificate and `r=1` leave three cross singular directions before the scalar peel; one row loss leaves two, and rank-two crossing has the critical `|t|^-1` Fourier envelope. The outer square contributes the half-Riesz weight `|t|^-1/2`, making the integral convergent.

With only a three-mode square certificate, the same `r=1` spill leaves only two cross singular directions before the peel and only one guaranteed direction afterward. Rank-one crossing has only the `|t|^-1/2` envelope; after multiplying by the half-Riesz weight the tail is `|t|^-1`, logarithmically divergent. Therefore a direct repetition cannot close three modes. A genuine additional mechanism must recover a second transverse direction, exploit a different grouped/hub receiver, or use the third large spectral resource before the scalar peel.

This is the exact remaining implication exposed by the present theorem, not a claim that QFORM is solved.

## 7. Designated partner fleet04/B12 applied to an actual inequality

Apply fleet04/B12's completed hybrid two-profile theorem to the following 16-dimensional baseline:

`A_0 = 2 [[0,I_8],[I_8,0]]`, so `A_0^2=4 I_16`.                (7.1)

Let `H` be the first eight ORIGINAL coordinates. Perform a commuting signed replacement packet `C` for which at most two ordered square losses are severe, so `d_3=0`. Then add an arbitrary symmetric, possibly full-rank and arbitrarily large, noncommuting packet `D` whose destructive square defect relative to the commuting intermediate matrix has rank at most one, so `nu_2=0`. Add an arbitrary-magnitude rank-one symmetric packet `L`, and finally a dense symmetric tail `T` with

`||T||op<=1/4`.                                                   (7.2)

The partner theorem with

`k=4`, `p=2`, `q=1`, `r=1`                                      (7.3)

spends exactly eight baseline square modes and gives the real inequality

`sqrt(lambda_4((A^2)[H,H]))
 >= sqrt(lambda_8(4I_8))-1/4
 = 7/4.`                                                          (7.4)

On the full 16-dimensional space, the same partner theorem with `k=3` uses only index seven and gives

`s_3(A)>=7/4`.                                                     (7.5)

Thus Theorem 5.1 applies with

`m=8`, `g=s=7/4`.                                                  (7.6)

Choose the explicit rational parameters

`c=1749/1000`, `b=27/125`, `a=3/500`.                            (7.7)

They satisfy

`0<a<b/28`, `0<b<c/8`, `0<c<7/4`.                               (7.8)

The five terms in (5.8) are

`finite_core = 4093.306831785954...`,
`definite_pair = 1832.595714594046...`,
`indefinite_pair = 4063.487286938139...`,
`rank3_cross = 140.2907227018117...`,
`rank1_shear_square_peel = 2599.0134738646216...`.               (7.9)

Therefore this target-class family satisfies the explicit uniform bound

`boxed: ||p_(X^T A X)||_(infinity,ess) < 4094.`                   (7.10)

The commuting replacement packet may contain arbitrarily large eigenvalue replacements of either sign except for the explicitly budgeted two destructive square losses; the noncommuting packet may itself be full rank and arbitrarily large except for its one-dimensional destructive square defect; the rank-one packet is unbounded; and the final dense tail is paid only through its matrix operator norm. No one of these is interpreted as an independent random quadratic error.

The partner's preceding six-mode compiler would need a larger post-loss reserve. Equation (7.4) shows the new theorem genuinely reduces the carrier requirement: after spending the same `p+q+r=4` hostile-mode budget, only **eight** baseline square modes are needed to leave four final physical square modes.

## 8. Finite consistency checks

`CHECK.py` uses a fixed seed and performs 10,000 deterministic randomized matrix tests. It found:

- zero violations of `s_2(B')>=ell(||eta||)s_3(B)`, minimum numerical margin `0.0807725004852817`;
- zero violations of the two-row Cauchy-Binet extraction, minimum observed ratio to the guaranteed lower bound `1.27251184150699`;
- zero violations of the three-row extraction, minimum observed ratio `1.76579430336841`.

It also recomputed every numerical constant in (7.9). These are sanity checks only. No histogram, Monte Carlo density estimate, or numerical extremality claim is used in the proof.

## 9. Remaining gap

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

This run reduces one concrete structural debt from a six/seven-mode square carrier to a four-mode carrier and makes the failure at three modes explicit. The next B12 step should attack the rank-one self-block / three-square-mode endpoint:

> Starting from only `lambda_3((A^2)[H,H])>=g^2` in a useful physical carrier, recover a second transverse smoothing direction after the scalar Schur peel, or route the aligned one-direction survivor into a proved hub/grouped-crossing/half-Riesz mechanism without assuming post-rotation independence or small random error.

Continuity is proved in the rank-three crossing branch only. The unrestricted continuous-density conclusion remains open.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and publication were used; no authenticated native learned-memory receiver was available or claimed. No task/schedule state, notification setting, email delivery, public release, paid API/Codex call, cross-account authentication, installation work, or permission was changed.
