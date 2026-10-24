SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T11:27:50Z.
attacking: quadratic-hub mass restoration—remove the exact zero-self restriction by copy-differencing the hub while retaining the full unnormalized slope-bank mass, then extend the partner rank-two leakage algebra to a general Schur direction without support, moment, fragment or translation taxes.

# account02/B14 r34 — arbitrary-self random-slope localization and Schur-direction leakage

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREMS / FULL QFORM OPEN / CONTINUITY SEPARATE**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 0. First unpaid implication and result

The preceding B14 obligation was to keep a whole smoothing direction when a completed physical pair leaves an exact zero-self hub

`X S(V)+R(V)`.

The unpaid issue was that an arbitrarily small but nonzero self coefficient cannot be discarded as a small random perturbation under unbounded inputs. This run removes that exact-zero restriction **without perturbation**.

The new core statement is:

> If `X` is one genuine original-coordinate cap-one variable, a bank submeasure of mass `m` drives a random slope whose unnormalized pushforward density is bounded by `L`, and
>
> `Y=hX^2+X S(V)+R(V)`
>
> with **arbitrary real `h`** and arbitrary correlation between `S(V)` and `R(V)`, then a copy-difference in `X` cancels `R` and turns the self term into a harmless translation of the same slope. The resulting small-ball and logarithmic-potential bounds retain a full factor `m`.

Combined with the physical-pair logarithmic envelope this gives

`||p_Q^sub||_inf <= 8 sqrt(mL/kappa) + C_* m/sqrt(D)`,             (0.1)

where `D=|det C|`, `kappa=sigma_min(C)` for the completed original-coordinate indefinite pair and

`C_* = 2 + log 2 + sqrt(2 pi e) erfc(1/sqrt(2))`
`    = 4.004506265397...`.                                        (0.2)

Thus the previous zero-loss condition `L_j <= H m_j` survives **unchanged** for arbitrary hub self-curvature. No support radius, fragment number/separation, shift, or moment enters.

The second new theorem applies this to any actual three-coordinate block containing an invertible indefinite physical pair. After exact pair completion the remaining physical coordinate has arbitrary self coefficient `h` and a whole-bank Schur leakage vector `a`; if `a != 0`, then

`||p_Q||_inf <= 8/sqrt(kappa ||a||_2) + C_*/sqrt(D)`               (0.3)

using only the required newest-Claude `L^p` lemma to prove the slope density cap. The sharper already-source-pinned product-projection constant improves the first term to

`8/[2^(1/4) sqrt(kappa ||a||_2)]`.                                (0.4)

This extends the newest account03/B14 exact-rank-two collective-kernel-leakage algebra to a general Schur direction; the constant does **not** deteriorate as the remaining self coefficient tends to zero or becomes large.

## 1. Sources actually consumed

Fresh brain control and the live correction corpus were read before work. In particular this proof does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea estimate, post-rotation independence, a conditional projection-density supremum, bounded-diameter localization, a fixed fragment-count reduction, coefficient-to-output-law continuity, or positive moments.

Required newest-Claude source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. The completed result actually applied below is Lemma 1:

`int |psi(t)|^p dt <= 4 pi/sqrt(p),     p>=2`,                    (1.1)

for every characteristic function of a cap-one probability density (and the stated twisted version). I use (1.1) in Section 5 to obtain a dimension-free density cap for the actual whole slope `a^T V`, not merely as background.

Newest compatible designated partner:

`account03/B14` r33, canonical source

`yspennstate/math-open-problems@20e9f45a5d8c8d79034aa09318d8922daae66599`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T103613Z-account03-B14-QFORM-r33/REPORT.md`.

That report proves the exact-rank-two identity after deleting a protected physical coordinate and completing the remaining indefinite pair. In its notation, if `k` spans the kernel of the rank-two triple and `i` is retained, then the completed self coefficient is exactly zero and

`A[S^c,S]k = k_i a`.                                             (1.2)

Section 6 below applies this completed partner algebra and shows that the new theorem remains valid after replacing the zero Schur self coefficient by an arbitrary number, without invoking law continuity.

The outer physical-pair logarithmic envelope is the already-paid source-pinned theorem at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`, together with its companion pair-log formula. Only its original-coordinate independence scope is used.

## 2. Arbitrary-self mixed-difference small-ball theorem

### Theorem 2.1 — `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1`

Let `X` be a real probability variable with density `f<=1`. Let `nu` be a positive finite measure on an arbitrary measurable bank space, independent of `X`, with mass

