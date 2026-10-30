# B06 improvement: same nine-eigenvalue theorem with constant 362; shared-overlap scalar receiver

Run: `20260924T153355Z-fleet01-B06-fixedmult-audit-r12`
Source audited: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.
Status: complete supporting derivation, not a replacement source file and not a multiplicity-eight theorem.

## Theorem 1 — retuned nine-eigenvalue constant

Under exactly the hypotheses of the pinned nine-eigenvalue manuscript,

- independent real coordinate densities bounded by `K`,
- arbitrary real symmetric `A`,
- arbitrary `b,c`,
- `s_9(A)>=s>0`,

one has

`||p_(X^TAX+b^TX+c)||_infinity < 362 K^2/s`.

The proof is the manuscript proof with only the pivot parameters retuned. No input hypothesis or spectral assumption changes.

### 1. Normalized parameters

Normalize `K=s=1` and set

`d=3/40`,
`p=1/340`,
`h=41/500`,
`kappa=h^2=1681/250000`.

A pivot is again either `|A_ii|>=d` or a principal two-coordinate determinant of modulus at least `p`.

Without a pivot,

`|A_ii|<d`,
`|A_ij|^2 < p+d^2 = 233/27200`.

Put `q0=13/140`. The exact comparison is

`q0^2-(p+d^2)=3/53312>0`,

so `|A_ij|<q0` for `i!=j`.

### 2. The disjoint-volume proposition still closes for k<=3

Suppose the order-`k` conclusion fails. Exactly as in Proposition 7.4 of the pinned source, choose `0<=r<=k-1` with `V_r>0` and

`V_(r+1)<kappa V_r`.

For `r=0`,

`||A|| <= d+sqrt(V_1) < d+h = 157/1000 <1`,

contradicting the required large singular value.

For `r=1,2`, the sampled interpolation gives

`A=D+R+E`,
`rank R<=3r`,
`rank R_LL<=r`,
`D=0` on the seed,
`E_ii=0`,
`||E||_F <= (r+1)h`.

The same rank perturbation forces `r+1` diagonal entries of `D` in `L` to have modulus at least `1-(r+1)h`. On those coordinates,

`|R_ii| >= 1-(r+1)h-d`,

while each off-diagonal entry is bounded by

`|R_ij| <= |A_ij|+|E_ij| < q0+(r+1)h`.

Hence the strict diagonal-dominance margins are

`1-d-r q0-(r+1)^2 h`.

They are exactly

- `r=1`: `3529/7000>0`,
- `r=2`: `9/7000>0`.

Thus the `(r+1)`-coordinate restricted block is invertible, contradicting `rank R_LL<=r`. Therefore for `k=1,2,3`,

`no pivot and s_(4k-3)(A)>=1  =>  V_k(A)>=kappa^k`.

The fair coordinate cut then gives a literal crossing block with

`Z_k >= 4^(-k) kappa^k`,

hence

`Z_k^(-1/(2k)) <= 2/h = 1000/41`.

### 3. A rigorous no-pivot density bound below 362

The manuscript constant is

`C3=3 sqrt(2) e (9/2)^(1/6)`.

We first record the elementary upper bound `e<68/25`. Indeed

`e = sum_(n=0)^6 1/n! + sum_(n>=7)1/n!`

and, because every factor after `7!` is at least `8`,

`sum_(n>=7)1/n! <= (1/7!)(1+1/8+1/8^2+...) = 1/4410`.

Thus

`e < 1957/720+1/4410 = 31967/11760 <68/25`.

Now `C3^6=26244 e^6`, and the exact rational comparison

`(7421/500)^6 - 26244(68/25)^6`
`= 962944162789009250521 / 15625000000000000 >0`

gives

`C3<7421/500`.

Therefore in the no-pivot `s_9>=1` branch,

`||p_Q||_infinity <= C3*(2/h)`
`< (7421/500)*(1000/41)`
`= 14842/41`
`=362`.

The inequality is strict because the bound on `C3` is strict.

For the no-pivot `s_5>=1` half-potential used later, the manuscript's `C2<14` and

`sqrt(2/h)=sqrt(1000/41)<5`

give the same convenient bound `<70`.

### 4. Scalar-pivot branches remain below 362

The first scalar branch is

`70 d^(-1/2) < 280`.

The pair-pivot Schur branch is

`16 p^(-1/4)d^(-1/2) <16*5*4=320`,

