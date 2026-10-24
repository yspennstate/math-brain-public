# B18 FEI: marginal-profile slack dual for restriction induction

**Date:** 21 September 2026  
**Status of full FEI:** **OPEN / NOT PROVED.**  
**Route:** APPROACH 11/12 (influence-greedy restriction / restricted-potential dual).  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive-brain retrieval was available or used.  
**Novelty:** not asserted. The point is a source-exact synthesis and a new proof target inside this repository, not a publication-priority claim.

## 1. Input already available

Let `X` be the spectral sample of a Boolean function `f`, `a_i = P(i in X) = Inf_i(f)`, `H(f)=H(X)`, and `I(f)=sum_i a_i`. The existing erasure/restriction package gives

\[
\Delta_iH:=H(f)-\frac{H(f_+)+H(f_-)}2=B_i+JS_i,
\qquad B_i=H(X_i\mid X_{-i}),
\]

and `JS_i <= (2/ln 2) min(a_i,1-a_i)`. The existing concave-restriction continuation gives the sharper exact fibre formula and cap

\[
\Delta_iH=\sum_T w_T\Psi(t_T)\le \Psi(j_i),\qquad
j_i=\min(a_i,1-a_i),
\]

with `Psi` strictly concave. I do not re-prove those settled results here.

The difficulty is that a coordinatewise estimate `Delta_i H <= C a_i` is false with any universal `C`; a proof has to retain slack from the children or choose coordinates adaptively.

## 2. A restricted potential that is non-vacuous

Define the **spectral marginal entropy**

\[
M(f):=\sum_j h_2(a_j).
\]

By ordinary entropy subadditivity,

\[
H(f)\le M(f).                                             \tag{2.1}
\]

Fix a candidate FEI constant `C` and define the computable marginal-profile slack

\[
\boxed{P_C(f):=(C I(f)-M(f))_+.}                         \tag{2.2}
\]

This is not the vacuous potential `CI-H`: it uses only the influence profile. If FEI with constant `C` is already known for a child `g`, then (2.1) and FEI together imply

\[
C I(g)-H(g)\ge \max\{0,CI(g)-M(g)\}=P_C(g).              \tag{2.3}
\]

### Marginal-slack induction criterion — PROVED

Suppose FEI with constant `C` holds in dimensions below `n`. For a nonconstant `n`-variable Boolean `f`, if there is a relevant coordinate `i` such that

\[
\boxed{
\Delta_iH(f)\le C a_i+\frac{P_C(f_+)+P_C(f_-)}2,
}                                                           \tag{2.4}
\]

then `H(f)<=C I(f)`.

**Proof.** The exact influence recursion is

\[
I(f)=a_i+\frac{I(f_+)+I(f_-)}2.
\]

Let `R_C(g)=C I(g)-H(g)`. By the lower-dimensional induction hypothesis and (2.3), `R_C(f_\pm)>=P_C(f_\pm)`. Hence

\[
\begin{aligned}
R_C(f)
&=\frac{R_C(f_+)+R_C(f_-)}2+C a_i-\Delta_iH(f)\\
&\ge \frac{P_C(f_+)+P_C(f_-)}2+C a_i-\Delta_iH(f)\ge0.
\end{aligned}
\]
This is (2.4). QED.

Thus a concrete full-FEI target is now

\[
\boxed{
\min_{i:\,a_i>0}
\left[
\Delta_iH-Ca_i-\tfrac12(P_C(f_+)+P_C(f_-))
\right]\le0                                               \tag{2.5}
}
\]

for every Boolean `f`. Unlike a finite-universe LP with the tautological potential `CI-H`, (2.5) restricts the credit to a fixed, explicit influence-profile statistic.

## 3. Parent-side form and a two-channel dependence identity

For `j != i`, write

\[
a_j^\pm=\operatorname{Inf}_j(f_\pm),\qquad
a_j=\frac{a_j^++a_j^-}{2},
\]

and set

\[
D_i:=\sum_{j\ne i}
\left[h_2(a_j)-\frac{h_2(a_j^+)+h_2(a_j^-)}2\right]\ge0. \tag{3.1}
\]

