Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL MOVEMENT (companion-certified, separate from the new P13 mechanism): the P13-before interval `L <= gamma_2 <= U_0` is strictly tightened to `L <= gamma_2 <= U_* < U_0` by P02's new exact algebraic-integer strictification of the inherited C045 upper certificate. P13 MECHANISM MOVEMENT: the dependence-preserving finite-to-infinite additive error for the correlated width-`w` strip is improved from `w 4^(2w)` to `2(4^(2w)-1)/3`, with an exact overlapping-reset tail recursion that strictly dominates the old aligned-block contraction.**

# P13 T02 — overlapping reset coupling and a sharper finite-to-infinite error

## 1. Scope, continuity, source, and P02 coordination

This run follows `operations/PROGRESS20_2026-09-20.md`, latest LIVE20 assignment T02. The source target remains the binary Chvatal--Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The match indicators in a row or column are therefore correlated through the shared raw letters. **No independent Bernoulli matching surrogate is used.**

Current source recovery: Alexander Tiskin, `arXiv:2212.01582v2` (v2 revised 2024-08-13), presents the binary coefficient as unresolved after removing unsupported claims from the earlier version. Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, provide the rigorous public lower endpoint

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

The latest P13 T02 report is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T01-24-00Z__boundary-carry-reachable-reset-certified-endpoint.md`.

It proved: (i) exact one-column boundary-carry extinction; (ii) the boundary-event coboundary identity `gamma_w=2/3+pi_w(B_w)/3`; (iii) a reachable-state `2w` mismatch reset; and (iv) the coarse aligned-block finite-to-infinite additive error `w 4^(2w)`. It also made the source interval endpoint numerically explicit through the then-current exact C045 certificate.

The latest completed P02 companion report recovered here is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T01-37-20Z__algebraic-integer-spectral-gap-report.md`.

P02 stays on the complementary covering/cone/variational side. It proves a genuinely strict exact improvement of the C045 spectral parameter from `lambda` to `lambda_*<lambda`; P13 does not duplicate that argument. Section 7 below records the consequent project-level source interval update separately from the new P13 boundary mechanism.

Short pre-LIVE20 P13 handoff, preserved but not reopened: P13 had terminally handed off P0342 at frozen source metric `2/2`; the later P0205 screen admitted no successor because the source's `tau(infinity)` notation was ambiguous. Retired I0051/clade work remains retired.

## 2. Exact correlated strip transition and the one dependency needed here

Fix strip half-width `w` and put

\[
m=2w.
\]

A reachable strip state is

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m),
\]

where the `x_i` are the actual raw `X` letters in the moving window and the `g_i` are vertical frontier increments of the band-restricted LCS dynamic program. A fresh source pair `(u,v)` consists of two independent fair bits. The **same** fresh `v` is compared with every old `x_i` in the column.

Define

\[
d_0=0,\qquad
 d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\qquad 1\le i\le m.
\tag{2.1}
\]

Then the exact transition is

\[
g_i'=g_{i+1}+d_{i+1}-d_i,\qquad 1\le i<m,
\tag{2.2}
\]

\[
g_m'=(1-d_m){\bf1}_{\{u=v\}},
\tag{2.3}
\]

and `x'=(x_2,...,x_m,u)`. The one-step diagonal reward `rho` takes values in `{0,1}`.

The previous P13 report proved the following reachable-state reset, which is the only inherited theorem needed below.

### Reset lemma

For either `a in {0,1}`, append the same mismatch source pair

\[
(u_t,v_t)=(a,1-a)
\]

for `m=2w` consecutive columns. Every reachable starting state is then sent to the same terminal state

\[
z_a=(a^m;0^m).
\tag{2.4}
\]

For completeness, the geometric reason is short. After `m` steps the raw `X` window is entirely the newly appended symbol `a`. Any scored diagonal involving one of those new `X` positions would have to meet a newly appended `Y` symbol `1-a`, hence cannot match. Therefore all final DP values across the frontier are equal and every final gradient is zero. This argument uses reachability as a genuine band-DP frontier; it is not a claim about arbitrary formal bit states.

The exact checker saved with this run independently re-verifies (2.4) on all reachable states for `w=1,2,3,4`, with state counts `14,224,3098,39774`.

## 3. New idea: use reset words at every offset, not only aligned blocks

The previous finite-to-infinite proof divided time into disjoint blocks of length `m`. Each block reset with probability

\[
q=2\,4^{-m},
\]

because either `(0,1)^m` or `(1,0)^m` works. This gave

\[
\operatorname{osc}(P_w^N f)
\le \operatorname{osc}(f)(1-q)^{\lfloor N/m\rfloor}
\]

