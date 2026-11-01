Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: a full-dimensional open `S_3` neighborhood with complete sharp Lyons domination

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured master before this artifact: `6050bf81ce2cc302be6480283ceae45e902085f6`.  
Previous own checkpoint: `research7_2026-09-17/R7-03/runs/2026-09-20/2026-09-20T101000Z__report.md`.  
Status: **CANDIDATE FULL PROOF for the explicit open `S_3` source class below; PROVED PARTIAL relative to full C0036.**

## 1. Exact outside target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

The source fixes a sofic group `Gamma` and a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with canonical group trace

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

and Fuglede--Kadison determinant

\[
\operatorname{FK}_\Gamma(Q)=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

The conjecture asks for the sharp stochastic domination on every increasing event

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For a finite group of order `n`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\tag{1.2}
\]

The source states that Conjecture 5.7 is open even for finite groups. The bounded literature check used in the preceding C03 runs found no source-matching resolution as of 2026-09-20; this negative search is not treated as proof of worldwide openness.

## 2. Why this run changes method

The previous run found lower-dimensional `S_3` families carrying a hidden regular `C_6` symmetry. Those families solve the whole process only under exact algebraic symmetry constraints. The natural next question is whether this is merely a thin phenomenon or whether complete two-sided domination persists after breaking all of those symmetries.

Instead of another transverse Hessian calculation, this run uses a strict finite-event margin plus an explicit Lipschitz argument. The result is an actual **open ball in the full six-real-dimensional space of Hermitian `S_3` convolution kernels**. Thus both symmetry-breaking coordinates may be nonzero.

## 3. A rational interior base kernel

Write

\[
S_3=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle
\]

and order coordinates as

\[
e,r,r^2,s,rs,r^2s.
\]

Let `Q_*` be the convolution kernel determined by

\[
q_*(e)=\frac12,
\qquad q_*(r)=q_*(r^2)=\frac1{20},
\tag{3.1}
\]

\[
q_*(s)=q_*(r^2s)=\frac1{30},
\qquad q_*(rs)=-\frac1{60}.
\tag{3.2}
\]

In the displayed ordering,

\[
Q_*=\begin{pmatrix}
\frac12&\frac1{20}&\frac1{20}&\frac1{30}&-\frac1{60}&\frac1{30}\\
\frac1{20}&\frac12&\frac1{20}&\frac1{30}&\frac1{30}&-\frac1{60}\\
\frac1{20}&\frac1{20}&\frac12&-\frac1{60}&\frac1{30}&\frac1{30}\\
\frac1{30}&\frac1{30}&-\frac1{60}&\frac12&\frac1{20}&\frac1{20}\\
-\frac1{60}&\frac1{30}&\frac1{30}&\frac1{20}&\frac12&\frac1{20}\\
\frac1{30}&-\frac1{60}&\frac1{30}&\frac1{20}&\frac1{20}&\frac12
\end{pmatrix}.
\tag{3.3}
\]

Its exact spectrum is

\[
\left\{\frac25,\frac25,\frac12,\frac12,\frac{11}{20},\frac{13}{20}\right\}.
\tag{3.4}
\]

Hence `Q_*` is a strict interior positive contraction with spectral distance at least `7/20` from the upper boundary and `2/5` from the lower boundary. Its determinants are

\[
\det Q_*=\frac{143}{10000},
\qquad
\det(I-Q_*)=\frac{567}{40000}.
\tag{3.5}
\]

Set

\[
p_*:=\left(\frac{143}{10000}\right)^{1/6},
\qquad
r_*:=1-\left(\frac{567}{40000}\right)^{1/6}.
\tag{3.6}
\]

Numerically these are approximately `0.4926698735` and `0.5080505139`, but the proof below uses rational one-sided bounds, not floating-point sign decisions.

## 4. Reduction to 76 invariant upper sets

Both `P^Q` and the Bernoulli comparator are invariant under the left regular action of `S_3`. For any increasing function `f` on `2^{S_3}`, group averaging gives an invariant increasing function with the same expectation under both laws. Layer-cake decomposition then reduces stochastic domination to invariant increasing events.

Exact orbit enumeration gives 16 subset orbits and exactly

\[
\boxed{76}
\tag{4.1}
\]

invariant upper sets.

For any such event `U`, inclusion--exclusion gives

\[
\mathbf P^Q(U)=\sum_{T\subseteq S_3}c_U(T)\det Q_T,
\tag{4.2}
\]

where

\[
c_U(T)=\sum_{\substack{S\in U\\S\subseteq T}}(-1)^{|T|-|S|}.
\tag{4.3}
\]

