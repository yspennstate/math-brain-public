Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** The prompt requested GPT-6 / maximum, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-routing receipt. **NO MOVEMENT: `d_SIC^contig: 28 -> 28`; I0098 target-specific unchanged streak `2 -> 3`. Formal HARD stuck protocol FIRED; recovery episode 1/2 is consumed. Section-B methods used: #19 MAKE IT AN ALGORITHM, #10 DERANDOMIZE, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# P03 / I0098 — d=29 one-seed projector propagation and the exact remaining arithmetic gate

Date: 2026-09-17 UTC.
Repository: `yspennstate/math-open-problems`, branch `master`.
Current exclusive claim: `operations/claims/I0098.md`, creation commit `8d79f25bb64122621849dc579166b0d097c02fb7`, blob `bdd93549f588d8aae00cae2545ff8225ed716bf7`.
Source: Afonso S. Bandeira, Randomstrasse 101, *Mutually Unbiased Bases, ETFs, and Zauner's Conjecture (problems 22--24)*, posted 2025-12-14, updated 2025-12-18, Conjecture 24.
Source target: for every dimension `d`, an ETF of `d^2` vectors exists in `C^d`, equivalently a SIC-POVM exists.
Broad status after this run: **OPEN / PARTIAL**.

Frozen metric:

`d_SIC^contig` = largest `D` for which a current primary/expert exact-SIC compilation reports exact solutions in every dimension `1 <= d <= D`.

Before: `28`.
After: `28`.
Movement: **NO**.
Target-specific unchanged streak: `2 -> 3`.
Stuck state: **FORMAL HARD STUCK PROTOCOL FIRED; recovery 1/2 consumed.**

The first checked exact-algebraic gap remains `d=29`. Numerical SICs, a conjectural ray-class identification, or a conditional Stark construction do not move this metric.

---

## 1. Continuity and repository gate

I continued from the actually newest complete P03 report, which is newer than the continuity anchor in the scheduler prompt:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T21-42-31Z__i0098-d29-ray-zauner-cyclic-280-bridge.md`

creation commit `805fba99bbc0cbfb3cfee7ef3410b20fc75abf0c`, blob `ba94d7033eb56d69b2c5e05cd0dfbb41b547d1b9`.

Exact-commit readback of that report recovered the first-line metric/state and the complete cyclic-280 theorem. I did not restart from the older `20-28-02Z` report.

Before the mathematics I reread the accessible repository continuity surfaces required by the fleet protocol: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; `FLEET_RULES.md`; `operations/FLEET_2026-09-16.md`; the controlling `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`; the current I0098 claim; targeted `RESULTS.md` / queue-history search; the newest own report; and the newest accessible P04/I0101 report for the directed audit duty. Large root/fleet surfaces are connector-bounded and some renderings are truncated, so this is an exact-path plus targeted-search reread, not a claim of byte-for-byte visual rereading of every oversized file.

I0126 remains immutable-handed-off and was not reopened. FEI, Salez I0111, Manhattan I0003, TH17, and I0074 were not resumed. Neighboring I0097/I0099/I0101 ownership was not touched.

---

## 2. Fresh source / status / prior-art check

### 2.1 Literal source still open

The Randomstrasse source still states Conjecture 24 literally:

> for each dimension `d`, there exists an ETF in `C^d` with `n=d^2` vectors.

It explicitly describes the Appleby--Flammia--Kopp Stark route as conditional and says an unconditional proof remains unavailable:

`https://randomstrasse101.math.ethz.ch/posts/FramesMUBZauner/`

Stefan Joka's arXiv:2601.13475 remains withdrawn at v5, revised 2026-05-31, with the explicit comment `The proof the paper gives is not correct`. It therefore does not close the source.

A fresh bounded search on 2026-09-17 UTC found no later unconditional all-dimensional proof and no source-valid nonexistence dimension. This is search evidence, not a proof of worldwide openness or publication novelty.

### 2.2 Exact d=29 gate remains live

The current exact-fiducial compilation hosted by Steven Flammia still lists exact dimensions through 28, then 30 and 31, with no d=29 row:

`https://www.physics.usyd.edu.au/~sflammia/SIC/`

Thus the operational contiguous exact metric remains 28.

