# P0434 / P01-A: exact atomic M-SERPT contact-jump theorem

## Scope and inherited state

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI `10.1145/3379477`.

This note is **PROVED PARTIAL** relative to Conjecture 8.1. It does not prove the arbitrary-law factor-two conjecture. The fixed full-source interval remains `[2,5]`.

Inherited R7-04 results used here:

1. factor two is proved for every law with at most three positive support points;
2. on an arbitrary finite-support terminal-stabilized open cell, outward motion of the last support point leaves `D=E[T_MS]-E[T_G]` constant and strictly increases `F=2E[T_G]-E[T_MS]`;
3. the stronger global tail-monotonicity route is false because an M-SERPT record contact can create a positive one-sided jump in `D`.

The paired P01-B report `probability_campaigns/progress_first_2026-09-20/P01/general/2026-09-20T041500Z__report.md` proves the continuous-density analogue of nonnegative rank-tie splitting and a one-sided reduction from the source presentation class to finite support. The purpose here is complementary: derive the **atomic finite-support contact jump exactly**, including the tie-sensitive term that appears under FCFS tie-breaking.

## 1. Notation

Let `X` be a positive finite-support service time with mean

\[
m=E[X],\qquad \rho=\lambda m<1.
\]

For `x>=0` write

\[
S(x)=P(X>x),\qquad N(x)=E[(X-x)^+],
\]

\[
m_x=E[X\wedge x],\qquad v_x=E[(X\wedge x)^2],\qquad A_x=1-\lambda m_x.
\]

Thus

\[
N(x)=m-m_x,
\qquad
m_y-m_x=\int_x^y S(t)\,dt,
\qquad
v_y-v_x=2\int_x^y tS(t)\,dt.
\]

The raw SERPT rank is `s(x)=N(x)/S(x)` whenever `S(x)>0`. M-SERPT is the nondecreasing record envelope of this rank.

## 2. Atomic plateau-contact configuration

Fix support ages

\[
0\le u<c<b.
\]

Assume that at the contact law:

1. the M-SERPT record level on `[u,b)` is a constant `L`;
2. `u` and `c` are raw SERPT contacts with that plateau,
   \[
   N(u)=L S(u),\qquad N(c)=L S(c);
   \]
3. there is no strict raw overtake before `b`, so
   \[
   N(x)\le L S(x)\qquad(c\le x<b);
   \]
4. at `b` the next record begins (or the support ends), so with the right-tail convention `S(b)=P(X>b)`,
   \[
   N(b)\ge L S(b).
   \]

The one-sided topology immediately after the contact keeps the rank ordering outside `[u,b)` fixed, keeps `[u,c)` at the old plateau, and makes `[c,b)` infinitesimally worse. A later record after `b` remains worse than both pieces. This is exactly the local topology change created when one affine M-SERPT candidate overtakes another while the Gittins topology itself stays fixed.

Define the affected masses and first moment

\[
p=P(u<X\le c),\qquad q=P(c<X\le b),
\]

\[
M=E[X\,1_{\{c<X\le b\}}].
\]

The two contact identities imply the useful exact relation

\[
\boxed{m_c-m_u=L p.}
\tag{2.1}
\]

Indeed,

\[
m_c-m_u=N(u)-N(c)=L(S(u)-S(c))=Lp.
\]

## 3. Exact one-sided SOAP jump

Let `T_0` be mean response under the unsplit plateau and `T_+` the right-sided mean response under the split topology, evaluated on the **same contact service law**. Put

\[
J:=T_+-T_0.
\]

Only jobs with sizes in `(u,b]` change their SOAP response.

### Jobs in `(u,c]`

Their worst future rank is still the lower plateau level. The new-work cutoff remains `u`; the old-work cutoff falls from `b` to `c`. Therefore their waiting term changes from

\[
W_0=\frac{\lambda v_b}{2A_bA_u}
\]

to

\[
W_c=\frac{\lambda v_c}{2A_cA_u},
\]

while their residence term is unchanged.

### Jobs in `(c,b]`

