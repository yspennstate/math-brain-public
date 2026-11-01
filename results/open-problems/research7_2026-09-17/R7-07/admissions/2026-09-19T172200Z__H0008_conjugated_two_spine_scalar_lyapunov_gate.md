Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# H0008 admission-feasibility mathematics: conjugated two-spine transfer, scalar Lyapunov certificate, and exact extremal equations

Date: 2026-09-19 UTC  
Worker: `R7-07` / native ID `6aabe8413f60819197825dd81ca138ae`  
Status: **PENDING_ADMISSION / H0008 NOT OWNED BY R7-07**  
Methods: **B11 DUALIZE / B24 FIND THE EXTREMAL OBJECT / B5 ADD A PARAMETER AND DIFFERENTIATE**

## 0. Scope and continuity

This is bounded feasibility mathematics on released HARD OUTSIDE source `H0008`. The canonical file `operations/claims/H0008.md` already exists and records `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`. R7-07's installed acquisition rule allows only a create-only canonical claim and requires a collision skip. Therefore this artifact does **not** claim ownership, does not edit that canonical history, and does not start an R7-07 source metric or stagnation counter.

The exact outside source remains Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), **Boundary fluctuations**. R14's terminal handoff preserves the still-open general finite-type harmonic-measure/dimension-drop clause. R7-07's preceding runs developed a genuinely different two-harmonic-ray route rather than replaying R14's exhausted direct fixed-point iteration.

The immediately preceding R7-07 artifact proved the exact many-to-two transfer below and isolated the boundary matrix `J`. The present run does not re-prove those source reductions; it starts from them and changes variables so that the remaining singular denominator disappears exactly.

## 1. Standing finite-type notation

Let the finite type set be `D={1,...,d}`. Under the source finite-type failed-cluster law, let

- `nu` be the potential-child count, with `m_* = E nu` and `E nu^2 < infinity` in the finite-variance regime used by the handoff;
- `q_j>0` be child-type frequencies;
- `p_ij>0` be the type-dependent transmission probabilities;
- `P_i` be the forward descendant-tree law from a type-`i` root;
- `B(T) in [0,1)` be the escape probability across the artificial parent edge, with `B=0` on extinction.

For a surviving vertex with positive child conductances `B_u`, put

`S = sum_u B_u`,

so electrical reduction gives

`B = S/(1+S)`, `S=B/(1-B)`.

Harmonic measure chooses child `u` with probability `B_u/S`.

For a distinguished transmitted child of conductance `b`, let `R_i>=0` be the total conductance of its transmitted surviving siblings when the parent has type `i`, under the size-biased sibling law already derived in the H0008 handoff. Define

`F_b(r) = (b+r)/(1+b+r)`.

R7-07 previously proved the source lower-tail estimates, uniformly over finitely many types,

`P_i(0<B<=x) <= C_B exp(-c_B/x)`

for all sufficiently small `x`, and, under the size-biased sibling law,

`P(0<R_i<=r) <= C_R exp(-c_R/r)`

for all sufficiently small `r`.

The extinction-Jacobian matrix is

`J_ij = G'(1-t_i) q_j p_ij`,

and R14 proved

`rho(J)<1`.

The exact pair-transfer operator from the preceding R7-07 run is, for nonnegative type-indexed densities `h=(h_i)`,

`(L_2 h)_j(b)`

` = m_* q_j b^2 sum_i p_ij E[ h_i(F_b(R_i)) / (b+R_i)^2 ]`.

It is the density-side adjoint of the same-child two-harmonic-ray kernel.

## 2. B11 — exact conjugation removes the singular denominator

### Theorem 2.1 (square-conductance conjugation)

For `0<b<1`, define

`c(b) = (b/(1-b))^2`.

Let `C` be multiplication by `c`, componentwise. Then

`L_2 C = C T`,

where the conjugated positive operator `T` is

`boxed:`

`(T g)_j(b)`

` = (1-b)^2 m_* q_j sum_i p_ij E[ g_i(F_b(R_i)) ].`

#### Proof

