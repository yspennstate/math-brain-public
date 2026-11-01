# HARD10-03 — 2026-09-16T13-18-15Z checkpoint addendum

**SOLUTION STATUS: PARTIAL.** The full `d=3` Tóth infinite-cycle conjecture remains open. This append-only file records the immutable main-report receipt, corrects one LaTeX serialization defect, and sharpens the scale choice in `NEW-L95`. No prior file is overwritten.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T13-18-15Z__report.md`

Create commit:

`fb49c17bc962b9fd92c1aa97d42a1014a71816f2`

Exact-create-commit readback blob:

`70e12a6ea990850a2252e4ec4adf1230bc55c853`

The report was fetched back using exactly that commit ref. The target/backfill section, the complete `NEW-L93` fresh phase-window proof, the `P=QW` restart construction in `NEW-L94`, the `NEW-L95` fresh-tube prefix proof, and the limitation/next-attack sections were read back from the immutable create commit. Main-report delivery is therefore **VERIFIED** in the repository-delivery sense. Mathematical correctness remains analytic self-review, not independent verification.

No transient retry was needed for the main report. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

## 2. Immutable serialization correction

The exact-commit readback exposed a LaTeX serialization defect in two displayed equations of the immutable main report. In equations (4.3) and (4.4), the intended term

\[
\varepsilon_{T,r}
\]

was rendered as plain `arepsilon_{T,r}` after the line break. The mathematics and all subsequent uses were intended to use the exit probability from `NEW-L93`.

The corrected equations are

\[
\boxed{
\mathbb P\bigl(a_{j+1}\in A_j\mid\mathscr F_j,Q\bigr)
\le C|A_j|T^{-3/2}+\varepsilon_{T,r},
}
\tag{A.1}
\]

and, for `A_j={a_0,...,a_j}`,

\[
\boxed{
\mathbb P\bigl(a_{j+1}\in\{a_0,\ldots,a_j\}\mid\mathscr F_j,Q\bigr)
\le C(j+1)T^{-3/2}+\varepsilon_{T,r}.
}
\tag{A.2}
\]

No old file is edited; this append-only addendum is the correction of record.

---

# 3. NEW-L95B — near-square-root fresh-tube prefix with cleaner optimized scales

The main report used a conservative one-parameter scale choice. The same proof gives a materially stronger and cleaner family.

Fix any

\[
0<\epsilon<\frac12.
\]

Set, with integer rounding suppressed,

\[
\boxed{
n=\beta^{1/2-\epsilon},\qquad
r=\beta^{1/3},\qquad
T=\beta^{2/3-\epsilon/2}.}
\tag{A.3}
\]

For large `beta`, `1<<r<<T<beta`.

Apply archived `NEW-L86` with horizon `H=n` and separation parameter `2r`. Then

\[
\begin{aligned}
\mathbb P\left(
\min_{0\le i<j\le n}|\pi_\beta^j(0)-\pi_\beta^i(0)|_2\le4r
\right)
&\le
C\left(\frac n{\sqrt\beta}
+\frac{n(2r)^3}{\beta^{3/2}}\right)\\
&\le C\left(\beta^{-\epsilon}+\beta^{-\epsilon}\right)\\
&\le C\beta^{-\epsilon}.
\end{aligned}
\tag{A.4}
\]

For a radius-`r` fresh tube of duration `T`, `NEW-L93` gives the maximal exit probability

\[
\varepsilon_{T,r}
\le C\exp\left[-c\frac{r^2}{T+r}\right].
\]

Since `T/r=beta^(1/3-epsilon/2)->infinity`,

\[
\frac{r^2}{T+r}
\ge c\frac{\beta^{2/3}}{\beta^{2/3-\epsilon/2}}
=c\beta^{\epsilon/2},
\]

so

\[
\boxed{
\varepsilon_{T,r}\le C e^{-c\beta^{\epsilon/2}}.
}
\tag{A.5}
\]

Run the same admissible one-window exploration as in `NEW-L95`, stopping before the first geometric overlap or tube exit. Before stopping, every selected `[0,T]` tube is genuinely untouched, so iterated conditioning gives

\[
\mathbb P(\text{some tube exit before overlap by stage }n)
\le Cn e^{-c\beta^{\epsilon/2}}.
\tag{A.6}
\]

Combining (A.4) and (A.6) yields the sharpened theorem:

## Theorem NEW-L95B — PROVED

For every fixed `epsilon in (0,1/2)`, with probability at least

\[
\boxed{
1-C\beta^{-\epsilon}
-C\beta^{1/2-\epsilon}e^{-c\beta^{\epsilon/2}},
}
\tag{A.7}
\]

the first

\[
\boxed{n=\lfloor\beta^{1/2-\epsilon}\rfloor}
\]

actual cyclic iterates admit an admissible exploration of the same physical phase window

\[
[0,T],\qquad T=\beta^{2/3-\epsilon/2},
\]

inside pairwise disjoint spatial tubes of radius

\[
r=\beta^{1/3},
\]

and every corresponding early-phase strand remains in its own tube.

Thus the certified fresh-tube horizon reaches `beta^(1/2-o(1))` cyclic iterates while retaining the natural `beta^(1/3)` spatial tube radius.

### Restart/recruitment scale

For (A.3),

\[
\begin{aligned}
n^2T^{-3/2}
&=
\beta^{1-2\epsilon}
\beta^{-1+3\epsilon/4}\\
&=
\boxed{\beta^{-5\epsilon/4}}.
\end{aligned}
\tag{A.8}
\]

Hence the corrected `NEW-L94` cumulative listed-target estimate becomes

\[
\boxed{
Cn^2T^{-3/2}+n\varepsilon_{T,r}
\le
C\beta^{-5\epsilon/4}
+C\beta^{1/2-\epsilon}e^{-c\beta^{\epsilon/2}}.
}
\tag{A.9}
\]

Again, this is a **restart-ready conditional estimate**, not a claim that the full cycle has length at least `n` by a new method; the older first-interaction theorem already gives a strong unconditional short-cycle bound.

---

## 4. Post-write proof-scope check

1. The factorization `P=Q o W` has the correct chronological order for `W=Phi_[0,T]` and `Q=Phi_[T,beta]`.
2. `Q` and `W` are independent because they are functions of disjoint physical-time Poisson increments. Conditioning on `Q` is used only for this one selected phase window.
3. If `A_j` is history-measurable, then after conditioning on `Q`, the target `Q^{-1}(A_j)` is history-measurable and has exactly `|A_j|` vertices. Targets outside the fresh spatial buffer are absorbed by the tube-exit event, which is why (A.1) remains valid without any spatial assumption on `Q^{-1}(A_j)`.
4. The adaptive tubes do not need to be independent. Before the stopping time their incident-edge space-time regions are disjoint and unrevealed; repeated conditional use of the uniform exit bound is sufficient.
5. `NEW-L86` is used only to bound the probability that the **actual cyclic anchors** fail to be spatially separated. The tube-exit estimate is uniform under the adaptive history, so a union bound between geometric-separation failure and pre-overlap tube exit is valid even though those events are correlated.
6. A chronological SRW is used only inside a certified fresh phase tube. No chronological path is identified with the complete permutation-cycle orbit.
7. The theorem certifies one phase window for almost `sqrt(beta)` iterates. It does not furnish infinitely many restarts at fixed `beta`, and it does not prove the target.

---

## 5. Updated next attack

The strongest missing step is now a **localized complement oracle**. Instead of conditioning on the entire `Q`, after a fresh-window endpoint `y=W(a_j)` is obtained, reveal only enough complement-time clocks to determine the single point `Q(y)`. The desired theorem is that the cumulative space-time region exposed by doing this through many stages has small enough phase/spatial density that another deterministic phase window retains fresh buffered regions with positive conditional frequency.

A successful bound of that type would permit genuine phase rotation/restart without the circular use of clocks already summarized inside a conditioned complement map. This is the point at which the `d=3` recurrence difficulty is now concentrated.
