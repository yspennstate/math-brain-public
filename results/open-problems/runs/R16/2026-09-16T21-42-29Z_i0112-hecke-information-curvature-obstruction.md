Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no model selector, no reasoning-effort selector, and no authenticated telemetry establishing GPT-6/maximum. **NO MOVEMENT:** `W_exp = 1/2 provisional -> 1/2 provisional`, unchanged count `2`. Methods actually tried: **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: **R16 / I0112 — Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.3: prove that every bounded-degree vertex-transitive expander sequence exhibits total-variation cutoff.** Status: **PARTIAL**.

# R16 — exact Hecke information lift; negative-curvature obstruction to the naive group/curvature route

Run ID: `2026-09-16T21-42-29Z_i0112-hecke-information-curvature-obstruction`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and mandatory state recovery

I did not restart Beck--Fiala or reset R16. Before doing mathematics I recovered/searched:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical ownership `operations/claims/I0112.md`;
- the newest complete own report `runs/R16/2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction.md`;
- the preceding synchronous-tensor report `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`;
- the current neighboring Salez report `runs/R01/20260916T2059Z_i0113_path_entropy_02.md`;
- the current R12 state: its newest located file is the I0102 handoff / I0060 claim `runs/R12/2026-09-16T20-33-03Z_i0102_handoff_i0060_claim_4b71c2.md`, not a complete I0060 proof package.

The intake corpus is too large for a literal full rendering in one connector response. I searched the exact I0112 source/claim and neighboring Salez entries and recovered the canonical intake hit; I do not claim a byte-for-byte semantic reread of all roughly 780 rows.

### Frozen metric

The canonical metric remains

\[
W_{\exp}:=\inf\Bigl\{w:\text{R16 certifies a new source-admissible family with cutoff window }O((\log|V|)^w)\Bigr\}.
\]

The synchronous direct-square theorem from the 19:48 report gives `W_exp=1/2` provisionally, pending prior-art/class clearance and the two required outside audits. The 20:45 report proved that `1/2` is an absolute floor for any cutoff family of bounded-degree expanders, so this metric cannot numerically improve. I therefore do not rename a reduction as metric movement.

## 2. Dated source and literature refresh — 16 September 2026

### Originating Beck--Fiala source

The originating Beck--Fiala assignment remains literature-`KNOWN`, not reopened.

- Bansal--Jiang, arXiv:2508.03961v2 (last revised 9 Sep 2025), explicitly proves the conjectured `O(sqrt(t))` order only for `t >= log^2 n`, and gives a polylogarithmically weakened bound below that range.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), still explicitly states the stronger Komlos theorem and the all-`t` Beck--Fiala corollary
  \[
  \operatorname{disc}(A)<3\sqrt{2\pi t}\qquad(t\ge1).
  \]
  The current arXiv search still shows v1; a bounded current search found no withdrawal, v2 correction, or proof-specific rebuttal. This is a fresh literature claim only six days old, not mature referee validation.

So Bansal--Jiang's dense regime is only a baseline, while the current primary preprint claim directly covers the full original existential target. R16 continues its canonical successor rather than duplicating R13/Komlos.

### I0112 / cutoff source

Salez's notes remain v1 (28 Aug 2025). The corresponding primary 2023 varentropy paper states explicitly:

> all vertex-transitive expanders exhibit cutoff

as Conjecture 1, and proves that for sparse expander chains cutoff is equivalent to the varentropy criterion. In particular, for graph expanders the unresolved problem is reduced to showing information-content fluctuations are `o((log |V|)^2)` at mixing time.

Fresh later-work checks:

1. Dylan J. Altschuler, arXiv:2609.14945 (14 Sep 2026), proves Gaussian-profile cutoff for every fixed-degree **long-range expander** and explicitly describes this as intermediate progress toward the transitive spectral-expander conjecture.
2. Pedrotti--Salez, arXiv:2607.05345, gives window control via the non-equilibrium/local Poincare constant `gamma_*`, with the easy lower bound `gamma_* >= kappa` from Bakry--Emery curvature for deterministic starts.
3. Hermon--Huang--Pedrotti--Salez, arXiv:2409.16869, proves dimension-free information concentration for **conjugacy-invariant** group walks; its abstract explicitly identifies non-negative Bakry--Emery curvature as a key ingredient.
4. Bounded searches for `varentropy homogeneous space`, `Hecke random walk varentropy`, `Schreier graph varentropy cutoff`, and `vertex-transitive varentropy coset` did not locate a theorem that extends the Hermon--Huang--Pedrotti--Salez result to arbitrary stabilizer-bi-invariant walks. This negative search is not a novelty certificate.

## 3. Method #14 + #3: exact information-preserving Hecke lift

The natural group language is stronger than a bare statement that a vertex-transitive graph is a Schreier graph: one can lift simple random walk to a symmetric group convolution **without changing the information-content random variable at all**.

### R16-I0112-C08 — information-preserving group lift

**STATUS: PROVED. The Schreier/Hecke viewpoint is standard; no novelty claim is made for the representation. The exact information-law identity is written out because it is the statistic needed by Salez's criterion.**

Let `X=(V,E)` be a finite connected undirected vertex-transitive `d`-regular graph with `d>=1`. Let `Gamma <= Aut(X)` be any finite subgroup acting transitively on `V`, fix `o in V`, and let

\[
H:=\operatorname{Stab}_{\Gamma}(o).
\]

Identify `V` with the right-coset space `Gamma/H` via `gH -> g o`. Define the orbital step set

\[
R:=\{g\in\Gamma:g o\sim o\}.
\tag{C08.1}
\]

Let `mu` be the uniform probability measure on `R`.

Then:

1. `R` is symmetric and `H`-bi-invariant:
   \[
   R^{-1}=R,\qquad HRH=R.
   \tag{C08.2}
   \]
2. `R` is the disjoint union of exactly `d` right `H`-cosets, hence
   \[
   |R|=d|H|.
   \tag{C08.3}
   \]
3. `R` generates `Gamma`.
4. If `U` is uniform on `H`, `N_t~Pois(t)`, and `W_1,W_2,...` are iid with law `mu`, independent of `U,N_t`, then
   \[
   Y_t:=U W_1\cdots W_{N_t}
   \tag{C08.4}
   \]
   is a reversible continuous-time convolution walk on `Gamma`, and
   \[
   Z_t:=Y_t o
   \tag{C08.5}
   \]
   is **exactly** continuous-time simple random walk on `X`, started from `o`, in the convention generator `P-I`.
5. Let `q_t` be the law of `Y_t` and `p_t` the law of `Z_t`. Then `q_t` is right-`H`-invariant and
   \[
   p_t(g o)=|H|q_t(g).
   \tag{C08.6}
   \]
   Since `|Gamma|=|V||H|`, the information contents relative to the uniform laws agree pointwise:
   \[
   \boxed{
   \log\bigl(|\Gamma|q_t(Y_t)\bigr)
   =
   \log\bigl(|V|p_t(Z_t)\bigr)
   \quad\text{a.s.}
   }
   \tag{C08.7}
   \]
   In particular, the complete law of the information content, all of its moments whenever finite, relative entropy, and varentropy are identical upstairs and downstairs.

### Proof

If `h_1,h_2 in H` and `r in R`, then

\[
(h_1 r h_2)o=h_1(ro),
\]

and `h_1` fixes `o` while permuting its neighbors, so `h_1rh_2 in R`. Hence `HRH=R`. If `ro~o`, applying the graph automorphism `r^{-1}` gives `r^{-1}o~o`, so `R^{-1}=R`.

For each neighbor `x~o`, the fiber

\[
\{r\in\Gamma:ro=x\}
\]

is one right coset of `H`, of cardinality `|H|`. There are exactly `d` neighbors. This proves (C08.3), and also shows that `Wo` is uniform on the `d` neighbors of `o` when `W~mu`.

To see that `R` generates `Gamma`, first note that `H` is generated by products of two elements of `R`: choose any `r in R`; for any `h in H`, right-`H`-invariance gives `rh in R` and symmetry gives `r^{-1} in R`, so

