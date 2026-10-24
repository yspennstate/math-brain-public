SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T02:06:07Z.
attacking: mass-homogeneous overlap-slope localization — extend the newest account03/B14 two-Plancherel receiver to positive subprobability pieces and prove zero-tax arbitrary fragmentation whenever an undecomposed original-coordinate anchor subbank retains slope norm.

# account02/B14 — mass-homogeneous overlap-slope localization

Run: `20260924T020607Z-account02-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: translations and localization / complementary constructions and source-valid counterexamples  
Control revision: `2026-09-22.15`  
Status: **NEW SUPPORTING LOCALIZATION THEOREM + EXACT FRAGMENT-FIRST BARRIER / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN: independent real coordinates with marginal densities at most one; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one; no moments, support, log-concavity, centeredness, connectedness, finite-fragment, diagonal-basis, or post-rotation-independence assumption. Continuity remains separate from the universal essential-height target.

## 1. First unpaid implication

The sharpened obligation from this run is

> **`QFORM-DIFFUSE-SLOPE-ANCHOR-OR-AGGREGATE-BEFORE-LOCALIZE-v1`.** In an overlap-preserving hub receiver, localize a rough slope bank only after either (i) its whole slope has been aggregated, or (ii) an undecomposed original-coordinate anchor subbank retains a universally positive amount of the slope `l2` norm. A fixed-cardinality anchor cannot replace this in a diffuse bank. Otherwise one needs a new mass-homogeneous aggregate estimate before active-fragment normalization.

The point is not support geometry. The issue is the exact mass power carried by the slope-density cap after positive localization.

## 2. Valid premises actually used

### 2.1 Designated partner account03/B14: overlap-preserving two-Plancherel theorem

Source:

- `yspennstate/math-open-problems@389a363c688ac948d056ed4c3cb6615603852b21`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260924T010202Z-account03-B14-QFORM-auto11/REPORT.md`
- theorem `QFORM-OVERLAP-HUB-SLOPE-TWO-PLANCHEREL-v1`.

Its abstract form is as follows. Let `X` have density at most one. Let `(L,Y)` be independent of `X` and have unnormalised slices

`P((L,Y) in dl dy)=nu_l(dy) dl`, `int nu_l(R) dl=1`,

with

`F_t(l)=int exp(ity) nu_l(dy)`, `ess sup_l |F_t(l)| <= A |t|^(-1/2)`.

Let `Z` be independent of `(X,L,Y)`, and let `S=S(Z)` have density cap `M`; `R=R(Z)` is arbitrary. For

`Q=H(X)+2XL+Y+2XS(Z)+R(Z)`,

the partner proves

`|phi_Q(t)| <= min(1, pi sqrt(A M) |t|^(-5/4))`,

and therefore

`||p_Q||_infinity <= 5 pi^(-1/5) (A M)^(2/5)`,

with a continuous `C_0` density. No support or moment assumptions enter.

### 2.2 Newest designated partner account03/B14: disjoint-bank Schur localization

The latest compatible partner result observed before publication is

- `yspennstate/math-open-problems@4366a5648435eb9bfd6dcc40d4aa6fc3b3e67f6c`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260924T013955Z-account03-B14-QFORM-auto11/REPORT.md`
- theorem `QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1`.

If three disjoint original-coordinate banks compress through vectors `u_r`, with `R=diag(||u_r||_2)`, and the active quadratic block factors as `U B U^T` with aligned exterior coupling and `tau=sigma_min(RBR)>0`, then

`||p_Q||_(infinity,ess) <= 12 sqrt(pi)/tau`.

Arbitrary outside self-curvature, translations, remote fragments and unbounded supports are allowed in its stated factorised chamber.

### 2.3 Fixed required Claude source

Freshly consumed at the owner-pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

were `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The completed result used below is `COUNTEREXAMPLE_SEARCH.md` Theorem A: in dimension three, for independent cap-one inputs, arbitrary affine terms, and a symmetric matrix all of whose eigenvalues have modulus at least `sigma`,

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

