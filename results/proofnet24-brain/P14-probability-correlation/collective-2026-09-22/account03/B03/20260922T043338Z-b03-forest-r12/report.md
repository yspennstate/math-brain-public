# FOREST — source-exact complete-graph module and clique-theta stress family

Candidate: `FOREST-STARK-THETA-EXACT-v1`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent status: **INTERNAL FULL-PROOF CANDIDATE EXISTS; public theorem/novelty/priority UNVERIFIED**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact target, assignment, and peer used

Target: for every finite simple graph `G=(V,E)`, uniformly over **all** acyclic edge subsets (including the empty forest, disconnected forests and every forest size), prove

`Z_e Z_f - Z Z_ef >= 0`

for every distinct pair of edges `e,f`.

Exact account03/B03 assignment: compute exact forest-pair counts for new asymptotic/structured adversaries to the shared candidate and use failures to derive the missing structural constraint, not a census-only report. Assigned partner: `account04/B01`.

This run substantively consumes the named OTHER-account partner theorem `FOREST-2CUT-MULTIBRIDGE-GLUING-v1`, handoff blob `312f5f1292906f995232fcae9d0281ba84146137`. For a two-vertex separator `{u,v}` with edge-disjoint `uv` bridges `B_i`, writing `D_i` and `C_i` for the weighted forest polynomials with `u,v` respectively disconnected and connected, the partner proved

`I_G = prod_i D_i + sum_i C_i prod_(j!=i) D_j`.

For marked edges in one bridge, the outside graph acts exactly as a positive virtual `uv` edge of weight

`lambda_i = sum_(k!=i) C_k/D_k`,

and the global Rayleigh difference is the local weighted difference times the positive square factor `A_i^2`. For marked edges in distinct bridges, the sign factors as `A_ij^2 R_i(e)R_j(f)`. I use these identities below rather than inheriting a PASS label.

The current lead complete-graph candidate is account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Prior independent review blobs `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e` and `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc` checked its end-to-end chain. The present run independently source-exactifies its delicate complete-graph enumeration and then constructs a new structured stress family.

## 2. Source-exact complete-graph generating functions

Dudley Stark, *The Edge Correlation of Random Forests*, Annals of Combinatorics 15 (2011), 529–539, DOI `10.1007/s00026-011-0104-7`, uses the standard rooted-tree series `R=z exp(R)` and unrooted-tree series

`T = R - R^2/2`, `F=exp(T)`, `A=T'=exp(R)`.

His exact labelled decompositions give the same three marked-edge formulas used by the lead:

`Z_n = n! [z^n] F`,

`E_n = (n-2)! [z^(n-2)] F A^2`,

`J_adj = (n-3)! [z^(n-3)] F A^3`,

`J_dis = (n-4)! [z^(n-4)] F A^4 (1+4/(1-R))`.

The delicate factor is source-exact: `T''=A^2/(1-R)`, and when two disjoint marked edges lie in the same tree, deleting them leaves three components with four endpoint pairings, producing the `4/(1-R)` term. Thus the candidate is not relying on a guessed disjoint-pair EGF.

## 3. One-line Cauchy/Hermite extraction

Here is a self-contained coefficient lemma that makes every index transparent.

**Lemma.** For integers `m,r>=0`, put `x=m+r+1`. Then, with probabilists' Hermite polynomials `He_j`,

`m! [z^m] F A^r = He_m(x)-m He_(m-1)(x)`,

and

`m! [z^m] F A^r/(1-R) = He_m(x)`.

**Proof.** In the Cauchy integral substitute `z=u exp(-u)`, so `R=u` and `dz=exp(-u)(1-u)du`. Since `F=exp(u-u^2/2)` and `A^r=exp(ru)`, the first integrand becomes

`u^(-m-1) exp(xu-u^2/2)(1-u) du`.

The Hermite generating function `exp(xu-u^2/2)=sum_j He_j(x)u^j/j!` gives the first identity. Division by `1-R=1-u` cancels the Jacobian factor and gives the second. QED.

For every complete-graph marked count above, `m+r+1=n+1`. Writing

