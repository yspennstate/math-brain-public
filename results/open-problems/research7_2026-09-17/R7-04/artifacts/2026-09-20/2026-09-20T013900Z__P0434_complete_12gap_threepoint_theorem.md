Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum is the owner's requested preference, not authenticated runtime telemetry here.

# P0434 / P01-A — complete arbitrary-mass `{1,2,2+d}` three-point family

## Source and scope

Outside source: Ziv Scully, Mor Harchol-Balter and Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477.

The source asks whether M-SERPT has mean response time at most twice that of Gittins for every source-admissible service distribution at every stable load. The published universal upper bound is 5 and the lower-bound construction approaches 2. This artifact proves the factor-two inequality for the **entire normalized three-point family**

\[
X\in\{1,2,2+d\},\qquad
P(X=1)=p,\quad P(X=2)=q,\quad P(X=2+d)=r,
\]

with arbitrary `p,q,r>0`, `p+q+r=1`, arbitrary `d>0`, and every stable load. It is a **PROVED PARTIAL** theorem relative to Conjecture 8.1: it is not yet the arbitrary-three-point theorem, because a general three-point support cannot in general be scaled so that its first two support points are exactly `1,2`.

The exact mean-response calculations use the SOAP theorem of Scully--Harchol-Balter--Scheller-Wolf (2018), including FCFS tie-breaking at equal rank. Earlier R7-04 reports already proved the far-tail cells. The new mathematics below closes every remaining cell and stitches the partition.

## 1. Parameters and exact thresholds

Write

\[
t=q+r=1-p,\qquad \mu=1+t=2-p,
\qquad m=E[X]=\mu+rd,
\]

and define

\[
d_0=\frac{t^2}{pr},\qquad
h_0=\frac1p,\qquad
h=\frac{\mu}{1-r},\qquad
 d_1=\frac tq.
\]

The exact ordering identities are

\[
d_0-h_0=\frac{t^2-r}{pr},
\]

\[
h-d_1=\frac{t^2-r}{q(1-r)},
\]

\[
d_0-h=\frac{t^2-r}{pr(1-r)},
\]

and

\[
h-h_0=\frac{r-t^2}{p(1-r)}.
\]

Thus there are only two mass regimes:

\[
r\le t^2:\qquad d_1\le h\le d_0,
\]

and

\[
r>t^2:\qquad d_0<h_0<d_1.
\]

The previously proved R7-04 cells are:

- `r<=t^2`, `d>d_0`: the one-Gittins-hill unequal-mass theorem;
- `r>t^2`, `d>d_1`: the two-Gittins-hill unequal-mass theorem.

This artifact proves the complementary regions.

## 2. The internal-switch wedge `r>t^2`, `d_0<d<=d_1`

This is the main previously unresolved topology.

### 2.1 Exact M-SERPT rank

The raw SERPT values on the three age intervals are

\[
m=1+t+rd,
\qquad
H=1+\frac{rd}{t},
\qquad
d.
\]

Because `d>d_0`,

\[
H-m=\frac{prd-t^2}{t}>0.
\]

Because `d<=d_1=t/q`,

\[
d-H=\frac{qd-t}{t}\le0.
\]

M-SERPT is the increasing envelope of SERPT, so its exact rank is therefore

\[
\boxed{
r_M(a)=
\begin{cases}
m,&0\le a<1,\\
H,&1\le a<2+d.
\end{cases}}
\tag{2.1}
\]

There is one M-SERPT demotion at age 1 and no second demotion at age 2.

### 2.2 Exact Gittins rank and its internal switch

Before age 1, `r>t^2` and `d>d_0` force the first-stop candidate to be the Gittins lower envelope, so

\[
r_G(a)=\frac{1-a}{p},\qquad 0\le a<1.
\]

On `[1,2)`, the two stopping candidates are

\[
B_1(a)=\frac{t(2-a)}q,
\qquad
B_2(a)=(2-a)+\frac{rd}{t}.
\]

They cross at

\[
\boxed{a_*=2-\frac{qd}{t}.}
\tag{2.2}
\]

