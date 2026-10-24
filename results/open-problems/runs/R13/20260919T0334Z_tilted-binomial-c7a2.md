Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 45541/6250 = 7.28656 -> 728151/100000 = 7.28151`, exact decrease `101/20000 = 0.00505`. Methods actually used: **#18 SAY IT IN ANOTHER LANGUAGE, #3 PROVE SOMETHING STRONGER, #25 COUNT THE SAME THING TWICE.**

Run ID: `20260919T0334Z_tilted-binomial-c7a2`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Worker: R13 HARD OUTSIDE.

## 1. Continuity, ownership, source status, and fixed metric

I continued from the newest complete R13 report

`runs/R13/20260919T0236Z_p53-frobenius-6c2f.md`.

Before new research I reread/reconciled `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report and its checker, the current R12/R16 neighboring-directory state, and the relevant intake reconciliation. The canonical intake alias is `I0091` in `probability_1000_intake_I_20260914/problems.jsonl`; the later intake reconciliation records the qualitative Boolean Komlos source as resolved/excluded while preserving R13's already-owned quantitative finite-dimensional track. `QUEUE.md` likewise treats Boolean Komlos/R13 as assigned, not as an unassigned reserve item. No ownership collision was found. I did not edit shared roots or peer-track files.

The qualitative source status remains **KNOWN in the September 2026 preprint literature**, not OPEN: Guo--Fang--Lu, arXiv:2609.11189v1 (10 September 2026), prove the genuine real-Boolean dimension-free bound `3 sqrt(2 pi)`; Karingula--Lovett, ECCC TR26-188 (17 September 2026), independently prove constant `36`; Akbas--Sra, arXiv:2609.20785v1 (17 September 2026), recover Komlos from Boolean small-ball inequalities. Bansal--Jiang, arXiv:2508.03961v2, remains the earlier `~O(log^(1/4)n)` real-Boolean comparison source, with their August 2026 exposition giving the explicit logarithmic form. R13 therefore makes **no claim to solve the qualitative conjecture**. The owner-fixed quantity is the complete rigorously certified finite-dimensional pointwise envelope

\[
K_n^*:=\sup_{m\ge1}\sup_{\substack{A\in\mathbb R^{m\times n}\\\|A_{\cdot j}\|_2\le1}}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty.
\]

This run proves

\[
\boxed{K_{86}^*\le\frac{728151}{100000}=7.28151}.\tag{1.1}
\]

The exact predecessor value was `45541/6250=7.28656`, so

\[
\frac{45541}{6250}-\frac{728151}{100000}
=\boxed{\frac{101}{20000}}=0.00505.\tag{1.2}
\]

The fixed-metric stagnation count is therefore `0`.

## 2. Retained real-Boolean DTV reduction

For `p>1`, dimension `D`, and cube half-side `C`, consider

\[
\rho_{C,p}(x)\propto\prod_{i=1}^D
\cos^p\!\left(\frac{\pi x_i}{2C}\right)\mathbf 1_{(-C,C)^D}(x).
\]

If `X` has this product density and

\[
T_i=\tan\!\left(\frac{\pi X_i}{2C}\right),
\]

then the one-dimensional change of variables gives

\[
T_i\stackrel d=\frac{G_i}{\sqrt{S_i}},\qquad
G_i\sim N(0,1),\quad S_i\sim\chi^2_{p+1},
\]

independently. Since

\[
\partial_i\log\rho_{C,p}(x)
=-\frac{p\pi}{2C}\tan\!\left(\frac{\pi x_i}{2C}\right),
\]

conditioning on the `S_i` gives

\[
V_u(\rho_{C,p})
=\frac{p\sqrt{\pi/2}}{C}
\mathbb E\sqrt{\sum_{i=1}^D\frac{u_i^2}{S_i}}.
\]

Put

\[
Y_i:=\frac{p-1}{S_i},\qquad X_D:=\frac1D\sum_{i=1}^DY_i.
\]

Then `EY_i=1`. For `w_i=u_i^2/\|u\|_2^2`, the map

\[
w\mapsto\mathbb E\sqrt{\sum_iw_iY_i}
\]

is symmetric and concave on the simplex, hence is maximized at the uniform vector. Therefore

\[
V_u(\rho_{C,p})
\le\frac{p\sqrt{\pi/2}}{C\sqrt{p-1}}
\mathbb E\sqrt{X_D}\,\|u\|_2.
\]

