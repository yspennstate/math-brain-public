# P0157 — compensated-queue theorem for the three-hub stress family

**Scope.** This is a self-contained HARD7-04 route theorem for the explicit finite-third-moment barely-subcritical configuration-model family already used in the P0157 stress test. It proves the Section-I special case

\[
\frac{L_1}{H_m}\xrightarrow{\mathbb P}3,
\qquad H_m:=\frac{d}{\delta_m},
\]

for that one family. It does **not** solve van der Hofstad's full finite-third-moment crossover problem, and it makes no novelty claim. The key new device is a hub-compensated active queue whose increments are uniformly bounded even when a new degree-\(m^2\) hub is discovered.

## 1. Family and prior inputs

Let \(m\to\infty\) through even integers and set

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2,
\]

\[
N_d=M,\qquad N_3=2m^{12}-x,\qquad N_1=6m^{12}+x-M.
\]

The \(M\) degree-\(d\) vertices are the designated **hubs**. The total number of half-edges is

\[
\ell=N_1+3N_3+Md
=\frac{m^5}{2}\left(24m^7-12m^6-m^4+4m^2-3\right)
\sim12m^{12}.
\tag{1.1}
\]

The positive subcriticality parameter is

\[
\delta:=1-\frac{6N_3+Md(d-1)}{\ell}
=\frac{12m^{11}}{\ell}
\sim m^{-1}.
\tag{1.2}
\]

Thus

\[
H_m:=\frac d\delta\sim m^3.
\tag{1.3}
\]

Two earlier HARD7-04 results will be used as inputs:

1. if \(H_{\max}\) is the largest number of designated hubs in one component, then
   \[
   \mathbb P(H_{\max}=3)\to1;
   \tag{1.4}
   \]
2. with probability tending to one there is a **good V-witness**: a tree component containing exactly three hubs whose minimal three-hub subtree consists of two internally vertex-disjoint degree-three paths with arm lengths \(r,s\in[m,2m]\). If \(Z_m^g\) is the number of ordered good witnesses, then
   \[
   \mathbb P(Z_m^g>0)\to1,
   \qquad
   \mathbb EZ_m\sim c_*m,
   \quad
   c_*:=\frac{(e^{-1}-e^{-2})^2}{144}>0,
   \tag{1.5}
   \]
   where \(Z_m\) counts all ordered V-witnesses.

The frozen local fluctuation metric remains

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\tag{1.6}
\]

Nothing proved below changes (1.6).

## 2. Main theorem

### Theorem 2.1 — exact mass constant on the stress family

For the configuration model with the degree sequence above,

\[
\boxed{\frac{L_1}{H_m}\xrightarrow{\mathbb P}3.}
\tag{2.1}
\]

Equivalently, for every fixed \(\varepsilon\in(0,1)\),

\[
\mathbb P\!\left((3-\varepsilon)H_m\le L_1\le(3+\varepsilon)H_m\right)\to1.
\tag{2.2}
\]

The proof rests on a compensated queue that turns the rare large hub jumps into bounded increments.

## 3. B8/B13: the compensated queue

Explore a component by the usual active-half-edge pairing process. Let \(A_t\) be the number of active half-edges after \(t\) pairing steps and let \(H_t\) be the number of designated hubs discovered by time \(t\). Define

\[
\boxed{C_t:=A_t-dH_t.}
\tag{3.1}
\]

The process \(H_t\) is monotone, and subtracting exactly \(d\) per discovered hub removes the large positive jump caused by a hub discovery. At a pairing step, before extinction, the four possible increments are

\[
\begin{array}{c|c|c|c}
\text{partner type}&\Delta A_t&\Delta H_t&\Delta C_t\\ \hline
\text{unseen degree }3&+1&0&+1\\
\text{unseen degree }1&-1&0&-1\\
\text{unseen hub}&d-2&+1&-2\\
\text{already active half-edge}&-2&0&-2.
\end{array}
\tag{3.2}
\]

Hence

\[
\boxed{\Delta C_t\in\{-2,-1,+1\}.}
\tag{3.3}
\]

This bounded-increment identity is the decisive feature missing from the ordinary active queue.

Let \(R_{1,t},R_{3,t}\) denote the numbers of already discovered non-root ordinary vertices of degrees 1 and 3, and let

\[
D_t:=\ell-2t-1.
\]

