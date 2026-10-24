# POS3 handoff — account03/B10 renewal odds control

**Run:** `20260922T092055Z-account03-B10-POS3-elliptic`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent:** POS3 remains **OPEN / NOT PROVED**.

Consumed named partner: account04/B11 r19, `proofnet24/collective-POS3/account04/B11/20260922T084137Z-B11-POS3-r19/REPORT.md`, blob `7d3327d016a644c5792c8ba6af5d3ade1779e122`.

Partner state: for the first strong-majority ideal chain block `C={c_1<...<c_m}`, `Q=P\C`, there are at most two first interrupters; the exact renewal coefficients are `beta_(q,j)=e(R_(q,j))/e(P)`, `m<=K=pi(P)`, and adjacent depth counts satisfy `N_(j+1)<=N_j<=K N_(j+1)`.

Applied prior actual-law block mass `4/9<alpha=e(Q)/e(P)<7/9`. Hence total nonprefix mass is `>2/9`, so some first-interrupter branch `q_*` has

`1/9 < beta_(q_*) < 1/3`.

The upper bound uses the actual full-law event `q_*<c_m`, whose probability is `<1/3` in a no-balanced candidate.

For `ell=m-lambda(q_*)<=K`, adjacent count comparability gives every depth coefficient

`beta_(q_*,j) > (K-1)/(9(K^ell-1)) >= (K-1)/(9(K^K-1))`.

More importantly, adjacent channel laws admit an exact measure-level size bias. For `c=c_(j+1)`, map a depth-`j` extension to depth `j+1` by moving `c` left to immediately before `q`. A target extension has exactly

`W_j=1+t in {1,...,K}`

preimages, where `t` is the initial run after `q` of elements incomparable with `c`. The move preserves the relative order of every element of `Q`. Thus for every Q-order event `A`,

`mu_j(A)=E_(mu_(j+1))[W_j 1_A]/E_(mu_(j+1))[W_j]`,

and therefore

`1/K <= odds(mu_j(A))/odds(mu_(j+1)(A)) <= K`.

Across `d` depths the odds distortion is at most `K^d`. Consequently, if a fixed Q-pair is balanced in one heavy-branch depth, its minority probability in every other depth is at least

`1/(1+2K^(ell-1)) >= 1/(1+2K^(K-1))`.

Since the branch itself has full-law mass `>1/9`, each orientation of that pair contributes more than

`1/[9(1+2K^(K-1))]`

to the original full law from this branch alone.

**Exact change in the residual:** depth-to-depth migration inside one heavy interrupter branch is no longer an unconstrained family of residual laws. The remaining escape must use a top-level Simpson displacement among the prefix/other branch/heavy branch, or a balanced pair whose identity essentially uses a surviving chain-tail element and hence is not a common Q-order event.

Next statement: `POS3-TOPLEVEL-OR-CHAINTAIL-BACKTRACK-MIGRATION-v1`. Couple the lead's disjoint external exact-backtrack packets to those two remaining escape mechanisms and force balance, span descent, or a proper ordinal/autonomous reduction.

Execution context remains `WITHOUT_VERIFIED_BRAIN_RESEARCH`; no induced law was renamed uniform.
