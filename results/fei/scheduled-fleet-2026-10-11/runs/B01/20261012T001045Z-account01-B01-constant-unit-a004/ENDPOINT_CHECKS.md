# A004 endpoint and unit checks

All logarithms in this file are base two.  Put (P(S)=\widehat f(S)^2), (v=1-P(\varnothing)), and (I_i=\Pr[f(x)\ne f(x^{\oplus i})]).

## Exact elementary endpoints

| Function | Spectral law | (H) | (I) | (v) | (I-v) | (D=\min_U I(\chi_Uf)) |
|---|---:|---:|---:|---:|---:|---:|
| constant (\pm1) | point mass at (\varnothing) | 0 | 0 | 0 | 0 | 0 |
| dictator (x_i) | point mass at (\{i\}) | 0 | 1 | 1 | 0 | 0 |
| character (\chi_U, U\ne\varnothing) | point mass at (U) | 0 | |(U)| | 1 | |(U)|-1 | 0 |
| parity on all (n) coordinates | point mass at ([n]) | 0 | (n) | 1 | (n-1) | 0 |

Constants satisfy FEI as (0\le C0); (H/I) is not formed.  Character multiplication translates the spectral law and preserves entropy, but it can change influence from (0) to (n) or back.  This is why a statement in terms of (D(f)) is not interchangeable with one in terms of (I(f)).

The normalized/non-normalized nonempty split is

\[
H(f)=h_2(v)+vH(P(\cdot\mid S\ne\varnothing)),
\]

whereas the raw nonempty entropy is (vH(P(\cdot\mid S\ne\varnothing))+v\log_2(1/v)).  These differ by the empty-atom term ((1-v)\log_2(1/(1-v))).

## Nearly constant one-point defect

Let (f=-1) at one input and (+1) elsewhere on (n) bits, and set (\delta=2^{-n}). Then

\[
\widehat f(\varnothing)=1-2\delta,\qquad
|\widehat f(S)|=2\delta\quad(S\ne\varnothing),
\]
\[
I_i=2\delta,quad I=2n\delta,quad
v=4\delta(1-\delta),quad
I-v=2\delta(n-2)+4\delta^2,
\]
and
\[
H=(1-2\delta)^2\log_2\frac1{(1-2\delta)^2}
 +(\delta^{-1}-1)4\delta^2\log_2\frac1{4\delta^2}.
\]
Thus (H/I\to4).  The rare logarithm is real, but this genuine Boolean family has bounded ratio and is not an FEI counterfamily.

## Sharp audit of the A003 additive constants

For a coordinate (i), write (a_T=\widehat f(T)), (b_T=\widehat f(T\cup\{i\})), (x=a_T^2), (y=b_T^2), and (q=x+y).  The pair contributions satisfy

\[
E_i-L_i=x\log_2(1+y/x),
\]
\[
J_i=\frac12(q+2|a_Tb_T|)\log_2\frac{q+2|a_Tb_T|}{q}
 +\frac12(q-2|a_Tb_T|)\log_2\frac{q-2|a_Tb_T|}{q},
\]
where (\Delta_iH=E_i+J_i).  The A003 bounds give

\[
E_i-L_i\le \frac{I_i}{\ln2},\qquad
J_i\le\frac{2I_i}{\ln2},\qquad
\Delta_iH-L_i\le\frac{3I_i}{\ln2}.
\]

These constants are each optimal for a universal **fixed-coordinate** inequality, even over genuine Boolean functions.  Let (m) be even, let (u:\{-1,1\}^m\to\{-1,1\}) be bent, and obtain (w) by flipping (u) at one input (x_0).  Define the selector (F(x,z)) whose two restrictions are (u,w).  At (z),

\[
b_T=2^{-m}u(x_0)\chi_T(x_0),\qquad
a_T=\widehat u(T)-b_T,qquad I_z(F)=2^{-m}.
\]

With (Q=2^{m/2}), the ratios (r_T=x/y) equal ((Q-1)^2) on ((Q^2+Q)/2) pairs and ((Q+1)^2) on ((Q^2-Q)/2) pairs.  Indeed (\sum_Ta_Tb_T=0), while (\sum_T\operatorname{sgn}(\widehat u(T)b_T)=Q).

For (r=x/y), define

\[
U(r)=r\log_2(1+1/r),
\]
\[
V(r)=(r+1)\phi\!\left(\frac{2\sqrt r}{r+1}\right),\quad
\phi(t)=\frac{(1+t)\log_2(1+t)+(1-t)\log_2(1-t)}2.
\]

Then ((E_z-L_z)/I_z) is the corresponding average of (U(r_T)), (J_z/I_z) is the average of (V(r_T)), and

\[
U(r)\to\frac1{\ln2},\qquad V(r)\to\frac2{\ln2}.
\]

Hence all three A003 local losses are asymptotically sharp simultaneously.  This does **not** prove that the sandwiches between the optimal global constants are sharp: the induction chooses an existential coordinate, and the bent-defect selector may have cheaper data coordinates.

The first unsupported improvement is therefore precise.  To replace (3/\ln2) by some (c<3/\ln2) in `DOWN => FEI`, one needs a nonlocal/existential theorem such as

\[
\min_{i:I_i>0}\frac{\Delta_iH}{I_i}\le \frac{L(f)}{I(f)}+c
\quad\text{for every nonconstant Boolean }f,
\]

not a better fixed-coordinate scalar inequality.  This remains OPEN.

