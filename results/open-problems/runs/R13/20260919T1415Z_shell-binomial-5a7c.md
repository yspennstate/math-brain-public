Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **FIXED UPPER METRIC MOVED:** `B_R13(86): 728141/100000 = 7.28141 -> 728139/100000 = 7.28139`, exact decrease `2/100000 = 1/50000 = 0.00002`; fixed-upper stagnation resets/remains at `0`. Methods actually used: **#13 FIND WHAT ONLY INCREASES, #19 MAKE IT AN ALGORITHM, #29 ADD THE POINTS AT INFINITY.**

# R13 — Boolean Komlós: monotone tilted transform, compactification at infinity, and shellwise recovery of omitted binomial mass

Run ID: `20260919T1415Z_shell-binomial-5a7c`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, source status, and fixed metric

I continued from the newest immutable R13 report

`runs/R13/20260919T1233Z_localized-cstar-7d3a.md`

at creation commit

`912cad73b90f8c906eda2b2837560b62cd843abb`,

rather than restarting the source or re-deriving the older finite-dimensional chain. Before doing new mathematics I reread/reconciled the required repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current I0091 source-status reconciliation, the newest R13 report/checker chain, the newest neighboring discrepancy/successor report visible in R02, and the canonical intake alias history. Boolean Komlós remains the R13 mathematical target; no posted exclusion or ownership change superseded this quantitative finite-dimensional continuation.

Fresh primary-source navigation on 2026-09-19 still gives the same qualitative status:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 2026-09-10, prove the genuine real-sign dimension-free bound `3 sqrt(2 pi)`;
- Akbas--Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 2026-09-17, recover Komlós among their real-Boolean consequences, but their displayed finite constant still depends on unnamed upstream universal constants;
- Bansal--Jiang, arXiv:2508.03961v2, remains the earlier `~O((log n)^(1/4))` real-Boolean comparison route.

Thus the **qualitative source status is KNOWN / RESOLVED in current 2026 preprint literature**. R13 is only a finite-dimensional quantitative sharpening track. Complex phases, vector colorings, and average-case statements are not substituted for the Boolean theorem.

The predecessor fixes

\[
K_{86}^*\le \frac{728141}{100000}=7.28141,
\qquad
K_{86}^*\ge \frac{225925611947}{10^{11}}=2.25925611947.
\]

The immediately preceding Section-B triple was `#8/#12/#27`. All thirty labels have appeared somewhere in the longer R13 history, so a literal globally-unused-label requirement is no longer satisfiable; the operative rule is to use a genuinely different route and not repeat the preceding triple. This run uses `#13/#19/#29` on a new mathematical mechanism.

## 2. Retained finite-dimensional DTV setup

Keep the certified cosine-power exponent

\[
p=\frac{33}{20},\qquad
\beta=\frac{13}{40},\qquad
a=\frac{53}{40},\qquad D=139.
\]

For

\[
Y\sim\operatorname{InvGamma}\left(\frac{53}{40},\frac{13}{40}\right),
\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\]

the real-Boolean directional-total-variation construction gives

\[
C_{33/20,D}
=
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}\,\mathbb E\sqrt{X_D}.
\tag{2.1}
\]

The exact Laplace transform is

\[
L(s)=
{}_0F_1\left(; -\frac{13}{40};\frac{13s}{40}\right)
+c_*s^{53/40}
{}_0F_1\left(;\frac{93}{40};\frac{13s}{40}\right),
\tag{2.2}
\]

and the tilted transform is

\[
G(s):=e^sL(s)=\mathbb E e^{-s(Y-1)}.
\tag{2.3}
\]

The predecessor checker certifies the lower polynomial `Z_old` after the substitution `t=u^40`, so that on `0<=u<=43/40`,

\[
G(t/139)\ge1+Z(u),\qquad Z(u)\ge0.
\tag{2.4}
\]

It also certifies

\[
c_*>0.78476,
\qquad
139^{-1/40}>\frac{8839437}{10^7},
\tag{2.5}
\]

while the older transform polynomial used only `0.78472`. Thus the coefficient improvement is

\[
\Delta c=\frac4{100000}.
\tag{2.6}
\]

The predecessor retained only the first six positive binomial layers of `(1+Z)^139-1`, and then added only the **linear** contribution from (2.6) on the short interval `0<=u<=41/40`. Its exact rational Jensen-defect floor was

\[
\delta_{\rm prev}
:=1-\mathbb E\sqrt{X_{139}}
>
0.05374822227154238\ldots .
\tag{2.7}
\]

This run does not change `p`, `D`, or `c_*`; it recovers positive mass that those earlier certificates deliberately discarded.