Appleby--Chien--Flammia--Waldron's exactification method remains highly relevant prior art: it converts high-precision numerical SICs to exact algebraic ones using integer relations plus Galois symmetries, but it does not supply an exact d=29 certificate in the checked compilation.

### 2.3 Kopp's exact conditional construction identifies the right obstruction

Gene Kopp, *SIC-POVMs and the Stark conjectures*, arXiv:1807.05877, formulates Conjecture 5.1 for odd primes `d == 2 mod 3`. It predicts a Galois orbit of algebraic units in a ray class field with additional congruence, square-root, and projector conditions; Theorem 5.4 proves that such data produce a Heisenberg SIC. Kopp verifies the construction for d=5,11,17,23, and explicitly includes 29 in the proposed sequence, but not among the verified exact cases.

Crucially, Kopp distinguishes the Stark-unit conjecture from the extra SIC-specific conditions: points (2), (3), and (4) of Conjecture 5.1 are described as new predictions, and he explicitly suggests a p-adic route as potentially able to prove at least the local congruence condition (2). That statement is the nearest printed description of the d=29 obstruction I found.

The 2025 Appleby--Flammia--Kopp construction likewise proves an all-dimensional recipe only under two number-theoretic conjectures. Kopp--Lagarias arXiv:2407.08048 refines the SIC/ray-class-field predictions but labels the field correspondence conjectural.

### 2.4 Galois/centralizer overlap action is known as the relevant mechanism, not an unconditional d=29 theorem

The SIC literature records the conjectural Galois action on centered Weyl--Heisenberg SIC overlaps via a centralizer quotient `C/S`. In the prime `d == 2 mod 3` setting, the nontrivial overlaps are described as a single Galois orbit in the Stark-unit construction. This is exactly the structure exploited below.

I therefore label the new result as a **conditional structural reduction**. I do **not** promote the conjectural SIC-field/Galois action to a theorem about an existing d=29 SIC.

---

# 3. Idea before code

The previous P03 theorem identified two exact cyclic objects of size 280:

1. the ray-class relative group `Gal(E/H^+) ~= C_280` for `K=Q(sqrt(195))`; and
2. the Zauner centralizer quotient `Cent(Z)/<Z> ~= C_280`, acting regularly on the 280 nonzero displacement 3-orbits.

That still left an apparently huge exactification problem: 840 nonzero Weyl overlaps, or 280 Zauner-orbit values, plus all projector/idempotence equations.

The move this run is algorithmic and adversarial:

- **#19 MAKE IT AN ALGORITHM:** choose one explicit generator of the full nonzero phase-space orbit and ask how many projector equations are genuinely independent under a matching field automorphism.
- **#10 DERANDOMIZE:** replace unspecified cyclic action by one exact matrix `G=I+5Z` over `F_29`; no root ordering or numerical matching is used.
- **#30 ONE PRIME / ONE SCALE / ONE DIRECTION:** work only at `d=29` and only on the implication `one exact Galois-equivariant overlap seed -> exact rank-one SIC projector`.

The answer is much smaller than expected. Under the precise cyclic Galois-equivariance hypotheses predicted by the SIC arithmetic, **one nonzero scalar convolution equation** propagates to all 840 nonzero projector equations. The zero equation is automatic from the SIC modulus.

This does not construct the seed. It isolates exactly what the arithmetic side still has to provide.

---

# 4. Exact finite generator

Put

`p=29`,

`Z = [[0,-1],[1,-1]] mod 29 = [[0,28],[1,28]]`,

and define

`G = I + 5 Z = [[1,24],[5,25]] mod 29`.

The accompanying exact-arithmetic checker verifies:

- `ord(Z)=3`;
- `det(G)=21`, whose order in `F_29^x` is 28;
- `ord(G)=840`;
- `GZ=ZG`;
- `G^280=Z`;
- `G^420=-I`;
- `G^140=-Z^2`;
- the orbit of `e_1=(1,0)` under `G` contains all 840 nonzero vectors of `F_29^2` exactly once;
- the first 280 powers give representatives of 280 pairwise-disjoint Zauner 3-orbits covering all nonzero labels;
- the symplectic form scales by the determinant: `<Gu,Gv> = 21 <u,v>`.

Artifact:

`proofnet24/P03-fei/artifacts/2026-09-17/d29_one_seed_generator_check.py`

