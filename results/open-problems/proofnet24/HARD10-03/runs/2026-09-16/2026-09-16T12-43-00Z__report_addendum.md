# HARD10-03 — 2026-09-16T12-19-39Z checkpoint addendum

**SOLUTION STATUS: PARTIAL.** This append-only file records the main-report delivery receipt, a cycle-wide strengthening of NEW-L86/88, and post-write checks. It does not overwrite any prior task file.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T12-19-39Z__report.md`

Create commit:

`f2b153e4b9938d83f5b89ba96017fbf45bebeafa`

Exact-create-commit readback blob:

`643c0c1d54ac759253a501603d9b501eb19a6003`

The file was fetched back using that exact commit ref. The opening target/status, the exponent calculation in NEW-L86, and the later NEW-L87/88 sections were all read back from that immutable commit. Main-report delivery is therefore **VERIFIED**.

No transient retry was needed for the main write. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

# 2. NEW-L89 — cycle-wide local coarse self-avoidance

NEW-L86 was stated from the distinguished root. The archived finite-cycle orbit-averaging identity upgrades it to an intrinsic statement around almost every vertex of a hypothetical finite cycle.

The reused identity is archived in

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T04-41-30Z__report.md`

(blob `9dfca3ea7475425c58eb98137c3f78d59b06a799`). If `T` is the measure-preserving point shift along the permutation orbit and `L=L_beta(0)`, then for every nonnegative measurable `f`,

\[
\mathbb E\left[
1_{\{L<\infty\}}\frac1L
\sum_{j=0}^{L-1}f(T^j\omega)
\right]
=
\mathbb E\left[1_{\{L<\infty\}}f(\omega)\right].
\tag{2.1}
\]

Fix `delta>0` and use the consecutive-period parameters of NEW-L86,

\[
H=\lfloor\beta^{1/2-\delta/2}\rfloor,
\qquad
R=\beta^{1/3-\delta/2}.
\tag{2.2}
\]

Let `B(omega)` be the indicator that the root window of `H+1` consecutive orbit points is not `2R`-separated:

\[
B(\omega)
=
1\left\{
\exists\ 0\le u<v\le H:\
|\pi_\beta^v(0)-\pi_\beta^u(0)|_2\le2R
\right\}.
\tag{2.3}
\]

NEW-L86 gives

\[
\mathbb E B\le C_\delta\beta^{-\delta/2}.
\tag{2.4}
\]

On `{L<infinity}`, define the fraction of bad cyclic starting positions

\[
\overline B(\omega)
:=
\frac1L\sum_{j=0}^{L-1}B(T^j\omega).
\tag{2.5}
\]

Applying (2.1) with `f=B`,

\[
\mathbb E\left[1_{\{L<\infty\}}\overline B\right]
\le
C_\delta\beta^{-\delta/2}.
\tag{2.6}
\]

Markov at threshold `beta^{-delta/4}` yields

\[
\boxed{
\mathbb P\left(
L<\infty,\ 
\overline B>\beta^{-\delta/4}
\right)
\le
C_\delta\beta^{-\delta/4}.
}
\tag{2.7}
\]

### Theorem NEW-L89A — PROVED

Except on an event of probability `O_delta(beta^{-delta/4})` inside the finite-cycle sector, at least a

\[
1-\beta^{-\delta/4}
\]

fraction of the cyclic starting vertices `j` have the following simultaneous property:

\[
\boxed{
\left\{
\pi_\beta^j(0),
\pi_\beta^{j+1}(0),
\ldots,
\pi_\beta^{j+H}(0)
\right\}
\text{ is pairwise }2R\text{-separated}.
}
\tag{2.8}
\]

Thus the coarse self-avoidance from NEW-L86 is not a peculiarity of the distinguished root. A hypothetical finite root cycle must look locally like a mesoscopically self-avoiding walk around almost every one of its own vertices.

A useful simultaneous corollary is that, on the same event, for **every** lag `1<=m<=H`,

\[
\boxed{
\frac1L
\#\left\{
0\le j<L:\
|\pi_\beta^{j+m}(0)-\pi_\beta^j(0)|_2\le2R
\right\}
\le
\beta^{-\delta/4}.
}
\tag{2.9}
\]

Indeed, any starting index that violates (2.9) for any such `m` is already counted by the bad-window indicator in (2.5). Indices are interpreted modulo `L` on a finite cycle.

This remains compatible with finiteness because `H=o(sqrt(beta))`; it does not control the global bridge at lags comparable with `L`.

---

