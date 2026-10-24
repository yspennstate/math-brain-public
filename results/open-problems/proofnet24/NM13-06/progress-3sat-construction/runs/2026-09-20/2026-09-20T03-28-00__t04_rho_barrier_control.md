Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 constructive random 3-SAT: exact branching-ratio drift and a barrier control law

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Current assignment: **T04 — classical iid random 3-SAT, constructive lower-bound route**  
Status: **OPEN / PARTIAL**

## 0. Source-level metric before / after

The exact source model remains: `m=floor(alpha n)` clauses, each clause choosing three distinct variables uniformly and then independent uniform signs.

The strongest unconditional explicit numerical bracket that I can support after a bounded fresh check is still

\[
\boxed{3.52\le \alpha_{3\text{-SAT}}\le 4.4898.}
\]

Thus

\[
[3.52,4.4898]\longrightarrow[3.52,4.4898],
\qquad
U-L=0.9698\longrightarrow0.9698.
\]

**No source-level threshold movement this run.**

The lower endpoint is Hajiaghayi--Sorkin, arXiv:math/0310193.  The unconditional explicit upper endpoint is Diaz--Kirousis--Mitsche--Perez-Gimenez, arXiv:0807.3600.  I specifically rechecked the occasionally quoted value `4.453`: Maneva--Sinclair (arXiv:0710.0805) rigorously rule out non-trivial core assignments above 4.453, but this is not by itself an unconditional unsatisfiability bound.  Diaz et al. explicitly note that promoting 4.453 to a satisfiability-threshold upper bound requires an additional solution-geometry conjecture which was not proved for `k=3`.  A 2026 random-k-SAT status check likewise does not close fixed `k=3`.

So the demonstrated gain below is a **mechanism gain**, not a numerical threshold gain.

## 1. Compact handoff and the obstruction found in the previous run

The preceding T04 report derived, for four-parameter degree classes

\[
q=(a,b,c,d)
\]

with

- `a` = positive 2-clause degree,
- `b` = negative 2-clause degree,
- `c` = positive 3-clause degree,
- `d` = negative 3-clause degree,

an exact first-order clause-risk polarity index for a linear potential

\[
V_\eta=m_2+\eta m_3.
\]

That report obtained

\[
D_T(V_\eta)-D_F(V_\eta)
=(d-c)+(b-a)\frac{g_\eta}{1-\rho}.
\tag{1.1}
\]

It also established `g_eta<=0` for every `eta>=1`, hence a `V_eta`-greedy rule actively values a subcritical unit cascade as a cleanup mechanism.

Two things were still missing:

1. **soundness detail:** the previous proof text informally normalized a positive unit by `2m2`; for an asymmetric state the correct sign-conditional denominators are the positive and negative 2-stub masses separately;
2. **control obstruction:** minimizing clause count alone can reward a very large unit avalanche even when that avalanche pushes the unit-propagation branching factor toward one.  A threshold proof needs an explicit control on that criticality, not only on `m2,m3`.

This run fixes (1) without losing the previous scalar formulas and resolves (2) at first-order fluid level by deriving the exact drift of the branching factor itself.

Historical failed routes remain preserved rather than restarted: the older small-fixed-k line had one-variable cavity iteration, fractional solution-count martingales, randomized boosters, generic helper replacement, mesoscopic-to-local Fourier transfer, loose-hypertree cavity, ranked-spreadness black boxes, and positive-temperature/free-energy compactification.  The present route stays constructive and degree-spectrum based.

## 2. State notation

Let `x_{a,b,c,d}` be the density, per original variable, of currently unset variables in class `(a,b,c,d)`.  Define signed stub masses

\[
A=\sum a x_{a,b,c,d},\qquad B=\sum b x_{a,b,c,d},
\]

\[
C=\sum c x_{a,b,c,d},\qquad D=\sum d x_{a,b,c,d}.
\]

Then

\[
A+B=2m_2,\qquad C+D=3m_3.
\tag{2.1}
\]

Also define the mixed 2-degree moment

\[
S:=\sum ab\,x_{a,b,c,d}.
\tag{2.2}
\]

The unit-cascade branching factor will be

\[
\rho=\frac{S}{m_2}.
\tag{2.3}
\]

