# B15 — balanced stop entropy is support-deficit paid, and root/deletion addresses fuse with an indispensable KL credit

**Run:** `20260922T040227Z-account02-B15-r12`  
**Role:** account02/B15, Campaign B Shannon / spectral-arithmetic remainder.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / BRIDGE_SHARPENED`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and scientific sources were read directly, but no installed/native research-brain context was used.

## 0. Change summary

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is proved.

**MECHANISM CHANGE:** the three most recent substantive B15 reports were (i) the common harmonic-deletion KL/valuation report `20260922T000114Z-harmonic-delete-kl-valuation`, (ii) the source-valid iterated shared-graft lower-bound report `20260922T011717Z-iterated-shared-graft`, and (iii) the partial-branch shared-core renormalization report `20260922T015258Z-partial-branch-renormalization`. Their missing implications were not identical for three consecutive runs. The current owner convergence makes the balanced-uniform all-gate slice FEI-complete, so this run returns to the common Shannon source but in the **balanced support-deficit currency** `beta=I-1`, not the older `O(I)` root bound and not another lower-bound recurrence.

The substantive advances are:

1. a universal theorem `T_stop <= C_stop (I-1)` for every balanced Boolean source, obtained from the exact harmonic stopping tree plus FKN stability and edge isoperimetry;
2. a universal theorem `J <= C_J (I-1)` for balanced Boolean sources, so the previously proved valuation reserve `R<=2J` is also paid at the correct support-deficit scale;
3. an exact fusion of the root address and all non-root deletion addresses into the normalized influence profile, exposing a **new negative weighted-Jensen-Shannon / KL credit**;
4. a genuine balanced Boolean one-point-suspension family proving that this mixing KL credit is indispensable: dropping only that credit creates an unbounded loss relative to `I-1`, while the true `H/(I-1)` tends to `4`.

This leaves one explicit occurrence-entropy implication, stated in Section 5. It is not claimed proved.

## 1. Exact live target and peer results consumed

The latest owner control makes the all-gate inequality the common FEI target. I use the completed other-account theorem

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T003238Z-balanced-uniform-gate-slice/REPORT.md`
(blob `cb99a17793db7919af1cfe21248198f1a6fb2f24`).

It consumes the earlier balanced-support-deficit equivalence and proves that, constant-for-constant,

\[
H(h)\le C I(h)\quad\hbox{for every Boolean }h
\]

is equivalent to

\[
\boxed{H(f)\le C\bigl(I(f)-1\bigr)\quad\hbox{for every balanced Boolean }f.}
\tag{1.1}
\]

Thus the balanced-uniform gate slice already contains the whole FEI conjecture; potential shape away from bias `1/2` cannot bypass (1.1).

