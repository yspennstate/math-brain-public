# fleet03 / B12 — first-spectral-member compression and two route-1/3 obstructions

**Run:** `20260921T141130Z-B12-fei-r11`  
**Status:** full uniform-cube Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Brain assistance:** **WITHOUT_VERIFIED_BRAIN**. A native `import math_brain` attempt in this invocation failed with `ModuleNotFoundError`; no authenticated brain retrieval or receiver-context use occurred.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction) and #3 (coupling to input sensitivity), after the previous fleet03/B12 `v -> 0` read-once boundary piece had already been advanced. This run does not audit or rerun that certificate.

No novelty or publication-priority claim is made.

## 1. Exact universal statement attempted

Let `f:{-1,1}^n -> {-1,1}`, let

\[
p_S=\widehat f(S)^2,\qquad S\sim p,\qquad
I_i=\Pr(i\in S)=\operatorname{Inf}_i(f),\qquad I=\sum_i I_i.
\]

Put

\[
\sigma=\Pr(S\ne\varnothing)=1-\widehat f(\varnothing)^2
\]

and, conditional on `S != empty`, choose a uniformly random member `J` of `S`.
Equivalently define

\[
a_i:=\sum_{S\ni i}\frac{p_S}{|S|},\qquad
\Pr(J=i\mid S\ne\varnothing)=\frac{a_i}{\sigma}.
\]

The attempted universal first-step compression statement was:

> **ROOT-CODE.** There is an absolute constant `C_root` such that
> \[
> \sigma H_2(J\mid S\ne\varnothing)\le C_{\rm root} I(f)
> \]
> for every Boolean `f`.

This is **PROVED** below, with the explicit constant

\[
C_{\rm root}
=\left(2+\frac1e\right)\log_2 e
=3.4161279272\ldots.
\]

This is only a first-stage sequential compression lemma. It does **not** prove FEI by itself.

## 2. PROVED: the root spectral member is a noise-average of sensitivity energy

For the normalized discrete derivative `D_i f`,

\[
\widehat{D_i f}(T)=\widehat f(T\cup\{i\}).
\]

Hence, coefficientwise,

\[
\boxed{\;
a_i
=\int_0^1\left\|T_{\sqrt t}D_i f\right\|_2^2\,dt.
\;}
\tag{2.1}
\]

Indeed, the coefficient from a set `S` containing `i` is

\[
p_S\int_0^1 t^{|S|-1}\,dt=\frac{p_S}{|S|}.
\]

This is a direct spectral-to-sensitivity bridge: `D_i f` is ternary, taking values in
`{-1,0,1}`, and

\[
\|D_i f\|_2^2=\Pr[D_i f\ne0]=I_i.
\]

## 3. PROVED: hypercontractivity gives an integrable logarithmic gain

For `0<=t<=1`, Bonami--Beckner with `rho=sqrt(t)`, target exponent `2`, and source
exponent `1+t` gives

\[
\|T_{\sqrt t}D_i f\|_2
\le \|D_i f\|_{1+t}.
\]

Because `D_i f` is ternary,

\[
\|D_i f\|_{1+t}^2=I_i^{\,2/(1+t)}.
\]

Therefore

\[
a_i\le F(I_i),\qquad
F(x):=\int_0^1x^{2/(1+t)}\,dt.
\tag{3.1}
\]

For `0<x<1`, write `L=ln(1/x)` and make the substitution

\[
s=\frac{1-t}{1+t}.
\]

Then

\[
\frac{F(x)}x
=2\int_0^1\frac{e^{-Ls}}{(1+s)^2}\,ds
\le 2\int_0^1e^{-Ls}\,ds
=\frac{2(1-x)}L.
\]

Thus

\[
\boxed{\;
a_i\ln\frac1{I_i}\le 2I_i(1-I_i)\le2I_i.
\;}
\tag{3.2}
\]

The endpoint cases follow by continuity; if `I_i=0` then `a_i=0`.

## 4. PROVED: ROOT-CODE with an explicit constant

Use as a coding distribution the normalized sensitivity-edge incidence profile

\[
q_i=\frac{I_i}{I}.
\]

Nonnegativity of relative entropy gives

\[
\sigma H_{\rm nat}(J\mid S\ne\varnothing)
\le
\sum_i a_i\ln\frac{I}{I_i}.
\]

By (3.2),

\[
\sum_i a_i\ln\frac{I}{I_i}
=
\sum_i a_i\ln\frac1{I_i}+\sigma\ln I
\le 2I+\sigma\ln I.
\]