and, after summing this coarse geometric tail, the additive constant

\[
\frac m q=\frac m2 4^m=w4^{2w}.
\tag{3.1}
\]

That argument discards almost all reset opportunities: a reset run may begin at **any** time, not merely at block boundaries.

Let the four possible source pairs be viewed as a four-letter iid alphabet. Write

\[
A=(0,1),\qquad B=(1,0)
\]

for the two mismatch letters, and let the other two source pairs be neutral letters. Define

\[
\tau_m=\min\{t\ge m:\ Z_{t-m+1}\cdots Z_t=A^m\text{ or }B^m\},
\tag{3.2}
\]

where `Z_t=(U_t,V_t)` is the genuine iid source-pair stream.

### Theorem 3.1 — overlapping-reset coupling

Drive any two reachable width-`w` strip states by the same future source-pair stream. Then they are identical from time `tau_m` onward. Consequently, for every bounded function `f`,

\[
\boxed{
\operatorname{osc}(P_w^N f)
\le \operatorname{osc}(f)\Pr(\tau_m>N).
}
\tag{3.3}
\]

**Proof.** If `tau_m=t`, then the final `m` source pairs ending at time `t` are either `A^m=(0,1)^m` or `B^m=(1,0)^m`. Apply the reset lemma to the two (reachable) states present at time `t-m`: both are mapped to the same `z_0` or `z_1` at time `t`. Thereafter the common future input keeps the trajectories identical. Under this synchronous coupling,

