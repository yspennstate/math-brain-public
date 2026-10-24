# B01 / A003 — dual-total-correlation endpoint and counterfamily normal form

**Run:** `20261012T031242Z-account01-B01-dual-tc-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-CRITICAL-STEP` / `G-R-SELECT`  
**Status:** new restricted endpoint and sharper normal form author-proved,
pending A086/A094 review. Full FEI remains **OPEN**.

## 1. Bounded objective and prior value

The prior A003 result gave the exact restriction split

\[
\Delta_iH=E_i+J_i,
\quad E_i=H(1_{\{i\in S\}}\mid S\setminus\{i\}),
\quad J_i=\operatorname{JS}(r_+,r_-),
\]

with `J_i <= (2/ln 2) min(I_i,1-I_i)`. A001 then reduced any possible
counterfamily to restriction-critical, tensor-prime functions and proved
that a high-ratio member has every influence exponentially small in `H/I`.
The remaining obstruction was that coordinate diffusion alone supplies no
contradiction.

This run asks for the first nonlocal information constraint forced by
restriction-criticality, while keeping the rare logarithms and physical
restriction terms intact.

## 2. PROVED: global dual-correlation payment

Let `X_i=1_{i in S}` under the Fourier spectral law and define

\[
\mathsf D^\vee(S)=H(S)-\sum_iH(X_i\mid X_{-i}).
\]

For every coordinate order,

\[
\mathsf D^\vee(S)=\sum_i I(X_i;X_{>i}\mid X_{<i})\ge0.
\]

If `f` is restriction-critical, meaning
`Delta_i H >= (H/I) I_i` for every relevant coordinate, then summing the
exact split gives

\[
\boxed{
0\le\mathsf D^\vee(S)
\le\sum_iJ_i
\le\frac2{\ln2}\sum_i\min\{I_i,1-I_i\}
\le\frac2{\ln2}I(f).}                                               \tag{2.1}
\]

No local term is reused: (2.1) is one global sum of the physical
restriction Jensen–Shannon remainders.

## 3. PROVED: a dimension-independent restricted endpoint

For every fixed `epsilon>0`, every restriction-critical genuine Boolean
function whose spectral law satisfies

\[
\mathsf D^\vee(S)\ge\varepsilon H(S)
\]

obeys

\[
\boxed{H(f)\le\frac2{\varepsilon\ln2}I(f).}                          \tag{3.1}
\]

This is a genuine class theorem, not an FEI restatement: the normalized
dual-correlation lower bound is an additional structural hypothesis and is
not preserved by admission of an arbitrary tensor factor.

Conversely, every restriction-critical sequence with `R_k=H/I -> infinity`
must satisfy

\[
\boxed{
\frac{\mathsf D^\vee(S_k)}{H(S_k)}
\le\frac2{R_k\ln2}\to0.}                                            \tag{3.2}
\]

Combining this with the prior source-pinned descent sharpens the potential
counterexample normal form. If FEI is false, a genuine Boolean counterfamily
can be chosen simultaneously:

- restriction-critical;
- tensor-prime;
- exponentially diffuse, `max_i I_i <= e^3 2^(-H/I)`;
- asymptotically zero in normalized spectral dual total correlation.

The combined statement inherits the pending review status of the A001
critical-prime and diffuse reductions. Equation (2.1) itself is proved
directly in `DUAL_TC_ENDPOINT.tex`.

## 4. Exact movement and remaining estimate

**Previous tracked value:** the residual class was only known to have
`max_i I_i <= e^3 2^(-R)`; no global dependence statistic was controlled.

**New value:** every member additionally satisfies

\[
\mathsf D^\vee/H\le 2/(R\ln2).
\]

Thus an unbounded-ratio family must become spectrally almost independent in
the normalized dual-correlation sense even though it remains tensor-prime as
a Boolean function.

The first unsupported universal line is now:

> Bound `R` on genuine Boolean functions that are restriction-critical,
> tensor-prime, exponentially coordinate-diffuse, and have
> `D^vee(S)/H(S)` tending to zero; or derive a Booleanity consequence that
> contradicts this simultaneous regime.