If `I<=1`, the last term is nonpositive. If `I>1`, use `sigma<=1` and
`ln I <= I/e`. Hence in all cases

\[
\sigma H_{\rm nat}(J\mid S\ne\varnothing)
\le\left(2+\frac1e\right)I.
\]

Converting nats to bits proves

\[
\boxed{\;
\sigma H_2(J\mid S\ne\varnothing)
\le
\left(2+\frac1e\right)\log_2(e)\,I
<3.417\,I.
\;}
\tag{4.1}
\]

Interpretation: the **first** uniformly chosen spectral coordinate has a
dimension-free description length when paid by total influence, even though its
ambient coordinate label may carry `log n` bits.

This is exactly the kind of payment route #1 asks for, and the proof uses the
input-side sensitivity event `D_i f != 0`, as requested by route #3.

## 5. REFUTED: raw sensitivity-set entropy cannot be the next payment

APPROACHES #3 proposed trying to reduce FEI to a bound of the form

\[
H(\operatorname{Sens}(X))\le C I(f).
\]

That exact subgoal is **REFUTED** by the one-point defect.

Let `f` differ from a constant at exactly one cube vertex. Then:

- at the defect vertex, `Sens(X)=[n]`;
- at each of its `n` neighbours, `Sens(X)` is the corresponding singleton;
- at every other vertex, `Sens(X)=empty`.

Thus there are `n+1` distinct rare nonempty sensitivity patterns, each with
probability `2^{-n}`, and

\[
I(f)=\frac{2n}{2^n}.
\]

Consequently

\[
\frac{H(\operatorname{Sens}(X))}{I(f)}
=
\frac{n+1}{2}
-\frac{2^n-n-1}{2n}
\log_2\!\left(1-\frac{n+1}{2^n}\right),
\]

so

\[
\frac{H(\operatorname{Sens}(X))}{I(f)}
=\frac n2+O(1)\to\infty.
\]

The script gives, for `n=4,8,12,16,20`,

\[
3.2433,\ 5.2971,\ 7.2802,\ 9.2663,\ 11.2574.
\]

Therefore a useful coupling cannot afford to encode the **entire** sensitivity
set. It must use a cheaper object such as a sensitive incidence, a cluster
representative, or a restriction-dependent local predictor.

This does not refute the possibility of a coupling between the spectral sample
and sensitivity information; it refutes only the raw entropy reduction above.

## 6. REFUTED: the earlier global influence-profile ordered code is unbounded

The previous B12 ordered-set bound was

\[
H(S)\le
U(f):=
H(K)+I\,H(q)-\mathbb E\log_2(K!),
\qquad K=|S|,\quad q_i=I_i/I.
\tag{6.1}
\]

A natural hope was `U(f)<=C I(f)` universally. Balanced tribes refute this.

Take `m` disjoint tribes of width `w`, with

\[
m=m_w\sim(\ln2)\,2^w
\]

chosen so that the output is asymptotically balanced. Symmetry makes `q`
uniform on `n=mw` coordinates, hence

\[
H(q)=\log_2(mw)=w+\log_2 w+O(1).
\tag{6.2}
\]

For one block put `a=1-2^{-w}`. In the normalized squared Fourier law of
`1-AND_w`,

- the empty block occurs with probability `a`;
- a nonempty block occurs with probability `2^{-w}`;
- conditional on being nonempty, its subset is uniform over the
  `2^w-1` nonempty subsets.

Therefore in the disjoint product law the number of active blocks is
`Bin(m,2^{-w})`, which tends to `Poisson(ln 2)`, while an active block
contributes `w/2+O_P(sqrt(w))` coordinates. After the harmless nonempty
conditioning and size bias needed for `E[K log K]/I`, this still gives

\[
\mathbb E_{\rm size\;biased}\log_2 K
=\log_2 w+O(1).
\tag{6.3}
\]

Also `I(f)=Theta(w)`, `H(K)=O(log w)`, and Stirling gives

\[
\mathbb E\log_2(K!)
=
\mathbb E[K\log_2K]-(\log_2 e)I+O(\log w).
\]

Combining with (6.2)--(6.3),

\[
\boxed{\;
\frac{U(f)}{I(f)}=w+O(1)\to\infty.
\;}
\tag{6.4}
\]

So the earlier global `q_i=Inf_i/I` code is **REFUTED as a universal FEI
closure**. The problem is structural: in tribes it pays the tribe/block label
again for many coordinates from the same block. A successful sequential code
must learn and reuse cluster information.