The key identity is exact:

`F_b(r)/(1-F_b(r)) = b+r`.

Therefore

`c(F_b(r)) = (b+r)^2`.

Substituting `h_i=c g_i` into the pair transfer gives

`(L_2 Cg)_j(b)`

`= m_* q_j b^2 sum_i p_ij E[ c(F_b(R_i)) g_i(F_b(R_i))/(b+R_i)^2 ]`

`= m_* q_j b^2 sum_i p_ij E[g_i(F_b(R_i))]`.

Since `c(b)=b^2/(1-b)^2`, this is exactly

`c(b) (1-b)^2 m_* q_j sum_i p_ij E[g_i(F_b(R_i))]`.

Hence `L_2 C=CT`. QED.

### Interpretation

The difficult factor `(b+R)^{-2}` was not intrinsic to the two-spine geometry. It is exactly the Jacobian created by expressing the pair transfer relative to the source conductance law. The natural coordinate is the squared electrical conductance

`c(B)=S^2`.

After conjugation, the transfer is a positive composition/averaging operator with only the explicit killing factor `(1-b)^2`.

This is a real simplification: all small-`b` singularity is moved into the choice of a Lyapunov weight rather than remaining inside the kernel itself.

## 3. The exact pipe boundary after conjugation

The size-biased sibling law satisfies

`P(R_i=0)=G'(1-t_i)/m_*`.

Indeed, under size bias the probability that each of the `hat nu-1` sibling slots fails to produce a transmitted surviving child is

`E[nu (1-t_i)^(nu-1)]/m_* = G'(1-t_i)/m_*`.

Therefore the exact `R_i=0` part of `T` is

`boxed:`

`(T_0 g)_j(b)`

`= (1-b)^2 sum_i J_ij g_i(phi(b)),`

where

`phi(b)=b/(1+b)`.

In the compactifying coordinate `u=1/b`,

`1/phi(b)=1+1/b`,

so a sole-positive-child pipe is exactly the translation

`u -> u+1`.

The genuine branch part `T_+=T-T_0` has `R_i>0` and sends

`u=1/b`

to

`u' = 1/F_b(R_i) = 1 + 1/(b+R_i)`.

Thus every fixed positive sibling conductance sends the `u=infinity` boundary back to a finite region; only `R=0` can remain at infinity. This makes the role of `J` completely transparent.

## 4. B24 — a strict boundary Lyapunov weight and the exact interior extremal problem

Because `rho(J)<1`, fix any number

`r_J` with `rho(J)<r_J<1`.

There exists a strictly positive row vector `ell=(ell_i)` such that

`ell^T J <= r_J ell^T`.

One explicit choice is

`ell^T = 1^T (I-J/r_J)^(-1)`.

Indeed,

`ell^T J = r_J(ell^T-1^T) <= r_J ell^T`.

If `J` is irreducible, one may instead take its positive left Perron vector and set `r_J=rho(J)`.

Choose

`0<eta<-log r_J`

and define the exponential compactification weight

`w_i(b)=ell_i exp(eta/b)`.

### Theorem 4.1 (exact weighted transfer ratio)

For every `0<b<1`,

`boxed:`

`(T w)_j(b)/w_j(b) = K_j(b;eta),`

where

`K_j(b;eta)`

`=(1-b)^2 exp(eta) (m_* q_j/ell_j)`

`  * sum_i p_ij ell_i E[ exp(-eta Q_b(R_i)) ]`

and

`Q_b(r)= r/[b(b+r)].`

#### Proof

Since

`1/F_b(r)=1+1/(b+r)`,

we have

`w_i(F_b(r))/w_j(b)`

`=(ell_i/ell_j) exp( eta + eta/(b+r) - eta/b )`

`=(ell_i/ell_j) exp(eta) exp(-eta r/[b(b+r)]).`

Substitute this identity in Theorem 2.1. QED.

### Corollary 4.2 (strict boundary gap)

At the pipe boundary,

`limsup_{b downarrow 0} K_j(b;eta) <= r_J exp(eta) < 1`

