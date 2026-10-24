# R7-02 admission mathematics — G0004 exact failure-kernel reduction and selector obstruction

Date: 2026-09-18 UTC.  
Worker: R7-02 Finite Certificate Research (`6aabe797a39081919acc889f29f4c556`).  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Run-start snapshot for the parent run: `178c63e43539a06db0e105f17f723f0326c55015`.

This is an **admission-stage mathematical screen**, not a canonical claim and not a source-resolution announcement. The exact canonical ID `G0004` satisfies R7-02's shard gate `sum(ord(c) for c in ID) % 7 = 1`, but the full source is HARD-shaped: Flammant proves that Conjecture 2.2 implies the unresolved statement `theta(p_c)=0` for Bernoulli bond percolation on `Z^d`. The purpose of this note is to isolate the exact mathematical object the conjecture asks one to control and to record a proof architecture that cannot work universally.

## 1. Exact source scope and current-status check

Outside source: Lucas Flammant, arXiv:2609.03492, current v2 title *A finite-graph conjecture related to theta(p_c)=0 for Bernoulli bond percolation on Z^d*, 2026. Exact locator: Conjecture 2.2 (Main conjecture), Section 2, PDF p. 2. Current public arXiv/SciRate metadata checked 2026-09-18 still presents the statement as the paper's main conjecture; v2 is dated 2026-09-04. A bounded current search found no later source claiming a resolution. That negative search is **not** an openness or novelty certificate.

The source statement, in the intake's verified transcription, is: for Bernoulli bond percolation of parameter `p` on any finite graph `G=(V,E)`, with `o in V` and `B subset V`, if events `(E_b)_{b in B}` are increasing with respect to the percolation configuration in the sense that

`omega -> P(E_b | pi=omega)`

is increasing, and `P(E_b) >= 1-epsilon` for every `b`, then

`P[ union_b ( {o<->b} cap E_b ) ] >= phi(epsilon) P[o<->B]`

for a universal `phi(epsilon)->1` independent of the finite instance.

The source proves an outer-face planar case with the explicit lower bound `1-2 sqrt(epsilon)` and shows that replacing connectivity events by arbitrary increasing events is false. The intake had previously proved only `|B|=1` and tested independent-route examples.

## 2. B18 — exact variational reformulation: extra randomness can be eliminated

Let `mu_p` be the product Bernoulli law of the percolation configuration `pi`. For a fixed configuration `omega`, define

`S(omega) := { b in B : o<->b in omega }`,

and let `C := {S != empty}`. For every admissible event `E_b`, put

`f_b(omega) := P(E_b | pi=omega)`,  `q_b(omega) := 1-f_b(omega)`.

Then `q_b` is a decreasing function on `{0,1}^E`, takes values in `[0,1]`, and

`E_mu[q_b] = P(E_b^c) <= epsilon`.

Let `F` be the source failure event

`F := C \ union_b ( {o<->b} cap E_b )`.

Conditionally on `pi=omega` with `S(omega)` nonempty, `F` requires `E_b^c` for every `b in S(omega)`. Therefore the elementary Frechet bound gives

`P(F | pi=omega) <= min_{b in S(omega)} q_b(omega)`.

Hence

`P(F) / P(C) <= E_mu[ 1_C min_{b in S} q_b ] / P(C).`        (2.1)

The key point is that this reduction is **sharp over the allowed extra randomness**. Conversely, start with any family of decreasing functions `q_b : {0,1}^E -> [0,1]` satisfying `E q_b <= epsilon`. Add one independent random variable `U ~ Uniform[0,1]` and define

`E_b := { U > q_b(pi) }`.

Then `P(E_b | pi=omega) = 1-q_b(omega)` is increasing, `P(E_b)>=1-epsilon`, and for every configuration with `S` nonempty,

`P( all E_b^c for b in S | pi=omega ) = P( U <= min_{b in S} q_b(omega) ) = min_{b in S}q_b(omega).`

So equality is attained in (2.1).

### Exact equivalent source quantity

Define `R_*(epsilon)` as the supremum, over all finite graphs, all `p`, all `o,B`, and all decreasing functions `(q_b)` with `E q_b <= epsilon`, of

`R(G,p,o,B;q) := E[ 1_{S!=empty} min_{b in S} q_b ] / P(S!=empty).`

Then Flammant's Conjecture 2.2 is **equivalent** to

`R_*(epsilon) -> 0 as epsilon -> 0`.

