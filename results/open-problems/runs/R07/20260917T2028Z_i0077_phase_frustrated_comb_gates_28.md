Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `27 -> 28` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The next source sentence is Problem 7.9 on forward Levy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 28: phase-frustrated alternating spatial-comb gates

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen equivalence convention that trivial Brownian rescaling/reflection and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T1925Z_i0077_sampled_spatial_comb_gates_27.md`,

creation commit `9572ce89ffe37ec5d9c156e185b6aa3c032ed103`. It moved the metric `26 -> 27` and used Section-B moves `#3,#11,#21`. The current triple is different.

All thirty Section-B moves have already appeared somewhere in the preceding I0077 chain, so the literal instruction to choose three moves never previously used on this problem is exhausted. I do not invent a false history. This run uses a new combination and a new mathematical application of `#2,#14,#19`.

Before new mathematics I re-read/recovered the required current state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/I0077.md`, the newest own R07 report and the I0077 chain, plus current neighboring/ownership evidence. The old R07 KPZ/FPP route remains preserved and retired rather than deleted. R15 has rotated away from its distinct Burdzy–Scheutzow Problem 7.2 predecessor; current C29 explicitly excludes I0077 because R07 owns it. `INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8; `POSTED.md` has no 7.8 exclusion. The canonical claim still says `PENDING_ADMISSION, not READY`; I preserve that shared status while following the owner’s explicit R07 assignment.

The `probability_1000_intake_*/problems.jsonl` mirrors are too large for literal row-by-row connector rendering. As in prior R07 admission reports, the intake reread is therefore honestly **targeted/partial due connector truncation**: the exact I0077 source row/wording, ownership, exclusions, queue entry, previous attempts and duplicate-source evidence were recovered; I do not claim a byte-for-byte reread of every unrelated intake row.

Entering metric: **27**.

## 2. Primary-source benchmark rechecked

Definitions 2.1–2.2 of the source normalize the process at `X_0=0`: an FBM admits random witness times `S_j -> -infinity` such that, for each fixed witness index,

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. A decomposable FBM is obtained by concatenating Brownian pieces.

Section 4 uses the principal Dirichlet exponent `lambda_0(c_1,c_2)` of the killed Ornstein–Uhlenbeck generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Theorem 4.3 has three clauses:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, a decomposable FBM exists with the corresponding normalized liminf/limsup confinement;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, a decomposable FBM exists which stays pointwise in the static parabolic strip for every negative time.

Remark 4.2 gives the exact critical identity

\[
\lambda_0(-1,1)=1,
\]

and Remark 4.1 gives strict domain monotonicity. These are the source-side existence facts used below.

## 3. Fresh current-literature/status pass

Fresh bounded searches dated 2026-09-17 included the exact Problem 7.8 wording, the original paper and later-author/citing variants, `Ornstein Uhlenbeck discrete sampling periodic target set persistence shifted lattice`, `Gaussian AR(1) persistence periodic sets shifted lattice target`, and discrete/alternating Gaussian persistence.

Nearest methodological prior art includes:

- S. N. Majumdar, A. J. Bray and G. C. M. A. Ehrhardt, *Persistence of a Continuous Stochastic Process with Discrete-Time Sampling*, Phys. Rev. E 64 (2001), 015101(R): discrete sampling of Gaussian Markov processes and alternating persistence;
- G. C. M. A. Ehrhardt, A. J. Bray and S. N. Majumdar, *Persistence of a Continuous Stochastic Process with Discrete-Time Sampling: Non-Markov Processes*, Phys. Rev. E 65 (2002), 041102;
- F. Aurzada and M. Kettner, *Persistence Exponents via Perturbation Theory: AR(1)-Processes*, J. Stat. Phys. 177 (2019), 651–665.

The sampled-Gaussian/AR(1) machinery is classical and is not claimed as new. I did not find a later paper in this bounded search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the phase-frustrated moving-comb FBM theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

## 4. New family: alternating shifted spatial combs at geometric scales

For `0 < eta < 6`, define two disconnected normalized combs of period 12,

\[
D^-_\eta=\bigcup_{j\in\mathbb Z}[12j-2-\eta,12j-2+\eta],
\qquad
D^+_\eta=\bigcup_{j\in\mathbb Z}[12j+2-\eta,12j+2+\eta].
\tag{4.1}
\]

At geometric physical times

\[
u_k=4^k,
\tag{4.2}
\]

require the normalized path to hit alternating phases:

