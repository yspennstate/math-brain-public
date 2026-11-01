Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is not GPT-6 at maximum. GPT-6 / maximum was requested, but no authenticated binding model-family or effort selector is exposed, so I do not claim otherwise.

# R7-04 P0220 six-unchanged-run retirement handoff

Date: 2026-09-19 UTC  
Worker: **R7-04 Constructive Model Research**  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Own root: `research7_2026-09-17/R7-04/`  
Canonical target: **P0220**  
Source classification at handoff: **CLOSABLE OUTSIDE / OPEN / PARTIAL**  
Worker-local disposition: **RESEARCH RETIRED AFTER SIX ORDINARY UNCHANGED RUNS**

This handoff is a worker-local protocol action. It is **not** a release of canonical ownership, not a claim that the source problem is solved, and not permission for another worker to ignore `operations/claims/P0220.md`. Only an owner/coordinator-authorized release or reassignment can alter that ownership boundary.

## 1. Source and exact closure criterion

Original/current source:

David Aldous, *A one-dimensional drift-jump particle process*, living problem page posted February 2018:

`https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html`

Historical source material:

Aldous--Diaconis unfinished 1993 notes, Sections 4.1--4.2:

`https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf`

The finite-k process has ordered particles

\[
0<X_1(t)<\cdots<X_k(t),
\]

linear drift `dX_i/dt=X_i`, and rate-one space-time Poisson events that move the closest particle to the right of an event point down to that point. The finite-k laws are consistent and have a unique stationary distribution. Aldous asks for a **fairly explicit description of that stationary distribution**.

The R7-04 source-closure criterion used throughout was stronger than a scalar marginal: give an explicit, rigorously source-matched description of every finite-dimensional stationary joint law, with enough convergence/normalization control that the formula is mathematically well-defined and constructively evaluable. Campaign closure additionally requires current prior-art reconciliation, independent P26 and distinct OTHER-track audits, and a self-contained source-scope paper package.

Admission record:

`research7_2026-09-17/R7-04/admissions/2026-09-19T004100Z__P0220_admission.md`

Admission creation commit:

`6558b41b333bbfb2b06711fabb3f1d2950a503d2`

Canonical ownership claim:

`operations/claims/P0220.md`

## 2. Frozen metric and retirement trigger

Frozen metric:

`K_Bessel = sup{k : a finite Toeplitz/Bessel determinant formula for P(X_k>x), all x>=0, is rigorously derived and source-matched}`.

Chronology:

- admission baseline: `K_Bessel=1`;
- first P0220 research run: `1 -> infinity` by the all-k Gessel/Bessel determinant formula;
- subsequent ordinary runs: `infinity -> infinity` each time;
- one mandatory STUCK1 diagnosis occurred after the third unchanged ordinary run;
- one recovery cycle was used;
- this final B5/B11/B29 run is the sixth ordinary unchanged run after saturation.

Therefore the owner rule for a CLOSABLE target requires R7-04 to stop active P0220 research now. Mathematical strengthening after saturation does not reset the frozen metric.

## 3. Safe cumulative mathematical core

The following results survived the R7-04 internal reconciliation and should be treated as the safe cumulative core unless an independent audit finds a defect.

### 3.1 Source-native stationary law = poissonized Plancherel first-row hitting times

Let `B(j)` be the stabilized j-th patience-pile top label in the Aldous--Diaconis representation, and let

\[
T_j=\inf\{n:(\Lambda_n)_1\ge j\}
\]

for discrete Plancherel growth. RSK gives

\[
(B(1),\ldots,B(k))\overset d=(T_1,\ldots,T_k).
\]

If `Gamma(n)` is the n-th arrival time of an independent rate-one Poisson process, then the source stationary law satisfies

\[
\boxed{
(X_1,\ldots,X_k)\overset d=(\tau_1,\ldots,\tau_k),
\qquad
\tau_j=\inf\{t:\Lambda_1(t)\ge j\},
}
\]

where `Lambda(t)` is rate-one poissonized Plancherel growth.

