# B13 — simultaneous affine-minimum primitive critical core and exchange-depth exclusion

**Status:** PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy-influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was consumed.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. **Configured/known reasoning:** UNKNOWN / selector not exposed. **Provider reasoning usage:** NOT_EXPOSED.

## 0. Fresh scope and source-bound dependency actually used

The applicable owner controls were refreshed from `yspennstate/math-research-brain`; the later collective order preserves B12–B18 on FEI and the execution reset assigns account02/B13 to Campaign A critical-core/tensor/gauge quantifiers. Scientific master was refreshed on `yspennstate/math-open-problems/master`.

The named completed **other-account** result used materially is

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2325Z-asymmetric-exception-compiler/REPORT.md`

blob `52039a8b5b499dc23c073e194e3183a6d9cc0205`.

I use its exact asymmetric coefficient-12 physical block theorem and its low-depth threshold
\[
\delta_{\rm asy}(r)=
\frac{W(2(\ln2)(8r+9))}{4(\ln2)(8r+9)} ,
\]
together with the support-stability estimate `e/j <= phi(delta) <= delta` for `0<delta<=eta0`, where the peer keeps `eta0<=1/32`.

Two earlier own inputs are used rather than reannounced: the exact affine-basis formula/exchange principle from `20260921T172807Z-affine-block-basis-profile`, and the exact derivative sign-defect decomposition from `20260921T180326Z-sign-stability-defect` (blob `b4812f3ae22e7f98596f4b1abcb284dc2d180457`).

## 1. Last three B13 substantive reports: exact before/after

The last three completed substantive B13 reports were:

1. `20260921T211122Z-block-holevo-support-boundary`: paid physical restriction-mixture information by the oriented support-boundary bank; left the conditional spectral-label term.
2. `20260921T215826Z-cross-plaquette-tensor-correction`: constructed an actual-anchor signed product correction with a dimension-free conditional-Shannon code; left the physical-to-Fourier Shannon transfer.
3. `20260921T232801Z-critical-core-tensor-tax`: proved the fixed-C minimum-dimensional `H-CJ` critical-core reduction, tensor primitivity, and the folded-cooling tensor tax; it did **not** prove that tensor primitivity/restriction criticality can coexist with a globally minimum affine basis, nor insert the newest asymmetric low-depth certificate into that core.

**FULL-PROBLEM CHANGE:** no finite universal FEI constant is proved. The new result makes the Campaign-A quantifiers simultaneous: if constant `C` fails, one may work with a *single* counterexample that is restriction-critical, tensor-primitive, and already in a globally minimum affine basis. At `C=12`, the account04 asymmetric low-depth certificate then rules out the entire zero/low-depth maximum-row regime and forces a strict affine surplus.

**MECHANISM CHANGE:** the previous run used a Laplace-transform cooling potential and tensor tax. This run instead uses orbit minimization under `GL(n,2)` + characters, vector-matroid basis exchange, and the actual Boolean mixed-derivative depth. This is a different mechanism, not another renamed profile.

## 2. Folded influence and affine influence

For Boolean `f` let
\[
J(f)=\sum_i \min\{\Inf_i(f),1-\Inf_i(f)\}.
\]
Multiplying by a character preserves Fourier entropy and can independently fold each coordinate, so
\[
\sup_f \frac{H(f)}{I(f)}
=
\sup_f \frac{H(f)}{J(f)}.
\]

For a translation `u` write
\[
c_f(u)=\mathbb E_x f(x)f(x+u),\qquad
\widetilde q_f(u)=\frac{1-|c_f(u)|}{2}.
\]
The earlier affine theorem gives
\[
I_{\rm aff}(f)
=
\min_{B\ {\rm basis}}\sum_{u\in B}\widetilde q_f(u)
=
\min_{T,a} I(\chi_a(f\circ T)),
\]
hence `I_aff(f) <= J(f)` by taking `T=Id` and the best character.

## 3. PROVED: one counterexample can be simultaneously primitive, restriction-critical, and affine-minimal

### Theorem 3.1 — simultaneous core compiler

Fix a finite `C`. If `H(f)<=C I(f)` fails for some Boolean function, then there exists a Boolean `g` of minimum possible ambient dimension such that simultaneously:

1. `H(g)>C J(g)`;
2. `g` is in a globally minimizing affine gauge:
   \[
   J(g)=I(g)=I_{\rm aff}(g);
   \]
3. `g` has no nontrivial disjoint Boolean tensor factorization;
4. for every nonempty proper physical coordinate block `A`,
   \[
   \boxed{\Delta_A H(g)> C D_A^J(g)\ge C I_A(g),}
   \tag{3.1}
   \]
   where
   \[
   D_A^J=J(g)-\mathbb E_a J(g_{A=a}),\qquad
   I_A=\sum_{i\in A}\Inf_i(g).
   \]

Thus every physical block theorem proved in the affine-minimizing coordinates is legitimate on the **same tensor-primitive critical core**.

### Proof

Failure of ordinary FEI at `C` implies failure of `H<=CJ`, because `J<=I`. Conversely a character multiplier realizes `I=J`, so the two universal constants are equivalent.

Choose a minimum-dimensional `f` with
\[
\delta_C(f):=H(f)-CJ(f)>0.
\]
Now choose `T,a` attaining `I_aff(f)` and put `g=chi_a(f o T)`. Entropy is unchanged and
\[
J(g)\le I(g)=I_{\rm aff}(f)\le J(f).
\]
The minimizing character in fact orients every basis correlation nonnegative, so every coordinate influence of `g` is at most `1/2`; hence `J(g)=I(g)=I_aff(f)`. Therefore
\[
\delta_C(g)\ge\delta_C(f)>0.
\]
The dimension did not change, so `g` is itself a minimum-dimensional `J`-violator.

Every proper restriction `g_{A=a}` has smaller dimension, hence
\[
\delta_C(g_{A=a})\le0.
\]
Therefore
\[
\Delta_AH-C D_A^J
=
\delta_C(g)-\mathbb E_a\delta_C(g_{A=a})
\ge\delta_C(g)>0.
\tag{3.2}
\]
Because the parent is fully folded, `J(g)=I(g)`, while `J(h)<=I(h)` for every child. The exact ordinary block restriction identity is
\[
I(g)-\mathbb E_a I(g_{A=a})=I_A(g).
\]
Consequently
\[
D_A^J
=I(g)-\mathbb E_aJ(g_{A=a})
\ge I(g)-\mathbb E_aI(g_{A=a})
=I_A(g),
\]
which proves (3.1).

Finally, both `H` and `J` are additive on a disjoint Boolean product. A nontrivial factorization of `g` would therefore put ratio `>C` on at least one smaller-dimensional factor (a zero-`J` character factor contributes zero entropy and can simply be removed), contradicting minimality. QED.

### Why this quantifier matters

The earlier affine formulation and the earlier tensor-critical reduction were separate. The theorem shows there is no gauge/tensor incompatibility: affine orbit minimization only decreases `J`, so it preserves violation and therefore preserves the minimum-dimensional critical-core conclusions.

## 4. PROVED: all-parity exchange envelope in the simultaneous core

Work in the minimizing coordinates of Theorem 3.1. Let the spectral sample be `X`, and put
\[
p_i=\Pr(i\in X)=\Inf_i(g)\le\frac12.
\]
For any nonempty `T subset [n]`, let
\[
q_T=\Pr\left(\bigoplus_{i\in T}X_i=1\right).
\]

### Theorem 4.1 — joint parity envelope

For every nonempty `T`,
\[
\boxed{\min(q_T,1-q_T)\ge\max_{i\in T}p_i.}
\tag{4.1}
\]

### Proof

Let `b_1,...,b_n` be the minimizing translation basis. For any `i in T`, replacing `b_i` by
\[
v_T=\bigoplus_{j\in T}b_j
\]
preserves a basis because the coefficient of `b_i` in `v_T` is one. Minimum basis weight therefore gives
\[
\widetilde q(v_T)\ge \widetilde q(b_i)=p_i.
\]
Taking the maximum over `i in T` proves (4.1). QED.

This is a jointly realizable family over **all** parities, not a sign-free independent-row relaxation.

## 5. PROVED: two-sided pair atoms and a universal mixed-depth cap

Write
\[
p_{ik}=\Pr(i,k\in X)=\|D_kD_i g\|_2^2
\]
and
\[
d_i=\sum_{k\ne i}p_{ik}.
\]

Taking `T={i,k}` in (4.1), and setting
\[
a=\max(p_i,p_k),\qquad b=\min(p_i,p_k),
\]
the XOR probability is `p_i+p_k-2p_ik` and must lie in `[a,1-a]`. Hence

\[
\boxed{
\max\!\left\{0,\ a+\frac b2-\frac12\right\}
\le p_{ik}\le \frac b2 .
}
\tag{5.1}
\]

Summing the upper bound gives, for every row,
\[
\boxed{
d_i\le\frac12\sum_{k\ne i}\min(p_i,p_k).
}
\tag{5.2}
\]

If `x` is a maximum-influence coordinate and `m=p_x`, then
\[
\boxed{d_x\le\frac{I_{\rm aff}(g)-m}{2}.}
\tag{5.3}
\]

Let its Boolean derivative-depth defect be
\[
\delta_x=\frac{d_x}{m}-\frac12\log_2\frac1m\ge0.
\]
The nonnegativity is the Boolean derivative edge-isoperimetric depth bound. Equation (5.3) yields the new scalar cap
\[
\boxed{
0\le\delta_x
\le
\frac12\left[
\frac{I_{\rm aff}(g)}m-1-\log_2\frac1m
\right].
}
\tag{5.4}
\]

Both boundary families can saturate (5.4): the one-point defect has `delta_x=0`, while quadratic bent functions have `m=1/2` and saturate the high-depth endpoint. Thus (5.4) is not itself an FEI proof; its use is through criticality below.

## 6. APPLYING account04/B13: a 12-critical affine core cannot have a zero/low-depth maximum row

Now specialize Theorem 3.1 to a hypothetical failure of the finite constant `C=12`. Then every physical block satisfies
\[
\Delta_AH>12I_A.
\tag{6.1}
\]

Take a maximum-influence row `x`, `m=p_x`.

### Zero defect is impossible

If `delta_x=0`, the exact sign-defect decomposition from the earlier B13 sign-stability report has all four nonnegative banks equal to zero. Hence `D_xg` has one sign on its support and the support is an edge-isoperimetric equality set, therefore a coordinate subcube `Q` of codimension `r`, with `m=2^{-r}`.

Let `Z` be its defining controls. Since `x` has maximum influence,
\[
I_Z\le r m.
\]
The support errors are exactly `E^-=E^+=0`, so account04/B13's asymmetric coefficient-12 theorem gives
\[
\Delta_ZH\le12I_Z,
\]
contradicting (6.1). Thus
\[
\boxed{\delta_x>0.}
\tag{6.2}
\]

### Low positive defect must be outside the asymmetric capture threshold

Suppose `0<delta_x<=eta0`. The consumed peer theorem gives a codimension-`r` proxy subcube `Q`, density `q=2^{-r}`, with
\[
e/m\le\phi(\delta_x)\le\delta_x.
\tag{6.3}
\]
If `delta_x<=delta_asy(r)`, that peer theorem again produces the physical coefficient-12 block certificate, contradicting (6.1). Therefore
\[
\boxed{\delta_x>\delta_{\rm asy}(r).}
\tag{6.4}
\]

Moreover `|q-m|<=e`. Since `eta0<=1/32`,
\[
q\ge (1-\delta_x)m\ge\frac{31}{32}m.
\]
Putting `L=log_2(1/m)` and `c_0=log_2(32/31)=0.0458036896...`,
\[
r\le L+c_0.
\tag{6.5}
\]
The continuous extension of `delta_asy(t)` is decreasing, since `W(x)/x=exp(-W(x))`. Hence
\[
\delta_x>\delta_{\rm asy}(L+c_0).
\tag{6.6}
\]

If instead `delta_x>eta0`, that is already the high-defect branch. Combining both branches gives the gauge-free scalar necessary condition
\[
\boxed{
\delta_x>
\tau(m):=
\min\left\{
\eta_0,\,
\delta_{\rm asy}\!\left(\log_2\frac1m+c_0\right)
\right\}.
}
\tag{6.7}
\]

Insert (6.7) into the affine depth cap (5.4):

\[
\boxed{
\frac{I_{\rm aff}(g)}m
>
1+\log_2\frac1m+2\tau(m).
}
\tag{6.8}
\]

This is a quantitative **anti-one-point surplus** forced on every minimum-dimensional 12-counterexample in its globally minimum affine gauge. The exact one-point family has equality `I_aff/m=1+log_2(1/m)` and is therefore excluded from such a critical core by a strict amount.

Equivalently the global row-defect bank obeys
\[
\mathcal D(g)=\sum_i p_i\delta_i
\ge m\delta_x
>m\tau(m).
\tag{6.9}
\]
This is not yet a universal `Omega(I)` payment, but it is a jointly realizable, tensor-compatible critical-core constraint that feeds both Campaign A (no capturable low-depth max row) and Interface B (the maximum row contributes a quantified positive defect).

## 7. Exact finite self-check

`check_affine_critical_exchange.py` is standard-library only. It exhausts every Boolean function modulo global output sign through `n=4` (32,906 functions). It verifies:

- 492,442 exact all-parity exchange-envelope inequalities;
- 394,000 exact lower/upper pair-atom inequalities;
- 131,474 exact mixed-depth caps;
- 459,536 exact folded-`J` block-drift inequalities in affine-minimizing gauges;
- 459,536 exact `I_aff` child-drift inequalities as a stronger diagnostic;
- 4 one-point/bent endpoint equalities.

Total: **1,936,992 checks, PASS**.

The witness diagnostics reproduce:
- one-point defect, `n=4`: `m=1/8`, `I_aff=1/2`, `d_x=3/16`, `delta_x=0`;
- one-point defect, `n=8`: `m=1/128`, `I_aff=1/16`, `d_x=7/256`, `delta_x=0`;
- quadratic bent, `n=4`: `m=1/2`, `I_aff=2`, `d_x=3/4`, `delta_x=1`;
- quadratic bent, `n=8`: `m=1/2`, `I_aff=4`, `d_x=7/4`, `delta_x=3`.

The finite checker is a self-check only; the theorems above are proved on the page.

## 8. What moved and what remains

**Proved this run:** a single FEI counterexample may be chosen simultaneously minimum-dimensional for folded `J`, tensor-primitive, strict under every physical restriction, and globally affine-basis-minimized; in that same core all parity biases satisfy the exchange envelope (4.1), every mixed derivative row satisfies (5.2), and a hypothetical 12-counterexample has the strict anti-one-point surplus (6.8).

**Not proved:** `H<=12I`, or any other finite universal FEI constant. The remaining branch is a genuinely high-depth/asymmetrically exceptional affine-minimum primitive core.

**Next exact target:** use the all-parity envelope (4.1), not just pairwise depth, to control the *high-depth cluster* left by account04/B13. The natural next quantity is the jointly realized parity code of the maximum-row Palm law. Any successful estimate must turn the forced surplus `tau(m)` into a block decrement without summing pairwise witnesses with reuse.
