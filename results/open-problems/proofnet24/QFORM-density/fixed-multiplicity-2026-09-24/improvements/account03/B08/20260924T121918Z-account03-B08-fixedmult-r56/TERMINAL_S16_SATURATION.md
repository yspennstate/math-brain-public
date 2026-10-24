# account03/B08 r56 — the `s_16` terminal chamber is quantitatively saturated

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T121918Z-account03-B08-fixedmult-r56`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Status: **proved supporting structural theorem; no `17 -> 16` theorem claimed**.

The fixed-multiplicity manuscript was reread end to end in this run. The 17-eigenvalue proof remains mathematically sound under this review. The new result below isolates, quantitatively, the only chamber left by the manuscript's interpolation mechanism if one tries to replace `s_17(A)>=1` by `s_16(A)>=1`.

Throughout

\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2}.
\]

`V_r(A)` denotes the manuscript's ordered disjoint-minor volume.

## Theorem — `QFORM-S16-TERMINAL-R4-SATURATION-v1`

Let `A=A^T` have no `eta`-pivot and satisfy

\[
s_{16}(A)\ge1.
\]

Assume, toward the order-five endpoint, that

\[
V_5(A)<\kappa^5.
\]

Then all of the following hold.

### 1. Every earlier volume ratio is good; the only bad ratio is `r=4`

One has

\[
V_j(A)\ge\kappa^j\qquad(1\le j\le4),
\]

and hence

\[
0<V_4(A),\qquad \frac{V_5(A)}{V_4(A)}<\kappa.
\tag{1}
\]

Indeed, if some ratio `V_{r+1}/V_r<kappa` occurred with `r<=3` (with the usual first-zero interpretation), the manuscript's sampled completion gives

\[
A=D+R+E,\qquad \operatorname{rank}R\le3r,\qquad
\operatorname{rank}R_{L,L}\le r,
\]

and `||E||<=1/16`. Since `16>=4r+1`, exactly the manuscript's diagonal-dominance contradiction applies. The `r=0` case is even simpler: `V_1<kappa` gives

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\frac1{100}+\frac1{80}<1,
\]

contradicting `s_16(A)>=1`. Thus the first four ratios are at least `kappa`, while the assumed strict inequality for `V_5` forces (1).

### 2. Canonical `r=4` completion

Apply volume-sampled interpolation at `r=4`. There are disjoint four-sets `S,T`, with

\[
B=A_{S,T}\quad\text{invertible},\qquad L=[n]\setminus(S\cup T),
\]

and

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot}
\]

such that the manuscript's completion obeys

\[
A=D+R+E,
\qquad \|E\|_F\le5\sqrt\kappa=\frac1{16},
\qquad \operatorname{rank}R\le12,
\qquad R_{L,L}=P_{L,L},
\qquad \operatorname{rank}P_{L,L}\le4.
\tag{2}
\]

As in the manuscript, `D` is diagonal and vanishes on `S union T`, while `E` has zero diagonal.

### 3. Exactly four diagonal coordinates can carry the terminal spectral mass

Rank perturbation in (2) gives

\[
s_{16}(D+R)=s_{16}(A-E)\ge\frac{15}{16}.
\]

Since `rank R<=12`,

\[
s_4(D)\ge\frac{15}{16}.
\tag{3}
\]

On the other hand set

\[
\beta:=\eta+4\left(\frac17+\frac1{16}\right)
=\frac{291}{350}.
\tag{4}
\]

There cannot be five indices in `L` with `|D_ii|>beta`. If `H_5` were such a five-set, then for every `i in H_5`,

\[
|R_{ii}|=|A_{ii}-D_{ii}|>\beta-\eta=\frac{23}{28},
\]

whereas for `i!=j` in `L`,

\[
|R_{ij}|=|A_{ij}-E_{ij}|<\frac17+\frac1{16}=\frac{23}{112}.
\]

Thus each off-diagonal row sum on `H_5` is strictly below `4(23/112)=23/28`, so `R_{H_5,H_5}` is strictly row-diagonally dominant and has rank five, contradicting `rank R_{L,L}<=4`. Hence

\[
s_5(D)\le\frac{291}{350}.
\tag{5}
\]

Combining (3) and (5), the terminal chamber has exactly four coordinates above the threshold (4), and at least four at level `15/16`.

### 4. The global rank-12 correction is quantitatively saturated

The elementary approximation inequality

\[
s_{i+j-1}(X+Y)\le s_i(X)+s_j(Y)
\tag{6}
\]

follows directly from the best low-rank approximation formula: add a rank `<i` approximation to `X` and a rank `<j` approximation to `Y`.

Apply (6) to `D+R` with `(i,j)=(5,12)`. Using (5),

\[
\frac{15}{16}
\le s_{16}(D+R)
\le s_5(D)+s_{12}(R),
\]

so

\[
\boxed{
s_{12}(R)\ge
\frac{15}{16}-\frac{291}{350}
=\frac{297}{2800}.
}
\tag{7}
\]

Thus the global `3r=12` rank allowance is not merely formal in the terminal `s_16` chamber: all twelve singular directions of `R` are quantitatively nontrivial.

### 5. The four heavy coordinates give a uniformly invertible interpolation block

Choose a four-set `H subset L` on which

\[
|D_{ii}|\ge\frac{15}{16}.
\]

For `i in H`,

\[
|P_{ii}|=|R_{ii}|\ge\frac{15}{16}-\frac1{100}
=\frac{371}{400},
\]

while for `i!=j` in `H`,

\[
|P_{ij}|=|R_{ij}|<\frac{23}{112}.
\]

There are only three off-diagonal terms per row, hence the strict dominance margin is

\[
\delta_4
:=\frac{371}{400}-3\frac{23}{112}
=\frac{109}{350}.
\tag{8}
\]

For any `x in R^4`, choose `i` with `|x_i|=||x||_infty`. Then

\[
\|P_{H,H}x\|_\infty\ge\delta_4\|x\|_\infty.
\]

Since `||x||_infty>=||x||_2/2`,

\[
\boxed{
s_4(P_{H,H})\ge\frac{\delta_4}{2}
=\frac{109}{700}.
}
\tag{9}
\]

In particular

\[
\boxed{
|\det P_{H,H}|\ge\left(\frac{109}{700}\right)^4.
}
\tag{10}
\]

This is substantially stronger than merely saying `rank P_{L,L}=4`.

### 6. Exact physical determinant chain and rank-four normal form

Because

\[
P_{H,H}=A_{H,T}B^{-1}A_{S,H},
\]

(10) yields the exact physical determinant inequality

\[
\boxed{
|\det A_{H,T}|\,|\det A_{S,H}|
\ge
\left(\frac{109}{700}\right)^4 |\det A_{S,T}|.
}
\tag{11}
\]

No rotation is involved: `S,H,T` are three disjoint four-banks of original coordinates.

Moreover (9) and `rank P_{L,L}<=4` imply `rank P_{L,L}=4`. Therefore, writing `L_0=L\setminus H`, the Schur complement of `P_{H,H}` inside `P_{L,L}` vanishes identically:

\[
\boxed{
P_{L_0,L_0}
=P_{L_0,H}P_{H,H}^{-1}P_{H,L_0}.
}
\tag{12}
\]

Equation (12) is an exact rank-four normal form for the terminal interpolation, not an approximation.

### 7. Each of the three rank-four pieces is quantitatively necessary

Let `Q=R-P` and let `Pi_T`, `Pi_S` denote row and column coordinate projections. The manuscript support identity is

\[
R=P+Q_T+Q_S,
\qquad
Q_T:=\Pi_TQ,
\qquad
Q_S:=(I-\Pi_T)Q\Pi_S,
\tag{13}
\]

with each of `P,Q_T,Q_S` of rank at most four.

Fix one of these three pieces, call it `C`. Replace `C` by a best rank-at-most-three approximation `C_3`. The sum of `C_3` and the other two exact pieces has rank at most eleven and approximates `R` with operator error `s_4(C)`. The best-rank approximation formula therefore gives

\[
s_{12}(R)\le s_4(C).
\]

Together with (7),

\[
\boxed{
\min\{s_4(P),s_4(Q_T),s_4(Q_S)\}
\ge\frac{297}{2800}.
}
\tag{14}
\]

Thus every one of the three nominal rank-four contributions is genuinely present at a fixed scale in the terminal chamber.

## Applying an existing analytic theorem to the new physical determinant chain

The completed account01/B01 theorem `SINGLE_CROSS_BANK_PLANCHEREL` states that an original-coordinate square `4 x 4` cross bank `M` gives, after conditioning on every other coordinate and retaining arbitrary same-bank phases,

\[
\|p_Q\|_\infty\le2\sqrt e\,|\det M|^{-1/4}.
\tag{15}
\]

From (11), one of `M=A_{H,T}` or `M=A_{S,H}` satisfies

\[
|\det M|
\ge
\left(\frac{109}{700}\right)^2 |\det B|^{1/2}.
\]

Hence the actual terminal matrix satisfies the conditional bound

\[
\boxed{
\|p_Q\|_\infty
\le
2\sqrt e\left(\frac{700}{109}\right)^{1/2}
|\det B|^{-1/8}
<8.357\,|\det B|^{-1/8}.
}
\tag{16}
\]

This is a genuine density estimate on the same full quadratic form. It does **not** close `s_16`, because volume sampling does not provide a dimension-free lower bound on the determinant of the selected seed `B`; many tiny determinants can carry fixed aggregate `V_4` mass. Equation (16) identifies that scalar seed-volume loss exactly.

## Designated account04/B08 result applied at an actual inequality

The completed account04/B08 theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` says: for an original-coordinate deletion

