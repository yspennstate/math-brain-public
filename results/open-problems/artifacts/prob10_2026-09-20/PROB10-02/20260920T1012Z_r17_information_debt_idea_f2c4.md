# R17 PROB10-02 idea before code — mismatch-root information refinement and the boundary-debt obstruction

Model requested: GPT-6 maximum reasoning. No authenticated applied-model / applied-effort selector or receipt is exposed in this runtime, so actual reasoning metadata is UNVERIFIED unless separately authenticated.

Target remains the true iid-uniform binary Chvatal–Sankoff constant. The same source bit is reused along a row/column of the LCS dynamic program; no independent Bernoulli matching array is introduced.

## Exact question for this run

The previous R17 run proved an exact recursive Bellman congruence but left essentially all mismatch-root classes. The next attempt therefore asks whether one can exploit **one extra source bit of lookahead without paying the full new-state cost**.

For an ell-window mismatch state s=(a,b), write the ordinary one-vector Bellman branches

A_h(s)=E_u h(a_2...a_ell u,b),
B_h(s)=E_v h(a,b_2...b_ell v).

If the next unseen bits u,v were revealed before choosing which string to advance, the tempting one-step value is

P_h(s)=E_{u,v} max{h(a_2...a_ell u,b), h(a,b_2...b_ell v)}.

Pointwise P_h(s)>=max{A_h(s),B_h(s)}. The crucial issue is whether P can be iterated while keeping the genuine source law. If choosing A depends on v, then v is not consumed and the posterior law of the unconsumed boundary bit is generally biased. The same issue occurs symmetrically for B.

### Attack 1 — exact no-free-peek theorem

Prove or falsify the following: any randomized action rule p(u,v)=P(advance A|u,v) for which, after the action, the unconsumed boundary bit remains conditionally fair given the chosen action and the consumed bit must have p(u,v) constant in (u,v). If true, no nontrivial memoryless max/expectation swap can preserve the iid projection exactly.

The intended algebra is to impose

p(u,0)=p(u,1) for each u

so that v is fair after choosing A conditional on u, and

1-p(0,v)=1-p(1,v) for each v

so that u is fair after choosing B conditional on v. These equations force all four p(u,v) equal. This is an exact obstruction, not an asymptotic heuristic.

### Attack 2 — minimal exact repair by a boundary-debt state

If Attack 1 succeeds, build the exact repaired state machine that records an exposed-but-unconsumed extra bit. At a clean state N, one may inspect one or both next bits. If A is advanced, a revealed v on B that was not consumed becomes debt Bv; if B is advanced, a revealed u becomes debt Au. The state therefore needs at least

N, A0, A1, B0, B1

as boundary-information statuses unless the action rule is trivial in the sense of Attack 1. Derive the exact transition law and Bellman/average-reward dual for this finite process. The goal is not to claim an endpoint from a small computation; it is to identify precisely what information must be carried to preserve dependence.

A useful strengthening would be a minimality statement: any exact Markov compression that permits an action to depend nontrivially on an unconsumed revealed bit must distinguish its two values somewhere in the state.

### Attack 3 — try to collapse debt by deterministic run-prefix dominance

A possible escape is that the action at a mismatch may be determined from the observed runs, so the extra bit is irrelevant on a large class of states. Test the natural deterministic claim: with opposite heads and leading run lengths i<j, advancing the shorter-run string is always weakly optimal for deterministic finite LCS continuation. If false, preserve the smallest exact counterexample and use it to rule out a run-length-only universal dominance shortcut.

## Success / failure criteria

A source endpoint moves only if a proved transfer changes the certified interval. Otherwise mechanism progress is recorded separately. The run stays OPEN/PARTIAL unless the full source target is closed with independent validation. Any finite check is evidence only unless paired with the written all-state proof it is checking.
