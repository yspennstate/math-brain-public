# B07 improvement/obstruction: exact ordered-child coefficients and the forbidden diagonal extension

Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

Status: **complete exact audit result / obstruction to two tempting sampling shortcuts; no multiplicity reduction claimed.**

## 1. Exact sorting sign

For increasing ordered seed sets `S,T`, an invertible `B=A[S,T]`, and distinct `ell,m` in the complement, let

`q_S(ell)=#{s in S:s>ell}`, `q_T(m)=#{t in T:t>m}`.

With both child index sets put back into increasing order,

`det A[S∪{ell},T∪{m}]
 = (-1)^(q_S(ell)+q_T(m)) det(B)
   (a_ell,m - A[ell,T] B^{-1} A[S,m]).`

The sign is exactly the parity of moving `ell` and `m` from their sorted locations to the final block row/column. Therefore the squared bordered identity in `lem:sampling` loses no magnitude and has no hidden orientation factor. Exact finite checks passed on 3,204 bordered extensions from symmetric integer matrices in dimensions 4–6 at seed orders 1–2.

## 2. Exact aggregate parent-coefficient identity

For every ordered disjoint child `(U,V)` with `|U|=|V|=r+1`, define

`c(U,V)=#{(ell,m)∈U×V : det A[U\{ell},V\{m}] != 0}`.

If `F_ST=off(A_LL-P_LL)` is the residual associated with a nonsingular ordered parent seed, then term-by-term reindexing gives the exact identity

`Σ_(nonsingular ordered parents S,T) det(A_ST)^2 ||F_ST||_F^2
 = Σ_(ordered disjoint children U,V) c(U,V) det(A_UV)^2.`

Thus the manuscript's inequality is precisely the pointwise bound `c(U,V)<=(r+1)^2`; singular parents are the only reason the aggregate relation can be strict.

This coefficient is maximally populated even under the manuscript's no-pivot hypothesis. Let

`A_ij = (1/100)/(i+j)` for distinct positive integer labels `i,j` (and the same formula on the diagonal).

The Cauchy determinant formula implies every square minor is nonzero, so every child has `c(U,V)=(r+1)^2`. Also `|A_ii|<=1/200<1/100`, and every principal two-coordinate determinant is `<(1/100)^2/4<1/100`; hence this is a no-pivot family. Consequently symmetry, no-pivot small entries, ordered/unordered conventions, or sorting signs cannot lower the `(r+1)^2` parent-count coefficient in this counting proof.

## 3. Counterexample: `ell=m` / full residual is false

The `off` in the manuscript's definition of `F` is mathematically essential. Consider

`A = [[0,1/20,0],
      [1/20,0,0],
      [0,0,1/200]]`,

with `r=1`, `S={1}`, `T={2}`. This is no-pivot. It has `V_1=1/200>0` and `V_2=0`, because three physical coordinates cannot contain two disjoint 2-sets. For this seed, `P_33=0`, so

`(A_LL-P_LL)_33=1/200 != 0`.

Therefore any attempted estimate of the **full** residual by `4 V_2/V_1` is false. The corresponding bordered determinant is

`det A[{1,3},{2,3}] = 1/4000`,

but its row and column sets overlap in coordinate 3. It is not a term of `V_2`. This pinpoints the combinatorial reason `lem:sampling` restricts to `ell != m`, takes `off(...)`, and then moves the diagonal residual into `D` in `lem:completion`.

## Consequence for the 17 threshold

These exact identities close off a purely combinatorial shortcut: neither a missing sorting sign, an ordered/unordered factor, nor inclusion of diagonal extensions can improve the sampling step. The sixteen-direction obstruction at the saturated `r=4` branch therefore has to be overcome by new structure beyond this parent count, or by a stronger order-four analytic endpoint. This is a method obstruction only; it is not an optimality result for 17 and not a counterexample to a lower-multiplicity density theorem.