All calculations below are in the same conditional-uniform configuration-model / differential-equation regime used by Hajiaghayi--Sorkin: conditional on the degree state, partner stubs are asymptotically uniform; collisions create only the standard `o(1)` fluid error while the tracked degrees are bounded and `rho<1-epsilon`.

## 3. Theorem 1 — the correct two-type unit cascade, and why the old scalar rho survives

A unit literal has a sign.  Let the two types be `+` and `-`.

A positive unit is attached, before consuming its source 2-stub, to class `q=(a,b,c,d)` with conditional probability

\[
\frac{a x_q}{A},
\tag{3.1}
\]

not `a x_q/(2m2)` unless `A=m2`.  Likewise a negative unit has class distribution

\[
\frac{b x_q}{B}.
\tag{3.2}
\]

If a positive unit sets its variable TRUE, it creates `b` child unit clauses; if a negative unit sets its variable FALSE, it creates `a` child unit clauses.  Each newly exposed partner literal has sign `+` with probability `A/(A+B)` and sign `-` with probability `B/(A+B)`.

Therefore, for `A,B>0`, the mean offspring matrix is

\[
M=
\begin{pmatrix}
S/(A+B) & SB/[A(A+B)]\\
SA/[B(A+B)] & S/(A+B)
\end{pmatrix}.
\tag{3.3}
\]

Its determinant is zero and its nonzero eigenvalue is

\[
\rho(M)=\frac{2S}{A+B}=\frac{S}{m_2}.
\tag{3.4}
\]

Thus the scalar branching factor used in the previous report is correct even without sign symmetry.  What needed correction was only the intermediate sign-conditional normalization.

### Proof

For a `+` parent, the expected number of children is

\[
\sum_q \frac{a x_q}{A}b=\frac{S}{A}.
\]

Splitting those children by partner sign gives the first row of (3.3); the negative-parent calculation is identical with `A,B` exchanged.  The determinant vanishes because the off-diagonal product equals the diagonal product.  The trace is `2S/(A+B)`, hence (3.4).  If `A=0` or `B=0`, then `S=0` and the process is trivially non-branching, so (3.4) holds by the obvious boundary interpretation.  QED.

There is an additional useful cancellation.  The sign distribution of **seed** units produced by any falsified 2-clause is

\[
p=\left(\frac{A}{A+B},\frac{B}{A+B}\right).
\tag{3.5}
\]

A direct multiplication gives

\[
pM=\rho p.
\tag{3.6}
\]

Therefore `b` seeds from a free TRUE assignment produce expected total forced sign-count vector

\[
\frac{b}{1-\rho}p,
\tag{3.7}
\]

and `a` seeds from a free FALSE assignment produce `a p/(1-rho)`.  This proves, with the correct two-type argument, that the previous scalar factors `b/(1-rho)` and `a/(1-rho)` were in fact right.

## 4. Clause-count drift, restated with the corrected proof

For a positive forced assignment, after its source positive 2-stub has already become a unit, the remaining clause drifts are

\[
f_2^+(q)=d-(a+b-1),\qquad f_3^+(q)=-(c+d).
\tag{4.1}
\]

For a negative forced assignment,

\[
f_2^-(q)=c-(a+b-1),\qquad f_3^-(q)=-(c+d).
\tag{4.2}
\]

Averaging over the stationary seed-sign mixture (3.5) gives

\[
g_2=\frac1{2m_2}\sum_q x_q
\left[a\{d-(a+b-1)\}+b\{c-(a+b-1)\}\right],
\tag{4.3}
\]

\[
g_3=-\frac1{2m_2}\sum_q x_q(a+b)(c+d).
\tag{4.4}
\]

For a freely chosen class `q=(a,b,c,d)`, including its complete expected subcritical avalanche,

\[
G_{2,T}=d-(a+b)+\frac{b g_2}{1-\rho},
\qquad
G_{3,T}=-(c+d)+\frac{b g_3}{1-\rho},
\tag{4.5}
\]

\[
G_{2,F}=c-(a+b)+\frac{a g_2}{1-\rho},
\qquad
G_{3,F}=-(c+d)+\frac{a g_3}{1-\rho}.
\tag{4.6}
\]

So (1.1) remains valid, now with a correct general proof.

## 5. Theorem 2 — exact first-order drift of the branching numerator S

