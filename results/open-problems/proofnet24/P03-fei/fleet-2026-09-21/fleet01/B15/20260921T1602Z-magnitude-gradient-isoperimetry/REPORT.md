# B15 — sharp isoperimetric payment for the one-sided Fourier magnitude gradient

**Status:** full Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used in this mathematics.  
**Route:** APPROACH 4/8, unequal Fourier magnitudes and spectral arithmetic structure.  
**Novelty:** no publication-priority claim. This is an internal proof-route lemma and obstruction until independently situated in the literature.

The current owner handoff already corrects the old sharp-constant target: Hod's `beta(1/2)=6.4547837...` is a read-once target, not the universal FEI constant; the recovered external Numaro 18-variable seed gives the strict full-FEI lower bound `C_FEI > 6.521845710923046575`. I therefore do not rerun the settled read-once certificate or try to prove the refuted universal-Hod claim.

This run continues the newest B15 quantity. For a physical coordinate `i`, write, for `T` not containing `i`,

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
\alpha_i=\sum_T v_T^2=\operatorname{Inf}_i(f),
\]

and

\[
L_i(f)=\sum_{T:v_T\ne0}v_T^2\log_2^+\frac{|u_T|}{|v_T|}.
\tag{1}
\]

The previous B15 handoff proved

\[
\Delta_iH\le \frac3{\ln2}\alpha_i+2L_i.
\tag{2}
\]

The new point is that `L_i` has an exact two-regime structural payment. One side is a pure log-sum bound; the other is a sharp edge-isoperimetric bound on the physical sensitivity section.

---

## 1. A universal information bound for one coordinate

Assume `0<alpha_i<1`; the endpoints are immediate. Put

\[
P(T)=\frac{v_T^2}{\alpha_i},\qquad
Q(T)=\frac{u_T^2}{1-\alpha_i}.
\]

Then

\[
\frac{2L_i}{\alpha_i}
=
\sum_TP(T)
\left[
\log_2\frac{(1-\alpha_i)Q(T)}{\alpha_iP(T)}
\right]_+.
\tag{3}
\]

Use `[log_2 x]_+ <= log_2(1+x)` and concavity of the logarithm. Since only points with `P(T)>0` contribute,

\[
\begin{aligned}
\frac{2L_i}{\alpha_i}
&\le
\sum_{P(T)>0}P(T)
\log_2\left(1+\frac{(1-\alpha_i)Q(T)}{\alpha_iP(T)}\right)\\
&\le
\log_2\left(1+\frac{1-\alpha_i}{\alpha_i}
\sum_{P(T)>0}Q(T)\right)\\
&\le \log_2\frac1{\alpha_i}.
\end{aligned}
\]

Hence

\[
\boxed{
L_i(f)\le \frac{\alpha_i}{2}\log_2\frac1{\alpha_i}.
}
\tag{4}
\]

No Boolean convolution identity was used in this step; only the squared-norm split `sum u^2=1-alpha_i`, `sum v^2=alpha_i`.

---

## 2. The derivative support forces exactly the same logarithmic budget into higher Fourier degree

Let

\[
h_i=(f_+-f_-)/2\in\{0,\pm1\}
\]

on the `(n-1)`-cube. Its Fourier coefficients are the `v_T`. Let

\[
A_i=\{x:h_i(x)\ne0\}.
\]

Then `Pr(A_i)=alpha_i`. Define the excess-degree energy

\[
J_i(f):=\sum_T |T|v_T^2
=\sum_{S\ni i}(|S|-1)\widehat f(S)^2.
\tag{5}
\]

By the Fourier Dirichlet identity,

\[
J_i(f)=\frac14\sum_{j\ne i}
\mathbb E\bigl(h_i(x)-h_i(x^{\oplus j})\bigr)^2.
\tag{6}
\]

Every edge crossing the support boundary of `A_i` contributes exactly `1` to the squared difference in (6); sign changes inside `A_i` only increase it. Thus

\[
J_i(f)\ge \frac14\sum_{j\ne i}
\Pr[1_{A_i}(x)\ne1_{A_i}(x^{\oplus j})].
\tag{7}
\]

The edge-isoperimetric inequality on the cube says that for a set of density `a<=1/2`, the directed boundary quantity on the right is at least

