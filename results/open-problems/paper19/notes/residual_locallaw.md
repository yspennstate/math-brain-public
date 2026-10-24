# Closing the keystone residual via the local law: the resolvent-monotonicity route

Agent note, 2026-06-28. Companions (read-only): `residual_nogaps.md` (identifies the
connection), `keystone_synthesis.md`, `keystone_tail.md`. This note attempts the path flagged at
the end of `residual_nogaps.md`: apply the isotropic/anisotropic local law to the deformed
sample covariance of the keystone's actual realization. The outcome is more favorable than the
companion's pessimistic "must be written, boundary of the literature": a single elementary
resolvent-monotonicity inequality *bypasses* the hard-edge eigenvector problem and reduces the
residual to the local law in its EASIEST regime (the resolvent below the spectrum), which is a
published estimate.

## 0. Target, realization, notation

Condition on the shared span `E` (dimension `m-D`). Inside `E^perp ~= F^D` the side-`S` normal is
`u`, the unit null vector of the `D-1` projected disjoint rows. The keystone's realization
(`residual_nogaps.md` lines 119-130) is
```
   g_i = B^* a_i in F^D,   a_i iid mean-0 var-1 entries in F^m (the disjoint private rows),
   B : F^D -> F^m  fixed isometry onto E^perp  (B^*B = I_D,  BB^* = P_{E^perp} =: P),
   G = [g_1 ... g_{D-1}] = B^* A,   A = [a_1 ... a_{D-1}] iid-entry  m x (D-1),
   Q := (1/D) G G^* = (1/D) B^*(A A^*) B,    u = unit eigenvector of Q for eigenvalue 0.
```
`Q` is `D x D` and has rank `<= D-1`, so `0` is an EXACT eigenvalue with eigenvector `u`
(unique up to phase a.s.). Write `M_E := E[u u^* | E]`. The target (closes II.B universality
upper side, hence the Gumbel law):
```
   (DELOC-EXP)   lambda_max(M_E) = sup_{||w||=1} E[ |<u,w>|^2 | E ]  = o(1),
```
equivalently, unconditionally, `lambda_max(E[u u^*]) = o(1)` (by convexity
`lambda_max(E_E M_E) <= E_E lambda_max(M_E)`).

What the keystone consumes downstream is `mu1 := E|rho|^2 = E_E[tr M_E^2]`, and
`tr M_E^2 <= lambda_max(M_E) tr M_E = lambda_max(M_E)` (since `tr M_E = 1` by isotropy). So
`(DELOC-EXP)` gives `mu1 <= E_E lambda_max(M_E) = o(1)`. Section 5 records that `mu1 = o(1)`
(not the sharper `O(1/D)`) already suffices for the assembly in `keystone_tail.md`.

## 1. The two published inputs (cited, not reproved)

**[BEKYY14] Isotropic local law (sample covariance).** Bloemendal, Erdős, Knowles, Yau, Yin,
"Isotropic local laws for sample covariance and generalized Wigner matrices," Electron. J.
Probab. 19 (2014), no. 33. For `X` an `M x N` matrix with iid entries (mean 0, variance `N^{-1}`,
suitable moments), `m_{MP}` the Marchenko–Pastur Stieltjes transform at ratio `phi = M/N`, and
deterministic unit vectors `v, w`, uniformly on the spectral domain `{ z = E+i\eta : \eta >=
N^{-1+eps} }` (including up to the edges),
```
   |<v, (X X^* - z)^{-1} w> - m_{MP}(z) <v,w>|  <  Psi(z),
   Psi(z) = sqrt( Im m_{MP}(z) / (N \eta) ) + 1/(N \eta),
```
in the sense of stochastic domination ("≺"). In particular `|<v, xi_alpha>|^2 ≺ 1/N` uniformly
in deterministic `v` for any bulk/edge eigenvector `xi_alpha` (isotropic delocalization). Hypothesis:
iid ENTRIES. This applies verbatim to `Q` only in the Gaussian case (where `g_i = B^*a_i` is
genuinely iid `N(0,I_D)`); for general entries `G = B^* A` is not iid-entry and we need:

**[KY17] Anisotropic local law (deformed/separable model).** Knowles, Yin, "Anisotropic local
laws for random matrices," Probab. Theory Related Fields 169 (2017), 257–352. For the separable
sample covariance `Q_Sigma = Sigma^{1/2} X X^* Sigma^{1/2}` (`X` iid `M x N`, `Sigma` deterministic
`M x M` PSD) there is a deterministic "anisotropic equivalent" `Pi(z)` (solving the matrix
Marchenko–Pastur/Dyson equation in `Sigma`) with, for deterministic `v,w` and `z` on the same
domain,
```
   |<v, (Q_Sigma - z)^{-1} w> - <v, Pi(z) w>|  <  Psi(z).
```
This is the tool that tolerates the non-iid structure `g_i = B^* a_i` (a linear image of iid).

## 2. Putting `Q` into the [KY17] form, and the deterministic equivalent

`Q = B^*(AA^*)B` (`D x D`) has the same nonzero spectrum and the same `E^perp`-resolvent as the
`m x m` matrix `P (AA^*) P = P^{1/2}(AA^*)P^{1/2}` with `P = BB^* = P_{E^perp}` (a projection, so
`P^{1/2}=P`). This is exactly the [KY17] separable model with
```
   X = A  (iid m x (D-1)),     Sigma = P = P_{E^perp}  (m x m, rank D).
```
Two structural points, both routine:

(a) **Rank-deficient `Sigma = P` decouples.** `P(AA^*)P` is block-diagonal w.r.t. `F^m = E ⊕
E^perp`: it kills `E` and maps `E^perp -> E^perp` with no cross term (`<x_E, P AA^* P x_{E^perp}>
= <Px_E, AA^* x_{E^perp}> = 0`). So for `z != 0`, `(P AA^* P - z)^{-1} = (-1/z)|_E ⊕
(Q|_{E^perp} - z)^{-1}`, and for `w in E^perp` (identified with `F^D` via `B`)
`<w,(Q - z)^{-1}w> = <Bw, (PAA^*P - z)^{-1} Bw>`. The kernel of `Sigma` (the only place `Sigma`
fails the usual `c <= Sigma <= C`) contributes only the trivial `E`-block and is invisible on
`E^perp`. Hence [KY17]'s estimate applies on `E^perp` with the effective population
`Sigma|_{E^perp} = I_D` and constants uniform over the isometry `B` (every `B` gives the SAME
class `B^*B = I_D`, `BB^* = ` rank-`D` projection).

(b) **The anisotropic equivalent is scalar on `E^perp`.** Because the effective population on
`E^perp` is the identity (`Cov(g_i) = B^*B = I_D`) and the aspect ratio is `(D-1)/D -> 1`, the
limiting spectral law of `Q` is Marchenko–Pastur with `c = 1`, density
`rho(x) = (2 pi)^{-1} sqrt((4-x)/x)` on `(0,4]` (hard edge at `0`), and `Pi(z) = m(z) I_D` on
`E^perp`, where `m = m_{MP,c=1}`. Thus for deterministic `w in F^D`, `||w||=1`,
```
   <w,(Q - z)^{-1} w> = m(z) + O_≺(Psi(z)),   and   ||E[(Q-z)^{-1} | E] - m(z) I_D|| = o(|m(z)|)
```
uniformly on the spectral domain (the operator-norm statement follows from the isotropic estimate
by a net over `w`, since `E[(Q-z)^{-1}|E]` is a single deterministic matrix).

**Hard-edge value of `m` below the spectrum.** For real `z = -eta`, `eta in (0,1)`, the resolvent
`(Q+eta)^{-1}` is PSD with `||(Q+eta)^{-1}|| = 1/(lambda_min(Q)+eta) = 1/eta` (the null direction),
but the DETERMINISTIC equivalent is the finite number
```
   m(-eta) = int_0^4 rho(x)/(x+eta) dx  =  (1+o(1)) eta^{-1/2}     (eta -> 0).
```
(Direct computation, dominated by `x ~ 0` where `rho ~ (pi sqrt x)^{-1}`:
`int_0^infty (pi sqrt x)^{-1}(x+eta)^{-1}dx = eta^{-1/2}`. Numerically `m(-eta) sqrt(eta) =
0.76, 0.85, 0.92, 0.95, 0.97, 0.98` at `eta = .3,.1,.03,.01,.003,.001`, increasing to `1`.) The
hard edge enters ONLY through this scalar `m(-eta)`; no delicate edge eigenvector statement is used.