Because `d<=t/q`, this lies in `[1,2)`. The lower envelope starts on `B_2` and then switches to `B_1`. At the crossing both candidates equal `d`. Hence

\[
\boxed{
r_G(a)=
\begin{cases}
(1-a)/p,&0\le a<1,\\
(2-a)+rd/t,&1\le a<a_*,\\
t(2-a)/q,&a_*\le a<2,\\
2+d-a,&2\le a<2+d.
\end{cases}}
\tag{2.3}
\]

The age-one hill has height `H`; the age-two terminal hill has height `d<=H`. This is the topology that was not covered by the earlier far-tail cancellation theorem.

### 2.3 Exact M-SERPT response formulas

Let

\[
\alpha=1-\lambda,
\qquad \rho=\lambda m<1,
\qquad
M_2=E[X^2]=p+4q+r(2+d)^2,
\]

and

\[
W_H=\frac{\lambda M_2}{2(1-\rho)\alpha}.
\]

SOAP gives

\[
\boxed{T_M(1)=1+\frac{\lambda}{2\alpha},}
\tag{2.4}
\]

\[
\boxed{T_M(2)=W_H+\frac2\alpha,}
\tag{2.5}
\]

\[
\boxed{T_M(2+d)=W_H+\frac{2+d}{\alpha}.}
\tag{2.6}
\]

At worst-future rank `H`, all old work is admitted, while a new job contributes exactly its first unit before the age-one jump.

### 2.4 Exact Gittins formulas: fresh-rank contact splits the wedge

Put

\[
h_0=1/p,
\qquad
\ell=\frac{q}{pt},
\qquad
z=\frac{qd}{t},
\qquad
\ell_0=h_0-\frac{rd}{t}.
\]

The old-work geometry at the fresh threshold `h_0` changes only when the terminal hill crosses `h_0`. Thus split at `d=h_0`.

#### Lower wedge: `d<h_0`

The Gittins path crosses `h_0` on the `B_2` segment. The size-2 recycled interval has length `ell_0`; a long job's corresponding old-work interval continues through the age-two jump and has total length

\[
\ell_0+d=h_0+z.
\]

Hence

\[
C_{0,L}=1+q\ell_0^2+r(h_0+z)^2,
\]

and the exact conditional response times are

\[
\boxed{T_G(1)=1+\frac{\lambda C_{0,L}}{2\alpha},}
\tag{2.7}
\]

\[
\boxed{T_G(2)=W_H+\frac{2-\ell_0}{\alpha}+\ell_0,}
\tag{2.8}
\]

\[
\boxed{T_G(2+d)=W_H+\frac{2-\ell_0}{\alpha}+d+\ell_0.}
\tag{2.9}
\]

#### Upper wedge: `d>h_0`

The post-age-one path instead crosses `h_0` on `B_1`, and the terminal hill stays above the fresh threshold. Define

\[
C_{0,U}=1+t\ell^2+r h_0^2.
\]

Then

\[
\boxed{T_G(1)=1+\frac{\lambda C_{0,U}}{2\alpha},}
\tag{2.10}
\]

\[
\boxed{T_G(2)=W_H+\frac{2-\ell}{\alpha}+\ell,}
\tag{2.11}
\]

\[
\boxed{T_G(2+d)=W_H+\frac{2+d-h_0}{\alpha}+h_0.}
\tag{2.12}
\]

The formulas on the two sides have the same continuous policy-gap limit at `d=h_0`.

### 2.5 New prefix-charge identity

Let

\[
D=E[T_M]-E[T_G].
\]

Exact averaging and simplification of `(2.4)--(2.12)` gives, in the lower wedge,

\[
\boxed{
D_L=
\frac{\lambda\bigl(t^2-p^2qrd^2\bigr)}
{2tp(1-\lambda)}.
}
\tag{2.13}
\]

In the upper wedge,

\[
\boxed{
D_U=
\frac{\lambda\bigl(t^2-qr\bigr)}
{2tp(1-\lambda)}.
}
\tag{2.14}
\]

