# B07 / A034 — soft Rényi fiber completion of phase energy

**Run:** `20261011T220628Z-fleet01-B07-a034-renyi-fiber`  
**Primary packet:** A034 (Phase-energy transfer)  
**Attempt:** `A034-RENYI-FIBER-2`  
**Claim version:** `B07-A034-RENYI-FIBER-v1`  
**Gap:** `G-PHASE-COND`  
**Status:** restricted theorem PROVED; independent review pending; full FEI OPEN.

## Result

Let `f:{-1,1}^X x {-1,1}^Y->{-1,1}` be genuine Boolean on disjoint uniform physical cubes, and suppose its `X`-Fourier degree is at most `d>=1`. Write

`P(R,T)=fhat(R,T)^2`, `p_X(R)=sum_T P(R,T)`,

and, when `p_X(R)>0`,

`q_R(T)=P(R,T)/p_X(R)`.

Define the soft fiber complexity

`A_{1/2}(f)=sum_R p_X(R) log_2 K_{1/2}(R)`,

where

`K_{1/2}(R)=(sum_T sqrt(q_R(T)))^2=(sum_T |fhat(R,T)|)^2/p_X(R)`.

Since Shannon entropy is at most Rényi entropy of order `1/2`,

`H(S_Y|S_X)<=A_{1/2}(f)`.

Combining this with the already proved Boolean-granularity phase estimate gives

`H(f) <= (2/ln 2) I_Y(f)+2(d-1)-E_y Gamma_d(f_y)+A_{1/2}(f)`.  (R1/2)

Thus, if `A_{1/2}(f)<=A` and `Var(f)>=nu>0`,

`H(f) <= [2/ln 2+(2(d-1)+A)/nu] I(f)-E_y Gamma_d(f_y)`.

This is dimension-independent for fixed `d,A,nu`. It is a restricted theorem, not full FEI.

## Proof

The chain rule is exact:

`H(f)=H(p_X)+sum_R p_X(R)H(q_R)`.

For every probability law `q`, monotonicity of Rényi entropy gives

`H(q)<=H_{1/2}(q)=2 log_2 sum_i sqrt(q_i)`.

Average this inequality over `R` and insert the proved marginal bound

`H(p_X)<=(2/ln2)I_Y(f)+2(d-1)-E_y Gamma_d(f_y)`.

For the variance consequence, Poincaré gives `I(f)>=Var(f)>=nu`, so the additive `2(d-1)+A` is at most `[(2(d-1)+A)/nu]I(f)`.

All zero-mass fibers are omitted. Every entropy is in bits. The physical input law remains the uniform product law; only the auxiliary spectral coordinates may be correlated.

## Why this advances the hard-support theorem

Cauchy--Schwarz gives

`K_{1/2}(R)<=|supp(q_R)|`.

Hence a hard support cap `K` implies `A_{1/2}<=log_2 K`, but not conversely. The soft condition admits actual Boolean fibers with unbounded support.

Let `a_k` be the Boolean AND sign on `k` variables, equal to `-1` only at the all-ones input. For `k>=2` its Fourier support has size `2^k`, while

`||ahat_k||_1=3-2^(2-k)<3`,

so its spectral Rényi-half effective support is

`K_{1/2}(a_k)=||ahat_k||_1^2<9`

uniformly in `k`. Therefore `f_k(x,y)=x a_k(y)` has `d=1`, variance one, unbounded conditional Fourier support, and `A_{1/2}(f_k)<log_2 9`. The theorem yields a uniform FEI bound on this genuine Boolean family, whereas the previous fixed hard-support hypothesis does not apply.

## Exact tensor guard

For `F(x,y,z)=f(x,y)g(z)` on a fresh block,

`q_R^F=q_R^f tensor p_g`.

Consequently

`K_{1/2}^F(R)=K_{1/2}^f(R) K_{1/2}(g)`

and

`A_{1/2}(F)=A_{1/2}(f)+H_{1/2}(p_g)`.

If `g` has positive spectral entropy then `H_{1/2}(p_g)>0`; repeated arbitrary-core tensor factors force linear growth. A fixed soft-complexity cap therefore excludes the known cyclic-marginal arbitrary-core embedding without assuming FEI.

## Controls and limitations

- Addressing, parity erasure, point defects, near tensors, majority/parity gates, and activation-equivalence examples obey (R1/2).
- The AND family proves the hypothesis is strictly softer than bounded fiber support on genuine Boolean functions.
- The exact tensor law prevents an arbitrary positive-entropy core from hiding behind a fixed marginal.
- Fixed-Rényi point-defect obstructions prevent treating `A_{1/2}` as universally bounded or automatically influence-paid. This theorem does not do so.
- No universal decomposition into bounded-`A_{1/2}` pieces is proved.

## Verification

`verify_renyi_fiber.py` uses exact `Fraction` Walsh transforms. It exhausts all 256 Boolean functions on an `X^2 x Y` cube, verifies normalization and `1<=K_{1/2}<=support` on every positive fiber, checks exact multiplicativity on tensor products, and verifies the AND formula through `k=10`. The analytic Shannon--Rényi inequality supplies the all-dimensional entropy step; the finite checks are controls, not extrapolation.

## Next action

Seek a Boolean-stable estimate that pays `A_{1/2}(f)` by influence or by the granularity deficit on a growing class. It must survive rare point defects and must not admit arbitrary positive-entropy tensor cores. Independent review targets: A088 and A094.