Guo--Fang--Lu's finite-step directional-total-variation signing theorem applies once this coefficient is at most `1/3`. Consequently every finite family of real vectors in `R^D` with Euclidean norm at most one admits actual signs in `{-1,+1}` with coordinate discrepancy strictly below

\[
C_{p,D}:=
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}\mathbb E\sqrt{X_D}.
\tag{2.1}
\]

No complex phases, rank-two coloring, or average-case relaxation appears here.

For the retained exactly-solvable exponent

\[
p=\frac53,
\]

we have

\[
Y\sim\operatorname{InvGamma}\!\left(\frac43,\frac13\right),
\qquad
C_{5/3,D}=\frac52\sqrt{3\pi}\,\mathbb E\sqrt{X_D}.
\tag{2.2}
\]

## 3. Method #18: tilt the exact inverse-gamma transform

The predecessor worked directly with a lower bound on `log L`, where

\[
L(s):=\mathbb E e^{-sY}.
\]

This run changes language and studies the **mean-cancelled tilted transform**

\[
G(s):=e^sL(s).
\tag{3.1}
\]

Since `EY=1`, Jensen already suggests `G(s)>=1`; the point is to certify a quantitative positive polynomial excess and then exploit it before taking the `D`th power.

For `Y~InvGamma(4/3,1/3)`, the exact Frobenius decomposition is

\[
L(s)=
{}_0F_1\!\left(; -\frac13;\frac s3\right)
+c_*s^{4/3}{}_0F_1\!\left(;\frac73;\frac s3\right),
\tag{3.2}
\]

where

\[
c_*=\frac{27}{4}3^{-4/3}
\frac{\Gamma(2/3)}{\Gamma(1/3)}.
\tag{3.3}
\]

For

\[
P_N:=\prod_{k=0}^{N-1}\frac{3k+1}{3k+2},
\]

Gautschi's gamma-ratio inequality yields

\[
c_*^3>\frac{243}{64}P_N^3\left(N-\frac13\right).
\]

Taking `N=20000`, the exact rational checker proves

\[
\boxed{c_*>\frac{788557}{10^6}=0.788557}.\tag{3.4}
\]

It also proves

\[
139^{-1/3}>\underline d:=\frac{193046411}{10^9}.
\tag{3.5}
\]

The analytic branch has the exact sign pattern

\[
{}_0F_1\!\left(; -\frac13;\frac s3\right)
=1-s-\frac{s^2}{4}-\frac{s^3}{60}-\frac{s^4}{1920}
-\frac{s^5}{105600}-\frac{s^6}{8870400}-\cdots.
\tag{3.6}
\]

Every nonconstant coefficient is negative. If

\[
D=139,\qquad U=\frac{33}{20},\qquad T=U^6,
\qquad 0\le s=\frac tD\le\frac TD,
\]

then after the sixth term the absolute consecutive-term ratio is at most `(T/D)/119`. Hence

\[
A(s):={}_0F_1\!\left(; -\frac13;\frac s3\right)
\ge 1-s-\frac{s^2}{4}-\frac{s^3}{60}-\frac{s^4}{1920}
-\frac{s^5}{105600}-\kappa_6s^6,
\tag{3.7}
\]

with

\[
\kappa_6:=\frac{1/8870400}{1-T/(119D)}.
\]

The nonanalytic factor has positive coefficients, so

\[
{}_0F_1\!\left(;\frac73;\frac s3\right)
\ge1+\frac s7+\frac{s^2}{140}+\frac{s^3}{5460}+\frac{s^4}{349440}.
\tag{3.8}
\]

Equations (3.4)--(3.8) give an explicit rational/fractional-power lower polynomial `L_lo(s)` for `L(s)`.

## 4. Method #3: prove the stronger pointwise tilted inequality

Set

\[
E_8(s):=\sum_{j=0}^8\frac{s^j}{j!}\le e^s.
\]

Since `L(s)>0`, `L(s)>=L_lo(s)`, and `E_8(s)>=0`,

\[
e^sL(s)\ge E_8(s)L(s)\ge E_8(s)L_{lo}(s).
\]

Now substitute

\[
t=u^6,\qquad 0\le u\le U=\frac{33}{20}.
\]

All powers become integral. Define the exact rational polynomial `Z(u)` by

\[
E_8(u^6/D)L_{lo}(u^6/D)=1+Z(u).
\tag{4.1}
\]

The first nonzero term is degree `8`. Dividing by `u^8`, discarding every positive nonleading monomial and placing every negative monomial at the endpoint `u=U` gives an exact lower certificate. The checker proves