# 3. NEW-L89B — cycle-root/phase averaged braid separation

NEW-L88 can be globalized in the same way.

For a root configuration let

\[
F(\omega)
=
\frac1\beta\operatorname{Leb}\left\{
0\le s<\beta:\
\exists\ 0\le u<v\le H,
|W(v\beta+s)-W(u\beta+s)|_2\le2R
\right\}.
\tag{3.1}
\]

The proof of NEW-L88 gives slightly more than its displayed high-probability statement. Before Markov, it gives the expectation estimate

\[
\mathbb E F
\le
C_\delta\beta^{-\delta/2}.
\tag{3.2}
\]

The reason is explicit: coupling failure contributes at most `C beta^{-delta/2}` because `0<=F<=1`, while on driver-coupling success the Fubini estimate is `O(beta^{-2delta})`.

On a finite cycle define

\[
\overline F(\omega)
:=
\frac1L\sum_{j=0}^{L-1}F(T^j\omega).
\tag{3.3}
\]

Using orbit averaging (2.1),

\[
\mathbb E\left[1_{\{L<\infty\}}\overline F\right]
\le
C_\delta\beta^{-\delta/2}.
\tag{3.4}
\]

Therefore

\[
\boxed{
\mathbb P\left(
L<\infty,\ 
\overline F>\beta^{-\delta/4}
\right)
\le
C_\delta\beta^{-\delta/4}.
}
\tag{3.5}
\]

### Interpretation

Outside an `O_delta(beta^{-delta/4})` exceptional event in the finite-cycle sector, if one samples a cycle starting vertex uniformly and a cyclic phase uniformly from `[0,beta)`, then the fraction of root/phase pairs for which the first `H+1` equal-phase strands contain a pair within `2R` is at most `beta^{-delta/4}`.

Equivalently, a hypothetical large finite cycle has a **cycle-wide, phase-wide separated braid** on almost all local windows. This is a stronger geometric input for a future nonanticipative local-escape lemma than separation at only the distinguished root.

No independence between cyclic roots or between phases is asserted or used; (3.5) uses only the exact orbit-averaging identity plus the one-root expectation estimate.

---

## 4. Post-write checks and scope

1. In NEW-L86, pair counting is by lag `m`: at most `k` pairs per lag and `sum m^{-3/2}<infinity`, so the driver collision term is `C k R^3/(h beta)^{3/2}` rather than a crude `k^2` term.
2. For the sparse superdiffusive specialization `a=1/2-7 epsilon/6`, `b=epsilon`, `rho=3/4-epsilon`, the two exponents are `-epsilon/6` and `-epsilon/4`; the stated failure `O(beta^{-epsilon/6})` is therefore correct.
3. In NEW-L88, the coupling is taken through `(H+1) beta`, sufficient for every displayed phase point `W(j beta+s)` with `j<=H`, `s<beta`.
4. The fixed-phase driver difference has exactly an `m beta` increment law; no independence across phases is needed before Fubini.
5. NEW-L89 uses the previously archived exact finite-cycle orbit average. The event `{L<infinity}` is point-shift invariant, so (2.1) applies without a size-bias correction.
6. Neither NEW-L87 nor NEW-L89 asserts that the final permutation-cycle support is nearest-neighbor connected. The hull/mediator distinction remains explicit.
7. None of NEW-L86--89 assumes monotonicity in `beta` or identifies chronological particle paths with permutation cycles after the first interaction.
8. These results still stop at the same substantive gap: after the first defect cluster, conditional freshness around adaptively selected separated strand neighborhoods has not been proved.

The full `d=3` target remains **OPEN / PARTIAL**.

---

## 5. Next attack sharpened by NEW-L89

The next attack should use the fact that coarse braid separation holds around almost every vertex of a hypothetical finite cycle, not just around the distinguished root. A viable closure route would be:

1. choose a uniformly re-rooted good window using the exact point-shift measure preservation;
2. inside its `H=beta^{1/2-o(1)}` separated strands, select a deterministic fraction of mesoscopic balls at a good phase;
3. expose only the clock information needed to certify the strand centers, leaving annular edge-time regions unqueried;
4. prove a conditional lower bound on one-period heat leakage or a conditional upper bound on cross-block heat using those fresh annuli;
5. invoke the archived conditional strong-Rayleigh/random-cut closure theorem.

The current missing lemma is step 3: an admissible exploration proving enough residual Poisson independence/freshness around adaptively chosen strand centers. Until that is proved, the separated-braid geometry is a rigorous resource but not a full solution.