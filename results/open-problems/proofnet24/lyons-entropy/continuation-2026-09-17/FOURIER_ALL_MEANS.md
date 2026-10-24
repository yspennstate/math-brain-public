# Fourier entropy: all fixed pair means, and joint common-mean motion

17 September 2026. **PARTIAL; unrestricted Lyons conjecture OPEN.** This strengthens the preceding `FOURIER_EXTENSION.md` checkpoint. It is a written restricted proof with exact self-checks, without independent audits or a historical-priority claim. The global three-site quantity `B_Phi` remains UNMEASURED. Model and reasoning settings are not independently exposed by the interface.

## 1. Two complete affine-family theorems

Let `F[j,k]=i^(jk)/2` and

    K(a,b,x,y)=F diag(a+x,b+y,a-x,b-y) F*.

**Theorem A (every fixed pair mean).** Fix any `a,b in [0,1]`. The configuration entropy is jointly concave in `(x,y)` throughout the entire closed rectangle

    |x| <= min(a,1-a),  |y| <= min(b,1-b).

There is no imbalance-sign condition and no upper threshold on either pair mean.

**Theorem B (three affine parameters).** The configuration entropy of `K(t,t,x,y)` is jointly concave in all three variables `(t,x,y)` on the convex contraction domain

    0<=t<=1,  |x|<=min(t,1-t),  |y|<=min(t,1-t).

This permits the diagonal mean to vary simultaneously with both real and imaginary edge components. Thus it strengthens the fixed-mean conclusion proved in the preceding checkpoint. The three-variable Hessian is negative definite at every strict nonscalar member of this family. At `(t,0,0)` it has the quadratic form `-4(dt)^2/[t(1-t)]`, with the two coupling directions flat.

Neither statement asserts concavity for arbitrary simultaneous independent changes of `a,b`. A directional cone for that larger family is given below.

## 2. The exact orbit law

Write `r=x^2`, `s=y^2`, `A=a(1-a)`, `B=b(1-b)`. If `u` and `v` are the count laws of the two spectral Bernoulli pairs, then

    u=((1-a)^2-r, 2(A+r), a^2-r),
    v=((1-b)^2-s, 2(B+s), b^2-s),
    f_k=sum_(i+j=k) u_i v_j.

The exact measured atoms, established by the Fourier minors in X088 and checked independently in `verify_fourier_extension.py`, are:

| Orbit | Size | Each atom |
|---|---:|---:|
| Empty | 1 | f_0 |
| Singletons | 4 | c_1=f_1/4 |
| Adjacent pairs | 4 | P=(u_1v_1+2u_2v_0+2u_0v_2)/8 |
| Opposite pairs | 2 | O=u_1v_1/4 |
| Triples | 4 | c_3=f_3/4 |
| Full | 1 | f_4 |

In particular

    f:=f_2=4P+2O,
    0<O<=2P,
    8(O-P)=2[x^2+y^2-(a-b)^2].                     (1)

All strict contraction atoms are positive. Everything below first takes place in the strict interior.

## 3. Three logarithmic atom ratios

Define

    alpha_0=log[c_1^2/(f_0 P)],
    alpha_1=log[PO/(c_1 c_3)],
    alpha_2=log[c_3^2/(f_4 P)].                     (2)

Each alpha is nonnegative. Indeed the L-ensemble odds matrix is positive definite, and Hadamard-Fischer gives `p_S p_T >= p_(S intersection T) p_(S union T)`. For `alpha_0`, take the two singletons of an adjacent pair. For `alpha_1`, take an adjacent and an opposite pair sharing a vertex. For `alpha_2`, take two triples whose intersection is an adjacent pair.

Let the ordinary count log-concavity ratios be

    L_k=log[f_(k+1)^2/(f_k f_(k+2))],  k=0,1,2.

The exact differences are

    beta_0:=L_0-alpha_0=log(16P/f),
    beta_1:=L_1-alpha_1=log[f^2/(16PO)],
    beta_2:=L_2-alpha_2=log(16P/f).                 (3)

In fact all three beta values are at least `log 2`. For the endpoint ratios this follows from `O<=2P`, hence `f<=8P`. For the middle ratio use

    f^2-32PO=(4P-2O)^2>=0.                        (4)

Consequently

    0<=alpha_k<=L_k.                             (5)

The point is that these are measured-atom logarithms bounded by count logarithms, rather than an assumption that the two entropies coincide.

## 4. Retain the local Shepp-Olkin comparison

Along an arbitrary affine eigenvalue line, define

    g_k=sum_i lambda_i' f_k^(i),
    h_k=sum_(i != j) lambda_i'lambda_j' f_k^(i,j),
    Q_k=g_k^2/f_k-2g_k g_(k+1)/f_(k+1)+g_(k+1)^2/f_(k+2).