The missing state variable is not merely `m2`; it is

\[
S=\sum ab x_q,
\]

because `rho=S/m2`.

Introduce one further mixed moment

\[
R:=\sum_q (bc+ad)x_q
\tag{5.1}
\]

and, for `m3>0`,

\[
\kappa:=\frac{2R}{3m_3}.
\tag{5.2}
\]

If `m3=0`, set `kappa=0`.

Interpretation: `kappa` is the expected increase of `S` caused by the two partner literals when one 3-clause is shortened to a 2-clause.

### Lemma 2a: deleting a 2-clause changes S by `-rho` in expectation through its partner variable

For a positive partner stub, removing that stub sends `a -> a-1`, so `ab` changes by `-b`.  Under positive 2-stub size bias the mean is

\[
-\frac{S}{A}.
\]

For a negative partner stub the corresponding mean is `-S/B`.  Mixing partner signs with probabilities `A/(A+B)` and `B/(A+B)` yields

\[
-\frac{S}{A+B}-\frac{S}{A+B}
=-\frac{2S}{A+B}
=-\rho.
\tag{5.3}
\]

### Lemma 2b: shortening one 3-clause changes S by `kappa` in expectation through its two partner variables

A positive 3-stub converted to a positive 2-stub sends `a -> a+1`, changing `ab` by `+b`; its size-biased mean is `sum bc x/C`.  A negative converted stub changes `ab` by `+a`, with mean `sum ad x/D`.  After mixing signs and multiplying by two partner literals, the expected change is exactly

\[
\frac{2}{3m_3}\sum_q (bc+ad)x_q=\kappa.
\tag{5.4}
\]

### Direct free-move S drift

For a free TRUE assignment of class `q`, deleting the selected variable itself contributes `-ab`; its `a+b` incident 2-clauses contribute `-(a+b)rho`; and its `d` falsified 3-clauses each shorten and contribute `+kappa`.  Hence

\[
s_T(q)=-ab-(a+b)\rho+d\kappa.
\tag{5.5}
\]

Similarly

\[
s_F(q)=-ab-(a+b)\rho+c\kappa.
\tag{5.6}
\]

### Forced-move S drift

For a positive forced unit, its source positive 2-stub was already consumed when the unit clause was formed.  The selected variable therefore removes `(a-1)b` from `S`, not `ab`.  Thus

\[
h_+(q)=-(a-1)b-(a+b-1)\rho+d\kappa.
\tag{5.7}
\]

For a negative forced unit,

\[
h_-(q)=-a(b-1)-(a+b-1)\rho+c\kappa.
\tag{5.8}
\]

Averaging with the correct sign/stub mixture gives

\[
\boxed{
 g_S=\frac1{2m_2}\sum_q x_q\bigl[a h_+(q)+b h_-(q)\bigr].
}
\tag{5.9}
\]

Consequently, after the complete expected avalanche,

\[
\boxed{
 H_T(q)=s_T(q)+\frac{b g_S}{1-\rho},
\qquad
 H_F(q)=s_F(q)+\frac{a g_S}{1-\rho}.
}
\tag{5.10}
\]

These are the first-order drifts of `S` per free assignment.

All terms above are exact conditional first-order expectations in the degree-sequence configuration model; only the standard finite-`n` collision error is suppressed.

## 6. Corollary — exact first-order drift of rho and its polarity index

Since

\[
\rho=\frac{S}{m_2},
\]

the quotient rule gives

\[
\boxed{
\mathcal R_T(q)
=\frac{H_T(q)-\rho G_{2,T}(q)}{m_2},
\qquad
\mathcal R_F(q)
=\frac{H_F(q)-\rho G_{2,F}(q)}{m_2}.
}
\tag{6.1}
\]

Subtracting and simplifying yields

\[
\boxed{
\mathcal R_T(q)-\mathcal R_F(q)
=\frac1{m_2}\left[
(d-c)(\kappa-\rho)
+(b-a)\frac{g_S-\rho g_2}{1-\rho}
\right].
}
\tag{6.2}
\]

Define

\[
\mu:=\frac{g_S-\rho g_2}{1-\rho}.
\tag{6.3}
\]

Then the instantaneous branching-safe polarity is