\[
\boxed{
\frac{Z(u)}{u^8}\ge
0.0007717702815598251\ldots>0
\quad(0<u\le U).}
\tag{4.2}
\]

Thus the stronger pointwise statement

\[
\boxed{G(t/D)=e^{t/D}L(t/D)\ge1+Z(u)\ge1}
\tag{4.3}
\]

holds throughout the entire integration interval. This avoids the predecessor's lossy logarithm step.

## 5. Method #25: count positive binomial layers before integrating

Because `Z(u)>=0`, equation (4.3) implies

\[
G(t/D)^D-1
\ge
\sum_{k=1}^{10}\binom{D}{k}Z(u)^k
=:B_{10}(u),
\qquad D=139.
\tag{5.1}
\]

The identity

\[
L(t/D)^D-e^{-t}
=e^{-t}\left(G(t/D)^D-1\right)
\tag{5.2}
\]

therefore has ten explicitly positive combinatorial layers available before integration.

For the exponential factor use the degree-81 odd Taylor polynomial

\[
W_{81}(t):=\sum_{j=0}^{81}\frac{(-t)^j}{j!}.
\]

Taylor's theorem gives

\[
e^{-t}\ge W_{81}(t)\qquad(t\ge0).
\tag{5.3}
\]

If `W_81(t)>=0`, (5.1)--(5.3) give the product lower bound directly. If `W_81(t)<0`, the true left side of (5.2) is nonnegative (by Jensen, or by `G>=1`), while `W_81(t)B_10(u)<=0`; hence the same lower bound remains valid. Therefore on the whole interval

\[
L(t/D)^D-e^{-t}\ge W_{81}(t)B_{10}(u).
\tag{5.4}
\]

For a positive mean-one random variable,

\[
1-\mathbb E\sqrt X
=\frac1{2\sqrt\pi}\int_0^\infty
\left(\mathbb Ee^{-tX}-e^{-t}\right)t^{-3/2}\,dt.
\tag{5.5}
\]

For `X_D=D^{-1}\sum_iY_i`, independence gives `Ee^{-tX_D}=L(t/D)^D`. Restrict (5.5) to `[0,T]`, use (5.4), and substitute `t=u^6`; then `t^{-3/2}dt=6u^{-4}du`. Every quantity is now an ordinary polynomial with rational coefficients. The exact checker evaluates

\[
I:=\int_0^U6u^{-4}W_{81}(u^6)B_{10}(u)\,du
=0.1817267842251606\ldots>0.
\tag{5.6}
\]

Using the exact rational square-root certificates

\[
\pi<\frac{355}{113},\qquad
\sqrt\pi<\frac{1772454}{10^6},\qquad
\sqrt{3\pi}<\frac{3069981}{10^6},
\tag{5.7}
\]

we obtain

\[
1-\mathbb E\sqrt{X_{139}}
> I\frac{500000}{1772454}
=0.05126417504351611\ldots.
\tag{5.8}
\]

Hence, from (2.2),

\[
C_{5/3,139}
<\frac52\frac{3069981}{10^6}
\left(1-0.05126417504351611\ldots\right)
=7.281502391589329\ldots
<\boxed{\frac{728151}{100000}}.
\tag{5.9}
\]

The archived exact execution terminates

`R13_TILTED_BINOMIAL_EXACT_PASS`.

## 6. Row pruning and the moved source metric

Set

\[
h:=\frac{728151}{100000}=7.28151.
\]

For an arbitrary real `m x 86` matrix with every column of Euclidean norm at most one, call row `r_i` active if

\[
\|r_i\|_2>\frac h{\sqrt{86}}.
\tag{6.1}
\]

The Frobenius budget is

\[
\sum_i\|r_i\|_2^2\le86.
\]

If `d` rows are active, then

\[
d<\frac{86^2}{h^2}.
\]

The exact checker proves

\[
139<\frac{86^2}{h^2}
=139.49350986879372\ldots<140,
\tag{6.2}
\]

so `d<=139`. Pad the active-row submatrix by zero rows if necessary and apply (5.9); this gives one Boolean signing controlling all active rows by `<h`. For every inactive row,

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\sqrt{86}\le h
\]

by Cauchy--Schwarz. Therefore

\[
\boxed{K_{86}^*\le7.28151}.
\tag{6.3}
\]

## 7. Complete universal bound after this run

The same row-pruning proof works for every column count. Define the new all-`n` branch