\[
\boxed{
\frac{X_{-4^k}}{2^k}\in
\begin{cases}
D^-_\eta,&k\text{ even},\\
D^+_\eta,&k\text{ odd}.
\end{cases}}
\tag{4.3}
\]

Between gate times the path is unconstrained. Hence the path may migrate among infinitely many teeth. Unlike run 27, however, the allowed periodic set itself changes phase every gate.

A Brownian rescaling by a power of 4 merely shifts gate parity; reflection exchanges `D^-` and `D^+`. Neither operation converts the period-two orbit of normalized target sets into the period-one static comb of run 27. The orbit size under one log-step (`2` here, `1` there) is a frozen structural invariant. This is therefore not a parameter change or trivial rescaling of the previous family.

## 5. The three method moves

### #2 ATTACK THE NEGATION FIRST

The first candidate belief was that the path could defeat a moving comb simply by jumping to another tooth at every geometric gate. I attacked that belief directly. It fails: for the arithmetic shifts `-2,+2` and OU contraction `1/2`, **every tooth center is sent into a gap of the opposite comb**, uniformly over the tooth index. Thus allowing arbitrary tooth migration does not remove the obstruction.

### #14 FIND THE GROUP ACTING

Quotient the tooth centers modulo the period `12`. Under the sampled-OU contraction `x -> x/2`, only the parity of the lattice index matters. The infinite migration problem collapses to two residue classes. This is the arithmetic core:

- from a `D^-` center `12j-2`, the contracted center is `6j-1`, which is always distance exactly `3` from the nearest `D^+` center;
- from a `D^+` center `12j+2`, the contracted center is `6j+1`, always distance exactly `3` from the nearest `D^-` center.

### #19 MAKE IT AN ALGORITHM

For rational sampled correlation `r=p/q`, periodic comb period `L`, and a finite phase word `(c_k)`, the separation quantity

\[
\Delta_k=\inf_{j,\ell\in\mathbb Z}
|r(jL+c_k)-(\ell L+c_{k+1})|
\tag{5.1}
\]

reduces to finitely many residue classes modulo `q`. Computing `Delta=min_k Delta_k`, enlarging the tooth width by the Brownian-terminal robustness margin, and checking one Gaussian tail inequality gives an exact obstruction certificate. The archived checker executes this procedure for the canonical two-phase example.

## 6. A general moving-target compiler

Let `P>0`, `u_k=e^{kP}`, `r=e^{-P/2}`, and `s=sqrt(1-r^2)`. Let `(A_k)` be deterministic Borel target sets and `(A_k^+)` deterministic enlarged target sets such that for some `delta>0`,

\[
A_k+[-\delta,\delta]\subset A_k^+
\qquad\text{for every }k.
\tag{6.1}
\]

Assume the sampled-OU one-step contraction

\[
q:=\sup_k\sup_{x\in A_k^+}
\Pr\{rx+sZ\in A_{k+1}^+\}<e^{-P},
\qquad Z\sim N(0,1).
\tag{6.2}
\]

Then for every FBM `X`,

\[
\boxed{
\Pr\left(\exists K:\ \frac{X_{-u_k}}{\sqrt{u_k}}\in A_k
\ \forall k\ge K\right)=0.
}
\tag{6.3}
\]

This is the moving-target analogue of the sampled persistence obstruction used in run 27.

### Proof of the compiler

Fix a deterministic `K`. It suffices to rule out the event with that `K`; the event with a random eventual index is a countable union over `K`.

Let `B` be standard Brownian motion. For a real terminal time `T` and a lag `u<=T`, define the reversed increment

\[
R_T(u)=B(T)-B(T-u).
\tag{6.4}
\]

For a fixed deterministic integer terminal `n`, `u -> R_n(u)` on `[0,n]` is standard Brownian motion. Consequently the geometric samples

\[
Y_k^{(n)}=\frac{R_n(u_k)}{\sqrt{u_k}}
\tag{6.5}
\]

obey the exact AR(1)/sampled-OU recursion

\[
Y_{k+1}^{(n)}=rY_k^{(n)}+sZ_{k+1}.
\tag{6.6}
\]

The reflected target sequence `-A_k^+` satisfies the same contraction constant `q` by Gaussian symmetry.

Now set

\[
R_n^{\rm min}=(\log(n+2))^4
\tag{6.7}
\]

and use only indices with

\[
R_n^{\rm min}\le u_k\le n/2.
\tag{6.8}
\]