uniformly over the finite type set. If `ell` is the Perron left vector, the limit is exactly

`rho(J) exp(eta)`.

At the opposite boundary,

`lim_{b upward 1} K_j(b;eta)=0`.

#### Proof at `b downarrow 0`

For `R_i=0`, the exponential factor equals one and the coefficient is exactly the `J` contribution. For each fixed `R_i>0`,

`Q_b(R_i) -> infinity`

as `b downarrow 0`, so the positive-branch exponential tends to zero. Dominated convergence is enough for the qualitative limit. The `ell^T J<=r_J ell^T` inequality gives the stated bound. The `b upward 1` limit follows from the explicit prefactor `(1-b)^2` and boundedness of the remaining expectation. QED.

### Quantitative boundary estimate

The earlier `R` lower-tail estimate makes the convergence explicit. Split `R_i>0` at `R_i=sqrt(b)`. Then

`E[exp(-eta Q_b(R_i));R_i>0]`

`<= P(0<R_i<=sqrt(b))`

`   + exp[-eta/(b(1+sqrt(b)))]`

`<= C_R exp(-c_R/sqrt(b))`

`   + exp[-eta/(b(1+sqrt(b))].`

Thus the genuine-branch correction to the pipe boundary is superpolynomially small in `b`.

### The exact extremal object

Let `S_j` be the topological support in `[0,1]` of the source law of `B` for type `j`, restricted to the surviving channel and then closed by adding any limit points. Because `K_j(.;eta)` extends continuously to `b=0` and `b=1`, define

`kappa(eta)=max_j sup_{b in S_j} K_j(b;eta).`

The supremum is attained on the compact union of the `S_j`. Moreover the two boundary limits above imply:

**if `kappa(eta)>=1`, then some maximizing obstruction `(j_*,b_*)` has `0<b_*<1`.**

So the boundary compactness problem is finished at the one-step Lyapunov level. Any failure of this certificate is a concrete interior conductance-scale obstruction, not escape of mass to `B=0` or `B=1`.

## 5. Scalar Lyapunov certificate implies the two-spine second-moment gate

The preceding run reduced the remaining two-spine obstruction to finiteness of the source expectation of

`B_o^2 E_T[tau^2]`,

where `tau=L+1` is the common-prefix lifetime of two independent harmonic rays in one tree.

The new conjugation yields a one-number sufficient certificate.

### Theorem 5.1 (scalar certificate)

Assume the source finite-variance regime and the previously proved escape lower tail. Fix `r_J`, `ell`, and `eta` as above, with in addition

`eta<c_B`,

where `c_B` is any exponential rate valid in

`P_i(0<B<=x)<=C_B exp(-c_B/x)`.

If

`boxed: kappa(eta)<1,`

then for every starting type `a`,

`boxed: E_{P_a}[ B^2 tau^2 ; B>0 ] < infinity.`

In fact the weighted pair-survival masses decay geometrically.

#### Proof

For a fixed starting type `a`, define the initial density vector

`h^(0)_i(b)=1_{i=a} b^2`.

Since `h^(0)=C g^(0)`,

`g^(0)_i(b)=1_{i=a}(1-b)^2`.

Because the type set is finite and `w_i(b)>=ell_i exp(eta)`, there is a finite constant `A` such that

`0<=g^(0)<=A w`

componentwise on source support.

The definition of `kappa` gives

`T w<=kappa(eta) w`

source-almost everywhere. Positivity therefore implies inductively

`T^n g^(0)<=A kappa(eta)^n w`.

Conjugating back,

`L_2^n h^(0) = C T^n g^(0)`

`<= A kappa(eta)^n Cw`.

It remains to show that `Cw` is integrable under every source type law. But

`c(B)w_i(B)=ell_i (B/(1-B))^2 exp(eta/B)`.

On `0<B<=1/2`, `(B/(1-B))^2<=4B^2<=1`, and the tail estimate on `1/B` gives

`E exp(eta/B)<infinity`

for every `eta<c_B`. On `B>1/2`,

