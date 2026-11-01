Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested in prompt text, but no authenticated reasoning-effort selector or runtime telemetry is exposed. HARD7-05: **no movement** in the frozen source milestone `W_{1/4}=1/8 -> 1/8`; methods tried: **B2 / B5 / B11**.

# HARD7-05 run 1 — integrated-fBM persistence exponent; exact covariance and a sharp comparison-route obstruction

## 1. Admission, ownership, and current-status check

This run began from `ADMISSION_PENDING` and read the controlling HARD7 policy, the September new-methods policy/directive, the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, relevant intake/claim records, and neighboring reports.

### Rejected Brownian-sheet candidate

The natural intake candidate `D0017` (Khoshnevisan, *Slices of Brownian Sheet*, Open Problem 2) was **not** admitted. In the final source PDF, equation (8.2) literally defines

\[
Y_d(s)=\{(t_1,t_2)\in \mathbb R_+^2:B(s,t_1)=B(s,t_2)\},
\]

and then asks whether `dim_H Y_d(s)=0` for every `s`. Literally this set contains the whole diagonal `{(t,t):t\ge0}`, hence has Hausdorff dimension at least one. The surrounding section is plainly about *double points*, so the intended set almost certainly excludes `t_1=t_2`; treating the literal typo as the hard intended problem would violate the source-scope rule, while treating it as a source-level hard theorem would be mathematically false. No claim was created for D0017. This is an admission/scope correction, not a claim that the intended off-diagonal problem has been solved.

### Admitted target

I instead admitted the current externally posed Gaussian-persistence problem from:

G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v1 (2025), §1, p. 3.

The primary source says explicitly that the exponent values for `alpha=2, H != 1/2` remain an unsolved problem. The same paper refutes the formerly long-standing formula `theta_{2,H}=H(1-H)`, so that obsolete conjectural formula is not our target.

The exact source object for this track is the one-sided persistence exponent of integrated fractional Brownian motion

\[
I_H(t):=\int_0^t B_H(u)\,du,
\qquad
\mathbb P\{I_H(t)<1\ \forall t\in(0,T)\}
 = T^{-\theta_{2,H}+o(1)}.
\]

A bounded current-literature search on 2026-09-18 recovered Molchan 2025, Aurzada--Kilian 2022, Kilian's 2023 thesis, the 2024 Aurzada--Mittenbuehler persistence paper, and adjacent 2025--2026 Gaussian-persistence papers, but no later exact determination of `theta_{2,H}`. This is negative evidence only, not a proof of worldwide openness.

Repository searches for `2509.10265`, the exact title, and `Molchan theta 2,H persistence exponent integrated fractional Brownian` found no existing claim/track. I therefore created the exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

at commit `d55ee25440dee044b7ee10830251a2cd9f8ad24d`.

## 2. Frozen measurable milestone

The full source target is the exact function `H -> theta_{2,H}` on `0<H<1`, `H != 1/2`. To make hourly progress measurable without changing the source, this track freezes the special point `H=1/4` and tracks

\[
W_{1/4}:=U_{1/4}-L_{1/4},
\]

where `[L_{1/4},U_{1/4}]` is the best rigorously verified bracket retained by this track for `theta_{2,1/4}`.

Molchan 2025, equation (3), gives

\[
\frac12(H\wedge(1-H))\le \theta_{2,H}
\]

and, for `H<1/2`, the displayed upper bound is the minimum of `H` and another larger explicit term at `H=1/4`. Hence

\[
\boxed{\frac18\le \theta_{2,1/4}\le \frac14},
\qquad
\boxed{W_{1/4}=\frac18}.
\]

This run does not improve either endpoint, so the metric is honestly `1/8 -> 1/8`.

The mathematical progress below is instead a **sharp elimination of a major Slepian-comparison route**: comparison with any time-rescaled integrated Brownian reference cannot improve the existing lower endpoint, at `H=1/4` or at any other `H`.

## 3. B5 — derive the exact Lamperti covariance and its two tail phases

Let `p=2H`. For `T>=1`, the fractional-Brownian covariance

\[
\mathbb E[B_H(u)B_H(v)]
=\frac12\bigl(u^{2H}+v^{2H}-|u-v|^{2H}\bigr)
\]

gives, by two elementary integrations,

\[
\operatorname{Cov}(I_H(T),I_H(1))
=
\frac1{2(p+1)}
\left[
T^{p+1}+T-
\frac{T^{p+2}+1-(T-1)^{p+2}}{p+2}
\right].
\tag{1}
\]

At `T=1` this yields

\[
\operatorname{Var} I_H(1)=\frac1{p+2}=\frac1{2H+2}.
\tag{2}
\]

Define the variance-one Lamperti transform

\[
X_H(t):=\sqrt{2H+2}\,e^{-(H+1)t}I_H(e^t),
\qquad t\in\mathbb R.
\]