\[
2a\log_2(1/a).
\]

For `a>1/2` apply the same statement to the complement. The elementary inequality

\[
(1-a)\log_2\frac1{1-a}\ge a\log_2\frac1a,
\qquad a\ge1/2,
\]

then gives, for every `0<a<1`,

\[
\boxed{
J_i(f)\ge \frac{\alpha_i}{2}\log_2\frac1{\alpha_i}.
}
\tag{8}
\]

Combining (4) and (8) proves the main structural bound

\[
\boxed{
L_i(f)\le
\min\left\{
\frac{\alpha_i}{2}\log_2\frac1{\alpha_i},\ J_i(f)
\right\}
\le J_i(f)
\quad\text{for every Boolean }f\text{ and every }i.
}
\tag{9}
\]

The constant `1` in `L_i<=J_i` is sharp; section 4 gives an explicit asymptotically saturating Boolean family.

This result is useful precisely because it retains unequal Fourier magnitudes. `J_i` is not the arithmetic remainder `D`; it is the amount of Fourier degree living *above* coordinate `i`, and (9) says a long one-sided magnitude likelihood tail cannot appear without that degree being present.

---

## 3. A hard-core reduction for the exploratory `kappa=3/2` selector

The previous B15 target was to find a relevant coordinate with

\[
L_i\le \kappa\alpha_i.
\tag{10}
\]

For `kappa=3/2`, (9) gives two immediate escape regimes. If

\[
\alpha_i\ge1/8,
\]

then

\[
\frac{L_i}{\alpha_i}
\le\frac12\log_2(1/\alpha_i)\le\frac32.
\]

If instead

\[
\frac{J_i}{\alpha_i}\le\frac32,
\]

then again `L_i/alpha_i<=3/2`.

Therefore any Boolean function that refutes the `kappa=3/2` selector must satisfy, **for every relevant coordinate**,

\[
\boxed{
\alpha_i<\frac18,
\qquad
\frac{J_i}{\alpha_i}>\frac32.
}
\tag{11}
\]

Equivalently, if `S` is the spectral sample,

\[
\frac{J_i}{\alpha_i}
=
\mathbb E[|S|-1\mid i\in S],
\]

so a selector counterexample must have every relevant bit both rare in the spectral sample and, conditional on appearing, accompanied by more than `3/2` other spectral bits on average.

Together with (2), the exact new local restriction bound is

\[
\boxed{
\Delta_iH
\le
\frac3{\ln2}\alpha_i
+
2\min\left\{
J_i,
\frac{\alpha_i}{2}\log_2\frac1{\alpha_i}
\right\}.
}
\tag{12}
\]

This does **not** prove full FEI. It removes all coordinates outside the hard core (11) from the remaining `kappa=3/2` problem.

---

## 4. Sharp obstruction: a genuine Boolean coordinate can have `L_i/Inf_i -> infinity`

The preceding B15 report proposed using the exact Boolean fibre constraints

\[
u*v=0,\qquad u*u+v*v=\delta_\varnothing
\tag{13}
\]

to improve the likelihood tail. Those constraints alone cannot give a uniform bound for a *fixed* coordinate.

Let `m=2r` and define the canonical bent quadratic

\[
b_r(y)=(-1)^{y_1y_2+\cdots+y_{2r-1}y_{2r}}.
\]

It has

\[
\widehat b_r(S)=q\,\sigma_S,
\qquad q=2^{-r},\quad \sigma_S\in\{\pm1\},
\]

with

\[
\#\{\sigma=+1\}=\frac{q^{-2}+q^{-1}}2,
\qquad
\#\{\sigma=-1\}=\frac{q^{-2}-q^{-1}}2.
\]

Define a Boolean function on `(y,t)` by taking one selector slice to be `b_r` and the other to be `b_r` with its value at `y=0` flipped. For the selector coordinate `t`,

\[
v_S=q^2,
\qquad
u_S=q\sigma_S-q^2,
\qquad
\alpha_t=q^2=2^{-2r}.
\tag{14}
\]

Hence

\[
\boxed{
\frac{L_t}{\alpha_t}
=
 r+rac12\left[
(1+q)\log_2(1-q)
+(1-q)\log_2(1+q)
\right]
=r-o(1).
}
\tag{15}
\]

