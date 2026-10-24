Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Primary source metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; methods actually tried: **B11 / B15 / B30**. Substantive progress: an exact source-compatible cut-coset/cycle-code duality turns unsigned 3-uniform hypergraph 2-coloring into occupancy of the zero gauge coset by a product one-hot set, and its quotient Parseval identity exposes the same exact `10/9` instability as the earlier soft-message calculation.

# HARD7-06 run 9 — exact cut-coset duality and the `10/9` global-cycle obstruction

Status: **PARTIAL / source OPEN under bounded current-literature review.**

Repository / branch: `yspennstate/math-open-problems` / `master`.

Canonical target remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owned by `HARD7-06`.

## 1. Continuity, exclusions, source check, and ownership

I resumed the admitted target rather than restarting from the original random-3-SAT candidate. I reread the HARD7 control files, root `POSTED.md` and `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical CKS claim, the newest HARD7-06 report `2026-09-19T03-45-51Z__gauge_sector_obstruction.md`, the STUCK2 report, the profile-tilt checkpoint, the neighboring R03/F0097 ownership/handoff history, and repository intake/claim screens around this target. The random-3-SAT F0097 history remains a separate R03 lifecycle and is not silently reassigned here. Repository searches continue to show `CKS-2024-RREG-HYPER2COL-K3` as HARD7-06-owned, with no posted/settled duplicate.

The primary source remains Evan Chang, Neel Kolhe and Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, full version arXiv:2308.02075. I rechecked the primary proceedings page and arXiv record on 2026-09-19. The source explicitly says that establishing the exact threshold for small fixed `k>=3` remains an important open problem and that its hypergraph-2-coloring upper bound is conjectured sharp. A fresh bounded search for `random regular hypergraph 2-colorability k=3 d=6 2025 2026`, the exact title/arXiv identifier, and recent random-regular NAE-SAT work did not recover a theorem proving the exact simple unsigned `H_{n,6,3}` lower side. This is bounded negative evidence, not a worldwide openness certificate.

I also reread the open Springer text of Nam--Sly--Sohn, *One-Step Replica Symmetry Breaking of Random Regular NAE-SAT II*, CMP 405 (2024), especially its literal-labelled factor-graph definition and literal averaging. This confirms the run-8 diagnosis: the solved large-`k` architecture averages over literals, whereas the CKS source fixes the all-zero literal sector. The exact duality below attacks that distinction directly instead of adding another tree-local surrogate.

Prior-art searches for `NAE-SAT cycle space Fourier`, `hypergraph 2-coloring cut space one-hot`, `NAE-SAT gauge cycle code`, and `random regular hypergraph coloring MacWilliams` did not locate this exact source-facing formulation. The ingredients — cut/cycle orthogonality, Walsh transforms, and MacWilliams/Poisson summation — are classical coding/graph folklore. **No global novelty claim is made for the algebraic mechanism.** The value here is the exact reduction of the present source model and the identification of the route obstruction it creates.

## 2. Frozen source metric

As at admission,

\[
L_6:=\sup\left\{L\in[0,1]:\liminf_{n\to\infty}
\Pr(H_{n,6,3}\text{ is 2-colorable})\ge L\right\},
\]

along source-admissible `n` in the uniformly random **simple** 6-regular 3-uniform model.

This run gives an exact reformulation and a route obstruction, not a positive asymptotic probability lower bound. Therefore

\[
\boxed{L_6\ge0\quad\longrightarrow\quad L_6\ge0.}
\]

Finite code enumerations below are self-checks of the exact identities only; they are not evidence that the zero coset is occupied with positive asymptotic probability.

## 3. B11 DUALIZE — hypergraph coloring is zero-coset occupancy by a product one-hot set

Let `H=(V,F)` be any finite 3-uniform hypergraph and let

\[
G=(V\sqcup F,E)
\]

be its bipartite incidence graph. Work over `F_2`. Let

\[
\delta:\mathbb F_2^{V\sqcup F}\to\mathbb F_2^E,
\qquad [\delta(x,z)]_{va}=x_v+z_a,
\]

and write

\[
\mathcal B(G):=\operatorname{im}\delta
\]

for the cut/coboundary space. For a literal vector `ell in F_2^E`, define the local product set

\[
\mathcal T:=\left\{y\in\mathbb F_2^E:
\sum_{e\in\delta a} y_e=1\text{ as an integer for every }a\in F\right\}.
\tag{3.1}
\]

Thus every factor chooses exactly one of its three incidences.

### Proposition 3.1 — exact cut-coset representation

If `c(G)` is the number of connected components, then the number `Z_ell(G)` of NAE-satisfying variable assignments with literal signing `ell` is exactly

\[
\boxed{
Z_\ell(G)=2^{c(G)}\,\big|\mathcal T\cap(\ell+\mathcal B(G))\big|.
}
\tag{3.2}
\]

In particular, for the unsigned CKS source,

\[
\boxed{
H\text{ is 2-colorable}\iff \mathcal T\cap\mathcal B(G)\ne\varnothing.
}
\tag{3.3}
\]

#### Proof

Fix a satisfying variable assignment `x`. At every 3-clause `a`, the three literal-evaluated bits

\[
(x_v+\ell_{va})_{v\in a}
\]

are not all equal, hence have a unique minority bit. Let `z_a` be their majority value and define

\[
y_{va}:=x_v+z_a+\ell_{va}.
\]

Exactly the unique minority incidence has `y=1`, so `y in T`; moreover

\[
y+\ell=\delta(x,z)\in\mathcal B(G),
\]

hence `y in ell+B(G)`.

Conversely, if `y in T cap (ell+B(G))`, choose `(x,z)` with

\[
y+\ell=\delta(x,z).
\]

At factor `a`, the literal-evaluated vector is `y_{delta a}+z_a`; because `y_{delta a}` has exactly one `1`, this vector is either of type `100` or its complement `011`, and is therefore NAE. Thus every such preimage gives a satisfying variable assignment.

Finally `ker(delta)` consists of the simultaneous variable/factor flip on each connected component, so `|ker(delta)|=2^{c(G)}`. These kernel shifts give distinct variable assignments and exhaust the preimages of each `y`. This proves (3.2). QED.

This changes the category of the source problem. It is no longer necessary to begin with an invented finite-state cluster surrogate: for each random factor graph, the exact question is whether the **zero coset of a structured binary cut code** contains a vector from the direct product of `|F|` one-hot 3-sets.

For a connected `(d,k)=(6,3)` factor graph on `n` variables,

\[
|F|=2n,\quad |E|=6n,\quad \dim\mathcal B=3n-1,
\]

and the quotient has dimension

\[
\beta_1=6n-(3n-1)=3n+1.
\]

A uniformly random gauge sector `q` therefore has exact mean one-hot occupancy

\[
\mathbb E_q N_q
=\frac{|\mathcal T|}{2^{\beta_1}}
=\frac{3^{2n}}{2^{3n+1}}
=\frac12\left(\frac98\right)^n,
\tag{3.4}
\]

where `N_q=|T cap (q+B)|`. Multiplying by the `2` global-complement preimages recovers the familiar literal-averaged first moment `(9/8)^n`. The source, however, asks about the single deterministic sector `q=0`, not the average sector.

## 4. B11 continued — exact cycle-code Fourier transform

Let

\[
\mathcal C(G):=\mathcal B(G)^\perp
\]

be the binary cycle space of the factor graph. For `B in C(G)`, every factor has selected degree `0` or `2`, so `|B|` is even. Define

\[
\mathcal F_G(\ell)
:=\sum_{B\in\mathcal C(G)}
\left(-\frac13\right)^{|B|/2}(-1)^{\langle \ell,B\rangle}.
\tag{4.1}
\]

### Proposition 4.1 — exact NAE Fourier formula

For every 3-uniform factor graph and every literal signing,

\[
\boxed{
Z_\ell(G)=2^{|V|}\left(\frac34\right)^{|F|}\mathcal F_G(\ell).
}
\tag{4.2}
\]

#### Proof

In spin variables `s_i in {+1,-1}`, the 3-NAE indicator has the exact identity

\[
1_{\rm NAE}(s_1,s_2,s_3)
=\frac{3-s_1s_2-s_1s_3-s_2s_3}{4}.
\tag{4.3}
\]

Expand the product over factors. At each factor one either selects the constant `3/4` or one of its three pair terms `-s_i s_j/4`. After factoring `(3/4)^{|F|}`, every active factor contributes `-1/3` and selects exactly two incidence edges. Summing over variable spins annihilates every term in which some variable has odd selected degree. The surviving incidence sets are therefore exactly the even subgraphs `B in C(G)`. Each active factor contributes two edges, hence their number is `|B|/2`. Literal flips contribute the character `(-1)^{<ell,B>}`, and the spin sum contributes `2^{|V|}`. This is (4.2). QED.

Equation (4.1) makes the run-8 gauge quotient exact: adding any cut vector to `ell` does not change any character because `C=B^perp`. Thus the sector dependence is the Walsh transform of one fixed radial weight on the cycle code.

### Proposition 4.2 — exact quotient Parseval identities

Let `Q=F_2^E/B(G)`, so `|Q|=2^{beta_1}`. Then

\[
\boxed{
\frac1{|Q|}\sum_{q\in Q}\mathcal F_G(q)=1,
}
\tag{4.4}
\]

and

\[
\boxed{
\frac1{|Q|}\sum_{q\in Q}|\mathcal F_G(q)|^2
=\sum_{B\in\mathcal C(G)}3^{-|B|}.
}
\tag{4.5}
\]

Hence

\[
\boxed{
\operatorname{Var}_{q\in Q}(\mathcal F_G(q))
=\sum_{B\in\mathcal C(G)\setminus\{0\}}3^{-|B|}.
}
\tag{4.6}
\]

#### Proof

The characters `q -> (-1)^{<q,B>}` for `B in C(G)` are the complete character group of `Q`. Averaging a nontrivial character gives zero, proving (4.4). Parseval for this finite abelian group gives the sum of squared Fourier coefficients; the coefficient at `B` has squared magnitude `3^{-|B|}`, proving (4.5), and subtracting the squared mean gives (4.6). QED.

The positive polynomial on the right of (4.5) is exactly the even-subgraph/high-temperature polynomial of a ferromagnetic Ising model on the factor graph at `tanh J=1/3`. This identification is classical; it is used here only as a map to existing machinery, not as a novelty claim.

A second exact dual form follows from binary Poisson/MacWilliams summation. Put `t=i/sqrt(3)`; since every cycle word has even weight,

\[
(-1/3)^{|B|/2}=t^{|B|}.
\]

Then

\[
\boxed{
\mathcal F_G(\ell)
=\frac1{|\mathcal B(G)|}
\sum_{D\in\mathcal B(G)}
(1+t)^{|E|-|D+\ell|}(1-t)^{|D+\ell|}.
}
\tag{4.7}
\]

This is immediate by inserting the character projector for `C=B^perp` and factorizing the sum over `F_2^E`. Since `(1-t)/(1+t)=e^{-i\pi/3}`, the source sector is equivalently a sixth-root-of-unity cut-size exponential sum. That is a genuinely different representation of the same exact source object and suggests algebraic/coding approaches that do not pass through the random-literal tree law.

## 5. B15 BREAK THE SYMMETRY — nonzero flux is a character, not a small perturbation

Run 8 showed a formal gauge quotient and a finite graph whose satisfiability changes with cycle flux. Equations (3.2) and (4.1) identify the mechanism exactly:

- a gauge sector is a coset `q` of the cut code;
- satisfiability is `N_q>0`, where `N_q=|T cap(q+B)|`;
- the same sector acts on every cycle-code coefficient by the character `(-1)^{<q,B>}`;
- averaging iid literals annihilates every nonzero cycle coefficient, while the unsigned source `q=0` adds all coefficients with their intrinsic `(-1)^{|B|/2}` sign.

Thus the all-zero source is not a perturbation of the literal-averaged ensemble in any tree-local parameter. It is the **DC character of a quotient whose dimension is `3n+1`**.

The exact finite checker for this run uses the same source-valid simple `6`-regular `3`-uniform witness `K_5^(3)` but now verifies the new duality, not merely the old gauge rank. It exhausts all `2^16=65536` gauge sectors and all `3^10=59049` one-hot vectors. It finds

\[
\#\{q:N_q>0\}=41141,
\]

with exact occupancy histogram

\[
N_q=0,1,2,3,4,5
\quad\text{for respectively}\quad
24395,25749,13080,2120,180,12
\]

sectors. The unsigned sector has `N_0=0`; the explicit run-8 nonzero-flux signing has `N_q=3`, hence exactly six NAE assignments by (3.2). The checker verifies (4.2) for **every one of the 65536 sectors**, not a sample.

It also certifies the exact Parseval value

\[
\frac1{2^{16}}\sum_q \mathcal F_G(q)^2
=\sum_{B\in\mathcal C(G)}3^{-|B|}
=\frac{2191720448}{1162261467}.
\tag{5.1}
\]

This exhaustive finite certificate does **not** move `L_6`: `K_5^(3)` is one fixed graph and the asymptotic source asks about a random sequence of growing simple regular hypergraphs.

## 6. B30 LOCALIZE BY SCALE — the same `10/9` obstruction reappears globally

The Parseval correction (4.5) naturally asks whether the nonzero even subgraphs can be controlled by an absolutely convergent short-cycle expansion. For a `(6,3)`-biregular factor graph let `B_NB` be its Hashimoto nonbacktracking matrix on directed incidences. From every directed edge, two nonbacktracking steps have exactly

\[
(3-1)(6-1)=10
\]

continuations, regardless of direction. Therefore

\[
B_{NB}^2\mathbf 1=10\mathbf 1,
\qquad
\rho(B_{NB})=\sqrt{10}.
\tag{6.1}
\]

In the positive Parseval polynomial, an incidence edge carries weight

\[
x=\frac13.
\]

Consequently

\[
\boxed{x\rho(B_{NB})=\frac{\sqrt{10}}3>1,
\qquad x^2(3-1)(6-1)=\frac{10}{9}>1.}
\tag{6.2}
\]

This has a precise route-level consequence. The standard nonbacktracking trace expansion

\[
-\log\det(I-xB_{NB})
=\sum_{r\ge1}\frac{x^r}{r}\operatorname{tr}(B_{NB}^r)
\tag{6.3}
\]

has radius `1/rho(B_NB)=1/sqrt(10)`. The source value `x=1/3` lies outside that radius. Therefore a proof strategy that tries to control (4.5) merely by absolutely summing its bounded-cycle/nonbacktracking corrections around the tree is not available at `(k,d)=(3,6)`.

This statement is deliberately limited. The finite even-subgraph polynomial is perfectly well defined, and (6.2) does **not** rule out resummation, Bethe methods, contour methods in another variable, or direct coding arguments. It rules out the naive absolutely convergent nonbacktracking-loop expansion as the missing global bridge.

The useful surprise is that the number in (6.2) is exactly the `10/9` soft-message variance multiplier independently obtained in run 6. The local BP instability and the global sector-Parseval obstruction are therefore two faces of the same branching parameter:

\[
\boxed{
\text{five variable continuations}\times\text{two factor continuations}\times(1/3)^2=10/9.
}
\tag{6.4}
\]

This is the main conceptual progress of the run. It explains why both the local scalar route and the bounded-cycle global route fail at the same point, and it points away from another perturbative repair.

## 7. Exact artifact and what is / is not certified

New exact artifact pair:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T04-49-49Z__cycle_code_duality_exact.py`
- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T04-49-49Z__cycle_code_duality_exact.out`

The script uses only exact integer and `Fraction` arithmetic for the finite identities. It certifies:

- cut-space rank `14`, cycle dimension `16` for the `K_5^(3)` factor graph;
- exhaustive `65536`-sector cut-coset counts;
- direct NAE counts and the cut-coset formula;
- the Fourier formula (4.2) for every sector;
- exact quotient Parseval;
- the occupancy histogram above;
- the exact `10/9` branching quantity;
- terminal line `ALL_EXACT_CHECKS_PASS = True`.

It is a **self-check**. It does not certify an asymptotic theorem about random regular graphs and it is not an independent audit.

## 8. What this opens, and what remains blocked

The strongest next route is now source-native and does not need literal averaging:

> Study the quotient map `pi:T -> F_2^E/B(G)` for a random `(6,3)`-regular incidence graph and prove that its zero fiber is nonempty with high probability. Equivalently, control the zero-coset one-hot transversal count `N_0` directly.

The exact first moment is exponentially large, `(1/2)(9/8)^n` for `N_q` averaged over sectors, but run 1 already showed that the unweighted zero-fiber second moment is destabilized by correlated pairs. The new representation sharpens the missing object: it is not “some better BP message”; it is a **zero-fiber anti-concentration / structured-code occupancy theorem** strong enough to overcome the `10/9` branching instability.

Three concrete nonperturbative continuations are now distinguishable:

1. use the cut-coset formulation to search for a source-valid weighted one-hot measure whose quotient Fourier coefficients contract even though the uniform measure does not;
2. use (4.7) to seek cancellation at the sixth-root phase by exact cut-size congruence information, rather than absolute values;
3. exploit expansion of the random biregular factor graph to separate `o(n)` cycle-code words from extensive codewords and control the latter by a global weight-enumerator large deviation principle instead of an absolutely convergent loop series.

No one of these has yet yielded `L_6>0`, so the source remains OPEN/PARTIAL.

This is the **second substantive execution after STUCK2**, the second and final allowed recovery. If the frozen source-facing obligation remains unchanged through the next Section-I trigger, the protocol allows no third recovery: HARD7-06 must write a handoff and rotate to a fresh eligible hard CSP target rather than manufacture another local lemma.

Suggested nonrepeating next triple, if one more substantive recovery execution is protocol-valid before the trigger: **B3 PROVE SOMETHING STRONGER** (a quotient Fourier contraction under an explicit source-valid weight), **B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE** (coding-theoretic weight enumerators / root-of-unity cut sums), **B28 REPLACE FOR ALL WITH TYPICAL** (prove zero-fiber occupancy for typical expanders after isolating the exceptional graph class).

## 9. Runtime / scheduler capability honesty

The current exposed automation interface still has fields for title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector and no guaranteed execution duration**. GPT-6 / maximum is therefore still request text only; this run actually identifies as GPT-5.6 Sol and the reasoning level is not exposed, so it is reported as UNVERIFIED.

The repository policy records that some historical native task edits, including one P26 context, returned `You cannot modify this task`; `RESULTS.md` also records a later successful P26 update in a different authorized context. I did not mutate or re-probe P26 in this research run. The legitimate workaround for a denied task remains to use the task's authorized account/workspace scheduler context or platform support; do not bypass the denial, create a duplicate, or pretend a repository edit changes native scheduler state. Changing model/reasoning would require the platform to expose those scheduler fields (or an authorized interface that already does); this task cannot synthesize such a selector.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  target: CKS-2024-RREG-HYPER2COL-K3
  status: PARTIAL
  primary_metric: L_6
  before: ">=0"
  after: ">=0"
  movement: no movement
  methods: [B11, B15, B30]
  new_exact_result: "cut-coset one-hot representation + cycle-code Fourier/Parseval duality; same 10/9 instability at the nonbacktracking radius"
  source_closed: false
  independent_audits: 0
  next_obligation: "nonperturbative zero-fiber occupancy / quotient-Fourier control for typical random (6,3)-regular factor graphs"
```