`H_j=He_j(n+1)`, `D_j=H_j-j H_(j-1)`,

the source formulas therefore give exactly

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj=D_(n-3)`, `J_dis=D_(n-4)+4H_(n-4)`.

This independently derives the candidate's Hermite identities directly from the published labelled forest decomposition.

## 4. All-n sign, independently compressed

Put `k=n-4`, `a=H_k`, and

`s=k H_(k-1)/H_k`.

Hermite recurrence gives

`J_dis/a = 5-s`,

`E_n/a = 2n+6-3s`,

`Z_n/a = n^2+3n+10-(n+4)s`.

Hence the harder disjoint-edge Rayleigh gap is

`E_n^2-Z_n J_dis = a^2 G_n(s)`,

where

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Let `lambda_1,...,lambda_k` be the real roots of `He_k` and let `x=n+1=k+5`. Root symmetry gives

`s = x sum_i 1/(x^2-lambda_i^2)`.

Also `sum_i lambda_i^2=k(k-1)`. Since `u -> 1/(x^2-u)` is convex on the relevant interval, Jensen gives

`s >= J_n := kx/(x^2-(k-1)) = (n-4)(n+1)/(n^2+n+6)`.

The positive labelled coefficient `D_k=H_k(1-s)` gives `0<s<1`. For `n>=6`, `G_n` is increasing on `[0,1]` because its derivative is minimized at `s=1` and

`G'_n(1)=n^2-6n+4>0`.

Direct substitution gives

`G_n(J_n)=(3n^4+40n^3-59n^2+488n-280)/(n^2+n+6)^2`.

Putting `n=t+4`, the numerator becomes

`3t^4+88t^3+709t^2+2704t+4056>0`.

Thus the disjoint gap is strictly positive for every `n>=6`. Moreover `J_dis=J_adj+H_(n-4)` with `Z_n,H_(n-4)>0`, so the adjacent gap is larger. The exact small cases are positive (`K_3` adjacent gap `2`; `K_4` disjoint gap `6`; `K_5` disjoint gap `210`). Hence every `K_n` satisfies the unit unrooted-forest pairwise inequality.

## 5. New structured adversary family: clique-theta graphs

For integers `m>=3`, `r>=2`, define `Theta(m,r)` by taking `r` copies of `K_m-uv`, making the copies share exactly the two vertices `u,v`, and keeping their other vertices disjoint. There is no edge `uv`. These are finite **simple** graphs with many overlapping cycles; they retain the actual target measure over all unrooted forests.

For one bridge `B=K_m-uv`, let `Z=Z_m`, `P=E_m`, and let `Q_a,J_adj` and `Q_d,J_dis` denote the two complete-graph pair counts. Then the bridge connectivity counts are exactly

`D=P`, `C=Z-2P`.

Indeed, forests of `K_m` containing `uv` are in bijection (delete `uv`) with forests of `K_m-uv` in which `u,v` are disconnected. For a marked bridge edge `h`, let `Q_tau` be `Q_a` or `Q_d` according as `h` is adjacent or disjoint from `uv`. Then

`D_h=Q_tau`, `C_h=P-2Q_tau`.

Applying the partner's gluing theorem gives the total count

`Z_Theta = D^r + r C D^(r-1)`.

For `e` in bridge 1 and `f` in bridge 2,

`Delta_Theta(e,f)=D^(2r-4) R_e R_f`,

where

`R_h = D C_h-C D_h = P^2-Z Q_tau`.

Thus every cross-bridge sign reduces exactly to a complete-graph Rayleigh gap involving `h` and the missing boundary edge `uv`.

For `e,f` in the same bridge, the outside graph induces the exact virtual weight

`lambda=(r-1) C/D = (r-1)(Z/P-2)`,

and

`Delta_Theta(e,f)=D^(2r-2) Delta_(K_m, w(uv)=lambda)(e,f)`.

This is not a new assumption: it is the assigned partner's exact weighted gluing identity specialized to an explicit simple family.

## 6. Structural constraint exposed by the stress family

Stark's complete-graph asymptotics give

