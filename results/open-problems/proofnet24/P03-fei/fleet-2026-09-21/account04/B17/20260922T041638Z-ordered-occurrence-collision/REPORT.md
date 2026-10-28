# B17 — ordered-occurrence KL fusion and collision-credit replacement for the balanced FEI remainder

**Run:** `20260922T041638Z-b17-fei-r18`  
**Role:** account04/B17, FEI adversarial constructions / remainder replacement.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / REMAINDER_SHARPENED`; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and scientific sources were read directly, but no installed/native research-brain retrieval or receiver context entered the mathematics.

## 0. What changed


Two newest B15 inputs matter.

1. `account02/B15/20260922T040227Z-balanced-stop-kl-fusion/REPORT.md` (scientific master commit `9f3833b06b5651220251d4d88cd0351b30a97c77`, report blob `dcc4a02a48fb0aefce00d2d3b9fd4ed66aeb90d6`) proves, for every balanced Boolean source, the exact identity

   \[
   H(f)=I H_2(q)+T_{\rm stop}-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix},
   \tag{0.1}
   \]

   where `K=|S|`, `I=E K`, `q_i=Pr(i in S)/I`, and both `K_rho` and `J_mix` are genuine nonnegative KL credits. It also proves `T_stop=O(I-1)` and that the valuation reserve is `O(I-1)`. Its first unpaid implication is the occurrence-entropy remainder after retaining all credits.

2. The newest compatible other-account B15 report is `account01/B15/20260922T0405Z-g10-terminal-atom-feasibility/REPORT.md` (commit `8c6d5f2de7bc6ebe90b6cd611ca14f853af20d8a`, report blob `04e4cb693cd1d3fd6709f3ae27cdb8aa2a067c29`). It proves that the exact G10 stopping corridor is compatible with one `Gamma(1/4)` iff the center `C=Gamma(1/2)` exceeds the balanced G10 ratio, with allowed interval

   \[
   T(C)\le \Gamma(1/4)\le C-2.
   \tag{0.2}
   \]

   Thus that local remainder survives once its terminal continuation is kept; the correct adversarial question is whether the remaining shape interval can be sharpened without throwing away a true credit.

This run gives two exact answers: (i) the upper face `Gamma(1/4)<=C-2` has **no uniform positive safety gap**, by a Boolean AND-suspension construction; and (ii) all three B15 information credits plus the unused stop-hazard slack fuse into one ordered-occurrence KL, which admits a new collision/without-replacement data-processing lower bound. The latter is the replacement remainder.

## 1. Exact Boolean adversary: AND-suspension makes the quarter-bias face sharp

Let `h:{-1,1}^n->{-1,1}` be balanced and let `Y` be a fresh uniform sign. Interpret `h` and `Y` as Boolean bits and form their AND. In sign notation the resulting gate is

\[
F(Y,x)=\frac{1+Y+h(x)-Yh(x)}2.
\tag{1.1}
\]

It is an actual Boolean function with output bias `1/4`. Because `h` is balanced, the four Fourier blocks in (1.1) are disjoint. If `p_S=\hat h(S)^2`, the spectrum of `F` consists of masses `1/4` at `emptyset` and `{Y}`, and two copies of `p_S/4` for each nonzero Fourier set of `h`. Therefore, exactly,

\[
\boxed{H(F)=2+\frac12 H(h)},\qquad
\boxed{I(F)=\frac{1+I(h)}2}.
\tag{1.2}
\]

At uniform input biases, writing

\[
C=\Gamma(1/2),\qquad g=\Gamma(1/4),\qquad
R(h)=\frac{H(h)}{I(h)-1},
\]

the all-gate defect of the suspended gate is

\[
\boxed{
D_\Gamma(F)
=(C-g-2)+\frac{I(h)-1}{2}\,[C-R(h)].
}
\tag{1.3}
\]

The binary AND atom itself gives `g<=C-2`. Formula (1.3) proves that this upper face cannot be uniformly strengthened to `g<=C-2-epsilon`: at a center approached by balanced hard cores, their AND suspensions approach equality on the same quarter-bias face. In particular, the newest G10 B15 interval cannot be closed by claiming a hidden positive terminal-AND gap. Any incompatibility has to come from a different bias value, a different prime-gate lower constraint, or a higher center obstruction.

This construction preserves Boolean realizability exactly; it is not a spectral relaxation.

## 2. New exact fusion: one ordered-occurrence KL contains every B15 credit

Now let `f` be any balanced Boolean function and sample a Fourier set `S` from its actual squared Walsh spectrum `p_S`. Put

\[
K=|S|\ge1,\quad W_k=\Pr(K=k),\quad I=\mathbb E K,\quad
j_i=\Pr(i\in S),\quad q_i=\frac{j_i}{I}.
\tag{2.1}
\]

Conditional on `K=k`, uniformly order the coordinates of `S` and call the resulting ordered distinct tuple `(X_1,...,X_k)`. Let `P_k` be its law. Thus, for an ordering `x` of a set `S` of size `k`,

\[
P_k(x)=\frac{p_S}{W_k k!}.
\tag{2.2}
\]

Define the genuine ordered-occurrence divergence

\[
\boxed{
\mathcal D_{\rm ord}
:=\sum_{k\ge1} W_k D_2(P_k\|q^{\otimes k}).
}
\tag{2.3}
\]

A direct expansion gives

\[
\begin{aligned}
\mathcal D_{\rm ord}
&=\sum_S p_S\log_2 p_S
 -\sum_k W_k\log_2 W_k
 -\mathbb E\log_2(K!)
 -\sum_i j_i\log_2 q_i\\
&=\boxed{I H_2(q)+H_2(K)-H(f)-\mathbb E\log_2(K!)}.
\end{aligned}
\tag{2.4}
\]

Equivalently,

\[
\boxed{
H(f)=I H_2(q)+H_2(K)-\mathbb E\log_2(K!)-\mathcal D_{\rm ord}.
}
\tag{2.5}
\]

Comparing (2.5) to the exact newest B15 identity (0.1) yields the exact credit fusion

\[
\boxed{
\mathcal D_{\rm ord}
=H_2(K)-T_{\rm stop}+\mathcal K_\rho+\mathcal J_{\rm mix}.
}
\tag{2.6}
\]

Thus this is not a credit-dropping rewrite. It retains the prefix-history KL, the root/deletion mixing KL, and also captures the nonnegative stop-hazard slack `H(K)-T_stop`. It is a single physical information quantity generated by the actual Boolean spectral source.

## 3. Collision/without-replacement data processing

Let

\[
e_k(q)=\sum_{|A|=k}\prod_{i\in A}q_i
\tag{3.1}
\]

be the `k`th elementary symmetric polynomial of the occurrence law. Under `q^{\otimes k}`, the probability that all `k` sampled coordinates are distinct is

\[
\Pr_{q^{\otimes k}}(\text{distinct})=k!e_k(q).
\tag{3.2}
\]

Under `P_k` that event has probability one. Data processing of KL under the indicator of the distinctness event therefore gives, exactly,

\[
\boxed{
D_2(P_k\|q^{\otimes k})\ge -\log_2(k!e_k(q)).
}
\tag{3.3}
\]

Substituting (3.3) into (2.5) cancels the factorial term and proves the new universal Boolean-source upper bound

\[
\boxed{
H(f)\le H_2(K)+\mathcal C_{\rm coll}(f),
\qquad
\mathcal C_{\rm coll}(f):=I H_2(q)+\mathbb E\log_2 e_K(q).
}
\tag{3.4}
\]

The newest B15 report already proves `H(K)=O(I-1)` for balanced Boolean sources. Therefore the remaining sufficient implication can be sharpened to the single collision remainder

\[
\boxed{
\mathcal C_{\rm coll}(f)\le C_{\rm coll}[I(f)-1]
\quad\text{for every balanced Boolean }f.
}
\tag{3.5}
\]

Any finite constant in (3.5), together with the already-paid stopping entropy, proves a finite dimension-independent FEI constant through the balanced-support-deficit equivalence. I do **not** prove (3.5) universally in this run. The advance is that (3.5) is a strictly more compressed, credit-preserving target: it depends only on the actual occurrence profile `q` and actual level `K`, while the three negative B15 credits are not discarded but are lower-bounded by a bona-fide without-replacement information cost.

## 4. Adversarial tests and boundary checks

### 4.1 Exact addressing family: coefficient below four is impossible

For the standard balanced `m`-address-bit addressing function with `2^m` data bits, its Fourier law has exactly one data coordinate and a uniformly random subset of the `m` address coordinates. Hence

\[
K=1+\operatorname{Bin}(m,1/2),\qquad
I=1+\frac m2,\qquad
H=2m,
\tag{4.1}
\]

and therefore

\[
\frac{H}{I-1}=4
\tag{4.2}
\]

exactly. Its occurrence profile is also exact:

\[
q_{\rm address}=\frac1{m+2},\qquad
q_{\rm data}=\frac{2^{1-m}}{m+2}.
\tag{4.3}
\]

Because (3.4) implies

\[
\mathcal C_{\rm coll}\ge H-H(K),
\]

and `H(K)<=log_2(m+1)`, this family forces

\[
\liminf_{m\to\infty}
\frac{\mathcal C_{\rm coll}}{I-1}\ge4.
\tag{4.4}
\]

So if (3.5) is true, its best possible constant is at least `4`. The exact checker evaluates the closed finite sum for `m=1,...,10`; the observed ratios increase from `3.169925...` to `3.787224725...`, with no violation of the natural coefficient-four candidate. This is evidence only; the universal `<=4` statement remains a conjectural next target.

### 4.2 Exhaustive actual-Boolean test through four variables

A standard-library checker enumerates every balanced Boolean truth table through dimension four, modulo global sign: `1+3+35+6435=6474` functions. For each, it independently constructs the Walsh spectrum, the ordered-occurrence KL in (2.3), the elementary-symmetric collision bound (3.3), and the AND suspension (1.1). It finds:

- maximum numerical residual in the ordered-KL identity below `2e-11` bits;
- all `6474` suspension entropy/influence identities pass;
- maximum observed `C_coll/(I-1)` is `3.977663610152280`;
- the same sweep contains a true entropy ratio `H/(I-1)=6`, illustrating that the paid `H(K)` term is genuinely needed and must not be silently dropped.

This finite sweep is a falsification check, not a proof of (3.5).

### 4.3 Booleanity is essential: a non-Boolean relaxation blows up

If one forgets Boolean realizability and merely takes `S` uniformly from the `2`-subsets of `[n]`, then `K=2`, `I-1=1`, `q` is uniform, and

\[
\mathcal C_{\rm coll}
=\log_2\binom n2,
\tag{4.5}
\]

which is unbounded. Thus (3.5) cannot be a theorem about arbitrary subset laws. The exact Boolean convolution constraints are essential.

For a concrete realizability failure, already at `n=3` the law uniform on `{12,13,23}` cannot be the squared spectrum of a Boolean function with any choices of coefficient signs: the Boolean convolution equation at `U={1,2}` contains exactly

\[
2\widehat f(13)\widehat f(23)=\pm\frac23\ne0.
\tag{4.6}
\]

This is the required boundary check against accidentally proving a non-Boolean relaxation.

## 5. Status and next obligation

**Proved in this run:** the exact AND-suspension identities (1.2)-(1.3); the ordered-occurrence KL identity (2.4)-(2.6); the collision data-processing bound (3.3)-(3.4); and the non-Boolean level-two obstruction (4.5)-(4.6).

**Not proved:** a universal finite constant in (3.5), coefficient four in (3.5), a universal `Gamma`, or full FEI.

The clean next adversarial obligation is now precise: attack

\[
\mathcal C_{\rm coll}(f)
=I H_2(q)+\mathbb E\log_2 e_K(q)
\stackrel{?}{\le} C[I(f)-1]
\tag{5.1}
\]

on actual balanced Boolean functions, not arbitrary subset laws. An exact Boolean counterexample with unbounded ratio would kill this replacement. If it survives the known hard families, the next proof step should derive (5.1) from Boolean convolution/degree structure rather than reintroducing separately paid root/deletion labels. The addressing family shows that any coefficient below four is impossible.

## 6. Verification artifact

`CHECKER.py` is standard-library only and reconstructs every finite object from truth tables or closed exact rational formulas. Executed-byte SHA-256:

`4cb7d635115abb438090edb43679683eaf60d18d55a93ffc8a3bd4a90cd5b3a2`.

Captured-output SHA-256:

`2c8758263f5823638f82e0516684daed7680e4ce2775a476a49ff5f0e814f23c`.

The checker is self-check/falsification evidence. Independent peer review is still required before promotion of the new universal identities beyond self-checked status.