Define the unit Brownian modulus on `[0,n+2]`,

\[
M_n=\sup\{|B(t)-B(s)|:0\le s,t\le n+2,\ |t-s|\le1\}.
\tag{6.9}
\]

A standard reflection-principle/union-bound estimate gives, for fixed `delta>0`,

\[
\sum_n
\Pr\left\{M_n>\frac{\delta}{2}\sqrt{R_n^{\rm min}}\right\}<\infty,
\tag{6.10}
\]

because the right tail is at most `C n exp(-c delta^2 (log n)^4)`.

If `T in [n,n+1]`, then for every lag in (6.8),

\[
|R_T(u)-R_n(u)|
\le |B(T)-B(n)|+|B(T-u)-B(n-u)|
\le2M_n.
\tag{6.11}
\]

Thus on the good-modulus event in (6.10), after division by `sqrt(u)>=sqrt(R_n^{min})`, a hit of `A_k` at terminal `T` implies a hit of the enlarged set `A_k^+` at integer terminal `n`.

Let

\[
\kappa=-\frac{\log q}{P}>1.
\tag{6.12}
\]

The number of geometric transitions in (6.8) is

\[
N_n=\frac{\log(n/R_n^{\rm min})}{P}+O(1).
\tag{6.13}
\]

By repeated conditioning in (6.6), the integer-terminal survival probability is at most `q^{N_n}`, hence

\[
\Pr\{\text{all enlarged gates in (6.8) hold at terminal }n\}
\le C\left(\frac{n}{R_n^{\rm min}}\right)^{-\kappa}.
\tag{6.14}
\]

Because `kappa>1`, the sum of (6.14) over `n` is finite even after the polylogarithmic factor from `R_n^{min}`. Combining (6.10)–(6.14) and Borel–Cantelli shows that a standard Brownian path has only finitely many real terminal times `T` satisfying all sufficiently large gate constraints. Equivalently,

\[
\Pr\{\exists\text{ such a good terminal }T\ge A\}\to0
\quad(A\to\infty).
\tag{6.15}
\]

Finally let `X` be an arbitrary FBM and let `S_j -> -infinity` be its witness times. Suppose the event in (6.3) has positive probability for the fixed deterministic `K`. For a fixed witness index `j`,

\[
W_j(t)=X_{S_j+t}-X_{S_j}
\tag{6.16}
\]

is standard Brownian motion. Put `T_j=-S_j`. Since `X_0=0`, for every gate lag `u_k<=T_j`,

\[
X_{-u_k}
=X_{S_j}+W_j(T_j-u_k)
=-\{W_j(T_j)-W_j(T_j-u_k)\}.
\tag{6.17}
\]

Thus on the eventual-gate event, `T_j` is a good real terminal for the standard Brownian path `W_j`, with reflected targets. There is no conditioning on `T_j`.

To make the dependence argument explicit, let the eventual-gate event have probability `p>0`. By (6.15), choose deterministic `A` so large that a standard Brownian path has a good terminal beyond `A` with probability `<p/4`. Since `T_j -> infinity` a.s. as the witness index tends to the far past, choose one **deterministic witness index** `j` with `Pr(T_j<A)<p/4`. Then

\[
p
\le \Pr\{\text{event and }T_j\ge A\}+\Pr\{T_j<A\}
<\frac p4+\frac p4,
\]

a contradiction. This proves (6.3). `square`

## 7. Arithmetic-frustration theorem for moving combs

Let the sampled correlation be `r=e^{-P/2}`. For a phase sequence `(c_k)` and comb period `L`, set

\[
D_k(\eta)=\bigcup_{j\in\mathbb Z}
[jL+c_k-\eta,jL+c_k+\eta].
\tag{7.1}
\]

Define the center-separation invariant

\[
\Delta=\inf_k\inf_{j,\ell\in\mathbb Z}
|r(jL+c_k)-(\ell L+c_{k+1})|.
\tag{7.2}
\]

Take `0<eta_0<eta_1<L/2` and assume

\[
d:=\Delta-(1+r)\eta_1>0.
\tag{7.3}
\]

If `x in D_k(eta_1)`, its OU conditional mean `rx` lies within `r eta_1` of a contracted tooth center. Every target tooth in `D_{k+1}(eta_1)` starts at least another `eta_1` away from its center, so the whole next target is at distance at least `d` from the conditional mean. Therefore