## 3. Method #13 — FIND WHAT ONLY INCREASES: the tilted transform is monotone

The useful invariant is not a new scalar estimate but a global shape fact about (2.3). Since

\[
G(s)=\mathbb E e^{-s(Y-1)},
\]
`G` is convex on `[0,infinity)`. Also

\[
G(0)=1,
\qquad
G'(0)=-\mathbb E(Y-1)=0,
\]
because the normalized inverse-gamma variable has `E Y=1`. Convexity therefore implies

\[
\boxed{G'(s)\ge0\quad(s\ge0),\qquad G(s)\ge1.}
\tag{3.1}
\]

This is the monotone quantity the previous local-transform proof did not exploit explicitly. It says that every extra positive lower contribution to `G-1` remains usable without having to worry that the tilt later falls below one.

A companion consequence is Jensen's inequality:

\[
L(t/D)^D
=\left(\mathbb E e^{-(t/D)Y}\right)^D
\ge e^{-t\mathbb EY}=e^{-t},
\tag{3.2}
\]
so the exact Jensen-defect integrand is globally nonnegative.

**Outcome #13:** a new global monotonicity/nonnegativity mechanism. It does not by itself move the metric, but it licenses the compactification and positive-term recovery below.

## 4. Method #29 — ADD THE POINTS AT INFINITY: the omitted tail is rigorously harmless

The Jensen identity is

\[
\delta_D
=
\frac1{2\sqrt\pi}
\int_0^\infty
\big[L(t/D)^D-e^{-t}\big]t^{-3/2}\,dt
\tag{4.1}
\]

or, after tilting,

\[
\delta_D
=
\frac1{2\sqrt\pi}
\int_0^\infty
 e^{-t}\big[G(t/D)^D-1\big]t^{-3/2}\,dt.
\tag{4.2}
\]

By (3.1)--(3.2), the integrand in (4.1) and (4.2) is nonnegative for every `t>=0`. Therefore a finite interval is a genuine lower certificate with no tail penalty:

\[
\delta_D
\ge
\frac1{2\sqrt\pi}
\int_0^T
 e^{-t}[G(t/D)^D-1]t^{-3/2}\,dt
\tag{4.3}
\]

for every `T>0`. In this sense infinity is a harmless boundary point: once the finite core is controlled, the entire remaining ray can be discarded rather than approximated.

This matters for the new shell algorithm because we can stop exactly at a rational endpoint in the `u` variable and keep only manifestly positive contributions.

**Outcome #29:** a rigorous tail-elimination principle for this DTV transform. No separate metric claim is made from it alone.

## 5. Method #19 — MAKE IT AN ALGORITHM: shellwise positive-term recovery

This method moves the fixed metric.

Write, on the predecessor interval,

\[
G(t/139)\ge1+Z(u)+w(u),
\qquad t=u^{40},
\tag{5.1}
\]
where `Z` is the old nonnegative lower polynomial and the sharpened Frobenius coefficient gives

\[
139\,w(u)
\ge
\Delta c\,\left(\frac{8839437}{10^7}\right)^{13}u^{53}.
\tag{5.2}
\]

Expand

\[
\begin{aligned}
(1+Z+w)^{139}-1
={}&[(1+Z)^{139}-1]\\
&+139w(1+Z)^{138}\\
&+\sum_{j=2}^{139}\binom{139}{j}w^j(1+Z)^{139-j}.
\end{aligned}
\tag{5.3}
\]

Every term displayed is nonnegative because `Z,w>=0`. The predecessor used only:

1. the `Z^k` terms for `k=1,...,6` globally on its compact interval;
2. the `r=0` part of the linear `139w(1+Z)^{138}` term, and only on `0<=u<=41/40`.

Everything below is therefore genuinely new positive mass, not double counting.

### 5.1 Exact shell floors for `Z/u^53`

Take the rational endpoint

\[
U_2=\frac{537}{500}=1.074<\frac{43}{40}.
\tag{5.4}
\]

Partition `[0,U_2]` into nine rational shells:

\[
[0,1],
[1,1.01],
[1.01,1.02],
[1.02,1.03],
[1.03,1.04],
[1.04,1.05],
[1.05,1.06],
[1.06,1.07],
[1.07,1.074].
\tag{5.5}
\]

Let

\[
Q(u):=\frac{Z(u)}{u^{53}}.
\]

On a shell `[l,r]`, each positive coefficient monomial of `Q` is bounded below at `l`, and each negative coefficient monomial is bounded below at `r`. The resulting exact rational shell floor is

\[
m(l,r)
=
\sum_{c_j>0}c_jl^j+
\sum_{c_j<0}c_jr^j.
\tag{5.6}
\]

All nine exact margins are positive. Their decimal diagnostics are

\[
\begin{array}{c|c}
\text{shell}&m(l,r)\\ \hline
[0,1]&0.0010970238409241985\\
[1,1.01]&0.0010943478752272668\\
[1.01,1.02]&0.001083258069530822\\
[1.02,1.03]&0.0010695608855624467\\
[1.03,1.04]&0.0010527348960828239\\
[1.04,1.05]&0.0010321377047612646\\
[1.05,1.06]&0.0010069185639549976\\
[1.06,1.07]&0.0009758247162828458\\
[1.07,1.074]&0.0009926701357806358.
\end{array}
\tag{5.7}
\]

The checker also independently re-verifies the predecessor global factor margin

\[
\frac{Z(u)}{u^{53}}>0.0008358012867340186
\quad(0<u\le43/40).
\tag{5.8}
\]

### 5.2 Exact positive weight for `e^{-t}`

Use the odd Taylor polynomial

\[
W_{61}(t)=\sum_{j=0}^{61}\frac{(-t)^j}{j!}.
\tag{5.9}
\]

Taylor's theorem gives `W_61(t)<=e^{-t}` for `t>=0`. Also

\[
W_{61}'(t)=-W_{60}(t),
\]
and the even partial sum `W_60(t)>=e^{-t}>0`, hence `W_61` is decreasing. The exact endpoint test gives

\[
W_{61}(U_2^{40})
=2.6239622167692963\ldots\times10^{-8}>0.
\tag{5.10}
\]

Thus `W_61` is nonnegative on the entire compact interval, so multiplying it by the positive binomial lower terms preserves inequality direction.

### 5.3 Three disjoint recovered contributions

The exact checker recovers three positive pieces beyond the predecessor floor.

**(i) Linear-tail extension.** Extend the already-counted `r=0` linear term from `u=41/40` to `u=537/500`:

\[
\Delta_{\rm lin,tail}
>1.2398465975648284\times10^{-7}.
\tag{5.11}
\]

**(ii) Previously omitted old-base binomial layers.** Recover `Z^k`, `k=7,...,12`, shellwise:

\[
\Delta_{7:12}
>1.779239260201759\times10^{-6}.
\tag{5.12}
\]

**(iii) Cross terms from the improved coefficient.** In

\[
139w(1+Z)^{138}
=139w\sum_{r=0}^{138}\binom{138}{r}Z^r,
\]
recover `r=1,...,7` shellwise:

\[
\Delta_{wZ}
>4.6820862851935045\times10^{-7}.
\tag{5.13}
\]

These are pairwise disjoint from the predecessor's retained contributions, so

\[
\Delta_{\rm new}
=
\Delta_{\rm lin,tail}+
\Delta_{7:12}+
\Delta_{wZ}
>2.371432548477592\times10^{-6}.
\tag{5.14}
\]

Combining with (2.7),

\[
\boxed{
1-\mathbb E\sqrt{X_{139}}
>0.053750593704090854\ldots .}
\tag{5.15}
\]

The retained exact prefactor bound is

\[
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}
<\frac{7694998}{10^6}=7.694998,
\tag{5.16}
\]
which is verified from `pi<355/113`. Therefore

