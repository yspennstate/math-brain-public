# Four crossings obstruct a global component-boundary comparison

Date: 2026-10-02. **Complete constructive proof; independent analytic audit passes.**

This note disproves the proposed dimension-independent inequality
\[
 \min\{B_+(f),B_-(f)\}\le D_m I(f)
\]
for fixed finite-crossing functions, already when \(m=4\). Here \(B_+\)
and \(B_-\) are the sums of the physical influences of the separate
positive and negative score-interval components. Empty components are
removed. Every component in the construction below is nonempty, and all
four crossings are genuine sign jumps. This is an obstruction to that
global proof method. The constructed functions themselves satisfy FEI
with a fixed constant, as shown at the end.

The [independent analytic audit](four_crossing_component_boundary_analytic_audit.md)
checks the construction and all three boundary formulas; a full
[continuity and entropy audit](four_crossing_component_boundary_continuity_entropy_audit.md)
also verifies the exact spectrum and the uniform FEI bound below. The
[independent integer checker](independent_four_crossing_component_check.py)
and [results](independent_four_crossing_component_checks.json) verify 19
full truth tables on 415,024 vertices through dimension 18, including
every component boundary and the complete integer Walsh spectrum. Seven
further exact symbolic cases extend to dimension 65,544. A separate
[five-crossing proof](global_component_boundary_analytic_candidate.md)
and its [exact checks](global_component_boundary_obstruction_checks.json)
are preserved. No novelty or external peer review is certified.

All variables are independent uniform signs. For an event \(E\), write
\(h_E=1-2\mathbf1_E\), and use physical flip influence
\(I(h)=\sum_i\Pr[h(X)\ne h(X^{\oplus i})]\).

## 1. An exact attained-score construction

Fix \(k\ge2\) and an even \(N=2d\ge2\). Put
\[
 p=2^{-k},\quad q=2^{-N},\quad
 a_i=1+2^{-i}\ (1\le i\le N),\quad
 A=2N+4.
\]
For coarse coordinates \(y_1,\ldots,y_k\) and fine coordinates
\(x_1,\ldots,x_N\), define the single linear score
\[
 s(y,x)=A\sum_{j=1}^k2^{j-1}y_j+T(x),
 \qquad T(x)=\sum_{i=1}^N a_i x_i.
\]
The coarse score takes distinct odd multiples of \(A\), spaced by
\(2A\). Its unique smallest positive value is \(A\), attained at
\[
 c^*=(-1,\ldots,-1,+1).
\]
The fine score lies in \([-R,R]\), where
\(R=N+1-q<A\), so the coarse score copies are disjoint. In particular,
the open interval \((0,2A)\) contains exactly the copy \(y=c^*\).

Let \(v\) have its first \(d\) fine coordinates \(+1\) and the
remaining \(d\) coordinates \(-1\). Its fine score is
\[
 t=T(v)=1-2^{1-d}+q.
\]
Every fine score is a distinct odd multiple of \(q\). To see
distinctness, the perturbation \(\sum_i2^{-i}x_i\) lies strictly between
\(-1\) and \(1\), so two different even integer values of
\(\sum_i x_i\) cannot agree after perturbation. Within a fixed integer
layer, binary subset sums are distinct. Equivalently, after multiplication
by \(2^N\), the final weight numerator is odd and all others are even,
so every score numerator is odd and the gap between distinct scores is
at least \(2q\). Consequently \((t-q,t+q)\) contains exactly \(v\),
and neither endpoint is attained. The point \(v\) is the unique
largest fine score in the central Hamming layer \(\sum_i x_i=0\).

Set \(a=A+t-q\) and \(b=A+t+q\). Define \(F:\mathbb R\to\{-1,1\}\)
by
\[
 F(u)=+1\quad\text{if }u<0,\ a<u<b,\ \text{or }u>2A,
 \qquad F(u)=-1\quad\text{otherwise}.
\]
Thus its four crossing points are \(0,a,b,2A\), with open-interval
labels \(+,-,+,-,+\). Their point labels are all \(-1\), each an
adjacent label. None of the four points is an attained score. They are
strictly ordered because \(-R<t-q<t+q<R\) and \(R<A\).

The resulting Boolean function is exactly
\[
 f(y,x)=F(s(y,x))
       =1-2\mathbf1\{y=c^*,\ x\ne v\}.
\tag{1}
\]
Its positive components are
\[
 E_1=\{y_k=-1\},\qquad
 E_2=\{y=c^*,x=v\},\qquad
 E_3=\{y_k=+1,y\ne c^*\}.
\]
Its negative components are
\[
 D_1=\{y=c^*,T(x)<t-q\},\qquad
 D_2=\{y=c^*,T(x)>t+q\}.
\]
The two outer positive components are nonempty because \(k\ge2\);
the middle one is a point. The all-minus and all-plus fine vertices
belong to \(D_1\) and \(D_2\), respectively. Thus no component can
be removed as empty, and adjacent attained components have opposite
labels.

## 2. Exact influence formulas