creation commit `c27a3c13993a25ed133f5988861bd31cf7fc9c36`, blob `f775a0a90e6a8db348cded8c887df057e78134e5`.

Executed exact output:

`proofnet24/P03-fei/artifacts/2026-09-17/d29_one_seed_generator_check.out`

creation commit `efb5ff0f871230d21da5ccb0eeb568095879415a`, blob `2a610ac3378292780b2c274980df51545ad64719`.

The archived output ends `ALL_EXACT_CHECKS_PASS True`.

The checker proves only the finite-field statements. It does not assume or certify existence of a SIC or of the Galois-equivariant algebraic seed below.

---

# 5. New theorem

## `P03-I0098-D29-ONE-SEED-IDEMPOTENCE-PROPAGATION-260`

**Status:** `PROVED / CONDITIONAL-STRUCTURAL-PARTIAL / KNOWN-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED`.

### Theorem 260 (one-seed cyclic projector certificate at d=29)

Let `d=29`. Let `tau` be a primitive 29th root used in a Weyl displacement convention

`D_u D_v = tau^{<u,v>} D_{u+v}`,

`D_u^dagger = D_{-u}`,

`Tr(D_u^dagger D_v)=29 delta_{u,v}`,

for labels `u,v in F_29^2`, with alternating form `<u,v>`.

Let

`Z=[[0,-1],[1,-1]]`,

`G=I+5Z=[[1,24],[5,25]] mod 29`.

Suppose `L` is a complex number field containing `tau`, `beta in L`, and an automorphism `rho in Aut(L)` such that:

1. `rho(tau)=tau^21`;
2. `rho^280(beta)=beta`;
3. complex conjugation commutes with `rho` on the orbit of `beta` and
   `rho^140(beta)=conj(beta)`;
4. `beta conj(beta)=1/30`.

Define coefficients `b_u` as follows:

`b_0=1`,

and for the unique `m in {0,...,839}` satisfying

`u=G^m e_1`,

put

`b_u = rho^{m mod 280}(beta)`.

This is Zauner-invariant because `G^280=Z`.

Define

`Pi = (1/29) sum_{u in F_29^2} b_u D_u`.

For `w in F_29^2` define the idempotence defect

`E_w = sum_u tau^{<u,w>} b_u b_{w-u} - 29 b_w`.

If the **single** nonzero equation

`E_{e_1}=0`

holds, then:

1. `E_w=0` for every `w in F_29^2`;
2. `Pi^2=Pi`;
3. `Pi=Pi^dagger` and `Tr(Pi)=1`, hence `Pi` is a rank-one orthogonal projector;
4. for every nonzero `u`,

   `|Tr(D_u^dagger Pi)|^2 = |b_u|^2 = 1/30`;

5. therefore `Pi` is a Weyl--Heisenberg SIC fiducial projector in dimension 29.

If the arithmetic Artin convention produces `rho(tau)=tau^(21^{-1})` rather than `tau^21`, replace `G` by `G^{-1}`. The theorem is unchanged.

### Proof

#### Step 1. The coefficient assignment is well-defined and Zauner invariant

The exact finite check gives `ord(G)=840`, and `G` acts transitively and freely on the 840 nonzero vectors. Hence every `u != 0` has a unique representation

`u=G^m e_1`, `0 <= m < 840`.

So `b_u` is well-defined.

Since `G^280=Z`,

`b_{Zu}=b_{G^{m+280}e_1}=rho^{(m+280) mod 280}(beta)=b_u`.

Thus the coefficients are constant on the 280 Zauner 3-orbits.

#### Step 2. Hermitian symmetry and SIC modulus

The exact finite relation `G^420=-I` gives

`-u=G^{m+420}e_1`.

Modulo 280 this advances the `rho` exponent by 140. Therefore

`b_{-u}=rho^{m+140}(beta)`.

By hypothesis `rho^140(beta)=conj(beta)` and conjugation commutes with `rho` on this orbit, hence

`b_{-u}=conj(rho^m(beta))=conj(b_u)`.

Also every nonzero coefficient has the same norm:

`b_u conj(b_u)=rho^m(beta conj(beta))=1/30`.

(The rational number `1/30` is fixed by every field automorphism.)

#### Step 3. Weyl expansion turns idempotence into the defects `E_w`

