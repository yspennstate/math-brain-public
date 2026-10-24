Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT on fresh HARD OUTSIDE successor D0036: `C_power: 0 -> 1`; status PARTIAL, not source closure. Methods actually used: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R14 — Bradley Question 8: exact quantization of finite algebraic spectral zeros

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Rotation continuity and repository read

The previous R14 target H0017 has already consumed both permitted hard-task stuck recoveries and was terminally handed off in

`runs/R14/2026-09-18T02-59-30Z_h0017_terminal_handoff_rotation_gate_91c4.md`.

I do **not** reopen H0017, the older negative-margin spherical perceptron target, I0089, or BIS32. The original perceptron handoff still preserves the last supported bracket

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

Before claiming a successor I reread/recovered the current campaign surfaces required by the owner protocol:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and current task-health admission deltas;
- the newest R14 terminal handoff;
- neighboring current screens, especially R15 on D0036 and R08 on the adjacent Bradley D0037 Gaussian/rho-star question;
- the D-intake row for D0036 and nearby Bradley/Virag candidates;
- current canonical ownership files.

The current CLOSABLE reserve remains exhausted on the screened front, but R14 is a HARD OUTSIDE lane. D0036 is exactly the kind of theorem-scale unassigned target the rotation rule permits after a terminal hard handoff.

Immediately before the claim, direct fetch of `operations/claims/D0036.md` at current `master` returned `404 Not Found`. A bounded repository search found no competing canonical D0036 owner. I therefore created the canonical exclusive claim

`operations/claims/D0036.md`

at commit `4e9f6cec5be238593e5cfe5f7ff5e5097a6da7e8`.

No shared root ledger, peer track file, scheduler, email, Drive, or public surface was modified.

## 1. New source and frozen metric

Outside source: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys **2** (2005), Section 6.5, Question 8, journal p. 132.

For a centered complex weakly stationary sequence `X=(X_k)`, Bradley defines

\[
r^*(n)=\sup_{\substack{Q,S\subset\mathbb Z\text{ finite, nonempty, disjoint}\\
\operatorname{dist}(Q,S)\ge n}}
\sup_{a,b}
\frac{|\operatorname{Cov}(\sum_{q\in Q}a_qX_q,\sum_{s\in S}b_sX_s)|}
{\|\sum_{q\in Q}a_qX_q\|_2\,\|\sum_{s\in S}b_sX_s\|_2}.
\]

Question 8 asks for a necessary-and-sufficient condition on the spectral density `f` for

\[
r^*(n)\longrightarrow0.
\]

The primary source was reopened in this run. The immediately relevant source facts are:

1. `r^*(n)->0` implies ordinary `r(n)->0` (Bradley (6.8) and the comments following it).
2. Helson--Sarason, Bradley Theorem 6.2: `r(n)->0` iff, a.e. on the circle,
   \[
   f=|p|^2\exp(u+\widetilde v),
   \tag{HS}
   \]
   where `p` is a polynomial and `u,v` are continuous real functions.
3. Bradley Theorem 6.5 completely handles the strictly positive continuous case.
4. R15/R08 independently proved the elementary finite-filter implication: if `Y` is `r^*`-mixing and `X=P(L)Y` for a finite Laurent polynomial of span `d`, then
   \[
   r_X^*(n)\le r_Y^*(n-d),\qquad n>d.
   \tag{FF}
   \]
   Thus `f=|P|^2g` with `g` positive continuous is sufficient, including arbitrary finite polynomial zero sets.

Fresh bounded searches on 2026-09-18 for Bradley Question 8, `r*(n)`, interlaced linear dependence, spectral zeros, Helson--Sarason, complete regularity, and later Bradley/Dominguez material found no source-matching full characterization and no exact priority match for the theorem below. This is bounded negative evidence only. The mechanism is close enough to classical Helson--Sarason/VMO theory that **priority is UNVERIFIED and the result may be folklore**; I make no novelty claim.

The frozen first R14 metric on D0036 is

`C_power in {0,1}`,

where `C_power=1` only after proving an exact necessary-and-sufficient criterion for the entire family

\[
f(e^{it})=g(e^{it})\prod_{j=1}^J|e^{it}-\zeta_j|^{\alpha_j},
\tag{P}
\]

with finite `J`, distinct `\zeta_j` on the unit circle, arbitrary `\alpha_j>0`, and continuous strictly positive `g`.

Before this run: `C_power=0`.  
After this run: **`C_power=1`**.

