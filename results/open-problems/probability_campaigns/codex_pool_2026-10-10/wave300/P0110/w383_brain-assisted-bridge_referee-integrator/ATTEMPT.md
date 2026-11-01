# P0110: referee attempt and bridge audit

The exact cited question is Auffinger–Damron–Hanson, Section 4.3, Question 22: find a passage-time distribution for which equation (4.19), `chi=2xi-1`, holds. The intake specializes this to a nondegenerate iid undirected nearest-neighbor lattice law. The survey says its exponent definitions and existence are themselves part of the problem. The September ranking's `attempted_un` is historical; current openness is UNKNOWN.

## Source hypothesis versus the proposed bridge

| Input | Primary theorem requires | Peer deductions establish |
|---|---|---|
| Model | iid nonnegative weights on `Z^d`, `d>=2`; Chatterjee Theorem 1.1 also assumes nearly-Gamma and a finite MGF near zero; Auffinger–Damron assumes an atom at the support infimum smaller than `p_c(d)` | w381 L1–L5 use iid weights in `[a,b]`, `0<a<b`; Uniform[1,2] fits this support class |
| Upper endpoints | uniform exponential moments for centered passage times and geodesic deviation over **every** nonzero displacement | an assumed uniform centered-time envelope yields a **directional** deviation tail along rounded minimizers of `g(u)`; w382 turns its full tail into a directional exponential moment |
| Lower endpoints | uniform variance and expected-deviation lower bounds; Chatterjee A3–A4 exclude a finite ball, while Auffinger–Damron printed (2.2) ranges over every nonzero displacement | no lower fluctuation or wandering endpoint; for Uniform[1,2], the printed Auffinger–Damron all-v lower wandering bound fails at `e_1` |
| Conclusion | `chi_a=chi_b` and `xi_a=xi_b` imply `chi=2xi-1`; Auffinger–Damron Theorem 2.2 does **not** need nearly-Gamma | neither exponent equality for a concrete law is established |

## Independent load-bearing checks

I rederived w381 L2 by writing `T(0,v)=T(0,z)+T(z,v)` along a minimizing path and substituting `T=g+b+X`; the interior biases appear with minus signs. For L3, the Euclidean excess inequality holds even if the perpendicular projection of `z` overshoots an endpoint: the closer-endpoint distance is `r`, the other leg is at least `L` and `r`, so `S-L>=r>=2r^2/S`. For L4, compactness gives `rho=min_{|u|=1}g(u)>0`; rounding `nu` to `v_n` changes its norm by at most `bd/2+rho sqrt(d)/2`. Every geodesic vertex is in the deterministic lattice set `Lambda_n`, and the distance-to-segment maximum along an edge occurs at an endpoint, so w381 L5's finite union bound is valid without independence of path-dependent variables. Exact verdicts and remaining gaps are in `CLAIMS.jsonl`.

w382's rare-tail example is an exact scalar counterexample to upgrading variance/mean exponents to uniform exponential endpoints. Its all-`t` tail upgrade is correct: with `Y=((D-sqrt(U))_+)^2/V`, `P(Y>t)<=e^-t`, `E e^(Y/2)<=2`, and Young's inequality yields the stated uniform exponential moment for `r>tau`. It remains directional under w381's inputs. For the small-displacement check, any alternative path between adjacent vertices has at least three edges; if `b<3a`, the direct edge is uniquely cheapest and `D(0,e_1)=0`. That invalidates an application of Auffinger–Damron's printed all-v premise to Uniform[1,2], while leaving Chatterjee's asymptotic A4 untouched.

I also composed the two peer steps with Chatterjee's published nonrandom-fluctuation theorem as a **pending conditional corollary**. For Uniform[1,2] and any `q>chi_a`, A1 gives the uniform centered envelope at scale `|w|^q`, while Chatterjee Theorem 4.1 gives `h(v_n)-g(v_n)=O(n^q log n)`. Then w381's complete finite-scale tail and w382's all-`t` upgrade give a uniform exponential moment of `D(0,v_n)/n^r` for every `r>(1+q)/2`. Letting `q` decrease to `chi_a` gives a directional upper endpoint at most `(1+chi_a)/2`. This is a composition of known and reviewed conditional steps, makes no novelty claim, and has been left out of the draft bundle pending the named referee w386. It still says nothing about every lattice direction or either lower endpoint.

## Brain finding and bounded repair

Read-only recall on 10,650 nodes and 15,700 edges put the Chatterjee conditional-theorem card at rank 9 for the exact P0110 query and rank 6 for a theorem-hypotheses query (`RETRIEVAL_MEASURE.json`). The P0110 card had no direct edge to either conditional theorem card (`TARGET_LINKS.json`). A strictly in-memory two-link simulation moved Chatterjee 9→7 on the first query and the Auffinger–Damron card 5→4 on the second (`LINK_SIMULATION.json`); this is a modest simulated gain, not a live recall improvement. The bigger content error is a stored card claiming the nearly-Gamma requirement remains for equality. Auffinger–Damron Theorem 2.2 explicitly gives conditional equality without it; the source-backed FIX is in `CORRECTIONS.jsonl`.

## Hardest open piece and next proof step

The single load-bearing gap is a concrete iid undirected law with matched **global** strong fluctuation and wandering endpoints. Before applying the 2014 theorem to Uniform[1,2], resolve its literal all-v lower premise; Chatterjee's A3–A4 are the suitable large-distance source for that law. A next mathematical step is to try an all-direction counterpart of w381's deviation tail under an assumed `q`-scale centered envelope, explicitly locating where lack of upper/lower curvature of the actual FPP norm blocks the bound. This still would only advance an upper endpoint; the lower endpoints require separate work.