This theorem is applied to the same exact-target stress family used for the localization obstruction below.

## 3. New theorem: positive-submeasure homogeneity of the overlap receiver

### Theorem `QFORM-OVERLAP-SLOPE-SUBPROBABILITY-HOMOGENEITY-v1`

Keep the partner's `(X,L,Y)` hypotheses and slice constant `A`. Replace the probability law of the slope bank `Z` by an arbitrary finite positive measure `tau` of mass

`m=tau(Omega)`, `0<m<=1`.

Let `S=S(Z)` and `R=R(Z)` be arbitrary measurable real functions. Assume only that the positive pushforward `S_# tau` has a Lebesgue density bounded by `L`. Let `eta` be the resulting finite output measure of

`Q=H(X)+2XL+Y+2XS(Z)+R(Z)`

when the `Z` law is `tau` rather than a probability law. Then `eta` has a continuous density and

`boxed: ||p_eta||_infinity <= 5 pi^(-1/5) A^(2/5) m^(3/5) L^(2/5).`      (3.1)

The estimate is uniform in every translation and in the arbitrary phase `R`.

### Proof

The first half of the partner proof is unchanged. Define

`G_t(x)=int exp(2itxl) F_t(l) dl`.

Since `|F_t(l)|<=nu_l(R)` and `ess sup |F_t|<=A|t|^(-1/2)`, the partner's first Plancherel step gives

`||G_t||_2 <= sqrt(pi A) |t|^(-3/4).`                                (3.2)

Now push the complex measure `exp(itR(z)) tau(dz)` forward by `S`. Call the resulting complex measure `gamma_t`. Its total variation is dominated by the positive measure `S_#tau`: for every Borel set `B`,

`|gamma_t|(B) <= (S_#tau)(B)`.

Hence `gamma_t` has a density `g_t` satisfying

`|g_t(s)| <= p_(S_#tau)(s)`,
`||g_t||_1 <= m`,
`||g_t||_infinity <= L`.

Therefore

`||g_t||_2^2 <= m L`.                                                  (3.3)

With

`K_t(x)=int exp(2itxs) g_t(s) ds`,

Plancherel and `xi=2tx` give

`||K_t||_2^2 = (pi/|t|)||g_t||_2^2 <= pi m L |t|^(-1)`,

so

`||K_t||_2 <= sqrt(pi m L)|t|^(-1/2).`                               (3.4)

The exact hub-level factorisation remains

`hat eta(t)=int f_X(x) exp(itH(x)) G_t(x) K_t(x) dx`.

Since `0<=f_X<=1`, Cauchy--Schwarz together with (3.2)-(3.4) gives

`|hat eta(t)| <= pi sqrt(A m L) |t|^(-5/4)`.                          (3.5)

Because `eta` has total mass `m`, also `|hat eta(t)|<=m`. Set

`C=pi sqrt(A m L)`.

The threshold at which `m=C t^(-5/4)` is `t_0=(C/m)^(4/5)`. Thus exactly

`int_R min(m,C|t|^(-5/4)) dt
 =2[m t_0 + 4 C t_0^(-1/4)]
 =10 C^(4/5)m^(1/5).`                                                  (3.6)

Fourier inversion yields a continuous density and

`||p_eta||_infinity
 <=(1/(2pi)) 10 [pi sqrt(A m L)]^(4/5)m^(1/5)
 =5 pi^(-1/5) A^(2/5)m^(3/5)L^(2/5).`

This proves (3.1). QED.

## 4. Exact countable-mixture compiler

Let the slope-bank probability law be decomposed into arbitrary positive finite measures

`tau=sum_j tau_j`, `m_j=tau_j(Omega)`, `sum_j m_j=1`,

and suppose the slope pushforward of piece `j` has density cap `L_j`. Applying (3.1) piecewise and summing the nonnegative output densities gives

