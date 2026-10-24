# B17 FEI creative continuation: one-overlap MUX closure with constant 6

**Status:** **PARTIAL. Full Friedgut--Kalai Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary route:** APPROACH 7 (larger composition/read-twice class), informed by the killed APPROACH 3 sensitivity coupling and APPROACH 14 point-process relaxations.  
**Fresh source state used:** `yspennstate/math-open-problems` master was refreshed during this run; the standing read-once continuation and newest B17 artifacts were read before this derivation.  
**Novelty:** no literature-priority claim is made.

## 1. What moved

The preceding B17 theorem handled a fresh selector `z` whose two Boolean branches lived on disjoint variable sets and proved that MUX composition preserves every FEI constant `C>=6`. The newest finite artifact then tested the first genuinely overlapping case, where

- `a=a(y,U)`,
- `b=b(y,V)`,
- `U` and `V` are disjoint,
- the branches share exactly one physical bit `y`, and
- `z` is a fresh selector.

This run closes that finite-to-universal gap analytically:

> **One-overlap MUX theorem.** If `a(y,U)` and `b(y,V)` are arbitrary Boolean functions with `U cap V=empty`, and
> `f=MUX_z(a,b)` with fresh `z`, then the extra spectral-entropy toll satisfies
>
> `Omega(a,b) <= 6 Inf_z(f)`.
>
> Consequently, if both branches satisfy `H<=C I` for some `C>=6`, then so does `f`.

Thus the previous disjoint-branch selector class extends to a recursive **one-overlap selector class**: at every MUX node the two child variable sets may intersect in one variable, not only in zero variables. Starting from literals/constants, every function in this class obeys `H<=6I`.

The theorem is a structured-class advance only. It does not cover arbitrary read-twice formulas and does not contradict the current unrestricted lower-bound handoff above 6.52.

## 2. Exact Fourier identities

Embed both branch spectra in the common cube on `{y} union U union V`. Write their Fourier coefficients as `alpha_S` and `beta_S`. For

`f = (a+b)/2 + z (a-b)/2`, 

we have for every subset `S` not containing `z`

`fhat(S)=(alpha_S+beta_S)/2`,  
`fhat(S union {z})=(alpha_S-beta_S)/2`.

Put `phi(t)=-t log_2 t` (`phi(0)=0`) and

`psi(x,y)=phi((x+y)^2/4)+phi((x-y)^2/4)-[phi(x^2)+phi(y^2)]/2`.

Then

`H(f)=[H(a)+H(b)]/2 + Omega`,  where  `Omega=sum_S psi(alpha_S,beta_S)`.      (2.1)

For influence, all nonselector coordinates are selected branchwise, while

`Inf_z(f)=Pr[a(y,U) != b(y,V)]`.

Let

`x=(alpha_empty,alpha_{y})`, `w=(beta_empty,beta_{y})`, `d=x dot w`.

Independence of `U,V` conditional on `y` gives `E[ab]=d`, hence

`q:=Inf_z(f)=(1-d)/2`,

and therefore

`I(f)=[I(a)+I(b)]/2 + q`.                                                    (2.2)

Because the residual variable sets are disjoint, the two spectra can overlap only on `empty` and `{y}`. Since `psi(t,0)=t^2`, Parseval gives

`Omega = R_a+R_b+psi(x_0,w_0)+psi(x_1,w_1)`,                                (2.3)

where

`R_a=1-x_0^2-x_1^2`, `R_b=1-w_0^2-w_1^2`.

The whole problem is therefore a four-scalar inequality, but with an important Boolean feasibility constraint. If `m_+` and `m_-` are the conditional means of `a` at `y=+1,-1`, then

`x_0=(m_++m_-)/2`, `x_1=(m_+-m_-)/2`,

so `|x_0|+|x_1|<=1`. Likewise `|w_0|+|w_1|<=1`. This diamond constraint is exactly what the unrestricted local restriction toll lacks.

## 3. Scalar slack lemma

For `r,s in [0,1]`, define

`L(r,s)=1+r^2+s^2-3rs-psi(r,s)`.

Let `M=max(r,s)` and `m=min(r,s)`. Then

`L(r,s) >= 1-M^2 + (1/2)(M-m)^2`.                                           (3.1)

### Proof

Set

`A=(M^2+m^2)/2`, `u=2Mm/(M^2+m^2)`, `v=(M^2-m^2)/(M^2+m^2)`.

Thus `u^2+v^2=1`. With

`g(t)=h_2((1+t)/2)`,

a direct grouping of the four `phi` terms gives

`psi(r,s)=A F(u)`,  `F(u)=1+g(u)-g(v)`.                                     (3.2)

We use the elementary binary-entropy bounds

`4p(1-p) <= h_2(p) <= 2 sqrt(p(1-p))`,                                      (3.3)

which imply `g(u)<=v` and `g(v)>=u^2`. Therefore

`F(u)<=1+v-u^2`.

Since `rs=A u`,

`L=1-A(F(u)-2+3u)`

and substitution of the preceding upper bound gives, after elementary simplification,

`L >= 1-M^2 + (M-m)^2 (M^2-Mm+m^2)/(M^2+m^2)`.                              (3.4)

Finally

`2(M^2-Mm+m^2)-(M^2+m^2)=(M-m)^2>=0`,

so the last fraction is at least `1/2`, proving (3.1).

For completeness, (3.3) is a one-variable calculus lemma. In the variable `t=|2p-1|`, `g(t)=h_2((1+t)/2)` has