This is a genuine source-relevant subclass classification but remains **PARTIAL** for Bradley Question 8.

## 2. #2 ATTACK THE NEGATION FIRST — fractional powers are the first counterexample candidate

The obvious attempt to refute the finite-polynomial-zero picture is the fractional-difference family

\[
f_a(e^{it})=|1-e^{it}|^{2a},\qquad a>0.
\tag{F}
\]

For positive integer `a=m`, `(F)` is the spectrum of the finite difference `(1-L)^m` of white noise, and in fact its covariance has finite range `m`, so

\[
r^*(n)=0\qquad(n>m).
\]

The serious test is noninteger `a`. The density is continuous, positive a.e., and has just one algebraic zero, so it is exactly the simplest place where a naive “all continuous zero-bearing spectra should be okay” conjecture could survive while the finite-filter mechanism fails.

The attack on the negation does **not** produce a counterexample to the polynomial-zero picture. Instead the Helson--Sarason representation quantizes the possible algebraic zero order: a noninteger fractional power cannot even satisfy ordinary `r(n)->0`, hence cannot satisfy `r^*(n)->0`.

That is the mechanism used below.

## 3. #18 SAY IT IN ANOTHER LANGUAGE — the local obstruction lives in VMO

I use one standard harmonic-analysis fact about the circular Hilbert transform `H`: it maps VMO to VMO; in particular, if `v` is continuous on the circle, its conjugate function `\widetilde v=Hv` represents a VMO class. This is classical Sarason theory; see D. Sarason, *Functions of vanishing mean oscillation*, Trans. AMS 207 (1975), and standard VMO references. Continuous functions themselves lie in VMO.

Hence the Helson--Sarason remainder in `(HS)`,

\[
w:=u+\widetilde v,
\]

belongs to VMO.

The entire local argument is then driven by the following elementary lemma.

### Lemma 3.1 — a VMO function cannot carry a nonzero logarithmic point singularity

Let `w` be locally integrable near `0`. Suppose

\[
w(x)=c\log|x|+r(x)
\tag{L}
\]

for a.e. sufficiently small nonzero `x`, where `r(x)->r_0` as `x->0` (essentially is enough). If `w` is VMO near `0`, then `c=0`.

#### Proof

On the one-sided interval `I_h=(0,h)`, the average of `\log x` is

\[
(\log x)_{I_h}=\log h-1.
\]

After `x=hs`, its mean oscillation is scale independent:

\[
\frac1h\int_0^h
\left|\log x-(\log h-1)\right|dx
=
\int_0^1|\log s+1|ds
=
\frac{2}{e}.
\tag{MO}
\]

Because `r(x)->r_0`, the mean oscillation of `r` over `I_h` tends to zero. Subtracting interval means in `(L)` and using the triangle inequality gives

\[
\operatorname{MO}_{I_h}(w)
\ge |c|\frac{2}{e}-\operatorname{MO}_{I_h}(r).
\]

If `c\ne0`, the right side has positive liminf as `h\downarrow0`, contradicting vanishing mean oscillation. Therefore `c=0`. QED.

This lemma is deliberately proved on the page; no finite checker is involved.

## 4. #25 COUNT THE SAME THING TWICE — algebraic zero orders are quantized

### Theorem 4.1 — local algebraic-zero quantization

Let `X` be a nondegenerate CCWS sequence with spectral density `f`. Assume

\[
r_X^*(n)\to0.
\]

Suppose at some `\zeta=e^{it_0}` there are `\alpha>0` and a positive finite constant `c` such that

\[
f(e^{i(t_0+x)})=c|x|^{\alpha}(1+o(1))
\quad\text{as }x\to0
\tag{A}
\]

through a.e. `x`. Then

\[
\boxed{\alpha\in 2\mathbb N.}
\tag{Q}
\]

In words: every genuine isolated algebraic zero of an `r^*`-mixing spectrum has **even integer order**.

#### Proof

Since `r(n)<=r^*(n)`, we have `r(n)->0`. Bradley Theorem 6.2 (Helson--Sarason) gives `(HS)`:

\[
f=|p|^2\exp(u+\widetilde v)
\]

a.e., for a polynomial `p` and continuous real `u,v`.

Let `m>=0` be the multiplicity of `p` at `\zeta`; if `p(\zeta)\ne0`, put `m=0`. Along the circle,

\[
|p(e^{i(t_0+x)})|^2
=c_p|x|^{2m}(1+o(1))
\]

for some `c_p>0`. Taking logarithms of this and `(A)` gives