The numbers of unseen vertices are \(U_1=N_1-R_{1,t}\), \(U_3=N_3-R_{3,t}\), and \(U_h=M-H_t\). Therefore

\[
\mu_t:=\mathbb E(\Delta C_t\mid\mathcal F_t)
=\frac{3U_3-U_1-2dU_h-2(A_t-1)}{D_t}.
\tag{3.4}
\]

From

\[
3N_3-N_1
=-\ell\delta-Md(d-2)
\tag{3.5}
\]

and \(C_t=A_t-dH_t\), (3.4) becomes the exact identity

\[
\boxed{
\mu_t=
\frac{-\ell\delta-Md^2-3R_{3,t}+R_{1,t}-2C_t+2}
{\ell-2t-1}.}
\tag{3.6}
\]

### Lemma 3.1 — uniform drift control up to the three-hub mass scale

Fix any constant \(K>0\). There is a deterministic \(\eta_m\downarrow0\), in fact one may take \(\eta_m=O(m^{-2})\), such that for all sufficiently large \(m\) and all \(t\le KH_m\) before extinction,

\[
\mu_t\ge-(1+\eta_m)\delta.
\tag{3.7}
\]

If additionally \(H_t\le3\), then

\[
\mu_t\le-(1-\eta_m)\delta.
\tag{3.8}
\]

#### Proof

Because every increment of \(C\) is at most 1,

\[
C_t\le C_0+t.
\tag{3.9}
\]

Also \(R_{1,t},R_{3,t}\le t\). Thus the numerator in (3.6) is bounded below by

\[
-\ell\delta-Md^2-O(t+|C_0|).
\tag{3.10}
\]

For all explorations used below \(|C_0|=O(m)\) or \(C_0=0\). Since

\[
Md^2=m^9,
\qquad
\ell\delta=12m^{11},
\qquad
H_m\asymp m^3,
\qquad
\frac{H_m}{\ell}=O(m^{-9}),
\tag{3.11}
\]

we have

\[
\frac{Md^2}{\ell\delta}=O(m^{-2}),
\qquad
\frac{t+|C_0|}{\ell\delta}=O(m^{-8}),
\qquad
\frac{2t+1}{\ell}=O(m^{-9}).
\tag{3.12}
\]

Dividing (3.10) by \(D_t\) proves (3.7).

If \(H_t\le3\) and the exploration has not died, then \(A_t\ge1\), so

\[
C_t=A_t-dH_t\ge1-3d.
\tag{3.13}
\]

Using \(R_{1,t}\le t\), dropping the favorable negative terms \(-Md^2\) and \(-3R_{3,t}\), and applying (3.13), the numerator in (3.6) is at most

\[
-\ell\delta+t+6d.
\tag{3.14}
\]

Now \((t+d)/(\ell\delta)=O(m^{-8})\), and again \(D_t/\ell=1+O(m^{-9})\), proving (3.8). \(\square\)

Define the martingale

\[
\mathcal M_t:=C_t-C_0-\sum_{s<t}\mu_s.
\tag{3.15}
\]

By (3.3), \(\mu_s\in[-2,1]\), so every martingale difference is bounded in absolute value by 3. Consequently, for any deterministic \(T\) and \(x>0\), Azuma-Hoeffding and a union bound give

\[
\mathbb P\!\left(\max_{t\le T}|\mathcal M_t|\ge x\right)
\le 2(T+1)\exp\!\left(-\frac{x^2}{18T}\right).
\tag{3.16}
\]

When \(T\asymp H_m=d/\delta\) and \(x\asymp d\), the exponent is of order

\[
\frac{d^2}{H_m}=d\delta\sim m.
\tag{3.17}
\]

Thus the compensated queue has an exponentially small mass-scale deviation probability, strong enough to survive polynomial post-selection over all hubs or all vertices.

## 4. Global upper bound: no component exceeds \((3+\varepsilon)H_m\)

Fix \(\varepsilon\in(0,1)\) and put

\[
t_+:=\left\lceil(3+\varepsilon)H_m\right\rceil.
\tag{4.1}
\]

First explore from a fixed hub. Then \(A_0=d\), \(H_0=1\), and

\[
C_0=0.
\tag{4.2}
\]

Stop if the component dies, if a fourth hub is discovered, or at time \(t_+\). On the event that the exploration survives through \(t_+\) while never seeing a fourth hub, we have \(H_{t_+}\le3\), hence

