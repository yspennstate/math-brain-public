# FOREST / account01 B20 — Jacobi closure of the Hermite step and source-bound end-to-end check

**Run:** `20260922T042049Z-B20-r11`  
**Run classification:** `ESSENTIAL_STEP_APPLIED`  
**Integrated candidate status after this run:** `FULL_PROOF_CANDIDATE` internally, not an external solved-problem/priority claim.  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target

For every finite simple graph `G=(V,E)`, choose `F` uniformly from all acyclic edge subsets of `E`, including the empty forest, disconnected forests, and every forest size. For all distinct `e,f in E`, prove

`Pr(e,f in F) <= Pr(e in F) Pr(f in F)`.

Equivalently, if `Z,Z_e,Z_f,Z_ef` count forests with the indicated marked-edge containments,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

## 2. Exact lead and OTHER-account versions consumed

The newest complete campaign-lead version available at invocation time was account01/B01 run

`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T030948Z-b01-forest-auto11/report.md`,

blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`, candidate `FOREST-KN-COCKS-RECONCILED-v3`, internally classified `FULL_PROOF_CANDIDATE`. The newer B01 `20260922T040935Z-b01-forest-r11` had only its start artifact at the source snapshot, so I did not infer mathematics from it.

The named OTHER-account result consumed and applied was partner account04/B03 run

`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T030927Z-B03-forest-r11/report.md`,

blob `571f84cd2916cdf6dc2b70d8160bf54d79e162c9`. The newer account04/B03 `20260922T040956Z-B03-forest-r12` likewise had only a start artifact at the source snapshot. The completed partner report independently rederived the complete-graph candidate and, using account02/B03's parallel-class aggregation identity, derived a weighted multigraph lift. I use that exact identity below rather than merely citing the partner.

## 3. Compact conditional end-to-end chain

The lead candidate reduces the theorem to the following chain.

1. Prove the unit uniform-all-forests pairwise inequality for every complete graph `K_n`.
2. Apply the fixed-graph theorem attributed to Cocks in the final Semple--Welsh paper: if a graph `G` satisfies their Conjecture 1.1, then `M(G)` is independence correlated, i.e. its independent-set Rayleigh difference is nonnegative for every positive edge weighting.
3. Apply Semple--Welsh Proposition 3.5: independence-correlated matroids are closed under minors.
4. Every finite simple `G` on `n` vertices is obtained from `K_n` by deleting nonedges (isolated vertices are irrelevant). Hence `M(G)` is independence correlated; set all surviving weights to one.

Thus the only original mathematics needed here is Step 1, while Steps 2--3 are imported published results. I found one implicit load-bearing point in Step 1 that the lead report stated but did not itself prove: the Hermite evaluation point lies to the right of every zero, and the required zero symmetry/second-moment identity. The next section pays that step from first principles.

## 4. New exact Jacobi--Hermite lemma

Let `He_k` be the probabilists' Hermite polynomial, normalized by

`He_0(x)=1`, `He_1(x)=x`, `He_{j+1}(x)=x He_j(x)-j He_{j-1}(x)`.

For `k>=1` let `J_k` be the real symmetric tridiagonal matrix with zero diagonal and off-diagonal entries

`sqrt(1), sqrt(2), ..., sqrt(k-1)`.

### Lemma 4.1 — exact spectral representation

`det(x I_k-J_k)=He_k(x)`.

**Proof.** Let `p_j(x)` be the determinant of the leading `j x j` block. Expanding the last row/column gives

`p_j=x p_{j-1}-(j-1)p_{j-2}`

with `p_0=1`, `p_1=x`. Hence `p_j=He_j` by the defining recurrence. QED.

Consequences, with roots `lambda_1,...,lambda_k` of `He_k`:

* all roots are real, because `J_k` is real symmetric;
* they are symmetric about zero, because with `D=diag(1,-1,1,-1,...)` one has `D J_k D=-J_k`;
* their squared sum is exact:

`sum_i lambda_i^2 = tr(J_k^2)=2 sum_{j=1}^{k-1} j = k(k-1)`;

* for `k>=2`, every root obeys

`|lambda_i| <= ||J_k||_infty <= sqrt(k-2)+sqrt(k-1) < 2 sqrt(k-1)`.

For the lead substitution `k=n-4` and `x=n+1=k+5`,

`x=k+5 > 2 sqrt(k-1)`

because, writing `u=sqrt(k-1)`, `k+5=u^2+6>2u`. The cases `k=0,1` are immediate. Therefore `x` lies strictly to the right of every Hermite zero for every needed `k`.

### Lemma 4.2 — the exact lower bound used by the complete-graph proof

Using `He_k'(x)=k He_{k-1}(x)`, put