\[
\sup_{x\in D_k(\eta_1)}
\Pr\{rx+sZ\in D_{k+1}(\eta_1)\}
\le2\exp\left(-\frac{d^2}{2s^2}\right).
\tag{7.4}
\]

Hence, if

\[
\boxed{
2\exp\left(-\frac{[\Delta-(1+r)\eta_1]^2}{2(1-r^2)}\right)
<e^{-P},
}
\tag{7.5}
\]

the compiler proves universal impossibility of eventual confinement to the moving comb gates with half-width `eta_0`.

This theorem is constructive: for rational `r=p/q` and a finite periodic phase word, `Delta` is a finite residue-class computation.

## 8. Theorem I0077-R07-T29 — canonical alternating comb

Take

\[
P=\log4,\qquad r=\frac12,\qquad s^2=\frac34,
\tag{8.1}
\]

and alternate the shifts `c_even=-2`, `c_odd=+2` with `L=12`.

For a `D^-` center `12j-2`, the contracted center is `6j-1`. If `j` is even this is congruent to `-1` mod 12; if `j` is odd it is congruent to `5` mod 12. Both are distance exactly `3` from the nearest `D^+` center `2 mod 12`. The reverse transition gives residues `1,7 mod 12`, both distance exactly `3` from the nearest `D^-` center `-2 mod 12`. Therefore

\[
\boxed{\Delta=3.}
\tag{8.2}
\]

Use actual gate half-width

\[
\eta_0=\frac1{10}
\]

and relaxed half-width

\[
\eta_1=\frac15.
\]

Then

\[
d=3-\left(1+\frac12\right)\frac15
=\frac{27}{10},
\tag{8.3}
\]

and the Gaussian Chernoff exponent is exactly

\[
\frac{d^2}{2s^2}
=\frac{(27/10)^2}{3/2}
=\frac{243}{50}>4.
\tag{8.4}
\]

The elementary Taylor lower bound

\[
e^4>1+4+\frac{4^2}{2}+\frac{4^3}{6}
=\frac{71}{3}>16
\tag{8.5}
\]

gives

\[
2e^{-243/50}<2e^{-4}<\frac18.
\tag{8.6}
\]

Since

\[
\frac18=4^{-3/2}<4^{-1}=e^{-P},
\tag{8.7}
\]

the compiler applies with persistence exponent at least `3/2>1`. Therefore, for **every** FBM `X`,

\[
\boxed{
\Pr\left(
\exists K:\
\frac{X_{-4^k}}{2^k}\in
\begin{cases}
D^-_{1/10},&k\text{ even},\\
D^+_{1/10},&k\text{ odd}
\end{cases}
\quad\forall k\ge K
\right)=0.
}
\tag{T29-}
\]

The exact finite arithmetic in (8.2)–(8.7) was executed and archived as a self-check:

- source: `artifacts/R07/20260917T2028Z_phase_frustrated_comb_exact.py` @ `aada0199945869bdf80b92bae34d11c018cf00d0`;
- output: `artifacts/R07/20260917T2028Z_phase_frustrated_comb_exact.out` @ `18427ccbe3884109e7e3add6fd9f7e01c2caeb52`;
- final output line: `PASS`.

This is a self-check, not an independent audit.

## 9. Source-side positive regime in the same family

The moving family also has a genuine existence regime. If

\[
3<\eta<6,
\tag{9.1}
\]

then the central tooth of `D^-_eta` centered at `-2` and the central tooth of `D^+_eta` centered at `+2` have common intersection

\[
[2-\eta,\eta-2].
\tag{9.2}
\]

Its half-width is `a=eta-2>1`. By `lambda_0(-1,1)=1` and strict domain monotonicity,

\[
\lambda_0(-a,a)<1.
\tag{9.3}
\]

Source Theorem 4.3(iii) therefore yields a decomposable FBM with

\[
|X_t|\le a\sqrt{|t|}\qquad\forall t\le0.
\tag{9.4}
\]

Because `[-a,a]` lies in both alternating comb phases, that process satisfies **every** gate, not merely eventually.

For the exact example `eta=7/2`, the common interval is `[-3/2,3/2]`, while each comb is still disconnected because `eta=7/2<6`. Thus the same structural family contains both a thin universal-obstruction regime (`eta=1/10`) and a wide decomposable-existence regime (`eta=7/2`). The intermediate sharp threshold is deliberately left open; it is not needed for T29 as stated.

## 10. Honest continuous space-time thickening

