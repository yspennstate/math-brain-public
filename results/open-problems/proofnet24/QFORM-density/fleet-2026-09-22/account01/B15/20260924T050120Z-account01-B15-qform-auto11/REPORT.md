# account01/B15 — regularity separation at the exact target

Run: `20260924T050120Z-account01-B15-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5` / current control `2026-09-22.15`.  
Status: **FULL QFORM OPEN**. Supporting theorem proved below. Execution: `WITHOUT_VERIFIED_BRAIN`.

## New theorem: no target-uniform modulus of continuity, even for smooth compactly supported inputs and A=I_3

### Theorem (`QFORM-NO-UNIVERSAL-C0-MODULUS-EVEN-SMOOTH-v1`)

There is a sequence `s_k -> infinity` and, for each `s=s_k`, an iid triple `X_{s,1},X_{s,2},X_{s,3}` with a common density `\tilde f_s` satisfying

- `\tilde f_s in C_c^infinity(R)`,
- `0 <= \tilde f_s <= 1`,
- `supp \tilde f_s subset [0,2.6]`,
- `int \tilde f_s = 1`,

such that for

`Q_s = X_{s,1}^2 + X_{s,2}^2 + X_{s,3}^2`

(the exact owner target with `A=I_3`, eigenvalues `1,1,1`) the density `p_s` obeys

`p_s in C_c(R),   ||p_s||_infinity <= pi/4,   supp p_s subset [0,21]`,

but the family `{p_s}` is **not equicontinuous**. More quantitatively,

`|\widehat p_s(s)| >= 1/125`

for all sufficiently large `s`. Consequently there is no function `omega(r)->0` as `r downarrow0` such that

`sup_s sup_t |p_s(t+h)-p_s(t)| <= omega(|h|)`

for all `h`.

Thus the target hypotheses, even augmented by smooth compact support and the already-paid uniform density height `pi/4`, do **not** imply any universal continuity modulus. In particular there is no target-uniform Holder, Lipschitz, or other equicontinuity estimate. Continuity is genuinely a separate fixed-instance conclusion downstream of the central `L^infinity` problem.

## Proof

### 1. A uniform Fresnel bound

For `u>0` and `L>0`, set

`I_u(L)=int_0^L exp(i u x^2) dx`.

Then

`|I_u(L)| <= 3 u^(-1/2)`.

Indeed, if `L<=u^(-1/2)` this is immediate. Otherwise let `a=u^(-1/2)`. On `[a,L]`, integration by parts using

`d/dx exp(iux^2)=2iux exp(iux^2)`

gives

`int_a^L exp(iux^2) dx = [exp(iux^2)/(2iux)]_a^L + int_a^L exp(iux^2)/(2iu x^2) dx`.

Hence the tail has modulus at most `3/(2 sqrt(u))`, while the initial interval contributes at most `1/sqrt(u)`.

### 2. Phase-aligned probability densities on one fixed compact interval

For `s>=400`, define

`F_s(L) = (1/2) int_0^L (1+cos(sx^2)) dx`.

The Fresnel bound yields

`F_s(3/2) <= 3/4 + 3/(2 sqrt(s)) < 1`,

`F_s(5/2) >= 5/4 - 3/(2 sqrt(s)) > 1`.

By continuity there is `L_s in [3/2,5/2]` with `F_s(L_s)=1`. Put

`f_s(x) = (1/2)(1+cos(sx^2)) 1_[0,L_s](x)`.

Then `f_s` is a probability density and `0<=f_s<=1`.

Let

`g_s = int exp(isx^2) f_s(x) dx`.

Using `cos(theta) exp(i theta) = (1+exp(2i theta))/2`,

`g_s = L_s/4 + (1/2) I_s(L_s) + (1/4) I_{2s}(L_s)`.

Therefore

`|g_s| >= 3/8 - 3/(2 sqrt(s)) - 3/(4 sqrt(2s)) > 1/4`

for every `s>=400`.

This is a concrete phase-aligned family inside a fixed compact set; no pointwise-decay assertion is used.

### 3. Apply the completed account02/B15 cap-preserving mollification/TV result

The newest designated-partner handoff is

`math-research-brain: scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B15/20260924T040438Z-account02-B15-qform.md`,

with canonical mathematics at

`math-open-problems@8356a46866b14c2ddb19a89b0918e867170d1b45`.

Its completed rough-input bridge says that convolution of each marginal with a positive probability approximate identity preserves the density cap and independence, converges in `L^1`, and deterministic quadratic pushforward contracts total variation.

Apply that result here. Choose a nonnegative one-sided `C_c^infinity` probability mollifier `eta_{rho_s}` supported in `[0,rho_s]`, with `rho_s<=1/10`, so small that