\[
h=r^{-1}(rh)\in\langle R\rangle.
\]

Now take any `g in Gamma`. Because `X` is connected, choose a graph path from `o` to `g o`. At each step, after transporting back to `o`, choose an element of `R` realizing that neighbor move. Thus some product `s in <R>` satisfies `s o=g o`. Hence `s^{-1}g in H <= <R>`, so `g in <R>`.

The measure `mu` is symmetric, so the convolution chain is reversible with respect to uniform measure on `Gamma`. Conditional on the current group element `g`, the next projected jump is

\[
g o\longmapsto g W o,
\]

and `Wo` is uniform on the neighbors of `o`; applying the automorphism `g` makes `gWo` uniform on the neighbors of `go`. With a rate-one Poisson jump clock, this is precisely continuous-time simple random walk on `X`.

The initial law `U_H` is right-`H`-invariant, and `mu` is right-`H`-invariant, so every `q_t` is right-`H`-invariant. Therefore for the coset corresponding to `go`,

\[
p_t(go)=\sum_{h\in H}q_t(gh)=|H|q_t(g).
\]

Finally `|Gamma|=|V||H|` by orbit-stabilizer, so

\[
|\Gamma|q_t(g)=|V|p_t(go).
\]

Evaluating at `g=Y_t` gives (C08.7). QED.

### Why this is useful

Method **#14 FIND THE GROUP ACTING** therefore gives an exact target class: source vertex-transitive walks are precisely represented by symmetric **`H`-bi-invariant orbital convolution walks**, with the relevant information statistic unchanged. This is stronger than merely transferring cutoff or spectrum.

Method **#3 PROVE SOMETHING STRONGER** was used literally: rather than seek only a varentropy inequality, C08 preserves the entire information-content distribution.

## 4. R16-I0112-C09 — exact reformulation of Salez's missing estimate

**STATUS: PROVED CONDITIONAL REDUCTION from C08 plus Salez's published expander criterion. It does not solve Problem 2.3.**

Let `(X_n)` be a source-admissible sequence of bounded-degree vertex-transitive expanders, let `(Gamma_n,H_n,mu_n)` be the C08 lifts, and let `q_{n,t}` denote the lifted law started from uniform `H_n`. Write `N_n=|X_n|=|Gamma_n/H_n|`.

Salez's Theorem 2 / Corollary 2 for sparse expanders says that cutoff is equivalent to the varentropy criterion; in this graph setting it is enough and necessary to have, for every fixed `epsilon in (0,1)`,

\[
V_{\rm KL}^{(n)}(t_{\rm mix}^{(n)}(\epsilon))
=o((\log N_n)^2).
\tag{C09.1}
\]

By C08.7, the quotient varentropy equals exactly

\[
\operatorname{Var}\left[
\log\bigl(|\Gamma_n|q_{n,t}(Y_{n,t})\bigr)
\right].
\]

Hence Salez Problem 2.3 is equivalent to the following **Hecke-information statement**:

\[
\boxed{
\operatorname{Var}\left[
\log\bigl(|\Gamma_n|q_{n,t_n}(Y_{n,t_n})\bigr)
\right]
=o\!\left(\log^2|\Gamma_n/H_n|\right)
}
\tag{C09.2}
\]

at each fixed-accuracy quotient mixing time `t_n`, for every symmetric orbital measure `mu_n` arising above with uniformly bounded quotient degree and uniformly positive quotient spectral gap.

This isolates exactly what the group method must prove. The relevant invariance is **bi-invariance under a stabilizer**, not conjugacy-invariance under the whole group.

## 5. Why the existing conjugacy-invariant group theorem does not directly solve C09

Hermon--Huang--Pedrotti--Salez prove a dimension-free varentropy bound for **conjugacy-invariant** random walks on groups. Their abstract states both that hypothesis and that non-negative Bakry--Emery curvature is a key ingredient. C08 only gives

\[
H\mu H=\mu,
\]

which is generally far weaker than