Their worst future rank becomes the upper split level. Their old-work cutoff remains `b`, but their new-work cutoff changes from `u` to `c`. Thus their waiting term changes from `W_0` to

\[
W_1=\frac{\lambda v_b}{2A_bA_c},
\]

and their residence changes from `x/A_u` to `x/A_c`.

Jobs of size at most `u` and greater than `b` have the same worst-future ordering on both sides of the contact, hence are unchanged.

Averaging gives the first exact formula

\[
\boxed{
J
=p\left(\frac{\lambda v_c}{2A_cA_u}-\frac{\lambda v_b}{2A_bA_u}\right)
+q\left(\frac{\lambda v_b}{2A_bA_c}-\frac{\lambda v_b}{2A_bA_u}\right)
+M\left(\frac1{A_c}-\frac1{A_u}\right).
}
\tag{3.1}
\]

Using `(2.1)`, this collapses to a single load-affine numerator:

\[
\boxed{
J=\frac{\lambda p}{2A_uA_cA_b}\,H_\lambda,
}
\tag{3.2}
\]

where

\[
\boxed{
H_\lambda
=A_b\bigl(v_c+2LM\bigr)
-v_b\bigl(A_c-\lambda Lq\bigr).
}
\tag{3.3}
\]

Because `A_b` and `A_c` are affine in `lambda`, `H_lambda` is itself affine in `lambda`.

This is the exact finite-support contact charge that was missing from the preceding R7-04 report. It depends only on the three cut ages `u,c,b`, the plateau level `L`, and truncated moments/masses; no Gittins quantity appears in the jump itself.

## 4. New sign theorem: every such atomic plateau split is nonnegative

### Theorem 4.1

Under the assumptions of Section 2, for every stable load,

\[
\boxed{J\ge0.}
\tag{4.1}
\]

Thus the downward jump of factor-two slack seen in the previous exact four-point example is not an accident: an atomic M-SERPT plateau refinement of this type can only increase, never decrease, M-SERPT mean response.

### Proof

Since the denominator in `(3.2)` is positive under stability, it is enough to prove `H_lambda>=0` for `0<=lambda<1/m`.

Because `H_lambda` is affine in `lambda`, it suffices to check the two endpoints `lambda=0` and `lambda=1/m` (the latter is an algebraic boundary value, not a stable queue).

#### Endpoint 1: zero load

At `lambda=0`,

\[
H_0=v_c+2LM-v_b.
\tag{4.2}
\]

Using `v_b-v_c=2\int_c^b xS(x)dx` and the identity

\[
M=c\,[S(c)-S(b)]
+\int_c^b [S(x)-S(b)]dx,
\]

a direct integration-by-parts rearrangement gives

\[
\boxed{
\frac{H_0}{2}
=\int_c^b \bigl(LS(x)-N(x)\bigr)dx
+b\bigl(N(b)-LS(b)\bigr).
}
\tag{4.3}
\]

Both terms are nonnegative by the plateau and next-record assumptions. Hence

\[
H_0\ge0.
\tag{4.4}
\]

#### Endpoint 2: the stability boundary

At `lambda=1/m`,

\[
A_b=\frac{N(b)}m.
\]

Also, since `N(c)=LS(c)` and `q=S(c)-S(b)`,

\[
A_c-\frac{Lq}{m}
=\frac{LS(b)}m.
\]

Therefore

\[
m H_{1/m}
=N(b)(v_c+2LM)-v_bLS(b).
\]

Insert `H_0=v_c+2LM-v_b` to obtain the manifestly nonnegative decomposition

\[
\boxed{
m H_{1/m}
=N(b)H_0+v_b\bigl(N(b)-LS(b)\bigr)\ge0.
}
\tag{4.5}
\]

Since an affine function nonnegative at both endpoints of `[0,1/m]` is nonnegative throughout the interval,

\[
H_\lambda\ge0\qquad(0\le\lambda\le1/m).
\]

Equation `(3.2)` now gives `J>=0` for every stable load. `square`

### Structural interpretation

