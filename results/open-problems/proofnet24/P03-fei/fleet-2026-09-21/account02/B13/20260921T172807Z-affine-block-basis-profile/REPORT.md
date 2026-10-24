TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T17:28:07.083804Z — affine block-basis influence profile, exact FEI equivalence, and collision/shell residual localization

**Status:** full uniform-cube Friedgut–Kalai Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No genuine retrieved brain context was consumed.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. **Configured/known reasoning level:** UNKNOWN / not exposed. **Provider reasoning usage:** null / not exposed.

## 0. Fresh state, scope, and creative moves

Live `yspennstate/math-research-brain` control was resolved at `main` commit `ae81c6d299799245d73b53c7c27047f84e19a48e`, OWNER CONTROL revision `2026-09-21.1`. I read `AGENTS.md`, `scheduled_tasks/README.md` including the full OWNER MESSAGE, `fleet.json`, `roles.json`, and `PROTOCOL.md`. No account02/B13 pause or stop was present. The later direct owner order `FEI-SEVEN-TASKS-2026-09-21` governs B13 despite the stale provisional benchmark row in `roles.json`.

I then read the owner-required FEI files in order: `TASKS_2026-09-21.md`, then the read-once continuation `REPORT.md`, then `APPROACHES.md`, followed by the fresh P03 FEI README and `FLEET_RULES.md`. The current owner-corrected unrestricted lower-bound scale is already `C_FEI > 6.521845710923046575`; the old `6.4547837` unrestricted target is obsolete.

The newest directly relevant dependencies consumed were:

- B13's preceding one-point-defect block-profile report, which proves simultaneous sharpness of the local two-sided block caps and refutes a fixed-fraction macroscopic projection-credit bridge;
- account02/B14's centered/refunded selector, in particular its restriction selector and the current threshold `rho(6.521845710923046575)=0.3156061323581677`;
- account02/B15's valuation-tail majorization and its warning that arithmetic/product interpolants still need negative information credits;
- account02/B18's arbitrary-q-flip dependent-triple/Radon frame result, which already owns the q-flip transport/phase-packing direction;
- the fresh account03/B12 global zero-depth rigidity theorem, which identifies exact zero Palm-depth defect with one-point defects and refutes a dimension-independent positive rigidity gap.

I used three FLEET_RULES moves that are different from the preceding local-cap/projection run:

1. **#1 CHANGE THE CATEGORY:** replace coordinate influence by a minimum-weight basis problem in the vector matroid of all block translations;
2. **#19 MAKE IT AN ALGORITHM:** solve that basis problem exactly by greedy selection and expose its rank-profile integral;
3. **#2 ATTACK THE NEGATION FIRST:** test the most obvious hoped-for affine-shell lower bound and kill it with an explicit bent Boolean family.

The tracked quantity moved from the ordinary coordinate influence `I(f)` to an **orbit-exact block profile** `I_aff(f)` which has the *same global FEI extremal constant* but imposes strong basis-exchange correlation constraints. This yields a new universal residual localization: any function above the current `6.521845...` scale must have large essential collision excess, while a minimal-dimensional violator must simultaneously have small first-shell ratio in every minimizing affine gauge.

---

## 1. Block translation correlations and affine-basis influence

Work on `G=F_2^n`. Let

`mu(xi)=fhat(xi)^2`

be the spectral law. For a translation `u in G`, define the genuine Boolean block disagreement and correlation

`q(u)=Pr_x[f(x) != f(x+u)]`,

`c(u)=E_x f(x) f(x+u)=1-2 q(u)=sum_xi mu(xi)(-1)^{<xi,u>}`.

A character multiplier can reverse the sign of `c(u)`, so the orientation-free cost of the block direction is

`qtilde(u)=min(q(u),1-q(u))=(1-|c(u)|)/2 in [0,1/2]`.

Define the affine-basis influence

`I_aff(f)=min_{T in GL(n,2), a in F_2^n} I( chi_a * (f o T) )`.

Here the multiplier is in the transformed coordinates. Fourier entropy is unchanged by this operation because the Fourier coefficients are only permuted and translated.

### Theorem B13-AFFINE-BLOCK-BASIS-01

For every Boolean `f`,

