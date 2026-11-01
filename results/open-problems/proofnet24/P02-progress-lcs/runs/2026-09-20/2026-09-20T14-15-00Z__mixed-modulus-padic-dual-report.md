Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but no authenticated model-selector or applied-effort receipt is exposed, so I do not claim otherwise.

# P02 / T02 — mixed-modulus p-adic aggregate dual strictification

## 0. Source-level before / after

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The dependence among the match indicators induced by the two source strings is retained throughout. The independent Bernoulli matching model is not substituted.

Retain the rigorous public lower endpoint
\[
L=0.792665992=\frac{99083249}{125000000}.
\]
The latest durable P02 certificate entering this run was
`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T13-10-25Z__padic-type01-dual-report.md`.
It proved
\[
L\le\gamma_2\le U_{01},
\qquad
U_{01}=\frac{\log(4t^2)}{\log\lambda_{01}}.
\]

This run proves an exact stronger finite dual rate `lambda_mm < lambda_01` and therefore
\[
\boxed{L\le\gamma_2\le U_{mm}<U_{01}},
\qquad
U_{mm}=\frac{\log(4t^2)}{\log\lambda_{mm}}.
\]
An exact rational positive-series logarithm enclosure proves the strict separator
\[
\boxed{
U_{mm}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443024
<U_{01}.
}
\]
Thus the certified repository-internal width moves strictly from `U_01-L` to `U_mm-L`.

Diagnostic high precision, not used as proof, gives
\[
U_{01}-U_{mm}\approx 5.1372731162434795\times10^{-77}.
\]
The source movement is minute because the underlying frozen covering rate is already extremely close to the preceding rational cone rate. The mechanism-level improvement is much larger: the universal two-step defect is multiplied by more than four.

Status: **PARTIAL / source OPEN / exact repository-internal candidate pending later independent review and public-priority checking.**

## 1. Source status, exclusions, coordination, and handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Root `POSTED.md` was checked; no posting exclusion covers T02.

Fresh source navigation rechecked Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13. Its abstract still calls the coefficient unresolved. The arXiv comments explicitly state that claims in the original preprint about the stochastic process and `gamma` turned out to be incorrect and were omitted from v2, while a supported partial estimate was retained. None of the withdrawn claims is used here.

Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, prove the rigorous lower endpoint `0.792665992`; their abstract records the conventional rigorous upper endpoint `0.826280`. Li--Ren--Wen, published online by Cambridge University Press on 2026-03-02, still describe determining the two-string binary constant as open and summarize the historical rigorous bounds. The narrower C045/P02 endpoint here is not represented as a published bound.

Prior LCS attempts relevant to this lane include the original Chvatal--Sankoff bounds, Deken, Dancik--Paterson finite-state/covering methods, Lueker's 2009 upper-bound improvement, later computational lower bounds culminating in `0.792665992`, and Tiskin's corrected stochastic-process estimate. P02 stays on the finite-state covering/cone variational route, but the present improvement is a new arithmetic dual on the frozen C045 witness.

Newest companion P13 report recovered:
`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T13-12-00Z__cesaro-block-transfer-and-carry-quotient.md`.
P13 works the genuine-source strip/Bellman/boundary-recursion lane and proves a Cesaro-block residual smoothing and carry quotient; it does not duplicate the covering/cone arithmetic here.

Newest same-source R17 report recovered:
`runs/prob10_2026-09-20/PROB10-02/20260920T1402Z_r17_greedy_frontier_upper_84c7.md`.
R17 uses canonical greedy embeddings and Pareto frontiers, with a different stopping-line upper transfer; it reports no source-endpoint movement relative to P02's bound.

Brief handoff of P02's actual earlier target: Aldous--Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; it is not reopened.

No historical or peer file was overwritten. No email, Drive, public posting, paid compute, permission, workflow, or schedule change was performed.

## 2. Frozen C045 data and preceding defect

Put
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]
\[
S=q^6d,\qquad A=t^2H,\qquad B=SH.
\]
The primitive C045 label coefficients are
\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),
\qquad c_7=p^7,
\]
with multiplicities
\[
(m_0,m_1,\ldots,m_7)=(2,4,4,4,4,4,4,4).
\]
Since `gcd(p,q)=gcd(p,d)=1`, the exact p-adic valuation of `c_k` is `k` for every `0<=k<=7`.