At `d=h_0=1/p`, `(2.13)` and `(2.14)` agree exactly. Therefore the whole wedge can be written compactly as the **saturated prefix charge**

\[
\boxed{
D=
\frac{\lambda}
{2tp(1-\lambda)}
\left[
 t^2-qr\min\{(pd)^2,1\}
\right].
}
\tag{2.15}
\]

This is the main transferable lemma of the run. The M-SERPT penalty decreases as the terminal atom moves outward until terminal/fresh Gittins contact, and is then exactly invariant. Local per-valley nonnegativity is not needed; the charge is a cross-valley prefix quantity.

### 2.6 Uniform `<3/2` ratio on the entire wedge

Both numerators in `(2.13)--(2.14)` are positive and strictly below `t^2`. Hence

\[
0<D<\frac{\lambda t}{2p(1-\lambda)}.
\tag{2.16}
\]

The first-demotion condition `d>d_0=t^2/(pr)` implies

\[
m-1=t+rd
>t+\frac{t^2}{p}
=\frac tp.
\tag{2.17}
\]

Stability `\lambda m<1` gives

\[
\frac{\lambda}{1-\lambda}<\frac1{m-1}<\frac pt.
\tag{2.18}
\]

Combining `(2.16)--(2.18)`,

\[
\boxed{0<D<\frac12.}
\tag{2.19}
\]

For every work-conserving policy, in particular Gittins,

\[
E[T_G]\ge E[X]=m>1.
\]

Therefore

\[
\boxed{
\frac{E[T_M]}{E[T_G]}
=1+\frac D{E[T_G]}
<\frac32<2
}
\tag{2.20}
\]

for every stable load throughout the full internal-switch wedge.

## 3. The missing `r<=t^2` middle cell

Assume now

\[
r\le t^2,
\qquad
h<d\le d_0,
\qquad h=\frac{\mu}{1-r}.
\tag{3.1}
\]

Here M-SERPT remains at its fresh rank through age 2 and has only a terminal demotion; Gittins has no genuine age-one hill and one terminal hill.

Let

\[
\beta=1-\lambda\mu,
\qquad
V=E[\min\{X,2\}^2]=1+3t,
\]

\[
W_\infty=
\frac{\lambda M_2}{2(1-\rho)\beta},
\qquad
W_h=
\frac{\lambda(V+r h^2)}{2\beta}.
\]

The exact M-SERPT formulas are

\[
T_M(1)=1+\frac{\lambda V}{2\beta},
\qquad
T_M(2)=2+\frac{\lambda V}{2\beta},
\]

\[
T_M(2+d)=W_\infty+\frac{2+d}{\beta}.
\tag{3.2}
\]

The exact Gittins formulas are

\[
T_G(1)=1+W_h,
\qquad
T_G(2)=2+W_h,
\]

\[
T_G(2+d)=W_\infty+\frac{2+d-h}{\beta}+h.
\tag{3.3}
\]

Averaging gives the second new exact identity

\[
\boxed{
D=E[T_M]-E[T_G]
=
\frac{\lambda r\mu^2}
{2(1-r)(1-\lambda\mu)}.
}
\tag{3.4}
\]

The far support location again cancels completely from the additive policy gap inside this topology.

Stability gives `\lambda<1/m`; because `\lambda/(1-\lambda\mu)` is increasing,

\[
\frac{\lambda}{1-\lambda\mu}
<\frac1{m-\mu}
=\frac1{rd}.
\]

Therefore

\[
D<\frac{\mu^2}{2(1-r)d}.
\]

Since `d>h=\mu/(1-r)`,

\[
\boxed{D<\frac\mu2.}
\tag{3.5}
\]

But `E[T_G]>=m>\mu`; hence

\[
\boxed{
\frac{E[T_M]}{E[T_G]}<\frac32<2
}
\tag{3.6}
\]

throughout this whole middle cell.

## 4. The two remaining neutral cells are exactly FCFS

Only a short closure argument is needed.

If `r>t^2` and `d<=d_0`, then

\[
H\le m,\qquad d<m,
\]

