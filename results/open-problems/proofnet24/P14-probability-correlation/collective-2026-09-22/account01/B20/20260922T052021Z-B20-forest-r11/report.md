# FOREST / account01 B20 — exact one-edge deletion theorem for complete graphs

**Run:** `20260922T052021Z-B20-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**New theorem:** `FOREST-KN-ONE-DELETION-v1`  
**Parent Grimmett--Winkler FOREST target:** **OPEN**; no public solved-problem claim is made.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and exact debt attacked

Fresh controls selected `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, revision `2026-09-22.2`. The newest completed campaign-lead report consumed was

`account01/B01/20260922T043718Z-b01-forest-auto11/report.md`, blob `adc332e97b112525d92cf601ad1493f2e1745987`.

That report correctly withdrew the earlier `FOREST-KN-COCKS-RECONCILED-v3` chain because the fixed-graph reading of the Cocks bridge could not be certified from the primary proof body. It preserves the exact unit theorem on every complete graph `K_n` and identifies a source-valid next route: obtain a **direct deletion comparison using unit data**, rather than silently importing arbitrary positive weights.

The assigned named OTHER-account partner result actually consumed and applied was

`account04/B03/20260922T040956Z-B03-forest-r12/report.md`, blob `8812d4c9be5debaec40c02c2b13779bba8b62fae`.

It proves the exact simple path-bundle identity and thereby shows that proving positive-weight Rayleigh on every `K_n` is already equivalent to the whole all-simple-graphs target. I use that result as a hard guard: the argument below stays entirely at **unit weights** and attacks the first deletion boundary `y_g=0` directly.

I also applied account03/B01

`20260922T042943Z-account03-B01-forest-r11/report.md`, blob `4241ecd865d71c84f011012bc91caa1197afcb04`,

which proves that in a one-edge interpolation of a complete graph the mixed deletion--contraction coefficient can be strictly negative. Thus coefficientwise positivity cannot be the mechanism. The new theorem proves the deletion endpoint anyway, for every marked-pair orbit.

## 2. The theorem