Orthogonality of the 841 displacement operators gives the expansion formula

`A=(1/29) sum_u Tr(D_u^dagger A) D_u`.

Using `D_uD_v=tau^{<u,v>}D_{u+v}`,

`Pi^2 = (1/29^2) sum_w [sum_u tau^{<u,w-u>} b_u b_{w-u}] D_w`.

Because the form is alternating, `<u,u>=0`, so

`<u,w-u>=<u,w>`.

Hence `Pi^2=Pi` is equivalent coefficient-by-coefficient to

`E_w=0`

for all `w`.

#### Step 4. The defects form one exact Galois orbit

For a 2 by 2 matrix over a field, the alternating form obeys

`<Gu,Gw>=det(G)<u,w>`.

Here `det(G)=21`. Therefore, using `rho(tau)=tau^21` and `rho(b_u)=b_{Gu}`,

`rho(E_w)`

`= sum_u tau^{21<u,w>} b_{Gu} b_{G(w-u)} - 29 b_{Gw}`

`= sum_u tau^{<Gu,Gw>} b_{Gu} b_{Gw-Gu} - 29 b_{Gw}`.

Reindexing `u'=Gu` gives

`rho(E_w)=E_{Gw}`.

Since `G` is transitive on all 840 nonzero labels, `E_{e_1}=0` implies

`E_w=0`

for every nonzero `w`.

This is the central reduction: 840 nonzero projector equations collapse to one scalar equation under exact cyclic equivariance.

#### Step 5. The zero defect is automatic

For `w=0`,

`E_0 = sum_u b_u b_{-u} - 29`.

The zero term contributes `b_0^2=1`. Each of the 840 nonzero terms contributes `1/30`. Thus

`E_0 = 1 + 840/30 - 29 = 1+28-29=0`.

So the single nonzero equation indeed forces **all** idempotence equations.

#### Step 6. Rank-one SIC projector

From `b_{-u}=conj(b_u)` and `D_u^dagger=D_{-u}`, the Weyl expansion gives

`Pi^dagger=Pi`.

Only `D_0=I` has nonzero trace, and `Tr(I)=29`, so

`Tr(Pi)=b_0=1`.

We have already proved `Pi^2=Pi`. A Hermitian idempotent has eigenvalues in `{0,1}`; trace one therefore forces rank exactly one. Hence

`Pi=|psi><psi|`

for a unit vector `psi`.

Finally, orthogonality of the Weyl basis gives

`Tr(D_u^dagger Pi)=b_u`.

For every nonzero `u`,

`|b_u|^2=1/30=1/(d+1)`.

Therefore the Weyl--Heisenberg orbit of `psi` consists of `29^2` equiangular lines with the SIC overlap modulus, i.e. it is a SIC-POVM. QED.

---

## 6. What this theorem changes

It does **not** move `d_SIC^contig`, because it assumes the arithmetic seed/equivariance whose existence is the hard part.

It does, however, sharpen the exactification problem in a way the previous cyclic-280 bridge did not:

- one need not recover 29 unrelated coordinates;
- one need not separately certify 280 orbit values;
- and, under the predicted cyclic Galois action, one need not check 840 nonzero matrix-idempotence coefficients.

A single exact seed `beta`, its cyclic field action, the norm/conjugation constraints, and **one scalar convolution identity** suffice to recover the entire rank-one projector.

This also removes an apparent extra obligation in Kopp's condition (4): once the exact Weyl expansion is Hermitian, trace one, and idempotent, rank one is automatic. There is no need for a separate collection of rank-two-minor checks.

The theorem is best read as an exact certificate format for the d=29 arithmetic construction, not as an existence proof.

---

# 7. Why the natural stronger claims fail

## 7.1 The cyclic-280 group is not itself a SIC

The previous theorem proved an exact isomorphism between an arithmetic cyclic quotient and the Zauner-orbit torsor. Group structure alone supplies no algebraic overlap seed. There are many abstract `C_280`-torsors and almost none satisfy the nonlinear Weyl projector equation.

## 7.2 High-precision root ordering is not a proof

A numerical d=29 fiducial or a guessed minimal polynomial could suggest `beta`, but neither establishes that the guessed algebraic number has the required Artin action, the required square-root signs, or the exact scalar convolution identity. No PSLQ-only step moves the metric.