\[
\boxed{
\text{TRUE iff }
(d-c)(\kappa-\rho)+(b-a)\mu\le0.
}
\tag{6.4}
\]

This is the direct analogue, for actual unit-cascade criticality, of the earlier clause-risk rule (1.1).

It also solves the **class-selection** ambiguity for the myopic branching objective: among occupied classes, choose the class/polarity with minimum value of `R_T` or `R_F`.  Thus the Hajiaghayi--Sorkin four-parameter question “which class, and how should it be set?” now has an explicit answer for two natural objectives:

- clause-risk minimization `V_eta`, and
- branching-criticality minimization `rho`.

The remaining problem is not local ambiguity; it is choosing the correct global tradeoff between those objectives and proving its trajectory succeeds above 3.52.

## 7. A fully specified candidate control family: logarithmic rho barrier

Clause cleanup alone is unsafe near criticality; rho minimization alone may preserve too many 3-clauses.  A natural combined fluid potential is

\[
\boxed{
\Phi_{\eta,\beta}
=m_2+\eta m_3-\beta\log(1-\rho),
\qquad \eta\ge1,\;\beta>0,
}
\tag{7.1}
\]

on the subcritical domain `rho<1`.

For a free action `P in {T,F}` define

\[
\boxed{
F_P(q)=G_{2,P}(q)+\eta G_{3,P}(q)
+\beta\frac{\mathcal R_P(q)}{1-\rho}.
}
\tag{7.2}
\]

**Candidate algorithm A(eta,beta):** after exhausting unit clauses, compute the current four-parameter degree state and the moments above; among all occupied degree classes and the two polarities choose a minimizer of `F_P(q)`; execute that free assignment; exhaust its unit cascade; repeat.  When `m2=0`, the barrier is inactive and one uses the direct `V_eta` drift.  A rigorous batched version sets `Theta(n)` variables from the selected class per differential-equation round exactly as in Hajiaghayi--Sorkin.

The polarity comparison is the single scalar index

\[
\boxed{
I_{\eta,\beta}(q)
=(d-c)+(b-a)\frac{g_\eta}{1-\rho}
+\frac{\beta}{m_2(1-\rho)}
\left[(d-c)(\kappa-\rho)+(b-a)\mu\right].
}
\tag{7.3}
\]

Choose TRUE iff `I_{eta,beta}(q)<=0`.

This is now a **complete deterministic degree-state rule**, not an unspecified lookup table.  It is still only a candidate lower-bound algorithm because this run has not integrated the complete truncated ODE and certified a density `alpha>3.52`.

### Why the barrier is structurally the right missing term

On any finite degree truncation with `m2` bounded below and the state away from other denominator boundaries, the clause-risk polarity difference grows at worst like `O((1-rho)^-1)`, while the barrier term in (7.3) can grow like `O((1-rho)^-2)`.  Therefore, whenever two available actions have genuinely different leading rho drift, the barrier dominates close enough to criticality.  This is precisely the behavior absent from the `V_eta`-only rule.

## 8. Exact finite-state certificates: cleanup and safety can demand opposite polarities

I wrote and executed an exact-rational verifier:

`artifacts/2026-09-20T03-28-00__rho_barrier_exact_verifier.py`

with archived output

`artifacts/2026-09-20T03-28-00__rho_barrier_exact_verifier.out`.

### Example A

Use the complement-symmetric synthetic fluid state obtained from three copies of each class

\[
(0,1,0,0),\ (1,0,0,0),\ (1,1,0,1),\ (1,1,1,0),
\]

normalized by the 12 variables.  Exact moments are

\[
m_2=\frac34,\qquad m_3=\frac16,\qquad
\rho=\frac23,\qquad \kappa=2,
\]

\[
g_2=-\frac13,\qquad g_3=-\frac23,\qquad g_S=\frac29.
\]

For class `q=(0,1,0,0)`:

\[
G_{1,T}=-4,\qquad G_{1,F}=-1,
\]

so total-clause cleanup strongly prefers TRUE.  But

\[
\mathcal R_T=\frac{16}{9},\qquad
\mathcal R_F=0,
\]

so branching safety prefers FALSE.

This is an exact counterexample to the idea that the previous `V_1` local objective alone can stand in for unit-cascade safety.