> **Theorem (`FOREST-KN-ONE-DELETION-v1`).** Let `n>=2`, let `g` be any edge of `K_n`, and put `G=K_n-g`. Under the uniform law on all acyclic edge subsets of `G`, every pair of distinct remaining edges `e,f` is negatively correlated:
> 
> `Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.
> 
> For `n>=4` every nontrivial orbit gap below is in fact strictly positive. For `n=3`, `K_3-g` is a two-edge path and the two edge indicators are independent, so the gap is zero.

This is the first nontrivial deletion step beyond the complete-graph theorem and uses no weighted-Cocks implication, no minor closure, and no positive-weight approximation.

## 3. Complete-graph input and a sharper Hermite ratio bound

Fix `g={1,2}`. For `n>=4` put

`m=n-4`, `x=n+1=m+5`, `h=He_m(x)`,

and for `m>=1`

`s=m He_(m-1)(x)/He_m(x)`;

for `m=0` set `s=0`.

The lead's exact labelled-forest/Hermite calculation gives, after normalization by `h`,

`Z/h   = m^2+11m+38-(m+8)s`,
`E/h   = 2m+14-3s`,
`J_a/h = 4-s`,
`J_d/h = 5-s`,
`K/h   = 1-s`.

Here `Z` is the total number of forests of `K_n`, `E` the number containing a fixed edge, `J_a,J_d` the counts containing a fixed adjacent/disjoint pair, and `K` the count containing a fixed connected three-edge tree on four prescribed vertices.

A useful bound is available from the Hermite recurrence alone. At the fixed point `x=m+5`, define

`r_j = j He_(j-1)(x)/He_j(x)`.

The recurrence gives

`r_j = j/(x-r_(j-1))`.

Starting from `r_1=1/x`, induction gives `0<r_j<1` for `1<=j<=m`, and more sharply

`r_j < j/(x-1)=j/(m+4)`.

Hence

`0<s<m/(m+4)<1`.                                           (3.1)

This bound is the key to paying all deletion orbits.

## 4. Two new three-edge counts

The deletion formulas require two three-edge configurations not needed by the complete-graph proof.

### 4.1 A two-edge path plus a disjoint edge

Let `U` be the number of forests of `K_n` containing a prescribed three-edge forest whose connected components have vertex sizes `3` and `2`. Necessarily `m>=1`.

Using the lead's tree/forest series `R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`, either the two prescribed components lie in distinct host-tree components, giving `F A^5`, or they lie in the same host tree. In the latter case one of the three vertices in the path component and one of the two vertices in the edge component lie in the connecting deleted-edge component, giving `3*2=6` choices and the factor `T''=A^2/(1-R)`. Therefore

`U=(m-1)! [z^(m-1)] F A^5 (1+6/(1-R))`.

The same Cauchy--Hermite substitution as in the lead report gives

`U=7 He_(m-1)(x)-(m-1)He_(m-2)(x)`

and hence

`U/h = 1 + ((2-m)/m)s`.                                    (4.1)

### 4.2 A three-edge matching

Let `V` be the number of forests containing three prescribed pairwise vertex-disjoint edges; here `m>=2`.

Fix the first two disjoint edges and let `u` mark the number of connected components of the containing forest. Their component-marked EGF is

`J_d(u)=m![z^m] exp(uT) A^4 (u^2+4u/(1-R))`.

Differentiating at `u=1` counts components over all forests containing the pair. Under `z=w exp(-w)`, the Cauchy factor turns the derivative bracket into

`6+3w-(7/2)w^2+(1/2)w^3`.

Thus, writing `C_d=sum_(F contains e,f) c(F)`, one obtains

`C_d/h = (m^2 s-m^2+2m s+2m-3s+12)/2`.

Since `|F|=n-c(F)`,

`S:=sum_(F contains e,f)(|F|-2)=(m+2)J_d-C_d`,

so

`S/h = (m^2+8m+8-(m^2+4m+1)s)/2`.                         (4.2)

Now count the possible third present edge. Relative to a fixed disjoint pair there are

- `4` cross edges joining an endpoint of one marked edge to an endpoint of the other, each contributing `K`;
- `4m` edges from one of the four marked endpoints to a new vertex, each contributing `U`;
- `binom(m,2)` edges on two new vertices, each contributing `V`.

Therefore

`S=4K+4mU+binom(m,2)V`.

Substituting the known `K`, (4.1), and (4.2) gives the exact closed form

`V/h = [m^2-(m^2-4m+9)s]/[m(m-1)]`.                       (4.3)

For example, at `n=6` this gives `V=61`, exactly matching brute enumeration.

## 5. Seven deletion orbits

In `K_n-g`, the stabilizer of `g` has exactly seven possible marked-pair orbits once the required vertices exist. Representatives are

A. `e=13,f=14` (star with `g`);  
B. `e=13,f=23` (triangle with `g`);  
C. `e=13,f=24` (three-edge path; `e,f` disjoint);  
D. `e=13,f=34` (three-edge path; `e,f` adjacent);  
E. `e=13,f=45` (path-of-two plus disjoint edge);  
F. `e=34,f=35` (remote adjacent pair; `g` disjoint);  
G. `e=34,f=56` (three-edge matching).

Let `L=(Z-E)/h=m^2+9m+24-(m+5)s`. Deleting `g` subtracts `E` from `Z`, subtracts `J_a` or `J_d` from a one-edge count according as the marked edge is adjacent or disjoint from `g`, and subtracts from the two-edge count the corresponding three-edge count `K`, `U`, or `V` (zero in the triangle case).

A direct substitution gives

`Delta_(K_n-g)(e,f)=h^2 A_X(m,s)`

in orbit `X`, where

`A_A = m^2-5ms+13m+4s^2-25s+28`,

`A_B = (m+1)(ms-s^2+4s+4)`,

`A_C = 4(-ms+m+s^2-5s+1)`,

`A_D = m^2-5ms+11m+4s^2-23s+18`,

`A_E = (2/m)(-m^2s+m^2+ms^2-3m-5s^2+24s)`,

`A_F = (1/m)(m^3-3m^2s+9m^2+2ms^2-3ms+9m-10s^2+48s)`,

and, for `m>=2`,

`A_G = [-m^3s+m^3+m^2s^2+5m^2s-6m^2-10ms^2+2ms+39m+45s^2-216s]/[m(m-1)]`.

These are exact identities, not numerical fits.

## 6. Positivity of all seven orbit gaps

Write

`u=m/(m+4)`.

By (3.1), `0<s<u` for `m>=1`.

### A, C, D

Each of `A_A,A_C,A_D` is strictly decreasing in `s` on `[0,1]`. At `s=u`,

`A_A(u)=(m^4+16m^3+107m^2+332m+448)/(m+4)^2 >0`,

`A_C(u)=4(m^2+4m+16)/(m+4)^2 >0`,

`A_D(u)=(m^4+14m^3+83m^2+228m+288)/(m+4)^2 >0`.

Thus all three are positive. The same formulas cover `m=0` directly with `s=0`.

### B

`A_B=(m+1)(ms-s^2+4s+4)>0`

immediately for `0<=s<1`.

### E

For `m>=5`,

`A_E'=(2/m)(2(m-5)s+24-m^2)<0`

throughout `0<=s<u`, so

`A_E(s)>A_E(u)=2(2m^2+11m+48)/(m+4)^2>0`.