\[
\boxed{
L_{TB}(n):=
\max\left\{\frac{728151}{100000},\frac n{\sqrt{140}}\right\},
\qquad n\in\mathbb N.}
\tag{7.1}
\]

Then `K_n^*<=L_TB(n)` for every integer `n>=1`: the pruning threshold `H=L_TB(n)` gives `d<n^2/H^2<=140`, hence `d<=139`, and (5.9) controls the active rows.

The predecessor branch was

\[
L_{5/3}(n)=
\max\left\{\frac{45541}{6250},\frac n{\sqrt{140}}\right\}.
\]

Thus `L_TB` strictly dominates `L_{5/3}` pointwise, with the **same dimension restriction/slope** and only the certified constant improved.

No historical branch is discarded. Let `B_prev(n)` be the exact complete pointwise envelope fixed in the immutable predecessor `runs/R13/20260919T0236Z_p53-frobenius-6c2f.md`. It contains the exact small-column values

\[
B_{prev}(1)=1,\qquad
B_{prev}(2)=\sqrt2,\qquad
B_{prev}(3)=\frac{\sqrt{11}+\sqrt2}{3},\qquad
B_{prev}(4)=\sqrt3,
\]

the elementary finite-`n` branch `sqrt(3n/4)`, the five-column block branch

\[
T_5\sqrt{\lceil n/5\rceil},\qquad
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\]

and the previously certified `G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_LT` branches with their exact constants, ceilings, infima and integer-dimension restrictions frozen in the predecessor chain. No logarithmic factor, parameter restriction, or finite-dimensional comparison is changed in this run.

Equivalently, the top-level complete envelope can be written

\[
B_{R13}^{new}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{LT}(n),L_{TB}(n)\},&5\le n\le85,\\
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{LT}(n),L_{TB}(n)\},&n\ge86.
\end{cases}
\tag{7.2}
\]

Here every named predecessor function means exactly its already-certified definition in the immutable predecessor envelope; (7.2) changes **only** the old `L_{5/3}` entry to the stronger explicit (7.1). In compact exact form,

\[
\boxed{B_{R13}^{new}(n)=\min\{B_{prev}(n),L_{TB}(n)\}.}
\tag{7.3}
\]

This is the complete retained universal bound, not an exponent-only report and not merely the `n=86` headline. Guo--Fang--Lu's dimension-free `3 sqrt(2 pi)` background control remains available wherever a growing finite-dimensional branch is worse.

The finite lower-obstruction history is unchanged:

\[
K_5^*=T_5,\qquad
K_6^*\ge1.84535465,\qquad
K_{11}^*\ge1.99488049,\qquad
K_{12}^*\ge2.013108.
\]

## 8. What the three section-B methods actually did

**#18 SAY IT IN ANOTHER LANGUAGE.** Replaced the predecessor's direct `log L` enclosure by the tilted transform `G(s)=e^sL(s)`, which exactly cancels the mean-one linear behavior. Outcome: success; the transform exposes a positive excess polynomial before taking the 139th power.

**#3 PROVE SOMETHING STRONGER.** Instead of proving only an integrated/logarithmic lower bound, proved the pointwise interval statement `G(t/139)>=1+Z(u)` with a strictly positive exact coefficient margin for every `0<u<=33/20`. Outcome: success; this removes the log-remainder loss.

**#25 COUNT THE SAME THING TWICE.** Expanded the positive excess through ten exact binomial layers before integration rather than collapsing it to `exp(R)-1>=R+R^2/2`. Outcome: success; the exact Jensen-defect lower bound rises enough to move the owner-fixed metric by `0.00505`.

The immediately preceding triple was `#5/#6/#16`, so this run does not repeat it.

## 9. Exact self-check and audit status

Exact checker source:

`artifacts/R13/20260919T0334Z_tilted-binomial-c7a2_checker.py`

creation commit:

`7b5878933fe62a1e91fe875929262801d079cb73`

The file was read back at that exact commit.

Executed output:

`artifacts/R13/20260919T0334Z_tilted-binomial-c7a2_checker.out`

creation commit:

`481265cd7ee88f9e8580d0d39b12328e41031daa`

The output was read back at that exact commit and terminates `R13_TILTED_BINOMIAL_EXACT_PASS`.

The self-check verifies in exact `Fraction` arithmetic: the `N=20000` Gautschi coefficient certificate; the `139^(-1/3)` rational lower bound; the analytic hypergeometric tail bound; the positive nonanalytic truncation; the full pointwise `Z>=0` margin; ten positive binomial layers; the degree-81 global Taylor lower bound after exact polynomial integration; the rational square-root bounds; `C_{5/3,139}<728151/100000`; `139<86^2/h^2<140`; and the exact movement `101/20000`.

