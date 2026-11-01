# B14 — exact propagation of the quadratic JS potential, and a recursive residual-selector obstruction

**Run:** `b14-20260921T153501Z-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED exact composition identity plus a rigorous finite obstruction. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** **UNVERIFIED; no novelty claim.**

This run followed the live FEI order and read the current `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`. It also consumed two newer compatible B14 handoffs rather than repeating old sweeps: the fleet02 recursive Numaro selector obstruction / fixed-seed convergence theorem, and fleet04's exact mass-weighted erasure-composition theorem. The old false every-prescribed-coordinate payment remains **REFUTED** and is not revived.

The immediate predecessor from this slot proved that
\[
P_2(f)=c_*\left(I(f)-\frac13\sum_j\operatorname{Inf}_j(f)^2\right),\qquad c_*={2\over\ln2},
\]
absorbs the whole Jensen--Shannon restriction term. If
\[
D_i(f):=\sum_{j\ne i}\left(\operatorname{Inf}_j(f_i^+)-\operatorname{Inf}_j(f_i^-)\right)^2,
\]
then
\[
{\Delta_iP_2\over \operatorname{Inf}_i(f)}
=c_*\left(1-\frac{\operatorname{Inf}_i(f)}3+{D_i(f)\over12\operatorname{Inf}_i(f)}\right),
\tag{0.1}
\]
and `Delta_i(H-P2)=B_i-G_i` with `G_i>=0`. The open hope was that the positive `D_i` term might grow under recursive composition strongly enough to collapse the hard residual selector.

## 1. Exact statement attempted

Let `G:{-1,1}^m->{-1,1}` and `H:{-1,1}^n->{-1,1}` be balanced Boolean functions and let
\[
F=G(H^{(1)},\ldots,H^{(m)})
\]
be their disjoint identical-inner composition. Fix a physical coordinate `x` in inner block `i`. Put
\[
a_i=\operatorname{Inf}_i(G),\qquad s_i=|\widehat G(\{i\})|,
\]
\[
p=\operatorname{Inf}_x(H),\qquad q=|\widehat H(\{x\})|,
\]
and
\[
A_2(H)=\sum_y\operatorname{Inf}_y(H)^2.
\]
The attempted question was:

> **Does the child-modulation rebate in `P2` amplify under balanced composition enough to neutralize the recursive local restriction obstruction?**

The exact propagation identity below answers the first part. On the current Numaro recursion the answer to the amplification hope is **no**: the normalized modulation rebate decays to zero.

## 2. PROVED: exact child-modulation composition identity

### Theorem 2.1

For the physical coordinate `x` in block `i`,
\[
\boxed{
\operatorname{Inf}_x(F)=a_i p,
\qquad
|\widehat F(\{x\})|=s_iq,
}
\tag{2.1}
\]
\[
\boxed{A_2(F)=A_2(G)A_2(H),}
\tag{2.2}
\]
and, most importantly,
\[
\boxed{
D_x(F)=a_i^2D_x(H)+q^2A_2(H)D_i(G).
}
\tag{2.3}
\]
Consequently the exact quadratic-potential drop is
\[
\boxed{
{\Delta_xP_2(F)\over \operatorname{Inf}_x(F)}
=c_*\left[
1-{a_ip\over3}
+{a_i^2D_x(H)+q^2A_2(H)D_i(G)\over12a_ip}
\right].
}
\tag{2.4}
\]

### Proof

Equations (2.1) are the standard balanced disjoint-composition factorization. Squaring the physical influences block by block gives (2.2).

For (2.3), first consider a second physical coordinate `y` in the same inner block `i`. Restricting `x` changes only that inner function. The outer logical derivative in coordinate `i` is sampled against the other balanced block outputs, so its squared multiplier remains exactly `a_i`. Hence
\[
\operatorname{Inf}_y(F_x^+)-\operatorname{Inf}_y(F_x^-)
=a_i\left(\operatorname{Inf}_y(H_x^+)-\operatorname{Inf}_y(H_x^-)\right).
\tag{2.5}
\]
The squared contribution of the same block is therefore `a_i^2D_x(H)`.

Now take `y` in another block `j!=i`. After restricting `x`, the logical output of inner block `i` has means `+q` and `-q` (up to swapping signs). Let `A_j^{(i)}(mu)` be the influence of logical coordinate `j` in the outer function when coordinate `i` has mean `mu` and all other logical coordinates are uniform. Pair the ordinary Fourier coefficients of `G` as
\[
u_K=\widehat G(K),\qquad v_K=\widehat G(K\cup\{i\}),\qquad i\notin K.
\]
The biased-basis Parseval formula gives
\[
A_j^{(i)}(\mu)
=\sum_{K\ni j,\ i\notin K}
\left(u_K^2+v_K^2+2\mu u_Kv_K\right).
\]
Therefore
\[
A_j^{(i)}(+q)-A_j^{(i)}(-q)
=4q\sum_{K\ni j}u_Kv_K
=q\,d_{ij}(G),
\tag{2.6}
\]
where `d_ij(G)=Inf_j(G_i^+)-Inf_j(G_i^-)`. A physical coordinate `y` in block `j` has its inner influence multiplied by `A_j^{(i)}(mu)`, so its child difference is
\[
q\,d_{ij}(G)\operatorname{Inf}_y(H).
\]
Squaring, summing over all `y` in block `j`, and then over `j!=i`, yields exactly
\[
q^2 A_2(H)\sum_{j\ne i}d_{ij}(G)^2=q^2A_2(H)D_i(G).
\]
Adding the same-block term proves (2.3), and (0.1) gives (2.4). QED.

This identity is exact and does not assume FEI or an every-coordinate selector.

## 3. Exact Numaro seed data for the new state

The verifier beside this report reconstructs the already-recovered external Numaro 18-variable balanced seed from the preserved source slices and rejects unless its truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Integer Walsh arithmetic gives the inherited influence classes
\[
a_C=s_C={57\over256},\qquad a_A=s_A={1\over256},
\]
and the new exact modulation data
\[
\boxed{A_2(G)={14625\over32768},}
\tag{3.1}
\]
\[
\boxed{D_C(G)={485\over2048},\qquad D_A(G)={1\over2048}.}
\tag{3.2}
\]
For a core coordinate the 17 values `d_ij` are `+11/64` four times, `-11/64` four times, `+1/128` four times, `-1/128` four times, and `0` once. For an auxiliary coordinate they are `+1/128` four times, `-1/128` four times, and `0` nine times. Thus (3.2) is exact, not a floating fit.

## 4. PROVED: `P2` does not erase the finite recursive selector obstruction

Let `F_r` be the depth-`r` self-composition of the Numaro seed. Every physical coordinate is represented by a word in the two coordinate classes `C,A`. Equations (2.1)--(2.3) propagate the exact rational state `(p,q,D,A2)` along each word. Because here `s_i=a_i`, one has `q=p` along every path.

At depth five the exact enumeration of all 32 path classes finds that the largest normalized `P2` drop occurs at `CCCCC`. Its rational bracket in (0.1) is
\[
{158488659292203726473027666639
 \over
 158456325028528675187087900672}.
\]
A rational `atanh(1/3)` enclosure of `ln 2` gives
\[
2.885390081777926814719849<c_*<2.885390081777926814719850,
\]
so for **every** physical coordinate of `F_5`,
\[
\boxed{
{\Delta_iP_2(F_5)\over\operatorname{Inf}_i(F_5)}
<2.885978868395897337361880.
}
\tag{4.1}
\]

The compatible fleet02/B14 certificate already proves, for the same finite `F_5`,
\[
{\Delta_iH(F_5)\over\operatorname{Inf}_i(F_5)}
>7.096060618744925556394954995917
\quad\text{for every relevant }i.
\tag{4.2}
\]
This run does not re-audit that certificate; (4.2) is an explicit inherited dependency. Subtracting the independently exact new bound (4.1) gives the new finite obstruction
\[
\boxed{
{\Delta_i(H-P_2)(F_5)\over\operatorname{Inf}_i(F_5)}
>4.210081750349028219033075
\quad\text{for every relevant }i.
}
\tag{4.3}
\]
Equivalently, for the residual-selector constant from the predecessor,
\[
K_R:=\sup_f\min_i{B_i-G_i\over\operatorname{Inf}_i(f)},
\]
we now have the rigorous lower bound
\[
\boxed{K_R>4.210081750349028219033075.}
\tag{4.4}
\]

This does **not** refute the residual-selector strategy: a finite universal `K_R` would still prove FEI. It does refute the hope that the explicit quadratic potential by itself makes the hard recursive selector small (for example near the `3.636...` calibration obtained by subtracting `c_*` from the currently known external FEI lower-bound scale).

## 5. PROVED for this recursion: the extra modulation rebate vanishes asymptotically

Write
\[
U_r={D_i(F_r)\over\operatorname{Inf}_i(F_r)}
\]
along an arbitrary leaf path. From (2.3), when the next outer class is `t in {C,A}`,
\[
U_{r+1}
=a_tU_r
+{q_r^2\over p_r}A_2(G)^r{D_t(G)\over a_t}.
\tag{5.1}
\]
For this seed `q_r=p_r`, and uniformly over paths
\[
p_r\le(57/256)^r,
\qquad
A_2(G)=14625/32768<1.
\]
Hence the forcing term in (5.1) is bounded by a constant times
\[
\left({57\over256}{14625\over32768}\right)^r,
\]
while the homogeneous multiplier is at most `57/256`. Both are strictly below one. Therefore
\[
\boxed{\sup_{\text{leaf paths}}U_r\to0,\qquad
\sup_{\text{leaf paths}}p_r\to0.}
\tag{5.2}
\]
Using (0.1),
\[
\boxed{
\sup_i\left|
{\Delta_iP_2(F_r)\over\operatorname{Inf}_i(F_r)}-c_*
\right|\to0.
}
\tag{5.3}
\]

The compatible fleet02 theorem proves that the potential-free selector minima `rho_0(F_r)` converge to a finite `rho_*(G)`. Uniform convergence in (5.3) therefore yields the exact asymptotic relation
\[
\boxed{
\min_i{\Delta_i(H-P_2)(F_r)\over\operatorname{Inf}_i(F_r)}
\longrightarrow \rho_*(G)-c_*.
}
\tag{5.4}
\]
Thus on this recursive obstruction the quadratic potential asymptotically subtracts only the scalar `2/ln 2`; its special child-modulation bonus disappears.

The predecessor's high-precision, non-certified exploration suggested `rho_*(G)≈7.111618180511835`, which would put the residual limit near `4.226228098733908`. That number is **EXPLORATORY only**; the rigorous result of this run is the finite bound (4.4) plus the limit identity (5.4).

## 6. Attempted refutation / dead route

The attack deliberately tried to refute the concern that the `D_i` bonus in `P2` is too local: perhaps repeated outer composition would create large child-influence modulation and make `G_i` grow with the same recursion that makes `Delta_iH/Inf_i` large.

Equation (2.3) gives the opposite outcome on the strongest current fixed-seed obstruction. The new cross-block modulation is multiplied by the squared singleton bias `q^2`, and `A_2` itself multiplies under composition. On the Numaro seed both factors contract. The exact path computation then shows that by depth five the maximum normalized `P2` drop is already only `2.885978868...`, very close to `c_*=2.885390081...`.

So the route

> **"the first-order quadratic influence modulation inside `P2` will recursively amplify enough to neutralize the Numaro local-selector obstruction"**

is **REFUTED for this fixed-seed family**. This is not a refutation of `P2` as a useful universal potential, nor of FEI.

## 7. OPEN / CONDITIONAL / REFUTED ledger

### PROVED in this run

- Exact child-modulation composition identity (2.3).
- Exact `A2` multiplicativity (2.2) and induced `P2` propagation (2.4).
- Exact Numaro values `A2=14625/32768`, `D_C=485/2048`, `D_A=1/2048` from integer Walsh arithmetic.
- Using the inherited certified `rho_0(F_5)` lower bound, every physical coordinate of `F_5` has residual ratio `>4.210081750349028219033075`; hence `K_R` exceeds that number.
- On the fixed Numaro recursion, normalized `P2` drop converges uniformly to `2/ln 2`, giving the asymptotic shift formula (5.4).

### CONDITIONAL / inherited

- The prior theorem `JS_i<=Delta_iP2` is inherited from this slot's earlier quadratic-potential report and its strong-concavity input.
- The numerical lower bound (4.2) is inherited from the fleet02/B14 rational-log certificate rather than re-audited here.
- The existence of finite `rho_*(G)` is inherited from fleet02/B14's fixed-seed convergence theorem.

### OPEN

- A dimension-independent universal upper bound on the residual selector `K_R`.
- Full uniform-cube FEI.
- Whether a richer potential using higher-order/block modulation can turn the mass-weighted activation refunds into a universally summable restriction-tree payment.

### REFUTED / NOT CLAIMED

- The known false every-prescribed-coordinate payment remains false.
- First-order `P2` modulation does not recursively grow on the Numaro self-composition; it vanishes after normalization.
- A finite recursive construction or a structured-class theorem is not full FEI closure.

## 8. Next attack

The exact failure mode points to a more specific next object. The concurrent mass-weighted erasure-composition theorem says that new outer erasure is transported through **singleton activation mass**, while (2.3) says first-order influence modulation is damped by its **square**. The next B14 attack should build a hierarchy that tracks block activation before squaring destroys it: for example, a block-modulation potential whose drop contains a term linear in the singleton activation fraction and whose restriction-tree telescoping includes the exact `E(mu^2,e)` refund from the arbitrary-bias erasure identity.

The target is existential and nonlocal: prove that either a coordinate has small `B_i-G_i`, or a block modulation/refund reserve increases by enough to pay the excess. Do not revert to an every-coordinate bound.

## 9. Reproducibility

`verify_p2_recursive_obstruction.py` reconstructs the published seed, verifies its source hash, computes the new exact modulation rows with integer Walsh arithmetic, enumerates all class paths through depth eight using exact rational recurrences, encloses `2/ln2` by a rational atanh series, and combines the depth-five maximum `P2` drop with the explicitly declared peer-certified `rho_0(F_5)` lower-bound dependency. Current-run result: `PASS`. The saved `verification.json` contains the exact path factors and headline bound.