Crucially, R7-04 later proved this stationary identification without relying on the historical balance PDE or on a Schur/Fredholm formula: the source finite-time laws converge to the Aldous--Diaconis candidate, the finite-k drift-jump semigroup is Feller under the common Poisson-point coupling, and the semigroup limit therefore leaves the candidate invariant.

### 3.2 All scalar stationary marginals

For `k>=1`,

\[
\boxed{
\Pr(X_k>x)
=
 e^{-x}
 \det[I_{i-j}(2\sqrt{x})]_{i,j=1}^{k-1}.
}
\]

This is Gessel's Toeplitz/Bessel determinant applied to the event that a poissonized random permutation has longest increasing subsequence shorter than `k`.

Special cases include

\[
\Pr(X_1>x)=e^{-x},
\]

\[
\Pr(X_2>x)=e^{-x}I_0(2\sqrt{x}),
\]

and

\[
\Pr(X_3>x)=e^{-x}[I_0(2\sqrt{x})^2-I_1(2\sqrt{x})^2].
\]

The determinant machinery is classical prior art; the source-specific composition is the object whose exact historical priority remains to be settled.

### 3.3 Positive full-joint partition/path law

For observation times `0=t_0<t_1<...<t_r` and nested diagrams

\[
\varnothing=\lambda^{(0)}\subset\cdots\subset\lambda^{(r)},
\]

with `n_a=|lambda^(a)|` and `d_a=n_a-n_(a-1)`,

\[
\boxed{
\Pr(\Lambda(t_a)=\lambda^{(a)},1\le a\le r)
=
 e^{-t_r}
 \frac{f^{\lambda^{(r)}}}{n_r!}
 \prod_{a=1}^r
 \frac{f^{\lambda^{(a)}/\lambda^{(a-1)}}(t_a-t_{a-1})^{d_a}}{d_a!}.
}
\]

Hence arbitrary stationary survival probabilities are exact positive sums over nested partitions with first-row constraints. A finite partition dynamic program truncated at total size `N` has error at most

\[
\Pr\{\operatorname{Pois}(T)>N\},\qquad T=\max t_a.
\]

### 3.4 Reconciled extended Schur/Fredholm formula

Under the forward Okounkov--Reshetikhin convention, the correct auxiliary factor is

\[
\boxed{\Phi(t,z)=e^{z-t/z}.}
\]

The temporary STUCK1 concern about `e^{tz-z^{-1}}` came from comparing raw specializations before the OR inversion convention; it was explicitly reconciled in the B6 run.

The extended kernel can be written

\[
\boxed{
K((t,x),(s,y))
=
\frac{1}{(2\pi i)^2}
\oint\!\oint
\frac{e^{z-t/z-w+s/w}}{z-w}
 z^{-x-1/2}w^{y-1/2}\,dw\,dz,
}
\]

with the contour nesting determined by the time ordering. If

\[
H_k=\{k-\tfrac12,k+\tfrac12,\ldots\},
\]

then

\[
\boxed{
\Pr(X_{k_a}>t_a\ \forall a)
=
\det(I-K)_{\bigsqcup_a\{t_a\}\times H_{k_a}}.
}
\]

An earlier run proved finite spatial truncation with a Poisson-tail error. The final B29 run additionally proved direct absolute convergence of the infinite-half-line Fredholm **series** and an order-truncation certificate; no trace-class assertion for a particular raw block-operator realization is needed.

### 3.5 Direct absolute Fredholm-series bound

For the multi-time gap set `A` with `r` time slices and `T=max t_a`, let `N_A` be the total number of Maya particles lying in the forbidden half-lines. Then

\[
N_A\le rN(T),\qquad N(T)\sim\operatorname{Pois}(T),
\]

so

\[
\mathbb E2^{N_A}\le e^{T(2^r-1)}<\infty.
\]

This equals the absolute sum of the factorial-moment/Fredholm expansion, proving direct absolute convergence. If the Fredholm series is cut after order `M`,

\[
\boxed{
R_M\le
 e^{T(2^r-1)}
 \Pr\!\left\{\operatorname{Pois}(2^rT)\ge
 \left\lfloor M/r\right\rfloor+1\right\}.
}
\]