## 3. The key tool: resolvent monotonicity bypasses the hard edge

The companion `residual_nogaps.md` despaired because isolating the EXACT null vector `u` by a
resolvent needs `eta` below the spectral gap (smallest nonzero eigenvalue of `Q` is at the hard-edge
scale `~ D^{-2}`), i.e. `eta << D^{-2}`, far below the local-law floor `D^{-1+eps}`. The following
one-line PSD inequality removes that need.

**Lemma (resolvent-monotonicity).** Let `Q = sum_k lambda_k u_k u_k^*` (spectral decomposition,
`lambda_0 = 0`, `u_0 = u`). For every `eta > 0`, as PSD matrices,
```
   u u^*  ⪯  eta (Q + eta)^{-1}.                                            (3.1)
```
*Proof.* `eta(Q+eta)^{-1} = sum_k [eta/(lambda_k+eta)] u_k u_k^*`. The `k=0` term is `1·u u^*`
(since `lambda_0 = 0`), and every other coefficient `eta/(lambda_k+eta) in (0,1]` is `>= 0`. So
`eta(Q+eta)^{-1} - u u^* = sum_{k>=1}[eta/(lambda_k+eta)] u_k u_k^* ⪰ 0`. ∎

Equivalently `|<u,w>|^2 <= eta <w,(Q+eta)^{-1} w>` for all `w`, all `eta>0`. The bound holds at
ANY scale, in particular at the local-law floor; it is loose by exactly the bulk contribution
`sum_{k>=1}[eta/(lambda_k+eta)]|<u_k,w>|^2 ~ sqrt(eta)`, which is the price we pay (Section 6).

Taking `E[· | E]` of (3.1) — the inequality is between random PSD matrices, so it survives
conditional expectation — gives the deterministic PSD bound
```
   M_E = E[u u^* | E]  ⪯  eta · E[(Q + eta)^{-1} | E],
   hence   lambda_max(M_E)  <=  eta · || E[(Q + eta)^{-1} | E] ||.          (3.2)
```
This is the whole reduction: the LEFT side is the hard-edge null-vector overlap; the RIGHT side is
the operator norm of an EXPECTED resolvent, controlled by the local law at any `eta` we like.

## 4. Main conditional theorem

**Theorem (conditional on [KY17]/[BEKYY14]).** With the notation of Section 0, fix any
`eta in [D^{-1+eps}, 1)`. The anisotropic local law of Section 2 gives
`|| E[(Q+eta)^{-1} | E] || = m(-eta)(1+o(1))`, uniformly over the isometry `B`. Combined with (3.2)
and `m(-eta) = (1+o(1)) eta^{-1/2}`,
```
   lambda_max(M_E)  <=  eta · m(-eta)(1+o(1))  =  (1+o(1)) sqrt(eta).        (4.1)
```
Choosing `eta = (log D)^{-1}` (a comfortably mesoscopic point, far above every edge scale) gives
```
   lambda_max(E[u u^* | E])  <=  (1+o(1)) (log D)^{-1/2}  =  o(1),
```
uniformly in `B`; pushing to the local-law floor `eta = D^{-1+eps}` gives the rate
`lambda_max(M_E) <= D^{-1/2 + eps/2 + o(1)}`. Either bound is `(DELOC-EXP)`, and unconditionally
`lambda_max(E[u u^*]) <= E_E lambda_max(M_E) = o(1)`. ∎

The estimate (4.1) is exactly `eta || E[(Q+eta)^{-1}] ||`; the numerics of `scratchpad` give
`eta||E[(Q+eta)^{-1}]|| = 0.50, 0.46, 0.43` at `D=16,32,64` (`eta = 1/log D`), tracking
`sqrt(eta) = 0.60, 0.54, 0.49`, while the TRUE `E|<u,w>|^2 = 0.065, 0.033, 0.014 ~ 1/D` sits well
below the bound (the bound is sound but lossy by the hard-edge factor, see Section 6).

