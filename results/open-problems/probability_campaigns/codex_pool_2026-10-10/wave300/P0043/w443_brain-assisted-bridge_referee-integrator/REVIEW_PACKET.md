# P0043 referee packet — 2026-10-10

## Scope and source

The target is iid Bernoulli **bond** percolation on an infinite connected locally finite quasi-transitive graph with `p_c<1`. Hutchcroft (2016), Conjecture 1.1, states that scope and proves the exponential-growth subclass in Theorem 1.2. A public 24 September 2026 manuscript states the entire conclusion in Theorem 1.1; its Lean challenge, comparator configuration and separate solution module name the same bond theorem. I checked statements and the main module, not the full manuscript proof or the imported Lean dependency closure. Thus the current status is **publicly claimed solved; independent full verification pending**, not a new proof by this triad.

Sources: https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2016.07.013.pdf ; https://github.com/openai/math/blob/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf ; https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.json ; https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/CriticalPercolation/Main.lean .

## Peer verdicts

| Claim | Verdict | Reproduction and limit |
|---|---|---|
| w441-L001; w442-C001 | KEEP | On `Z`, an infinite root cluster at `p<1` requires an entire right or left ray, each probability `lim_n p^n=0`; at `p=1` all bonds are open. The two rows duplicate the same necessary `p_c<1` boundary. |
| w442-C002 | KEEP | For `0<a<1`, `f_n(p)=min(1,(p/a)^n)` is continuous, nondecreasing in `p`, nonincreasing in `n`; `inf_n f_n(a)=1` but `inf_n f_n(q)=0` for every `q<a`. For each `n`, `q_n=a(1/2)^(1/n)<a` has `f_n(q_n)=1/2`. This refutes the **uniform lower-bound** quantifier exchange only, not P0043. |
| w442-C003 | KEEP | Positive anchored boundary ratio `c` for all sufficiently large rooted connected sets would force `|B_H(o,r+1)| >= (1+c/Delta)|B_H(o,r)|`; `B_H(o,r) subset B_G(o,r)` contradicts subexponential ambient growth. This is a deterministic route obstruction. |
| w441-L002 | KEEP | Independently rederived: fresh independent `q` thinning of iid `p` bonds is iid `pq`; for each rational `q<min(1,p_c(G)/p)` no thinned infinite component exists. Tonelli plus countably many components gives the quenched statement simultaneously for those rationals; monotonicity gives `p_c(C)>=min(1,p_c(G)/p)` for every infinite sampled component. No independence of the selected clusters is assumed. |
| w441-L003 | KEEP | Injective images of the `b^n` depth-`n` vertices lie in `B_G(f(root),Ln)`. For arbitrary radius `r`, choose `n=floor(r/L)`, giving lower exponential growth `b^(1/L)`. The fixed corridor length and injectivity are essential. |
| w441-L004/L004b | FIX | The union bound is sound: at most `Delta^(2(n-1))` rooted connected `n`-sets via canonical depth-first walks, and a finite open root cluster `K` requires its `H`-edge boundary closed. The geometric sum is `a/(1-Delta^2 a)<1` when `a=(1-q)^h<1/(Delta^2+1)`. State the Bernoulli parameter as **`q in [0,1)`**, not merely `q<1`; the current wording permits undefined negative parameters. The critical-cluster corollary follows from L002 after this edit. |
| w441-L005 | FIX | At radius `2n+1`, `2^n` graft leaves prove only a subsequence bound. For every large integer `r`, set `n=floor((r-1)/2)`; all `2^n` leaves lie in `B(s_0,r)`, proving the claimed `liminf >= sqrt(2)`. Non-quasi-transitivity can be certified by the strictly increasing number of vertices in finite components of `H\{s_n}`. The counterexample to exponential growth alone is valid with these steps. |
| w441-L006 | KEEP, contingent on L004 wording fix | If `h>0`, L004 gives `p_c(C)<=1-(Delta^2+1)^(-1/h)` by letting `q` decrease to the sufficient threshold. L002 gives `p_c(C)>=p_c(G)/p`. Hence `(Delta^2+1)^(-1/h)<=(p-p_c)/p` and `h<=log(Delta^2+1)/log(p/(p-p_c))`. At `p=p_c`, the same two bounds force `h=0`. The bound is for each fixed `p`, not simultaneous over uncountably many `p`. |

## Brain comparison and one bounded repair

`python -X utf8 .\recall_probe.py` against `~/math-brain-build/local/population/brain.sqlite3` returned **0 theorem cards in the top five** for the named Hutchcroft/exponential-growth query. It returned the older P0043/C0084 open-problem and attempt cards, a Russo paper card, and unrelated exponential-growth cards. The top P0043 card says only `quasi-transitive` and `p_c<1`, omitting connected/local-finite/bond assumptions; its open status is expressly dated 2026-09-07. `RECALL_MEASURE.json` and `CARD_READS.json` hold the raw read-only receipts. Proposed repair: add the exact Hutchcroft 2016 theorem as a source-backed node, link it as a special case of P0043, and add a dated concept pointer to the later public full-scope claim. Ask the integrator to recheck status before replacing the old open label. A draft alone does not demonstrate retrieval improvement.

The single hard gap for any independent new proof is the subexponential case. L002 says a hypothetical critical infinite cluster dies under every independent `q<1` thinning. L004 supplies survival only under positive anchored expansion, and C003 rules that condition out for subexponential ambient growth. The 2026 manuscript claims other finite-connection and structural arguments; none were reproved here. A KEEP on these partial lemmas does not solve P0043.

No new lemma is claimed by w443; the corrected wording of L004/L005 is a referee fix. A newly authored lemma would require w446 review before theorem promotion.

NEXT: Have the coordinator review the exact theorem draft and the public comparator closure; remeasure the named query only after integration.
