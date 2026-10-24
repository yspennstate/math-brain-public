# account01/B18 — radius-two changed-support rigidity for the 18-row FEI obstruction

**Classification:** `ESSENTIAL_STEP_APPLIED` to the direct falsification branch; **full unrestricted uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and source mathematics were read, but no authenticated native research-brain receiver context entered the mathematics.

## 1. Live candidate and exact peer result applied

The live stable post-falsifier candidate is
\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]
with the still-open all-gate obligation `D_{Gamma_*}(G;p)>=0` for every Boolean gate and every interior product bias. At a balanced gate and unbiased inputs this specializes exactly to
\[
H(G)\le C_*\,[I(G)-1].
\tag{1.1}
\]
Thus an explicit balanced gate with `H/(I-1)>C_*` would refute this candidate at its center.

This run substantively consumes the exact other-account theorem **account02/B17**, commit
`a8d01c24a9afa8d69d27dd42c321a7bed50bcf01`, report
`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T041256Z-onecell-support-rigidity/REPORT.md`.
It reconstructs the exact nine-core/nine-host representation of the source-valid balanced 18-variable composition-prime gate and proves the following host-bank fact. For any 18-row positive support `U`, partitioned into nine unordered two-row host blocks,
\[
H_{\rm host}=\frac9{16},\qquad I_{\rm host}\ge\frac{45}{256}.
\tag{1.2}
\]
Consequently every actual pairing `pi` obeys the optimistic comparison
\[
\frac{H(F_{U,\pi})}{I(F_{U,\pi})-1}
\le
R_{\rm opt}(U):=
\frac{H(a_U)+9/16}{I(a_U)+45/256-1}.
\tag{1.3}
\]
The same peer theorem exhaustively closed every **one-row** exchange of the published 18-row support, proving every such actual gate has ratio below `6.492`. Its first remaining changed-support freedom was therefore support-exchange distance at least two.

The inherited exact source support is
\[
T=\{78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457\}.
\tag{1.4}
\]
The nine-bit source `g_0` has 265 positive rows. Puncturing the 18 rows of `T` gives a mean-zero core `a_T`; the 247 other positive source rows form the set `P` available for support exchanges.

## 2. The first missing falsification inference

The exact old missing implication was:

> Could replacing **two** rows of `T` by two other positive source rows produce a balanced gate whose central ratio `H/(I-1)` challenges or exceeds the stable cap `C_*`?

For distinct `x_1,x_2 in T` and distinct `y_1,y_2 in P`, set
\[
U=(T\setminus\{x_1,x_2\})\cup\{y_1,y_2\}.
\tag{2.1}
\]
There are exactly
\[
\binom{18}{2}\binom{247}{2}=4,648,293
\tag{2.2}
\]
such supports. All signs are retained. If
\[
A_T(S)=\sum_z a_T(z)\chi_S(z)
\]
is the integer Walsh numerator, then
\[
\boxed{
A_U(S)=A_T(S)+\chi_S(x_1)+\chi_S(x_2)-\chi_S(y_1)-\chi_S(y_2).
}
\tag{2.3}
\]
No absolute-value relaxation is used before entropy evaluation.

## 3. Exact influence update by a Hamming-one kernel

Put `N=512` and
\[
K(u,v):=\sum_{S\subseteq[9]}|S|\chi_S(u)\chi_S(v).
\]
Expanding `|S|=sum_i 1_{i in S}` and summing the characters gives the exact kernel
\[
\boxed{
K(u,v)=
\begin{cases}
2304,&u=v,\\
-256,&d_H(u,v)=1,\\
0,&d_H(u,v)\ge2.
\end{cases}}
\tag{3.1}
\]
Indeed, for each singled coordinate `i`, all remaining character sums cancel unless `u xor v` is either empty or exactly `{i}`.

Define
\[
L(z):=\sum_S |S|A_T(S)\chi_S(z),
\qquad
J(U):=\sum_S |S|A_U(S)^2=N^2 I(a_U).
\]
Let `e_x` indicate whether `x_1,x_2` are adjacent, `e_y` whether `y_1,y_2` are adjacent, and `e_{xy}` be the number of Hamming-one cross pairs among the four pairs `(x_i,y_j)`. From (2.3) and (3.1),
\[
\boxed{
J(U)-J(T)
=2[L(x_1)+L(x_2)-L(y_1)-L(y_2)]
+9216-512e_x-512e_y+512e_{xy}.
}
\tag{3.2}
\]
This turns all 4,648,293 influence computations into exact integer arithmetic.

The exact enumeration gives
\[
\boxed{J(U)-J(T)\ge2048}
\tag{3.3}
\]
for every two-row exchange, with equality for example at
\[
(78,79)\longrightarrow(84,85).
\]
Hence
\[
\boxed{
I(a_U)\ge I(a_T)+\frac{2048}{512^2}
=I(a_T)+\frac1{128}.
}
\tag{3.4}
\]
So every radius-two support mutation pays a strictly positive core-influence tax before the host bank is even considered.

## 4. Rigorous entropy enclosure