The numerator test is unexpectedly simple: **the sign of an atomic M-SERPT topology jump is a two-endpoint problem in load**. The zero-load endpoint is paid by the integrated SERPT deficit inside the plateau plus the next-record overshoot; the critical-load endpoint is then automatically paid by the same two nonnegative quantities.

This is the discrete/atomic counterpart of P01-B's continuous-density tie-split theorem, but it is not merely a restatement: atoms produce the extra boundary overshoot term

\[
b\,[N(b)-LS(b)],
\]

which is exactly what is absent from a smooth valley ending at another same-level contact.

## 5. Exact factor-two contact obligation

Suppose, in addition, that the Gittins rank topology and `E[T_G]` are continuous through this M-SERPT-only contact. Let

\[
F^-:=2E[T_G]-E[T_{MS}]\quad\text{at the tied contact},
\]

and `F^+` denote the right-sided value. Then

\[
\boxed{F^+=F^- -J.}
\tag{5.1}
\]

Consequently the abstract contact condition from the preceding report is equivalent here to the explicit local truncated-moment inequality

\[
\boxed{
F^-
\ge
\frac{\lambda p}{2A_uA_cA_b}
\left[
A_b(v_c+2LM)-v_b(A_c-\lambda Lq)
\right].
}
\tag{5.2}
\]

This is the useful handoff to the arbitrary-law/prefix-credit line: the jump that must be paid is now an exact local object. A future global proof does **not** need to control arbitrary behavior at an atomic contact; it needs to show that the pre-contact Gittins/source slack dominates the explicit charge `(5.2)`, possibly after summing charges over a record chain.

## 6. Exact four-point checks

### Previous obstruction

For

\[
X\in\left\{1,\frac52,\frac72,\frac{17}2\right\},
\qquad
P=\left(\frac13,\frac1{12},\frac12,\frac1{12}\right),
\qquad
\lambda=\frac1{10},
\]

the contact is

\[
u=0,\qquad c=1,\qquad b=\frac72,\qquad L=3.
\]

The local quantities are

\[
m_c=1,\quad m_b=\frac{31}{12},\quad
v_c=1,\quad v_b=8,
\]

\[
p=\frac13,\quad q=\frac7{12},\quad M=\frac{47}{24}.
\]

Formula `(3.2)` gives

\[
\boxed{J=\frac{65}{712},}
\]

exactly matching the independently evaluated one-sided drop in factor-two slack from the previous R7-04 checker.

### Independent second contact family

Take masses

\[
\left(\frac8{23},\frac7{23},\frac6{23},\frac2{23}\right)
\]

on support

\[
\left\{1,\frac52,3,\frac{181}{16}\right\}.
\]

The first two SERPT record candidates tie at

\[
L=\frac{23}{8},
\]

while the third candidate is `165/64<L` and the terminal candidate is `133/16>L`. At load `rho=1/3`, hence `lambda=8/69`, the exact formula gives

\[
\boxed{J=\frac{62092}{556991}.}
\]

A direct exact SOAP evaluation of the contact topology and a post-contact point in the same stabilized cell gives the same difference in `E[T_MS]-E[T_G]`.

## 7. What this solves and what remains

Solved this run:

- the one-sided **atomic** M-SERPT plateau-contact jump is derived exactly;
- its sign is proved nonnegative at every stable load by a two-endpoint affine argument;
- the previous four-point jump `65/712` is explained by a general theorem rather than an isolated computation;
- the remaining factor-two contact obligation is reduced to the explicit local inequality `(5.2)`.

Still open:

- `(5.2)` has not been proved from the available global Gittins/prefix credits;
- therefore finite-support factor two beyond the already proved three-support theorem is not yet closed;
- Conjecture 8.1 remains open in full source scope.

The next attack should combine `(5.2)` with P01-B's exact residence/waiting credits `Xi` and `W` and its continuous tie-split charge. The concrete target is to dominate a sum of atomic `H_lambda` charges along one M-SERPT record chain by a single prefix-credit account, rather than trying to force each contact to be harmless pointwise.
