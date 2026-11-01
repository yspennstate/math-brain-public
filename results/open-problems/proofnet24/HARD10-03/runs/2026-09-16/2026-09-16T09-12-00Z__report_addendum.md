# HARD10-03 — 2026-09-16T08-56-00Z checkpoint addendum

This file is append-only. It records delivery receipts, a post-write sharpening of NEW-L71, a potential-theoretic leakage corollary, and the optional finite-state certificate. It does not overwrite the mathematical checkpoint.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T08-56-00Z__report.md`

Create commit:

`9bac6abdd46fec8a59fe37cfbec01ebb8d06757e`

Exact-create-commit readback blob:

`f52a86c355746640da068082d5e7887ac24c5f69`

The file was fetched using the exact create commit ref above. Therefore the main report delivery is **VERIFIED**.

No transient write retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

## 2. NEW-L71A — sharper beta-dependent surface leakage

The main report proves the valid but nonoptimal bound

\[
\mu_\beta(A)\ge 6e^{-6}|A|^{2/3}
\qquad(\beta\ge1).
\]

The same spectral representation gives a substantially better constant and, in fact, a bound for every `beta>0`.

Let `L` denote the nonnegative nearest-neighbor graph Laplacian on `Z^3`, so

\[
P_\beta=e^{-\beta L},
\qquad
\mu_\beta(A)=
\langle 1_A,(I-e^{-\beta L})1_A\rangle.
\]

The spectrum of `L` lies in `[0,12]`. For fixed `beta>0`, the scalar function

\[
r_\beta(\lambda)
:=\frac{1-e^{-\beta\lambda}}{\lambda}
\]

(with its continuous value `beta` at zero) is decreasing on `[0,infinity)`. Hence, on `[0,12]`,

\[
1-e^{-\beta\lambda}
\ge
\frac{1-e^{-12\beta}}{12}\,\lambda.
\]

By spectral calculus,

\[
\mu_\beta(A)
\ge
\frac{1-e^{-12\beta}}{12}
\langle 1_A,L1_A\rangle.
\tag{2.1}
\]

For an indicator, the Dirichlet form is exactly the unoriented edge boundary:

\[
\langle 1_A,L1_A\rangle=|\partial_EA|.
\tag{2.2}
\]

The projection/Loomis--Whitney argument in the main report proves

\[
|\partial_EA|\ge6|A|^{2/3}.
\tag{2.3}
\]

Therefore:

### Theorem NEW-L71A — PROVED

For every finite nonempty `A subset Z^3` and every `beta>0`,

\[
\boxed{
\mu_\beta(A)
\ge
\frac{1-e^{-12\beta}}2\,|A|^{2/3}.
}
\tag{2.4}
\]

Combining with NEW-L69,

\[
\boxed{
\mathbb P(\pi_\beta(A)=A)
\le
\exp\left\{-\frac{1-e^{-12\beta}}2|A|^{2/3}\right\},
}
\tag{2.5}
\]

and, for `u in A`,

\[
\boxed{
\mathbb P(C_{\pi_\beta}(u)=A)
\le
\exp\left\{-\frac{1-e^{-12\beta}}2|A|^{2/3}\right\}.
}
\tag{2.6}
\]

For the large-time regime `beta>=1`, the exponent constant is `(1-e^-12)/2`, essentially `1/2`, rather than `6e^-6`. The weaker main-report theorem remains correct; NEW-L71A should be used going forward.

This sharpening uses monotonicity only of the one-particle spectral multiplier `1-e^{-beta lambda}`. It does **not** assume monotonicity of permutation-cycle events in `beta`.

---

## 3. NEW-L73 — Green-energy-to-leakage inequality

The previous checkpoint introduced the transient `d=3` Green kernel

\[
g(x)=\int_0^\infty p_t(0,x)\,dt
\]

and the uniform Green self-energy

\[
\mathcal E_g(A)
=\frac1{|A|^2}\sum_{x,y\in A}g(y-x).
\]

There is a direct deterministic bridge from that potential-theoretic quantity to the heat leakage used in NEW-L69.

For `f=1_A`, define the heat content

\[
H_t(A)=\langle f,P_tf\rangle
=\sum_{x,y\in A}p_t(x,y).
\]

Since `P_t=e^{-tL}` with `L>=0`, `H_t(A)` is nonincreasing in `t`. Therefore

\[
tH_t(A)
\le
\int_0^tH_s(A)\,ds
\le
\int_0^\infty H_s(A)\,ds.
\tag{3.1}
\]

By Tonelli and translation invariance,

\[
\int_0^\infty H_s(A)\,ds
=
\sum_{x,y\in A}g(y-x)
=|A|^2\mathcal E_g(A).
\tag{3.2}
\]

Thus

\[
H_\beta(A)
\le
\frac{|A|^2}{\beta}\mathcal E_g(A).
\]

Since `mu_beta(A)=|A|-H_beta(A)`, we obtain:

### Theorem NEW-L73 — PROVED

For every finite nonempty `A subset Z^3` and every `beta>0`,

\[
\boxed{
\mu_\beta(A)
\ge
|A|\left(1-
\frac{|A|\mathcal E_g(A)}{\beta}
\right).
}
\tag{3.3}
\]

Consequently NEW-L69 gives

\[
\boxed{
\mathbb P(\pi_\beta(A)=A)
\le
\exp\left\{-|A|\left(1-
\frac{|A|\mathcal E_g(A)}{\beta}
\right)_+\right\},
}
\tag{3.4}
\]

and the same upper bound holds for `P(C_u=A)`.

### Why NEW-L73 is useful

This connects the two newest strands of the project without a tagged-particle estimate. The preceding checkpoint proved, under the hypothetical all-finite regime, that the **random final root cycle** has very small uniform Green energy on average. NEW-L73 says that any *nonanticipatively selected* candidate set having comparable low Green energy and size `|A| E_g(A) << beta` pays an essentially `e^{-|A|}` closure cost.

It does not by itself permit substituting the final cycle for `A`: that would again be anticipative. The remaining task is to produce such low-energy candidates during an admissible exploration before exposing the clocks that decide closure.

---

## 4. Optional finite-state certificate

After publishing the main mathematical report, I executed an exact finite-state matrix-exponential checker on `path4`, `cycle4`, `star4`, and `cycle5` at times `0.2,1,2`, checking every nonempty vertex subset. It verifies numerically

\[
P(P(A)=A)
\le
\prod_{y\in A}\sum_{x\in A}K(x,y)
\le e^{-\mu_A}
\]

and

\[
P(C_u=A)\le e^{-\mu_A}.
\]

A separate time-inhomogeneous four-cycle case uses two random interchange segments with different edge rates and a forced transposition between them. Its one-particle kernel has maximum asymmetry

\[
0.051880846034700945,
\]

so this is genuinely non-self-adjoint rather than an accidentally reversible test.

Across all checked cases, the largest positive numerical violation was

\[
2.220446049250313\times10^{-15},
\]

and the checker returned `PASS`. This is a finite-state sanity check only; the proof of NEW-L69/70 is analytic and uses strong-Rayleigh negative association.

Checker source:

`proofnet24/HARD10-03/artifacts/2026-09-16T09-03-00Z__heat_leakage_cut_survival_check.py`

create commit

`45c0392f57fed12632e5ff014faf96faa4ede7cc`

exact-commit readback blob

`40b0f33817498eb7d8ec4ec50150df7f11ae565a`.

Delivery: **VERIFIED**.

Executed output:

`proofnet24/HARD10-03/artifacts/2026-09-16T09-03-00Z__heat_leakage_cut_survival_check_output.json`

create commit

`79fffbae62c35117fdd3bbc3bdaa5287cf569fb4`

exact-commit readback blob

`d1c96dfba8ed24f52c1172d974548f2ef5e4917c`.

Delivery: **VERIFIED**.

---

## 5. Post-write self-review and current bottleneck

The following points were checked after exact readback:

1. The `P(A)=A` event is exactly the all-red-on-`A` exclusion event because the number of red particles is conserved and equals `|A|`.
2. Negative association is used only for increasing events on disjoint site coordinates.
3. Conditional NEW-L70 inherits the exact hypotheses of the archived admissible no-peeking strong-Rayleigh theorem; it is not asserted for arbitrary anticipative conditioning.
4. The spectral bound NEW-L71A uses the exact `Z^3` Laplacian spectral range `[0,12]` and the exact Dirichlet identity `<1_A,L1_A>=|partial_E A|`.
5. NEW-L73 uses only monotonicity of heat content under a self-adjoint positive semigroup and Tonelli for the transient Green kernel.
6. None of these estimates converts the final-cycle geometry from NEW-L65--68 into a stopping candidate automatically. That nonanticipative extraction remains the principal missing step.

No contradiction or full proof is claimed. The strongest new operational target is now: during a no-peeking exploration, construct a controlled-entropy family of history-measurable candidate traps with either large conditional heat leakage or low Green energy relative to `beta/|A|`, then apply NEW-L70/72/73 to charge closure.

No Gmail/email, Google Drive, public posting, repository settings/workflows/permissions changes, force-push, credential inspection, third-party contact, or paid compute was used.