`B/(1-B)=S<=nu`,

and `exp(eta/B)<=exp(2eta)`, so finite variance gives

`E[c(B)w_i(B);B>1/2] <= ell_i exp(2eta) E[nu^2] < infinity`.

Hence there is `A'<infinity` with

`sum_i E_i[(L_2^n h^(0))_i(B)] <= A' kappa(eta)^n`.

By the defining transfer duality, the left side for the chosen starting component is

`m_n = E_{P_a}[ B^2 P_T(tau>n) ]`.

For integer `tau>=1`,

`tau^2 = sum_{n=0}^{tau-1}(2n+1)`.

Tonelli therefore gives

`E_{P_a}[B^2 tau^2]`

`=sum_{n>=0}(2n+1)m_n`

`<=A' sum_{n>=0}(2n+1)kappa(eta)^n`

`<infinity`.

QED.

### What this theorem does and does not prove

It is a genuine sufficient theorem. It converts the infinite-dimensional two-spine moment question into the scalar inequality `kappa(eta)<1` for one admissible `eta`.

It does **not** prove that such an `eta` exists under every H0008 source law. A pointwise one-step Lyapunov certificate can be stronger than the true spectral/Green-function condition. Therefore failure of `kappa(eta)<1` is not a counterexample to the source problem and is not even a proof that the two-spine moment diverges.

Under the preceding R7-07 roof reduction, verifying this certificate would discharge the isolated two-spine moment sufficient condition used to establish finite mean of the exit-level regeneration roof. The remaining H0008 clauses (stationary tower equivalence and the full PF-KL identification) would still need their separately recorded arguments.

## 6. B5 — differentiate the weight parameter: exact convex optimization

The scalar certificate has a useful one-dimensional variational structure.

For fixed `(j,b)` define positive coefficients

`a_{ij}=m_* q_j p_ij ell_i/ell_j`

and

`Z_{j,b}(eta)=sum_i a_{ij} E[exp(-eta Q_b(R_i))].`

Then

`K_j(b;eta)=(1-b)^2 exp(eta) Z_{j,b}(eta).`

Let `E_{j,b,eta}` denote expectation under the probability law on pairs `(i,R_i)` obtained by normalizing the weights

`a_{ij} exp(-eta Q_b(R_i)).`

### Proposition 6.1 (parameter derivatives)

For every fixed `j` and `0<b<1`,

`boxed:`

`d/deta log K_j(b;eta) = 1-E_{j,b,eta}[Q_b(R)],`

and

`boxed:`

`d^2/deta^2 log K_j(b;eta)`

` = Var_{j,b,eta}(Q_b(R)) >=0.`

Thus `eta -> log K_j(b;eta)` is convex. Consequently

`Psi(eta)=log kappa(eta)=sup_{j,b in S_j} log K_j(b;eta)`

is convex wherever finite.

#### Proof

For fixed `b>0`, `0<=Q_b(R)<=1/b`, so differentiation under the expectation is immediate. Since

`log K = constant + eta + log Z`,

one obtains

`(log Z)'=-E_eta Q`,

`(log Z)''=Var_eta(Q)`.

A supremum of convex functions is convex. QED.

### The exact competitor threshold

The sign of the first derivative is governed by whether `Q_b(R)` is above or below one. Algebra gives

`Q_b(R)>1`

iff

`R > b^2/(1-b)`.

Therefore increasing `eta` suppresses ordinary genuine branches, but **very small positive competitor conductance below `b^2/(1-b)` pushes in the opposite direction because of the global `exp(eta)` pipe-shift factor**. This is why simply taking `eta` as large as the pipe condition allows cannot be a proof. The previously proved `exp(-c/R)` rarity of near-pipe branches is exactly the input needed at this threshold.

At an interior minimizing `eta` for a single active extremizer, the stationarity equation is

`boxed: E_{j,b,eta}[Q_b(R)]=1.`

With several active extremizers, zero must lie in the convex hull of their slopes `1-E[Q]`.