`Z_m = sqrt(e) m^(m-2) + (5/2)sqrt(e)m^(m-3) + (11/8)sqrt(e)m^(m-4) + O(m^(m-5))`,

`P_m = 2sqrt(e)m^(m-3) + 4sqrt(e)m^(m-4) - (23/4)sqrt(e)m^(m-5) + O(m^(m-6))`.

Therefore

`Z_m/P_m = m/2 + 1/4 + 13/(8m) + O(m^-2)`,

so the bridge response is

`C/D = Z_m/P_m-2 = m/2 - 7/4 + 13/(8m) + O(m^-2)`,

and, for fixed `r>=2`,

`lambda=(r-1)(m/2 - 7/4 + 13/(8m)+O(m^-2)) -> infinity`.

**Structural consequence.** A separator/globalization proof that controls only unit boundary weight, or only weights in any fixed bounded interval, cannot cover all simple clique-theta graphs. The all-graphs argument genuinely needs positive-weight control for arbitrarily large virtual boundary response. This explains why the Cocks fixed-graph upgrade to all positive weights is not cosmetic: it supplies exactly the missing closure demanded by explicit source-valid simple graphs.

This family therefore stress-tests the shared candidate rather than merely enlarging a finite census.

## 7. Exact regression

The accompanying standard-library checker independently verifies:

- brute forest enumeration equals the Hermite formulas for `K_3,...,K_6`;
- the Jensen/Hermite sign identities exactly for every `6<=n<=2000`;
- exact total/single/pair counts for clique-theta cases `(m,r)=(3,2),(4,2),(4,3),(5,2)`;
- the partner's cross-bridge factorization on those graphs;
- the same-bridge weighted gluing identity at its exact rational `lambda` for `(4,2),(4,3),(5,2)`.

Representative exact outputs include

`Theta(4,3)`: cross-bridge `Delta=51744`, response `C/D=5/7`; same-bridge `lambda=10/7`, `Delta=2000768`.

`Theta(5,2)`: cross-bridge `Delta=410760`, response `C/D=35/31`; same-bridge `lambda=35/31`, `Delta=17690004`.

The computed response already grows from `5/7` at `m=4` to approximately `23.2836` at `m=50`, consistent with the proved asymptotic. Computation is regression only; the displayed identities and asymptotics are the mathematical argument.

## 8. All-graphs bridge and status

The final Semple–Welsh paper records Cocks's fixed-graph result: if Grimmett–Winkler Conjecture 1.1 holds for a graph `G`, then its graphic matroid `M(G)` is independence correlated; Semple–Welsh Proposition 3.5 proves independence correlation is minor-closed. Independence correlation is the positive-weight pairwise property. Therefore

`unit pNC on every K_n`
`=> positive-weight IC of M(K_n)`
`=> positive-weight IC of every deletion minor`
`=> unit pNC for every finite simple n-vertex graph`.

Every graphic-matroid independent set is precisely an acyclic edge subset, so this transfer retains disconnected forests, all forest sizes, the empty forest, and arbitrary isolated vertices. No rooted or fixed-size measure is substituted.

Cocks's 2008 published abstract also states that the Grimmett–Winkler conjecture is equivalent to statements about correlated graphic matroids. The current 2026 literature found by the campaign still describes the full all-graphs uniform-forest problem as open; Tang–Zhang 2026 proves different complete-graph fixed-component/excess regimes for sufficiently large `n`, not this theorem. Consequently this repository result remains an **internal full-proof candidate** pending ordinary expert/source scrutiny. No public solved-problem, novelty, or priority claim is made here.

## 9. Earliest remaining scientific gate and recipients

I find no new mathematical counterexample to the candidate chain. The first remaining gate is **external/source-level validation of the complete published Cocks implication together with the exact Stark-to-Hermite coefficient extraction**, followed by ordinary expert scrutiny of the assembled proof before any public claim. In particular, a search miss is not novelty evidence.

Recipients: campaign lead `account01/B01` and assigned partner `account04/B01`. The lead should integrate the Cauchy extraction as the shortest source-to-Hermite bridge and retain the clique-theta family as an adversarial explanation for why unrestricted positive virtual weights are structurally necessary.
