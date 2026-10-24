Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum is the owner's requested preference, not authenticated runtime telemetry here.

# P0434 / P01-A: factor two for every finite law with at most one strict M-SERPT record jump

## Scope

Outside source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI `10.1145/3379477`.

This note is **PROVED PARTIAL** relative to Conjecture 8.1. It does not prove the arbitrary-law conjecture. The source's presentation assumes a continuous density for convenience, while explicitly saying its results were confirmed for discrete job-size laws; the present statement is deliberately a finite-support theorem.

Inherited source facts used here are Lemma 5.3 (every Gittins hill age is an M-SERPT hill age), Proposition 4.7 (the SOAP waiting lower bound, with equality for monotonic rank), and Proposition 4.9 (`E[R] >= E[X]`). Write

\[
A(a)=1-\lambda E[X\wedge a],\qquad
\tau(a)=\frac{\lambda}{2}E[(X\wedge a)^2].
\]

## 1. Finite-law one-record hypothesis

Let `X` have positive finite support and

\[
\mu=E[X],\qquad \rho=\lambda\mu<1.
\]

Write

\[
S(a)=P(X>a),\qquad N(a)=E[(X-a)^+],\qquad r_S(a)=\frac{N(a)}{S(a)}
\]

when `S(a)>0`.

Assume the increasing envelope of `r_S`, namely the M-SERPT rank, has exactly one strict internal record jump, at age `b`. Equivalently,

\[
r_S(a)\le \mu\quad(a<b),
\]

\[
L:=r_S(b)>\mu,
\]

and

\[
r_S(c)\le L\quad(c>b)
\]

until the support endpoint. Thus M-SERPT has two plateau levels. The zero-record case is the FCFS-neutral boundary and is not the substantive case below.

Set

\[
r=P(X>b),\qquad p=1-r,
\]

\[
m=E[X\wedge b],\qquad B=E[X1_{\{X>b\}}],
\]

\[
V_b=E[(X\wedge b)^2],\qquad V=E[X^2],
\]

and

\[
A=1-\lambda m,\qquad \alpha=1-\rho.
\]

## 2. Hill-alignment lemma: the unique M-SERPT record is necessarily a Gittins hill

The source gives one direction: every Gittins hill is an M-SERPT hill. In the present topology the converse holds for the unique strict record.

For a finite law, a Gittins stopping candidate from age `a` to a later support age `c` is the integrated-tail chord

\[
R(a,c)=\frac{N(a)-N(c)}{S(a)-S(c)},
\]

with `c=infinity` giving the SERPT candidate `N(a)/S(a)`. Hence

\[
r_G(a)\le r_S(a).
\]

For `a<b`,

\[
r_G(a)\le r_S(a)\le \mu. \tag{2.1}
\]

At `b`, define

\[
D_\mu(x)=N(x)-\mu S(x).
\]

Because `r_S(b)=L>mu`,

\[
D_\mu(b)=S(b)(L-\mu)>0.
\]

For any valid stopping endpoint `c>b`, the one-record hypothesis gives `r_S(c)<=L`. If `S(c)<S(b)`, then

\[
D_\mu(c)=S(c)(r_S(c)-\mu)\le S(c)(L-\mu)<S(b)(L-\mu)=D_\mu(b).
\]

Therefore

\[
N(b)-N(c)>\mu[S(b)-S(c)],
\]

so every genuine chord satisfies

\[
R(b,c)>\mu. \tag{2.2}
\]

Endpoints with `S(c)=S(b)` have zero completion probability and are not genuine stopping candidates; the `c=infinity` candidate is `L>mu`. Thus

\[
\boxed{r_G(b)>\mu.} \tag{2.3}
\]

Combining (2.1) and (2.3), `b` is a strict Gittins hill. Source Lemma 5.3 rules out any other internal Gittins hill because there is no other M-SERPT hill. Hence the Gittins and M-SERPT hill boundaries are the same two-block partition:

\[
(0,b]\quad\text{and}\quad(b,\infty). \tag{2.4}
\]

Gittins may still have a nonconstant raw rank inside either valley; only the hill endpoints are being identified.

## 3. Exact M-SERPT response formulas and a pointwise Gittins waiting comparison

Because M-SERPT has monotonic rank, Propositions 4.7 and 4.8 are equalities.

For a job with `x<=b`,

\[
y(x)=0,\qquad z(x)=b,
\]

so

\[
Q_{MS}(x)=\frac{\tau(b)}A,\qquad R_{MS}(x)=x.
\]

For a job with `x>b`,

\[
y(x)=b,\qquad z(x)=\infty,
\]

so

\[
Q_{MS}(x)=\frac{\tau(\infty)}{A\alpha},\qquad R_{MS}(x)=\frac{x}{A}.
\]

Averaging gives

\[
\boxed{
Q_{MS}=\frac{\lambda}{2A}\left(pV_b+\frac{rV}{\alpha}\right)
} \tag{3.1}
\]

and

\[
\boxed{
R_{MS}=E[X1_{\{X\le b\}}]+\frac BA
=\mu+\frac{\lambda mB}{A}.
} \tag{3.2}
\]

By the hill-alignment lemma, Gittins has the same `y,z` endpoints for every size. Proposition 4.7 therefore gives pointwise

\[
Q_G(x)\ge Q_{MS}(x),
\]

and hence

\[
\boxed{Q_G\ge Q_{MS}.} \tag{3.3}
\]

Proposition 4.9 gives

\[
\boxed{R_G\ge\mu.} \tag{3.4}
\]

Thus it is enough to prove `Q_MS+2mu-R_MS>0`.

## 4. Two-block response-slack inequality

### Theorem 4.1

For every stable load under the one-record hypothesis,