So `L_t/Inf_t -> infinity` in an entirely genuine Boolean family satisfying all convolution constraints (13). In fact `v_S^2` is uniform over all `S subseteq [2r]`, so

\[
J_t=\alpha_t r,
\]

and therefore

\[
\boxed{
\frac{L_t}{J_t}\to1.
}
\tag{16}
\]

This proves the sharpness of the constant `1` in (9).

The same example also shows why an existential selector can still survive. Every inner coordinate `j` has

\[
\alpha_j=\frac12+q^2.
\tag{17}
\]

For the canonical quadratic, the only positive magnitude-gradient fibres for `j` occur when the paired frequency bit is present and the bent Fourier sign changes from `-` to `+`. Their exact number is

\[
M_r=\frac{4^{r-1}-2^{r-1}}2.
\]

Consequently

\[
\boxed{
L_j
=M_r(q-q^2)^2
\log_2\frac{q+q^2}{q-q^2},
}
\tag{18}
\]

and

\[
\boxed{
\frac{L_j}{\alpha_j}\sim \frac{2^{-r}}{2\ln2}\to0.
}
\tag{19}
\]

Thus one coordinate can realize essentially the worst possible logarithmic magnitude tail while *every other coordinate becomes asymptotically easy*. Pairwise Booleanity is insufficient; any proof of the existential selector must use a genuinely cross-coordinate mechanism.

This is also a clean stress test of APPROACH 4: the selector Fourier coefficients carrying the derivative mass are all of size `2^{-2r}`, much smaller than the bent background scale `2^{-r}`, but that tiny-coefficient phenomenon costs `r` units of conditional spectral degree exactly as (9) predicts.

---

## 5. What this changes for the full FEI attack

The previous next step was “derive a level-set estimate from `u*v=0`, `u*u+v*v=delta`.” The bent-one-flip family shows that no fixed-coordinate estimate of that type can be uniformly constant: the full positive likelihood tail can remain at mass `alpha_t` for `Theta(r)` logarithmic scales.

The surviving route is narrower and global:

1. use (9) to dispose of any coordinate with `alpha_i>=1/8` or conditional excess degree `J_i/alpha_i<=3/2`;
2. in the hard core (11), exploit **cross-coordinate consistency** of the derivative supports, rather than a one-coordinate convolution inequality;
3. the concrete target is now to show that a Boolean function cannot have `L_i/alpha_i>3/2` simultaneously on every coordinate satisfying (11), or else build such a function as a genuine counterexample candidate.

A useful aggregate identity for the next run is

\[
\sum_iJ_i
=
\sum_S |S|(|S|-1)\widehat f(S)^2.
\tag{20}
\]

It is not by itself enough (parity makes the right side huge while every `L_i=0`), so the next lemma must retain the *one-sided magnitude* information from (1), not replace it wholesale by `J_i`.

The fresh public-source check on 21 September 2026 still has unrestricted FEI open: González--MacManus--Pereyra (arXiv:2606.00246) explicitly leave the universal restriction step open, while Potapov (arXiv:2609.21563, submitted 18 September 2026) proves sharp constant `4` for plateaued functions and constant `2` for partially bent functions, not arbitrary unequal-magnitude spectra.

---

## 6. Reproducibility

`check_magnitude_isoperimetry.py` exhausts every Boolean function through dimension four for

\[
L_i\le \min\{J_i,\tfrac12\alpha_i\log_2(1/\alpha_i)\},
\]

then constructs the bent-one-flip family through `r=7` by exact integer Walsh transforms and checks (15), (17), and (18) against the direct spectrum.

The universal statements (4), (8), and (9) are analytic; the finite computation is only a sanity control and a closed-form-family verification.

Checker SHA-256: `4a422f37c797760bcb65c8fa31f83bccd750fb7e49d02264f908ed37bd0b4e87`  
Recorded stdout SHA-256: `b73b7ed09c31038331018be18feee80f701eabdcf45fd72e1b95129731096b3f`

**Next B15 attack:** stay on APPROACH 4. Search for a cross-coordinate inequality that uses the sign/magnitude edge gradients themselves and proves an existential `L_i/alpha_i<=3/2` inside the hard core (11). Do not return to a fixed-coordinate likelihood bound: section 4 rules that out sharply.