\[
\Pr(S_N\ne S_N')\le\Pr(\tau_m>N).
\]

The oscillation inequality follows from the coupling bound for a function whose range length is `osc(f)`. QED.

This is still the true binary-string model. The reset letters are actual pairs `(U_t,V_t)`; no `m x m` field of independent match indicators is introduced.

## 4. Exact reset-tail recursion and exact mean coupling time

The law of `tau_m` is elementary but the overlap matters. Let

- `N_n` be the probability that no reset has occurred by time `n` and the current terminal run is neutral (the last letter is neither `A` nor `B`, with `n=0` included),
- `R_{n,r}` be the probability that no reset has occurred and the word ends in a run of exactly `r` copies of either `A` or `B`, aggregated over the two signs, `1<=r<m`.

Set `N_0=1` and all `R_{0,r}=0`. Then

\[
N_{n+1}=\frac12\left(N_n+\sum_{r=1}^{m-1}R_{n,r}\right),
\tag{4.1}
\]

\[
R_{n+1,1}=\frac12N_n+\frac14\sum_{r=1}^{m-1}R_{n,r},
\tag{4.2}
\]

\[
R_{n+1,r+1}=\frac14R_{n,r},\qquad 1\le r<m-1.
\tag{4.3}
\]

Therefore

\[
\boxed{
 a_m(n):=\Pr(\tau_m>n)=N_n+\sum_{r=1}^{m-1}R_{n,r}
}
\tag{4.4}
\]

is an exactly computable dyadic rational for every finite horizon. Since avoiding a reset at *all* offsets implies avoiding it in the disjoint aligned blocks,

\[
a_m(n)\le (1-2\,4^{-m})^{\lfloor n/m\rfloor},
\tag{4.5}
\]

and the inequality is strict once unaligned reset opportunities can occur (for example at `n=2m`, as checked exactly below).

The tail sum has a closed form.

### Theorem 4.1 — exact mean first overlapping reset

\[
\boxed{
\mathbf E\tau_m=\frac{2(4^m-1)}3.
}
\tag{4.6}
\]

**Proof.** Let `E_0` be the expected remaining waiting time when no `A/B` run is currently active, and `E_r` the expected remaining waiting time given a current run of one mismatch letter of length `r`, `1<=r<m`. By symmetry the sign of the run does not matter. From the next source pair,

\[
E_0=1+\frac12E_1+\frac12E_0,
\]

so

\[
E_0=2+E_1.
\tag{4.7}
\]

For `1<=r<m`, with `E_m=0`, the next letter continues the same run with probability `1/4`, switches to the opposite mismatch letter with probability `1/4`, and is neutral with probability `1/2`. Hence

\[
E_r=1+\frac14E_{r+1}+\frac14E_1+\frac12E_0.
\tag{4.8}
\]

Put

\[
K=1+\frac14E_1+\frac12E_0=2+\frac34E_1
\]

using (4.7). Iterating (4.8) backward from `E_m=0` gives

\[
E_1=K\sum_{j=0}^{m-2}4^{-j}
=K\frac43(1-4^{-(m-1)}).
\]

Since multiplying the last factor by `3/4` gives `1-4^{-(m-1)}`, direct rearrangement yields

\[
E_1=\frac83(4^{m-1}-1).
\]

Substituting in (4.7),

\[
E_0=2+\frac83(4^{m-1}-1)
=\frac{2(4^m-1)}3.
\]

The process starts in the neutral state, so `E tau_m=E_0`. QED.

## 5. Sharper finite-to-infinite transfer

Let `pi_w` be the unique stationary law of the reachable strip chain and `gamma_w=pi_w(rho)` its stationary strip reward. Couple a fixed reachable start `s` to an independent stationary start using the same future source pairs. By Theorem 3.1 the two trajectories agree after `tau_m`. Since `rho in [0,1]`,

\[
|P_w^t\rho(s)-\gamma_w|\le\Pr(\tau_m>t).
\tag{5.1}
\]

Summing from `t=0` to `N-1` and using the tail-sum identity for an integer-valued positive waiting time gives

\[
\begin{aligned}
|\mathbf E_sR_N-N\gamma_w|
&\le \sum_{t=0}^{N-1}\Pr(\tau_m>t)\\
&\le \sum_{t\ge0}\Pr(\tau_m>t)\\
&=\mathbf E\tau_m.
\end{aligned}
\]

Therefore

\[
\boxed{
|\mathbf E_sR_N-N\gamma_w|
\le \frac{2(4^{2w}-1)}3.
}
\tag{5.2}
\]

Since the strip is a restriction of the unrestricted LCS dynamic program,

\[
\gamma_w\le\gamma_2,
\]

so every exact finite computation now has the improved rigorous source transfer

\[
\boxed{
\gamma_2\ge\gamma_w\ge
\frac{\mathbf E_sR_N}{N}
-\frac{2(4^{2w}-1)}{3N}.
}
\tag{5.3}
\]

This strictly improves the previous P13 constant `w4^(2w)` for every `w>=1`, because with `m=2w>=2`,

\[
\frac{2(4^m-1)}3<\frac m2 4^m.
\]

The asymptotic improvement factor is

\[
\frac{w4^{2w}}{2(4^{2w}-1)/3}
=\frac{3w}{2}\frac{4^{2w}}{4^{2w}-1}
\longrightarrow \frac{3w}{2}.
\tag{5.4}
\]

The boundary-event identity from the preceding P13 report also gets a sharper **finite-horizon** error. For

\[
B_w(S)=\{g_m=0\text{ and the terminal zero-gradient raw-}X\text{ suffix contains both bits}\},
\]

that report proved

\[
\gamma_w=\frac23+\frac13\pi_w(B_w).
\]

Apply (3.3) to `f=1_{B_w}` and couple to stationarity:

\[
\boxed{
\left|\frac23+\frac13\Pr_s(B_w(S_N))-\gamma_w\right|
\le \frac13 a_{2w}(N),
}
\tag{5.5}
\]

where `a_m(N)` is given by the exact recursion (4.1)--(4.4). This is strictly sharper than the previous aligned-block error

\[
\frac13(1-2\,4^{-2w})^{\lfloor N/(2w)\rfloor}
\]

whenever the overlap recursion is strict.

## 6. Exact executed checks and quantitative gain

Artifacts:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T02-06-47Z__overlapping_reset_error_checker.py`

and executed output

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T02-06-47Z__overlapping_reset_error_checker.out`.

The checker re-verifies the `2w` reset on every reachable state through `w=4`, solves the exact rational run-length equations, checks the closed form (4.6), and compares the exact overlapping tail with the old aligned-block tail at `N=4w`.

| `w` | old additive constant `w4^(2w)` | new exact constant `2(4^(2w)-1)/3` | old/new |
|---:|---:|---:|---:|
| 1 | 16 | 10 | 1.600000000000 |
| 2 | 512 | 170 | 3.011764705882 |
| 3 | 12288 | 2730 | 4.501098901099 |
| 4 | 262144 | 43690 | 6.000091554131 |
| 5 | 5242880 | 699050 | 7.500007152564 |

At `N=4w=2m`, the exact overlap tail is strictly smaller than the old two-block bound in every checked case. For example at `w=5`,

\[
a_{10}(20)=\frac{549746900993}{549755813888}
<\frac{274876858369}{274877906944}
=(1-2\,4^{-10})^2,
\]

with exact gap

\[
\frac{6815745}{549755813888}>0.
\]

The output ends `ALL_EXACT_CHECKS_PASS`.

These are self-checks of the finite arithmetic. The theorem-sized claims are proved on the page above.

## 7. Source-level before/after: strict update from P02, kept separate

The preceding P13 report's exact source interval used

\[
U_0=\frac{\log(4t^2)}{\log\lambda},
\qquad
 t=\frac{256717}{800000},
\]

with the inherited C045 rational Collatz parameter `lambda`, giving the displayed decimal prefix

\[
U_0=0.82627594276228262501510658\ldots.
\]

P02's later companion report proves, using the integer scaling of the exact C045 matrix and an algebraic-integer separation argument, an explicit rational

\[
\lambda_* = \lambda-
\frac{1}{2Cb(2a)^{N-1}}
<\lambda,
\]

where its exact data include `N=11614187` and reduced denominator

\[
b=4220452010631561279>1.
\]

Because `0<4t^2<1` and

\[
z\mapsto\frac{\log(4t^2)}{\log z}
\]

is strictly increasing on `(0,1)`, the companion theorem gives

\[
\boxed{
U_*:=\frac{\log(4t^2)}{\log\lambda_*}<U_0.
}
\tag{7.1}
\]

Therefore the project-level exact interval carried into this P13 run moves from

\[
\boxed{L\le\gamma_2\le U_0}
\]

to

\[
\boxed{L\le\gamma_2\le U_*<U_0}.
\tag{7.2}
\]

The gain is astronomically small (P02 estimates the `lambda`-level strictification around `10^{-931054320}`), so the ordinary decimal prefix of the upper endpoint does not visibly change. This is nevertheless a genuine exact source-level shrink, not extra printed digits.

**Separation of credit/scope:** equation (7.2) is the P02 companion's variational/cone-side source movement recovered after P13's prior report. The new P13 overlapping-reset theorem in Sections 3--6 is a distinct boundary-recursion mechanism gain. I do **not** claim that (5.2) by itself improves `L` yet.

Both the internal C045/P02 upper certificate and this new P13 transfer remain pending later independent review under the current progress-first policy; no final determination of `gamma_2` is claimed.

## 8. Honest obstruction and next attack

The new transfer removes a factor asymptotic to `3w/2` from the previous additive error, but its absolute scale is still exponential in the strip width:

\[
\frac{2(4^{2w}-1)}3\asymp \frac23 4^{2w}.
\]

That is not enough, by itself, to turn a feasible large-width finite computation into a new lower endpoint. The inherited exact strip computation also already proves that widths `w<=5` lie below the public lower endpoint, so making their stationary arithmetic more precise cannot move `L`.

The residual mathematical bottleneck is therefore **event-specific**, not generic mixing: exploit the boundary event `B_w` and the one-column nonbranching carry extinction to control `pi_w(B_w)` without enumerating the full reachable strip state space. The next attack should replace full-state synchronization by a smaller suffix/carry renewal that forgets only the information relevant to `B_w`; the quantitative target remains

\[
\pi_w(B_w)>3L-2=0.377997976.
\]

A valid route must preserve the shared raw `Y` bit down each column. A computation in an independent Bernoulli matching field would not transfer to `gamma_2`.

## 9. Ledger delta

```yaml
ledger_delta:
  track: P13
  target: T02-binary-LCS
  source_model: "two independent iid uniform binary strings; correlated match array retained"
  source_status: "OPEN / PARTIAL"
  source_metric:
    lower_before: "L = 99083249/125000000"
    lower_after: "L = 99083249/125000000"
    upper_before: "U_0 = log(4t^2)/log(lambda)"
    upper_after: "U_* = log(4t^2)/log(lambda_*), with lambda_*<lambda from latest P02 exact companion theorem"
    movement: "STRICT SHRINK, companion P02 route; ordinary decimal prefix unchanged"
  p13_mechanism_before:
    finite_to_infinite_additive_error: "w*4^(2w)"
    boundary_horizon_error: "(1/3)*(1-2*4^(-2w))^floor(N/(2w))"
  p13_mechanism_after:
    finite_to_infinite_additive_error: "2*(4^(2w)-1)/3"
    boundary_horizon_error: "(1/3)*a_{2w}(N), exact overlapping-reset avoidance recursion"
    strict_gain: true
  proof_status: "complete on page; exact finite self-check saved"
  independent_review: "pending later review; not a final gamma_2 determination"
  obstruction: "new generic coupling constant remains exponential in w; widths <=5 cannot beat L"
  next_attack: "event-specific suffix/carry renewal for pi_w(B_w), target > 0.377997976"
  companion: "P02 covering/cone/variational route; not duplicated"
  previous_p13_successor_handoff: "P0342 terminal handoff preserved; later P0205 screen admitted no successor; retired clade work not reopened"
```