The exact enumeration also gives the uniform coefficient bound

\[
\boxed{
W_U:=\sum_{T\subseteq S_3}|c_U(T)|\,|T|\le480
}
\tag{4.4}
\]

for every one of the 76 invariant upper sets.

## 5. Exact strict base margins

For the lower product comparator choose the rational number

\[
\bar p:=\frac{49267}{100000}.
\tag{5.1}
\]

Direct integer arithmetic gives

\[
\bar p^6-\det Q_*
=
\frac{22023812095993331568569}{10^{30}}>0,
\tag{5.2}
\]

so `p_*<bar p`. Since every upper event is increasing in the Bernoulli density,

\[
\mathbf P^{p_*I}(U)\le \mathbf P^{\bar p I}(U).
\]

The exact 76-event enumeration then gives, for every invariant upper set except the three structurally forced equality events `empty`, `whole space`, and `{S_3}`,

\[
\mathbf P^{Q_*}(U)-\mathbf P^{\bar p I}(U)
\ge
\delta_- ,
\tag{5.3}
\]

where the exact minimum is

\[
\boxed{
\delta_-=
\frac{509351537331256502398728569}
{200000000000000000000000000000}
>0.0025467.
}
\tag{5.4}
\]

Thus the true lower-comparator gap at `p_*` is at least `delta_-` on every non-forced event.

For the upper comparator choose

\[
\underline r:=\frac{50805}{100000}.
\tag{5.5}
\]

Then

\[
(1-\underline r)^6-\det(I-Q_*)
=
\frac{5685754240766244961}
{64000000000000000000000000}>0,
\tag{5.6}
\]

so `underline r<r_*`. Exact enumeration gives, for every invariant upper set except the three structurally forced equality events `empty`, `whole space`, and `nonempty`,

\[
\mathbf P^{\underline r I}(U)-\mathbf P^{Q_*}(U)
\ge
\delta_+,
\tag{5.7}
\]

with exact minimum

\[
\boxed{
\delta_+=
\frac{185372629975314782364961}
{64000000000000000000000000}
>0.0028964.
}
\tag{5.8}
\]

Therefore `Q_*` has a positive all-event margin away from only the identities that are forced by determinant sharpness.

## 6. A uniform perturbation bound for DPP event probabilities

Let `A,B` be `k x k` Hermitian positive contractions. Weyl's eigenvalue inequality allows their ordered eigenvalues to be paired so that

\[
|\lambda_j(A)-\lambda_j(B)|\le\|A-B\|_{\rm op}.
\]

Since all eigenvalues lie in `[0,1]`, telescoping the products gives

\[
|\det A-\det B|\le k\|A-B\|_{\rm op}.
\tag{6.1}
\]

If `Q` and `Q_*` are positive contractions and

\[
\|Q-Q_*\|_{\rm op}\le\varepsilon,
\tag{6.2}
\]

then every principal compression obeys the same operator-norm bound. Equations (4.2), (4.4), and (6.1) therefore imply

\[
\boxed{
|\mathbf P^Q(U)-\mathbf P^{Q_*}(U)|\le480\varepsilon
}
\tag{6.3}
\]

for every invariant upper set `U`.

## 7. The moving sharp product parameters are also Lipschitz

Assume `epsilon<=1/10`. Along the segment from `Q_*` to `Q`, (3.4) gives

\[
\lambda_{\min}\ge\frac25-\frac1{10}=\frac3{10}.
\]

For

\[
f(A)=(\det A)^{1/6}
\]

on positive definite `6 x 6` matrices,

\[
df_A(H)=\frac{f(A)}6\operatorname{Tr}(A^{-1}H).
\]

Because `f(A)<=1` for contractions,

\[
|df_A(H)|\le\frac1{\lambda_{\min}(A)}\|H\|_{\rm op}.
\]

Hence

\[
|p(Q)-p_*|\le\frac{10}{3}\varepsilon,
\qquad p(Q):=(\det Q)^{1/6}.
\tag{7.1}
\]

Likewise, `I-Q_*` has minimum eigenvalue `7/20`. Along the same segment and for `epsilon<=1/10`, its minimum eigenvalue is at least `1/4`. Therefore

\[
|r(Q)-r_*|\le4\varepsilon,
\qquad
r(Q):=1-(\det(I-Q))^{1/6}.
\tag{7.2}
\]

For six independent Bernoulli variables, the probability of any increasing event is `6`-Lipschitz in the common density: a standard monotone coupling, or Russo's formula with six influences each at most one, gives

