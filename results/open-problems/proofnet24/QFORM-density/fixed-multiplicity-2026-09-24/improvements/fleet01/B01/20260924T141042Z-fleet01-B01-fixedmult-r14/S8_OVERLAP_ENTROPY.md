# fleet01/B01 r14 improvement — sharpened invertible overlap mass and five-role entropy cancellation

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **PROVED SUPPORTING THEOREM. Multiplicity eight remains open.**

This note strengthens the B01 invertible-seed overlap-one currency and removes a separate combinatorial/dimension obstruction. It does not supply the still-missing shared-anchor analytic Fourier inequality.

## 1. Invertible-seed overlap volume

For a real symmetric matrix `A`, define

\[
V_2(A)=\sum_{\substack{|S|=|T|=2\\S\cap T=\varnothing}}
       \det A_{S,T}^2,
\qquad
V_3(A)=\sum_{\substack{|S|=|T|=3\\S\cap T=\varnothing}}
       \det A_{S,T}^2,
\]

and

\[
W^\times_{2,1}(A)=
\sum_{\substack{|S|=|T|=2,\ S\cap T=\varnothing\\
                \det A_{S,T}\ne0}}
\ \sum_{h\notin S\cup T}
\det A_{S\cup\{h\},T\cup\{h\}}^2.
\tag{1.1}
\]

The restriction to invertible seeds is essential: singular two-seeds can have nonzero overlap-one three-borders, while determinant-squared seed sampling never sees them.

Sample an ordered disjoint two-seed `(S,T)` with probability

\[
\Pr(S,T)=\frac{\det(B)^2}{V_2(A)},\qquad B=A_{S,T}.
\]

Every sampled seed is invertible. Let `L=[n]\setminus(S\cup T)` and use the baseline interpolation/completion

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},\qquad A=D+R+E,
\]

with `rank R<=6`, `D=0` on the seed, `E` zero diagonal and

\[
\mathbb E\|E\|_F^2\le9\frac{V_3}{V_2}.
\tag{1.2}
\]

For `h in L`, the bordered determinant identity is

\[
\det A_{S\cup\{h\},T\cup\{h\}}^2
 =\det(B)^2D_{hh}^2.
\]

Because (1.1) sums exactly over the nonsingular seeds in the sampling law,

\[
\boxed{
\frac{W^\times_{2,1}(A)}{V_2(A)}
=\mathbb E\sum_{h\in L}D_{hh}^2.
}
\tag{1.3}
\]

If `s_8(A)>=1`, put `eps=||E||_F`. Perturbation and `rank R<=6` give

\[
s_2(D)\ge s_8(D+R)=s_8(A-E)\ge(1-\varepsilon)_+.
\]

Since `D` is diagonal,

\[
\sum_hD_{hh}^2\ge2(1-\varepsilon)_+^2.
\tag{1.4}
\]

The function `x -> (1-x)_+^2` is convex. Hence (1.2), Cauchy--Schwarz and Jensen imply

\[
\frac{W^\times_{2,1}}{V_2}
\ge2\bigl(1-\mathbb E\varepsilon\bigr)_+^2
\ge2\left(1-3\sqrt{V_3/V_2}\right)_+^2.
\tag{1.5}
\]

This slightly sharpens the earlier linearized estimate
`2 V_2-12 sqrt(V_2 V_3)`.

### Normalized `s_8` terminal corollary

Keep the baseline `kappa=1/6400` and assume no `eta`-pivot, `s_8(A)>=1`. Then `s_5(A)>=1`, so the audited order-two spectral-to-volume theorem gives

\[
V_2(A)\ge\kappa^2.
\]

Therefore either

\[
V_3(A)\ge\kappa^3,
\]

or, if `V_3<kappa^3`,

\[
\mathbb E\varepsilon<3\sqrt\kappa=\frac3{80}
\]

and (1.5) gives

\[
\boxed{
W^\times_{2,1}(A)
>\frac{5929}{3200}\,V_2(A)
\ge\frac{5929}{131072000000}
=4.523468017578125\times10^{-8}.
}
\tag{1.6}
\]

The coefficient `5929/3200=2(77/80)^2=1.8528125` is a strict improvement over the previous `37/20=1.85` linearized coefficient.

## 2. Five-role overlap entropy theorem

Let `P` be any finite or countable family of overlap packets

\[
p=(S,T,h),\qquad |S|=|T|=2,\quad S\cap T=\varnothing,\quad h\notin S\cup T,
\]

with positive amplitudes `Delta_p`. Put

\[
W=\sum_{p\in P}\Delta_p^2>0,
\qquad
w_p=\Delta_p^2/W.
\]

For every original coordinate `i`, define its total packet-inclusion marginal

\[
\alpha_i=\Pr_{p\sim w}\{i\in S\cup T\cup\{h\}\}.
\]

Thus `sum_i alpha_i=5`.

### Theorem `QFORM-OVERLAP1-FIVE-ROLE-ENTROPY-v1`

\[
\boxed{
H(w)+\sum_i\alpha_i\log\alpha_i
\le5\log5-\log4
=\log(5^5/4).
}
\tag{2.1}
\]