`boxed{ I_aff(f) = min_{B basis of F_2^n} sum_{u in B} qtilde(u) }`

and equivalently

`boxed{ I_aff(f) = 1/2 [ n - max_{B basis} sum_{u in B} |c(u)| ]. }`      (1.1)

Moreover the unrestricted FEI extremal constant is unchanged by replacing ordinary influence with `I_aff`:

`boxed{ sup_f H(f)/I(f) = sup_f H(f)/I_aff(f). }`                       (1.2)

The suprema omit the zero-denominator character cases, for which `H=0`.

### Proof

Fix `T`. Its columns `u_i=T e_i` form a basis of `G`. For

`g(x)=chi_a(x) f(Tx)`,

the `i`th coordinate correlation is

`E g(x)g(x+e_i)=(-1)^{a_i} c(u_i)`.

Because the bits `a_i` are independently selectable, the minimum possible `i`th influence for this basis is exactly

`(1-|c(u_i)|)/2=qtilde(u_i)`.

Summing and then minimizing over bases proves the first formula, and the second is algebraic rearrangement.

For (1.2), `I_aff(f)<=I(f)` gives

`sup H/I <= sup H/I_aff`.

Conversely, for every `f` choose an orbit representative `g=chi_a(f o T)` attaining `I(g)=I_aff(f)`. Entropy is invariant, so

`H(f)/I_aff(f)=H(g)/I(g)`

is already one of the ordinary FEI ratios. Taking the supremum gives the reverse inequality. QED.

### Meaning

This is not a structured-class relaxation. It is an **exact reformulation of the full FEI constant** in terms of the complete Boolean block-correlation profile `u -> c(u)`. Therefore one may, without changing the global problem, work in a basis that minimizes folded block influence.

---

## 2. Exact minimum-basis rank profile and two-sided exchange constraints

For `0<=t<=1/2`, let

`E_t={u != 0 : qtilde(u)<=t}`,

`r(t)=rank_F2(E_t)`.

### Theorem B13-BLOCK-RANK-PROFILE-02

`boxed{ I_aff(f) = integral_0^{1/2} [n-r(t)] dt. }`                    (2.1)

If `B={u_1,...,u_n}` is any minimum-cost basis in (1.1), then for every `i` and every

`v in span(B \ {u_i})`,

`boxed{ qtilde(u_i+v) >= qtilde(u_i) }`                               (2.2)

or equivalently

`boxed{ |c(u_i+v)| <= |c(u_i)|. }`                                    (2.3)

Thus each minimizing basis direction is the largest absolute Boolean correlation in its entire fundamental coset.

### Proof

The costs `qtilde(u)` define a weighted vector matroid. Greedy selection in nondecreasing cost gives a minimum-weight basis. At every threshold `t`, greedy has selected exactly `r(t)` basis vectors of cost at most `t`; otherwise it would fail to take a maximum independent subset of `E_t`. If the selected costs are `b_1,...,b_n`, then

`sum_i b_i = integral_0^{1/2} #{i:b_i>t} dt`

`             = integral_0^{1/2} [n-r(t)] dt`,

proving (2.1).

For (2.2), replacing `u_i` by `u_i+v` preserves the basis because `u_i+v` lies outside the span of the other `n-1` vectors. A lower cost would contradict minimality. Equation (2.3) is the identity `qtilde=(1-|c|)/2`. QED.

### Why this is useful for approach 2/13

The preceding B13 local caps constrain one block at a time and can be simultaneously sharp on one-point defects. Equations (2.1)–(2.3) instead impose a **global compatible family of two-sided block-correlation inequalities**: an optimal basis cannot have a cheaper parity hidden anywhere in a fundamental coset. This is precisely the kind of cross-block compatibility that the one-point-defect obstruction said was missing.

---

## 3. Essential-dimension quotient and a collision payment

The zero-cost directions

`Z={u : qtilde(u)=0}`

form a linear subspace: `qtilde(u)=0` means the spectral parity `(-1)^{<Xi,u>}` is deterministic, and products of deterministic parities are deterministic. Let

`d = n-rank(Z)`.

Equivalently, `d` is the affine dimension of the Fourier support. Entropy therefore satisfies

`H(f)<=d`.                                                            (3.1)

Let

`CP(mu)=sum_xi mu(xi)^2`,