This is a **self-check**, not an independent audit. The new tilted/binomial sharpening has `0/2` required OTHER-track audits. The old R12/P26 checks of earlier Komlos/GFL statements do not count as audits of this new finite-dimensional calculation.

## 10. Prior-art/current-source search and novelty label

Fresh checks dated 19 September 2026 included the exact current sources and later independent papers:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026: real-Boolean bound `3 sqrt(2 pi)` and the DTV framework;
- Bansal--Jiang, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlos Bounds Beyond Banaszczyk*, arXiv:2508.03961v2: earlier `~O(log^(1/4)n)` real-Boolean result; their 28 August 2026 exposition gives `O((log n)^(1/4)(log log n)^(7/4))`;
- Karingula--Lovett, ECCC TR26-188, 17 September 2026: elementary real-Boolean constant `36`;
- Akbas--Sra, arXiv:2609.20785v1, 17 September 2026: Boolean small-ball inequalities recovering Komlos;
- Guillen--Kobzar, arXiv:2609.15071v1, 14 September 2026: complex phases/rank-two vector discrepancy only, not a substitute for Boolean signs.

I also ran bounded topic searches for `cosine-power Komlos directional total variation`, `inverse-gamma Komlos discrepancy`, and `Frobenius Komlos discrepancy inverse gamma`. No matching finite-dimensional tilted-transform/binomial sharpening was found. A negative bounded search is not a priority theorem. **NOVELTY remains UNVERIFIED.**

## 11. Model/control truth and denied-task history

The scheduler/control limitation remains unchanged. The exposed automation schema has title, prompt, schedule, enablement and timing controls, but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run effort telemetry. Thus the prompt text `GPT-6 / maximum` does not prove that runtime. This report truthfully identifies the actual model as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

Repository policy records the historical `You cannot modify this task` failure (including the earlier P26 context) as an authorization/context boundary; `RESULTS.md` separately records that P26 was later updated from an authorized P/C context. The legitimate remedy for any still-denied task is therefore the owning/authorized product/workspace/API/admin surface or platform support, not duplication or permission bypass. Consistent with the owner instruction, this run made **no scheduler, permission, workflow, email, Drive, purchase, or public-posting change**.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric:
    name: complete_rigorously_certified_pointwise_upper_envelope_B_R13_n
    predecessor_report: runs/R13/20260919T0236Z_p53-frobenius-6c2f.md
    after_definition: "B_new(n)=min(B_prev(n), L_TB(n))"
    new_branch: "L_TB(n)=max(728151/100000, n/sqrt(140)) for every integer n>=1"
    pointwise_dominates_predecessor_branch: "L_p53(n)=max(45541/6250,n/sqrt(140))"
    headline_n: 86
    before_at_headline: "45541/6250"
    after_at_headline: "728151/100000"
    exact_improvement: "101/20000"
    moved: true
  theorem_new:
    p: "5/3"
    finite_dimension: 139
    transform: "G(s)=exp(s)L(s)"
    binomial_levels_certified: 10
    exp_lower_taylor_degree: 81
    certified_cube_half_side: "<728151/100000"
    real_boolean_signs: true
    all_n_row_pruning_branch_proved: true
  methods_this_run: [18, 3, 25]
  predecessor_methods: [5, 6, 16]
  checker:
    path: artifacts/R13/20260919T0334Z_tilted-binomial-c7a2_checker.py
    creation_commit: 7b5878933fe62a1e91fe875929262801d079cb73
    status: SELF_CHECK_PASS
  output:
    path: artifacts/R13/20260919T0334Z_tilted-binomial-c7a2_checker.out
    creation_commit: 481265cd7ee88f9e8580d0d39b12328e41031daa
    terminal_marker: R13_TILTED_BINOMIAL_EXACT_PASS
  outside_audits_new_sharpening: "0/2"
  novelty: UNVERIFIED
  stagnation_count_after: 0
  next_research_routes:
    - change the product-density family rather than further scalar retuning of p
    - derive a nonproduct symmetric DTV density with l2 rather than l1 directional control
    - couple exact small-column/block discrepancy information into the active-row reduction
  scheduler_or_permission_changes: none
```

Status: **SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED METRIC MOVED / full written proof / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED / stagnation count 0**.
