# A quantitative Sidorenko inequality for equal three-block regular hosts

**Date:** 17 September 2026.  
**Claim:** `C30-EQUAL-THREE-BLOCK-STABILITY-20260917`.  
**Mathematical status:** computer-assisted proof of the restricted theorem below; **PARTIAL relative to the unrestricted source conjecture**.  
**Source target:** Sidorenko's conjecture for `H = K_{5,5} minus C_10`.  
**Independent external audits:** not performed. Internal cross-checks are not separate research-track audits.  
**Novelty:** not certified. The bounded literature check did not establish whether this particular restricted inequality or a stronger result has appeared previously.

## 1. Result and exact scope

Let `H` have left vertices `x_0,...,x_4` and right vertices `y_0,...,y_4`, where `y_i` is adjacent to `x_i,x_{i+1},x_{i+2}` with indices modulo five. The ten missing bipartite edges form a single cycle. Thus this is exactly `K_{5,5} minus C_10`, with ten vertices and fifteen edges.

A symmetric matrix `A=(A_ij)_{i,j=0}^2` represents a kernel constant on the nine rectangles of a partition into **three sets of measure 1/3 each**. Matrix diagonal entries represent within-block weights and are allowed to be positive. They are not forbidden loops in the source graph. Define

$$
t_H(A)=3^{-10}\sum_{\phi:V(H)\to\{0,1,2\}}
       \prod_{uv\in E(H)} A_{\phi(u),\phi(v)}.
$$

### Theorem 1: normalized three-block inequality and stability

Suppose that `A` is symmetric, entrywise nonnegative, and every row sums to 3. Put

$$
\rho=1-\min_{i,j} A_{ij}.
$$

Then `0 <= rho <= 1` and

$$
\boxed{t_H(A)\ge 1+\frac{725117}{3179904}\rho^4
                    \ge 1+\frac15\rho^4.}
\tag{1}
$$

In particular `t_H(A)>=1`, with equality **if and only if `A` is the all-ones matrix `J`**. With the kernel norm

$$
\|A-1\|_{L^2}^2=\frac19\sum_{i,j}(A_{ij}-1)^2,
$$

one also has

$$
\boxed{t_H(A)\ge1+\frac1{20}\|A-1\|_{L^2}^4.}
\tag{2}
$$

The constants in (1) and (2) are certified lower bounds; no optimality is asserted.

### Unnormalized form

Let `W` be a nonnegative symmetric equal-three-block kernel of constant degree `d`, meaning that its matrix row sums are `3d`. If `d>0`, apply (1) to `A=W/d` and use the fifteen-edge homogeneity:

$$
t_H(W)\ge d^{15}\left[1+\frac15
       \left(1-\frac{\min_{i,j}W_{ij}}d\right)^4\right].
\tag{3}
$$

For `d=0`, nonnegativity forces `W=0`, and the source inequality is trivial. All the displayed results include zero entries and boundary or singular matrices. They do not assume positive semidefiniteness.

**Not covered:** arbitrary unequal block measures, arbitrary irregular three-block hosts, arbitrary numbers of blocks, or general graphons. In particular this is not a proof that `H` is Sidorenko for every host.

## 2. Parametrize and cover the entire admissible set

Every normalized matrix has the unique form

$$
A(a,b,c)=\begin{pmatrix}
1-a-b&1+a&1+b\\
1+a&1-a-c&1+c\\
1+b&1+c&1-b-c
\end{pmatrix}.
\tag{4}
$$

Its nonnegative domain is the bounded polytope

$$
a,b,c\ge-1,\qquad a+b,a+c,b+c\le1.
\tag{5}
$$

Boundedness follows, for example, from `a>=-1`, `b>=-1`, and `a+b<=1`, which imply `a,b<=2`, and cyclically. Its vertices are

$$
L=(-1,-1,-1),\quad U=(1/2,1/2,1/2),
$$
$$
V_1=(2,-1,-1),\quad V_2=(-1,2,-1),\quad V_3=(-1,-1,2).
$$

There are six triangular faces, in two coordinate-permutation orbits: the three lower faces where one coordinate is `-1`, and the three upper faces where the sum of two coordinates is `1`. For example, `c=-1` leaves `a,b>=-1` and `a+b<=1`, the triangle `L,V_1,V_2`. On `a+b=1`, the other inequalities give `-1<=c<=min(a,b)`, the triangle `U,V_1,V_2`. This verifies the faces directly. The checker also enumerates every intersection of three defining planes using exact rational arithmetic and verifies the complete vertex set.