so M-SERPT's increasing envelope is constant at `m`. For Gittins, the lower envelope starts at `m`, and every later selected rank is at most `m`; once a job begins service it is never displaced by a fresh job. Thus both policies are sample-path FCFS.

If `r<=t^2` and `d<=h`, then similarly the Gittins fresh rank is `m`, every later selected rank is at most `m`, and M-SERPT's increasing envelope is constant at `m`. Again both policies are sample-path FCFS.

Hence in both regions

\[
\boxed{E[T_M]/E[T_G]=1.}
\tag{4.1}
\]

## 5. Complete partition theorem for `{1,2,2+d}`

### Theorem

For every `p,q,r>0`, `p+q+r=1`, every `d>0`, and every stable arrival rate `\lambda`, if

\[
P(X=1)=p,
\quad P(X=2)=q,
\quad P(X=2+d)=r,
\]

then

\[
\boxed{E[T_{M\text{-}SERPT}]<2E[T_{Gittins}].}
\tag{5.1}
\]

At the FCFS-neutral parameter boundaries equality of policies may occur, but the factor-two inequality remains strict whenever the mean response times are finite and nonzero.

### Proof by exhaustive rank topology

For `r<=t^2`, threshold ordering gives `d_1<=h<=d_0`:

1. `d<=h`: Section 4, both policies FCFS;
2. `h<d<=d_0`: Section 3, ratio `<3/2`;
3. `d>d_0`: previous R7-04 one-hill theorem, ratio `<2`.

For `r>t^2`, ordering gives `d_0<h_0<d_1`:

1. `d<=d_0`: Section 4, both policies FCFS;
2. `d_0<d<=d_1`: Section 2, ratio `<3/2`;
3. `d>d_1`: previous R7-04 two-hill theorem, ratio `<2`.

These cases are exhaustive. QED.

## 6. Structural handoff to P01-B

The new identity `(2.15)` sharpens the earlier tail-displacement observations. In a topology where the terminal hill is **below an earlier hill**, the additive policy gap still has a monotone contact law: it decreases quadratically with outward tail displacement until the terminal hill reaches the fresh Gittins rank, then saturates and becomes exactly location-invariant.

This suggests an arbitrary-law object more robust than per-valley charges:

> **Prefix-charge/envelope-contact principle (finite-law evidence).** The excess `E[T_M]-E[T_G]` accumulated before a terminal tail can be represented by a cross-valley prefix charge. Outward tail transport decreases that charge until an envelope-contact threshold and leaves it unchanged thereafter. The same first-demotion inequality that creates positive charge also strengthens the mean service enough that stability bounds the normalized charge.

In the internal-switch wedge this mechanism is exact:

\[
D=
\frac{\lambda}{2tp(1-\lambda)}
\left[t^2-qr\min\{(pd)^2,1\}\right],
\]

and the source-valid stability relation alone turns it into `D<1/2`.

A scaled family with first support point `a` gives the corresponding dimensional cap `D<a/2`. This is a concrete candidate ingredient for P01-B's high-load cross-block charging inequality, where purely local per-valley charging has already failed.

## 7. What remains

The fixed full-source interval remains `[2,5]`; this theorem does not change the arbitrary-law source constant. The next finite-law target should not be another isolated example. It is the general three-point geometry

\[
X\in\{1,b,b+d\},\qquad b>1,
\]

with arbitrary masses. The purpose is to determine whether the prefix-charge/contact identity survives a variable middle support location. If it does, the finite-support argument begins to resemble an extremal-measure reduction; if it fails, the failure term is the precise information P01-B needs in the arbitrary-law transport derivative.

## 8. Exact self-check

Corrected exact SymPy checker:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T013700Z__P0434_complete_12gap_threepoint_certificate.py`

Archived exact output:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T013700Z__P0434_complete_12gap_threepoint_certificate.out`

The output ends with `ALL_EXACT_CHECKS_PASS`. This is self-validation, not an independent audit. The earlier `013600Z` script is an unexecuted superseded draft whose final threshold-order assertion accidentally included an extra factor `t`; it is not used as evidence here.