\[
C_{33/20,139}
<7.281387288948208\ldots
<\boxed{\frac{728139}{100000}=7.28139}.
\tag{5.17}
\]

The exact-arithmetic execution terminates

`R13_SHELL_BINOMIAL_RECOVERY_EXACT_PASS`.

**Outcome #19:** success; the fixed metric moves.

## 6. Active-row pruning and the source-matching finite theorem

Set

\[
h=\frac{728139}{100000}=7.28139.
\]

For an arbitrary real `m x 86` matrix with Euclidean column norms at most one, call row `r_i` active when

\[
\|r_i\|_2>\frac h{\sqrt{86}}.
\]

Since

\[
\sum_i\|r_i\|_2^2\le86
\]
and exact arithmetic gives

\[
139<\frac{86^2}{h^2}
=139.49810771594062\ldots<140,
\tag{6.1}
\]
there are at most `139` active rows. Apply the `D=139` genuine real-Boolean DTV theorem with (5.17) to the active rows. Every inactive row is at most `h` by Cauchy--Schwarz. Hence

\[
\boxed{K_{86}^*\le\frac{728139}{100000}=7.28139.}
\tag{6.2}
\]

The exact fixed-metric movement is

\[
\frac{728141}{100000}-\frac{728139}{100000}
=\boxed{\frac1{50000}=0.00002}.
\tag{6.3}
\]