Relabeling the three host blocks realizes every permutation of the three off-diagonal parameters, so it preserves `t_H(A(a,b,c))`. It suffices to cover one face of each orbit. Use the triangle `u,v>=0`, `u+v<=1` and charts

$$
f_-(u,v)=(-1+3u,-1+3v,-1),
\tag{6}
$$
$$
f_+(u,v)=\frac12(1+3u-3v,\ 1-3u+3v,\ 1-3u-3v).
\tag{7}
$$

These are exactly the convex combinations `(1-u-v)L+uV_1+vV_2` and `(1-u-v)U+uV_1+vV_2`.

The origin is strictly inside (5). For any nonzero admissible point put

$$
r=\max\{-a,-b,-c,a+b,a+c,b+c\}=\rho.
\tag{8}
$$

If the maximum were nonpositive, then `a,b,c>=0` and their pair sums would be nonpositive, forcing all three to vanish. Hence `r>0`; (5) gives `r<=1`. Dividing `(a,b,c)` by `r` puts it on a boundary face. Thus every admissible matrix other than `J`, after a block relabeling, is represented by

$$
(a,b,c)=r f_\pm(u,v),\qquad 0<r\le1.
\tag{9}
$$

Finally `u=s`, `v=(1-s)t`, with `s,t in [0,1]`, covers the whole closed triangle. When `s=1`, necessarily `v=0`; no boundary point is lost.

## 3. An exact polynomial for the homomorphism gap

For colors `i,j,k in {0,1,2}` define the **unnormalized** triple contraction

$$
D_{ijk}=\sum_{w=0}^2 A_{wi}A_{wj}A_{wk}.
$$

Summing independently over the five right-side colors gives the identity

$$
F(a,b,c):=\sum_{z\in\{0,1,2\}^5}
       \prod_{i=0}^4D_{z_i,z_{i+1},z_{i+2}}-3^{10}
       =3^{10}(t_H(A(a,b,c))-1).
\tag{10}
$$

The subtraction `3^10`, rather than `3^5`, is essential: each of the five `D` factors already sums over one right-side color. The verifier derives (10) from (4), grouping all 243 left colorings into 39 triple-pattern multisets. It obtains a polynomial with 664 nonzero integer monomials and total degree at most 15.

There are no terms of degree below four. One can also see this without symbolic computation. Write `A=J+B` and expand the product over source edges. An edge subset with a degree-one vertex contributes zero because `B` has zero row sums. A nonempty surviving subgraph must therefore have minimum positive degree at least two, hence contain a cycle. Since `H` is simple and bipartite, it needs at least four edges. This proves the required fourth-order divisibility along every ray.

The polynomial SHA-256 is

`b2ed30695d104e2661c53cca618c1485b4948f7b9223915bb646a63057f97c21`,

under the canonical serialization specified by `verify.py`. The script regenerates it rather than trusting a supplied polynomial file.

## 4. The continuum certificate

For each of (6) and (7), form the rational polynomial

$$
G_\pm(r,s,t)=\frac{F(r f_\pm(s,(1-s)t))}{3^{10}r^4}.
\tag{11}
$$

The value at `r=0` is the polynomial extension, not an undefined quotient. The multidegrees in `(r,s,t)` are at most `(11,15,15)`. Subdivide **only `s` at `1/2`**. This leaves four closed cubes: two face types times two half-intervals.

Recall the univariate Bernstein basis

$$
B_{i,d}(x)=\binom di x^i(1-x)^{d-i},\qquad 0\le i\le d.
$$

On `[0,1]` its entries are nonnegative and sum to one, by the binomial theorem. The products of three such bases therefore form a nonnegative partition of unity on a cube. Consequently a polynomial is bounded below by the smallest of its tensor Bernstein coefficients.

The conversion from a power coefficient `p_k` to a degree-`d` Bernstein coefficient is

$$
b_i=\sum_{k\le i}p_k\frac{\binom ik}{\binom dk}.
\tag{12}
$$

