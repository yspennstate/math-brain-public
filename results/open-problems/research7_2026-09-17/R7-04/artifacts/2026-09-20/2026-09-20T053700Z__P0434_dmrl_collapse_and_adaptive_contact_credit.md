# P0434 / P01-A: DMRL collapse, a counterexample to the strengthened RC proof obligation, and the corrected contact-adaptive credit

## Scope

Outside source: Ziv Scully, Mor Harchol-Balter, and Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477.

This note is **PROVED PARTIAL** relative to Conjecture 8.1. It does not prove or refute the source conjecture. It does two things that matter for the current P01-A/P01-B proof architecture:

1. it proves an exact collapse theorem for the whole DMRL class: Gittins = M-SERPT = FCFS;
2. it proves that P01-B's strengthened residual-credit inequality `(RC)` is false even on a strict contact-collapsed source-admissible rank skeleton at high load, and identifies the weaker contact-adaptive inequality that survives the counterexample.

The newest paired P01-B report proved that all smooth/atomic tie-refinement charges in one M-SERPT valley are bounded in aggregate by the `D1+D3` part of that valley's exact Lemma-5.7 residence slack. The issue addressed here is how much of `D1+D3` may safely be discarded when there are *no* contacts to pay.

## 1. DMRL notation

Let

\[
S(a)=\Pr\{X>a\},\qquad
N(a)=\int_a^\infty S(t)\,dt,
\]

and define the mean residual life / SERPT rank

\[
m(a)=\frac{N(a)}{S(a)}
\]

whenever `S(a)>0`. Assume the source presentation regularity and finite mean. For the explicit slack formulas below also assume a finite second moment.

Call the law DMRL when `m(a)` is nonincreasing. If it is strictly decreasing on every positive-age interval with positive survival, call it strict DMRL.

## 2. The Gittins rank equals the mean residual life for DMRL laws

For a job of attained age `a`, the Gittins stopping candidate with endpoint `b>a` is

\[
R(a,b)
=
\frac{\mathbb E[\min\{X-a,b-a\}\mid X>a]}
{\Pr\{X\le b\mid X>a\}}
=
\frac{N(a)-N(b)}{S(a)-S(b)}.
\tag{2.1}
\]

Because the law is DMRL,

\[
\frac{N(b)}{S(b)}\le \frac{N(a)}{S(a)},
\]

so

\[
N(b)S(a)\le N(a)S(b).
\]

This is exactly equivalent to

\[
\frac{N(a)-N(b)}{S(a)-S(b)}
\ge \frac{N(a)}{S(a)}=m(a).
\tag{2.2}
\]

On the other hand, sending `b` to the right endpoint of the support (or to infinity) makes the candidate in `(2.1)` converge to `m(a)`. Hence

\[
\boxed{r_G(a)=m(a).}
\tag{2.3}
\]

This is an exact theorem, not an approximation.

## 3. DMRL collapse: Gittins = M-SERPT = FCFS

M-SERPT is the nondecreasing envelope of the SERPT rank, so

\[
r_{MS}(a)=\sup_{0\le u\le a}m(u).
\]

For DMRL laws, `m` is nonincreasing. Therefore

\[
\boxed{r_{MS}(a)=m(0)=\mathbb E X\quad\text{for all }a.}
\tag{3.1}
\]

With the source's FCFS tie-breaking convention, a constant M-SERPT rank is exactly FCFS.

Equation `(2.3)` says the Gittins rank itself is nonincreasing with age. Hence a job already in service never becomes worse than a fresh arrival; among jobs that have received different amounts of service, the oldest job has the smallest rank. Under FCFS ties this also implements FCFS. Consequently

\[
\boxed{
T_G=T_{MS}=T_{FCFS}\quad\text{sample-path-wise for every DMRL law.}
}
\tag{3.2}
\]

In particular the source factor-two inequality is true with ratio exactly one on this whole class.

For strict DMRL, the raw SERPT rank satisfies `m(a)<m(0)` for every positive finite age. Thus the M-SERPT envelope is one strict whole-line plateau with **no finite internal contact points**. This is a contact-collapsed skeleton in the sense relevant to the current P01-B reduction.

## 4. Evaluate P01-B's strengthened `(RC)` on the DMRL skeleton

Use the notation of P01-B's exact slack report:

\[
A(a)=1-\lambda\mathbb E[X\wedge a],\qquad
\tau(a)=\frac\lambda2\mathbb E[(X\wedge a)^2],
\]