The executable finite-width calculation confirms the asymptotic mechanism:

| width `w` | balanced `m` | `I` | `H(q)-E_sb log2 K` | `U/I` |
|---:|---:|---:|---:|---:|
| 4 | 11 | 2.8845 | 3.7143 | 5.3342 |
| 6 | 44 | 4.1914 | 5.7647 | 7.3933 |
| 8 | 177 | 5.5551 | 7.7945 | 9.4035 |
| 10 | 709 | 6.9335 | 9.8101 | 11.3991 |
| 12 | 2839 | 8.3190 | 11.8206 | 13.3930 |

This is not an exhaustive Boolean-function sweep; it is a single explicit
family used to attack the negation of the proposed universal code.

## 7. PROVED: a restriction-slice identity that points to the repair

The obstruction above says the predictor must become local after observing a
prefix. There is an exact way to bring Boolean restrictions back into the
non-Boolean higher-derivative prefix state.

Fix `A`, let `z` be uniform in `{-1,1}^A`, and let `f_z` denote the Boolean
restriction. For `i notin A` and `0<=s<=1` define the prefix fixed-scale child
energy

\[
E_{A,i}(s)
=
\sum_{D\subseteq A^c\setminus\{i\}}
\widehat f(A\cup\{i\}\cup D)^2s^{|D|}.
\]

The restriction Fourier formula and orthogonality in `z` give

\[
\boxed{\;
\mathbb E_z\|T_{\sqrt s}D_i f_z\|_2^2
=
\sum_{B\subseteq A}
\sum_{D\subseteq A^c\setminus\{i\}}
\widehat f(B\cup\{i\}\cup D)^2s^{|D|}
\ge E_{A,i}(s).
\;}
\tag{7.1}
\]

Thus every fixed-scale prefix child profile is one orthogonal Fourier slice of
an average of **genuine Boolean-restriction sensitivity profiles**.

This is the concrete route-1/route-3 repair suggested by the two
counterexamples:

- do not encode the whole sensitivity set;
- do not keep using the global influence profile after a cluster has been
  discovered;
- instead, use restriction-conditioned/noise-scale sensitivity profiles to
  predict the next spectral coordinate, while explicitly paying only the
  information needed to select the `B=A` Fourier slice in (7.1).

The missing step is an aggregate bound for that slice-selection information.
A pointwise bound is not asserted.

## 8. Attempted refutation / stress tests

Three potential closures were deliberately stress-tested.

1. **Raw sensitivity entropy:** refuted exactly by the one-point defect,
   with ratio `~n/2`.
2. **Global influence ordered code `U<=CI`:** refuted by balanced tribes,
   with `U/I=w+O(1)`.
3. **ROOT-CODE:** no refutation; it is proved universally by (2.1)--(4.1).
   Balanced tribes are a useful stress test: the root first-member entropy
   payment is still only `O(I)`, even though the global repeated-label code
   diverges.

For the balanced tribes rows above, the actual root first-member
cost divided by `I` is approximately `1.8921, 1.9193, 1.8843, 1.8449,
1.8099` at widths `4,6,8,10,12`, respectively, well below the proved
universal `3.4162` bound.

## 9. Classification and next attack

- **PROVED:** root first-spectral-member compression (4.1), universal for
  every uniform-cube Boolean function.
- **PROVED:** exact noisy sensitivity-energy representation (2.1).
- **PROVED:** exact restriction-slice orthogonality/domination (7.1).
- **REFUTED:** `H(Sens(X))<=C I(f)` with universal `C`.
- **REFUTED:** the earlier global influence-profile ordered-code target
  `U(f)<=C I(f)`.
- **OPEN:** a dimension-independent aggregate payment for the slice-selection
  information in (7.1).
- **OPEN:** full FEI.

**Next attack:** augment the uniform-prefix chain by a latent Boolean
restriction label `z` and the beta/noise scale. Use (7.1) to code the next
coordinate from a genuine restricted sensitivity profile, then isolate the
extra mutual information needed to select the `B=A` Fourier slice. The target
is to show that this *aggregate* selector information is summable by `O(I)`;
balanced tribes demand that the proof reuse block information after the first
hit, while the one-point defect demands that it never encode the full
sensitivity pattern.

## 10. Reproducibility

`root_shadow_tribes_check.py` is standard-library only. It evaluates the exact
one-point sensitivity law and the disjoint-product Fourier level law for
balanced tribes, using a binomial active-block decomposition. No old `n<=5`
FEI exhaustive sweep is rerun.

The full FEI conjecture remains **OPEN**.
