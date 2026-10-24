# POS3 account03/B10 — endpoint 4/9 atom and exact insertion-cut moment law

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability lies in `[1/3,2/3]` under the uniform law on all linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh collective state and peer results actually consumed

The current owner control `2026-09-22.2` supersedes this slot's former benchmark-validation role and assigns account03/B10 to POS3: apply bounded-width/high-variance results to the exact width-three target and derive the exceptional-case requirement with constants and hypotheses explicit.

The newest named partner result consumed is

`proofnet24/collective-POS3/account04/B11/B11-20260922T011236Z-pos3-r12/REPORT.md`

(blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`).  It pins the surviving range to `7<=pi(P)<=K_3` in a hypothetical counterexample, using Peczarski's solved 6-thin case and Aires--Kahn's qualitative bounded-width theorem, and proves that bounded range/variance/insertion multiplicity plus connectedness and module-primality do **not** imply a finite kernel: an arbitrary-size width-three prime interval-order family already exists at `pi=7`.  Therefore the next valid step must use a genuinely no-balanced-specific probability constraint rather than another compactness/census shortcut.

I also consume the partner's preceding report

`proofnet24/collective-POS3/account04/B11/B11-20260922T001443Z-pos3-r1/REPORT.md`

(blob `f4b7ca2b9a3902e527f9d30de8cb8ea043f670d4`), which proves the boundary-product refinement, the generic canonical-rank atom `>16/6561`, and the one-element deletion mean `E W_x<6561/16` in a hypothetical counterexample.

A newer compatible integrator result appeared during this invocation and was consumed before finalization:

`proofnet24/collective-POS3/account04/B20/20260922T011156Z-b20-auto11/REPORT.md`

(blob `b6b06537e4543c606c96d3f159567192fc0daeac`).  It proves an exact lower-fringe-minus-upper-fringe formula for nested chain-profile swap defects and proves that an entire strong-majority same-chain block stays in its canonical gap relative to either other chain with probability `>1/3`, independent of block length.  This sharpens the eventual transfer target to a two-boundary charge, not a product of local distortion factors.

The external bounded-width source is Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1 (30 Oct 2025).  The qualitative `K_3` is not assigned a numerical value here.  No benchmark gold, answer key, FEI proof material, or solver/evaluator state is used.

## 2. Strong-majority endpoints have atom greater than `4/9`

Assume `P` has width at most three and no balanced incomparable pair.  For `x in P` define

`D_x={y!=x : Pr(y precedes x)>2/3}`,

`U_x={y!=x : Pr(x precedes y)>2/3}`.

As in the consumed B11 argument, `D_x,U_x` partition `P-{x}`, with `D_x` an ideal and `U_x` a filter.

Suppose `D_x` is empty, so `x` is the lower endpoint of the common strong-majority order.  Put `B=min(U_x)`.  Since `B` is an antichain and `P` has width at most three, at most **two** members of `B` can be incomparable with `x`; otherwise `x` together with three such members would be a four-element antichain.  Every `b in B` comparable with `x` is forced above `x` and contributes probability `1`; every incomparable `b` satisfies `Pr(x precedes b)>2/3`.

Shepp's XYZ inequality therefore gives

`Pr(x precedes every b in B) >= product_{b in B} Pr(x precedes b) > (2/3)^2 = 4/9`.

Preceding every minimal member of the finite filter `U_x` forces `x` below every member of `U_x`; because `D_x` is empty, this is exactly the event that `x` is first in the full extension.  The case `U_x` empty is symmetric.

### Theorem 2.1 — strengthened endpoint atom

At either endpoint of the common strong-majority order of a width-three counterexample,

`Pr(endpoint occupies its canonical extreme rank) > 4/9`.

This strengthens the `>8/27` endpoint estimate in the earlier B11 report.  Let `Q=P-x`, let `tau` be uniform in `L(Q)`, and let `W_x(tau)` be the exact number of legal gaps for reinserting `x`.  The insertion identity gives

`e(P)=sum_tau W_x(tau)`.

At a lower endpoint, every extension of `Q` has exactly one lift with `x` first, hence

`Pr_P(x first)=e(Q)/e(P)=1/E_Q W_x`.

Therefore

`E_Q W_x < 9/4`,                                                   `(2.1)`

and in particular

`E_Q(W_x-1) < 5/4`.                                                `(2.2)`

The upper endpoint is identical after order reversal.

## 3. Exact minority-error identity under the true uniform deletion law

Fix any `x` with no balanced incomparable partner and put `Q=P-x`.  For

`tau=(q_1,...,q_n) in L(Q)`

define

`a=max({pos_tau(q):q<_P x} union {0})`,

`b=min({pos_tau(q)-1:x<_P q} union {n})`,

`W=b-a+1`.

The elements `q_{a+1},...,q_b` form the insertion corridor and are all incomparable with `x`.  Write `I(x)` for the incomparability set and `m_x=|I(x)|`.

Define the baseline forced-majority-error count

`R_x(tau)=#{u in U_x intersect I(x):pos_tau(u)<=a}`

`          +#{d in D_x intersect I(x):pos_tau(d)>b}`.

Number corridor positions relatively by `t=1,...,W-1`, and set

`C_x(tau)=W R_x(tau)`

`          + sum_{q_{a+t} in D_x} t`

`          + sum_{q_{a+t} in U_x} (W-t)`.

For `y in D_x`, the minority event is `x precedes y`; for `y in U_x`, it is `y precedes x`.

### Lemma 3.1 — exact insertion-cut identity

With `mu_x=E_Q W_x`,

`sum_{y in D_x intersect I(x)} Pr_P(x precedes y)`

`+ sum_{y in U_x intersect I(x)} Pr_P(y precedes x)`

`= E_Q C_x / mu_x`.                                                `(3.1)`

**Proof.**  A baseline-error element is reversed in every one of the `W` lifts of `tau`.  A corridor element in `D_x` at relative position `t` is reversed in exactly the first `t` insertion gaps, while a corridor element in `U_x` is reversed in exactly the final `W-t` gaps.  Thus `C_x(tau)` is exactly the sum, over all lifts of `tau`, of the number of majority-oriented incomparable pairs involving `x` that are reversed.  Summing over `tau` and dividing by `e(P)=e(Q)mu_x` proves `(3.1)`. `□`

In a counterexample every summand on the left of `(3.1)` is strictly below `1/3`; hence the genuinely no-balanced-specific constraint is

`E_Q C_x < (m_x/3) mu_x`.                                         `(3.2)`

This is under the **uniform** law on `L(P-x)`, so it does not make the invalid uniform-projection substitution refuted by the insertion-recurrence work.

## 4. Quadratic insertion-moment obstruction

For one fixed corridor, let `p` of its `W-1` elements carry the `D_x` label and `q` carry the `U_x` label.  Ignoring the nonnegative baseline term, the variable cost is minimized by placing all `D_x` labels first and all `U_x` labels last.  The minimum for fixed `(p,q)` is

`p(p+1)/2 + q(q+1)/2`.

Minimizing over `p+q=W-1` gives exactly `floor(W^2/4)`.  Consequently

`C_x(tau) >= floor(W_x(tau)^2/4)`                                  `(4.1)`

for every fiber.  Combining `(3.2)` and `(4.1)`, and using `floor(W^2/4)>=(W^2-1)/4`, yields:

### Theorem 4.1 — no-balanced second-moment constraint

`E_Q[W_x^2] < (4m_x/3) E_Q[W_x] + 1`.                             `(4.2)`

Using the earlier B11 generic mean `E_Q W_x<6561/16`,

`E_Q[W_x^2] < (2187/4)m_x + 1`.                                   `(4.3)`

The newest partner result shows why `(4.2)` must not be interpreted as a finite-kernel theorem: even `pi=7` and uniformly bounded insertion fibers allow arbitrary size.  Its value is instead that `(4.2)` is a probability constraint specific to the assumed absence of a balanced pair and carries the majority orientation needed by the nested-fringe transfer.

If Aires--Kahn's qualitative theorem is invoked, `m_x<=K_3` in a hypothetical counterexample and `(4.3)` becomes a uniform finite second-moment bound, but no numerical `K_3` is claimed.

## 5. Endpoint factorial-moment law

At a lower strong-majority endpoint `D_x` is empty.  Then `a=0`, the baseline term vanishes, and every corridor element lies in `U_x`.  Hence exactly

`C_x(tau)=W(tau)(W(tau)-1)/2`.

The upper endpoint is symmetric.  Therefore

`sum_{y||x} minority_probability(x,y)`

`= E_Q[W(W-1)] / (2 E_Q W)`.                                      `(5.1)`

Using the strict `<1/3` minority bounds and `(2.1)` gives

`E_Q[W(W-1)] < (2m_x/3)E_Q W < 3m_x/2`,                           `(5.2)`

`E_Q[W^2] < 3m_x/2 + 9/4`,                                        `(5.3)`

and, for every integer `t>=2`,

`Pr_Q(W>=t) < 3m_x/(2t(t-1))`.                                    `(5.4)`

Thus the strong-majority endpoints of a counterexample have an exact insertion-fiber budget with mean below `2.25`, not merely a qualitative bounded-variance statement.

## 6. How this changes the current two-boundary route

The newest B20 result writes every context-sensitive nested chain-profile swap defect as a lower-fringe charge minus an upper-fringe charge and proves `>E/3` canonical-gap mass for whole strong-majority chain blocks.  The present result supplies an orthogonal no-balanced-specific control on one-element fibers:

- global majority-error mass is exactly `E C_x/E W_x`;
- `C_x` dominates `floor(W_x^2/4)`;
- the two global strong-majority endpoints satisfy the stronger `4/9` extreme-rank atom and `E W_x<9/4`;
- their factorial insertion moment is explicitly bounded by `(5.2)`.

A valid successor can therefore charge a proposed width-two reflection/exchange simultaneously against the B20 lower/upper fringe decomposition and the cut-cost budget `(3.2)`, rather than treating insertion multiplicity as an arbitrary bounded density.  This directly respects the newest partner warning that bounded local state alone does not compactify the problem.

The next unpaid implication is still global: sum the two-boundary defects across consecutive strong-majority blocks and prove that all required orientations cannot retain the same sign while every element also satisfies the cut-cost inequalities, or construct a genuine width-three family satisfying the complete system and identify the missing invariant.

## 7. Deterministic regression

The standard-library checker `verify_insertion_moment.py` was run before repository delivery.  It exhausts every distinct transitively closed strict relation compatible with the natural order through six vertices, restricts to width at most three, enumerates all linear extensions exactly, and checks every local `(P,x)` with no balanced incomparable partner.

Archived `CHECK_OUTPUT.txt` reports:

- `3702` width-at-most-three posets through `n=6`;
- `2419` qualifying local `(P,x)` cases;
- `1662` endpoint cases;
- exact identity `(3.1)` in every qualifying case;
- pointwise bound `(4.1)` in every fiber;
- generic moment inequality `(4.2)` in every qualifying case;
- endpoint atom `>4/9`, mean `<9/4`, and factorial-moment inequality in every endpoint case;
- smallest observed endpoint atom `10/19`;
- largest observed endpoint mean `19/10`;
- final marker `POS3_INSERTION_MOMENT_CHECK_PASS`.

This finite enumeration is regression evidence only.  Sections 2--5 are the proofs.

## 8. Status

- Endpoint atom strengthened from `>8/27` to `>4/9`: **PROVED**.
- Endpoint mean insertion multiplicity strengthened from `<27/8` to `<9/4`: **PROVED**.
- Exact insertion-cut minority identity `(3.1)`: **PROVED**.
- Generic no-balanced second-moment constraint `(4.2)`: **PROVED**.
- Endpoint factorial-moment constraints `(5.1)--(5.4)`: **PROVED**.
- Finite-kernel shortcut from bounded range/variance/fibers: **still REFUTED**, consistent with the newest B11 family.
- Full POS3 target: **OPEN / NOT PROVED**.

No novelty/priority claim, benchmark result, FEI claim, public release, key material, credential use, scheduler mutation, email/Drive action, paid model/API/Codex use, or remote workflow dispatch is made.
