# FOREST fleet04/B03 — aggregate variance squeeze for the remaining 3-connected obstruction

Run: `20260922T053904Z-B03-forest-r13`  
Outcome: **AUXILIARY_ONLY**  
Candidate: `FOREST-3CONN-VARIANCE-SQUEEZE-v1`  
Parent target: **OPEN / not promoted**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact scope and inherited proof state

Target: for every finite simple graph `G`, under the uniform law on all acyclic edge subsets, prove pairwise negative correlation for every distinct pair of edges.

Latest complete team-lead state consumed: fleet01/B01 `FOREST-KN-COCKS-REDUCTION-v2`, shared handoff commit `95fbb93a41b0ae74f5240f781da23c193d94db45`. That route proves the complete-graph theorem by an exact Hermite calculation and proposes the source-dependent chain

`all K_n at unit weight -> Cocks fixed-graph weighted upgrade -> minor closure -> every simple G by deletion`.

I did not repeat that proof here. The current fleet01/B01 run was incomplete when read, so the latest complete lead handoff above was used.

Named OTHER-account result consumed and directly applied: fleet02/B01, report commit `97feb5d7c3122f12cd446f95c2bfb3eec6ffe0ff`, `FOREST` run `B01-20260922T021602Z-forest-r12`. Its exact minimal-counterexample theorem gives:

1. a lexicographically minimal simple counterexample `(G,e,f)` is 3-connected;
2. with `G0=G-{e,f}` and `H` uniform over forests of `G0`, define
   `X=1{H+e is a forest}`, `Y=1{H+f is a forest}`, `S=1{H+e+f is a forest}`,
   `x=E X`, `y=E Y`, `r=E S`, and `D=xy-r=-delta<0`;
3. for every third edge `g`, with `T_g=1{g in H}`, `v_g=Var(T_g)`,
   `a_g=-Cov(X,T_g)`, `b_g=-Cov(Y,T_g)`, one has

       a_g>0,  b_g>0,  a_g b_g >= delta v_g.

The fleet02/B01 proof obtains this from the exact deletion/contraction mixture identity plus fixed-graph Cocks on strictly smaller simple graphs. I use that theorem exactly in this form; peer PASS labels are not substituted for its formulas.

Source chronology was also checked against the published Semple-Welsh text. The final paper's added Note states that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Cocks, *Correlated Matroids*, CPC 17 (2008), 511-518, DOI `10.1017/S0963548308009152`, states in its abstract that the Grimmett-Winkler conjecture is equivalent to a correlated-graphic-matroid statement. This report does not require a new use of Cocks beyond the named peer theorem above.

## 2. New aggregate theorem

### Theorem (rank-sensitive variance squeeze)

Under the minimal-counterexample hypotheses above, let `M0=M(G0)` and let `rho=r(M0)`. Then

    delta <= sqrt(x(1-x)y(1-y)) / rho <= 1/(4 rho).

Because fleet02/B01 already proves that the minimal counterexample `G` is 3-connected, deleting the two marked edges leaves `G0` connected, so `rho=|V(G)|-1`. Hence every remaining minimal obstruction satisfies the explicit necessary condition

    delta <= sqrt(x(1-x)y(1-y)) / (|V(G)|-1)
          <= 1 / (4(|V(G)|-1)).

This is not a contradiction and therefore is not parent-problem closure. It is the first exact aggregate compatibility condition I know here that simultaneously uses *all* of the peer's per-third-edge inequalities.

### Proof

Put

    K = |H| = sum_g T_g,
    A = sum_g a_g = -Cov(X,K),
    B = sum_g b_g = -Cov(Y,K),

where the sums range over `E(G0)`.

By Cauchy-Schwarz and the peer inequality `a_g b_g >= delta v_g`,

    A B
      = (sum_g a_g)(sum_g b_g)
      >= (sum_g sqrt(a_g b_g))^2
      >= delta (sum_g sqrt(v_g))^2.                 (1)

A second covariance Cauchy-Schwarz bound gives

    A <= sqrt(Var(X) Var(K)),
    B <= sqrt(Var(Y) Var(K)),

hence

    A B <= sqrt(x(1-x)y(1-y)) Var(K).               (2)

Minimality applies to `G0`, which has fewer edges than `G`. Thus every pair of distinct third-edge indicators is negatively correlated under the uniform forest law of `G0`. Consequently

    Var(K)
      = sum_g v_g + 2 sum_{g<h} Cov(T_g,T_h)
      <= sum_g v_g.                                  (3)

It remains to compare `sum v_g` with `sum sqrt(v_g)`. Two elementary matroid facts suffice.

**Fact A: every element of a uniformly random independent set has inclusion probability at most `1/2`.**
For a loopless matroid `M` and element `g`, independent sets containing `g` are in bijection, after deleting `g`, with `Ind(M/g)`. The identity map injects `Ind(M/g)` into `Ind(M\g)`, because `I union {g}` independent implies `I` independent. Therefore `P(g in I)<=1/2`.