## 5. The three adaptation points (as posed)

**(a) Hard edge / null vector.** This is the point the companion thought fatal, and it is the one
the Lemma dissolves. We never resolve the bottom of the spectrum: (3.2) trades the null-vector
overlap for `eta || E[(Q+eta)^{-1}] ||` at a chosen `eta = o(1)` that is still `>> D^{-1}`. At
`z = -eta` the spectral parameter sits OUTSIDE the support (negative real axis), at distance
`eta >= D^{-1+eps}` from the hard edge — the easiest regime for any local law (the resolvent is
PSD and bounded, `Im m -> 0`, large deviations are simplest off the support). The hard-edge density
`rho ~ x^{-1/2}` enters only through the scalar `m(-eta) ~ eta^{-1/2}`; the genuinely hard object
(isotropic delocalization of the bottom singular vector at scale `D^{-1}`) is never invoked.

**(b) Deformation by `B`.** Handled by Section 2: `Q = B^*(AA^*)B` is the [KY17] separable model
with `Sigma = P_{E^perp}`. The projection is rank-deficient (its kernel `E` violates the usual
`c <= Sigma`), but the kernel decouples (block-diagonal, point 2(a)) and is invisible on `E^perp`,
where `Sigma|_{E^perp} = I_D` makes the deterministic equivalent the scalar `m(z) I`. `B` is a
fixed, low-complexity (orthonormal-columns) deformation; the local-law constants are uniform over
all such `B`, so no "atypical `E`" is excluded and the conditional bound holds for every shared span.

**(c) Expectation suffices; the rare event is free.** Two ways the `L^2`/expectation target is
weaker than the full high-probability local law, both exploited:
  - The PSD route (3.2) needs only the EXPECTED resolvent `E[(Q+eta)^{-1}|E]`, i.e. the local law
    *in mean* — no almost-sure or simultaneous-in-`w` control. The operator norm of a single
    deterministic matrix is read off from the isotropic estimate by a net.
  - If one prefers the high-probability form `<w,(Q+eta)^{-1}w> = m(-eta)(1+o(1))` on a good event
    `Omega` with `P(Omega^c) <= D^{-100}`, then for fixed `w`,
    `E[|<u,w>|^2] <= E[eta<w,(Q+eta)^{-1}w>; Omega] + P(Omega^c)·1 <= sqrt(eta)(1+o(1)) + D^{-100}`,
    the bad event killed by the trivial `|<u,w>|^2 <= 1` (the codimension-`(D-1)` cap is harmless
    in `L^2`). Either way `o(1)` follows.

## 6. Why `o(1)` and not the sharp `polylog(D)/D`; what the assembly actually needs

The bound (4.1) is capped at `sqrt(eta) >= sqrt(D^{-1+eps}) = D^{-1/2+eps/2}`: the monotone Lemma
(3.1) over-counts the bulk, `eta(Q+eta)^{-1} = u u^* + (bulk ~ sqrt(eta))`. Reaching the numerically
true rate `E|<u,w>|^2 ~ 1/D` (`residual_nogaps.md` numerics, and `scratchpad`) would require
`eta ~ D^{-2}` — below every local law — i.e. genuine HARD-EDGE ISOTROPIC EIGENVECTOR
delocalization `|<u,w>|^2 ≺ polylog(D)/D` for the bottom null vector. That statement is at the
boundary of the published literature (a theorem to write, parallel to the TAIL), and the Lemma
does NOT deliver it.

It is not needed. The assembly in `keystone_tail.md` Section 3 uses only the mean
`mu1 = E|rho|^2`, and tolerates `mu1 = o(1)` (not just `O(1/D)`) with the geometric-mean cut
`eta_* := sqrt(mu1)` in place of the note's `D^{-1/2}`:
  - Claim A(ii): `E[X^{-a}; y_1 < X <= 1/2] <= 2 y_1^{-a} mu1 = o(1)`.
  - Claim B, band `{1/2 < X <= 1-eta_*}`: `<= 2^a P{1-X >= eta_*} <= 2^a mu1/eta_* = 2^a sqrt(mu1)
    = o(1)`; band `{X > 1-eta_*}`: `<= O(eta_*) = O(sqrt(mu1)) = o(1)`.
  - Claim A(i) (singular part, via the tuned tail) is unconditional.