`boxed:
 ||p_Q||_infinity
 <=5 pi^(-1/5) A^(2/5)
   sum_j m_j^(3/5)L_j^(2/5).`                                      (4.1)

No finite fragment count is required.

The exact zero-tax condition is now visible. If

`L_j <= M_0 m_j`                                                       (4.2)

for every piece, then (4.1) becomes

`||p_Q||_infinity
 <=5 pi^(-1/5) A^(2/5) M_0^(2/5) sum_j m_j`

and therefore

`boxed:
 ||p_Q||_infinity <=5 pi^(-1/5)(A M_0)^(2/5).`                      (4.3)

Thus arbitrary countable localization is genuinely free when the unnormalised slope cap carries one full power of the piece mass. This is the overlap-receiver analogue of the mass-homogeneous localization principle sought by this slot.

## 5. Anchor-bank zero-tax localization

### Corollary `QFORM-OVERLAP-SLOPE-ANCHOR-LOCALIZATION-v1`

Let the slope bank consist of independent original-coordinate subbanks

`Z=(Z_H,Z_C)`,
`S=a_H^T Z_H + a_C^T Z_C`,

with `a_H !=0`. Keep the entire `H` subbank undecomposed and decompose the law of `Z_C` arbitrarily into positive finite measures `tau_j` of masses `m_j`. The pieces may be remote, disconnected, unbounded, countably many, and need not individually be normalised.

For independent cap-one original coordinates, the Ball--Rogozin projection bound gives

`||p_(a_H^T Z_H)||_infinity <= sqrt(2)/||a_H||_2`.                   (5.1)

For each complement piece, its contribution to `a_C^T Z_C` is a positive measure of total mass `m_j`. Convolution with (5.1) implies that the **unnormalised** full-slope pushforward obeys

`L_j <= m_j sqrt(2)/||a_H||_2`.                                      (5.2)

This remains enough even when `R(Z_H,Z_C)` couples both subbanks arbitrarily, because the phase-weighted slope pushforward is dominated in total variation by the positive unweighted pushforward used in (5.2).

Substituting (5.2) into (4.3) gives

`boxed:
 ||p_Q||_infinity
 <=5 pi^(-1/5)
   [A sqrt(2)/||a_H||_2]^(2/5).`                                    (5.3)

Therefore the entire complementary slope bank may be localized at zero count/separation/support/tail cost. The only quantitative price is the retained `l2` norm of the undecomposed original-coordinate anchor.

If the account03/B14/account04 slice core has

`A=4 sqrt(pi)/(|h| sqrt(|gamma|))`,

then (5.3) simplifies exactly to

`boxed:
 ||p_Q||_infinity
 <=10 ||a_H||_2^(-2/5)|h|^(-2/5)|gamma|^(-1/5).`                   (5.4)

Hence a positive fraction of diffuse slope energy can be kept whole without any requirement on the remaining fragments.

## 6. Exact fragment-first obstruction inside the full target

The mass exponent in (3.1) also shows precisely why localising **all** of an active slope before payment is unsafe.

Let `X,L,Y` be independent Uniform`[-1/2,1/2]`. For `N>=1`, let

`E_N = union_(j=1)^N [4^j,4^j+1/N]`,

and let `Z_N` have density `1_(E_N)`, independent of `X,L,Y`. Define

`Q_N = 2X(L+Z_N)+Y^2`.                                                (6.1)

The exponentially remote tooth locations are inessential; any disjoint locations work. Every input density is at most one, with no common support diameter.

### 6.1 Exact target spectrum

In the original independent coordinates `(X,L,Z_N,Y)`, the quadratic matrix is

`A_N = [[0,1,1,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,1]].`

The star vector from `X` to `(L,Z_N)` has Euclidean norm `sqrt(2)`, so

`spec(A_N)={sqrt(2),-sqrt(2),1,0}`.                                  (6.2)