The inherited positive integer cone witness satisfies
\[
1\le V_i\le M=5\cdot10^{18},
\qquad
BV\le\frac abV,
\]
where
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\qquad \gcd(a,b)=1,
\qquad b\le M<2b.
\]
Define integer row slack
\[
\boxed{s_i=aV_i-b(BV)_i\ge0.}
\tag{2.1}
\]
Let
\[
\alpha=a\bmod b=1884560463669269501,
\qquad
h=707440146652911839,
\]
so `alpha*h == 1 (mod b)`. Therefore every state satisfies
\[
\boxed{V_i\equiv h s_i\pmod b.}
\tag{2.2}
\]
For every row put
\[
T_i=(Bs)_i.
\]
The exact two-step identity is
\[
\boxed{a^2V_i-b^2(B^2V)_i=a s_i+bT_i.}
\tag{2.3}
\]

The preceding 13:10 report proved the universal normalized defect
\[
D_{01}=\frac{97a}{1094462055227467919}
\tag{2.4}
\]
and hence
\[
B^2V\le\frac{a^2-D_{01}}{b^2}V.
\tag{2.5}
\]
Its residual obstruction was that a scalar parent ratio could no longer be improved without using successor structure. The present run uses successor structure, but in an aggregate mixed-modulus form that avoids enumerating individual successor decompositions.

## 3. New mixed-modulus aggregate lemma

Fix one coefficient type `k`, containing `m_k` labels. For an actual row, let `R_k` be the sum of successor slacks over accepted labels of this type and `W_k` the corresponding sum of successor witness values. Rejected labels contribute `(0,0)`.

By (2.2), each accepted successor with slack `r` and witness value `W` satisfies `W == h r (mod b)`. Summing gives
\[
\boxed{W_k\equiv hR_k\pmod b.}
\tag{3.1}
\]
Also
\[
0\le W_k\le m_kM.
\tag{3.2}
\]

Now suppose the p-adic row equation forces
\[
W_k\equiv z_k\pmod p.
\tag{3.3}
\]
Let
\[
r_k=(hR_k)\bmod b\in\{0,\ldots,b-1\}.
\]
Every solution of (3.1) is `W_k=r_k+ell*b`. Because `m_k<=4`,
\[
m_kM\le4M<8b<pb.
\]
Thus an admissible `ell` must satisfy `0<=ell<8<p`. Since `gcd(p,b)=1`, equation (3.3) uniquely fixes `ell mod p`, namely
\[
\boxed{
ell\equiv (z_k-r_k)b^{-1}\pmod p.}
\tag{3.4}
\]
Therefore, for a fixed integer aggregate slack `R_k`, there is **at most one** aggregate witness sum `W_k` compatible with both moduli and the witness range. It is obtained by (3.4) and accepted exactly when `W_k<=m_kM`.

This is deliberately a relaxation: it does not require that `(R_k,W_k)` decompose into actual successor states or respect repeated successor identities. Hence if this larger aggregate relaxation has no configuration below a proposed defect, then the actual C045 row cannot have one either.

## 4. p-adic lifting through aggregate types

For a parent pair `(s,V)` define
\[
u=\frac{aV-s}{b}=(BV)_i.
\tag{4.1}
\]
The exact row equation is
\[
\boxed{u=\sum_{k=0}^7 c_kW_k.}
\tag{4.2}
\]
Suppose `W_0,...,W_{k-1}` have been fixed by the preceding digits. Since `v_p(c_j)=j`, subtracting those terms from (4.2), dividing by `p^k`, and reducing modulo `p` kills every type above `k` and determines
\[
\boxed{
W_k\equiv z_k:=
\left(\frac{u-\sum_{j<k}c_jW_j}{p^k}\right)
(c_k/p^k)^{-1}\pmod p.
}
\tag{4.3}
\]
Combining (4.3) with the aggregate lemma gives a one-dimensional exact scan over `R_k`, rather than an enumeration over every successor label.