\[
g\mu g^{-1}=\mu\quad\forall g\in\Gamma.
\]

There is also a quantitative support-size obstruction to a naive black-box application: C08 has

\[
|\operatorname{supp}\mu|=d|H|,
\]

and `|H|` need not be uniformly bounded even when quotient degree `d` is. Thus a theorem whose generic bound scales with the number of group generators/support atoms does not automatically become a dimension-free quotient bound.

The next subsection shows that the curvature ingredient itself genuinely fails on classical source-positive examples, rather than merely being missing from the representation.

## 6. Method #20 — exact negative-curvature witness on tree-like transitive graphs

### R16-I0112-C10 — girth at least five forces a negative Bakry--Emery test direction

**STATUS: PROVED. This is an explicit route obstruction. The general fact that regular trees/locally tree-like graphs have negative discrete curvature is part of the graph-curvature literature; no novelty claim is made for the phenomenon. The exact normalized test calculation below is self-contained.**

Let `G` be a finite `d`-regular graph, `d>=3`, and let `o` be a vertex whose radius-two neighborhood has the tree structure guaranteed by girth at least five. Let

\[
L=P-I
\]

be the normalized continuous-time random-walk generator. Define the carré du champ convention

\[
2\Gamma(f,g)=L(fg)-fLg-gLf,
\]

and

\[
\Gamma_2(f)=\frac12L\Gamma(f)-\Gamma(f,Lf).
\]

Then the Bakry--Emery curvature at `o` satisfies

\[
\boxed{
\kappa_{BE}(o)\le -\frac{d-2}{d}<0.
}
\tag{C10.1}
\]

### Proof

Let `v_1,...,v_d` be the neighbors of `o`. Choose real numbers `a_1,...,a_d`, not all zero, such that

\[
\sum_{i=1}^d a_i=0,
\qquad
S_2:=\sum_{i=1}^d a_i^2>0.
\]

Set

\[
f(o)=0,\qquad f(v_i)=a_i.
\]

Because the girth is at least five, the `d-1` neighbors of `v_i` other than `o` are distinct from the first shell and from the corresponding second-shell vertices of every other `v_j`. Assign

\[
f(w)=2a_i
\]

for each such second-shell neighbor `w` of `v_i`. Values outside the radius-two ball are irrelevant.

At `o`,

\[
Lf(o)=\frac1d\sum_i a_i=0,
\]

and

\[
\Gamma(f)(o)
=\frac1{2d}\sum_i a_i^2
=\frac{S_2}{2d}.
\tag{C10.2}
\]

At `v_i`, all `d-1` outward differences equal `a_i`, while the edge back to `o` also has squared difference `a_i^2`. Hence

\[
\Gamma(f)(v_i)=\frac{a_i^2}{2}.
\tag{C10.3}
\]

Also

\[
Lf(v_i)
=\frac{(d-1)2a_i}{d}-a_i
=\frac{d-2}{d}a_i.
\tag{C10.4}
\]

Therefore

\[
L\Gamma(f)(o)
=\frac1d\sum_i\frac{a_i^2}{2}-\frac{S_2}{2d}
=0,
\]

while the bilinear edge formula gives

\[
\Gamma(f,Lf)(o)
=\frac1{2d}\sum_i
 a_i\left(\frac{d-2}{d}a_i\right)
=\frac{d-2}{2d^2}S_2.
\]

Thus

\[
\Gamma_2(f)(o)
=-\frac{d-2}{2d^2}S_2
=-\frac{d-2}{d}\Gamma(f)(o).
\]

Any curvature lower bound `kappa` satisfying `Gamma_2 >= kappa Gamma` for all test functions must therefore obey (C10.1). QED.

### Consequence for the attempted general proof

High-girth fixed-degree vertex-transitive expanders are not exotic counterexamples: Ramanujan families of Lubotzky--Phillips--Sarnak type have logarithmic girth, and Altschuler's current paper explicitly lists such high-girth Ramanujan examples while proving cutoff for the larger long-range class. Thus for all large members of such a family, C10 supplies a **uniformly negative** Bakry--Emery direction even though cutoff is known.

