Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and no stronger runtime metadata is exposed. SOURCE-LEVEL MOVEMENT SINCE THE PREVIOUS P13 REPORT: the companion P02 primitive-content strictification gives a strictly smaller certified upper endpoint `U_prim < U_prev`, with the lower endpoint `L=0.792665992` unchanged. P13 MECHANISM MOVEMENT: a new one-defect synchronizing family lowers the correlated-strip finite-to-infinite additive constant from `2(4^(2w)-1)/3` to `(8*4^(2w)+10)/21` for every `w>=2`, asymptotic factor `4/7`.**

# P13 / T02 — one-defect boundary reset and exact sharper strip transfer

## 1. Scope, continuity, and source

This run follows `operations/PROGRESS20_2026-09-20.md` and the LIVE20 P13 assignment T02: dependence-preserving boundary recursion for the binary Chvatal--Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The match cells in a common row/column are dependent through the shared source letters. No independent Bernoulli matching model is substituted.

Source recovery remains Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. The current arXiv page states that the binary coefficient is unresolved and explicitly says that incorrect claims from the preprint were removed, retaining only the supported estimate. Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, give the rigorous lower endpoint

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

Consumed repository dependencies only:

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`;
- previous P13 report `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T02-06-47Z__overlapping-reset-error-and-p02-strict-update.md`, blob `f792b0364676dfabaa6da284944deb3ee21fc309`;
- latest P02 companion report `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T02-18-00Z__primitive-content-spectral-gap-report.md`, blob `01d12b7b795f3b628bd37e1897fd61037b15b90c`.

Short pre-LIVE20 P13 handoff, preserved and not reopened: P0342 had already been terminally handed off at frozen metric `2/2`; the later P0205 screen admitted no successor because the source notation `tau(infinity)` was ambiguous. Retired I0051/clade work remains retired.

## 2. Source-level before/after is companion-derived and separate

The preceding P13 report carried P02's then-current algebraic-integer strictification. Write its exact source upper endpoint as

\[
U_{\rm prev}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm old})},
\qquad t=\frac{256717}{800000}.
\]

The new P02 report extracts primitive scalar content before applying the algebraic-integer separation argument and proves exactly

\[
\varepsilon_{\rm prim}=K^N\varepsilon_{\rm old},
\qquad
K=36663618914556095488>1,
\qquad N=11614187.
\]

Hence `epsilon_prim > epsilon_old`. Since `0<4t^2<1`, `0<lambda-epsilon_prim<lambda-epsilon_old<1`, and

\[
z\longmapsto \frac{\log(4t^2)}{\log z}
\]

is strictly increasing on `(0,1)`, the project-level source interval moves from

\[
\boxed{L\le\gamma_2\le U_{\rm prev}}
\]

to

\[
\boxed{L\le\gamma_2\le U_{\rm prim}<U_{\rm prev}},
\qquad
U_{\rm prim}:=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})}.
\]

This strict source shrink is P02's complementary variational/covering contribution since the previous P13 report. P13 does not duplicate that proof. At ordinary decimal precision the change is invisible because the exact spectral separation is extremely small.

The new P13 theorem below is a separate mechanism gain. It improves every finite correlated-strip lower transfer, but in this run it does **not** itself raise the best source lower endpoint above `L`; no finite computation is promoted to a gamma_2 bound unless the proved transfer is applied.

## 3. Exact correlated boundary recursion

Fix strip half-width `w` and put

\[
m=2w.
\]

A formal strip boundary state is

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m)\in\{0,1\}^{2m}.
\]

Reachable LCS-strip states form a subset, but the reset theorem below will hold on **all** formal states.

For one fresh source pair `(u,v)` (independent fair bits, but with the same `v` used against every old `x_i` in this column), define

\[
d_0=0,
\qquad
 d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\quad 1\le i\le m.
\tag{3.1}
\]

Then

\[
x'=(x_2,\ldots,x_m,u),
\tag{3.2}
\]

\[
g_i'=g_{i+1}+d_{i+1}-d_i,
\quad 1\le i<m,
\tag{3.3}
\]

\[
g_m'=(1-d_m){\bf1}_{\{u=v\}}.
\tag{3.4}
\]

This is the true dependent-string transition. In particular the entire column shares one random bit `v`; no independent cell field appears.

Write

\[
A=(0,1),\qquad B=(1,0),\qquad C=(0,0),\qquad D=(1,1).
\]

## 4. New theorem: one defect inside an almost-reset run still synchronizes

### Lemma 4.1 — zero-suffix growth under `A`

After `k` consecutive `A` inputs, `0<=k<=m`, the final `k` coordinates of both `x` and `g` are zero, for every formal starting state.

**Proof.** Induct on `k`. The statement is empty for `k=0`. Assume the final `k` coordinates are `(x_i,g_i)=(0,0)`. Under `A` we have `u=0,v=1`, so the shifted raw window acquires one additional terminal zero. Also `g_m'=0` because `u!=v`. For each output index whose old successor lies in the common zero suffix, the carry recursion sees `x_{i+1}=0`, `g_{i+1}=0`, `v=1`, hence `d_{i+1}=d_i`; (3.3) gives `g_i'=0`. Thus the zero suffix grows from length `k` to `k+1`. QED.

In particular `A^m` sends every formal state to `(0^m;0^m)`. By bit-complement symmetry, `B^m` is also a constant map.

### Theorem 4.2 — one-defect reset

For every source-pair letter `Z=(u,v) in {A,B,C,D}`,

\[
\boxed{A^{m-1}ZA\text{ is a constant map on all formal states}.}
\tag{4.1}
\]

More precisely, its terminal state is

\[
\boxed{
(x;g)=\bigl(0^{m-2},u,0;\ 0^{m-2},u,0\bigr),
}
\tag{4.2}
\]

where `u` is the first coordinate of `Z`. By bit-complement symmetry, every word `B^{m-1}ZB` is likewise a constant map.

**Proof.** By Lemma 4.1, after the first `m-1` copies of `A` the state has the form

\[
x=(a,0^{m-1}),\qquad g=(b,0^{m-1})
\tag{4.3}
\]

for some bits `a,b`; these are the only remnants of the initial state.

First suppose the defect has `v=0`. Put

\[
q=(1-b){\bf1}_{\{a=0\}}.
\]

At the defect column, `d_1=q`, while for every `i>=2` the old letter is `x_i=0`, the old gradient is `g_i=0`, and this now **matches** `v=0`; hence `d_i=1`. Equations (3.2)--(3.4) therefore give

\[
x^Z=(0^{m-1},u),
\qquad
g^Z=(1-q,0^{m-1}).
\tag{4.4}
\]

Apply the final `A=(0,1)`. Along positions `1,...,m-1` the raw letters are zero and mismatch `v=1`, so the carries are all zero. At the final position the carry is exactly `u`. Thus the only nonzero possible output gradient is at index `m-1`, and it equals `u`; the final gradient is zero. The shifted raw window is also `(0^{m-2},u,0)`. This proves (4.2) when `v=0`.

Now suppose `v=1`. At the defect column let

\[
q=(1-b){\bf1}_{\{a=1\}}.
\]

The trailing zeros mismatch `v=1`, so the carry remains equal to `q` throughout that suffix. Hence

\[
x^Z=(0^{m-1},u),
\qquad
g_i^Z=0\ (i<m),
\qquad g_m^Z=(1-q){\bf1}_{\{u=1\}}.
\tag{4.5}
\]

Apply the final `A`. Its carry is zero through positions `1,...,m-1`. If `u=0`, then `g_m^Z=0` and the last carry is zero. If `u=1`, the last output-gradient increment is

\[
g_m^Z+(1-g_m^Z)=1.
\]

Thus again the terminal raw window and gradient vector are both `(0^{m-2},u,0)`, independent of `a,b`. This proves (4.2) in all cases.

Finally, simultaneous bit complementation `x_i -> 1-x_i`, `(u,v)->(1-u,1-v)` preserves every equality indicator in (3.1)--(3.4), sends `A` to `B`, and therefore gives the `B^{m-1}ZB` statement. QED.

The three choices `Z!=A` in (4.1), and the three bit-complementary choices `Z!=B`, are genuinely new reset words: they contain neither `A^m` nor `B^m`.

## 5. Exact reset automaton and exact mean coupling time

Let `tau_m^dagger` be the first ending time at which the iid source-pair stream contains one of

\[
\mathcal R_m=
\{A^m,B^m\}
\cup\{A^{m-1}ZA:Z\ne A\}
\cup\{B^{m-1}ZB:Z\ne B\}.
\tag{5.1}
\]

Every word in `R_m` is a constant map, so two strip chains driven by the same future source pairs have coupled by `tau_m^dagger`.

For `m>=3`, the expected waiting time is exactly solvable with only `m+2` symmetry classes. Let

- `E_0` be the expected remaining time from the neutral prefix state;
- `E_r`, `1<=r<=m-1`, be the expected remaining time given a current run of `r` identical mismatch letters (`A` or `B`);
- `F` be the armed-opposite state, e.g. suffix `A^{m-1}B`;
- `G` be the armed-neutral state, e.g. suffix `A^{m-1}C` or `A^{m-1}D`.

The exact source-pair probabilities give

\[
E_0=1+\frac12E_1+\frac12E_0,
\tag{5.2}
\]

\[
E_r=1+\frac14E_{r+1}+\frac14E_1+\frac12E_0,
\qquad1\le r\le m-2,
\tag{5.3}
\]

\[
E_{m-1}=1+\frac14F+\frac12G,
\tag{5.4}
\]

\[
F=1+\frac14E_2+\frac12E_0,
\qquad
G=1+\frac14E_1+\frac12E_0.
\tag{5.5}
\]

The omitted probability in (5.4)--(5.5) is immediate absorption.

Set

\[
K=2+\frac34E_1.
\]

From (5.2), `E_0=2+E_1`; hence (5.3) becomes

\[
E_r=K+\frac14E_{r+1}.
\tag{5.6}
\]

Also `G=K`. Using the `r=1` instance of (5.6) in the formula for `F` gives

\[
F=\frac34E_1.
\tag{5.7}
\]

Therefore

\[
E_{m-1}=2+\frac9{16}E_1.
\tag{5.8}
\]

Let `q=4^{-(m-2)}`. Iterating (5.6) from `r=1` to `m-1`,

\[
E_1
=K\sum_{j=0}^{m-3}4^{-j}+qE_{m-1}
=\left(2+\frac34E_1\right)\frac43(1-q)
+q\left(2+\frac9{16}E_1\right).
\]

Rearrangement gives

\[
\frac{7q}{16}E_1=\frac{8-2q}{3},
\]

so

\[
E_1=\frac{8\,4^m-32}{21}
\]

and finally

\[
\boxed{
\mathbf E\tau_m^\dagger=E_0=rac{8\,4^m+10}{21},
\qquad m\ge3.
}
\tag{5.9}
\]

For the exceptional `m=2` automaton the exact value is `114/17`; it is not needed for the general width-`w>=2` theorem.

### Exact finite-horizon recursion

The same prefix automaton gives a finite-horizon tail without any independence approximation. Let `n_t` be surviving mass in the neutral state, `r_{t,j}` surviving mass in a run state of length `j`, `f_t` in the armed-opposite state and `g_t` in the armed-neutral state. For `m>=3`, starting from `n_0=1` and all other masses zero,

\[
n_{t+1}=\frac12n_t+\frac12\sum_{j=1}^{m-2}r_{t,j}+\frac12f_t+\frac12g_t,
\tag{5.10}
\]

\[
r_{t+1,1}=\frac12n_t+\frac14\sum_{j=1}^{m-2}r_{t,j}+\frac14g_t,
\tag{5.11}
\]

\[
r_{t+1,2}=\frac14r_{t,1}+\frac14f_t,
\tag{5.12}
\]

\[
r_{t+1,j+1}=\frac14r_{t,j},\qquad2\le j\le m-2,
\tag{5.13}
\]

\[
f_{t+1}=\frac14r_{t,m-1},
\qquad
g_{t+1}=\frac12r_{t,m-1}.
\tag{5.14}
\]

Thus

\[
\Pr(\tau_m^\dagger>t)
=n_t+\sum_{j=1}^{m-1}r_{t,j}+f_t+g_t.
\tag{5.15}
\]

All randomness here is the actual iid source-pair stream `(U_t,V_t)`; the shared-column dependence is preserved exactly.

## 6. New finite-to-infinite bound

Let `pi_w` be the stationary law of the reachable width-`w` strip chain, `rho in {0,1}` its one-step diagonal reward, and

\[
\gamma_w=\pi_w(\rho).
\]

Couple a chain from any reachable state `s` with a stationary chain using the same future source pairs. Theorem 4.2 and the old `A^m/B^m` reset imply that the chains coincide from time `tau_m^dagger` onward. Therefore

\[
|P_w^t\rho(s)-\gamma_w|
\le \Pr(\tau_m^\dagger>t).
\tag{6.1}
\]

For cumulative reward `R_N`, summing and using the tail-sum identity gives

\[
\begin{aligned}
|\mathbf E_sR_N-N\gamma_w|
&\le\sum_{t=0}^{N-1}\Pr(\tau_m^\dagger>t)\\
&\le\mathbf E\tau_m^\dagger.
\end{aligned}
\]

With `m=2w` and `w>=2`, (5.9) yields the new exact additive transfer

\[
\boxed{
|\mathbf E_sR_N-N\gamma_w|
\le C_w^\dagger:=\frac{8\,4^{2w}+10}{21}.
}
\tag{6.2}
\]

Because a width-`w` strip restricts the unrestricted LCS dynamic program,

\[
\gamma_w\le\gamma_2,
\]

so every exact finite computation has the certified source lower transfer

\[
\boxed{
\gamma_2\ge\gamma_w\ge
\frac{\mathbf E_sR_N}{N}
-\frac{8\,4^{2w}+10}{21N}.
}
\tag{6.3}
\]

The previous P13 overlapping-run constant was

\[
C_w^{\rm old}=\frac{2(4^{2w}-1)}3.
\]

The improvement is exact:

\[
\boxed{
C_w^{\rm old}-C_w^\dagger
=\frac{2(4^{2w}-4)}7>0
\qquad(w\ge2).
}
\tag{6.4}
\]

Moreover

\[
\frac{C_w^\dagger}{C_w^{\rm old}}\longrightarrow\frac47.
\tag{6.5}
\]

Thus the additive finite-to-infinite error is cut asymptotically by `3/7`, not merely by a lower-order correction.

The inherited boundary-event identity also immediately sharpens. If `B_w` is the mixed terminal zero-gradient-suffix event from the preceding report, then

\[
\gamma_w=\frac23+\frac13\pi_w(B_w),
\]

and (5.15) gives

\[
\boxed{
\left|\frac23+\frac13\Pr_s(B_w(S_N))-\gamma_w\right|
\le \frac13\Pr(\tau_{2w}^\dagger>N),
}
\tag{6.6}
\]

with the right side computed exactly by the finite recursion (5.10)--(5.15).

## 7. Executed exact checks

Artifacts:

- `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T03-03-05Z__defect_reset_error_checker.py`
- `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T03-03-05Z__defect_reset_error_checker.out`

The checker exhaustively verifies `A^{m-1}ZA` and `B^{m-1}ZB` on **all** `4^m` formal states for `m=2,...,7`, independently solves the exact prefix-automaton linear system for `m=2,...,10`, and checks (5.9) exactly for every `m>=3` in that range. The executed output ends `ALL_EXACT_CHECKS_PASS`.

Selected exact constants:

\[
\begin{array}{c|c|c|c}
w&C_w^{\rm old}&C_w^\dagger&\text{gain}\\\hline
2&170&98&72\\
3&2730&10926/7&8184/7\\
4&43690&174766/7&131064/7\\
5&699050&399458&299592
\end{array}
\]

The finite checker is a self-check of the finite core, not an independent proof audit. The written derivation above is the general proof.

## 8. Failed route / obstruction / next attack

The earlier exploratory repeated-jump Chernoff route in the `00-47-00Z` artifacts remains **rejected for theorem use**: it would require a conditional freshness statement for lookahead raw `X` bits after conditioning on the evolving correlated boundary state. That conditional independence was not proved, so none of its stronger numerical tails are used here.

The new reset theorem fixes a different obstruction cleanly: the previous coupling discarded near-reset trajectories that reached `m-1` equal mismatch pairs and were interrupted once. Allowing exactly one defect followed by the original mismatch letter cuts the general additive constant from asymptotic `(2/3)4^{2w}` to `(8/21)4^{2w}`.

Residual obstruction: `C_w^dagger` is still exponential in the width. Therefore it is too expensive by itself to turn a moderate finite horizon at wide `w` into a competitive new lower endpoint. The next attack should be **event-specific rather than full-state synchronization**: use the exact nonbranching carry-extinction identity to couple only the terminal mixed-suffix event `B_w`, while conditioning on the actual source-pair filtration so that no unproved freshness assumption is introduced. A successful event-specific coupling with scale closer to `2^w` (or polynomial in `w`) could make the exact boundary-event formula computationally competitive with the public lower endpoint.

## 9. Status and ledger_delta

The source problem remains **OPEN / PARTIAL**. This run does not determine `gamma_2` and makes no novelty claim from bounded source checking.

`source_before` (previous P13-carried project interval):

`L <= gamma_2 <= U_prev`.

`source_after` (latest companion-certified project interval):

`L <= gamma_2 <= U_prim < U_prev`.

`p13_mechanism_before`:

`|E_s R_N - N gamma_w| <= 2(4^(2w)-1)/3`.

`p13_mechanism_after` for every `w>=2`:

`|E_s R_N - N gamma_w| <= (8*4^(2w)+10)/21`.

`ledger_delta`:

```yaml
slot: P13
parent: T02-binary-LCS
model: iid-uniform-binary-strings
independent_bernoulli_matching_used: false
source_status: OPEN_PARTIAL
source_lower: 99083249/125000000
source_upper_before: U_prev
source_upper_after: U_prim
source_upper_strict_improvement: true
source_improvement_origin: P02-primitive-content-companion
mechanism: one-defect-synchronizing-boundary-reset
strip_error_old: 2*(4^(2w)-1)/3
strip_error_new: (8*4^(2w)+10)/21
strip_error_scope: all w>=2, all reachable starts, all finite N
strip_error_asymptotic_ratio_new_over_old: 4/7
finite_core_checker: PASS_SELF_CHECK
rejected_route: repeated-jump-Chernoff-with-unproved-conditional-freshness
next_attack: event-specific-B_w-coupling-under-source-pair-filtration
previous_p13_successor_handoff: P0342-terminal; P0205-not-admitted
retired_clade_reopened: false
```

No peer file, historical report, POSTED entry, claim, schedule, permission, email/Drive resource, public post or workflow was modified.