\[
c(\rho)=\frac{2}{1+\sqrt{1-\rho}},\qquad
L(\rho)=\frac1\rho\log\frac1{1-\rho}.
\]

Let

\[
Q=\frac{\lambda\mathbb E[X^2]}{2(1-\rho)}
\]

be the FCFS mean waiting time.

### 4.1 M-SERPT credit `Xi`

There are no M-SERPT hills. The one whole-line valley has terminal survival zero, so its `D2` boundary term is zero. Therefore

\[
\boxed{\Xi=0.}
\tag{4.1}
\]

### 4.2 Gittins waiting surrogate and AM-GM credit

The Gittins rank is decreasing on the whole age line, so the source Proposition-4.7 lower surrogate consists of one whole-line valley and is exact:

\[
\boxed{\underline Q_G=Q.}
\tag{4.2}
\]

For this valley,

\[
s_V=1-\rho,\qquad
a_V=\frac{A(\infty)}{A(0)}=1-\rho,
\]

hence `c_V=c(rho)`. The square credit is

\[
\Omega_V
=Q\frac{a_V+s_V/a_V-2\sqrt{s_V}}{1-s_V}
=Q\frac{(1-\sqrt{1-\rho})^2}{\rho}.
\]

Since

\[
c(\rho)-1
=\frac{1-\sqrt{1-\rho}}{1+\sqrt{1-\rho}},
\]

we obtain the exact identity

\[
\boxed{\mathcal W=(c(\rho)-1)Q.}
\tag{4.3}
\]

### 4.3 `(RC)` fails above an explicit load

P01-B's strengthened sufficient inequality is

\[
\Xi+\mathcal W
\ge
(c(\rho)-1)\underline Q_G
+\left(\frac{L(\rho)}2-1\right)\mathbb E X.
\tag{RC}
\]

Substituting `(4.1)--(4.3)` cancels the entire waiting term and leaves

\[
0\ge\left(\frac{L(\rho)}2-1\right)\mathbb E X.
\tag{4.4}
\]

Therefore `(RC)` holds on DMRL laws iff `L(rho)<=2`, and it **fails** whenever

\[
\boxed{L(\rho)>2.}
\tag{4.5}
\]

Let `rho_c` be the unique nonzero root of

\[
-\log(1-\rho)=2\rho.
\tag{4.6}
\]

The derivative of the left-minus-right side is

\[
\frac1{1-\rho}-2,
\]

which is negative on `(0,1/2)`, positive on `(1/2,1)`, and the function tends to `+infinity` as `rho` tends to one. Hence `(4.6)` has exactly one positive root. Numerically only as a locator,

\[
\rho_c=0.7968121300200200461\ldots
\]

Thus every strict DMRL law at every stable load `rho>rho_c` is a source-valid **counterexample to `(RC)` as a universal proof obligation**, while still satisfying the actual M-SERPT/Gittins ratio exactly equal to one.

This directly refutes the plan "prove `(RC)` on the contact-collapsed skeleton" from the previous paired report. The failure is not caused by atomic contacts, rank ties, or four-point pathology.

## 5. Explicit strict source-class witness: mean-one Erlang-2

Take

\[
X\sim\mathrm{Erlang}(2,\text{rate }2).
\]

Then `E[X]=1`, `E[X^2]=3/2`, and

\[
S(a)=e^{-2a}(1+2a),\qquad
N(a)=e^{-2a}(1+a).
\]

Therefore

\[
m(a)=\frac{1+a}{1+2a},
\qquad
m'(a)=-\frac1{(1+2a)^2}<0.
\]

This is strict DMRL, so it has no finite M-SERPT internal contacts and both policies are exactly FCFS.

At

\[
\rho=\frac9{10},\qquad\lambda=\frac9{10},
\]

we have

\[
Q=\frac{(9/10)(3/2)}{2(1/10)}=\frac{27}{4},
\]

and

\[
L(9/10)=\frac{10}{9}\log 10.
\]

The amount by which `(RC)` fails is exactly

\[
\boxed{
\frac{L(9/10)}2-1
=\frac59\log 10-1
=0.27921394055\ldots>0.
}
\tag{5.1}
\]

Again, this is **not** a counterexample to Conjecture 8.1: here `T_MS/T_G=1` exactly.

## 6. Where the discarded credit went

For a DMRL law, the exact Lemma-5.7 residence slack is

