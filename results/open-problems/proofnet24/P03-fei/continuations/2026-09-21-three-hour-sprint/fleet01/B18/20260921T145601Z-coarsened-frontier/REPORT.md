# B18 FEI: coarsening-stable scalar frontier and arithmetic rigidity of the hard-core endpoint

**Date:** 21 September 2026  
**Status:** **PARTIAL / PROVED structural implications. Full Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**  
**Route:** APPROACH 11/12: influence-greedy restriction / decision-tree entropy payment plus a restricted-potential dual.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Novelty:** no publication-priority claim.

Scientific base recovered before derivation: `master` at `7f0c28d8bdbb3e67743cca9053d8c512221dc0cd`, with later fresh heads observed during the write. Inputs used at exact scope: the current read-once `TASKS_2026-09-21.md`, `REPORT.md`, `APPROACHES.md`; B18's `20260921T111435Z-erasure-exit-dual/REPORT.md`; B14's `20260921T110553Z-scalar-erasure-frontier/REPORT.md`; and B14's `20260921T101355Z-block-lsi-overlap/REPORT.md`. No settled certificate or finite FEI sweep was rerun.

## 1. Setup

Let `g:{-1,1}^R->{-1,1}` be a nonconstant physical restriction descendant maximizing

\[
r=H(g)/I(g)
\]

among its physical restriction descendants. Let `X` be its Fourier spectral sample, `Pr[X=S]=\hat g(S)^2=:p_S`, and put `p_i=Pr[i in X]=Inf_i(g)`, `I=sum_i p_i`. The inherited all-block criticality theorem gives

\[
\Delta_AH(g)\ge r I_A,\qquad I_A=\sum_{i\in A}p_i
\tag{1.1}
\]

for every nonempty physical block `A`.

For one coordinate put

\[
Q_i=Pr(X_i=1\mid X_{-i}).
\]

The exact fibre identity is

\[
\Delta_iH=E\Psi(Q_i),\qquad B_i:=H(X_i\mid X_{-i})=E h_2(Q_i),
\tag{1.2}
\]

where

\[
\Psi(q)=h_2(q)+j(q),\qquad
j(q)=1-h_2(1/2+\sqrt{q(1-q)}).
\tag{1.3}
\]

For `r>4`, the inherited scalar-frontier theorem defines the unique `tau=tau(r) in (0,1/2)` by

\[
\kappa(\tau)=r,\qquad \kappa(q)=\Psi(q)/q,
\]

and sets

\[
b(r)=\beta(\tau(r)),\qquad \beta(q)=h_2(q)/q.
\tag{1.4}
\]

It proves: if `E Q=alpha>0` and `E Psi(Q)>=r alpha`, then

\[
E h_2(Q)\ge b(r)\alpha.
\tag{1.5}
\]

Equality forces the positive values of `Q` to equal `tau(r)` and forces equality in the `Psi` moment. The same scalar-frontier proof gives strict concavity of `j` on `(0,1/2)` through

\[
j''(q)=\frac{4[y-atanh(y)]}{(\ln2)y^3}<0,
\qquad y=2\sqrt{q(1-q)},
\]

and symmetry handles `(1/2,1)`. Hence `Psi` is concave on `[0,1]`.

## 2. New theorem: scalar frontier survives every spectral coarsening

### Theorem 2.1

For every relevant coordinate `i` and every sub-sigma-field

\[
\mathcal G\subseteq\sigma(X_{-i}),
\]

one has

\[
\boxed{H(X_i\mid\mathcal G)\ge b(r)p_i.}
\tag{2.1}
\]

### Proof

Let

\[
\bar Q_i=Pr(X_i=1\mid\mathcal G)=E[Q_i\mid\mathcal G].
\]

Concavity of `Psi` gives

\[
E\Psi(\bar Q_i)\ge E\Psi(Q_i)=\Delta_iH\ge rp_i
\]

by singleton criticality. Also `E \bar Q_i=p_i`. Apply the scalar-frontier theorem (1.5) to the law of `\bar Q_i`:

\[
H(X_i\mid\mathcal G)=E h_2(\bar Q_i)\ge b(r)p_i.
\]

QED.

This genuinely extends the current singleton frontier: the same sharp coefficient survives arbitrary forgetting, grouping, or coarsening of the other spectral coordinates.

## 3. New all-block floor and a restricted-potential dual

For disjoint `A,V subseteq R`, order `A={i_1,...,i_m}`. The chain rule plus Theorem 2.1 gives