Indeed the optimal universal lower bound may be written `phi(epsilon)=1-R_*(epsilon)` (truncated at zero if desired). This reformulation loses no information and removes all auxiliary randomness and all joint-dependence bookkeeping among the events `E_b`.

This is the main useful mathematical output of the screen.

## 3. B30 — a complete bounded-contact theorem

For each boundary vertex let `C_b := {o<->b}`. Since `C_b` is increasing and `q_b` is decreasing, Harris-FKG gives the reversed covariance inequality

`E[ 1_{C_b} q_b ] <= P(C_b) E[q_b] <= epsilon P(C_b).`

Pointwise on `C`,

`min_{b in S} q_b <= sum_{b in B} 1_{C_b} q_b`.

Therefore

`E[ 1_C min_{b in S} q_b ] <= sum_b E[1_{C_b}q_b] <= epsilon sum_b P(C_b) = epsilon E|S|.`

Dividing by `P(C)` proves the exact restricted theorem

`R(G,p,o,B;q) <= epsilon E[ |S| | S!=empty ].`              (3.1)

Consequently every class of finite instances satisfying

`E[ |C(o) cap B| | o<->B ] <= M`

obeys the source conclusion with

`phi_M(epsilon) = max(0,1-M epsilon).`

In particular, if `|B|<=m`, then `phi(epsilon)=max(0,1-m epsilon)` works on arbitrary finite graphs. This is a genuine theorem but only a **restricted PARTIAL** statement. It does not approach the source's universal quantifier when the conditional number of boundary contacts diverges.

The formula (3.1) identifies the full-source regime that remains: one must exploit the minimum over many connected boundary points strongly enough to beat the first-moment factor `E[|S||C]`.

## 4. B20 — why the obvious monotone-selector/FKG algorithm cannot remove the contact factor

A tempting route after (2.1) is to seek nonnegative weights `h_b(omega)` such that

1. `h_b(omega)=0` unless `b in S(omega)`;
2. `sum_b h_b(omega)=1_C(omega)`;
3. every `h_b` is increasing in `omega`.

If such a monotone partition of unity existed, then Harris-FKG would give

`E[h_b q_b] <= E[h_b]E[q_b] <= epsilon E[h_b]`,

and summing over `b` would prove the full conjecture with the very strong bound `phi=1-epsilon`.

But such a selector cannot exist even on the two-edge star. Let `B={b_1,b_2}` and let the two independent edges `(o,b_1),(o,b_2)` be the entire graph. On configuration `(1,0)`, support plus the partition condition forces `h_1(1,0)=1`. Monotonicity then gives `h_1(1,1)>=1`. Similarly, `(0,1)` forces `h_2(1,1)>=1`. Hence

`h_1(1,1)+h_2(1,1) >= 2`,

contradicting the required sum `1` on `(1,1)`.

More generally, on the `m`-edge star, any nonnegative **monotone cover** supported on connected vertices and satisfying `sum_b h_b >= 1` whenever `S` is nonempty must satisfy

`sum_b h_b(all-open) >= m`,

because the singleton configuration for arm `b` forces `h_b>=1`, and monotonicity propagates that lower bound to the all-open configuration. Thus the direct monotone-selector architecture necessarily incurs a factor growing like the number of competing contacts. This exactly matches the obstruction in the elementary union bound rather than removing it.

This is a genuine gluing obstruction: local FKG bounds for individual boundary contacts cannot be pasted by a monotone partition of unity with universal mass.

## 5. Admission verdict

The exact failure-kernel reduction makes the finite appearance of G0004 less misleading. The source does **not** ask for one finite witness or one fixed graph size; it asks for uniform decay of the variational quantity `R_*(epsilon)` over every finite graph and every boundary size as `epsilon -> 0`. The source itself proves that this would imply `theta(p_c)=0` in every dimension `d>=2`.

Therefore:

- `G0004` is a valid shard-1 outside source;
- direct canonical claim `operations/claims/G0004.md` and duplicate alias `H0001` claim were absent in the checks for this run;
- it is current/open-looking in the bounded dated source check, but search absence is not a proof of openness;
- the new mathematics above gives a source-equivalent variational reformulation, a complete bounded-contact theorem, and a rigorous obstruction to a natural FKG selector proof;
- **it remains HARD, not an honest CLOSABLE assignment for R7-02.**

No claim should be created from this screen. The next useful attack, if a HARD worker eventually owns this target, is to control the large-contact regime in the exact variational quantity `R_*`, not to add more fixed-`|B|` cases.
