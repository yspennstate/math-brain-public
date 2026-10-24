SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-23T22:41:21Z.
attacking: the surviving one-overlap third-compound packet — split every bordered determinant into two orthogonal positive currencies before selecting or reciprocating any physical minor.

# Early calculation: an exact positive compiler for one-shared 3x3 minors

Let `H,I,J` be pairwise disjoint ORIGINAL-coordinate banks. Fix `h in H`, and abbreviate

- `a=A_hh`,
- `m=A[h,J] in R^J`,
- `u_i=A[i,h]` for `i in I`,
- `k_i=A[i,J] in R^J`.

For `r<s` in `I`, let `D_rs` be the 2-form on the physical `J`-coordinates whose `(c,d)` coefficient (`c<d`) is

`det A[{h,r,s},{h,c,d}]`.

Expanding along the shared physical column gives exactly

`D_rs = a k_r wedge k_s - u_r m wedge k_s + u_s m wedge k_r`.      (E1)

Assume first `m!=0`. Orthogonally decompose the coefficient rows relative to the literal hub star `m`:

`k_i = alpha_i m + c_i`,
`alpha_i=<k_i,m>/||m||^2`,
`c_i perpendicular to m`,

and put

`beta_i = a alpha_i-u_i`.                                           (E2)

Then direct substitution into (E1) yields

`D_rs = a c_r wedge c_s + m wedge (beta_r c_s-beta_s c_r)`.         (E3)

The two terms in (E3) are orthogonal in `Lambda^2(R^J)`: the first belongs to `Lambda^2(m^perp)`, while the second belongs to `m wedge m^perp`. Therefore

`||D_rs||^2
 = a^2 ||c_r wedge c_s||^2
   +||m||^2 ||beta_r c_s-beta_s c_r||^2`.                           (E4)

Summing over every physical row pair gives the exact positive identity

`Omega_1(h)
 :=sum_{r<s in I} sum_{c<d in J}
      det A[{h,r,s},{h,c,d}]^2
 =a^2 Z_2(h)+||m||^2 W(h)`,                                        (E5)

where

`Z_2(h)=sum_{r<s}||c_r wedge c_s||^2`,
`W(h)=sum_{r<s}||beta_r c_s-beta_s c_r||^2`.                        (E6)

A second exact Lagrange identity is

`W(h)=||beta||^2 ||C||_F^2-||C^T beta||^2 >=0`,                     (E7)

where the rows of `C` are the `c_i`.

If `m=0`, (E1) reduces to `D_rs=a k_r wedge k_s`, so (E5) remains valid with

`Z_2(h)=e_2(KK^T)`, `W(h)=0`.                                       (E8)

Hence the full banked one-overlap packet has no hidden cancellation:

`Omega_1(H,I,J)
 =sum_{h in H} a_h^2 Z_2(h)
  +sum_{h in H: m_h!=0} ||m_h||^2 W(h)`.                            (E9)

This directly targets the r39 debt. Account01/B09's completed random-color localization gives a literal three-bank partition with

`Omega_1(H,I,J) >= (16/3125)E_1(A)`.                               (E10)

Thus if the winning overlap class has `E_1(A)>=1/4`, then

`sum_h a_h^2 Z_2(h)+sum_h ||m_h||^2 W(h) >=4/3125`,                (E11)

so at least one of these two aggregate positive currencies is at least `2/3125`.

The first currency is visibly adjacent to the completed one-hub/two-volume receiver because that receiver uses `V_3(h)=||m_h||^2 Z_2(h)`. The ratio `||m_h||/|a_h|` is therefore the exact remaining conversion factor for that term; no individual 3x3 determinant is selected. The second currency is a distinct skew-star/plane-mismatch packet and is retained rather than falsely declared to be an independent projected-volume packet.

Finite random checks already performed in-run verify (E5) and (E7) to machine precision. The final report will include a deterministic checker and a separate principal-triple normalization gate using the designated account04/B07 physical-core theorem.