For `m=3,4`, `A_E` is concave, so its minimum on `[0,u]` is at an endpoint; `A_E(0)=2(m-3)>=0` and `A_E(u)>0`, with strict positivity at the actual `s>0`. The remaining values are exact:

`m=1: s=1/6, A_E=31/9`,

`m=2: s=7/24, A_E=229/64`.

Hence orbit E is positive whenever it exists.

### F

For `1<=m<=5`, `A_F` is concave in `s`, while

`A_F(0)=m^2+9m+9>0`

and

`A_F(u)=(m^4+14m^3+84m^2+242m+336)/(m+4)^2>0`.

For `m>=5`, its derivative is negative throughout `[0,u]`, so the same positive endpoint bound applies. Thus orbit F is positive.

### G

The numerator of `A_G` is a convex quadratic in `s`, and its derivative is still negative at `s=u`:

`A_G'(u)=-[m^4-3m^3-2m^2+118m+864]/[m(m-1)(m+4)]<0`.

(The bracket is positive for `m=2,3`; for `m>=4`, `m^2(m^2-3m-2)>0` and the remaining terms are positive.) Hence `A_G` is decreasing on `[0,u]`. For `m>=3`,

`A_G(u)=[4m^3+19m^2+53m-240]/[(m-1)(m+4)^2]>0`,

because the numerator equals `198` at `m=3` and is strictly increasing thereafter. The sole smaller case is exact:

`m=2: s=7/24, A_G=3533/1152>0`.

Therefore orbit G is also positive.

This proves the theorem for every `n>=4`. As noted above, `n=3` is a two-edge tree and has gap zero; smaller `n` are trivial.

## 7. Relation to the negative mixed coefficient

The result directly extends account03/B01's interpolation obstruction. For the `K_5` disjoint marked pair with bridge edge `g`, that report found

`Delta(t)=148-2t+64t^2`.

The negative middle coefficient kills coefficientwise deletion--contraction positivity. The theorem here proves the deletion endpoint `Delta(0)=148>0` as one instance of orbit C and then proves the corresponding endpoint for **every** one-edge-deletion orbit and every `n`.

Thus the direct deletion route survives, but it must use cancellation rather than coefficientwise positivity.

## 8. Exact audit

Standard-library checker:

`forest_kn_minus_edge_checker.py`

SHA-256 of executed source:

`72dd570ca535315625bec20510773ddfe448e45b290f9a32c9b1b5b164c5473f`

SHA-256 of clean captured stdout:

`1ddafd55cc87372c8c9040b23f847dd011974ada5fcbf696b15d4899a0024cd8`

The checker exhaustively enumerates every forest and every remaining marked pair in `K_n-g` for `3<=n<=6`, which already realizes all seven orbits, and matches every gap to the formulas above. It then evaluates the closed forms in exact integer/rational arithmetic through `n=1000` as a regression check. The symbolic argument above, not the finite loop, is the proof.

Exact output:

```text
BRUTE 3 {'B': 0}
BRUTE 4 {'A': 28, 'B': 4, 'C': 4, 'D': 18}
BRUTE 5 {'A': 1336, 'B': 346, 'C': 148, 'D': 916, 'E': 124, 'F': 928}
BRUTE 6 {'A': 110896, 'B': 39156, 'C': 9616, 'D': 79984, 'E': 8244, 'F': 80916, 'G': 7066}
FORMULA_POSITIVITY_EXACT n=4..1000 PASS
ALL_EXACT_CHECKS_PASS
```

## 9. Compact end-to-end state and next unpaid implication

The source-secure chain is now

`exact unit pNC on every K_n`

`-> NEW: exact unit pNC on every K_n minus one edge`

`-> MISSING: a deletion mechanism that survives an arbitrary growing set of missing edges`

`-> arbitrary finite simple graph`.

The theorem is genuine progress on the corrected lead's direct-deletion route, but it does not iterate automatically. In particular account04/B03's path-bundle theorem warns that replacing the missing iteration by an all-positive-weight `K_n` statement simply restates the full parent problem.

The most concrete next mathematical question is therefore: after deleting a set `D` of nonedges, can the Rayleigh gap for deleting one further edge be bounded from the already-proved unit gaps by a cancellation inequality analogous to, but weaker than, coefficientwise positivity? The one-edge theorem supplies the exact base case for such an induction.

## 10. Classification and privacy/source review

**Classification: `ESSENTIAL_STEP_APPLIED`.**

- The parent FOREST conjecture remains open.
- The prior fixed-graph-Cocks full candidate remains withdrawn fail-closed under the latest lead state.
- No brain readiness claim is used.
- No benchmark material, credentials, machine paths, unrelated private data, email, Drive, public posting, paid/remote model call, workflow dispatch, permission bypass, cross-account native action, or scheduler identifier appears in these scientific artifacts.