`||f_s*eta_{rho_s}-f_s||_1 <= 1/20`.

Set

`\tilde f_s = f_s*eta_{rho_s}`.

Then `\tilde f_s in C_c^infinity`, `0<=\tilde f_s<=1`, it has total mass one, and its support lies in `[0,2.6]`.

Let

`\tilde g_s = int exp(isx^2) \tilde f_s(x) dx`.

The partner's deterministic-pushforward/TV contraction gives, at this actual equation,

`|\tilde g_s-g_s| <= || Law(\tilde X_s^2)-Law(X_s^2) ||_{TV,L1} <= ||\tilde f_s-f_s||_1 <= 1/20`.

Thus

`|\tilde g_s| >= 1/4-1/20 = 1/5`.

For three iid coordinates,

`\widehat p_s(s) = E exp(isQ_s) = \tilde g_s^3`,

so

`|\widehat p_s(s)| >= 1/125`.  
This is the required concrete application of the completed partner result.

### 4. Uniform height and instancewise continuity

Because `\tilde f_s` is supported on the nonnegative axis, the density `h_s` of `Y_s=\tilde X_s^2` is

`h_s(y) = \tilde f_s(sqrt(y))/(2 sqrt(y)) 1_{y>0}`,

hence

`h_s(y) <= 1/(2 sqrt(y))`.

Therefore, for `q_s=h_s*h_s`,

`q_s(t) <= (1/4) int_0^t [u(t-u)]^(-1/2) du = pi/4`.

Since `p_s=q_s*h_s` and `||h_s||_1=1`,

`||p_s||_infinity <= pi/4`.

Also

`||tau_h p_s-p_s||_infinity <= ||q_s||_infinity ||tau_h h_s-h_s||_1 ->0`

for each fixed `s`, by translation continuity in `L^1`. Thus every `p_s` is uniformly continuous; compact support gives `p_s in C_c`. Because `\tilde X_s<=2.6`,

`supp p_s subset [0,3(2.6)^2] subset [0,21]`.

This step proves continuity **after** the height estimate; continuity was not used to create the `L^infinity` bound.

### 5. Non-equicontinuity

Assume, toward contradiction, that a universal modulus `omega(r)->0` exists for this exact-target family:

`sup_s sup_t |p_s(t+h)-p_s(t)| <= omega(|h|)`.

Take

`h_s = pi/s`.

Using the Fourier shift identity,

`2 |\widehat p_s(s)| = |1-exp(i s h_s)| |\widehat p_s(s)|`

`<= ||tau_{h_s}p_s-p_s||_1`.

Both functions are supported in the union of two translates of `[0,21]`, whose measure is at most `22` for `s>=400`. Hence

`2/125 <= 22 omega(pi/s)`,

so

`omega(pi/s) >= 1/1375`

for arbitrarily large `s`, contradicting `omega(r)->0`.

This proves the theorem.

## Regularity ledger

1. **Absolute continuity:** for any nonzero quadratic form and any absolutely continuous joint input, qualitative absolute continuity of the scalar pushforward is much easier than the owner height problem; the critical set of a nonconstant quadratic is a proper affine/linear subspace and coarea excludes singular target mass. No universal height follows from this.
2. **Essential boundedness:** this is the central owner target. The family above is already uniformly paid by `pi/4`, yet still exhibits arbitrarily fine output oscillation across instances.
3. **Continuous density:** every member of the family has a continuous compactly supported representative, but there is no target-uniform continuity modulus even with smooth compactly supported marginals and fixed `A=I_3`.

Therefore a full-QFORM proof should aim first at the interval/density-height estimate. Any continuity upgrade must be treated as a downstream fixed-instance statement; trying to obtain a universal modulus from the bare target hypotheses is impossible.

## Connection to the full target

This theorem does **not** prove or refute the universal density-height conjecture. It closes a regularity-side ambiguity: smooth-core reduction does not buy uniform continuity. The remaining full-target obstruction is still structural/analytic: prove a universal interval domination for arbitrary smooth cap-one product laws and arbitrary symmetric `A` with `s_3(A)>=1`, retaining original-coordinate product provenance through the diffuse/coupled regimes.

## Corrections preserved

- no uniform pointwise quadratic Fourier decay is assumed; the construction itself exhibits a nondecaying target-frequency coefficient across a varying source family;
- no rotated-coordinate independence is used (`A=I_3` throughout);
- no projection-only/X-ray shortcut is used;
- partner mollification is used only through cap preservation and deterministic pushforward TV contraction, exactly in its completed scope.