`m=nu(1) in (0,1]`.

Let `S,R` be arbitrary measurable real functions on the bank and assume the pushforward measure `S_#nu` has an absolutely continuous density bounded by `L`. Put

`H=L/m`.

For arbitrary `h in R`, define the output submeasure by

`Y = hX^2 + X S(V) + R(V)`.                                      (2.1)

Then for every center `t` and every `rho>0`,

`nu_Y{|Y-t|<rho} <= m sqrt(G(4Hrho)),`                            (2.2)

where

`G(q) = 2q[1+log(1/(2q))],   0<q<=1/2,`
`G(q) = 1,                    q>=1/2.`                            (2.3)

The bound is uniform in `h`, in `R`, and in translations of `S`.

### Proof

For fixed bank point `v`, write

`p(v)=P_X(|hX^2+S(v)X+R(v)-t|<rho)`.

Cauchy-Schwarz against the finite measure `nu` gives

`[int p(v) nu(dv)]^2 <= m int p(v)^2 nu(dv)`.                    (2.4)

Let `X'` be an independent copy of `X`. The square `p(v)^2` is the probability that both `X` and `X'` land in the same target interval. On this event, subtracting the two polynomial values yields

`|(X-X') [ h(X+X') + S(v) ]| < 2rho`.                            (2.5)

The arbitrary remainder `R(v)` cancels **exactly**. This is the point of the copy-difference. The nonzero self coefficient is not discarded: it survives only as the translation `h(X+X')` inside the slope variable.

Condition on `X,X'`. For `D=X-X' !=0`, (2.5) asks `S(v)` to lie in an interval of length `4rho/|D|`. Therefore

`nu{v:(2.5)} <= min(m, 4Lrho/|D|)`.                              (2.6)

The same formula is interpreted as `m` at `D=0`. Hence

`nu_Y{|Y-t|<rho}^2`
` <= m^2 E min(1, q/|D|),       q=4Hrho.`                        (2.7)

The difference `D=X-X'` has a probability density bounded by one because

`p_D(u)=int f(x)f(x-u)dx <= ||f||_inf int f <=1`.                (2.8)

For any probability density bounded by one, layer cake gives, for `0<q<1/2`,

`E min(1,q/|D|)`
` = int_0^1 P(|D|<q/u) du`
` <= int_0^(2q) 1 du + int_(2q)^1 2q/u du`
` =2q[1+log(1/(2q))].`                                          (2.9)

For `q>=1/2` use the trivial bound one. No optimizer on the infinite line is assumed. Combining (2.7)-(2.9) proves (2.2). QED.

### Remarks

1. `R` may depend on exactly the same bank coordinates as `S`; no conditional density for `R`, and no independence between `R` and `S`, is needed.
2. `h` is completely arbitrary. In particular the estimate is stable at `h=0` without claiming output-law continuity in `h`.
3. The bank itself need not be product once its slope pushforward cap `L` is known. Product structure is used later only to obtain that cap from original coordinates.

## 3. Exact translated logarithmic potential

Define

`J(q)=int_0^infinity sqrt(G(q e^(-v))) dv`.                       (3.1)

Layer cake and Theorem 2.1 give, for every `A>0`,

`int log_+(A/|t-y|) dnu_Y(y)`
` <= m J(4HA)`.                                                   (3.2)

This is uniform in `t,h,R`.

The function `J` can be evaluated explicitly enough for the pair compiler. Let

`C0 = int_0^infinity e^(-w/2) sqrt(1+w) dw`
`   = 2 + sqrt(2 pi e) erfc(1/sqrt(2))`
`   = 3.311359084837...`.                                        (3.3)

If `q>=1/2`, split at `v=log(2q)` to get exactly

`J(q)=log(2q)+C0`.                                                (3.4)

If `0<q<=1/2`, put `a=log(1/(2q))`; then

`J(q)=sqrt(2q) int_0^infinity e^(-v/2)sqrt(1+a+v)dv`             (3.5)

and equivalently

`J(q)=2^(3/2)e^(1/2) Gamma(3/2,(1+a)/2)`.                        (3.6)

In particular

`J(1)=log2+C0`
`    = C_* =4.004506265397...`.                                  (3.7)

The small-`q` behavior is of order `sqrt(q log(1/q))`; this is more than integrable against the outer logarithmic pair kernel.

## 4. Physical-pair compiler and exact mass restoration