`g'(t)=-atanh(t)/ln 2`, `g''(t)=-1/[(1-t^2)ln 2]`.

For the lower bound, `g(t)-(1-t^2)` vanishes at `t=0,1`; its second derivative is strictly decreasing and changes sign once, so its first derivative rises from zero and then falls through zero once, leaving the function nonnegative. For the upper bound, `sqrt(1-t^2)-g(t)` also vanishes at `0,1`; its second derivative has the sign of `1/ln2-1/sqrt(1-t^2)` and therefore changes sign once, giving the same rise-then-fall argument. Hence `1-t^2<=g(t)<=sqrt(1-t^2)`, equivalent to (3.3).

## 4. Diamond lemma

Let `a=(a_0,a_1)` and `b=(b_0,b_1)` be nonnegative vectors with

`a_0+a_1<=1`, `b_0+b_1<=1`.

Then

`L(a_0,b_0)+L(a_1,b_1)>=1`.                                                 (4.1)

### Proof

For each coordinate let `M_j=max(a_j,b_j)` and `m_j=min(a_j,b_j)`. By (3.1),

`sum_j L(a_j,b_j) >= 2-(M_0^2+M_1^2) + (1/2) sum_j (M_j-m_j)^2`.             (4.2)

If both coordinatewise maxima come from the same vector, then

`M_0^2+M_1^2 <= (M_0+M_1)^2 <=1`,

and (4.1) follows immediately. The same is true if the maxima are mixed but their squared sum is at most one.

It remains to consider the mixed case, say

`M_0=a_0>=b_0=m_0`, `M_1=b_1>=a_1=m_1`, and `a_0^2+b_1^2>1`.

Put `t=a_0+b_1-1>0`. From the two `l_1` constraints,

`b_0<=1-b_1`, `a_1<=1-a_0`,

so

`a_0-b_0>=t`, `b_1-a_1>=t`.

Hence the final term in (4.2) is at least `t^2`. But

`t^2-(a_0^2+b_1^2-1)=2(1-a_0)(1-b_1)>=0`.

Thus (4.2) is again at least one. This proves (4.1).

## 5. One-overlap toll theorem

Return to the signed Fourier cores `x,w`. Since `psi` is unchanged if either scalar argument changes sign,

`Omega` depends on the core signs only through the selector denominator. Replacing `x_j,w_j` by their absolute values can only increase the dot product, hence can only make `3(1-d)` smaller. It therefore suffices to prove the inequality for the nonnegative absolute-value cores, which satisfy the diamond constraints.

From (2.3),

`3(1-d)-Omega`
` = 1+||x||_2^2+||w||_2^2-3d-[psi(x_0,w_0)+psi(x_1,w_1)]`
` = L(|x_0|,|w_0|)+L(|x_1|,|w_1|)-1`
` >=0`

by the diamond lemma. Therefore

`Omega <= 3(1-d)=6q=6 Inf_z(f)`.                                            (5.1)

Combining (2.1), (2.2), and (5.1), if `H(a)<=C I(a)` and `H(b)<=C I(b)` with `C>=6`, then

`H(f) <= C[I(a)+I(b)]/2 + 6q <= C I(f)`.

This proves the theorem.

## 6. Recursive one-overlap selector class

Define a class recursively from literals and constants. At an internal node take

`F=MUX_z(A,B)`,

where `z` is fresh and the child variable sets intersect in at most one variable. If the intersection is empty, the preceding disjoint-selector theorem applies; if it is one variable, theorem (5.1) applies. Induction yields

`H(F)<=6 I(F)`

for every function in this one-overlap recursive MUX class.

This is strictly a semantic/syntactic class theorem. It is not asserted that every read-twice formula admits such a decomposition. The next obstruction is a gate whose two children share two or more physical variables: the two-dimensional diamond becomes a `2^r`-coefficient bounded-function Fourier body, and the above mixed-maxima argument no longer directly closes.

## 7. Stress test and boundary behavior

A fresh exhaustive stress test over every ordered pair of three-bit Boolean branches `a(y,u_1,u_2)` and `b(y,v_1,v_2)` gives `256^2=65,536` overlapping branch pairs. For all pairs the theorem slack `6q-Omega` is nonnegative. The largest observed `Omega/q` is

`4.905865002596163`,

at core vectors `(-3/4,1/4)` and `(-1/4,3/4)`, where `q=5/16` and `Omega=1.5330828133113008`.

The finite test is only a stress test; the proof above is continuous and dimension-free in the residual blocks.

The previously observed bent-plus-one-point-flip family still kills the stronger unrestricted pointwise claim `Omega<=C q` when the whole overlap block is allowed to grow: there `Omega/q` grows like the overlap dimension. The present theorem survives precisely because a **single shared physical bit** forces the core into the two-dimensional `l_1` diamond.

## 8. Next target

The next useful extension is not another sensitivity-set coupling. It is the `r=2` overlap case. The right object is the Fourier image of a bounded function `g:{-1,1}^2->[-1,1]`, not an arbitrary four-vector. A successful proof should exploit the eight physical box inequalities `|g(y)|<=1` for the two branch conditional means. The concrete target is a finite constant `C_2` in

`Omega <= C_2 Inf_z`

for two shared bits with otherwise disjoint residuals. Proving `C_r=O(r)` for fixed overlap `r`, and then finding a summable way to charge overlap size in a read-twice decomposition, would materially enlarge the class toward full FEI.