\[
C_{t_+}=A_{t_+}-dH_{t_+}\ge1-3d.
\tag{4.3}
\]

By the upper drift bound (3.8), for all large \(m\),

\[
\mathcal M_{t_+}
=C_{t_+}-\sum_{s<t_+}\mu_s
\ge 1-3d+(1-\eta_m)\delta t_+
\ge \frac{\varepsilon d}{2}.
\tag{4.4}
\]

Therefore (3.16) yields, uniformly over the chosen hub,

\[
\mathbb P\{\tau>t_+,\ H_s\le3\text{ for all }s\le t_+\}
\le \exp(-c_\varepsilon m)
\tag{4.5}
\]

for some \(c_\varepsilon>0\) and all sufficiently large \(m\). Since there are only \(M=m^5\) hubs,

\[
\mathbb P\{\exists\text{ hub-rooted exploration surviving past }t_+\text{ with at most three hubs}\}
=o(1).
\tag{4.6}
\]

The earlier theorem (1.4) gives \(\mathbb P(H_{\max}>3)=o(1)\). Hence with high probability every hub-containing component is exhausted in at most \(t_+\) pairing steps from any one of its hubs. A component with \(v\) vertices requires at least \(v-1\) pairing steps to expose, so

\[
\max_{C:\,C\text{ contains a hub}}|C|
\le t_++1
\le(3+\varepsilon)H_m+2
\tag{4.7}
\]

with high probability.

It remains to exclude a larger hub-free component. Fix an ordinary root \(v\), so \(C_0=A_0\le3\), and let

\[
t_0:=\lceil\varepsilon H_m\rceil.
\tag{4.8}
\]

On the event that the component is hub-free and survives through \(t_0\), we have \(H_s=0\) and hence \(C_{t_0}=A_{t_0}\ge1\). By (3.8),

\[
\mathcal M_{t_0}
\ge1-C_0+(1-\eta_m)\delta t_0
\ge\frac{\varepsilon d}{2}
\tag{4.9}
\]

for all large \(m\). Thus