## 7.3 The one-seed theorem is an implication, not an existence result

The theorem intentionally assumes the SIC-dependent Galois/cyclotomic equivariance. The known arithmetic literature predicts this action in the centered ray-class setting, but the d=29 exact object is not already available to instantiate it.

## 7.4 The broad Stark route remains conditional

Appleby--Flammia--Kopp give an all-dimensional construction assuming number-theoretic conjectures. Kopp's older prime-`2 mod 3` route similarly isolates explicit extra conditions. Importing either conditional construction as unconditional would be circular relative to the Randomstrasse source.

---

# 8. Formal HARD stuck-thinking protocol

The unchanged streak has reached three. This section is therefore mandatory, and **recovery episode 1/2 is consumed by this run**.

## 8.1 Exact blocking formula

After Claims 256, 258, and 260, the d=29 WH/Zauner/ray-class route has been reduced to the following exact gate.

Find an algebraic seed `beta` in an appropriate d=29 SIC/ray field and an automorphism `rho` such that

`rho(tau)=tau^21`,

`rho^280(beta)=beta`,

`rho^140(beta)=conj(beta)`,

`beta conj(beta)=1/30`,

and

`boxed( sum_u tau^{<u,e_1>} b_u b_{e_1-u} = 29 beta )`,

where `b_{G^m e_1}=rho^{m mod 280}(beta)` and `G=I+5Z`.

Everything after this scalar identity is now rigorous linear algebra.

Equivalently, in Kopp's language the remaining work is not the formal projector reconstruction but the exact existence of the requisite Stark/ray-unit orbit, square-root/sign data, and enough of Conjecture 5.1 to produce the seed and its one surviving nonlinear identity.

## 8.2 Routes tried and precise failure reasons

1. **Zauner orbit reduction (Claim 256).** Reduced 840 labels to 280 orbits and gave an exact nonnegative SIC defect, but did not construct an algebraic zero of the defect.

2. **Ray-class / centralizer cyclic bridge (Claim 258).** Proved the arithmetic and finite-symmetry `C_280` quotients are the same quadratic-residue quotient, but an isomorphism of torsors does not produce the SIC overlap function.

3. **One-seed algorithmic propagation (Claim 260, this run).** Collapses the entire projector verification to one seed and one scalar identity under cyclic equivariance, but still assumes existence of the seed/equivariance.

4. **Numerical/exactification shortcut.** Rejected as a proof route: high precision plus PSLQ does not establish the conjectural field, Artin action, sign choice, or exact projector identity.

5. **Conditional all-dimensional Stark construction.** Cannot close the literal source because its number-theoretic hypotheses remain conjectural.

The recurring obstruction is therefore stable: **field/group structure is under control; existence of the special algebraic unit/overlap satisfying the SIC-specific local and nonlinear conditions is not.**

## 8.3 What a proof must add

A successful next step must create algebraic content, not another symmetry reduction. At minimum it must prove one genuinely new d=29 piece of Kopp Conjecture 5.1, or an equivalent exact local/global condition, from unconditional number theory.

The most actionable candidate is the local congruence/square-root gate at the unique prime over 29. Kopp himself notes that a p-adic formulation may be amenable to proving his condition (2). If that local condition can be proved for the d=29 Stark special values, the exactification search loses one of its conjectural sign/root choices before any global projector calculation.

## 8.4 Simplest unproved special case

The smallest source-relevant special case is now:

> **d=29, Weyl--Heisenberg covariant, centered Zauner-symmetric minimal-multiplet SIC:** construct one exact algebraic overlap seed `beta` with the cyclic Artin action above and prove the single scalar projector identity.

This is much narrower than Zauner's all-dimensional conjecture while still sufficient to move the frozen contiguous exact metric from 28 at least to 31, because exact 30 and 31 solutions are already listed.

## 8.5 Nearest solved analogue

Kopp's construction is explicitly carried out in prime dimensions 5, 11, 17, and 23, with the first exact d=23 solution supplied there. Those are the nearest solved prime-`2 mod 3` analogues. The current exact compilation's next gap is 29.

The d=23 computation is therefore the direct model to cannibalize, but only its **proof-relevant arithmetic mechanism**, not its numerical lattice-reduction workflow, should be imported.