\[
A=\begin{pmatrix}a&b^T\\b&C\end{pmatrix},
\]

if `C` has three singular values at least `m` and its projection onto the spectral window `|lambda(C)|>=m/64` has maximum physical leverage at most `1/32`, then

\[
\|p_{X^TAX}\|_\infty<\frac{64}{m},
\]

with a continuous `C_0` density.

This has a particularly clean fixed-multiplicity consequence. Since deleting one original coordinate changes the embedded child by a matrix of rank at most two,

\[
s_{j+2}(A)\le s_j(C).
\]

Therefore already

\[
s_5(A)\ge1\quad\Longrightarrow\quad s_3(C)\ge1
\tag{17}
\]

for **every** original-coordinate deletion. Applying the partner theorem with `m=1` gives:

\[
\boxed{
\text{If }s_5(A)\ge1\text{ and for some deletion child }C_i,
\ \max_j(P_{C_i}(1/64))_{jj}\le\frac1{32},
\text{ then }\|p_Q\|_\infty<64,\ p_Q\in C_0.
}
\tag{18}
\]

After the standard scaling, for coordinate density caps `K` and `s_5(A)>=s`, (18) becomes

\[
\boxed{
\|p_Q\|_\infty<64K^2/s.
}
\tag{19}
\]

Consequently every unpaid `s_16` terminal survivor above must, in addition to (1)--(14), satisfy for every deletion `i`

