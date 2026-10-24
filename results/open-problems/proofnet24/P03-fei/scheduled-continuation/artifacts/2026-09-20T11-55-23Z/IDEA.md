# PROB10-01 idea checkpoint — dependent recombination via Walsh uncertainty

Runtime model/effort requested by owner: GPT-6 / maximum. The exposed scheduler/runtime does not authenticate such a selector here, so model/effort is **UNVERIFIED**. This file changes no schedule, workflow, permission, visibility, notification, email, Drive object, or ownership.

Parent target remains full Friedgut–Kalai FEI for every Boolean function in every dimension. Status entering this bounded continuation: **OPEN**.

## Consumed live state before code

Required entrypoints were read from current `master`:

- `operations/PROB10_2026-09-20.md`;
- `proofnet24/P03-fei/README.md`.

Newest complete P03 owner report consumed:

- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-00-16+0300__fei-endpoint-onepoint-oblique-average.md`.

Newest complete scheduled report consumed:

- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T10-30-50Z__report.md`.

Newest checker/output then present and consumed:

- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__check_recombination_dominated.py`;
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__recombination_dominated_check.json`.

The output reports PASS through all 262,948 coordinate splits of all Boolean functions through dimension four for the candidate `JS_i <= B_i`, with equality on the controlled-character witness. This is self-check evidence only; no proof was imported from the checker.

The fresh-control theorem at commit `ef1087448014f0f6e5c9b4671c200a4020d8e3ea` remains restricted to `Gamma_c`, `c>=3`, `2^{-c}M_0(f)<=1`; `Gamma_c` appends variables and is not a fixed-domain derivative transition. The rare-controls/quadratic-coupling/affine-variance/balanced-substitution correction chain remains in force. All owner-listed false shortcuts remain retired.

## New idea and precise gap before code

For one physical coordinate, write each parent Fourier fibre as `(u,v)`, `w=u^2+v^2`, and normalize `p=(u^2,v^2)/w`. The two child restrictions apply the normalized two-point Walsh transform, producing a second probability vector `q`. The already observed identity is

`Delta_i H = B_i + JS_i`,

where `B_i` is the weighted entropy of `p` and `JS_i` is the weighted entropy deficit `1-H(q)`. The two-dimensional entropic uncertainty relation gives `H(p)+H(q)>=1`, hence **pointwise on every fibre**

`0 <= JS_i <= B_i`.

The main new route is to stop treating this as a one-coordinate accident. For any codimension-`k` affine restriction `pi(x)=a`, the parent Fourier spectrum decomposes into `2^k`-point cosets of `ker(pi)^perp`, and the `2^k` child restrictions are related to each parent coset by a normalized Walsh-Hadamard transform. Sharp Hausdorff–Young/Riesz–Thorin differentiation should give the exact all-dimensional block inequality

`B_pi <= Delta_pi H <= 2 B_pi`,

where `B_pi = H(S | S + ker(pi)^perp)` is the conditional spectral entropy inside those Fourier cosets. This removes every independence/control hypothesis from the recombination step and extends the live one-bit checker to arbitrary dependent affine blocks.

For an ordinary physical stopping tree this should imply, exactly,

`H_L + R_T <= H(f) <= H_L + 2 R_T`,

and for a full tree

`R_T <= H(f) <= 2R_T`, hence `R_* <= H <= 2R_*`.

This would make the hereditary allocation functional `R_*` constant-factor equivalent to full Fourier entropy without the previous additive `(2/ln 2) I` recombination payment. It still does **not** prove `R_* <= K I`; that remains FEI-hard.

## Three materially different attacks in this run

### A. Scalar binary uncertainty / exact one-coordinate domination

Give an analytic proof of the checker target `JS_i<=B_i`, independent of finite enumeration. A simple route is the sharp binary inequality `h_2(x)>=4x(1-x)`: if `t=min(u^2,v^2)/w` and `q=1/2+sqrt(t(1-t))`, then

`1-h_2(q) <= 4t(1-t) <= h_2(t)`.

This also identifies the sharp equality geometry.

### B. Arbitrary block / affine-coset recombination

Use the `2^k x 2^k` Walsh matrix and a self-contained Riesz–Thorin differentiation argument to prove `H(p)+H(Wp-amplitudes)>=k` for every real unit vector. Insert that fibrewise into the exact block restriction entropy identity. This is a new mechanism beyond a scalar constant: fully dependent branches, arbitrary block size, and no fresh variables.

### C. Try to turn block freedom into a universal allocation selector

Test whether allowing blocks can bypass known bad single-coordinate geometries via a dimension-free nontrivial selector of the form

`B_A <= K sum_{i in A} Inf_i`

for some proper queried block `A` chosen from the current state. This is only useful if `A` is genuinely smaller than the whole remaining cube and the choice is hereditary. Stress-test against one-point, addressing, bent/quadratic, coded, tensor, majority-substitution, and fresh-control families. If the only universally safe choice degenerates to `A=[n]`, record the obstruction rather than call it progress.

## Precise remaining full-scope gap

Even if A and B succeed, full FEI remains exactly the missing universal hereditary allocation estimate

`R_*(f) <= K I(f)`

(or an equivalent fully paid selector/global accumulated allocation theorem) for one finite universal `K`. The new recombination theorem would remove the separate dependent-branch payment obstacle, not the allocation obstacle itself.