For a target normalized defect `D`, attempted violation
\[
a s+b\sum_jc_jR_j<DV
\tag{4.4}
\]
provides, after fixing the earlier `R_j`, an exact integer upper budget
\[
R_k\le
\left\lceil
\frac{DV-a s-b\sum_{j<k}c_jR_j}{bc_k}
\right\rceil-1.
\tag{4.5}
\]
Equations (4.3)--(4.5) are the full exact filtering rule used below.

## 5. New universal defect

Define
\[
\boxed{
D_{mm}:=
\frac{655209040831815247751186134103526570372190622578374697627001555}
{925139970226099634}.
}
\tag{5.1}
\]
Equivalently this is the reduced value
\[
D_{mm}=\frac{110a+1815bc_0}{1850279940452199268}.
\tag{5.2}
\]
The denominator in (5.2) is a residue-compatible witness value for parent slack `110`, so the target is tied to the exact arithmetic rather than chosen from floating-point output.

Exact comparison gives
\[
\boxed{D_{mm}>4D_{01}.}
\tag{5.3}
\]
Diagnostic only,
\[
D_{mm}/D_{01}=4.0050390669492098320\ldots .
\]

### 5.1 Parent reduction

For any row with slack `s`,
\[
\frac{as}{V}\ge\frac{as}{M}.
\]
The exact cutoff is
\[
C=\left\lceil\frac{D_{mm}M}{a}\right\rceil=1775,
\]
with
\[
\frac{1775a}{M}\ge D_{mm},
\qquad
\frac{1774a}{M}<D_{mm}.
\]
Thus only `s<1775` can violate the target.

By (2.2) and `M<2b`, a fixed positive slack `s` has at most two possible witness values: the least positive residue `(hs mod b)` and, when still at most `M`, that residue plus `b`; for `s=0`, positivity and `M<2b` force `V=b`. The exact scan therefore has only `2105` possible parent pairs.

### 5.2 Type 0 leaves only 17 aggregate branches

Across all 2105 parents, (4.5) gives maximum relevant budget
\[
R_0\le5820.
\]
For each integer `R_0` in its parent-specific budget, equations (3.1), (3.4), and (4.3) determine at most one `W_0`. The exact enumeration leaves only **17** relaxed type-0 branches.

For reproducibility, their parent slacks are
\[
17,88,120,181,269,291,340,347,362,418,511,621,692,763,841,912,1186.
\]
The checker archives every exact `(s,V,R_0,W_0,lift,z_0,R_0^{max})` tuple and asserts the complete list, so this count is not inferred from floating arithmetic.

### 5.3 Type 1 leaves only four branches

Applying the next p-adic digit (4.3) and the same mixed-modulus aggregate rule, with maximum relevant budget `R_1<=12597`, leaves exactly four relaxed branches:
\[
\begin{array}{c|c|c|c|c}
s&R_0&W_0&R_1&W_1\\ \hline
362&702&7050549717083002614&459&12401578526950999455\\
511&1163&3985200494813580631&705&731966135778615573\\
621&2978&9192107448485500879&946&10847865075131040170\\
763&50&5828843258224662997&923&3017645723377190431
\end{array}
\tag{5.4}
\]
Again these are relaxed aggregate states, not claims that such actual row decompositions exist.

### 5.4 Type 2 kills all four

For the four surviving branches, the forced type-2 residues and exact violation budgets are
\[
\boxed{
(362,79595,12879),
(511,193213,1657),
(621,194825,906),
(763,14479,15287),
}
\tag{5.5}
\]
where each triple is `(parent slack, required W_2 mod p, R_2^{max})`.

For every integer `R_2` up to the corresponding budget, the mixed-modulus lift (3.4) violates the aggregate witness range `W_2<=4M`. Thus **no** relaxed type-2 branch survives.

Since every actual row maps to a relaxed aggregate configuration, there is no actual row satisfying (4.4). Hence
\[
\boxed{
\frac{a s_i+bT_i}{V_i}\ge D_{mm}
\qquad\text{for every C045 row }i.
}
\tag{5.6}
\]
Combining with the exact identity (2.3) proves the new finite dual theorem
\[
\boxed{
B^2V\le\frac{a^2-D_{mm}}{b^2}V.
}
\tag{5.7}
\]

This is the main substantive advance of the run. It improves the preceding universal defect by more than a factor four while using only three p-adic coefficient types and a safe aggregate relaxation.