For an integer Walsh amplitude `z=|A_U(S)|`, its spectral entropy contribution is
\[
h_z=
\frac{z^2}{N^2}\log_2\frac{N^2}{z^2}
=rac{2z^2}{N^2}\log_2\frac Nz.
\tag{4.1}
\]
Every `h_z`, `0<=z<=N`, is upper-enclosed by exact rational arithmetic. For `q in [1,2]`, with
\[
t=\frac{q-1}{q+1},
\]
use
\[
\ln q=2\sum_{j=0}^{m-1}\frac{t^{2j+1}}{2j+1}+R_m,
\qquad
0\le R_m\le
\frac{2t^{2m+1}}{(2m+1)(1-t^2)}.
\tag{4.2}
\]
The checker uses `m=40`, a rational lower bound for `ln 2`, and then rounds every upper bound upward at scale
\[
M=10^{17}.
\]
Thus the stored integer table satisfies
\[
\operatorname{hfix}(z)\ge M h_z.
\tag{4.3}
\]
For each support, the rigorous optimistic entropy numerator is therefore
\[
H^{\uparrow}(U)=
\frac1M\sum_S\operatorname{hfix}(|A_U(S)|)+\frac9{16}
\ge H(a_U)+\frac9{16}.
\tag{4.4}
\]

Write the exact optimistic denominator as
\[
I(a_U)+\frac{45}{256}-1=\frac{d(U)}{N^2}.
\tag{4.5}
\]
Only 15 distinct values of `d(U)` occur over the 4,648,293 candidates. For each denominator the checker retains the largest rigorous entropy upper enclosure and proves the integer inequality
\[
M\cdot3239\,d
-500N^2\,M H^{\uparrow}>0.
\tag{4.6}
\]
The minimum integer slack in (4.6) is
\[
\boxed{480945804743933952000>0.}
\tag{4.7}
\]

## 5. New theorem — every radius-two support mutation is far below the live center

### Theorem 5.1
For every support `U` obtained from `T` by replacing exactly two rows by two rows of `P`, and for **every** partition `pi` of `U` into nine two-row hosts,
\[
\boxed{
\frac{H(F_{U,\pi})}{I(F_{U,\pi})-1}
<\frac{3239}{500}=6.478.
}
\tag{5.1}
\]

### Proof
Equation (1.3) reduces every actual host pairing to `R_opt(U)`. Equations (4.4)--(4.7) prove `R_opt(U)<3239/500` simultaneously for all 4,648,293 supports. QED.

The descriptive largest rigorous fixed-point upper ratio encountered by the checker is
\[
6.477964949728548
\]
at the exchange `(78,79)->(86,87)`; this decimal is diagnostic only. The pass/fail theorem is the rational bound (5.1).

The source gate itself has the certified central excess ratio
\[
R_T=6.5218457109230465756581439729485784683666622922105\ldots,
\]
so the full radius-two family lies at least
\[
R_T-6.478
>0.0438457109230465
\tag{5.2}
\]
below the source obstruction. Combining account02/B17's radius-one theorem with Theorem 5.1 gives a certified radius-two basin around the published support inside this exact punctured-core/two-row-host construction family.

## 6. What changed for the full candidate

**Before.** The current post-falsifier gate candidate could already not be attacked by changing only one exceptional support row; support-exchange distance two was the first unresolved source-valid mutation of the same prime obstruction.

**After.** Every such two-row mutation is rigorously noncompetitive at the uniform balanced point, even after granting it the unrealistically favorable minimum host influence `45/256` without requiring that its support actually admits an all-adjacent perfect matching.

This does **not** prove `D_{Gamma_*}(G;p)>=0` for arbitrary gates or arbitrary biases. It also does not prove that the published 18-row support is globally optimal. It closes one concrete first missing falsification inference.

The next exact adversarial freedoms are now:
1. support-exchange distance at least three within the same nine-core/two-row-host source model;
2. change the underlying base core rather than only its puncture set;
3. reuse/overlap host coordinates or abandon the two-row host model;
4. keep the current prime gate but move to genuinely nonuniform product bias, where the full shape of `Gamma_*` matters rather than only `Gamma_*(1/2)`.

Given the live owner's request to converge on direct proof/falsification, the most economical next attack is (4): optimize the source-valid prime gate over nonuniform biases before opening a combinatorially much larger support-radius-three search.

## 7. Verification and provenance

Committed deterministic checker:
`CHECKER.py`, Git blob `ac876b1fc58f20587180209da84e244283ddf779`.

Committed captured output:
`CHECK_OUTPUT.txt`, Git blob `8267aed4339541893b53d73ca915b2ae5c987271`.
Captured-output SHA-256:
`bf275c5d5cd051c74d0f0ec5de106e477604b766865efe1adfd8f189698bdbf5`.

The executable logic was run locally from an equivalent copy of the committed checker; repository-only comments/docstrings do not affect that logic. The output reports `PASS`, all `4,648,293` supports checked, minimum influence-numerator increase `2048`, and the positive exact integer slack in (4.7).

The source truth-table reconstruction is inherited from account01/B12's exact composition-primality certificate, whose published truth-table SHA-256 is
`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

No novelty or publication-priority claim is made. Full FEI remains **OPEN / NOT PROVED**.