### Example B — near criticality the logarithmic barrier actually flips the decision

Use three copies of each class

\[
(0,3,3,0),\ (3,0,0,3),\ (1,3,3,0),\ (3,1,0,3),
\]

again normalized by 12.  Then

\[
m_2=\frac74,\qquad m_3=1,\qquad \rho=\frac67,
\]

and for `q=(0,3,3,0)`

\[
G_{1,T}=-69,\qquad G_{1,F}=-3,
\]

while

\[
\mathcal R_T=\frac{7272}{49},\qquad
\mathcal R_F=\frac{432}{49}.
\]

For `Phi_{1,beta}`, the exact polarity-flip point is

\[
\boxed{\beta_*=\frac{77}{1140}\approx0.06754386.}
\tag{8.1}
\]

Thus `beta=0.1` already rejects the spectacular immediate clause-count gain because it is too dangerous for the branching factor.  The verifier checked every displayed fraction exactly with Python `Fraction`; output is `EXACT VERIFIER: PASS`.

This is a demonstrated mechanism gain: the new state functional detects and corrects a failure mode that the preceding control law provably misses.

## 9. Poisson closure sanity check — heuristic, not a threshold proof

For intuition only, suppose the remaining-variable density is `u` and

\[
a,b\stackrel{iid}{\sim}\operatorname{Poisson}(p),
\qquad
c,d\stackrel{iid}{\sim}\operatorname{Poisson}(q),
\]

with

\[
p=\frac{m_2}{u},
\qquad
q=\frac{3m_3}{2u}.
\]

Then exact moment algebra under this closure gives

\[
\rho=p,\qquad \kappa=2p,
\tag{9.1}
\]

\[
g_2=q-2p,\qquad g_3=-2q,
\tag{9.2}
\]

\[
g_S=p(2q-3p),
\tag{9.3}
\]

and hence

\[
\mu=\frac{p(q-p)}{1-p}.
\tag{9.4}
\]

Therefore the rho-minimizing polarity index (6.4) becomes, after dividing by positive `p`,

\[
\boxed{
(d-c)+(b-a)\frac{q-p}{1-p}.
}
\tag{9.5}
\]

This exposes a clean phase distinction.  When `q>p`, i.e.

\[
m_3>\frac23 m_2,
\tag{9.6}
\]

branching control puts a **positive** price on the 2-degree seed imbalance `b-a`: early in a 3-clause-heavy trajectory it wants to suppress dangerous seed production.  By contrast, the `V_1` coefficient is

\[
\frac{g_1}{1-p}
=-\frac{q+2p}{1-p}<0,
\tag{9.7}
\]

so clause cleanup always rewards the same unit-seeding direction.  This analytic disagreement is exactly what the barrier interpolates.

The closure is not asserted for the degree-selected process.  It is only a sanity calculation revealing the sign mechanism; the exact theorems are Sections 3--7.

## 10. What would constitute a rigorous lower-bound improvement from here

The local control ambiguity is no longer the main missing ingredient.  To turn this into `alpha_LB>3.52`, a later run must complete all of the following.

1. **Full four-parameter truncated ODE.**  Track `x_{a,b,c,d}` up to a cutoff `h`, including neighbor transitions from 2-clause deletion and 3-to-2 shortening.  The moments `rho,kappa,g2,g3,gS` above are algebraic functions of that state.
2. **Batched implementation of A(eta,beta).**  On each compact region where one degree class/polarity uniquely minimizes (7.2), set `delta n` such variables, then follow the induced forced process.  Tie surfaces can be handled by a deterministic rule.
3. **Subcritical certificate.**  Produce an interval proof that `rho<=1-epsilon` throughout.  This is now a directly tracked obligation rather than an indirect hope from clause counts.
4. **Terminal satisfiability theorem.**  Enter the exact Cooper--Frieze--Sorkin residual regime used by Hajiaghayi--Sorkin, with all required degree/tail hypotheses checked.
5. **Rigorous numerics.**  Use interval integration plus an explicit high-degree tail bound and Lipschitz enclosure.  Hajiaghayi--Sorkin themselves note that this is required to turn the differential-equation numerics into a completely rigorous decimal.
6. **First target density.**  Test `alpha=3.52+epsilon` for a small explicit `epsilon` (for example `10^-3` only as an initial numerical target), and only call the source lower endpoint moved if the whole chain above certifies it.

