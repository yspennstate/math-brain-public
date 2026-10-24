# FOREST / account04 B03 — loopless-minimality removes STAR-2, with an all-conditioner spectral squeeze

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** OPEN  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`  
**Run:** `20260922T070756Z-B03-forest-r12-34330b0f`

## 1. Exact inherited state and correction

The target remains the unit uniform law on **all** acyclic edge subsets of a finite simple graph. For distinct edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.

I read the latest complete team-lead version, account01/B01 `20260922T050946Z-b01-forest-auto11`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155` and canonical report created at `79044b575c4b689248892f37b9930e983dddabca`. Its first unpaid source step is the triangle-contraction `{1,2}` STAR-2 comparison. I also applied the later correction account01/B02 `20260922T054825Z`, shared blob `fb4265dc413059fc93e8dada0ef0ba90a008d947`: the rank-degree complete-log-concavity strengthening is false already on `K3`; only the ground-set-degree homogenization is retained.

Named OTHER-account input used substantively: account03/B02 `20260922T051758Z`, shared blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`. Its useful structural idea is to work with an edge-minimal **loopless multigraph** counterexample. I reprove below the portion needed here directly, without importing its separate Cocks-dependent 3-connectivity sentence.

For the spectral step I use Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, Theorem 4.1: the ground-set-degree homogenization of a matroid independent-set polynomial is completely log-concave.

## 2. The first missing coverage step disappears in the correct minimal class

Assume the simple-graph target is false. Then the larger class of finite loopless multigraphs (parallel labelled edges allowed, a parallel pair being a 2-cycle) contains a counterexample, because it contains every simple graph. Choose a counterexample `M` with the minimum number `m` of physical edges, and choose a violating pair `e,f`. Write `X_h=1[h in F]` under the uniform independent-set/forest law of `M`.

Fix any third physical edge `g`.

* Given `X_g=0`, the law is exactly the uniform forest law of `M\g`, which has fewer physical edges and hence is nonpositively correlated for every pair by minimality.
* Given `X_g=1`, delete the compulsory `g`. This is exactly the uniform independent-set law of `M/g`. Contraction may turn edges parallel to `g` into loops; deleting those loops changes no forest count because loops occur in no independent set. If `e` or `f` becomes such a loop, the conditional covariance is zero. Otherwise the loop-deleted contraction is a smaller loopless multigraph and is nonpositively correlated by minimality.

Therefore, for **every** third edge, not merely a triangle-free one,

`Cov(X_e,X_f | X_g=0) <= 0`,  
`Cov(X_e,X_f | X_g=1) <= 0`.

Let `C_ij=Cov(X_i,X_j)`, `v_i=Var(X_i)`, and suppose `C_ef=C>0`. The binary law of total covariance gives

`C = (1-p_g) C_ef|0 + p_g C_ef|1 + C_eg C_fg/v_g`.

Hence the exact all-conditioner Simpson inequality is

**(S)** `C_eg C_fg >= C v_g > 0` for every `g notin {e,f}`.

This directly pays the lead's STAR-2 contraction debt. In the lead's original simple frame, contracting a triangle edge produces parallel classes and was rewritten as a `{1,2}`-weighted star. In the loopless-multigraph minimal frame the same object is simply the smaller contraction minor itself, so no weighted closure theorem is needed. The aggregation of a size-two parallel class into a weight-two simple edge is exact but unnecessary for induction.

As a regression, on `K4` with `g=01`, `e=02`, `f=13`, conditioning on `g=1` gives counts `(Z,Z_e,Z_f,Z_ef,Delta)=(14,4,4,1,2)`. Contracting `01` gives the three-vertex multigraph with the two expected parallel classes and exactly the same five counts. The checker records this identity exactly; the proof above is general and does not rely on the finite check.

## 3. Global sign geometry: positive covariance is a matching

Standardize `rho_ij=C_ij/sqrt(v_i v_j)`. From (S),

`rho_eg rho_fg >= rho_ef =: a > 0`.

Thus `rho_eg` and `rho_fg` have the same nonzero sign for every third edge `g`. They cannot both be positive. If they were, all three pairs `(e,f),(e,g),(f,g)` would violate. Applying (S) cyclically gives

`a <= b c`, `b <= a c`, `c <= a b`

for `a=rho_ef,b=rho_eg,c=rho_fg` in `(0,1)`. Multiplication yields `1 <= abc`, impossible because distinct nonloop edge indicators in the uniform independent-set law are not almost surely identical. Therefore

**(M)** `C_eg<0` and `C_fg<0` for every third edge `g`.

Applying the same argument to any violating pair shows that the graph whose vertices are physical edges and whose edges are positive-covariance pairs is a matching. This upgrades the lead's triangle-free matching statement to **all physical edges**, including edges in triangles and parallel classes.

## 4. Source-valid ground-set CLC budget, now over every conditioner

Let `K=|F|`, `mu=E K`, `L=m-mu`, `c_i=Cov(X_i,K)`, and use the correct ALOV homogenization

`g(y,z)=sum_{I independent} y^(m-|I|) product_{h in I} z_h`.

At the all-ones point set `U=(m-K,X_1,...,X_m)`, `A=diag(E U)`, and `Sigma=Cov(U)`. Complete log-concavity gives `A-Sigma >=0`, while `Sigma>=0`. Therefore `N=A^(-1/2) Sigma A^(-1/2)` satisfies `0<=N<=I`, hence `N^2<=N`. Its edge diagonal yields, for every edge `i`,

**(B)**

`c_i^2/[L p_i(1-p_i)] + sum_{h!=i}(1-p_h) rho_ih^2 <= p_i`.

Every nonloop edge has `0<p_h<=1/2`, by the deletion injection from forests containing `h` to forests omitting it.

Add (B) for the violating pair `e,f`. Put

`T_i=c_i^2/[L p_i(1-p_i)]`.

The `e-f` terms contribute `(2-p_e-p_f)a^2 >= a^2`. For every one of the `m-2` third edges, (S) gives `rho_eg rho_fg>=a`, so

`(1-p_g)(rho_eg^2+rho_fg^2) >= (1/2)*2a = a`.

Since `p_e+p_f<=1`, we obtain the source-safe all-edge obstruction

**(A)** `T_e + T_f + a^2 + (m-2)a <= 1`.

This is the corrected ground-set-degree analogue of the lead's triangle-free budget, but its coverage set is now all `m-2` conditioners. In particular

`a <= [sqrt((m-2)^2+4)-(m-2)]/2`.

No rank-degree CLC statement is used.

## 5. A second new quantitative consequence: every third edge has an occupancy floor

The edge-only principal block of `A-Sigma` is PSD. By (M), for a third edge write

`A_g=-C_eg>0`, `B_g=-C_fg>0`.

The `(e,f,g)` block is

`[[p_e^2,-C,A_g],[-C,p_f^2,B_g],[A_g,B_g,p_g^2]]`.

Its determinant is nonnegative. Exact expansion and one square give

`p_g^2(p_e^2 p_f^2-C^2)-2 A_g B_g(p_e p_f+C)
 = det + (A_g p_f-B_g p_e)^2 >= 0`.

Using (S), `A_g B_g>=C p_g(1-p_g)`, therefore

`p_g(p_e p_f+C) >= 2C`.

So every third physical edge obeys

**(P)** `p_g >= 2C/(p_e p_f+C)`.

Since `p_g<=1/2`, this already forces

`C <= p_e p_f/3`, and therefore `rho_ef<=1/3`.

Summing (P) and using the deterministic rank bound `K<=r(M)` gives the further density squeeze

**(D)**

`2(m-2) C <= (r(M)-p_e-p_f)(p_e p_f+C)`.

This use of rank is only the elementary bound on forest size; it does not revive the refuted rank-homogenized CLC claim.

The exact symbolic checker verifies the determinant identity and the reduction of the Simpson substitution to `p_g(p_e p_f+C)-2C>=0`.

## 6. Compact conditional end-to-end argument and remaining debt

The corrected source-safe chain is now:

1. if a simple counterexample exists, choose an edge-minimal counterexample in the larger loopless-multigraph class;
2. every deletion and contraction minor is smaller after discarding loops, so both conditional strata for **every** third edge are good;
3. the lead's STAR-2 triangle-contraction gap is therefore paid exactly, with no external-field theorem;
4. all-conditioner Simpson gives the global matching sign geometry (M);
5. the correct ground-set-degree ALOV spectral budget then gives (A), while its 3-edge PSD block plus Simpson gives the occupancy floor (P) and density squeeze (D).

The parent FOREST conjecture is **not** closed by these inequalities. The first remaining universal debt is now genuinely global: rule out a loopless graphic-matroid independent-set law having one positive matched pair while every third edge is negatively correlated with both and simultaneously satisfying (S), (A), (P), and the graphic exchange constraints. Merely improving an auxiliary constant in (A) or (D) is not closure.

This run therefore records `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 7. Exact computation and failures preserved

`checker.py` verifies the determinant square identity, the occupancy-floor algebra, and the exact `K4` conditioning/contraction regression. `checker_output.txt` terminates `STATUS=PASS`.

Preserved failures/corrections:

- the lead's rank-degree CLC strengthening is not used;
- no fixed-graph Cocks unit-to-weighted implication is used;
- no universal STAR-2 monotonicity is asserted;
- no finite census is treated as proof;
- enlarging the minimal class to loopless multigraphs is an auxiliary contradiction frame, not a claim that the original theorem had a multigraph hypothesis.

## 8. Handoff

Recipient: account01/B01 lead and the FOREST team. The immediate useful replacement for the former STAR-2 branch is: work from an edge-minimal loopless-multigraph counterexample, import (S)/(M)/(A)/(P)/(D), and attack the residual global graphic compatibility rather than a weighted-star closure statement.