It is stationary, and for `t>=0`, with `T=e^t`, its correlation is therefore

\[
R_H(t)=
\frac{p+2}{2(p+1)}T^{-(p+2)/2}
\left[
T^{p+1}+T-
\frac{T^{p+2}+1-(T-1)^{p+2}}{p+2}
\right].
\tag{3}
\]

This formula is exact.

Now expand

\[
(T-1)^{p+2}
=T^{p+2}-(p+2)T^{p+1}
+\frac{(p+2)(p+1)}2T^p
-\frac{(p+2)(p+1)p}{6}T^{p-1}
+O(T^{p-2}).
\]

Substituting into the bracket in (3) gives

\[
T+\frac{p+1}{2}T^p-\frac{p(p+1)}6T^{p-1}
+O(T^{p-2}+1).
\tag{4}
\]

There are two distinct leading terms depending on whether `p<1` or `p>1`.

For `0<H<1/2`, `T` dominates `T^p`, and

\[
\boxed{
R_H(t)\sim \frac{H+1}{2H+1}e^{-Ht}
}
\qquad(t\to\infty).
\tag{5}
\]

For `1/2<H<1`, `T^p` dominates `T`, and

\[
\boxed{
R_H(t)\sim \frac{H+1}{2}e^{-(1-H)t}
}
\qquad(t\to\infty).
\tag{6}
\]

At the transition `H=1/2`, both terms have the same order and (3) simplifies exactly to

\[
\boxed{
R_{1/2}(t)=\frac12\left(3e^{-t/2}-e^{-3t/2}\right).
}
\tag{7}
\]

Thus the correlation-tail exponent of the Lamperti process is exactly

\[
h(H):=H\wedge(1-H).
\tag{8}
\]

At the tracked point `H=1/4`, (5) becomes

\[
R_{1/4}(t)\sim \frac56e^{-t/4}.
\tag{9}
\]

This calculation is elementary but important for route selection: any stationary-Gaussian comparison that has the wrong correlation decay at infinity cannot improve a persistence bound, however good its local covariance fit is.

## 4. B11 + B2 — a sharp ceiling for the time-rescaled integrated-Brownian Slepian route

The exact persistence exponent of integrated Brownian motion is

\[
\theta_{2,1/2}=\frac14.
\tag{10}
\]

A natural attempt to improve a lower bound for `theta_{2,H}` is to compare `X_H` by Slepian's inequality with a time-rescaled integrated-Brownian Lamperti process `X_{1/2}(ct)`. Its correlation is

\[
R_{1/2}(ct)
=\frac12\left(3e^{-ct/2}-e^{-3ct/2}\right)
\sim \frac32 e^{-ct/2},
\tag{11}
\]

and its persistence exponent is `c/4`.

For the covariance order needed to get the lower bound

\[
\theta_{2,H}\ge \frac c4,
\]

one would seek

\[
R_H(t)\le R_{1/2}(ct)
\quad\text{for all }t\ge0.
\tag{12}
\]

### Proposition (comparison-route ceiling)

If `H in (0,1)`, `H != 1/2`, and (12) holds for some `c>0`, then

\[
\boxed{c\le 2\bigl(H\wedge(1-H)\bigr)}.
\tag{13}
\]

Consequently the resulting Slepian lower bound can never exceed

\[
\boxed{
\frac c4\le \frac12\bigl(H\wedge(1-H)\bigr),
}
\tag{14}
\]

which is exactly the already-known lower endpoint displayed in Molchan's equation (3).

#### Proof

Set `h=H wedge (1-H)`. Equations (5)--(6) give a positive constant `A_H` such that

\[
R_H(t)\sim A_H e^{-ht}.
\]

Equation (11) gives

\[
R_{1/2}(ct)\sim \frac32e^{-(c/2)t}.
\]

If `c/2>h`, then

\[
\frac{R_H(t)}{R_{1/2}(ct)}
\sim \frac{2A_H}{3}e^{(c/2-h)t}\to\infty,
\]

contradicting (12). Hence `c/2<=h`, which is (13). Multiplying by the known reference exponent `1/4` gives (14). QED.

### Tracked special point

For `H=1/4`, any comparison of form (12) necessarily has

\[
c\le\frac12,
\]

so it can give at best

\[
\theta_{2,1/4}\ge\frac18.
\]

Therefore **no amount of sharpening the pointwise covariance algebra within this entire reference family can move the tracked lower endpoint above `1/8`**. The obstruction is not a loose inequality at finite time; it is the exact mismatch of the correlation-tail exponents.

This is the main substantive result of the run. It is a route-elimination theorem, not a solution of the source problem and not claimed as new to the literature.

## 5. B2 — the even simpler OU/fBM reference also cannot supply the missing lower bound