Small dual total correlation alone cannot be declared sufficient. A future
argument must exploit the complete signed Boolean autocorrelations or a
nonlocal physical payment, and must survive near tensors and activation
equivalence.

## 5. Mandatory controls

| Control | Outcome |
|---|---|
| Sparse one-point defects | For `q_n`, `D^vee/H -> 1/2` and `H/I -> 4`; the rare logarithms remain visible and no false contradiction occurs. |
| Addressing/multiplexers | Their bounded-ratio behavior is compatible; no fresh-selector result is reproposed. |
| Exact tensors | `D^vee`, `H`, and `I` are additive. The restricted hypothesis in (3.1) is an entropy-weighted factor condition, not arbitrary-seed admission. |
| Near tensors | Not excluded; they prohibit treating tensor-primality as a quantitative dependence gap. |
| Actual prime gates | Two-bit AND has an independent uniform spectral law and `D^vee=0`, showing tensor-prime Booleanity alone does not imply positive dual correlation. |
| Parity-zero erasure | Parity has `H=D^vee=0`; the theorem is interpreted without dividing by `H`. |
| Shared variables | No composition or disjointness claim is made beyond the explicit tensor diagnostic. |
| Activation equivalence | Rarity and low influence alone remain FEI-hard; (3.1) requires the additional dual-correlation fraction. |
| Weighted physical TC | `WEIGHTED_TC` concerns conditional biased input laws, whereas (2.1) concerns the Fourier spectral indicator vector. No refuted physical-TC payment is revived. |

## 6. Verification

Command:

`python3 verify_dual_tc_endpoint.py`

The checker imports no earlier campaign code. It reconstructs genuine Boolean
truth tables, integer Walsh spectra, physical restrictions, conditional
spectral entropies, and `J_i=Delta_iH-E_i`.

Observed result: **PASS**, with 4,165 function checks, 1,681
restriction-critical functions, and 256 exact-product additivity checks.
Coverage includes every nonconstant Boolean function through dimension three,
4,096 deterministically generated dimension-four masks giving 3,872 unique
nonconstant tables, point defects through
dimension ten, parity through dimension eight, addressing for one and two
address bits, majority-three, two-bit AND, an exact tensor, and a one-point
near-tensor surgery. Arithmetic uses exact integer Walsh transforms and
`Fraction` marginals with 80-digit decimal logarithms. There is no randomness.

Finite computation checks normalization and signs. The all-dimensional proof
is the chain rule plus the exact restriction split in Sections 2–3.

## 7. Source pins and scope

- A003 endpoint source: open-problems run
  `20261011T210729Z-account01-B01-minimal-target-a003`, report blob
  `85308728bbfffe5cd3afd554cae783110fc57035`, proof blob
  `3fd599db6c06961773ba9e89e9a8bd508240c689`.
- A001 critical-prime source: open-problems commit
  `c8c6b995401f238e67317ab4d5b44aea6173a845`, report blob
  `662411dfae5b8d91d0b07e449c59274537492500`.
- A001 critical-diffuse source: open-problems run
  `20261012T021256Z-account01-B01-critical-diffuse-a001`, proof blob
  `c266c0a5456b32a110e8d0b20cea7c54433c6c92`.
- B01 contract blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`;
  protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
  stream-index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.

No literature novelty or priority claim is made. This is a source-bound new
campaign deduction from the exact physical restriction identity.

## 8. Disposition

- `B01-A003-DUAL-TC-PAYMENT-v1`: **AUTHOR_PROVED_PENDING_REVIEW**.
- `B01-A003-DUAL-TC-RESTRICTED-FEI-v1`: **AUTHOR_PROVED_PENDING_REVIEW**.
- Combined four-property counterfamily normal form: **AUTHOR_PROVED_PENDING_REVIEW** because its A001 dependencies remain pending.
- Independent review: A086/A094 requested.
- Model: Codex as exposed; runtime version and reasoning-effort metadata were not exposed.
- Subagents: none.
- Scheduler/shared-registry/graph mutation: none.
- Native Brain ingestion: not claimed.
- Full FEI: **OPEN**.