\[
\log f(e^{i(t_0+x)})
=\alpha\log|x|+\log c+o(1),
\]

and

\[
2\log|p(e^{i(t_0+x)})|
=2m\log|x|+\log c_p+o(1).
\]

Subtracting according to `(HS)`,

\[
u(e^{i(t_0+x)})+\widetilde v(e^{i(t_0+x)})
=(\alpha-2m)\log|x|+C+o(1).
\tag{*}
\]

The left side belongs to VMO: `u` is continuous, and the conjugate/Hilbert transform of continuous `v` belongs to VMO. The remainder `C+o(1)` in `(*)` has vanishing local mean oscillation. Lemma 3.1 therefore forces

\[
\alpha-2m=0.
\]

Thus `\alpha=2m`; because `\alpha>0`, `m>=1`, proving `(Q)`. QED.

### Corollary 4.2 — exact finite power-zero classification

For the entire family `(P)`,

\[
\boxed{
 r^*(n)\to0
 \quad\Longleftrightarrow\quad
 \alpha_j\in 2\mathbb N\text{ for every }j.
}
\tag{C}
\]

#### Necessity

Fix `j`. All factors with index `k\ne j` and `g` are positive continuous at `\zeta_j`, so locally

\[
f(e^{i(t_j+x)})=c_j|x|^{\alpha_j}(1+o(1)),\qquad c_j>0.
\]

Theorem 4.1 gives `\alpha_j\in2\mathbb N`.

#### Sufficiency

Write `\alpha_j=2m_j` and define the finite polynomial

\[
P(z)=\prod_{j=1}^J(z-\zeta_j)^{m_j}.
\]

Then, up to an irrelevant positive constant absorbed into `g`,

\[
f=|P|^2g.
\]

Let `Y` be a CCWS sequence with spectral density `g`. Bradley Theorem 6.5 gives `r_Y^*(n)->0` because `g` is continuous and strictly positive. Let `X'=P(L)Y`. It has spectral density `f`. The finite-filter contraction `(FF)` gives `r_{X'}^*(n)->0`. Since `r^*` is determined entirely by the covariance form, any CCWS sequence with the same spectral density `f` has the same `r^*` coefficients. Hence the original `X` also satisfies `r_X^*(n)->0`. QED.

This proves `C_power=1`.

### Corollary 4.3 — fractional differencing family is completely decided

For

\[
f_a(e^{it})=|1-e^{it}|^{2a},\qquad a>0,
\]

one has

\[
\boxed{
r^*(n)\to0
\quad\Longleftrightarrow\quad
a\in\mathbb N.
}
\tag{FD}
\]

For noninteger `a`, the failure occurs already at the weaker ordinary condition `r(n)->0`; no interlaced-specific construction is needed. For integer `a=m`, the covariance is finite-range and in fact `r^*(n)=0` for every `n>m`.

This also explains why finite-dimensional numerical canonical-correlation experiments are dangerous here: a fixed truncation can look rapidly decorrelated while the infinite past/future supremum required by `r(n)` is controlled by a local logarithmic/VMO obstruction. No numerical value is promoted to a rigorous endpoint in this report.

## 5. What moved, and what did not

The result does **not** answer Bradley Question 8. It does something narrower but exact:

- it converts the R15/R08 finite-filter sufficient class into a **necessary-and-sufficient theorem** for every spectrum having finitely many isolated algebraic power-law zeros and otherwise a positive continuous factor;
- it rules out every non-even-integer local power cusp as soon as `r^*(n)->0` is assumed;
- it shows that the next genuinely unresolved zero geometry is not “fractional power versus integer power.” It must be **subpower/non-algebraic** behavior compatible with the VMO remainder in Helson--Sarason, or an infinite/accumulating zero set.

So the source-wide remaining obligation is now sharper. In the Helson--Sarason representation

\[
f=|p|^2\exp(u+\widetilde v),\qquad u,v\in C(\mathbb T),
\]

Question 8 reduces to identifying exactly which VMO-type remainder factors preserve the much stronger *interlaced* angle decay after the finite polynomial zeros are removed. The positive-continuous remainder is solved by Bradley Theorem 6.5; power-law singular remainders are excluded by Theorem 4.1. The hard residual consists of conjugate-continuous factors whose singularities are milder/non-power or occur on more complicated zero sets.

## 6. Prior-art / current-status honesty

Searches in this run included:

- exact Bradley Question 8 language and `r*(n)` / interlaced linear dependence;
- Helson--Sarason spectral-density zeros and complete regularity;
- later Bradley and Dominguez work on generalized maximal correlation / matricial Helson--Sarason;
- fractional-difference / FARIMA canonical-correlation and mixing searches;
- standard VMO/Hilbert-transform references.

I found Bradley's source, Helson--Sarason follow-on literature, Dominguez's extensions, and time-series canonical-correlation work, but not an exact published statement of `(Q)`/`(C)` in the bounded search. This does **not** certify novelty. The proof is a short corollary of deep classical ingredients plus an elementary local VMO calculation, so the responsible label is:

**priority: UNVERIFIED; likely classical/folklore-adjacent until a dedicated literature audit says otherwise.**

The source question itself remains open-looking under this bounded current search.

No closure audit is requested yet because D0036 remains PARTIAL and the source-wide metric has not closed.

## 7. Next route

The preceding terminal H0017 triple was `22,26,27`; this run used `2,18,25`. The next D0036 run should not repeat `2,18,25`.

The mathematically changed obligation suggests **#3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #30 ONE SCALE AT A TIME**:

1. **#3:** strengthen Theorem 4.1 from exact regular variation `c|x|^alpha(1+o(1))` to a local index theorem for any zero with a well-defined logarithmic order
   \[
   \lim_{x\to0}\frac{\log f(t_0+x)}{\log|x|};
   \]
2. **#12:** identify an interlaced-angle invariant under removal of the finite polynomial factor, so the remaining question is stated directly for the VMO outer factor rather than for arbitrary `f`;
3. **#30:** study one non-power VMO zero profile at a time, starting with logarithmic corrections such as
   \[
   |1-e^{it}|^{2m}(\log(e/|t|))^{-\beta},
   \]
   and determine whether ordinary `r` already excludes it or whether the obstruction is genuinely interlaced.

A route that only accumulates more polynomial-zero examples is not enough; the point of the next run is to cross into the subpower residual.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  previous_target:
    id: H0017
    status: TERMINAL_HANDOFF
    reopened: false
    old_metric: "L_cone = pi/4"
    hard_recoveries_consumed: 2
  older_handoffs:
    negative_margin_spherical_perceptron:
      reopened: false
      last_bracket: "6.30297437506 <= alpha_c(-1) <= 12.78437096216"
      width: "6.48139658710"
    I0089: {reopened: false}
    BIS32: {reopened: false}
  active_target:
    id: D0036
    source: "Richard C. Bradley (2005), Probability Surveys 2, Question 8"
    target: "necessary-and-sufficient spectral criterion for r*(n)->0 for CCWS sequences"
    claim_path: "operations/claims/D0036.md"
    claim_commit: "4e9f6cec5be238593e5cfe5f7ff5e5097a6da7e8"
    status: PARTIAL
    source_current_status: "OPEN_CURRENT_BOUNDED / full later resolution not found"
    ownership: "R14 EXCLUSIVE"
  metric:
    name: C_power
    meaning: "complete iff classification for all finite algebraic-power zero spectra f=g prod |z-zeta_j|^{alpha_j}, g positive continuous"
    before: 0
    after: 1
    movement: true
    source_closure: false
  theorem:
    statement: "For the finite algebraic-power family, r*(n)->0 iff every alpha_j is an even positive integer. More locally, any isolated algebraic zero of an r*-mixing spectrum has even integer order."
    proof_dependencies:
      - "Bradley Theorem 6.2 / Helson-Sarason"
      - "circular Hilbert transform maps continuous functions into VMO"
      - "elementary scale-invariant mean oscillation of log|x| = 2/e"
      - "finite-filter contraction plus Bradley Theorem 6.5 for sufficiency"
    priority: UNVERIFIED_FOLKLORE_ADJACENT
  methods_used: [2, 18, 25]
  next_methods: [3, 12, 30]
  remaining_obligation: "classify subpower/non-algebraic VMO zero factors and infinite/accumulating zero sets; isolate the genuinely interlaced condition after finite polynomial factors are removed"
  finite_claims_requiring_checker: 0
  checker: none
  artifacts_created: []
  audit_ids: []
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 9. Model / scheduler-control truth

The exposed task-management surface still provides prompt/title/scheduling/timing/enablement controls but no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated completed-run model telemetry. Therefore GPT-6/maximum remains prompt text only here. I cannot truthfully claim it actually ran.

The historical P26 `You cannot modify this task` failure remains an authorization-context boundary. The legitimate workaround is the authorized owning context, ownership/admin transfer, or platform support—not task duplication, permission bypass, or GitHub edits.