One might instead compare directly to the Lamperti transform of ordinary Brownian motion, whose correlation is `e^{-a|t|}` after a time rescaling and whose persistence exponent is explicit.

That route fails already at the origin. The process `I_H` is once mean-square differentiable. From

\[
X_H'(0)=\sqrt{2H+2}\left(B_H(1)-(H+1)I_H(1)\right)
\]

and

\[
\operatorname{Var} B_H(1)=1,
\qquad
\operatorname{Var} I_H(1)=\frac1{2H+2},
\qquad
\operatorname{Cov}(I_H(1),B_H(1))=\frac12,
\]

we obtain

\[
\operatorname{Var}X_H'(0)=1-H^2.
\]

Hence the stationary correlation has the quadratic expansion

\[
\boxed{
R_H(t)=1-\frac{1-H^2}{2}t^2+o(t^2)
}
\qquad(t\to0).
\tag{15}
\]

By contrast, an OU correlation is

\[
e^{-a|t|}=1-a|t|+O(t^2).
\]

For every `a>0`, (15) therefore implies `R_H(t)>e^{-a|t|}` for all sufficiently small positive `t`. Thus the covariance order `R_H<=R_OU` needed for an OU-based Slepian lower bound is impossible. The exact persistence exponent of ordinary fBM/Brownian motion cannot simply be imported through this direct comparison.

Together, Sections 4--5 rule out the two most obvious exact-reference strategies: the non-smooth OU family fails locally, while the smooth integrated-Brownian family is globally capped by the exact long-time correlation exponent.

## 6. What actually moved mathematically

The frozen numerical bracket did **not** move:

\[
[1/8,1/4]\to[1/8,1/4],\qquad W_{1/4}=1/8\to1/8.
\]

But the run produced three source-relevant structural facts that materially narrow the search:

1. the exact normalized Lamperti correlation formula (3) for the source process, in a form suitable for symbolic comparison;
2. the exact two-phase correlation tail (5)--(6), including the transition formula (7);
3. a proof that the entire time-rescaled integrated-Brownian Slepian family is **provably incapable** of improving the existing lower bound, plus a local smoothness obstruction to direct OU comparison.

This says what a successful next method must contain: it cannot be a one-reference global covariance comparison to either of those exact solvable processes. It must exploit more of the spectral shape than the leading tail, use a parameter-dependent differential comparison, or introduce a genuinely different variational/conditioning representation of the persistence event.

## 7. Next run: do not repeat B2/B5/B11

Suggested next method triple: **B6 / B17 / B30**.

- `B6` (deform from the solved point): start at `H=1/2`, where `theta=1/4`, and derive a controlled perturbation of the *full stationary spectral density*, not just a fixed Slepian reference.
- `B17` (look for the constants elsewhere): identify whether the derivative/variation of the persistence exponent at the integrated-Brownian point is encoded by the killed two-dimensional Markov generator of `(I_{1/2},B_{1/2})`; the source's 2025 spectral duality gives a nontrivial consistency constraint on any derivative.
- `B30` (one scale at a time): separate low-frequency/tail and high-frequency/local-smoothness contributions, since this run proves that either endpoint alone is insufficient for a strict lower-bound improvement.

A concrete next milestone is to derive a rigorous first-order inequality for `theta_{2,H}` on one side of `H=1/2` from a differentiable covariance/spectral interpolation. A finite-difference numerical estimate alone will not move `W_{1/4}`.

## 8. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  source: "G. Molchan, arXiv:2509.10265v1 (2025), integrated-fBM one-sided persistence exponent"
  claim_path: operations/claims/MOLCHAN-2025-THETA2H.md
  claim_commit: d55ee25440dee044b7ee10830251a2cd9f8ad24d
  status: PARTIAL
  full_source_target: "determine theta_{2,H} for 0<H<1, H != 1/2"
  fixed_metric: "W_{1/4}=U_{1/4}-L_{1/4}"
  metric_before: "1/8"
  metric_after: "1/8"
  movement: "no movement"
  methods:
    - B2: "attack exact-reference comparison routes before investing in them"
    - B5: "derive exact H-dependent Lamperti covariance and tail phases"
    - B11: "Slepian/covariance dual reformulation; prove comparison-route ceiling"
  substantive_result:
    - "R_H(t) ~ (H+1)/(2H+1) exp(-Ht) for H<1/2"
    - "R_H(t) ~ (H+1)/2 exp(-(1-H)t) for H>1/2"
    - "any global comparison R_H(t)<=R_{1/2}(ct) forces c<=2 min(H,1-H), so it cannot beat the known lower bound"
    - "direct OU comparison for a lower bound is blocked by quadratic-vs-linear covariance loss at t=0"
  finite_claims_requiring_checker: []
  artifacts: []
  audits: []
  next_methods: [B6, B17, B30]
  remaining_obligation: "obtain a strictly improved rigorous theta bracket or exact value; full source requires all H"
```