The retained lower obstruction is unchanged, so the current same-dimension certified interval is

\[
\boxed{2.25925611947\le K_{86}^*\le7.28139.}
\tag{6.4}
\]

## 7. Complete current universal upper envelope `B_R13(n)`

Define

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\tag{7.1}
\]

### 7.1 Oldest retained DTV row-pruning branch

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\tag{7.2}
\]

### 7.2 Retained one-threshold branch

\[
D_*(n)=
\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=
\max\left\{\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\tag{7.3}
\]

### 7.3 Retained three-threshold occupancy branch

The exact predecessor defines

\[
\begin{aligned}
Q_D^{(3)}(x)=1&-(1-a_3x)^D
-D(a_3-a_1)x(1-a_3x)^{D-1}\\
&-\binom D2[(a_3-a_2)^2+2(a_2-a_1)(a_3-a_2)]
 x^2(1-a_3x)^{D-2}
\end{aligned}
\tag{7.4}
\]
with the same exact threshold constants `a_1,a_2,a_3` and failed-threshold conventions fixed in the immutable predecessor chain. Writing

\[
Q_D^{(3)}(x)=\sum_{\ell=1}^D c_{\ell,D}^{(3)}x^\ell,
\]

\[
\beta_D^{\uparrow,3}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(3)}
\left[
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right].
\tag{7.5}
\]

With

\[
D_9(n)=
\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=
\max\left\{
\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D_9(n)}^{\uparrow,3})
\right\}.
\tag{7.6}
\]

### 7.4 Retained lower-tail branches

For every integer `D>=135`, keep exactly the predecessor conditional-tail functions and their zero convention when a threshold feasibility test fails:

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\]

\[
L_-(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\tag{7.7}
\]

and for `r=2,3,4`,

\[
C_D^{(r)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\]

\[
L_r(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\tag{7.8}
\]

These symbols mean the exact finite conditional-tail formulae, constants, shell thresholds, and failed-threshold zero conventions in `runs/R13/20260919T1233Z_localized-cstar-7d3a.md` and its immutable predecessor chain; no asymptotic shorthand or changed parameter range is introduced here.

### 7.5 Retained five-threshold occupancy / Cantelli branch

For `k=1,...,5`,

\[
A_{k,D}=
\frac{5}{7(4437/5000)}
\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},
\qquad
a_k=A_{k,D}/D,
\tag{7.9}
\]

with `a_0=0` and `d_k=a_k-a_{k-1}`. Define

\[
F_{1,0}=1,
\qquad
F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!},
\]

\[
C_{D,5}(x)=
\sum_{r=0}^4
\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r}.
\tag{7.10}
\]

Write

\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]

\[
\beta_{D,5}^{\uparrow}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right].
\tag{7.11}
\]

Keep exactly the predecessor truncated `U=157/20`, four-shell Cantelli lower-tail functional `\beta_{D,5}^{\downarrow}` and all its feasibility/zero conventions. Then

\[
L_5(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\frac n{\sqrt{D+1}}
\right\}.
\tag{7.12}
\]

### 7.6 Retained transform branch and the moved branch

\[
L_{\rm LT}(n)=
\max\left\{
\frac{739097}{100000},
\frac n{\sqrt{136}}
\right\},
\tag{7.13}
\]

and the new pointwise-improving branch is

\[
\boxed{
L_{33/20}^{\rm shell}(n)=
\max\left\{
\frac{728139}{100000},
\frac n{\sqrt{140}}
\right\}.}
\tag{7.14}
\]

It strictly dominates the predecessor

\[
L_{33/20}^{\rm loc}(n)=
\max\left\{\frac{728141}{100000},\frac n{\sqrt{140}}\right\}
\]
pointwise.

Therefore the complete current fixed metric is

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&5\le n\le85,\\[2mm]
\min\{G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&n\ge86.
\end{cases}}
\tag{7.15}
\]

All constants, integer-domain restrictions, ceilings, infima, threshold feasibility tests, and inherited tail-zero conventions remain exactly those of the predecessor chain. Only the last branch changes this run.

## 8. Exact checker, output, and reproducibility

The exact checker is

`artifacts/R13/20260919T1415Z_shell-binomial-5a7c_checker.py`

created at commit

`b869093fe84664df3bb150238c58fd2e4b006422`.

Its archived execution output is

`artifacts/R13/20260919T1415Z_shell-binomial-5a7c.out`

created at commit

`d2ce51a9aa0fd48bc35268eda03ad9705619ae41`.

The checker uses Python `Fraction` throughout every acceptance test. Decimal values are diagnostics only. Its output records