No simulation or replica value will be substituted for these steps.

## 11. Honest failed-attack accounting this run

- **V_eta-only continuation:** rejected as insufficient.  Exact Example A proves that the clause-count objective can prefer a polarity with strictly worse instantaneous rho drift.
- **Treating the unit cascade as one sign-blind Galton--Watson process from the outset:** the scalar rho happens to be right, but the old sign-conditional normalization was not.  Replaced by the exact rank-one two-type process, which recovers the scalar formulas legitimately.
- **Immediate threshold-number search before deriving rho drift:** not attempted.  Without a safety state variable, such a numerical search would only optimize an analytically incomplete heuristic and would not justify spending this run on a large checker.

This is therefore **one substantive mechanism advance with an exact verifier, but no source-level bound change**.

## 12. Next attack

The next run should not add another local potential.  It should write the finite-cutoff transition equations for `x_{a,b,c,d}` and execute a first interval/validated integration comparison of:

- the inherited two-parameter Hajiaghayi--Sorkin rule,
- `A(1,0)` (clause cleanup only), and
- `A(1,beta)` for a small grid of positive beta,

with the primary diagnostic `max_t rho(t)` and the terminal CFS admissibility condition.  A useful run must either produce a certified epsilon above 3.52 or isolate the exact state/tie/tail obstruction preventing certification.

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  current_role: NM06_Constructive_Random_3SAT
  target: T04
  source_model: "iid random proper 3-CNF; m=floor(alpha n); 3 distinct variables; independent uniform signs"
  source_status: OPEN
  worker_status: PARTIAL
  source_metric:
    name: "strongest supported unconditional explicit threshold bracket"
    before: "[3.52, 4.4898], width 0.9698"
    after: "[3.52, 4.4898], width 0.9698"
    movement: NO_SOURCE_NUMERICAL_MOVEMENT
  mechanism_gain:
    before: "four-parameter V_eta polarity law; no exact rho-drift control; sign-conditional unit normalization misstated"
    after: "exact two-type branching proof; exact first-order drift of S=sum(ab x), exact rho drift, rho polarity index, and fully specified logarithmic rho-barrier control family Phi_{eta,beta}"
    key_formulas:
      branching_factor: "rho = (sum ab*x)/m2"
      shortening_gain: "kappa = 2*sum(bc+ad)x/(3m3)"
      forced_S_drift: "gS=(1/(2m2))*sum x*[a h_plus+b h_minus]"
      rho_drift: "R_P=(H_P-rho G2_P)/m2"
      rho_polarity: "TRUE iff (d-c)(kappa-rho)+(b-a)(gS-rho*g2)/(1-rho) <= 0"
      barrier: "Phi_eta_beta=m2+eta*m3-beta*log(1-rho)"
    demonstrated_tradeoff:
      example_A: "V1 prefers TRUE (-4<-1), while rho drift prefers FALSE (16/9>0)"
      example_B: "near rho=6/7, exact barrier flip beta*=77/1140; beta=0.1 reverses the V1 choice"
  exact_artifacts:
    code: "proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T03-28-00__rho_barrier_exact_verifier.py"
    output: "proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T03-28-00__rho_barrier_exact_verifier.out"
    result: "EXACT VERIFIER: PASS"
  literature_check_2026_09_20:
    lower: "Hajiaghayi-Sorkin arXiv:math/0310193 -> 3.52"
    upper_unconditional: "Diaz-Kirousis-Mitsche-Perez-Gimenez arXiv:0807.3600 -> 4.4898"
    conditional_4453_note: "Maneva-Sinclair 4.453 is a core-structure result; Diaz et al. state the satisfiability-upper-bound interpretation needs an unproved k=3 geometry conjecture"
    recent_scope: "2026 random-k-SAT work checked; no fixed-k=3 threshold closure used"
  failed_this_run:
    - "V_eta-only control is unsafe for rho; exact counterexample recorded"
    - "sign-blind branching justification corrected to a two-type derivation"
  next_step: "derive the complete truncated x_abcd ODE and run validated interval integration for A(1,beta), tracking max rho and the terminal CFS condition; attempt a certified alpha>3.52"
```
