SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T05:00:29Z.
attacking: the newest account03/B20 r25 collar debt, first by paying the 3/4-dominant physical-star endpoint and then compiling the large adjusted-diagonal branch into fixed original-coordinate aggregate resources.

# Early checkpoint — dominant-star payment and adjusted-diagonal compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T050029Z-account02-B20-QFORM-r25`.
Status: substantive checkpoint; full QFORM remains OPEN.

The newest completed designated-partner report is account03/B20 r25, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T041231Z-account03-B20-QFORM-r25/REPORT.md`. In its exact-rank-three small-Pluecker collar, after earlier paid exits, there is an ORIGINAL physical hub `i` with

`a=A_ii`, `m=A[i,-i]`, `M=||m||_2`,

`|a|<1/64`, `M^2>1023/4096`.

For the nondominant-star side it proves a stable-alignment representation of the residual physical block `H=A[-i,-i]`: there exists `theta` such that

`||Off(H-theta m m^T)||_F^2 <= (32/M^2) sum_j Delta_j^2`,

where

`Delta_j^2=||m_{-j}||^2||H[j,-j]||^2-<m_{-j},H[j,-j]>^2`.

It then leaves the `3/4`-dominant physical-star endpoint and the large adjusted-diagonal branch among the debts. The calculations below stay in original coordinates.

## 1. The 3/4-dominant physical-star endpoint is fully paid

Assume some physical residual coordinate `j` satisfies

`m_j^2>(3/4)M^2`.

Then

`m_j^2>3069/16384`,

so

`|m_j|>sqrt(3069)/128 = 0.432801...`.

If `|H_jj|>=1/32`, the completed exact-rank-three scalar-pivot theorem already pays the branch (account03/B20 r25 records the bound `<1024`). Hence every still-unpaid dominant-star state may be assumed to satisfy `|H_jj|<1/32`.

Consider the ORIGINAL physical principal pair

`P=[[a,m_j],[m_j,H_jj]]`.

Because `|a|<1/64`,

`det P=a H_jj-m_j^2<0`,

and quantitatively

`D:=|det P|>3069/16384-1/2048=3061/16384`.

Also `P` is a diagonal perturbation of `[[0,m_j],[m_j,0]]` of operator norm at most `1/32`, so Weyl's singular-value inequality gives

`kappa:=sigma_min(P) > sqrt(3069)/128-1/32=(sqrt(3069)-4)/128`.

The completed arbitrary-rank physical-indefinite-pair theorem applies under the full target hypothesis `s_3(A)>=1` and gives

`||p_Q||_infinity <= 3*400^(1/3)(D^2 kappa)^(-1/6)`.

Substitution of the preceding exact lower bounds yields

`||p_Q||_infinity <45.017 <46`.

Thus the entire `3/4`-dominant **physical star atom** endpoint of the r25 collar is paid, without any rank restriction on additional ambient spectrum and without rotating the product source.

## 2. A large adjusted diagonal compiles into a second star or aggregate two-gradient energy

Now assume the partner's nondominant condition

`m_j^2 <= (3/4)M^2` for every residual j,

and write

`D_*=diag(a, d_j:j in J)`, `d_j=H_jj-theta m_j^2`,

`E_*=Off(H-theta m m^T)`.

Suppose `||D_*||_op>1/2`. Since `|a|<1/64`, there is a residual `j` with `|d_j|>1/2`.

Again, if `|H_jj|>=1/32`, the scalar-pivot exit pays. Otherwise

`|theta|m_j^2 >= |d_j|-|H_jj| >15/32`.                         (2.1)

Put `e_j=H[j,-j]-theta m_j m_{-j}`. There are two cases.

### Case A: `||e_j||_2<=1/8`

The nondominant condition gives

`||m_{-j}||/|m_j| >=1/sqrt(3)`.

Using (2.1),

`||H[j,-j]||_2
 >= |theta||m_j|||m_{-j}||-||e_j||
 >15/(32sqrt(3))-1/8
 =(5sqrt(3)-4)/32
 =0.145632... .`

Therefore a SECOND ORIGINAL physical star has squared norm

`||H[j,-j]||_2^2 > ((5sqrt(3)-4)/32)^2 >0.0212089`.             (2.2)

The completed heavy-hub compound-energy identity may then be applied to this actual physical row; it forces a fixed one-overlap or fully-disjoint aggregate second-gradient packet before any local minor is selected.

### Case B: `||e_j||_2>1/8`

Then `||E_*||_F>1/8`. The partner's stable-alignment inequality yields

`sum_l Delta_l^2 >= (M^2/32)||E_*||_F^2
 > M^2/2048
 >1023/8388608`.                                                (2.3)

Randomly partitioning the residual physical coordinates exactly as in account03/B20 r25 captures one eighth of this aggregate in an ORIGINAL cross block, hence produces a physical cross block `B` with

`e_2(BB^T)>1023/67108864`.                                      (2.4)

This is weaker numerically than the partner's main aggregate branch but, crucially, is a fixed dimension-free resource. It shows that a large adjusted diagonal cannot remain an isolated non-source-realizable coefficient: unless an actual scalar pivot already pays, it creates either a second physical star or a fixed aggregate two-gradient packet.

## 3. Near-coloop endpoint is reduced to the same nondominant aggregate geometry

In the exact-rank-three selected-frame notation, if the hub leverage satisfies `c_i=||u_i||^2>3/4`, then

`a^2+M^2=u_i^T M_core^2 u_i >=c_i`.

Since `|a|<1/64`,

`M^2>3/4-1/4096=3071/4096`.

If this stronger star has a `3/4`-dominant physical atom, Section 1 pays it by `<46`. Otherwise the stable-alignment compiler of the partner applies with the larger `M`. In particular, on its aggregate branch with `||D_*||op<=1/2`, it strengthens to

`sum_j Delta_j^2>3071/524288`,

and a physical cut captures

`e_2(BB^T)>3071/4194304`.

If that cut additionally has `s_3(B)>=1/64` and maximum row range-leverage at most `1/2`, the partner's q=4/3 three-volume receiver gives a continuous density `<340` (the exact expression is `(9sqrt(3)e/2)[(3071/4194304)/(3*4096)]^(-1/6)`). Thus the near-coloop endpoint is no longer a separate dominant-star debt: after the paid atom case it is another, quantitatively stronger, aggregate localization problem.

## 4. Current mathematical frontier

The first unpaid implication after these calculations is no longer the partner's raw `3/4`-dominant-star splice. It is an aggregate-third-source problem: turn the fixed one-overlap/disjoint compound energy, or a captured `e_2` cross block when the three-volume diffuse gate fails, into a universal `L^infinity` bound while keeping arbitrary same-bank curvature and original-coordinate product provenance.

This cannot be solved by declaring `e_2>0` alone sufficient: the rank-two product model has a logarithmic output singularity. A genuine third source must be spent. The newest account03/B19 r26 theorem supplies one such paid mechanism when an exact rank-two physical cross bank has a transverse within-bank curvature direction; the remaining work is to force one of those paid third-source geometries from the localized/low-cross-rank aggregate collar.

No pointwise oscillatory decay, unrestricted fiber supremum, arbitrary-joint 3D coarea, or post-rotation independence is used here. Full QFORM remains open.