To turn the discrete gate family into an honest positive-width space-time tube, work in logarithmic time `r=log u`. Around each gate center `k log4`, choose pairwise disjoint windows of half-width `epsilon_k>0`, with `sum epsilon_k<infinity`. At the center use the alternating comb `D_k(eta)`; as `|r-k log4|` increases to `epsilon_k`, enlarge every tooth linearly until its half-width reaches `6`, at which point the period-12 union equals all of `R`. Outside the windows impose no spatial restriction.

Any path confined to this thickened tube must satisfy the center gates, so the thin-regime impossibility follows from T29. In the wide regime, the common central strip (9.2) is contained in every enlarged cross-section, so the decomposable source construction remains confined. The total constrained logarithmic time can be made arbitrarily small. This thickening is part of the **same** metric family, not an additional count.

## 11. Why this is a new metric family rather than run-27 parameter drift

Run 27 used one fixed periodic normalized set `D_{L,eta}` at every geometric gate. Its target orbit under one gate step had cardinality one. Here the target orbit has cardinality two and the key obstruction is **arithmetic phase frustration**: OU contraction sends every tooth center into a gap of the next phase.

The path may change tooth at every gate in both families, so the difference is not a continuity artifact. Nor can Brownian scaling or reflection remove the alternating phase: scaling shifts parity and reflection swaps the two phases, leaving a period-two moving target. Therefore the frozen equivalence convention counts this as a genuinely distinct nonparabolic shape family.

Metric movement:

\[
\boxed{27\longrightarrow28.}
\]

Unchanged count resets to `0`.

## 12. What the result does and does not say

T29 is a complete theorem for a genuinely new shape family and gives both a universal-obstruction regime and a source-side decomposable-existence regime. It also refutes the proposed heuristic

> “an infinite comb with freely selectable teeth at sparse geometric times can always be followed by switching teeth.”

The arithmetic phase pattern can make every switch costly. This is **not** a refutation of Burdzy–Scheutzow Problem 7.8 itself, which is open-ended.

No claim is made that the `eta` threshold is sharp, that every phase word is classified, or that the sampled-Gaussian persistence method is new. Publication novelty remains UNVERIFIED.

## 13. Closure status and next mathematical route

Overall source status remains **PARTIAL**. T29 currently has `0/2` required independent OTHER-track audits. It therefore does not satisfy closure protocol and no paper package is created.

The strongest next route is to replace the crude one-step Chernoff bound by the spectral radius of the finite-phase transfer operator on the period-12 quotient. That could determine a substantially sharper critical tooth width for this moving-comb family and may expose a genuine phase transition governed jointly by spatial arithmetic and OU persistence.

## 14. Model / scheduler control status

The model request is still not enforceable from the exposed scheduler surface used by this fleet. The task interface exposes prompt/title, schedule/start-offset, enabled state and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6/maximum therefore remains prompt-only here.

The root fleet ledger now records that P26’s historical `You cannot modify this task` denial was authorization-context-specific: a later authorized context successfully updated P26. The legitimate workaround for any task that still returns that denial is the owning/authorized account or workspace context, or platform support exposing the needed controls—not a duplicate task, permission bypass, or repository-only edit. Enforcing GPT-6 maximum would require the product/backend to expose and persist model/reasoning fields and provide authenticated run telemetry. No scheduler mutation was attempted in this run.

## 15. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  allocation: CLOSABLE OUTSIDE
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  claim_id: I0077-R07-T29
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 27
  after: 28
  movement: +1
  unchanged_count: 0
  new_family: "phase-frustrated alternating spatial-comb gates"
  theorem_scope: "universal thin-comb obstruction plus wide-comb decomposable existence"
  canonical_thin_parameters: "P=log 4, L=12, shifts +/-2, eta0=1/10, relaxed eta1=1/5"
  exact_center_separation: 3
  exact_chernoff_exponent: "243/50"
  one_step_bound: "q < 1/8 = 4^(-3/2) < e^(-P)"
  canonical_wide_parameter: "eta=7/2; common central halfwidth=3/2"
  exact_self_check: PASS
  self_check_source_commit: aada0199945869bdf80b92bae34d11c018cf00d0
  self_check_output_commit: 18427ccbe3884109e7e3add6fd9f7e01c2caeb52
  independent_audits_for_T29: "0/2"
  source_status: PARTIAL
  publication_novelty: UNVERIFIED
  methods: [2, 14, 19]
  preceding_methods: [3, 11, 21]
  scheduler_change: NONE
```