`s = k He_{k-1}(x)/He_k(x)` at `x=k+5=n+1`.

By Lemma 4.1 and the logarithmic derivative,

`s = sum_i 1/(x-lambda_i)`.

Pair every nonzero root `lambda` with `-lambda`. Since `|lambda|<x`,

`1/(x-lambda)+1/(x+lambda)`
`=2x/(x^2-lambda^2)`
`=(2/x)/(1-lambda^2/x^2)`
`>=2/x+2 lambda^2/x^3`.

A possible zero root contributes exactly `1/x`. Summing all pairs and using `sum lambda_i^2=k(k-1)` gives

`s >= k/x + k(k-1)/x^3`
`= (n-4)/(n+1) + (n-4)(n-5)/(n+1)^3`
`= (n-4)(n-1)(n+4)/(n+1)^3 =: L_n`.

This proves, from the Hermite recurrence alone, every zero fact used in the lead's all-`n` bound. No external theorem on Hermite zero locations is needed.

## 5. Reproduction of the complete-graph positivity

With `k=n-4`, `H_j=He_j(n+1)` and the same `s`, the lead's Cauchy/Lagrange coefficient calculation gives

`J_dis/H_k=5-s`,
`J_adj/H_k=4-s`,
`E/H_k=2n+6-3s`,
`Z/H_k=n^2+3n+10-(n+4)s`.

Thus the disjoint-edge gap divided by `H_k^2` is

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Also `J_dis-J_adj=H_k>0`, hence the disjoint orbit is the harder orbit. For `n>=6`, `G_n` is increasing on `[0,1]` because

`G_n'(1)=n^2-6n+4>0`

and the derivative is affine with negative slope. The coefficient representation gives `0<=s<1`, and Lemma 4.2 gives `s>=L_n`. Therefore

`G_n(s)>=G_n(L_n)`.

Exact symbolic simplification gives

`(n+1)^6 G_n(L_n)`
`=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Writing `n=t+6`, this is

`2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0`.

The lead's exact small cases are `K_3` adjacent gap `2`, `K_4` disjoint gap `6`, and `K_5` disjoint gap `210`, so every complete graph is covered.

I independently rechecked the load-bearing algebra symbolically. The exact script is `verify_hermite_algebra.py`; exact output is `verify_hermite_algebra.out`:

```text
G(s)= n**2*s - n**2 - n*s**2 - 4*n*s + 9*n + 5*s**2 - 6*s - 14
(n+1)^6 G(L_n)= 2*n**6 + 70*n**5 - 33*n**4 + 185*n**3 + 1369*n**2 - 3147*n + 1170
n=t+6: 2*t**6 + 142*t**5 + 3147*t**4 + 33233*t**3 + 187651*t**2 + 551661*t + 666396
ALL_EXACT_SYMBOLIC_CHECKS_PASS
```

The computation is an audit only; the proof is the symbolic argument above.

## 6. Published bridge rechecked against the final source

The final Charles Semple--Dominic Welsh paper, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423--435, DOI `10.1017/S0963548307008978`, defines independence correlation using **all positive real weightings**. Proposition 3.5 explicitly proves that independence-correlated and spanning-correlated matroids are each closed under minors. The same final paper's post-submission Note states that Cocks proved: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated, settling their open question (3).

The cited Cocks article is Clifford C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`. Its published abstract says the Grimmett--Winkler and Pemantle conjectures are equivalent to statements about correlated graphic matroids.