\[
\max_j(P_{C_i}(1/64))_{jj}>\frac1{32}.
\tag{20}
\]

This adds a concrete physical localization obstruction to the algebraically saturated `r=4` chamber.

Partner source: `yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

## Exact remaining implication for `17 -> 16`

The existing architecture plus this run reduces the threshold-lowering problem to a much narrower statement:

> In the no-pivot `s_16>=1` chamber, with the exact saturated rank-four interpolation (7)--(14), the determinant chain (11), and the all-deletion localized-window condition (20), obtain a dimension-free density estimate without paying `|det B|^{-1/8}`; equivalently, aggregate the seed determinant before inversion, or convert the forced child localization into a physical pivot/crossing receiver.

This is genuinely stronger information than the bare observation that the old rank count stalls at `r=4`, but it is not yet a complete `s_16` theorem.

## Audit clarification: the singular Schur-limit paragraph

A peer note suggested that the baseline singular-ambient proof of `lem:schur` needs replacement because its threshold `t-|epsilon|` moves. I rechecked this point directly. The baseline passage is terse but valid: if `q=N_A(t)-k`, the invertible case gives the `q`-th ordered absolute eigenvalue of `S_epsilon` at least `t-|epsilon|`; `S_epsilon -> S` in operator norm, hence that ordered absolute eigenvalue converges and its limit is at least `t`. Thus the moving threshold itself creates no gap. The peer's fixed-`delta` version is a clearer alternative proof, but it repairs exposition rather than a mathematical failure.

## Scope

- The 17-eigenvalue manuscript: **PASS in this run's full textual audit**.
- A universal 16-eigenvalue theorem: **not proved**.
- The unrestricted three-eigenvalue conjecture: **OPEN**.
- Continuity: proved only on branches such as (18); the manuscript's full theorem claims only essential boundedness.
- No Gaussianity, moments, bounded support, log-concavity, exact-rank assumption, or independence after rotation is used above.