The common Shannon source is account03/B18

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T235729Z-harmonic-deletion-residual/HANDOFF_B.md`
(blob `4c872737c5d91a6054face583380f959192f8326`).

For the spectral sample `S` with `p_A=P(S=A)`, `K=|S|`, and uniform-prefix shadows

\[
v_A=\sum_{S\supseteq A}\frac{p_S}{\binom{|S|}{|A|}},\qquad t_A=v_A-p_A,
\]

it gives

\[
H(f)=H(J)+T_{\rm stop}+D_{\rm del}.
\tag{1.2}
\]

My preceding B15 report proved the exact canonical KL form

\[
D_{\rm del}
=\beta H_2(\rho)-\mathbb E\log_2(K!)-\mathcal K_\rho,
\tag{1.3}
\]

where

\[
\beta_i=\mathbb E\!\left[\frac{K-1}{K}\mathbf 1_{\{i\in S\}}\right],
\quad \beta=\sum_i\beta_i=\mathbb E(K-1)_+,
\quad \rho_i=\frac{\beta_i}{\beta},
\tag{1.4}
\]

and

\[
\mathcal K_\rho
=\sum_{a\ge1}\sum_{|A|=a}
 t_A D_{\rm KL,2}(\pi_A\|\rho)\ge0
\tag{1.5}
\]

is the actual prefix-dependent deletion-label KL rebate. It also proved that charging an unbounded valuation price independently at every deletion is false on standard addressing; valuation can be spent only once or coupled to these information credits.

Finally I use the already proved B15 valuation theorem

\[
R(f):=\mathbb E r(S)\le2J(f),
\qquad
J(f)=\sum_i\min(\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)),
\tag{1.6}
\]

with its stronger stop-loss form retained but not re-proved here. No physical projection integrality is assumed.

The newest account03/B18 shared-graft lower-bound report was also read. It raises the necessary balanced cap but does not alter the upper-bound implication (1.1); the present run attacks (1.1) directly rather than freezing another lower-bound cap.

## 2. First new theorem: harmonic stopping entropy is paid by the balanced support deficit

Assume from now on that `f` is balanced. Then `p_emptyset=0`, hence `K>=1` almost surely. Put

\[
I=\mathbb E K,\qquad \beta=I-1=\mathbb E(K-1).
\tag{2.1}
\]

The quantity `beta` is exactly the denominator in the balanced FEI formulation (1.1).

### 2.1 The stop entropy is at most the entropy of the level

Let

\[
W_a=\Pr(K=a),\qquad Q_a=\Pr(K\ge a).
\]

For each level `a>=1`, the prefix identities satisfy

\[
\sum_{|A|=a}v_A=Q_a,
\qquad
\sum_{|A|=a}p_A=W_a.
\tag{2.2}
\]

The stop term at level `a` is

\[
T_a=\sum_{|A|=a}v_A h_2(p_A/v_A).
\]

By concavity of binary entropy,

\[
T_a\le Q_a h_2(W_a/Q_a).
\tag{2.3}
\]

The right side is exactly the hazard-chain contribution to the entropy of the positive integer stopping time `K`; summing over `a` gives

\[
\boxed{T_{\rm stop}\le H_2(K).}
\tag{2.4}
\]

This is an analytic identity/inequality for the actual harmonic prefix process; no Boolean relaxation is introduced.

### 2.2 Booleanity removes the generic `beta log(1/beta)` stopping loss

A generic positive-integer law with mean `1+beta` can have entropy of order `beta log(1/beta)` as `beta->0`. Balanced Boolean spectra cannot realize that bad near-character behavior.

Let

\[
\delta=\Pr(K\ge2)=\sum_{k\ge2}W_k.
\]

Since every `k>=2` contributes at least `k-1>=1`,

\[
\delta\le\beta.
\tag{2.5}
\]

Use the quantitative Friedgut--Kalai--Naor stability theorem in the following standard form: there are absolute constants `A>=1` and `delta_F>0` such that, whenever a Boolean function has Fourier mass at most `delta_F` above level one, it is `A delta`-close in probability to a constant or a signed dictator. For a balanced function and sufficiently small `delta`, the constant case is impossible. Thus there are `i,sigma` with

\[
r:=\Pr[f\ne\sigma\chi_i]\le A\delta.
\tag{2.6}
\]

Let `g=f sigma chi_i`. Then `g` is Boolean and has minority density `r`. Also

\[
\widehat f(\{i\})=\sigma(1-2r),
\]

so, writing `j_i=Inf_i(f)`,

\[
1-j_i\le1-\widehat f(\{i\})^2
=4r(1-r)\le4r.
\tag{2.7}
\]

Multiplication by `chi_i` toggles membership of coordinate `i` in every Fourier set and leaves the other coordinate incidences unchanged. Hence

\[
I(g)=I(f)+1-2j_i
=\beta+2(1-j_i)
\le\beta+8r.
\tag{2.8}
\]

The sharp cube edge-isoperimetric inequality gives, for `r<=1/2`,

\[
I(g)\ge2r\log_2(1/r).
\tag{2.9}
\]

Also `W_1>=\widehat f(\{i\})^2`, hence

\[
\delta\le4r(1-r)\le4r.
\tag{2.10}
\]

Choose once and for all

\[
\eta=\min\!\left\{\delta_F,\frac1{4A},\frac1{256A^2}\right\}>0.
\tag{2.11}
\]

If `beta<eta`, then `delta<eta`, `r<=1/2`, and

\[
\log_2(1/r)-4
\ge \frac12\log_2(1/\delta).
\]

Combining (2.8)--(2.10),

\[
\beta\ge2r(\log_2(1/r)-4)
\ge r\log_2(1/\delta)
\ge\frac\delta4\log_2(1/\delta).
\tag{2.12}
\]

Therefore

\[
h_2(\delta)
\le\delta\log_2(1/\delta)+\frac\delta{\ln2}
\le\left(4+\frac1{\ln2}\right)\beta.
\tag{2.13}
\]

If `beta>=eta`, simply `h_2(delta)<=1<=beta/eta`. Thus in all cases

\[
h_2(\delta)\le C_h\beta,
\qquad
C_h:=\max\!\left\{4+\frac1{\ln2},\frac1\eta\right\}.
\tag{2.14}
\]

Conditional on `K>=2`, the positive integer `N=K-1` has mean `mu=beta/delta`. Among positive-integer laws of given mean, the geometric law maximizes entropy, and its entropy is at most `mu/ln2`. Hence

\[
H_2(K)
=h_2(\delta)+\delta H_2(N\mid N\ge1)
\le h_2(\delta)+\frac\beta{\ln2}.
\tag{2.15}
\]

Combining (2.4), (2.14), and (2.15) proves:

### Theorem B15-STOP-SUPPORT-01

There is a finite absolute constant

\[
\boxed{
C_{\rm stop}
=\max\!\left\{4+\frac2{\ln2},\frac1\eta+\frac1{\ln2}\right\}<\infty
}
\tag{2.16}
\]

(depending only on any fixed quantitative FKN constants) such that every balanced Boolean function satisfies

\[
\boxed{T_{\rm stop}(f)\le C_{\rm stop}\,[I(f)-1].}
\tag{2.17}
\]

This is the first support-deficit payment in this run. It is not a finite-dimensional observation.

## 3. Second universal payment: folded influence and the valuation reserve are also support-deficit paid

The same FKN stability immediately converts the old valuation reserve into the balanced currency.

When `beta<eta`, use the signed dictator from (2.6). By (2.7), `a:=1-j_i<=4A beta`; our choice of `eta` makes `j_i>=1/2`. Therefore

\[
\begin{aligned}
J(f)
&=\sum_k\min(j_k,1-j_k)\\
&\le (1-j_i)+\sum_{k\ne i}j_k\\
&=a+(I-j_i)\\
&=\beta+2a\\
&\le(1+8A)\beta.
\end{aligned}
\tag{3.1}
\]

When `beta>=eta`, the trivial `J<=I=1+beta` gives

\[
J\le\left(1+\frac1\eta\right)\beta.
\tag{3.2}
\]

Hence:

### Theorem B15-FOLDED-SUPPORT-02

For every balanced Boolean function,

\[
\boxed{J(f)\le C_J[I(f)-1],}
\qquad
C_J:=\max\!\left\{1+8A,1+\frac1\eta\right\}<\infty.
\tag{3.3}
\]

Consequently the already proved valuation-tail theorem is now available in the balanced all-gate currency:

\[
\boxed{R(f)\le2J(f)\le2C_J[I(f)-1].}
\tag{3.4}
\]

This matters because the preceding harmonic-deletion report showed that valuation cannot be charged once per deletion. Equation (3.4) certifies that it *can* be spent once globally without losing the support-deficit scale required by the all-gate equivalence.

## 4. Exact root/deletion fusion: a new negative KL credit

Still assume `beta>0`; the character case `beta=0` is terminal and all continuation terms vanish.

Define the root-coordinate law

\[
\alpha_i:=\Pr(J=i)
=\mathbb E\!\left[\frac{\mathbf1_{\{i\in S\}}}{K}\right].
\tag{4.1}
\]

Since `K>=1`, `alpha` is a probability law. Define the normalized influence/occurrence law

\[
q_i:=\frac{j_i}{I},
\qquad j_i=\Pr(i\in S).
\tag{4.2}
\]

By (1.4),

\[
\alpha_i+\beta\rho_i
=\mathbb E\!\left[\frac1K\mathbf1_{i\in S}
+\frac{K-1}{K}\mathbf1_{i\in S}\right]
=j_i=I q_i.
\tag{4.3}
\]

Thus `q` is exactly the mixture

\[
q=\frac1I\alpha+\frac\beta I\rho.
\tag{4.4}
\]

The weighted Jensen-Shannon identity gives

\[
I H_2(q)-H_2(\alpha)-\beta H_2(\rho)
=D_{\rm KL,2}(\alpha\|q)
+\beta D_{\rm KL,2}(\rho\|q).
\tag{4.5}
\]

Define this nonnegative **root/deletion mixing credit** by

\[
\boxed{
\mathcal J_{\rm mix}
:=D_{\rm KL,2}(\alpha\|q)
+\beta D_{\rm KL,2}(\rho\|q)\ge0.
}
\tag{4.6}
\]

Now substitute the preceding exact deletion identity (1.3) into (1.2), use `H(J)=H(alpha)`, and then (4.5). This yields the exact source identity

### Theorem B15-OCCURRENCE-KL-03

For every balanced noncharacter Boolean `f`,

\[
\boxed{
H(f)
=I(f)H_2(q)
+T_{\rm stop}(f)
-\mathbb E\log_2(K!)
-\mathcal K_\rho
-\mathcal J_{\rm mix}.
}
\tag{4.7}
\]

Every negative term is a genuine information credit arising from the actual Boolean spectral source:

- `E log K!` is the permutation/factorial refund;
- `K_rho` is the history-dependent deletion-label KL refund;
- `J_mix` is the new refund for revealing whether a coordinate occurrence is the root occurrence or one of the remaining occurrences.

No positive part is taken. In particular, (4.7) is stronger bookkeeping than separately upper-bounding `H(J)` and `D_del`.

Combining (4.7) with Theorem B15-STOP-SUPPORT-01 gives

\[
H(f)
\le
\underbrace{I H_2(q)-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}}_{\mathcal U_{\rm occ}(f)}
+C_{\rm stop}\beta.
\tag{4.8}
\]

This identifies the first remaining Shannon implication in the balanced FEI-complete formulation.

## 5. Compact conditional universal argument and the exact unpaid implication

The end-to-end argument is now short.

1. By the completed account03/B13 balanced-support-deficit equivalence, it suffices to prove `H(f)<=C beta` for every balanced Boolean `f`, where `beta=I-1`.
2. The exact harmonic code and Theorem B15-OCCURRENCE-KL-03 give (4.7).
3. Theorem B15-STOP-SUPPORT-01 pays `T_stop<=C_stop beta` universally.
4. Therefore one finite constant in

\[
\boxed{
\mathcal U_{\rm occ}(f)
:=I H_2(q)-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}
\le C_{\rm occ}\,[I(f)-1]
}
\tag{5.1}
\]

would prove full FEI with constant `C_occ+C_stop`.

This is the **first missing Shannon implication** after the new paid step. It retains both relative-entropy refunds and the factorial refund.

The valuation theorem can be spent once, at the correct scale, by Theorem B15-FOLDED-SUPPORT-02. Hence the formally weaker joint-credit target

\[
\boxed{
\mathbb E\log_2(K!)+\mathcal K_\rho+\mathcal J_{\rm mix}+R(f)
\ge I H_2(q)-C_*\beta
}
\tag{5.2}
\]

is also sufficient: (3.4) and (4.8) would give

\[
H(f)\le(C_*+2C_J+C_{\rm stop})\beta,
\]

and therefore the same finite constant for unrestricted FEI via (1.1).

Equation (5.2), not a repeated per-deletion valuation fee, is the source-exact place where the valuation reserve can now enter.

## 6. Genuine Boolean obstruction: the mixing KL cannot be dropped

The new credit in (4.6) is not cosmetic. Consider the balanced suspension of the one-point defect. On `m` old variables let

\[
h_m(x)=1-2\mathbf1_{\{x=x_0\}},
\]

and on one new independent coordinate `y` put

\[
f_m(y,x)=y\,h_m(x).
\tag{6.1}
\]

Then `f_m` is balanced. Set

\[
\varepsilon=2^{1-m},\qquad \beta_m=m\varepsilon,
\qquad I(f_m)=1+\beta_m.
\tag{6.2}
\]

The spectral sets all contain `y`. The singleton `{y}` has mass `(1-epsilon)^2`; every `{y} union T`, `T nonempty`, has mass `epsilon^2`. Thus

\[
q_y=\frac1{1+\beta_m},
\qquad
q_{x_i}=\frac\varepsilon{1+\beta_m},
\tag{6.3}
\]

and exactly

\[
I H_2(q)=\log_2(1+\beta_m)+\beta_m(m-1).
\tag{6.4}
\]

Let `u_m` be the total root-law mass on the old `x` coordinates. The beta-integral/binomial identity

\[
\sum_{\ell=0}^m\frac{\binom m\ell}{\ell+1}
=\frac{2^{m+1}-1}{m+1}
\]

gives

\[
\boxed{
 u_m
=\varepsilon\frac{2m-2+\varepsilon}{m+1}.
}
\tag{6.5}
\]

By symmetry,

\[
\alpha=(1-u_m,u_m/m,\ldots,u_m/m),
\tag{6.6}
\]

while

\[
\rho=(u_m/\beta_m,
(1-u_m/\beta_m)/m,\ldots,(1-u_m/\beta_m)/m).
\tag{6.7}
\]

Therefore the mixing KL has the exact closed form

\[
\boxed{
\begin{aligned}
\mathcal J_{\rm mix}(f_m)
={}&\log_2(1+\beta_m)
+\beta_m(m-1-\log_2m)\\
&-h_2(u_m)-\beta_m h_2(u_m/\beta_m).
\end{aligned}
}
\tag{6.8}
\]

Since

\[
\frac{u_m}{\beta_m}
=\frac{2m-2+\varepsilon}{m(m+1)}
=\frac2m+O(m^{-2}),
\]

we obtain

\[
\boxed{
\frac{\mathcal J_{\rm mix}(f_m)}{\beta_m}
=m-\log_2m+O(1)\longrightarrow\infty.
}
\tag{6.9}
\]

In contrast, direct evaluation of the two spectral magnitude masses gives

\[
\boxed{
\frac{H(f_m)}{\beta_m}\longrightarrow4.
}
\tag{6.10}
\]

Now look at the exact identity (4.7). If one drops **only** the negative term `-J_mix`, while retaining `T_stop`, the factorial credit, and the prefix KL credit exactly, the resulting upper proxy is identically

\[
H(f_m)+\mathcal J_{\rm mix}(f_m).
\]

By (6.9)--(6.10), its ratio to `I(f_m)-1=beta_m` diverges. Hence:

### Theorem B15-MIXING-CREDIT-OBSTRUCTION-04

No balanced support-deficit proof of (5.1) can discard the root/deletion mixing KL credit `J_mix`, even if the factorial and prefix-history KL credits are retained exactly. The failure occurs on a genuine balanced Boolean family whose true support-deficit entropy ratio tends to `4`.

This is not a counterexample to FEI. It is a counterexample to a stronger credit-dropping lemma. It also explains why a root code paid separately in `O(I)` units is too coarse near characters: the root and deletion address laws must be recombined before the `I-1` cancellation becomes visible.

## 7. Finite sanity check

`check_balanced_stop_kl.py` independently reconstructs Walsh spectra, all uniform-prefix shadows, the stop term, the deletion kernel, `K_rho`, and `J_mix` for **every balanced Boolean function through dimension four**.

The archived output reports:

- balanced functions checked: `12,948`;
- maximum absolute residual in the exact fusion identities: `1.7763568394002505e-15` bits;
- maximum observed `T_stop/H(K)`: exactly `1.0` within floating arithmetic;
- maximum observed `H(K)/(I-1)`: `2.648920586603283`;
- maximum observed `J/(I-1)`: `3.0`.

It also evaluates the exact suspension formulas at `m=4,8,16,32`; `J_mix/beta` grows from `0.0459...` to `25.2690...`, while `H/beta` is already `3.9651...` at `m=32`. The finite sweep is only a sanity check; Theorems 2.17, 3.3, 4.7 and the asymptotic obstruction are analytic.

## 8. Literature / applicability

The only external structural theorem used in the new support-deficit payments is the classical Friedgut--Kalai--Naor stability theorem: low Fourier mass above degree one forces a Boolean function to be `O(delta)`-close to a constant or dictator. The original 2002 paper is *Boolean functions whose Fourier transform is concentrated on the first two levels*, Advances in Applied Mathematics 29, 427--437. No claim is made that the present corollaries are new in the literature.

Current FEI literature checked for scope remains partial: González--MacManus--Pereyra (2026) give restriction/stopping-tree progress and structured classes; Potapov (18 September 2026) proves FEI for plateaued and partially bent functions, not the unrestricted conjecture; Li--Han's information-theoretic inequality retains an influence-profile entropy term. None supplies (5.1) or (5.2) as an unrestricted theorem.

## 9. Exact status / next obligation

**PROVED this run:**

- `T_stop <= C_stop (I-1)` for all balanced Boolean functions, for one finite universal constant;
- `J <= C_J (I-1)`, hence the old valuation reserve `R<=2J` is spendable once at support-deficit scale;
- the exact occurrence-profile identity (4.7) with the new negative mixing KL credit;
- the balanced one-point-suspension obstruction proving that `J_mix` cannot be dropped.

**UNPAID:** either (5.1) or the weaker valuation-assisted joint-credit inequality (5.2).

The next B15 attack should therefore work directly on the coordinate-occurrence entropy

\[
I H_2(q)
\]

against the **combined** factorial + prefix-KL + root/deletion-mixing-KL + one-time valuation credits. A rowwise or per-deletion charge is already refuted; a credit-free influence-profile inequality is also the wrong target. The one-point suspension, addressing, recursive majority, the unequal-magnitude physical-lattice counterexample, and the shared-graft balanced gates are mandatory stress tests.

## 10. Working-rule moves used

This run used three fresh working-rule moves on the live implication: **#11 dualize** (convert root/deletion entropy into exact KL divergences), **#18 say it in another language** (view the harmonic prefix code as a positive-integer stopping process and use hazard entropy), and **#30 one scale/direction at a time** (first pay the scalar stop-time level entropy at `I-1` scale before returning to coordinate identities). The first two produced the new exact bridge; the third produced Theorem B15-STOP-SUPPORT-01.
