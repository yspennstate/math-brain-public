# account01/B10 improvement attempt — fixed multiplicity

Run: `20260924T121937Z-account01-B10-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.  
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **PROVED same-threshold constant improvement; PROVED structural reduction of the attempted 17->16 step; multiplicity 16 itself remains OPEN in this run.** Nothing here is marked independently validated; the new material needs two genuinely separate complete reviews before any validation label.

## I. Same hypotheses improve the integer constant from 10000 to 5338

Normalize `K=s=1` exactly as in the manuscript.

The proof of Proposition `prop:pivot-H` gives the following three actual truncated-half-potential bounds, before its convenient rounding to 600:

1. scalar pivot:
   `H(Q) <= 10(20+12 log 16) = 200+120 log 16`;
2. definite pair: `H(Q)<40 pi`;
3. indefinite pair: `H(Q) <= 10(32+4 log 16)+4/e`.

The scalar value is the largest of the three. In the no-pivot nine-direction branch the manuscript gives the stronger full half-potential `<200`. Hence Proposition `prop:nine` can be replaced by

`sup_a E |Q-a|^{-1/2} <= 201+120 log 16`

under `s_9(A)>=1`.

At the scalar pivot in the main theorem, `|a_ii|^{-1/2}<=10`, so

`||p_Q||_infinity <= 2010+1200 log 16`.

Every other main branch is smaller: no-pivot `<2400`; definite pair `<40`; indefinite pair `<251` in the manuscript's rounding. Therefore

`||p_Q||_infinity <= (2010+1200 log 16)`

in the normalized theorem.

To give a rigorous integer constant below 5610 without relying on a floating-point logarithm, put `q=6933/10000`. The positive Taylor series gives

`e^q > sum_{j=0}^5 q^j/j!`

and exact arithmetic yields

`sum_{j=0}^5 q^j/j! = 8000538853437808386631 / 4000000000000000000000 > 2`.

Thus `log 2 < 6933/10000`, so

`log 16 = 4 log 2 < 6933/2500`.

Consequently

`2010+1200 log 16 < 2010+4800*(6933/10000) = 133446/25 = 5337.84 < 5338`.

Rescaling exactly as in the manuscript proves the strengthened statement

> If the independent real coordinate densities are bounded by `K` and `s_17(A)>=s>0`, then
> `||p_(X^TAX+b^TX+c)||_infinity <= 5338 K^2/s`.

No hypothesis changes, and the full-three-eigenvalue problem is not implicated.

## II. The 16-direction attempt reduces to one explicit terminal saturation chamber

This section works in the normalized no-pivot regime with the manuscript's

`eta=1/100`, `kappa=1/80^2`.

Assume `s_16(A)>=1`.

If `V_5(A)>=kappa^5`, the manuscript's fair-cut plus order-five Fourier receiver already gives a bounded continuous density `<2400`; no seventeen-direction input is needed after the volume is known. Therefore the only unresolved case for a putative 16-direction theorem is

`V_5(A)<kappa^5`.

By the same telescoping argument used in Proposition `prop:volume`, there is `0<=r<=4` with `V_r>0` and `V_{r+1}<kappa V_r`. For `r<=3`, the existing contradiction still works because

`16 >= 4r+1`.

Thus every unresolved 16-direction case is forced into the single terminal value

`r=4`.

Choose the volume-sampled disjoint 4-sets `S,T` from Lemma `lem:sampling`; write `B=A[S,T]`, `L=[n]\(S union T)`, and use the manuscript completion

`A=D+R+E`, `R[L,L]=P[L,L]`, `P=A[:,T]B^{-1}A[S,:]`.

The sampling estimate gives

`||E|| <= ||E||_F <=5 sqrt(kappa)=1/16`.

Since `rank R<=12`, singular-value perturbation now gives

`s_4(D) >= s_16(D+R) >= s_16(A)-||E|| >=15/16`.

Hence there is a four-set `H subset L` with

`|D_ii|>=15/16` for every `i in H`.

Because `diag E=0` and there is no pivot,

`|P_ii|=|R_ii| >=15/16-1/100 =371/400`.

For distinct `i,j in H`,

`|P_ij|=|R_ij| <= |A_ij|+|E_ij| <1/7+1/16 =23/112`.

Now `H` has four elements, so each row has only three off-diagonal entries. Thus

`sum_{j in H, j!=i}|P_ij| <3*(23/112)=69/112`,

and the exact row-dominance margin is

`371/400-69/112 =109/350 >0`.

Therefore `P[H,H]` is invertible. More quantitatively, the standard max-coordinate proof of strict diagonal dominance gives

`||P[H,H]^{-1}||_infinity <=350/109`.

Since the block is `4 x 4`, `||M||_2<=2||M||_infinity`, hence

`s_min(P[H,H]) >=109/700`

and

`|det P[H,H]| >= (109/700)^4`.

But the exact interpolation factorization on this four-set is

`P[H,H] = A[H,T] B^{-1} A[S,H]`.

Therefore both physical cross blocks `A[H,T]` and `A[S,H]` are invertible, and

`|det A[H,T] det A[S,H]|`
` = |det P[H,H]| |det B|`
` >= (109/700)^4 |det B|`.

So the only surviving 16-direction chamber contains **three disjoint four-sets `S,H,T` with a quantitative rank-four triangle of physical cross blocks**.

There is a second exact identity. For every `h in H`, the bordered determinant with one shared physical coordinate satisfies

`det A[S union {h}, T union {h}]`
` = det(B) (A_hh-P_hh)`
` = det(B) D_hh`.

Hence

`|det A[S union {h}, T union {h}]| >= (15/16)|det B|`.

These are order-five minors whose row and column sets overlap in exactly the coordinate `h`; they are precisely the same-index bordered minors excluded from the disjoint volume `V_5`.

### What this proves and what it does not

This is a strict reduction of the 17->16 problem, not a 16-eigenvalue density theorem. It proves that the existing argument already handles every `s_16` case except the terminal `r=4` saturation state described above. In that survivor, the missing fifth disjoint direction is replaced by four quantitatively large **overlap-one** bordered minors and by a quantitative triangle of three physical rank-four cross blocks.

The next proof obligation is therefore sharply localized:

`QFORM-FIXEDMULT-16-OVERLAP-ONE-RECEIVER-v1`:

> Convert the terminal rank-four triangle / overlap-one fifth-minor structure above into a dimension-free density receiver for arbitrary independent cap-one coordinates and arbitrary affine/self-quadratic terms, without assuming independence after rotation.

A successful receiver would complete the reduction from 17 to 16. No such receiver is proved in this run.

## III. Why numerical tightening alone cannot give 16

At terminal `r=4`, `s_16` plus global rank `<=12` forces only four large diagonal residual coordinates. A diagonally dominant `4 x 4` block has rank four, exactly compatible with `rank R[L,L]<=4`. The account01/B10 exact checker records an explicit algebraic rank-saturation example at `r=1`, and direct sums saturate `(rank R, rank R[L,L])=(3r,r)` simultaneously. Therefore no choice of smaller `eta`, smaller `kappa`, or tighter arithmetic changes the basic `4r` versus `4r+1` rank count. A true 16 theorem needs the new overlap-one/triangle structure or another analytic mechanism.

## Dependency map for the new results

- Constant 5338: only the already proved scalar/definite/indefinite pivot estimates + `prop:nine` case split + manuscript scaling.
- 16 terminal reduction: `lem:sampling` -> `lem:completion` -> singular-value perturbation -> no-pivot entry bounds -> strict diagonal dominance -> exact interpolation factorization / bordered determinant identity.
- No numerical diagnostic is used as a premise in either proof.

Review state: **UNREVIEWED NEW IMPROVEMENT MATERIAL**. Two independent complete reviews are required before any validated-improvement status.