Then exactly

\[
M(f)-\frac{M(f_+)+M(f_-)}2=h_2(a_i)+D_i.                  \tag{3.2}
\]

Let `TC(f)=M(f)-H(f)` be the total correlation of the spectral-membership vector. Combining (3.2) with the restriction entropy decrement gives

\[
\boxed{
\Delta_i TC=h_2(a_i)+D_i-\Delta_iH.                       \tag{3.3}
}
\]

There is also a direct information interpretation. The erasure identity gives

\[
h_2(a_i)-B_i=I(X_i;X_{-i}).
\]

If `Y_j` is the input-side indicator that the `j`-edge is pivotal, then `a_j^\pm=P(Y_j=1\mid x_i=\pm1)`, so each summand in (3.1) is `I(x_i;Y_j)`. Therefore

\[
\boxed{
\Delta_iTC
=I(X_i;X_{-i})
 +\sum_{j\ne i} I(x_i;Y_j)
 -JS_i.                                                    \tag{3.4}
}
\]

Equation (3.4) is the useful synthesis: restriction can create/pay spectral total correlation through **two observable dependence channels**—dependence of the spectral bit on the rest of the spectral sample, and dependence of the queried input bit on the other pivotal indicators—against the already controlled `JS_i` debit. Together with the existing bound on `JS_i`,

\[
\Delta_iTC\ge I(X_i;X_{-i})+\sum_{j\ne i}I(x_i;Y_j)
-\frac{2}{\ln2}j_i.                                      \tag{3.5}
\]

This does not prove a dimension-free lower bound on the right side.

For a parent-only version of (2.4), put `G_C(f)=M(f)-C I(f)`. Since `x -> x_+` is convex, (3.2) gives

\[
\frac{P_C(f_+)+P_C(f_-)}2
\ge
\left[h_2(a_i)+D_i-Ca_i-G_C(f)\right]_+.                 \tag{3.6}
\]

Thus it is sufficient to find `i` with

\[
\boxed{
\Delta_iH\le Ca_i+
\left[h_2(a_i)+D_i-Ca_i-G_C(f)\right]_+ .                \tag{3.7}
}
\]

There are two regimes. If the bracket vanishes, one needs the ordinary local payment `Delta_i H<=C a_i`. If the bracket is positive, (3.3) shows that (3.7) is exactly `Delta_i TC>=G_C(f)`. This isolates a precise alternative for a future greedy proof: **either pay locally, or spend a certified drop of spectral total correlation.**

## 4. Why child slack is genuinely necessary: a bent-selector family

A coordinatewise universal payment is not merely unproved; it is false by an explicit Boolean family.

Let `m` be even, `N=2^m`, and let `g:{0,1}^m->{+-1}` be bent, so every Fourier coefficient has magnitude `N^{-1/2}`. Fix a point `y_0`, and let `g'` be obtained by flipping only `g(y_0)`. Define an `(m+1)`-variable Boolean function with selector bit `z` by

\[
f(y,z)=\begin{cases}g(y),&z=+1,\\ g'(y),&z=-1.\end{cases} \tag{4.1}
\]

The selector influence is

\[
a_z=2^{-m}=1/N.                                           \tag{4.2}
\]

Write the parent Fourier fibre along `z` as `(u_T,v_T)`. After harmless signs,

\[
|v_T|=N^{-1},\qquad
u_T=N^{-1/2}\varepsilon_T-N^{-1},
\]

where `epsilon_T in {+-1}` and, after normalizing `g(y_0)=1`,

\[
\#\{\varepsilon_T=+1\}=\frac{N+\sqrt N}{2},\qquad
\#\{\varepsilon_T=-1\}=\frac{N-\sqrt N}{2}.              \tag{4.3}
\]

Set

\[
A_\pm=N\mp2\sqrt N+2.
\]

The erasure entropy of the selector is therefore exactly

\[
B_z=
\frac{N+\sqrt N}{2}\frac{A_+}{N^2}h_2(A_+^{-1})
+rac{N-\sqrt N}{2}\frac{A_-}{N^2}h_2(A_-^{-1}),        \tag{4.4}
\]