\[
\mathcal S=Q_{MS}+L(\rho)\mathbb E X-R_{MS}.
\]

Because both policies are FCFS,

\[
Q_{MS}=Q,
\qquad
R_{MS}=\mathbb E X.
\]

Hence

\[
\boxed{
\mathcal S=Q+(L(\rho)-1)\mathbb E X.
}
\tag{6.1}
\]

In the P01-B valley decomposition this whole slack is

\[
D_1+D_3,
\]

with

\[
D_1=Q,\qquad D_3=(L(\rho)-1)\mathbb E X,\qquad D_2=0.
\tag{6.2}
\]

There are no internal contacts to pay. Thus `(RC)` fails precisely because it throws away **all** of the available `D1+D3` reserve even when the realized contact charge is zero.

## 7. Corrected proof target: contact-adaptive residual credit

Let `J_contact` denote the actual total tie/contact-refinement response cost that must be paid when lifting a contact-collapsed skeleton through the finite-support/quantization argument. The newest P01-B theorem gives

\[
J_{contact}\le\sum_V(D_{1,V}+D_{3,V}),
\tag{7.1}
\]

while

\[
\mathcal S
=2\Xi+\sum_V(D_{1,V}+D_{3,V}).
\tag{7.2}
\]

Therefore the credit that remains after paying the contacts is

\[
\mathcal S-J_{contact}
=2\Xi+
\left[\sum_V(D_{1,V}+D_{3,V})-J_{contact}\right]
\ge 2\Xi.
\]

The natural sufficient inequality is not `(RC)` but

\[
\boxed{
\mathcal S-J_{contact}+2\mathcal W
\ge
2(c(\rho)-1)\underline Q_G
+(L(\rho)-2)\mathbb E X.
}
\tag{CARC}
\]

Equivalently,

\[
\boxed{
\Xi+\mathcal W
+\frac12\left[
\sum_V(D_{1,V}+D_{3,V})-J_{contact}
\right]
\ge
(c(\rho)-1)\underline Q_G
+\left(\frac{L(\rho)}2-1\right)\mathbb E X.
}
\tag{7.3}
\]

This is the **contact-adaptive residual-credit inequality**. It preserves exactly the part of `D1+D3` that is not actually spent on contact refinements.

On a contact-collapsed skeleton, `J_contact=0`, so the correct target is the full-slack `(RC-exact)` inequality, not `(RC)`. On the DMRL class, `(CARC)` has the exact positive margin

\[
\boxed{\frac{Q+\mathbb E X}{2}=\frac{T_G}{2}.}
\tag{7.4}
\]

For the Erlang-2 witness at `rho=9/10`, this margin is

\[
\frac12\left(\frac{27}{4}+1\right)=\frac{31}{8}.
\]

## 8. Consequence for the paired proof architecture

The aggregate contact-payment theorem remains useful, but its correct interpretation is **adaptive**:

- reserve `J_contact`, the charge actually realized by contact refinements;
- do not discard the entire `D1+D3` budget preemptively;
- attack `(RC-exact)` on the contact-collapsed skeleton;
- when lifting contacts, subtract the proved aggregate charge and retain the leftover `D1+D3-J_contact` reserve.

The strict DMRL theorem shows that any proof architecture that permanently discards all `D1+D3` cannot close the high-load problem, even on a class where the actual scheduling conjecture is trivial with ratio one.

## 9. Status

- Full Conjecture 8.1: **OPEN / PARTIAL**; fixed source interval `[2,5]` unchanged.
- `<=3` positive support theorem: **PROVED PARTIAL**, inherited.
- Generic atomic contact theorem and finite sawtooth reduction: **PROVED PARTIAL**, inherited.
- Aggregate contact payment `J_contact<=sum(D1+D3)`: **PROVED PARTIAL**, paired P01-B result inherited.
- DMRL collapse `Gittins=M-SERPT=FCFS`: **PROVED PARTIAL** relative to source endpoint, new here.
- Strengthened `(RC)` on contact-collapsed skeleton: **REFUTED AS A UNIVERSAL PROOF OBLIGATION**, new here.
- Contact-adaptive residual-credit target `(CARC)`: **DERIVED SUFFICIENT TARGET**, new here; universal proof remains open.

The next useful finite-law attack should therefore study `(RC-exact)/(CARC)` on the smallest non-DMRL contact-collapsed four-point skeleton, rather than attempting to prove the now-refuted `(RC)` or generating another contact checker.