A point event in \(r\) coordinates has influence \(2r2^{-r}\).
For product events in disjoint coordinate blocks,
\[
 I(h_{U\times V})
 =\Pr(V)I(h_U)+\Pr(U)I(h_V),
\tag{2}
\]
by conditioning each coordinate flip on the other block. Equation (1)
therefore gives
\[
 \boxed{I(f)=2kp(1-q)+2pNq.}
\tag{3}
\]

For any increasing Boolean function \(h\), conditioning on all other
coordinates shows \(I_i(h)=\mathbb E[x_i h(x)]\). Hence
\(I(h)=\mathbb E[h(x)\sum_i x_i]\). A positive-weight threshold
whose boundary cuts the central Hamming layer is negative on
\(\sum_i x_i<0\) and positive on \(\sum_i x_i>0\), so its central
labels make no contribution to this identity. Its influence is exactly
\[
 M_N:=\mathbb E\left|\sum_{i=1}^N x_i\right|
     =\frac{N\binom N{N/2}}{2^N}.
\tag{4}
\]
For completeness, the last equality follows by summing the positive
layers and using
\((2r-N)\binom Nr=N[\binom{N-1}{r-1}-\binom{N-1}r]\);
the sum telescopes, and \(N\) is even.

Since \(0\le t-q<t+q<1\), both threshold boundaries cut only that central
layer: the perturbation magnitude is less than 1, while all noncentral
integer scores have magnitude at least 2. Thus both fine threshold
component indicators have influence \(M_N\). As their probabilities
sum to \(1-q\), applying (2) to \(D_1,D_2\) gives
\[
 \boxed{B_-(f):=I(h_{D_1})+I(h_{D_2})
              =2kp(1-q)+2pM_N.}
\tag{5}
\]

The first positive component has influence 1. The last one has influence
\(1+2(k-2)p\): the increasing sign function
\(2\mathbf1_{E_3}-1=-h_{E_3}\) is the highest-bit
dictator with the single value at \(c^*\) changed from \(+1\) to
\(-1\), so the same monotone identity gives
\[
 I(h_{E_3})=1-2p\sum_j c_j^*=1+2(k-2)p.
\]
The singleton \(E_2\) has influence \(2(k+N)pq\). Therefore
\[
 \boxed{B_+(f):=\sum_{j=1}^3I(h_{E_j})
              =2+2(k-2)p+2(k+N)pq.}
\tag{6}
\]

These formulas also verify the generic cancellation identities
\(B_\pm=I(f)+2J_\pm\), where \(J_\pm\) counts edges joining
different components with the same sign. The cancellations are essential.

## 3. A diverging ratio with four crossings

Take \(N=2^{2k}\). The elementary central-binomial lower bound
\[
 \frac{\binom{2d}d}{4^d}\ge\frac1{2\sqrt d}
\]
follows by induction: the ratio of successive left sides is
\((2d+1)/(2d+2)\), whose square is at least \(d/(d+1)\).
Consequently \(M_N\ge\sqrt{N/2}\), and (5) yields
\(B_-\ge\sqrt2\). Equation (6) gives \(B_+\ge2\).
Meanwhile \(Nq\le1\), so (3) gives
\(I(f)\le2p(k+1)\). Hence
\[
 \boxed{\frac{\min\{B_+(f),B_-(f)\}}{I(f)}
        \ge\frac{2^k}{\sqrt2(k+1)}\longrightarrow\infty.}
\tag{7}
\]
No universal \(D_4\) exists. The same class inclusion disproves such
a comparison for every bound \(m\ge4\). This argument does not decide
whether an appropriate comparison holds for at most three crossings.

## 4. The example is not an FEI counterexample

Here the entropy can be computed exactly. Put
\(e(u)=u\log_2(1/u)\), \(e(0)=0\). The empty coefficient is
\(1-2p(1-q)\). The \(2^k-1\) coefficients supported nontrivially
only in the coarse block have squared magnitude \(4p^2(1-q)^2\).
All coefficients with a nonempty fine support have squared magnitude
\(4p^2q^2\); their number is \(2^k(2^N-1)\). Thus
\[
 H(f)=e([1-2p(1-q)]^2)
 +(2^k-1)e(4p^2(1-q)^2)
 +2^k(2^N-1)e(4p^2q^2).
\tag{8}
\]
In particular, these functions satisfy \(H(f)<7I(f)\) uniformly.
To check this explicitly, write \(L_e=\log_2e\). The empty term is
at most \(4L_ep(1-q)\), using
\(e(1-V)\le L_eV\). The other two terms are
\[
\begin{aligned}
 &4p(1-p)(1-q)^2[2k-2-2\log_2(1-q)]\\
 &\qquad+4pq(1-q)[2k+2N-2].
\end{aligned}
\]
Their terms involving \(k,N\) sum to at most \(4I(f)\), because
\((1-p)(1-q)+q\le1\). The remaining logarithmic term is at most
\(8L_epq(1-q)\), using \(-\ln(1-q)\le q/(1-q)\).
Since \(q\le1/4\), the remainder together with the empty term is
at most \(6L_ep(1-q)\). Finally
\(I(f)\ge2kp(1-q)\ge4p(1-q)\), so
\[
 H(f)\le(4+\tfrac32\log_2e)I(f)<7I(f).
\]
The failure of the global component-influence comparison therefore
reflects entropy and boundary cancellations which that comparison loses.