## 6. Spectral improvement

By Collatz monotonicity on the positive vector `V`,
\[
\rho(B)^2\le\frac{a^2-D_{mm}}{b^2}.
\]
Define the rational strict majorant
\[
\boxed{
\beta_{mm}:=\frac ab-\frac{D_{mm}}{2ab}.
}
\tag{6.1}
\]
Then
\[
\beta_{mm}^2
=\frac{a^2-D_{mm}}{b^2}
+\frac{D_{mm}^2}{4a^2b^2}
>\frac{a^2-D_{mm}}{b^2},
\]
so
\[
\rho(B)<\beta_{mm}.
\tag{6.2}
\]
Since `D_mm>D_01`,
\[
\beta_{mm}<\beta_{01}.
\]
Rescaling from `B=SH` and `A=t^2H`, set
\[
\boxed{
\lambda_{mm}=\frac{t^2}{S}\beta_{mm}.
}
\tag{6.3}
\]
The exact endpoint checker verifies
\[
\boxed{
\rho(A)<\lambda_{mm}<\lambda_{01}<1.
}
\tag{6.4}
\]

## 7. Dependence-preserving finite-to-infinite transfer

This step is for the original two-source-string LCS problem, not an independent Bernoulli match array.

The retained C045 covering machine enumerates accepted collations of actual ordered binary source-string pairs. At fugacities `(x,y)`, if its finite operator `A(x,y)` has spectral radius below `z<1`, finite dimensionality gives a finite constant `K_z` for which accepted weight at collation length `m` is at most `K_z z^m`. Coefficient positivity and the covering property then give, for actual iid uniform binary strings of common length `n`,
\[
\boxed{
\Pr\{L_n\ge m\}
\le K_z(4xy)^{-n}z^m.
}
\tag{7.1}
\]
Here `4^{-n}` is the probability of an actual ordered source pair. No independent probabilities are assigned to the `n^2` match indicators.

Fix
\[
c>\frac{\log(4xy)}{\log z}.
\]
Because both logarithms are negative in the retained parameter regime, the exponent in (7.1) is strictly negative for `m=floor(cn)`, so the upper tail decays exponentially. Summing the LCS tail and using `0<=L_n<=n`, then passing to the limit, yields
\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{7.2}
\]
Take `x=y=t=256717/800000` and `z=lambda_mm`. Equations (6.4) and (7.2) give
\[
\boxed{
\gamma_2\le U_{mm}:=\frac{\log(4t^2)}{\log\lambda_{mm}}
<U_{01}.
}
\tag{7.3}
\]
This is the promised dependence-preserving finite-to-infinite transfer from the strengthened finite dual certificate to the original Chvatal--Sankoff constant.

## 8. Exact endpoint separation

The endpoint checker uses the positive atanh series
\[
-\log z=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},
\qquad u=\frac{1-z}{1+z},
\]
with `180` exact rational terms and the geometric tail enclosure
\[
0<\text{tail}\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]
It separately encloses `-log(4t^2)`, `-log(lambda_mm)`, and `-log(lambda_01)`. Exact rational interval division proves the intervals for `U_mm` and `U_01` are disjoint and produces the 77-digit separator
\[
\boxed{
U_{mm}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443024
<U_{01}.
}
\tag{8.1}
\]
The lower endpoint `L` is also exactly below the lower enclosure for `U_mm`.

Diagnostic decimals only:
\[
U_{mm}=0.8262759427622826250151065815372966328234619961931900238808061833125629444302310962\ldots,
\]
\[
U_{01}=0.8262759427622826250151065815372966328234619961931900238808061833125629444302824690\ldots .
\]

## 9. Essential soundness checks and artifacts

The theorem-critical scan uses Python integer arithmetic and `fractions.Fraction`; no floating arithmetic enters the branch exclusion or defect comparison.

Core checker:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T14-15-00Z__mixed_modulus_padic_dual_checker.py`
- creation commit `423f9b6238d91dc769a2ec3014e6a2b774794b3d`
- verified blob `e3eeae7fd71ce8c28cf3b348c7491eadbdb2de53`

Core executed output:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T14-15-00Z__mixed_modulus_padic_dual_checker.out`
- creation commit `f88c36a461f60fe0ba15c0dbbba9f9354d3cfbc7`
- verified blob `f9fefcda1b20704eb9f474deb4f3b0975358c665`
- ends `TYPE2_OBSTRUCTION=PASS`, `GLOBAL_TWO_STEP_DEFECT_D_NEW=PASS`, `ALL_EXACT_CHECKS_PASS`.