Apply this to `M0`. If `p_g=P(T_g=1)`, then `p_g<=1/2`, so

    v_g=p_g(1-p_g) >= p_g/2.                         (4)

**Fact B: a uniform independent set of a rank-`rho` matroid has mean size at least `rho/2`.**
Let `i_k` be the number of independent `k`-sets. Every independent `k`-set extends to a basis, so it has at least `rho-k` one-element independent extensions. Double-counting extension pairs gives

    (k+1) i_{k+1} >= (rho-k) i_k.

Thus `q_k=i_k/binom(rho,k)` is nondecreasing. Since `binom(rho,k)=binom(rho,rho-k)`, for `k<rho/2` one has `i_{rho-k}>=i_k`; pairing these levels gives

    E K = (sum k i_k)/(sum i_k) >= rho/2.            (5)

From (4)-(5),

    sum_g v_g >= (1/2) sum_g p_g = E K/2 >= rho/4.  (6)

Also `v_g<=1/4`, so `sqrt(v_g)>=2v_g`. Therefore

    sum_g sqrt(v_g) >= 2 sum_g v_g,

and hence

    [sum_g v_g] / [sum_g sqrt(v_g)]^2
       <= 1/[4 sum_g v_g]
       <= 1/rho.                                      (7)

Combining (1), (2), (3), and (7) yields

    delta <= sqrt(x(1-x)y(1-y))/rho.

Finally `x(1-x),y(1-y)<=1/4`, giving `delta<=1/(4rho)`. For the remaining 3-connected obstruction, standard `kappa(G)<=lambda(G)` gives edge-connectivity at least three, so deleting `e,f` preserves connectedness and `rho=|V(G)|-1`. QED.

## 3. Exact finite regression

The proof above is symbolic. A separate exact-rational checker was nevertheless run against every nonempty labelled simple graph on `n=2,3,4,5`. For each graph it enumerates all forests and checks the three generic ingredients used above: `p_g<=1/2`, `E K>=rho/2`, and `Var(K)<=sum_g Var(T_g)` (the last using the exact pairwise forest inequalities at these small sizes).

Captured output:

    n=2 graphs=1 min(mean-r/2)=0 max_p=1/2 max(VarK-sumv)=0
    n=3 graphs=7 min(mean-r/2)=0 max_p=1/2 max(VarK-sumv)=0
    n=4 graphs=63 min(mean-r/2)=0 max_p=1/2 max(VarK-sumv)=0
    n=5 graphs=1023 min(mean-r/2)=0 max_p=1/2 max(VarK-sumv)=0
    violations=0

Files beside this report:
- `variance_squeeze_check.py`
- `variance_squeeze_check.out`

The finite enumeration is regression evidence only; it is not used to justify the all-rank matroid facts or the all-graph conclusion.

## 4. What this pays and what remains unpaid

**Paid in this run:** the fleet02/B01 family of edgewise constraints is no longer merely a list of signs. It implies one global, rank-sensitive necessary inequality on the exact target deficit `delta`. The derivation includes disconnected forests automatically because `H` ranges over the full independent-set complex, not bases or rooted forests.

**Still unpaid:** this numerical squeeze alone does not rule out a 3-connected minimal counterexample. In particular, `delta` is a positive rational with denominator governed by the forest count and can be much smaller than `1/(4rho)`. Treating the new bound as closure would be exactly the forbidden mistake of promoting an auxiliary constant to a universal proof.

A next proof worker should combine the rank squeeze with genuinely graph-global information that lower-bounds the deficit or forces additional cancellation in the 3-connected core. A promising exact target is to strengthen (3) or (7) using the fact that all `a_g,b_g` are strictly positive *and* arise from endpoint-connectivity addability events, rather than arbitrary Bernoulli variables. Merely improving `1/(4rho)` without a contradiction is not enough.

## 5. Conditional end-to-end map

There are currently two compatible routes:

1. **Lead route:** exact `K_n` Hermite theorem -> source-checked Cocks fixed-graph upgrade -> weighted minor closure -> every simple graph by deletion. This is the strongest candidate and should be judged from its complete lead proof plus independent reviews, not from this auxiliary theorem.
2. **Minimal-counterexample route:** Cocks-paid deletion/contraction and separator transfer -> minimal obstruction is 3-connected -> strict all-third-edge sign forcing -> **this run's aggregate rank squeeze** -> still-missing graph-global contradiction.

This run strengthens route 2 but does not supersede or independently certify route 1.

## 6. Integrity and provenance

Only the private mathematics repository, the listed FOREST peer artifacts, and public mathematical sources were used. No benchmark answer material, credentials, scheduler identifiers, machine paths, unrelated private material, email, Drive, public posting, paid model/API, Codex, or remote workflow was used. A scoped manual review of the files created in this run found no secrets or unrelated data. No production population or historical artifact was modified.

`full_brain_connected=false`; no authenticated brain retrieval/context activation occurred in this run.