Let an outer pair of **original coordinates** have an invertible indefinite symmetric block `C`; put

`D=|det C|`, `kappa=sigma_min(C)>0`.                              (4.1)

After exact completion of that pair, suppose the remaining active submeasure is of the form in Theorem 2.1. The completed pair-log envelope has, for every cutoff `r>0`, the submeasure form

`p_Q^sub(t) <= 2sqrt(2)m/r`
` + D^(-1/2) int log_+( 2r^2/(kappa|t-y|) ) dnu_Y(y)`.            (4.2)

Using (3.2) and setting

`q=8H r^2/kappa`                                                  (4.3)

gives

`||p_Q^sub||_inf`
` <= m inf_(q>0) { 8 q^(-1/2) sqrt(H/kappa) + D^(-1/2) J(q) }`.  (4.4)

At `q=1`,

`boxed: ||p_Q^sub||_inf <= 8 sqrt(mL/kappa) + C_* m/sqrt(D).`     (4.5)

This is the promised arbitrary-self mass-homogeneous compiler.

### Corollary 4.2 — zero-loss slope-cap mixture localization

Suppose the bank is decomposed into any finite or countable positive family `nu=sum_j nu_j` with masses `m_j`, and the unnormalized slope pushforward of piece `j` has density cap `L_j`. If

`L_j <= H0 m_j`                                                  (4.6)

for every `j`, then summing (4.5) gives

`sum_j ||p_(Q,j)^sub||_inf`
` <= [8 sqrt(H0/kappa)+C_*/sqrt(D)] sum_j m_j`
` = 8 sqrt(H0/kappa)+C_*/sqrt(D).`                               (4.7)

Thus the full constant is preserved exactly. Piece locations, diameters, fragment counts, and translations never occur. In particular, any mixture of bank probability laws whose slope density caps are uniformly `<=H0` is safe, even when the mixture components are arbitrarily remote or unbounded. Affine conditioning shifts only translate the slope and do not change (4.6).

This is a localization principle at the correct unnormalized-mass level. It deliberately does **not** claim that arbitrary two-sided active fragmentation preserves (4.6); previous B14 counterexamples show that it need not.

## 5. Required newest-Claude result applied: a whole-slope density cap

I now derive a concrete slope cap directly from the required Claude Lemma 1 (1.1).

### Lemma 5.1 — Claude-`L^p` product projection cap

Let `V_j` be independent original-coordinate probability variables with densities at most one, and let `a !=0`. Then

`boxed: ||p_(a^T V)||_inf <= 2/||a||_2.`                         (5.1)

Proof. If some coefficient satisfies `|a_h|>=||a||_2/sqrt(2)`, condition on all other coordinates. Convolution with the translated law of `a_hV_h` gives

`||p_(a^T V)||_inf <=1/|a_h| <=sqrt(2)/||a||_2 <2/||a||_2`.     (5.2)

Otherwise put `alpha_j=a_j^2/||a||_2^2`, omitting zero coefficients. Then `alpha_j<=1/2`, `sum alpha_j=1`, and `p_j=1/alpha_j>=2`. For the characteristic functions `psi_j`, Hölder and the required Claude bound (1.1) give

`int_R prod_j |psi_j(a_j t)| dt`
` <= prod_j [ |a_j|^(-1) int |psi_j(u)|^(p_j)du ]^(alpha_j)`
` <= prod_j [4pi sqrt(alpha_j)/|a_j|]^(alpha_j)`
` =4pi/||a||_2`.                                                  (5.3)

Fourier inversion yields (5.1). QED.

Therefore the translated slope

`S(V)=beta+2a^T V`                                                (5.4)

has density cap

`H <=1/||a||_2`.                                                  (5.5)

Substituting (5.5) in (4.5) for a probability bank (`m=1`) is the actual newest-Claude mathematical application:

`boxed: ||p_Q||_inf <= 8/sqrt(kappa ||a||_2) + C_*/sqrt(D).`      (5.6)

The sharper product-projection theorem already source-pinned in the partner report gives `||p_(a^TV)||_inf<=sqrt(2)/||a||_2`, hence

`||p_Q||_inf <= 8/[2^(1/4)sqrt(kappa||a||_2)] + C_*/sqrt(D).`    (5.7)

Equation (5.6), however, is completely sourced from the required e5f71d79 completed `L^p` lemma plus the new theorem of this run.

## 6. General Schur-direction leakage theorem; partner r33 applied