Endpoint checker:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T14-15-00Z__mixed_modulus_endpoint_checker.py`
- creation commit `0b532fd6f0a5698c94dcbd1418f78e7795f1628d`
- verified blob `7d3caa8694e43a753dc337b79e900efa895a6a11`

Endpoint executed output:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T14-15-00Z__mixed_modulus_endpoint_checker.out`
- creation commit `ce03d94888711d07e238dce6abf017220d0e3ebc`
- verified blob `12e0927893238bb6e9ad3e7c0ddd27024fe563f9`
- ends `EXACT_LOG_INTERVALS_DISJOINT=PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS`, `LOWER_ENDPOINT_RETAINED=PASS`, `ALL_EXACT_CHECKS_PASS`.

The checker explicitly asserts the complete surviving branch lists at types 0 and 1 and the four type-2 residue/budget records, rather than merely asserting final emptiness.

Full candidate status remains pending later independent review. In particular, this run does not independently reconstruct the entire 11,614,187-state C045 machine; it uses its previously retained exact gauge-correct operator/witness and the already-proved actual-string covering transfer as dependencies. The new arithmetic theorem itself is self-contained relative to those frozen data.

## 10. Residual obstruction and next attack

The mixed-modulus lemma is much stronger than the previous label-by-label relaxation because it couples total successor slack and total successor witness value simultaneously modulo `b`, then reads p-adic digits of the row equation. The present target dies already at type 2.

The next useful attack should optimize the target defect against this same exact aggregate recurrence rather than return to raw successor enumeration. A natural exact objective is the minimum normalized defect over the finite mixed-modulus branch tree: advance `D` until a genuine relaxed branch survives through all eight p-adic types, then either certify that threshold or use actual successor identities to kill the terminal relaxed branch. That is a materially stronger mechanism than merely adding endpoint decimals.

## 11. ledger_delta

```text
ledger_delta:
  target: T02_binary_Chvatal_Sankoff
  owner_lane: P02_stationary_variational_covering_dual
  prior_target_handoff: Aldous_Fill_OP2.34_frozen_11_of_11_unchanged
  public_lower: 0.792665992
  public_conventional_upper: 0.826280
  source_before: L <= gamma_2 <= U_01
  source_after:  L <= gamma_2 <= U_mm < U_01
  source_metric: certified_U_minus_L_strictly_shrunk
  exact_separator: U_mm < 0.82627594276228262501510658153729663282346199619319002388080618331256294443024 < U_01
  prior_defect: D_01 = 97*a/1094462055227467919
  new_defect: D_mm = 655209040831815247751186134103526570372190622578374697627001555/925139970226099634
  mechanism_gain: D_mm > 4*D_01
  new_claim: P02-T02-MIXED-MODULUS-PADIC-AGGREGATE-DUAL-01
  assumptions: frozen_gauge_correct_C045_operator_and_positive_integer_witness; actual_string_pair_covering_transfer
  dependence_model: actual_two_binary_source_strings; NOT_independent_Bernoulli_matching
  exact_core: 2105_parent_pairs -> 17_type0_aggregate_branches -> 4_type1_branches -> 0_type2_branches
  p13_nonduplication: genuine_source_strip_Bellman_boundary_recursion
  r17_nonduplication: canonical_greedy_embedding_Pareto_frontier
  status: PARTIAL_INTERNAL_EXACT_CANDIDATE_PENDING_INDEPENDENT_REVIEW_AND_PRIORITY_CHECK
  artifacts:
    - 2026-09-20T14-15-00Z__mixed_modulus_padic_dual_checker.py
    - 2026-09-20T14-15-00Z__mixed_modulus_padic_dual_checker.out
    - 2026-09-20T14-15-00Z__mixed_modulus_endpoint_checker.py
    - 2026-09-20T14-15-00Z__mixed_modulus_endpoint_checker.out
```