The full derivation is in

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T074600Z__P0220_beta_duality_and_absolute_fredholm.md`.

### 3.6 Finite-particle row-cap duality

For sorted observation times define suffix-min thresholds

\[
\kappa_a=\min_{b\ge a}k_b,
\qquad m_a=\kappa_a-1.
\]

After transposition, arbitrary joint width constraints become nondecreasing finite row caps

\[
\Lambda_1(t_a)<k_a\ \forall a
\iff
\ell(\Lambda'(t_a))\le m_a\ \forall a.
\]

With particle coordinates `x_i(mu)=mu_i-i` and Poisson one-particle kernel

\[
p_u(a,b)=1_{a\ge b}\frac{u^{a-b}}{(a-b)!},
\]

Jacobi--Trudi gives

\[
s_{\mu/\lambda}(\rho_u)=\det[p_u(x_i(\mu),x_j(\lambda))].
\]

The arbitrary joint law is therefore a finite-particle transfer sum with checkpoint pinnings `x_i=-i` for rows above the current cap. Constant caps collapse by Cauchy--Binet to the scalar determinant; changing caps insert genuine projections and block the naive single-determinant collapse. No claim is made that some more elaborate finite determinant is impossible.

### 3.7 Terminal-parameter beta deformation and source moment identities

Replacing the terminal Plancherel specialization `rho_1` by `rho_beta` produces

\[
\frac{dP_\beta}{dP_1}=e^{-(\beta-1)T}\beta^{N_T},
\]

and exactly time-dilates growth:

\[
(\Lambda_\beta(t_a))_a\overset d=(\Lambda_1(\beta t_a))_a.
\]

The Schur kernel obeys the gauge identity

\[
K_\beta((t,x),(s,y))
=
\beta^{x-y}K_1((\beta t,x),(\beta s,y)).
\]

For a stationary survival event `E` with probability `p(t_1,...,t_r)` and dilation derivative `D=sum t_a d/dt_a`,

\[
\boxed{E[N_T\mid E]-T=D\log p,}
\]

\[
\boxed{\operatorname{Var}(N_T\mid E)-E[N_T\mid E]=(D^2-D)\log p,}
\]

and hence

\[
\boxed{\operatorname{Var}(N_T\mid E)=T+D^2\log p.}
\]

These give source-level diagnostics for any future representation.

### 3.8 Low-dimensional explicit formulas

The historical `k=2` density resums to

\[
p_2(x_1,x_2)
=e^{-x_2}\left[
\frac{I_1(2\sqrt{x_2-x_1})}{\sqrt{x_2-x_1}}
-
\frac{I_2(2\sqrt{x_2-x_1})}{x_2-x_1}
\right],
\]

for `0<x_1<x_2`. The first gap `G=X_2-X_1` is independent of `X_1`, with

\[
\Pr(G>u)=e^{-u}\frac{I_1(2\sqrt u)}{\sqrt u}.
\]

More generally,

\[
\Pr(X_1>s,X_k>t)
=
\begin{cases}
e^{-s},&s\ge t,\\
e^{-t}D_{k-1}(t-s),&s<t,
\end{cases}
\]

where `D_m(u)=det[I_{i-j}(2sqrt(u))]_(i,j=1)^m`, and

\[
X_1\perp(X_2-X_1,X_3-X_1,\ldots).
\]

An independent exact `k=3` nested-partition series was also derived, including the skew-tableau reflection identity

\[
f^{(2^q,1^r)/(1^m)}
=
\binom{2q+r-m}{q}-\binom{2q+r-m}{q-m-1}.
\]

The exact checker for that run passed all enumerated hook, skew-tableau, coefficient, and boundary checks.

### 3.9 Correct source generator and historical balance-equation defect

For the finite-k drift-jump process, the source generator is

\[
L_k f(x)
=
\sum_{i=1}^k x_i\partial_i f(x)
+
\sum_{i=1}^k\int_{x_{i-1}}^{x_i}
[f(x^{i\leftarrow y})-f(x)]\,dy.
\]

The correct stationary adjoint equation is

\[
\boxed{
x_kp_k
=-k p_k-\sum_{i=1}^k x_i\partial_i p_k
+\sum_{i=1}^k\int_{x_i}^{x_{i+1}}
 p_k(x_1,\ldots,z,\ldots,x_k)\,dz.
}
\]

The unfinished 1993 notes print `-p_k` rather than `-k p_k`; the difference is the divergence `k` of the linear drift. R7-04 does not claim the historical authors themselves identified this specific typo.

The generator also yields the Laplace functional equation archived in the B12 artifact and the moment identity

\[
E X_j=\frac12E(X_j-X_{j-1})^2.
\]

## 4. Exact/certified checks already archived

The cumulative exact checks include:

- historical `k=2` discrete patience/Bessel identity;
- Gessel determinant coefficient checks for small determinant sizes and permutation sizes;
- an exact witness that the discrete first-row hitting sequence is not Markov in only its most recent hitting time;
- the `k=3` skew-tableau reflection identity and both Bessel boundary reductions through finite shape size 9;
- all relevant scripts and outputs were created after the corresponding derivations, not used as substitutes for proofs.

Do not call those finite checks a proof of the source theorem by themselves.

## 5. Prior art / openness state at handoff

A fresh 2026-09-19 check of Aldous's living page still shows the problem in his active open-research list and still asks for a fairly explicit stationary distribution. The same page warns generally that his list may not reflect every later result.

Established prior machinery that must be credited includes:

- Aldous--Diaconis patience-sorting representation and the historical stationary candidate;
- Gessel/BDJ longest-increasing-subsequence determinant machinery;
- Okounkov--Reshetikhin Schur-process determinantal theory;
- Borodin--Olshanski dynamical Plancherel/discrete-Bessel correlations;
- Nica's identification of poissonized Robinson--Schensted trajectories with a Schur process/nonintersecting Poisson ensemble.

Bounded source-title, stationary-law, Plancherel, Schur, Fredholm, and Hammersley searches did not find a publication explicitly making the complete source-specific chain

Aldous drift-jump stationary law -> patience pile tops -> Plancherel first-row hitting times -> explicit all-k marginals/full finite-dimensional Fredholm/positive path formulas.

That search miss is only negative evidence. **No novelty or priority claim is certified.**

## 6. Unfinished closure obligations

P0220 must remain `OPEN / PARTIAL` in R7-04's ledger because all of the following are still missing:

1. an independent **P26** full-proof audit of the source-matching package;
2. a distinct **OTHER-track** independent full-proof audit;
3. a source-scope self-contained `paper_<name>/` package reviewed against those audits;
4. stronger source-specific historical/citing-literature reconciliation sufficient to classify the candidate answer as genuinely new, already known, or a rediscovery/composition of known tools.

Self-review, the exact checkers, and coordinator receipts do not satisfy the two-auditor requirement.

## 7. Suggested future recovery route if ownership is lawfully reassigned

Do not restart scalar Bessel calculations; that metric is saturated. The highest-value mathematical continuation is the changing-row-cap finite-particle representation from the final B11 run. Write the joint law as a product of noncolliding Poisson transfer kernels and explicit checkpoint projections, then determine whether an Eynard--Mehta/Cauchy--Binet block determinant collapses that product to a source-friendly finite determinant. Use the beta deformation moment identities as normalization tests and the positive Young-diagram formula as the noncircular reference law.

If the goal is closure rather than new mathematics, the next action should instead be independent audits and a careful prior-art/source comparison, not another R7-04 research iteration.

## 8. Ownership / retirement boundary

- `operations/claims/P0220.md` still names R7-04 and was reread during the terminal run.
- This handoff does **not** delete, edit, overwrite, or release that claim.
- It does **not** edit shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.
- It does **not** revive any retired/held source or transfer any metric to a successor.
- R7-04 must rotate only after a different unclaimed shard-3 outside source passes the complete admission gate.

Final R7-04 P0220 state:

`OPEN / PARTIAL / WORKER-LOCAL RESEARCH RETIRED AFTER SIX UNCHANGED RUNS / OWNERSHIP NOT RELEASED / AUDITS MISSING`.