Take an actual three-coordinate set `S=P union {i}`, where `P` consists of two original coordinates. Write the full coefficient matrix, in the order `(P,i,V)`, as

`A = [[ C, b, F ],`
`     [ b^T, d, g^T ],`
`     [ F^T, g, E ]]`,                                           (6.1)

and assume only that the physical pair `C` is invertible indefinite. Define

`h = d-b^T C^(-1)b`,                                             (6.2)
`a = g-F^T C^(-1)b`.                                             (6.3)

Completing the two original coordinates in `P` is exact and leaves

`Y = h X_i^2 + X_i[beta+2a^T V] + R(V)`,                         (6.4)

where `beta` is arbitrary and `R` is the full remaining quadratic-affine function. No coordinate rotation has occurred.

### Theorem 6.1 — `QFORM-SCHUR-DIRECTION-COLLECTIVE-LEAKAGE-v1`

Under (6.1), if `a!=0`, then arbitrary independent cap-one original-coordinate laws and arbitrary affine perturbations satisfy

`boxed: ||p_Q||_inf <= 8/sqrt(kappa||a||_2)+C_*/sqrt(D),`        (6.5)

where `D=|det C|` and `kappa=sigma_min(C)`. With the sharper product-projection cap, replace the first coefficient `8` by `8/2^(1/4)`.

The bound is uniform in the Schur self coefficient `h`; in particular it does not worsen as `h->0`, and it also permits large `h`.

### Material use of designated partner r33

For the rank-exactly-two indefinite triple in account03/B14 r33, the partner proves that the protected deletion index `i` satisfies

`h=0`,                                                           (6.6)

and, with unit kernel `k`,

`A[S^c,S]k = k_i a`.                                             (6.7)

Thus its collective kernel leakage is exactly the `h=0` endpoint of (6.3)-(6.4). The partner's zero-self compiler is numerically sharper there (`2/sqrt(D)` rather than `C_*/sqrt(D)`), so it remains the preferred exact endpoint.

The new result pays the genuinely new case obtained by changing the remaining Schur self coefficient away from zero while keeping the same whole leakage vector. This is not a coefficient-continuity argument: equations (2.4)-(2.9) prove the bound separately for every value of `h`.

Equivalently, define the unnormalised Schur direction on the three physical coordinates by

`r_P=-C^(-1)b`, `r_i=1`.                                         (6.8)

Then `(Br)_P=0`, `(Br)_i=h`, and

`A[S^c,S]r=a`.                                                    (6.9)

At the partner's rank-two endpoint, `r=k/k_i`; for a full-rank or near-rank-two triple, (6.8)-(6.9) continue to make exact sense and (6.5) continues to apply.

## 7. Exact-target stress family: nonzero self curvature plus diffuse leakage

The new theorem is not only a restatement of the exact rank-two endpoint. Let `0<epsilon<=1/2`, `m>=2`, and

`w_m=m^(-1/2)(1,...,1) in R^m`.

Consider independent cap-one original coordinates and the quadratic form

`Q_(epsilon,m)`
` = epsilon^(-1) U_1^2 - epsilon U_2^2`
`   + epsilon X^2 + 2 epsilon^(-1) X (w_m^T V).`                 (7.1)

The matrix is the orthogonal direct sum of the physical pair

`C_epsilon=diag(epsilon^(-1),-epsilon)`                           (7.2)

and the hub-star block

`[[epsilon, epsilon^(-1) w_m^T],`
` [epsilon^(-1)w_m, 0]]`.                                       (7.3)

The pair contributes eigenvalues `epsilon^(-1)` and `-epsilon`. The two nonzero hub-star eigenvalues are

`lambda_+- = [epsilon +- sqrt(epsilon^2+4epsilon^(-2))]/2`,      (7.4)

with product `-epsilon^(-2)`. For `epsilon<=1/2`,

`|lambda_-|>=1`

because `epsilon^(-2)>=1+epsilon`; also `lambda_+>1`. Therefore (7.1) has **at least three actual eigenvalues of modulus at least one** for every `m` and every `0<epsilon<=1/2`: it is inside the exact QFORM target.

For (7.2),

`D=1`, `kappa=epsilon`,                                          (7.5)

while the whole Schur leakage vector in (6.3) is

`a=epsilon^(-1) w_m`, `||a||_2=epsilon^(-1)`.                   (7.6)

The newest-Claude slope cap (5.5) gives `H<=epsilon`, and (6.5) yields the completely uniform estimate