\[
\boxed{
Q_{MS}+2\mu-R_{MS}
\ge
\frac{\mu(1-\rho)(1-\rho/2)}A
>0.
} \tag{4.1}
\]

### Proof

Multiply the left side by `A>0`. From (3.1)-(3.2),

\[
\begin{aligned}
K&:=A(Q_{MS}+2\mu-R_{MS})\\
&=\mu-\lambda m(\mu+B)
+\frac\lambda2\left(pV_b+\frac{rV}{\alpha}\right).
\end{aligned} \tag{4.2}
\]

Use

\[
m\le\mu,\qquad B\le\mu,\qquad pV_b\ge0. \tag{4.3}
\]

By Cauchy-Schwarz on the tail event `{X>b}`,

\[
B^2=E[X1_{\{X>b\}}]^2
\le rE[X^2 1_{\{X>b\}}]\le rV. \tag{4.4}
\]

Therefore

\[
K\ge \mu-\lambda\mu(\mu+B)+\frac{\lambda B^2}{2\alpha}. \tag{4.5}
\]

Put

\[
y=B/\mu\in[0,1],\qquad \rho=\lambda\mu.
\]

Then

\[
\frac K\mu
\ge
1-\rho(1+y)+\frac{\rho y^2}{2(1-\rho)}. \tag{4.6}
\]

The right side has the exact completed-square form

\[
\boxed{
1-\rho(1+y)+\frac{\rho y^2}{2(1-\rho)}
=(1-\rho)(1-\rho/2)
+\frac{\rho}{2(1-\rho)}(y-(1-\rho))^2.
} \tag{4.7}
\]

Hence `K>=mu(1-rho)(1-rho/2)`, which after division by `A` proves (4.1). QED.

The proof uses no optimization over the detailed support below `b`: all of that geometry is discarded through `m<=mu`, while the entire tail is paid by the single second-moment Cauchy charge (4.4).

## 5. Factor-two consequence

Using (3.3), (3.4), and (4.1),

\[
\begin{aligned}
2T_G-T_{MS}
&=2(Q_G+R_G)-(Q_{MS}+R_{MS})\\
&\ge Q_{MS}+2\mu-R_{MS}\\
&\ge \frac{\mu(1-\rho)(1-\rho/2)}A>0.
\end{aligned}
\]

Therefore

\[
\boxed{E[T_{MS}]<2E[T_G]} \tag{5.1}
\]

for every stable load and every positive finite-support law whose M-SERPT envelope has at most one strict internal record jump.

The no-strict-record boundary is FCFS-neutral and also satisfies the conclusion. Thus a finite-support counterexample to Conjecture 8.1, if one exists, must have **at least two strict internal M-SERPT record jumps**.

Combined with the inherited theorem for at most three positive support points, any finite-support counterexample must simultaneously have

1. at least four positive support points; and
2. at least two strict internal M-SERPT record jumps.

This is a topology restriction, not merely a support-cardinality restriction.

## 6. Exact high-load four-point check

Take

\[
X\in\{1,2,3,5\}
\]

with masses

\[
(3/5,3/10,9/100,1/100).
\]

The successive raw SERPT record candidates are

\[
38/25,\quad 13/10,\quad 6/5,\quad 2,
\]

so the only strict M-SERPT record jump is at `b=3`. The exact finite-law Gittins lower-envelope calculation likewise has its only strict internal record at age 3.

At

\[
\rho=19/20,\qquad \lambda=5/8,
\]

we have

\[
\mu=38/25,\qquad m=3/2,\qquad A=1/16,
\]

and (3.1)-(3.2) give

\[
Q_{MS}=649/40,\qquad R_{MS}=227/100.
\]

Thus

\[
Q_{MS}+2\mu-R_{MS}=3399/200,
\]

while the universal lower bound in (4.1) is

\[
399/625>0.
\]

This is deliberately a high-load non-DMRL four-point check, not evidence in place of the proof.

## 7. Handoff to P01-B and next structural target

P01-B's newest report preserves the exact valley-by-valley waiting-excess coefficient

\[
\eta_V=\frac{(1-a_V)(a_V-g_V)}{a_V(1-g_V)}
\]

and the master reduction based on `Q_MS <= Qbar_G + E_loc`.

The theorem above shows that when the M-SERPT record chain has at most two blocks, there is no waiting-excess problem at the Proposition-4.7 surrogate level:

\[
\boxed{\underline Q_G=Q_{MS}.}
\]

The only required charge is the explicit response slack (4.1), paid by one terminal second-moment Cauchy term.

The next genuinely new finite-law topology is therefore **two strict internal M-SERPT record jumps**, i.e. three M-SERPT blocks. The concrete question is whether the proof of (4.1) can be iterated as a prefix/tail Cauchy charge. A natural candidate is

\[
R_{MS}-2\mu\stackrel{?}{\le}Q_{MS},
\]

but this is not claimed here. If it is too strong globally, the fallback is to charge the first-block deficit to the next block while leaving exactly P01-B's local `eta_V Qbar_{G,V}` penalty for the remaining prefix.

A proof for arbitrary record-chain length would be a structural bridge to the arbitrary-law program. A counterexample already at three blocks would identify the minimal topology that must be handled by P01-B's chord-defect credit.

## 8. Exact self-check

Executed checker:
`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T064300Z__P0434_one_record_checker.py`

Archived output:
`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T064300Z__P0434_one_record_checker.out`

The checker verifies the completed-square identity exactly, the four-point M-SERPT record candidates, the exact Gittins record age, the high-load rational response formulas, and the tail Cauchy inequality. It terminates with `ALL_EXACT_CHECKS_PASS`.

No claim is made that this self-check is an independent audit.