Thus this family lies squarely inside the owner's exact three-large-eigenvalue target for every `N`.

### 6.2 A uniform whole-slope certificate

Use `L` as the slice coordinate and `Y^2` as the slice phase. Put

`I(t)=int_(-1/2)^(1/2) exp(it y^2) dy`.

For `|t|<=16`, `|I(t)|<=1<=4|t|^(-1/2)`. For `T=|t|>16`, set `a=T^(-1/2)`. The central interval `[-a,a]` contributes at most `2/sqrt(T)`. On `[a,1/2]`, integration by parts against `d exp(iTy^2)=2iTy exp(iTy^2)dy` gives

`|int_a^(1/2) exp(iTy^2)dy| <= 1/sqrt(T)`,

and the negative tail is identical. Hence

`boxed: |I(t)| <= 4 |t|^(-1/2)`,                                    (6.3)

so the partner slice constant is `A=4`.

The whole slope `S=Z_N` has density cap `M=1`, independent of `N` and every fragment separation. The account03/B14 two-Plancherel theorem therefore gives

`boxed:
 ||p_(Q_N)||_infinity
 <= C_*:=5 pi^(-1/5)4^(2/5)
 =6.924111078456...`                                                  (6.4)

for every `N`, with a continuous `C_0` density.

### 6.3 Fragment-first payment diverges on the unchanged law

Now change **only the bookkeeping**: split the same slope law into its `N` tooth submeasures

`tau_j(dz)=1_[4^j,4^j+1/N](z) dz`.

Each has exact mass

`m_j=1/N`,

but its unnormalised slope-density cap is still

`L_j=1`,                                                               (6.5)

not `1/N`. Applying the new subprobability theorem (3.1) to the teeth separately and summing yields

`||p_(Q_N)||_infinity
 <= C_* N (1/N)^(3/5)
 = C_* N^(2/5).`                                                       (6.6)

The certificate diverges although the probability law in (6.1) has not changed and the whole-law certificate (6.4) stays fixed. The loss is exactly the failure of the active tooth cap to carry a full mass factor before normalisation.

This is **`QFORM-WHOLE-SLOPE-BEFORE-FRAGMENTATION-BARRIER-v1`**. It is a proof-interface obstruction, not a lower bound on the true density and not a QFORM counterexample.

## 7. Applying the latest partner and fixed Claude theorem to the same family

### 7.1 Latest account03/B14 disjoint-bank theorem

For (6.1), take the three disjoint original-coordinate banks

`I_1={X}`, `I_2={L,Z_N}`, `I_3={Y}`,

with bank vectors

`u_1=(1)`, `u_2=(1,1)`, `u_3=(1)`.

Then `R=diag(1,sqrt(2),1)` and the compressed three-bank matrix is

`B=[[0,1,0],[1,0,0],[0,0,1]].`

Thus

`R B R=[[0,sqrt(2),0],[sqrt(2),0,0],[0,0,1]]`

has minimum absolute eigenvalue `tau=1`. The **newest** account03/B14 theorem therefore independently gives the real whole-law inequality

`boxed: ||p_(Q_N)||_(infinity,ess) <=12 sqrt(pi)=21.269446210866...`  (7.1)

uniformly in `N` and all tooth locations. This directly applies the designated partner to a fragmented exact-target instance.

### 7.2 Required fixed-source Theorem A

There is an even simpler source-valid aggregation. Define

`T_N=L+Z_N`.

Because `L` has density cap one and is independent of `Z_N`, convolution gives

`||p_(T_N)||_infinity<=1`.                                            (7.2)

The three variables `(X,T_N,Y)` are genuinely independent because they depend on disjoint original-coordinate source sets. In these variables

`Q_N=2XT_N+Y^2`

has the `3x3` matrix

`B=[[0,1,0],[1,0,0],[0,0,1]]`

with eigenvalues `{1,-1,1}`. Therefore the completed Theorem A in the required fixed Claude source gives