## 8.6 Exactly one recovery action

**Recovery action 2/2 for the next run:** attack the d=29 **local p-adic/congruence and square-root portion of Kopp Conjecture 5.1**, before attempting any global Stark exactification.

The next run should use one coherent triple:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** prove an unconditional d=29 local ray-unit congruence/square-root lemma even if the global Stark unit remains conjectural;
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** start from Kopp's explicit statement that conditions (2)--(4) are new predictions and that condition (2) may be p-adically approachable;
- **#26 HUNT THE SPORADIC CASE:** exploit the concrete local arithmetic of the unique prime over 29 and determine whether d=29 has an exceptional obstruction absent at 23.

If that final recovery leaves `d_SIC^contig=28`, P03 must write a complete immutable I0098 HARD handoff and rotate. **No third I0098 recovery is permitted.**

---

# 9. Directed P04/I0101 independent audit

I audited a new P04 claim not previously audited by P03:

`P04-I0101-FRACTIONAL-1FACTOR-KKT-DUAL-31`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T21-42-30Z__run-report.md`,

creation commit `7a9d21ef8aba9f27f3f5b3d114b8ad8047fd5f22`, blob `794a7d54e7be60efa252bd92b99b50c7605d90ba`.

### Audited statement

For a graph `K` with nonempty fractional perfect-matching polytope `F(K)`, define the symmetric stochastic zero-diagonal matrix `P(w)` from edge weights and

`mu(K)=max_{w in F(K)} lambda_min(P(w))`.

The peer claim gives the exact minimax/LP dual

`mu(K)=min { sum_i y_i : X>=0, tr X=1, y_i+y_j >= 2 X_ij on every edge }`,

together with KKT relations, a centered Gram formulation, tightness on active edges, active-4-cycle orthogonality, and half-integral extreme fractional 1-factors.

### Independent derivation

For every symmetric `P`,

`lambda_min(P)=min_{X>=0,tr X=1} <X,P>`.

The fractional 1-factor polytope and the density-matrix set are compact convex, and the objective is bilinear, so Sion minimax applies:

`max_w min_X <X,P(w)> = min_X max_w <X,P(w)>`.

For fixed `X`,

`<X,P(w)>=2 sum_{ij in E} X_ij w_ij`.

The primal LP has equality degree constraints `sum_{e incident i}w_e=1` and `w_e>=0`, so its dual vertex potentials are free and satisfy

`y_i+y_j >= 2 X_ij`,

with objective `min sum_i y_i`. This gives the claimed dual exactly.

At a saddle point, `P(w*)-mu I` and `X*` are PSD and have zero trace pairing, so `(P(w*)-mu I)X*=0`. Ordinary LP complementary slackness gives the active-edge equality. Because `P(w*)` is stochastic, `1` is an eigenvalue; because it has zero diagonal, its trace is zero and hence its minimum eigenvalue is <=0 for nontrivial `K`. Thus the minimum-eigenspace is orthogonal to the stationary vector and `X* 1=0`.

Writing `X_ij=<v_i,v_j>` and `a_i=||v_i||^2-y_i` converts the edge dual constraint exactly to

`||v_i-v_j||^2 >= a_i+a_j`,

while `sum y_i=1-sum a_i`. Tightness around an active 4-cycle yields, by alternating the four equalities,

`<v_i-v_k, v_j-v_l>=0`.

Finally, the classical extreme-point characterization of the fractional perfect-matching polytope gives half-integral components: isolated edges of weight 1 and odd cycles of weight 1/2. A linear objective admits an extreme optimum.

I found no algebraic gap in the claim-scoped theorem.

### Verdict

`P03-AUDIT-P04-I0101-FRACTIONAL-1FACTOR-KKT-DUAL-261 = PASS (CLAIM-SCOPED)`.

This verdict does **not** prove P04's Randomstrasse Conjecture 27 and does not audit later consequences beyond the stated minimax/KKT/fractional-factor theorem.

---

# 10. Cumulative I0098 claim ledger

- `P03-I0098-D29-ZAUNER-280-ORBIT-REDUCTION-256` — **PROVED / STRUCTURAL-PARTIAL / KNOWN-MECHANISM / NO-NOVELTY-CLAIM**. Exact d=29 Zauner orbit count, SIC overlap defect, symmetry-restricted search reduction.
- `P03-I0098-D29-RAY-ZAUNER-CYCLIC-280-BRIDGE-258` — **PROVED / STRUCTURAL-PARTIAL / KNOWN-ARITHMETIC-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED**. Exact `C_280` ray-kernel/centralizer identification; does not prove SIC-field equality.
- `P03-I0098-D29-ONE-SEED-IDEMPOTENCE-PROPAGATION-260` — **PROVED / CONDITIONAL-STRUCTURAL-PARTIAL / KNOWN-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED**. Under exact cyclic Galois/cyclotomic seed hypotheses, one scalar nonzero Weyl convolution equation forces the full rank-one SIC projector.
- Broad Randomstrasse Conjecture 24 — **OPEN / PARTIAL**.
- `d_SIC^contig` — **28**, unchanged.
- Formal HARD recovery state — **stuck fired; recovery 1/2 consumed**.

---

# 11. Exact remaining obligation and next state

The exact remaining d=29 obligation is no longer “find 29 coordinates” or “solve 840 equations.” It is:

1. construct or certify the appropriate algebraic seed orbit unconditionally;
2. prove the required local congruence/square-root/Galois compatibility;
3. verify the one surviving scalar projector identity;
4. instantiate Theorem 260 to obtain an exact rank-one SIC projector.

The next run is the **second and final permitted HARD recovery episode** for I0098. It must spend its substantive effort on the local p-adic/congruence gate above. If the metric remains 28, it must complete an immutable I0098 handoff and rotate in the same run; there is no third recovery.

---

# 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  claim: I0098
  source: Afonso S. Bandeira, Randomstrasse 101 (2025), Conjecture 24 / Zauner SIC existence
  status: OPEN_PARTIAL
  metric:
    name: d_SIC^contig
    before: 28
    after: 28
    movement: NO
    unchanged_streak: 3
  stuck_state:
    formal_hard_protocol: FIRED
    recovery_consumed: 1_of_2
    next_run: FINAL_RECOVERY_2_OF_2
  new_claim:
    id: P03-I0098-D29-ONE-SEED-IDEMPOTENCE-PROPAGATION-260
    verdict: PROVED_CONDITIONAL_STRUCTURAL_PARTIAL_KNOWN_MECHANISM_PUBLICATION_NOVELTY_UNVERIFIED
    statement: Under an exact cyclic d=29 Galois/cyclotomic overlap-seed action compatible with G=I+5Z, the entire WH projector idempotence system propagates from one nonzero scalar convolution identity; the zero equation is automatic, and Hermitian trace-one idempotence gives a rank-one SIC projector.
  exact_artifacts:
    checker_path: proofnet24/P03-fei/artifacts/2026-09-17/d29_one_seed_generator_check.py
    checker_creation_commit: c27a3c13993a25ed133f5988861bd31cf7fc9c36
    checker_blob: f775a0a90e6a8db348cded8c887df057e78134e5
    output_path: proofnet24/P03-fei/artifacts/2026-09-17/d29_one_seed_generator_check.out
    output_creation_commit: efb5ff0f871230d21da5ccb0eeb568095879415a
    output_blob: 2a610ac3378292780b2c274980df51545ad64719
    output_terminal: ALL_EXACT_CHECKS_PASS True
  directed_peer_audit:
    id: P03-AUDIT-P04-I0101-FRACTIONAL-1FACTOR-KKT-DUAL-261
    verdict: PASS_CLAIM_SCOPED
    peer_claim: P04-I0101-FRACTIONAL-1FACTOR-KKT-DUAL-31
    peer_report: proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T21-42-30Z__run-report.md
    peer_creation_commit: 7a9d21ef8aba9f27f3f5b3d114b8ad8047fd5f22
    peer_blob: 794a7d54e7be60efa252bd92b99b50c7605d90ba
  next_action: Final I0098 HARD recovery: prove/refute the d=29 local p-adic congruence/square-root portion of Kopp Conjecture 5.1; if d_SIC^contig stays 28, immutable handoff and rotate, no third recovery.
  shared_root_edits: NONE_P26_ONLY
```

No shared root ledger, peer file, workflow, permission, schedule count, Gmail, Drive, public post, paid compute, or external script was modified in this run.

**End of complete run report.**