I could inspect the final Semple--Welsh statement and its full minor-closure proof in this run, but not the body of the Cocks article itself. Therefore I treat Cocks's fixed-graph theorem as a published imported theorem explicitly recorded by Semple--Welsh, not as a theorem independently reproved here. If direct inspection of Cocks later contradicts that exact attribution, the candidate must immediately fall back and the weighted-complete-graph bridge becomes unpaid again.

With the published theorem accepted exactly as stated, the end-to-end deduction is now complete:

`unit pNC on every K_n`
`=> M(K_n) independence correlated` (Cocks)
`=> every deletion minor M(G) independence correlated` (Semple--Welsh Proposition 3.5)
`=> Delta_G(e,f)>=0 at unit weights`.

## 7. Application of the named OTHER-account result

I applied account04/B03's completed multigraph integration, which in turn uses account02/B03's exact parallel-class identity. For a loopless multigraph `M`, collapse each parallel class `C` to one simple quotient edge and set

`Y_C=sum_{h in C} y_h`.

Because an acyclic set contains at most one edge from a parallel class,

`Z_M({y_h})=Z_Q({Y_C})`.

For marked edges in different classes, the relevant first and second derivatives agree with those of the quotient; for two marked edges in the same class, joint inclusion is impossible. Hence the simple-graph all-positive-weight theorem supplied by Cocks plus the completed simple-graph proof yields pairwise negative correlation for **arbitrary positive edge weights on finite multigraphs** as well. This strengthening is not needed for the user's simple/unit target, but it verifies that parallel multiplicities introduced by matroid operations are not silently being discarded.

## 8. Honest status and public-literature cross-check

Current public references still describe the general uniform-forest edge-negative-association conjecture as open, and Stark's 2011 result only covers complete graphs for sufficiently large `n`. This makes the all-`n` complete-graph Hermite argument the genuinely novel load-bearing ingredient and makes ordinary publication-level scrutiny essential before any external announcement.

**Run classification: `ESSENTIAL_STEP_APPLIED`.** The new step is Lemma 4.1--4.2, which closes the lead's implicit Hermite-root-location/symmetry/second-moment assumption from first principles. After incorporating this step, I find no mathematical gap in the internal end-to-end chain **provided the published Cocks theorem is used exactly as recorded in the final Semple--Welsh Note**. Thus the integrated object remains an internal `FULL_PROOF_CANDIDATE`, not an externally verified resolution.

## 9. Failures / boundaries

* The newest same-hour B01 and account04/B03 runs had only start artifacts when inspected; I used the newest completed versions and did not infer future results.
* The body of Cocks (2008) was not directly accessible in this runtime; only the final Semple--Welsh explicit theorem attribution and the Cocks publication/abstract were available.
* No brain retrieval was used; status is `WITHOUT_VERIFIED_BRAIN`.
* No public posting, email, Drive, paid model/API, remote workflow, benchmark work, brain-installation work, permission changes, or cross-account native action occurred.

## 10. Source-bound handoff

The next FOREST worker should treat `FOREST-KN-COCKS-RECONCILED-v3 + B20-JACOBI-CLOSURE-20260922` as the current compact candidate. Do **not** spend another run reproving the basic Hermite zero facts: the Jacobi matrix proof above is complete. The highest-value remaining action is direct inspection of the original Cocks proof (or an independent self-contained reconstruction of the fixed-graph upgrade), followed by journal-grade line-by-line review of the complete-graph coefficient identities. If either fails, report the exact first broken implication rather than preserving the `FULL_PROOF_CANDIDATE` label.

## 11. Model / effort metadata

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured effort: `UNKNOWN / NOT_EXPOSED`. Provider reasoning/usage counters: `UNKNOWN / NOT_EXPOSED` (not zero). Elapsed execution time is recorded separately at finish and is not pure thinking time.