Consequently, for every `theta>0`,

\[
\boxed{
\prod_p\Delta_p^{-\theta w_p}
\prod_i\alpha_i^{(\theta/2)\alpha_i}
\le
\left(\frac{5^5}{4W}\right)^{\theta/2}.
}
\tag{2.2}
\]

Zero marginals are omitted, with the usual `0 log 0=0` convention.

### Proof

After drawing `p=(S,T,h)` with law `w`, independently order the two elements of `S` uniformly and the two elements of `T` uniformly. The resulting five-role tuple

\[
R=(S_1,S_2,T_1,T_2,h)
\]

has entropy

\[
H(R)=H(w)+\log(2!)+\log(2!)=H(w)+\log4,
\tag{2.3}
\]

because the ordered tuple determines the packet and its two internal orderings.

Let `p_r` be the coordinate distribution in role `r`, `r=1,...,5`. Entropy subadditivity gives

\[
H(w)+\log4=H(R)\le\sum_{r=1}^5H(p_r).
\tag{2.4}
\]

The average role distribution is

\[
\bar p_i=\frac15\sum_{r=1}^5p_r(i)=\frac{\alpha_i}{5}.
\]

Concavity of entropy therefore yields

\[
\sum_{r=1}^5H(p_r)
\le5H(\bar p)
=5\log5-\sum_i\alpha_i\log\alpha_i.
\tag{2.5}
\]

Combining (2.4)-(2.5) proves (2.1).

For (2.2), `Delta_p^2=w_p W`, so

\[
\sum_pw_p\log\Delta_p
=\frac12\log W-\frac12H(w).
\]

Taking logarithms of the left side of (2.2) gives

\[
-\frac\theta2\log W
+\frac\theta2\left(H(w)+\sum_i\alpha_i\log\alpha_i\right),
\]

which is at most `(theta/2) log(5^5/(4W))` by (2.1). QED.

## 3. Application to the `s_8` overlap currency

Take `Delta_(S,T,h)=|det A_{S+h,T+h}|` over the invertible-seed packets in (1.1). In the no-pivot `s_8` terminal branch `V_3<kappa^3`, (1.6) and (2.2) give a fully dimension-free determinant/entropy currency.

For the exponent `theta=1/2`, which is the natural determinant exponent in a square-root/Plancherel Holder step,

\[
\prod_p\Delta_p^{-w_p/2}
\prod_i\alpha_i^{\alpha_i/4}
\le
\left(\frac{5^5}{4W^\times_{2,1}}\right)^{1/4}
<362.519.
\tag{3.1}
\]

This proves that the *number of overlap packets* and the Shannon entropy of determinant-squared sampling are not intrinsic obstacles to a dimension-free `s_8` receiver. In the diffuse marginal subbranch `alpha_i<=1/2`, the same marginals are exactly in the range where the manuscript scalar Fourier-power estimate can be used with Holder exponents `1/alpha_i>=2`.

If some `alpha_i>1/2`, then among the five ordered role marginals at least one role places `i` with probability `>1/10`; this identifies the precise promotion branch that a complete overlap receiver must handle.

## 4. Relation to the newest critical `s_8` endpoint

The current source-backed two-sided-collar analysis proves, in the same normalized no-pivot `s_8`, `V_3<kappa^3` chamber, a critical split-row characteristic-function envelope

\[
|\phi_Q(t)|\le\min(1,U/|t|),
\]

and therefore uniform membership of the output density in every finite `L^r` plus `epsilon log(1/epsilon)` small-ball control. Separately, (1.6) shows that this chamber simultaneously contains dimension-free invertible-seed overlap-one mass, and (2.1)-(3.1) show that aggregating that mass does not incur an uncontrolled entropy/cardinality loss.

Thus the remaining multiplicity-eight obstruction is narrowed further:

**GAP `QFORM-S8-SHARED-ANCHOR-ANALYTIC-LOG-REMOVAL`.** Prove a product-preserving Fourier/small-ball inequality that consumes the overlap-one shared physical anchor (including the heavy-marginal promotion cases) and gains any integrable improvement beyond the critical `1/|t|` endpoint. The combinatorial entropy bill is already paid by (2.1); what remains is the analytic shared-coordinate dependence.

This note does not claim the general `s_8` bounded-density theorem. The lowest complete full theorem remains multiplicity nine, and the unrestricted three-eigenvalue conjecture remains open.

## Dependency map and checks

Dependencies used here are only the audited baseline `lem:rank`, `lem:sampling`, `lem:completion`, `prop:volume`, plus the exact bordered determinant identity proved there. The entropy theorem is elementary and independent of the analytic grouped compiler. Exact arithmetic checks:

- `2(77/80)^2=5929/3200=1.8528125`;
- `(5929/3200)*(1/6400)^2=5929/131072000000=4.523468017578125e-8`;
- `(5^5/(4 W_0))^(1/4)=362.518042767...` at the lower bound `W_0` above.

Manual privacy review of the changed-file allowlist found only mathematical content and nonsecret repository/run identifiers.