\[
\boxed{H(X_A\mid X_V)\ge b(r)I_A.}
\tag{3.1}
\]

In particular

\[
\boxed{B_A:=H(X_A\mid X_{A^c})\ge b(r)I_A\quad\text{for every block }A.}
\tag{3.2}
\]

This improves the previous uniform all-block consequence

\[
B_A\ge \max\{r/2,r-2/\ln2\}I_A
\]

without using the block-dependent prediction error `M_A`. At the currently relevant unrestricted lower-bound calibration

\[
r_0=6.521845710923046575,
\]

numerical evaluation gives

\[
\tau(r_0)\approx0.1740316570325050,
\qquad b(r_0)\approx3.831744944624373,
\]

while `r_0-2/ln2 approximately 3.636455629145120`; the uniform coefficient gain is about `0.195289315479253`. These decimals are calibration only; (3.2) is exact.

Define the set function

\[
\boxed{\mathcal P_r(U)=H(X_U)-b(r)\sum_{i\in U}p_i.}
\tag{3.3}
\]

Then `P_r(empty)=0`; it is nonnegative, monotone, and submodular. Indeed

\[
\mathcal P_r(U\cup\{i\})-\mathcal P_r(U)
=H(X_i\mid X_U)-b(r)p_i\ge0,
\]

and entropy is submodular while the influence term is modular. This is a concrete restricted-potential dual for APPROACH 12. It does not itself upper-bound `r`, since `P_r(R)=(r-b(r))I` may remain positive.

Taking `G` trivial in Theorem 2.1 gives `h_2(p_i)>=b(r)p_i`. Since `b(r)>2` for `r>4`, this forces `p_i<1/2`; because `beta(q)=h_2(q)/q` decreases on `(0,1/2)`, it recovers the sharp cap

\[
\boxed{p_i\le\tau(r).}
\tag{3.4}
\]

## 4. Aggregate equality already forces the hard-core endpoint

Summing the singleton floor gives

\[
B(g):=\sum_iH(X_i\mid X_{-i})\ge b(r)I(g).
\tag{4.1}
\]

### Proposition 4.1

If `B(g)=b(r)I(g)`, then for every relevant `i`,

\[
\Delta_iH=rp_i,
\qquad Q_i\in\{0,\tau(r)\}\quad a.s.
\tag{4.2}
\]

Consequently the nonzero spectral support `F={S:p_S>0}` is downward closed and, with

\[
\theta=\tau/(1-\tau),
\]

one has

\[
\boxed{p_S=p_\varnothing\theta^{|S|}\quad(S\in F).}
\tag{4.3}
\]

Proof: equality of the sum (4.1) forces equality coordinatewise. In the supporting-line proof of the scalar frontier, either a strict `Psi` moment or a nonendpoint posterior would make `B_i>b(r)p_i`; hence (4.2). If `p_{T union {i}}>0`, the posterior `p_{T+i}/(p_T+p_{T+i})` equals `tau`, so `p_T>0` and `p_{T+i}/p_T=theta`. Iterate from the empty set. QED.

This removes a hypothesis from the previously recorded endpoint statement: separate assumptions `Delta_iH=rp_i` need not be imposed once aggregate equality is known.

## 5. New arithmetic rigidity of the exact endpoint

### Theorem 5.1

Under Proposition 4.1, if `g` is nonconstant Boolean, then necessarily

\[
\boxed{\theta=1/9,\qquad \tau=1/10,\qquad
r=36-18\log_2 3\approx7.470674987019189.}
\tag{5.1}
\]

Thus exact aggregate saturation `B=b(r)I` is impossible at every other `r>4`.

### Proof: rational-root quantization

Let `a_S=\hat g(S)`. Boolean Fourier coefficients on a finite uniform cube are dyadic rational. From (4.3), for every relevant singleton,

\[
|a_i|/|a_\varnothing|=\sqrt\theta=:z,
\]

so `z` and `theta=z^2` are rational.

Booleanity `g^2=1` gives

\[
\sum_S a_Sa_{S\triangle U}=0\qquad(U\ne\varnothing).
\tag{5.2}
\]

For `U={i}`, pair terms with and without `i`, divide by the nonzero `a_empty^2 z`, and use (4.3). This gives an integer polynomial

\[
P_i(\theta)=0
\]

whose constant coefficient is `+1` or `-1` (the empty/singleton pair). It is nonconstant because that term must cancel. If `theta=A/B` is reduced, the rational-root theorem forces `A=1`. Since `theta` is a rational square,