So `E[X^{-a}] <= 1 + O(sqrt(mu1)) = 1 + o(1)`. Section 4 supplies `mu1 <= E_E lambda_max(M_E) <=
sqrt(eta) = o(1)` (take `eta = (log D)^{-1}`, giving `mu1 = O((log D)^{-1/2})`, hence
`sqrt(mu1) = O((log D)^{-1/4}) -> 0`). The keystone closes.

## 7. Verdict

**Proved, conditional on citation.** `(DELOC-EXP)` — `lambda_max(E[u u^* | E]) = o(1)`, in fact
`<= (1+o(1)) sqrt(eta)` for any `eta in [D^{-1+eps},1)` — follows from:
  1. the elementary resolvent-monotonicity Lemma (3.1)/(3.2) (proved here, not a cited theorem);
  2. the anisotropic local law [KY17] (isotropic [BEKYY14] in the Gaussian sub-case) for the
     deformed sample covariance `Q = B^*(AA^*)B`, used ONLY at `z = -eta` below the hard edge, in
     the easy outside-the-support regime, to get `|| E[(Q+eta)^{-1}|E] || = m(-eta)(1+o(1)) ~
     eta^{-1/2}`.
Plus the observation (Section 6) that `keystone_tail.md`'s assembly runs on `mu1 = o(1)`. Hence the
keystone (II.B universality upper side, and the Gumbel law) is closed conditional on citing
[KY17]/[BEKYY14].

**Honest residual (citation-level only, NOT a new local law).** Two items keep this from being a
verbatim one-line citation, both routine and strictly easier than a hard-edge eigenvector law:
  - [KY17] is stated for `Sigma` bounded below and on spectral domains around the bulk/soft edge;
    we use `Sigma = P_{E^perp}` (rank-deficient, kernel decouples — point 2(a)) and `z = -eta`
    just below the hard edge (outside support). This is a mild extension of the stated theorem
    (same proof; the off-support regime is where local laws are easiest), not a new result.
  - The exact-zero eigenvalue of `Q` is deterministic (rank `<= D-1`); the local law is applied to
    the resolvent, which sees it only through `lambda_min(Q) = 0` entering `m(-eta)` continuously.

The previously-feared object — hard-edge isotropic delocalization of the bottom null vector at the
sharp `polylog(D)/D` scale — is NOT required for the keystone and is deliberately avoided. This is a
strict improvement on `residual_nogaps.md`'s verdict ("must be written, boundary of the literature"):
the monotone Lemma converts that hard object into the easy off-support resolvent, and the `o(1)`
rate it yields is enough.

Suggested bib (already in `residual_nogaps.md`): [KY17] Knowles–Yin, PTRF 169 (2017) 257–352;
[BEKYY14] Bloemendal–Erdős–Knowles–Yau–Yin, EJP 19 (2014) no. 33.

## 8. Numerical check (scratchpad, F=R, Rademacher/Gauss/uniform entries)

- Monotone bound (3.1): `|<u,w>|^2 <= eta<w,(Q+eta)^{-1}w>` held in every trial (`D=16,32,64`).
- `lambda_min(Q) = 0` to machine precision (`~1e-17`) — the exact null vector.
- `eta||E[(Q+eta)^{-1}]|| = 0.50, 0.46, 0.43` vs `sqrt(eta) = 0.60, 0.54, 0.49` (`eta=1/log D`):
  confirms (4.1)'s `~ sqrt(eta)` scaling.
- `m(-eta) sqrt(eta) -> 1` as `eta -> 0` (0.76 ... 0.98 at `eta=.3 ... .001`): confirms the
  hard-edge `m(-eta) ~ eta^{-1/2}`.
- True `E|<u,w>|^2 = 0.065, 0.033, 0.014 ~ 1/D`: the bound is valid and lossy by the hard-edge
  factor (Section 6), distribution-free across the three entry laws.