`boxed:
 ||p_(Q_N)||_infinity <=6 sqrt(pi)
 =10.634723105433...`                                                  (7.3)

for every `N`.

Equation (7.3) is the requested application of a completed fixed-source result to a real obstruction: the true source-valid density stays uniformly bounded while the fragment-first overlap certificate (6.6) grows like `N^(2/5)`.

## 8. Diffuse-anchor quantitative barrier

The anchor corollary also quantifies the structural cost in a diffuse slope bank. Let

`S_m=m^(-1/2) sum_(j=1)^m Z_j`

with independent cap-one `Z_j`. Its full coefficient vector has norm one, so the whole-bank Ball--Rogozin cap is at most `sqrt(2)` and the overlap theorem is uniform in `m`.

If only `k` of these `m` original coordinates are retained as the undecomposed anchor, their coefficient norm is

`||a_H||_2=sqrt(k/m)`.

The guaranteed anchor-localization bound (5.3) therefore pays exactly the factor

`(m/k)^(1/5)`                                                          (8.1)

relative to keeping the full slope bank. In particular a fixed-cardinality anchor cannot yield a uniform certificate as `m->infinity`; a positive fraction of the slope `l2` energy, or whole-slope aggregation before localization, is required by this mechanism.

This is not asserted to be an impossibility theorem for every conceivable proof. It identifies the exact failure mode of the mass-homogeneous anchor compiler and rules out replacing the whole diffuse slope by a bounded number of active coordinates inside this interface.

## 9. Translation / localization ledger

The new theorem and corollaries retain the user's full localization requirements:

- arbitrary deterministic translations of `X`, `L`, or the slope bank only alter phases/affine terms and do not change (3.1)-(5.3);
- positive slope pieces may be arbitrarily remote and countably many;
- no common support radius or diameter is introduced;
- no moment or tail quantity appears;
- `R(Z)` may contain arbitrary self-curvature and affine terms on the whole slope bank;
- the source product structure is used before compression, never inferred after a spectral rotation;
- the whole active slope must be aggregated, or an undecomposed original-coordinate anchor must remain, before reciprocal/mass-sensitive payment.

The remote comb (6.1) shows that replacing this ordering by normalised active-fragment payment can manufacture an unbounded proof cost while changing neither the law nor the exact-target spectrum.

## 10. What remains unpaid

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new analytic localization step removes one more rough-law obstruction: once a source-disjoint slope bank shares a physical hub with a valid half-order slice core, arbitrary localization of the slope complement is free provided a whole anchor carries a fixed amount of slope norm.

The remaining bridge is structural. Starting only from `s_3(A)>=1`, before active fragmentation one must force at least one of:

1. a whole-law D'/D5/projected-crossing/ridge/hub/pair/receiver payment;
2. the newest partner's three-disjoint-bank Schur compression with uniformly nondegenerate `RBR`;
3. an overlap two-Plancherel chamber in which the whole slope is aggregated;
4. an overlap chamber with an undecomposed original-coordinate anchor of uniformly positive slope norm; or
5. a new aggregate estimate for the residual case where every prospective slope resource is diffuse and entangled with the same-bank curvature needed by the core.

The central rule is now exact: **aggregate the active slope before localization, unless an unnormalised slope cap proportional to piece mass has already been secured.** Translation and remote fragmentation themselves are not the remaining debt.

## 11. Continuity and integrity

The subprobability theorem proves a continuous `C_0` density on its stated overlap branch because its Fourier transform is integrable. The latest disjoint-bank partner theorem is used only for essential height and does not add continuity. The unrestricted target's continuity question remains OPEN.

No false arbitrary-joint coarea estimate, post-rotation independence, law-uniform pointwise quadratic-phase decay, conditional-density-supremum shortcut, bounded-diameter/fixed-fragment reduction, or uniformly good physical minor is used. No numerical histogram is used as proof.