This turns weight selection into a one-dimensional convex minimax problem rather than an arbitrary Lyapunov-function search.

## 7. B24 continued — exact conductance equation for an interior maximizer

For fixed `eta`, suppose `(j,b_*)` is an interior differentiable maximizer of `K_j(b;eta)` over the support and `0<b_*<1`. Since the sibling law does not depend on the distinguished child's realized conductance `b`, differentiation in `b` is legitimate.

We have

`d/db Q_b(R)`

`= - R(2b+R)/[b^2(b+R)^2].`

Hence

`d/db log K_j(b;eta)`

`= -2/(1-b)`

`  + eta E_{j,b,eta}[ R(2b+R)/(b^2(b+R)^2) ].`

At an interior extremum,

`boxed:`

`eta E_{j,b_*,eta}[ R(2b_*+R)/(b_*^2(b_*+R)^2) ]`

`=2/(1-b_*).`

Thus a failed scalar certificate is not amorphous. It produces an actual type `j_*`, conductance scale `b_*`, and tilted sibling law satisfying an exact balance between the explicit `(1-b)^2` killing and sensitivity to sibling conductance.

## 8. Strongest conclusion of this run

The infinite-dimensional pair transfer has been reduced, without approximation, to the regular positive operator

`(Tg)_j(b)=(1-b)^2 m_* q_j sum_i p_ij E[g_i(F_b(R_i))]`.

The `B=0` compactification boundary is strictly subcritical because it is exactly the old extinction Jacobian `J`; the `B=1` boundary is killed by `(1-b)^2`. An exponential weight converts the remaining one-step proof to one scalar support supremum `kappa(eta)`. If that scalar is below one for any admissible `eta`, the source-weighted second moment `E[B^2 tau^2]` is finite with an explicit geometric Green bound.

The only remaining issue in this route is **interior**, not boundary: prove the scalar inequality, or replace the one-step sup criterion by a weaker spectral/quasi-compact argument that can average over rare interior conductance states.

That distinction matters. The source lower-tail theorem and `rho(J)<1` have already eliminated escape to `B=0` as the obstruction to this weighted proof. If the scalar criterion fails, the next run should not return to pipe estimates; it should study the compact interior transfer and exploit the exact mass-loss identity of the pair kernel.

## 9. Honest status

- H0008 source: **OPEN / PARTIAL** in the canonical history.
- R7-07 ownership: **NONE / PENDING_ADMISSION** because the canonical claim-history path already exists and the installed protocol is create-only.
- R7-07 fixed source metric: **UNMEASURED -> UNMEASURED**; no stagnation count has started.
- New theorem-sized results in this artifact: exact square-conductance conjugation; exact exponential Lyapunov ratio; strict compactification-boundary gap; scalar sufficient certificate for `E[B^2 tau^2]<infinity`; convex `eta` variational formulas; interior conductance extremality equation.
- Full H0008 closure: **NOT CLAIMED**.
- Novelty: **UNVERIFIED**. The closest recovered one-type work remains Rousselin's regeneration/invariant-environment theory; the exact multitype conjugated two-spine criterion above has not been established as absent from all prior literature.

## 10. Next nonrepeating route if no lawful shard-6 source becomes claimable

Do **not** repeat B11/B24/B5 next run. The natural next triple is:

- **B1 CHANGE THE CATEGORY:** treat `T` as a renewal/transfer operator on the compactified variable `u=1/B`, with `R=0` the translation channel and `R>0` a reset channel;
- **B29 ADD THE POINTS AT INFINITY:** prove a Doeblin-Fortet / quasi-compact estimate on a weighted Lipschitz space whose boundary operator is `J`;
- **B13 FIND WHAT ONLY INCREASES / DECREASES:** use the exact two-spine mass-loss `Lambda_h(1)-Lambda_h P_2(1)=Lambda_h(Delta)` to exclude a peripheral unit eigenmeasure once quasi-compactness is available.

A successful implementation would be strictly weaker than requiring `kappa(eta)<1` pointwise and therefore has a realistic chance to close the interior gap left by this run.