\[
\boxed{\theta=1/v^2}
\tag{5.3}
\]

for an integer `v>=2`, hence `tau=1/(v^2+1)`. Direct simplification of `r=kappa(tau)` gives

\[
\boxed{r=r_v=(v+1)^2\log_2(v+1)+(v-1)^2\log_2(v-1)-2v^2\log_2v.}
\tag{5.4}
\]

### Proof: global ratio plus the dyadic mean

Let `d=max{|S|:S in F}` and

\[
Z=\sum_{S\in F}v^{-2|S|},\qquad
P=v^{2d}Z=\sum_{S\in F}v^{2(d-|S|)}\in N.
\]

Since `p_empty=1/Z=a_empty^2`,

\[
|a_empty|=v^d/\sqrt P.
\]

The left side is rational, so `sqrt(P)` is an integer `s`. Since `a_empty` is dyadic rational, every odd prime divisor of `s` (and hence of `P`) must divide `v`.

Put

\[
W=\sum_{S\in F}|S|v^{2(d-|S|)}\in N,
\qquad I=W/P.
\]

The entropy of (4.3) is

\[
H=\log_2Z+2I\log_2v.
\]

Equating `H/I` with (5.4), multiplying by `W`, and exponentiating gives the exact rational identity

\[
\boxed{P^P v^{2((v^2+1)W-dP)}
=(v+1)^{(v+1)^2W}(v-1)^{(v-1)^2W}.}
\tag{5.5}
\]

Compare odd-prime valuations. The left side has odd-prime support only among primes dividing `v`. Any odd prime dividing `v-1` or `v+1` is coprime to `v` and occurs on the right with positive exponent, contradiction. Hence both `v-1` and `v+1` contain no odd prime factor. If `v` is even, both are positive odd integers and would both have to equal one, impossible. If `v` is odd, they are powers of two differing by two; the only pair is `2,4`. Therefore `v=3`, proving (5.1). QED.

## 6. Further exact constraints at the sole surviving endpoint

At `v=3`, write `sqrt(P)=2^a3^b`. Taking 2-adic and 3-adic valuations in (5.5) yields

\[
a=18I,\qquad d-b=10I.
\tag{6.1}
\]

Thus

\[
\boxed{k:=2I\in N,\qquad a=9k,\qquad d-b=5k,}
\tag{6.2}
\]

and

\[
\boxed{|\hat g(empty)|=(243/512)^k.}
\tag{6.3}
\]

Moreover `k>=3`. After output negation if needed, put `q=Pr[g=-1]=(1-|a_empty|)/2`. Since `243/512<1/2`, `q in (1/4,1/2)`. Edge isoperimetry gives

\[
I(g)\ge2q\log_2(1/q)>1,
\]

because `2q log_2(1/q)` is strictly concave and equals one at both `q=1/4` and `q=1/2`. Since `I=k/2`, `k=1,2` are impossible.

No existence claim is made for the surviving endpoint.

## 7. Scope and next missing lemma

The genuine universal advance is Theorem 2.1: every restriction-maximal FEI counterexample core with `r>4` retains at least `b(r)p_i` bits of conditional uncertainty in every spectral coordinate under **every** coarsening of the remaining spectrum. Equivalently every conditional block obeys `H(X_A|X_V)>=b(r)I_A`, and the residual entropy set function (3.3) is a monotone Shannon polymatroid.

The exact equality face is much smaller: aggregate equality forces the hard-core down-set law, Boolean signed convolution quantizes its activity, and the global ratio plus dyadic mean leave only `tau=1/10`, `r approximately 7.470675`, with the arithmetic signature (6.2)--(6.3).

This does **not** prove a positive dimension-free stability gap above `b(r)I`. Unbounded Fourier denominators can approximate nonattained scalar parameters in growing dimension, so exact arithmetic nonattainment is not enough for FEI.

The next APPROACH 11/12 target is therefore precise: prove a quantitative stability theorem saying that if `B(g)-b(r)I(g)` is small, then either `r` is quantitatively close to the isolated endpoint `36-18 log_2 3` with the arithmetic pattern above, or a proper physical block satisfies `Delta_AH/I_A<r`. A complementary formulation is to combine the monotone residual polymatroid with the Bernoulli-erasure EXIT curve from the previous B18 run and force Boolean phase-sensitive curvature.

**Full FEI remains OPEN / NOT PROVED.**