since `340<5^4` and `d^(-1/2)<4`.

For the scalar/scalar logarithmic branch, use

`d^(-1/2)<11/3`

because `40/3<121/9`. Also use the elementary inequalities

`pi<22/7`, `log 2<7/10`, `log 5<161/100`.

The last two are proved by positive exponential Taylor partial sums:

`sum_(j=0)^3 (7/10)^j/j! =12013/6000>2`,

and

`sum_(j=0)^7 (161/100)^j/j!`
`=40011628664174467/8000000000000000>5`.

For completeness, `pi<22/7` follows from the classical positive integral identity

`0 < integral_0^1 x^4(1-x)^4/(1+x^2) dx =22/7-pi`.

Therefore

`J0+2L0 = pi+4 log2+8+8 log5`
`< 22/7 +14/5 +8 +322/25`
`=4694/175`.

Consequently

`d^(-1/2)+(J0+2L0)/d`
`< 11/3 +(4694/175)*(40/3)`
`=37937/105`
`<362`.

### 5. Two-coordinate pivot branches remain below 362

For a definite pair,

`pi/sqrt(p)=pi sqrt(340)<4*19=76`.

For an indefinite pair, the manuscript bound becomes

`sqrt(340)(10+4 log10)+1/e`.

The positive Taylor partial sum

`sum_(j=0)^6 (7/3)^j/j! =1071641/104976>10`

proves `log10<7/3`. Also `sqrt(340)<37/2` and `1/e<1/2`. Hence

`sqrt(340)(10+4log10)+1/e`
`< (37/2)*(58/3)+1/2`
`=2149/6`
`<362`.

All cases are therefore strictly below `362` in the normalized theorem. The manuscript scaling `Y=KX`, `Q=(s/K^2) Qtilde` then gives

`||p_Q||_infinity <362 K^2/s`.

This completes Theorem 1.

---

## Theorem 2 — an exact scalar receiver for one shared overlap minor

This is a supporting step toward multiplicity eight, not an aggregate theorem.

Let `h` be a literal original coordinate with `a=A_hh !=0`. Let `S,T` be disjoint two-element original-coordinate sets, also disjoint from `h`, and suppose

`B=A_(S,T)`

is invertible. Write

`u=A_(S,h)`, `v=A_(T,h)`

as column vectors and define the same-index bordered determinant

`Delta = det A_(S union {h}, T union {h})`.

After completing the square in the literal coordinate `X_h`, the Schur complement on the remaining coordinates has `S`-to-`T` crossing block

`B' = B-u v^T/a`.

The matrix determinant lemma gives the exact identity

`det B'`
`=det B * (1-v^T B^(-1)u/a)`
`=Delta/a`.

The scalar conditional profile from the manuscript gives, for almost every output `z`,

`p_Q(z) <= |a|^(-1/2) E|z-R|^(-1/2)`,

where `R` is the Schur-complement quadratic polynomial in the remaining original independent coordinates.

Apply the manuscript's marginal-free order-two theorem to the literal disjoint crossing block `B'`. Since for a `2x2` matrix

`Z_2(B')=det(B')^2`,

that theorem yields

`sup_z E|z-R|^(-1/2) <= C2 |det B'|^(-1/4)`.

Therefore

`||p_Q||_infinity`
`<= C2 |a|^(-1/2) |Delta/a|^(-1/4)`
`= C2 (|a Delta|)^(-1/4)`.

No rotation of the random variables is used; the pivot and crossing block are both in literal original coordinates, and arbitrary affine/self terms are retained by the two quoted manuscript lemmas.

### Why this does not yet prove multiplicity eight

The current eight-eigenvalue algebraic theorem controls the aggregate unweighted overlap mass

`W_(2,1)^cross = sum Delta^2`.

The receiver above costs `(|a Delta|)^(-1/4)`. An aggregate lower bound on `sum Delta^2` gives neither a dimension-free lower bound on a single `|a Delta|` nor any control at the allowed endpoint `a=0`. In particular, the no-pivot chamber is perfectly compatible with every shared diagonal being arbitrarily small.

Thus the first remaining implication is now explicit:

> construct a product-preserving shared-coordinate analytic receiver that remains finite at `a=0` and consumes aggregate overlap mass without replacing it by a largest-minor bound.

Until that endpoint is closed, multiplicity eight is not established. The unrestricted three-eigenvalue theorem is also not established.