```text
R13_SHELL_BINOMIAL_RECOVERY_EXACT_PASS
gautschi_relative_margin = 4.04577511371523e-06
W61_endpoint = 2.6239622167692963e-08
global_Z_factor_margin = 0.0008358012867340186
shell_count = 9
delta0 = 0.053745767
inc_prev = 2.4552715423799785e-06
delta_prev = 0.05374822227154238
lin_tail = 1.2398465975648284e-07
old_extra_k7_k12 = 1.779239260201759e-06
cross_extra_r1_r7 = 4.6820862851935045e-07
new_extra_total = 2.371432548477592e-06
delta_new = 0.053750593704090854
C_upper = 7.281387288948208
old_h = 7.28141
new_h = 7.28139
improvement = 2e-05
row_ratio = 139.49810771594062
```

This is a self-check, not an outside audit.

## 9. Prior-art and novelty status

The general DTV route is published/preprinted in Guo--Fang--Lu, and the inverse-gamma/cosine-power family is built on that route. A fresh bounded search checked the current Komlós papers and searched for the specific numerical constant `7.28139`, the rational exponent `33/20`, and the inverse-gamma/Frobenius finite-dimensional mechanism. I did not find this exact shellwise binomial-recovery sharpening. That is only bounded negative evidence, not a priority proof.

Therefore

**novelty = UNVERIFIED.**

No claim is made that the qualitative Komlós theorem is new; it is already KNOWN in the current 2026 preprint literature.

## 10. Model / scheduler-control truthfulness

The exposed task-control interface still has prompt/title, schedule or timing, enablement, and update/list controls, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. GPT-6/maximum therefore remains prompt-only on this surface.

The historical P26 response `You cannot modify this task` was an authorization-context boundary. Repository evidence records a later successful P26 update from a different authorized context. The legitimate remedy for any such refusal is the owning/authorized product or workspace surface, explicit owner/admin access where supported, or platform support — never task duplication, identity substitution, or permission bypass.

No scheduler, workflow, permission, email, Drive, purchase, or public-posting action was made in this run.

## 11. Status and next route

Status after this run:

**SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED UPPER METRIC MOVED / fixed-upper stagnation count 0 / exact self-check PASS / outside audits of this sharpening 0/2 / novelty UNVERIFIED.**

The next run should not merely add more shell layers or another decimal to the same polynomial. This shell algorithm has exposed the next genuinely different possibilities: use a nonproduct density that changes the balanced-direction law, derive a finite explicit constant chain from a different Boolean-small-ball mechanism, or prove a small-column universal theorem strong enough to improve the block compiler. If the fixed upper metric goes unchanged for three consecutive runs, the owner-prescribed stuck protocol applies.

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  metric:
    name: complete_rigorously_certified_universal_upper_envelope_B_R13
    distinguished_dimension: 86
    before: "728141/100000"
    after: "728139/100000"
    before_decimal: 7.28141
    after_decimal: 7.28139
    exact_movement: "1/50000"
    movement: true
  same_dimension_lower_obstruction:
    value: "225925611947/100000000000"
    decimal: 2.25925611947
    movement: false
  current_interval_n86: "2.25925611947 <= K_86^* <= 7.28139"
  moved_branch:
    name: L_33_over_20_shell
    formula: "max{728139/100000, n/sqrt(140)}"
  methods: [13, 19, 29]
  previous_methods: [8, 12, 27]
  proof_mechanism:
    - tilted_transform_G_is_nondecreasing
    - Jensen_defect_tail_is_globally_nonnegative
    - rational_shell_floors_for_Z_over_u53
    - recover_old_binomial_layers_7_through_12
    - recover_linear_tail_past_41_over_40
    - recover_Dw_times_Z_cross_layers_1_through_7
  exact_checker:
    path: artifacts/R13/20260919T1415Z_shell-binomial-5a7c_checker.py
    creation_commit: b869093fe84664df3bb150238c58fd2e4b006422
    result: R13_SHELL_BINOMIAL_RECOVERY_EXACT_PASS
  checker_output:
    path: artifacts/R13/20260919T1415Z_shell-binomial-5a7c.out
    creation_commit: d2ce51a9aa0fd48bc35268eda03ad9705619ae41
  outside_audits: "0/2"
  novelty: UNVERIFIED
  fixed_upper_stagnation_count: 0
  shared_root_edits: false
  peer_file_edits: false
  scheduler_changes: false
  remaining_obligation: "Find a qualitatively different route that moves the complete envelope or an explicit finite obstruction; do not spend the next run only adding more shell/binomial layers."
```