Therefore the direct strategy

\[
\text{vertex transitivity + spectral expansion}
\Longrightarrow \kappa_{BE}\ge0
\Longrightarrow \gamma_*\gtrsim1
\Longrightarrow \text{cutoff}
\]

is impossible. Transitivity does **not** force the non-negative curvature that powers the easy Hermon--Huang--Pedrotti--Salez / Pedrotti--Salez route.

This was Method **#20 FIND WHY THE ALGORITHM FAILS**: the failure is an exact local witness, not merely the absence of a proof.

## 7. Synthesis: what a successful group proof must contain

C08--C10 sharpen the source obstruction substantially.

The source conjecture is not asking for another Cayley theorem. Every transitive graph can be lifted without information loss, but the resulting step law has only stabilizer bi-invariance. A successful universal group-level argument must therefore exploit the pair `(Gamma,H)` in a way that survives:

1. potentially enormous stabilizers `H`;
2. non-normal generating orbitals;
3. negative ordinary Bakry--Emery curvature on high-girth positive examples;
4. absence of whole-group conjugacy invariance.

The natural algebra is the `H`-bi-invariant / Hecke algebra rather than the ordinary center of the group algebra. But a general Hecke algebra need not be commutative (the pair need not be a Gelfand pair), so the abelian/conjugacy-invariant tensorization mechanism cannot simply be renamed.

A plausible next target is therefore a **quotient-sensitive information inequality** whose constant depends on quotient degree and spectral expansion, but not on `|H|` or the number `d|H|` of group-level support atoms.

## 8. Metric / stuck status

There is no honest numerical movement:

\[
W_{\exp}:\quad \frac12\text{ provisional}\to\frac12\text{ provisional}.
\]

This is the second consecutive unchanged run after the 19:48 movement, so `unchanged_count=2`. Per the owner protocol, the next unchanged run would trigger the first I0112 stuck report. I therefore do not add another auxiliary lemma to the same route in advance.

The strongest genuine progress this run is structural:

- the missing information estimate is transferred **exactly** to stabilizer-bi-invariant group walks;
- the full information law, not only varentropy, is preserved;
- the most obvious curvature extension is ruled out by an explicit negative-curvature test on high-girth source-positive examples.

## 9. Next three new-method moves

Do not repeat `#3,#14,#20`, nor the previous triples `#5,#12,#27` and `#10,#11,#15`.

If the metric has not moved by the next invocation, the run must follow the stuck protocol rather than produce another lemma. The three genuinely different probes should be:

- **#1 CHANGE THE CATEGORY:** replace the group algebra by the finite Hecke algebra / association-scheme operator system and ask for a quotient-sensitive entropy tensorization that sees only the `d` neighbor orbitals, not `d|H|` group atoms;
- **#7 TAKE THE LIMIT:** study Benjamini--Schramm / local weak limits of transitive expanders and whether information fluctuations can be decomposed into an entropy-rate term plus an `o(log^2 N)` finite-volume correction;
- **#26 HUNT THE SPORADIC CASE:** search small-degree transitive expanders with several stabilizer suborbits for the first exact obstruction to a proposed Hecke tensorization, rather than testing Cayley/arc-transitive examples where the algebra is unusually symmetric.

If those three fail to move `W_exp`, the required five-part stuck report should isolate the simplest still-unproved subclass (likely non-normal Cayley expanders or a bounded-rank non-Gelfand Schreier class) and choose exactly one recovery.

## 10. R12 directed-audit status

The revised R12 assignment was read from the current repository rather than assumed to be the historical AT task. R12 has handed off I0102 and claimed Auffinger--Damron--Hanson Question 17 / I0060. The newest located R12 file is still the handoff/claim package, not a complete theorem package. Therefore

`R16_AUDIT_R12 = PENDING_NOT_READY`.

No missing audit is counted as an audit and no peer file is modified.

## 11. Model / scheduler escalation status

Nothing changed in the exposed model-control surface. The scheduler interface available to this environment permits prompt/title/schedule/timing/enabled-state edits but exposes **no model field and no reasoning-effort field**. Prompt text can request GPT-6/maximum but cannot enforce or verify it.

