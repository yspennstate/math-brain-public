# Scalar-Q_rest conditioning is also not a universal bridge

Run: `20260922T175342Z-fleet03-B16-QFORM-r14`  
Programme: QFORM-DENSITY-3EIG-20260922  
Status: **new correction after owner-control revision 2026-09-22.11; full QFORM remains OPEN**.

## 1. Claim tested

Owner-control revision 2026-09-22.11 correctly retires conditioning on the entire complementary spectral vector, but proposes as the new highest-value bridge the scalar conditioning

\[
M:=\sup_b\|p_{Q_3\mid Q'=b}\|_\infty,
\qquad Q'=Q_{\rm rest},
\]

with the hope that `M` is universally bounded. The identity

\[
p_Q(t)=\mathbb E_{Q'}p_{Q_3\mid Q'}(t-Q')
\]

and hence `||p_Q||_infinity<=M` are valid. What fails is the proposed universal bound on `M`.

The counterexample below lies inside the **diagonal target class**, whose full output density is already known to be bounded by `pi`. Thus it refutes only the scalar-conditioning proof interface, not the QFORM conjecture.

## 2. Independent cap-one laws and orthogonal core/rest split

Fix an integer `m>=1`. Let

\[
E_m=\bigcup_{k=0}^{m-1}[10k,10k+1/m].
\]

Take independent variables with densities

\[
f_1=1_{[0,1]},\qquad f_2=1_{E_m},\qquad
f_3=f_4=1_{[0,1]}.
\]

All are probability densities bounded by one. Define the orthogonal coordinates

\[
S=\frac{X_1+X_2}{\sqrt2},\qquad
D=\frac{X_1-X_2}{\sqrt2}.
\]

Split the quadratic form as

\[
Q_3=D^2+X_3^2-X_4^2,
\qquad Q'=S^2.
\]

Then

\[
Q=Q_3+Q'=X_1^2+X_2^2+X_3^2-X_4^2. \tag{2.1}
\]

Thus the full matrix is simply `diag(1,1,1,-1)`, with four eigenvalues of magnitude one. In particular it satisfies the full target assumptions, and the proved diagonal theorem gives `||p_Q||_infinity<=pi`.

## 3. An exact scalar level makes the remaining core nearly rank two

Put

\[
s_m=\frac{1}{\sqrt2 m},\qquad
b_m=s_m^2=\frac1{2m^2},\qquad
a_m=\frac1{\sqrt2 m}.
\]

Because `X_1,X_2>=0`, conditioning on `Q'=b_m` is the same as conditioning on `S=s_m`.

The orthogonal change `(X_1,X_2)<->(S,D)` has Jacobian one. At `S=s_m`, the equation `X_1+X_2=1/m` can meet only the first component `[0,1/m]` of `E_m`; the other components begin at ten. The admissible interval is exactly

\[
-a_m\le D\le a_m,
\]

and the joint `(S,D)` density equals one there. Therefore

\[
p_S(s_m)=2a_m=\frac{\sqrt2}{m}
\]

and

\[
\boxed{D\mid(Q'=b_m)\sim {\rm Unif}[-a_m,a_m].} \tag{3.1}
\]

The variables `X_3,X_4` are untouched by this conditioning and remain independent uniforms on `[0,1]`.

## 4. Exact logarithmic lower bound for the conditional core density

Let

\[
T=X_3^2-X_4^2.
\]

For `0<t<1`, the density of `T` is

\[
\begin{aligned}
p_T(t)
&=\frac14\int_0^{1-t}\frac{dv}{\sqrt{v(v+t)}}\\
&=\frac12\operatorname{arsinh}\sqrt{\frac{1-t}{t}}.
\end{aligned} \tag{4.1}
\]

The law is symmetric, so `p_T(-t)=p_T(t)`. For `0<d<1`, substituting `t=d^2` gives

\[
p_T(d^2)=\frac12\operatorname{arcosh}(1/d). \tag{4.2}
\]

From (3.1), the conditional density of `Q_3=D^2+T` at zero is

\[
\begin{aligned}
p_{Q_3\mid Q'=b_m}(0)
&=\frac1{2a_m}\int_{-a_m}^{a_m}p_T(-d^2)\,dd\\
&=\frac1{a_m}\int_0^{a_m}p_T(d^2)\,dd\\
&=\frac1{2a_m}\int_0^{a_m}\operatorname{arcosh}(1/d)\,dd.
\end{aligned} \tag{4.3}
\]

Since for `0<d<1`,

\[
\operatorname{arcosh}(1/d)
=\log\frac{1+\sqrt{1-d^2}}{d}
\ge\log(1/d),
\]

we obtain

\[
\boxed{
 p_{Q_3\mid Q'=b_m}(0)
 \ge \frac12\left(\log\frac1{a_m}+1\right)
 =\frac12\bigl(\log(\sqrt2 m)+1\bigr).
} \tag{4.4}
\]

Consequently

\[
\boxed{
\sup_b\|p_{Q_3\mid Q'=b}\|_\infty
\ge\frac12\bigl(\log(\sqrt2 m)+1\bigr)\to\infty.
} \tag{4.5}
\]

This is an exact analytic divergence. No histogram, pointwise oscillatory estimate, rotated-coordinate independence, or receiver-only projection bound is used.

## 5. Interpretation

The scalar conditioning `Q'=b_m` forces the spectral coordinate `D` into an interval of width `O(1/m)`. The remaining two opposite-sign squares `X_3^2-X_4^2` have the mandatory rank-two logarithmic singularity. The small `D^2` term regularizes it only at scale `m^{-2}`, leaving a peak of order `log m`.

Yet after averaging over `Q'=S^2`, the full form (2.1) is diagonal and has density at most `pi`. The shift/mixing over `Q'` is therefore essential; replacing the mixture by the worst conditional core discards exactly the smoothing that makes the full density bounded.

Hence owner revision 2026-09-22.11's proposed scalar conditional-local-limit target is another **sufficient but non-universal** interface. The next proof mechanism must control the shifted mixture directly, or aggregate product structure before taking a worst-case scalar condition.

## 6. Relation to the earlier B16 and concurrent B18 corrections

The earlier B16 report proved that conditioning on the full complementary vector makes every positive conditional projection-density moment exponent below one unbounded, even with pair Gram area `1/2`. Fleet03/B18 independently corroborated the vector-conditioning failure and embedded it in a full-rank spectral-window family.

The present correction is strictly different: even after replacing the whole complementary vector by the single scalar quadratic statistic `Q'`, the worst conditional **quadratic output density** itself is unbounded. Thus neither a normalized conditional-vector moment nor the scalar worst-condition `M` can serve as the universal bridge.

Full QFORM remains OPEN. The full density in this counterexample is bounded; continuity of the general theorem is not established here.