`D_d = 2^d CP(mu)-1 >=0`.                                             (3.2)

`D_d` is the collision excess over the uniform law on an affine `d`-flat.

### Theorem B13-DIFFUSE-COLLISION-PAYMENT-03

For every Boolean `f`,

`boxed{ I_aff(f) >= 1/2 [ d - sqrt(d D_d) ]_+. }`                     (3.3)

Consequently, for any `0<=alpha<1`,

`D_d <= alpha^2 d`

implies the genuine FEI bound

`boxed{ H(f)/I(f) <= H(f)/I_aff(f) <= 2/(1-alpha). }`                 (3.4)

### Proof

For `z in Z`, the parity `(-1)^{<Xi,z>}` is constant on the spectral support. Hence

`|c(u+z)|=|c(u)|`.

So absolute correlations descend to the quotient `G/Z`, which has `2^d` elements. Parseval for `c`, divided by `|Z|`, gives

`sum_{u mod Z} |c(u)|^2 = 2^d sum_xi mu(xi)^2 = 1+D_d`.              (3.5)

The zero quotient class contributes `1`.

A minimum basis contains a basis of `Z` at zero cost plus `d` quotient-independent directions. If their absolute correlations are `w_1,...,w_d`, Cauchy–Schwarz and (3.5) give

`sum_j w_j <= sqrt(d sum_{u mod Z, u!=Z}|c(u)|^2)`

`             = sqrt(d D_d)`.

Insert this in the quotient form of (1.1),

`I_aff = d/2 - (1/2) sum_j w_j`,

and truncate the lower bound at zero to get (3.3). If `D_d<=alpha^2 d`, then `I_aff >= (1-alpha)d/2`; combine with `H<=d` to prove (3.4). QED.

### Current hard-scale corollary

At the owner-corrected scale

`C0=6.521845710923046575`,

set

`alpha_C0=1-2/C0`

`          =0.693338344902836254067296585569999948...`

and

`alpha_C0^2=0.480718060512604323411478660050184230...`.

Therefore **every** Boolean function with

`H(f)/I(f) > C0`

must satisfy

`boxed{ 2^d sum_xi mu(xi)^2 - 1 > 0.4807180605126043... d. }`         (3.6)

So any genuinely hard FEI example at the current scale is forced into a quantitatively **high-collision essential spectrum**. Near-flat spectra are already paid directly by the affine block-correlation profile.

This is complementary to B15: B15 controls packet valuation tails but leaves packet/mesh information credits; (3.6) says an above-current-scale obstruction cannot live in the low-collision sector at all.

---

## 4. Coupling to B14's restriction selector

Choose an affine-basis minimizer `g` of `f`. The character orientation in Theorem 1 may be chosen so every coordinate influence of `g` is at most `1/2`, while

`I(g)=I_aff(f)`.

Let

`W_1(g)=sum_i ghat({i})^2`,

`r_aff(g)=W_1(g)/I(g)`.

The current B14 selector proves that if `r_aff(g)=r>0`, then some coordinate `i` has

`Delta_i H(g) <= [F(r)+2/ln 2] Inf_i(g)`,                            (4.1)

with the explicit decreasing selector function `F` from B14.

The affine optimization makes this selector inductively legitimate rather than costing a factor at every change of basis:

### Proposition B13-AFFINE-SELECTOR-COMPILER-04

Fix `C`. Suppose every nonconstant Boolean function has an affine-basis minimizer `g` with a coordinate satisfying

`Delta_i H(g)<= C Inf_i(g)`.                                         (4.2)

Then full FEI holds with constant `C`.

### Proof

Induct on dimension. For the two physical restrictions `g_{i,+}`, `g_{i,-}`, induction gives

`H(g_{i,±}) <= C I_aff(g_{i,±}) <= C I(g_{i,±})`.

Using (4.2) and the exact influence restriction identity,

`I(g)=Inf_i(g)+1/2[I(g_{i,+})+I(g_{i,-})]`,

we get `H(g)<=C I(g)=C I_aff(f)<=C I(f)`. QED.

Thus at any candidate constant `C`, a minimal-dimensional violation of the affine reformulation must have `r_aff` below the B14 selector threshold in **every** minimizing affine gauge. At the current scale `C0`, B14's computed threshold is