Here deletion superscripts have their usual independent-Bernoulli meaning. Then `f_k'=g_(k-1)-g_k`, `f_k''=h_k-2h_(k-1)+h_(k-2)`, and

    I_count:=sum_(k=0)^4 (f_k')^2/f_k
       =g_0^2/f_1+g_3^2/f_3+Q_0+Q_1+Q_2.          (6)

Count log-concavity implies `Q_k>=0`. The all-real-slope local inequality of Hillion and Johnson, Proposition 2.4, equation (6), [arXiv:1503.01570](https://arxiv.org/pdf/1503.01570), implies

    Q_k-h_k L_k>=0  whenever h_k>=0.              (7)

A short derivation from that exact source inequality is given in Section 3 of `FOURIER_EXTENSION.md`. It uses only `2rho log(1/rho)<=1-rho^2` for `0<rho<=1`. The signed slopes here satisfy the source's unrestricted-slope hypotheses.

It follows from (5)-(7), in both sign cases, that

    Q_k-h_k alpha_k>=0.                           (8)

More quantitatively, with `h^+=max(h,0)` and `h^-=max(-h,0)`,

    Q_k-h_k alpha_k >= h_k^+ beta_k+h_k^- alpha_k. (9)

For positive `h_k`, subtract the smaller alpha instead of `L_k` in (7). For negative `h_k`, use `Q_k>=0` and `alpha_k>=0`. No sign restriction on any Bernoulli slope has been imposed.

## 5. The exact remaining acceleration is only 4 a' b'

For a general affine line write

    a'=c, b'=d, x'=u, y'=v,
    lambda'=(c+u,d+v,c-u,d-v).

The crucial polynomial identity is

    2O''+h_1=4cd.                                (10)

For clarity, set `R_a=(1-2a)c+2xu` and `R_b=(1-2b)d+2yv`. Direct differentiation of `O=(A+r)(B+s)` gives

    2O''=4(u^2-c^2)(B+s)+4(v^2-d^2)(A+r)+4R_a R_b.

The within-pair terms of `h_1` are the negatives of the first two terms. Its cross-pair terms are

    8[(a+b-2ab)cd+(2b-1)xu d+(2a-1)yv c-2xyuv].

Adding these expressions cancels every term except `4cd`, proving (10).

The frozen logarithm contribution to negative entropy curvature therefore has the exact expression

    sum_S p_S'' log p_S
       =-sum_(k=0)^2 h_k alpha_k+4cd log(O/P).      (11)

One can check it by comparing the six log coefficients. The coefficients of `log f_0`, `log c_1`, `log c_3`, and `log f_4` agree by the count second-difference identity. The coefficient of `log O` on the right is `-h_1+4cd=2O''`; the coefficient of `log P` follows because `f_2''=4P''+2O''`.

Measured Fisher information dominates count Fisher information by Cauchy-Schwarz within each count layer. Here its excess is explicitly

    I_measured-I_count=8(OP'-PO')^2/(PO f)>=0.       (12)

Combine (6), (8), (11), and (12). The full entropy curvature is exactly

    -H''=(I_measured-I_count)+g_0^2/f_1+g_3^2/f_3
             +sum_(k=0)^2 (Q_k-h_k alpha_k)
             +4cd log(O/P).                       (13)

All terms except the final one are nonnegative. This is an exact identity with the signed atom acceleration retained.

## 6. Proofs and boundary extension

For Theorem A, the pair means are fixed, so `c=d=0`. Equation (13) proves the Hessian inequality everywhere in the strict physical rectangle, regardless of the sign of `O-P`. Integrate it on each interior segment. Approximate boundary means by `(1-epsilon)a+epsilon/2` and `(1-epsilon)b+epsilon/2`, and multiply both endpoint couplings by `1-epsilon`; this places the entire segment strictly inside the contraction domain. Entropy continuity gives the assertion for the original closed rectangle, including degenerate pair means.

For Theorem B, `a=b=t` and `c=d=t'`. Equation (1) gives `O>=P`, so the final term in (13) is `4(t')^2 log(O/P)>=0`. This proves the full three-variable interior Hessian inequality. The physical domain is defined by four affine eigenvalues lying in `[0,1]`, hence is convex. Contract each desired segment toward `(t,x,y)=(1/2,0,0)` and pass to the boundary by continuity.

For strictness off the scalar line, if `t'!=0` then `O>P` supplies a strictly positive last term. If `t'=0` and `(x',y')!=0`, the strictly positive lower bound from Section 5 of `FOURIER_EXTENSION.md` applies. At a scalar kernel the product-law calculation gives `-H''=4(t')^2/[t(1-t)]`, as claimed.

More generally, (13) proves the pointwise entropy Hessian inequality in every direction satisfying

    a'b' log(O/P)>=0,

or equivalently `a'b'[x^2+y^2-(a-b)^2]>=0`. This is a directional assertion; it is not a global convex-domain statement about arbitrary pair-mean motion.

## 7. Precise remaining four-variable problem

Put

    R=(I_measured-I_count)+g_0^2/f_1+g_3^2/f_3
                     +sum_(k=0)^2 (Q_k-h_k alpha_k)>=0.

The full four-eigenvalue Fourier problem is now exactly the question whether

    R >= -4 a'b' log(O/P)                          (14)

in the adverse sign cone. The previously proved theorems cover all other directions. The quantitative lower bound (9) offers a possible payment in (14), but nonnegativity of `R` alone does not prove it. In particular, neither a sign-free extension of (13) nor full ambient Hermitian concavity is claimed.

`verify_fourier_all_means.py` checks (10)-(13) using exact rational polynomial coefficients, exact rational Fisher identities, and outward rational logarithm enclosures at representative directions. All checks are self-checks. The earlier `FOURIER_EXTENSION.md` remains as the original checkpoint and supplies the stronger strictness bound used above.