The repository now records two apparently different permission contexts: one authorized P/C deployment succeeded in updating P26, while another context returned `You cannot modify this task` for P26/P01/P03 and denied R-series edits. The compliant workaround is to perform the change from the authorized owning workspace/context or have platform support / the workspace owner repair task ownership. Creating duplicate schedules or bypassing permissions is not a valid workaround. No scheduler state was changed in this run.

## 12. Artifact decision

No checker artifact was created. C08 is an exact finite theorem proved symbolically on the page; C09 is a theorem-to-theorem reduction; C10 is a universal local calculation written line by line. There is no finite enumeration or numerical certificate whose correctness would be improved by a checker. Creating one solely to prove that the run executed would violate the 90-percent new-methods rule.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  active_source: "Justin Salez (2025), arXiv:2508.21055v1, Problem 2.3"
  source_target: "all bounded-degree vertex-transitive expander sequences exhibit total-variation cutoff"
  metric: W_exp
  before: "1/2 provisional"
  after: "1/2 provisional"
  movement: "NO MOVEMENT"
  unchanged_count: 2
  status: PARTIAL
  methods: [3, 14, 20]
  exact_evidence:
    - "R16-I0112-C08: every vertex-transitive SRW has a symmetric H-bi-invariant group lift started from U_H with exactly identical information-content law"
    - "R16-I0112-C09: Salez's expander varentropy criterion is exactly equivalent to an o(log^2 |Gamma/H|) information-variance estimate for those Hecke lifts"
    - "R16-I0112-C10: girth>=5 d-regular normalized SRW has kappa_BE <= -(d-2)/d via an explicit radius-two test function"
  prior_art_status:
    Beck_Fiala: "KNOWN by fresh primary preprint claim Guo--Fang--Lu arXiv:2609.11189v1; Bansal--Jiang v2 only covers t>=log^2 n at square-root order"
    I0112: "OPEN in bounded current primary search; Altschuler arXiv:2609.14945 is long-range-expander partial progress"
    C08_C10_novelty: "NOT CLAIMED; Schreier/Hecke representation and negative tree-like curvature are standard themes; exact derivations recorded as route tools"
  audits:
    P26: PENDING
    second_other_track: PENDING
    R12_directed_audit: PENDING_NOT_READY
  remaining_obligation: "prove quotient-sensitive information concentration for general H-bi-invariant orbital walks, or find a source-valid obstruction/counterexample; naive nonnegative-curvature route is now ruled out"
  next_methods: [1, 7, 26]
```

## 14. Primary references

1. Justin Salez, _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1 (2025), Problem 2.3.
2. Justin Salez, _The varentropy criterion is sharp on expanders_, arXiv:2307.10066, Theorem 2, Corollary 2, Conjecture 1.
3. Jonathan Hermon, Xiangying Huang, Francesco Pedrotti, Justin Salez, _Concentration of information on discrete groups_, arXiv:2409.16869.
4. Francesco Pedrotti, Justin Salez, _The local product condition implies cutoff_, arXiv:2607.05345.
5. Dylan J. Altschuler, _Long-range expanders: construction and cutoff_, arXiv:2609.14945 (14 Sep 2026).
6. Shengtao Guo, Ethan X. Fang, Junwei Lu, _Vector Balancing via Directional Total Variation_, arXiv:2609.11189v1 (10 Sep 2026).
7. Nikhil Bansal, Haotian Jiang, _Decoupling via Affine Spectral-Independence: Beck--Fiala and Komlos Bounds Beyond Banaszczyk_, arXiv:2508.03961v2 (9 Sep 2025).

**End status:** I0112 remains OPEN/PARTIAL; `W_exp` is unchanged at `1/2` provisional. The exact group lift identifies the missing symmetry correctly as stabilizer bi-invariance, and the high-girth calculation rules out a direct nonnegative-curvature proof. No shared root, peer file, email, Drive content, public post, permission, workflow, or scheduler state was modified.