`rho(C0)=0.3156061323581677`.

Combining with (3.6), a minimal-dimensional violation at `C0` is localized to the joint regime

1. `D_d > 0.4807180605126043... d` (high essential collision);
2. `r_aff < 0.3156061323581677` in every minimizing affine gauge (small first shell);
3. every minimizing basis obeys all fundamental-coset exchange inequalities (2.3).

This is a stricter universal residual class than either the raw B14 shell condition or the previous B13 one-block caps alone.

---

## 5. Decisive negative test: a fixed affine-shell lower bound is false

The simplest hoped-for completion would assert a universal `rho>0` with

`r_aff(g)>=rho`

for an affine-basis minimizer. This is false for genuine Boolean functions.

For even `n=2m`, take the quadratic bent function

`f(x)=(-1)^{x_1 x_2 + x_3 x_4 + ... + x_{n-1}x_n}`.

Its Fourier magnitudes are all `2^{-n/2}`, hence `mu` is uniform on `F_2^n`. Therefore

`H(f)=n`,

`c(u)=0` for every `u!=0`,

`I_aff(f)=n/2`,

and every affine gauge is again spectrally uniform. In particular

`W_1=n/2^n`,

so

`boxed{ r_aff=2^{1-n} -> 0. }`                                       (5.1)

Yet `H/I_aff=2`, and Theorem 3 pays this family exactly at the diffuse endpoint `D_d=0`.

So the route cannot be "prove a positive affine first-shell fraction". The viable form is a **dichotomy**: low shell must be paired with a diffuse/collision payment, while the remaining high-collision + low-shell sector needs a different Boolean mechanism.

The one-point-defect family sits at the opposite boundary: it is high-collision and has tiny first-shell ratio, while the fresh account03/B12 result identifies it as the exact zero Palm-depth configuration. B12 also proves there is no dimension-independent positive gap away from that equality family. Therefore the next bridge must distinguish high-collision/low-shell spectra by something finer than either shell mass or zero-depth slack alone.

---

## 6. Exact engineering self-check

`affine_block_basis_checker_v2.py` is standard-library only and exhausts every Boolean function modulo global output sign for `n<=4`.

It verifies exactly, with rational/integer arithmetic:

- 32,906 instances of the correlation-basis formula (1.1);
- 32,906 instances of the rank-integral formula (2.1);
- 1,050,146 fundamental-coset exchange inequalities (2.2);
- 32,906 quotient-sharp collision lower bounds (3.3).

Total exact checks: **1,181,770**, all PASS.

The archived diagnostics also reproduce the current hard-scale collision coefficient

`0.480718060512604323411478660050184230...`

and the bent-family decay `r_aff=2^{1-n}` through `n=20`.

The earlier same-run checker file used the ambient dimension in the collision estimate; it is valid but weaker when exact spectral periods/dummy directions exist. The `v2` checker contracts the zero-cost subspace and is the report's authoritative version.

---

## 7. What this does and does not settle

**Proved this run:** an exact full-FEI-equivalent minimum block-basis formulation; its greedy/rank-profile identity; its two-sided fundamental-coset correlation constraints; a quotient-sharp diffuse-spectrum FEI payment; an explicit high-collision necessary condition above the current lower-bound scale; and an affine restriction compiler importing B14 without repeated change-of-basis loss.

**Refuted this run:** any universal positive lower bound on the minimizing affine first-shell ratio, by the quadratic bent Boolean family.

**Not proved:** a dimension-independent FEI constant. The residual high-collision + low-shell sector remains open.

### Next precise target

Use the minimum-weight basis `B` and the quotient rank filtration `E_t` to build a **multiscale restriction payment indexed by rank jumps**, rather than by coordinate depth. The candidate must pay the high-collision/low-shell residual while surviving both boundary tests:

- bent/near-flat spectra, already paid by Theorem 3;
- one-point-defect and B12's near-rigidity perturbations, where local caps and fixed positive depth gaps fail.

A promising interface is to charge entropy at a rank-jump `t` only to correlations in the fundamental cosets from (2.3), then seek a bounded-overlap sum over the matroid rank filtration. This stays complementary to B18's q-flip transport frame and B15's packet valuation tail.