\[
|\mathbf P^{tI}(U)-\mathbf P^{sI}(U)|\le6|t-s|.
\tag{7.3}
\]

Combining (7.1)--(7.3), the lower sharp-product comparator moves by at most `20 epsilon` and the upper comparator by at most `24 epsilon`.

## 8. An explicit six-dimensional open ball

Take

\[
\boxed{\varepsilon_*=4\times10^{-6}.}
\tag{8.1}
\]

Let `Q` be **any Hermitian `S_3`-equivariant operator** satisfying

\[
\boxed{
\|Q-Q_*\|_{\rm op}\le\varepsilon_*.
}
\tag{8.2}
\]

By (3.4) this automatically remains a strict positive contraction.

For every non-forced lower event, (5.4), (6.3), and (7.3) give

\[
\mathbf P^Q(U)-\mathbf P^{p(Q)I}(U)
\ge
\delta_- -(480+20)\varepsilon_*
>
0.0025467-0.002
>0.
\tag{8.3}
\]

The lower forced event `{S_3}` is always an identity because

\[
\mathbf P^Q(\{S_3\})=\det Q=p(Q)^6.
\tag{8.4}
\]

The empty event and whole sample space are trivial identities.

For every non-forced upper event,

\[
\mathbf P^{r(Q)I}(U)-\mathbf P^Q(U)
\ge
\delta_+-(480+24)\varepsilon_*
>
0.0028964-0.002016
>0.
\tag{8.5}
\]

The upper forced event `nonempty` is always an identity because

\[
\mathbf P^Q(X\ne\varnothing)
=1-\det(I-Q)
=1-(1-r(Q))^6.
\tag{8.6}
\]

Thus all 76 invariant upper sets satisfy both sharp inequalities. By the averaging reduction in Section 4, **every increasing event** does.

### Theorem 8.1 (open `S_3` neighborhood)

For every Hermitian `S_3`-equivariant `Q` satisfying (8.2),

\[
\boxed{
\operatorname{Ber}((\det Q)^{1/6})^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-(\det(I-Q))^{1/6}\right)^{\otimes S_3}.
}
\tag{8.7}
\]

Both constants are sharp by (8.4) and its empty-set dual.

This is a **full-dimensional open subset** of the full six-real-parameter space of Hermitian `S_3` convolution kernels. In particular, unlike the previous mean-zero, constant-coset, or hidden-`C_6` families, no exact equality among the six real Fourier/convolution parameters is imposed inside the ball. Small perturbations may simultaneously make `Im q(r) != 0`, make all three transposition coefficients distinct, and make their sum nonzero.

## 9. Why this is stronger than the previous structural faces

The prior exact families were lower-dimensional algebraic submanifolds. Theorem 8.1 proves that complete Lyons domination is not confined to those symmetry loci: it survives a certified amount of arbitrary `S_3`-equivariant symmetry breaking.

The proof also supplies a reusable principle for finite groups:

> If all non-forced invariant upper-event inequalities are strict at one interior equivariant kernel, then exact finite-event margins plus determinant/event Lipschitz bounds produce an explicit open neighborhood on which the full sharp stochastic domination persists.

This principle is independent of the particular symmetrization used to find the base point.

## 10. Honest status and remaining gap

- Full C0036 over all source-admissible sofic groups: **PROVED PARTIAL / unchanged**.
- Arbitrary `S_3`: **OPEN in this work**.
- The explicit operator-norm ball (8.2): **CANDIDATE FULL PROOF for the complete two-sided stochastic-domination statement**, supported by exact finite arithmetic and a self-contained perturbation argument.
- This theorem is not merely a necessary condition, a selected-event inequality, or another two-of-three orbit count: it proves the whole process inequality on a full-dimensional open class.

The exact finite enumeration is owner-track self-verification, not an independent audit.

## 11. Next attack

The open-ball theorem suggests replacing local Hessian calculations by a continuation argument. The next useful target is to characterize the connected component of the strict-domination region containing `Q_*`.

A concrete route is:

1. for each of the 73 non-forced lower invariant events and 73 non-forced upper invariant events, write the exact gap as a function on the six-real-dimensional `S_3` contraction body;
2. identify which gap first reaches zero when moving from `Q_*` toward a generic arbitrary `S_3` kernel;
3. prove that any first zero inside the positive-contraction interior is structurally forced (or derive the exact algebraic obstruction if not);
4. if interior first zeros are excluded, continuation from the present open ball to the whole connected contraction body would prove arbitrary `S_3`.

This attacks the global boundary of stochastic domination directly rather than repeating a symmetry-specific spectral expansion.