`boxed: ||p_(Q_(epsilon,m))||_inf <= 8+C_* <12.005.`             (7.7)

Using the sharper projection constant gives

`||p||_inf <=8*2^(-1/4)+C_* <10.732`.                            (7.8)

This remains true if every `V_j` has arbitrarily distant finite fragments or unbounded support; only the cap-one hypothesis enters.

For comparison, the general arbitrary-rank physical-pair theorem applied only to (7.2) gives

`3*400^(1/3) epsilon^(-1/6)`,                                   (7.9)

which diverges as `epsilon->0`. Thus the new whole-bank slope mechanism pays a genuinely different poorly-conditioned-pair regime.

### Single-coordinate selection loses

If all bank coordinates except `V_j` are conditioned first, the surviving slope is

`beta + 2 epsilon^(-1)m^(-1/2)V_j`.                              (7.10)

Its density cap can be as large as

`H_j=epsilon sqrt(m)/2`                                          (7.11)

(for example for a unit-density one-dimensional marginal). Feeding this into the same arbitrary-self compiler gives only

`8 sqrt(H_j/kappa)+C_*`
` =4sqrt(2)m^(1/4)+C_*`,                                         (7.12)

which diverges with `m`, while the whole-bank bound (7.7) is constant. Hence

`QFORM-ARBITRARY-SELF-SINGLE-LEAKAGE-SELECTION-BARRIER-v1`:

**even with a nonzero Schur self coefficient, selecting one leakage coordinate before paying the aggregate slope incurs an artificial `m^(1/4)` loss.** This is a proof-order obstruction, not a lower bound on the true density and not a counterexample to QFORM.

The obstruction persists for remote fragmented laws, because neither (7.6) nor the one-coordinate scaling (7.11) depends on fragment centers.

## 8. Localization consequences and remaining implication

The safe order furnished by this run is now

`whole slope bank -> copy-difference arbitrary-self hub -> translated logarithmic potential -> outer pair payment -> outside conditioning/mixture`.  (8.1)

This strictly enlarges the preceding zero-self branch. Active fragments may be localized with zero loss whenever their **unnormalized** slope caps satisfy `L_j<=H0 m_j`; arbitrary translations of those fragments are harmless. Inactive original coordinates may be conditioned freely once the active certificate is fixed because they only create affine terms. No bounded-diameter or fixed-fragment shortcut is used.

The first unpaid structural implication becomes

`QFORM-SCHUR-LEAKAGE-OR-WHOLE-VOLUME-EXIT-v1`:

> In every surviving N3/no-pivot state, expose before active-law fragmentation either (i) an original-coordinate invertible indefinite pair whose Schur direction has quantitatively useful whole-bank leakage `a` so that `kappa||a||` and `D` pay (6.5), with **no need for exact zero self curvature**; or (ii) an existing whole-law D'/D5/ridge/mixed-hub/bank certificate; or (iii) a new outside-curvature mechanism. A small nonzero Schur self coefficient is no longer an unpaid reason to abandon the random-slope branch.

What remains structural is the possibility that every useful indefinite physical pair has poor `D` and the corresponding Schur leakage is too small, while the third spectral resource is stored in dense outside curvature not caught by an existing whole-law certificate.

## 9. Integrity

- Full QFORM: **OPEN / not proved / not disproved**.
- Continuity: **not proved here**; all conclusions are essential-density bounds.
- New proved theorem: `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1`, equations (2.2)-(4.5).
- New proved localization principle: `QFORM-SLOPE-CAP-MIXTURE-TRANSFER-v1`, equation (4.7).
- New proved structural branch: `QFORM-SCHUR-DIRECTION-COLLECTIVE-LEAKAGE-v1`, equation (6.5).
- New source-valid proof-order obstruction: `QFORM-ARBITRARY-SELF-SINGLE-LEAKAGE-SELECTION-BARRIER-v1`, equations (7.10)-(7.12).
- Required newest-Claude completed result actually applied: `L^p` Lemma 1 at (5.3), yielding the real slope-density inequality (5.1)-(5.6).
- Designated partner account03/B14 r33 actually applied at (6.6)-(6.9); the new theorem extends its exact zero-self algebra rather than re-labelling it.
- No moments, bounded support, fixed fragment count, Gaussianity, log-concavity, identical-law assumption, post-rotation independence, conditional-density supremum, or coefficient-to-output-law continuity is used.
- Repository transport is not verified learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