\[
\mathbb P\{C(v)\text{ is hub-free and }|C(v)|>t_0+1\}
\le \exp(-c'_{\varepsilon}m).
\tag{4.10}
\]

There are \(n=8m^{12}\) vertices, so a union bound gives

\[
\mathbb P\{\exists\text{ hub-free component of size }>\varepsilon H_m+2\}=o(1).
\tag{4.11}
\]

Combining (4.7) and (4.11),

\[
\boxed{L_1\le(3+\varepsilon)H_m+2\quad\text{with probability }1-o(1).}
\tag{4.12}
\]

## 5. Conditioned witness lower bound

The upper bound is global. For the matching lower bound, we exploit the already proved good V-witness occurrence and obtain a mass tail **before** post-selecting a witness.

Fix a potential V-witness \(w\) with arm lengths \(r,s\in[m,2m]\) and put

\[
R:=r+s\in[2m,4m].
\tag{5.1}
\]

Condition on the \(R\) prescribed matching pairs of \(w\) being present. The residual matching on the remaining half-edges is uniform. The skeleton contains its three hubs and \(R-2\) degree-three internal vertices. Its unpaired active half-edge count is

\[
A_0=3d+R-6,
\qquad H_0=3,
\qquad C_0=R-6.
\tag{5.2}
\]

Let \(r_{1,t},r_{3,t}\) count newly discovered ordinary vertices during the residual exploration. The exact conditioned analogue of (3.6) is

\[
\boxed{
\mu_t^{(w)}
=
\frac{-\ell\delta-Md^2-3R+8-3r_{3,t}+r_{1,t}-2C_t}
{\ell-2R-2t-1}.}
\tag{5.3}
\]

Indeed, one simply replaces \(U_3\) by \(N_3-(R-2)-r_{3,t}\) in (3.4); the three skeleton hubs are already included in \(H_t\).

For \(t\le4H_m\), (3.3) still gives \(C_t\le C_0+t\), while \(r_{3,t}\le t\). Using (3.11)-(3.12) and \(R=O(m)\), there is the same deterministic \(\eta_m=O(m^{-2})\to0\) such that, uniformly over every possible witness \(w\),

\[
\mu_t^{(w)}\ge-(1+\eta_m)\delta.
\tag{5.4}
\]

Let \(\tau_w\) be the residual extinction time and put

\[
t_-:=\left\lfloor(3-\varepsilon)H_m\right\rfloor.
\tag{5.5}
\]

If \(\tau_w\le t_-\), then at extinction \(A_{\tau_w}=0\) while at least the three skeleton hubs have been discovered. Hence

\[
C_{\tau_w}=-dH_{\tau_w}\le-3d.
\tag{5.6}
\]

For the conditioned martingale

\[
\mathcal M_t^{(w)}:=C_t-C_0-\sum_{s<t}\mu_s^{(w)},
\tag{5.7}
\]

(5.4)-(5.6) imply, on \(\{\tau_w\le t_-\}\),

\[
\mathcal M_{\tau_w}^{(w)}
\le-3d-C_0+(1+\eta_m)\delta\tau_w
\le-\frac{\varepsilon d}{2}
\tag{5.8}
\]

for all sufficiently large \(m\), uniformly in \(w\). Applying (3.16) to the stopped conditioned martingale gives

\[
\boxed{
\sup_w
\mathbb P\!\left(\tau_w\le t_-\mid w\text{ occurs}\right)
\le p_m(\varepsilon),
\qquad
p_m(\varepsilon)\le C m^3e^{-c_\varepsilon m}=o(m^{-A})
\ \forall A>0.}
\tag{5.9}
\]

(The harmless \(Cm^3\) factor comes from the union bound over stopping times up to \(t_-\).)

Now let \(B_m(\varepsilon)\) be the number of occurring V-witnesses whose residual host exploration dies by \(t_-\). By linearity and the uniform conditional bound (5.9),

\[
\mathbb EB_m(\varepsilon)
\le p_m(\varepsilon)\,\mathbb EZ_m
=O\!\left(m^4e^{-c_\varepsilon m}\right)
=o(1),
\tag{5.10}
\]

using \(\mathbb EZ_m\asymp m\). Therefore

\[
\mathbb P(B_m(\varepsilon)>0)=o(1).
\tag{5.11}
\]

By the prior input (1.5), with probability \(1-o(1)\) there exists a good V-witness; by (5.11), with probability \(1-o(1)\) no occurring witness is early. Choose a good witness on their intersection. Its host component is a tree, so every residual pairing discovers a new vertex. The pre-exposed skeleton itself contains \(R+1\) vertices. Hence

\[
|C(w)|=R+1+\tau_w
>R+1+t_-
\ge(3-\varepsilon)H_m-O(1).
\tag{5.12}
\]

Thus

\[
\boxed{L_1\ge(3-\varepsilon)H_m-O(1)\quad\text{with probability }1-o(1).}
\tag{5.13}
\]

Combining (4.12) and (5.13) proves Theorem 2.1. \(\square\)

## 6. Why the route works and what it changes

The ordinary active queue has a jump of size \(d-2\) when it discovers a hub, so a direct Azuma argument cannot give a selection-safe tail. The transformation

\[
C_t=A_t-dH_t
\]

uses the monotone hub count to replace that jump by exactly \(-2\). On the stress family the remaining correction in its drift is only

\[
\frac{Md^2}{\ell\delta}=O(m^{-2}),
\]

so \(C_t\) follows a bounded-increment walk with drift \(-(1+o(1))\delta\) at precisely the scale needed to determine component mass. The exponentially small \(e^{-c m}\) tail then survives both the \(m^5\)-hub and \(m^{12}\)-vertex union bounds.

The resulting picture is now rigorous for this family:

\[
H_{\max}\xrightarrow{\mathbb P}3
\quad\text{and}\quad
\frac{L_1}{d/\delta}\xrightarrow{\mathbb P}3.
\tag{6.1}
\]

Thus the marked-hub skeleton and the bulk mass map really do combine multiplicatively here. In particular, a source-level crossover theorem cannot depend only on \(d_{\max}/\delta\) and the local variance ratio \(Q_n\); it must also encode the interaction of multiple comparable upper-tail degrees.

## 7. Verification and status

This is an asymptotic theorem with a complete on-page proof. It introduces no finite exhaustive assertion, so no checker-only artifact is manufactured. It uses only exact configuration-model pairing identities, bounded increments, Azuma-Hoeffding, polynomial union bounds, and the previously archived HARD7-04 theorems (1.4)-(1.5).

Status: **SELF-CHECK / PARTIAL / source OPEN.** It requires an independent proof audit before being promoted beyond a route theorem. It is not a proof of the full van der Hofstad crossover question and is not a novelty certificate.