and hence

\[
\boxed{
\frac{B_z}{a_z}=m+\frac1{\ln2}+o(1).                     \tag{4.5}
}
\]

Using the local JS expansion from the exact fibre identity gives

\[
\boxed{
\frac{\Delta_zH}{a_z}=m+\frac3{\ln2}+o(1).               \tag{4.6}
}
\]

So no inequality `Delta_i H<=C Inf_i` can hold for **every** coordinate with a universal `C`.

This family does **not** kill influence-greedy restriction. For every old coordinate `j`, bentness gives `Inf_j(g)=1/2`, and flipping one truth-table value changes a coordinate influence by at most `2/N`. Therefore

\[
\operatorname{Inf}_j(f)=\frac12+O(N^{-1}),               \tag{4.7}
\]

while the bad selector has influence `1/N`. Greedy restriction queries the old coordinates, not `z`.

More importantly, the marginal-slack dual (2.4) pays even the deliberately bad selector. The clean child `g` has

\[
I(g)=m/2,\quad M(g)=m,\quad P_C(g)=m(C/2-1)\quad(C>2),    \tag{4.8}
\]

and the one-point-toggled child has the same quantities up to `O(m/N)`. Thus the child slack is order `m`, whereas the selector debit in (4.6) is only order `m/N`. This is exactly the kind of slack discarded by the potential-free induction.

## 5. Fresh computations for the new criterion

I tested (2.5), not the already-settled read-once certificate. At

\[
C=6.4547837,
\]

an exhaustive Walsh computation over every Boolean function through `n=4` found no violation of the marginal-slack criterion. The worst value of the left side of (2.5) (minimum over relevant coordinates, then maximum over functions) was

```
n=1   -6.4547837000
n=2   -4.4547837000
n=3   -2.6241705883
n=4   -1.4176954811
```

Negative means that at least one relevant coordinate closes the induction with explicit margin.

For width-two tribes (all coordinates are symmetric), the same residual for `s=2,...,10` tribes (`n=2s`) was

```
s      2       3       4       5       6       7       8       9       10
R   -6.2483 -5.9295 -4.9349 -3.9292 -2.9454 -2.0688 -1.3394 -0.7641 -0.3468
```

The corresponding potential-free local ratios `Delta_iH/a_i` were

```
3.2451, 4.1502, 5.3918, 5.7825, 5.9406, 5.9968, 6.0037, 5.9870, 5.9599.
```

Thus the new credit stays nonnegative on the family that pushed the potential-free experiment to about `6.0037`; by `s=10` the local ratio itself is already below Hod's `6.4548` target.

For the bent-selector family, at `m=2,4,6,8,10,12`, the deliberately bad selector has

```
Delta_zH/a_z = 4.8677, 8.0300, 10.2560, 12.3102, 14.3236, 16.3270,
```

but its marginal-slack residual in (2.5) is respectively

```
-9.0790, -10.5159, -13.9186, -17.9987, -22.3293, -26.7452.
```

This is a useful discrimination test: the restricted potential repairs a real unbounded local-payment obstruction rather than merely improving a constant on examples where the old step already worked.

These computations are exploratory checks of the new criterion, not a proof in arbitrary dimension.

## 6. What remains / next move

Full FEI is still open. The next target on APPROACH 11/12 is now sharply stated: prove (2.5), preferably with an influence-greedy or dependence-greedy selector. Equation (3.4) says that a proof may combine two sources of credit. A coordinate with small spectral dependence `I(X_i;X_-i)` must be compensated by information that the physical input bit carries about the other pivotal indicators, or else it approaches the forbidden product-spectrum regime. The newest product-spectrum and pivotal-subcube rigidity lemmas suggest attacking precisely this two-channel alternative rather than trying another one-statistic potential.

A useful next quantitative lemma would be a dimension-free implication of the form

\[
\text{large } B_i/a_i
\quad\Longrightarrow\quad
\text{large child }P_C\text{ or large }D_i
\]

for at least one influence-greedy coordinate. The bent-selector calculation shows why the child-slack term is the correct side of such an implication; the one-point and tribes families should remain mandatory scope tests.