Indeed, substitute `x^k = sum_{i=k}^d [binom(i,k)/binom(d,k)] B_{i,d}(x)`; the identity follows from `binom(d,i)binom(i,k)=binom(d,k)binom(d-k,i-k)` and the binomial theorem. Apply it in each of the three variables.

### Exact certificate output

Each cube has `12*16*16 = 3072` coefficients. The smallest coefficient of the normalized polynomial (11) on each cube is:

| Face | Range of `s` before rescaling | Coefficients checked | Exact minimum |
|---|---|---:|---:|
| lower | `[0,1/2]` | 3072 | `17929/38220` |
| lower | `[1/2,1]` | 3072 | `43/84` |
| upper | `[0,1/2]` | 3072 | `725117/3179904` |
| upper | `[1/2,1]` | 3072 | `5055/11648` |

The smallest of these is `725117/3179904 > 1/5`. Thus (11) is at least this constant throughout both complete face charts and every `0<=r<=1`. Equations (8)--(11) prove (1). If `rho>0`, its right side is strictly greater than one. If `rho=0`, (8) forces `a=b=c=0` and `A=J`, which has density one. This proves the equality assertion.

### Integer scaling and subdivision: reproducible details

The implementation initially forms `Q=2^15 F(r f)/r^4`; the factor clears all halves in (7). Let `D=11! (15!)^2`. Along an axis of degree `d`, the integer matrix

$$
M^{(d)}_{ik}=\begin{cases}\binom ik k!(d-k)!,&k\le i,\\0,&k>i\end{cases}
$$

implements (12) scaled by `d!`. Applying the three matrices returns `D` times the Bernstein coefficients of `Q`.

For a midpoint split of the degree-15 `s` variable, the integer matrices are

$$
L_{ij}=\mathbf1_{j\le i}\binom ij2^{15-i},\qquad
R_{ij}=\mathbf1_{j\ge i}\binom{15-i}{j-i}2^i.
$$

These return another factor `2^15` times the respective child coefficients. The final common denominator for the normalized coefficients of `G` is therefore

$$
D\,2^{30}\,3^{10}
=4327801742145527144913035241123427123200000000.
$$

Every one of the 12,288 integer numerators `N` satisfies the exact inequality `5N > D*2^30*3^10`. No floating-point tolerance enters this decision.

The entire child tensor is additionally obtained a second way: substitute `s=z/2` or `s=(1+z)/2` directly into the power polynomial, clear `2^15`, and apply (12) again. The two derivations agree in every entry. This independently checks the midpoint identities used by the implementation, although it is not an external independent audit of the theorem.

## 5. Proof of the L2 stability bound

When `rho>0`, set `A_*=J+(A-J)/rho`. By the radial construction, `A_*` is also nonnegative, symmetric, and has row sums three. Hence `P_*=A_*/3` is a symmetric stochastic matrix. For a vector `v`, Jensen's inequality in each row gives `(P_*v)_i^2 <= (P_*(v^2))_i`. Sum over `i`; column sums are also one, so `||P_*v||_2<=||v||_2`. Its eigenvalues are therefore in `[-1,1]`.

The two eigenvalues `lambda_1,lambda_2` of `(A-J)/3` on the mean-zero subspace have absolute value at most `rho`. Symmetry and the zero eigenvalue on the constants yield

$$
\|A-1\|_{L^2}^2
=\operatorname{Tr}\left(((A-J)/3)^2\right)
=\lambda_1^2+\lambda_2^2\le2\rho^2.
$$

Squaring and combining with the `rho^4/5` bound proves (2). The case `rho=0` is immediate.

## 6. Structured higher-block consequence

The restricted result also extends to every finite tensor product of these normalized kernels. On a product probability space define `A(x,y)=product_j A_j(x_j,y_j)`. Fubini's theorem directly factors each homomorphism integral:

$$
t_H(A)=\prod_j t_H(A_j)\ge1.
$$

Normalization and nonnegativity are preserved. Products of `k` three-block factors have `3^k` equal blocks, and can have unbounded rank as `k` grows. Equality holds exactly when every factor is constant. **This covers a structured tensor-product family, not arbitrary `3^k`-block kernels.** It supplies no reduction from the unrestricted source conjecture to three blocks.

## 7. Reproduction and validation record

Run from this directory using Python 3.9 or later:

```sh
python3 verify.py --output reproduced.json
python3 -c "import json; assert json.load(open('reproduced.json')) == json.load(open('results.json'))"
```

Only the Python standard library is used. The verifier has no network calls or external certificate inputs. All decisive inequalities use integers or `fractions.Fraction`. It checks all polytope vertices/faces, the omitted ten-cycle, all six parameter permutations, normalization, tensor ordering, all four exact coefficient arrays, and both independent ways of computing the child coefficients.

As regression checks, it separately sums all `3^10=59049` complete vertex colorings for each of six integer parameter triples, including a signed matrix outside the admissible domain. These agree with polynomial evaluation. Those six evaluations are **not** the continuum proof; the complete positive Bernstein certificates are the proof. The executed deterministic output in `results.json` is `ALL_EXACT_CHECKS_PASS`.

This is a computer-assisted proof with a transparent exact checker, not a Lean/Coq formal proof or a claim of independent human review.

## 8. Provenance, literature, and remaining gap

The repository input snapshot was `84bb64e8061c82e9a14b82f3568d5582bc517b52` on `master`. Relevant C30 reports inspected:

- `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T17-14-40Z__report.md`: triple-moment and pair-state transfer reductions.
- `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T18-50-49Z__report.md`: zero cubic-tensor host class and finite-host partial coverage.
- Latest recovered C30 report commit `9156a4076f4cf74731310921640a9100c29126ed`: support-profile certificates for eleven-vertex hosts with 28, 29, or 30 edges, and mandatory handoff.

This note reuses the exact triple contraction, but replaces the unresolved indefinite transfer-operator argument with radial polytope charts and a complete Bernstein certificate. General equal-three-block hosts can have two interacting nonconstant spectral directions; zero cubic moments and rank-two kernels are not imposed here.

Primary sources checked on 17 September 2026:

1. Joonkyung Lee and Bjarne Schuelke, *Convex graphon parameters and graph norms*, arXiv:1910.08454; published in Israel Journal of Mathematics 242 (2021), 549-563, doi:10.1007/s11856-021-2112-6. The abstract identifies this exact graph as a difficult Sidorenko case and proves that it is not weakly norming. The abstract and publisher metadata were checked; the full-text HTML endpoint failed. No uninspected full-text theorem is asserted here.
2. Yuqi Zhao, *Conjugacy Class Averages and Sidorenko's Conjecture*, arXiv:2606.15368v1, 13 June 2026, Introduction and abstract, HTML checked. This gives the general source formulation and a conditional conjugacy-averaging reduction. It does not identify the three-block statement above as a theorem or justify reducing every host to three blocks.

The source-target searches were bounded and some three-block queries returned irrelevant material. Therefore no exhaustive current-open check, priority claim, or publication-readiness conclusion is made. Mathematical correctness of the restricted certificate and research novelty are separate questions.

The missing mathematical step is a proof for arbitrary normalized regular kernels, or a valid inequality reducing that class to a certified family. Coarsening a kernel to three blocks has not been proved to decrease this homomorphism density. No such step is silently assumed. The unrestricted fixed-graph source target remains **not solved by this contribution**.

### Ledger delta for this direct user-requested contribution

```json
{
  "report_kind": "direct_user_requested_research_contribution",
  "native_task_id": null,
  "target_id": "C30-sidorenko-K55minusC10",
  "claim_id": "C30-EQUAL-THREE-BLOCK-STABILITY-20260917",
  "input_snapshot_sha": "84bb64e8061c82e9a14b82f3568d5582bc517b52",
  "previous_report_commit": "9156a4076f4cf74731310921640a9100c29126ed",
  "frozen_complete_simple_host_order_before": 10,
  "frozen_complete_simple_host_order_after": 10,
  "new_result": "Exact continuous equal-three-block regular-host stability theorem and tensor-product consequence",
  "mathematical_status": "PARTIAL_SOURCE; RESTRICTED_COMPUTER_ASSISTED_PROOF",
  "source_solved": false,
  "novelty_certified": false,
  "independent_external_audit_refs": [],
  "artifacts": ["README.md", "verify.py", "results.json"],
  "scheduler_changes": "NONE",
  "root_ledger_changes": "NONE",
  "existing_worker_holds": "PRESERVED",
  "delivery": "PRIVATE_GITHUB_ONLY"
}
```
