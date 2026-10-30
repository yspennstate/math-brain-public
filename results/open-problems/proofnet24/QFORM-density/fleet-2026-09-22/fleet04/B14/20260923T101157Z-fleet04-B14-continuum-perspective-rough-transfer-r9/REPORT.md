SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B14, 2026-09-23T10:11:57Z.
attacking: measurable affine-fiber localization and zero-loss rough-product transfer.

# B14 — continuum perspective localization and cap-preserving rough transfer

## Status

Proved supporting localization and approximation theorems. Full QFORM remains open. Continuity is separate.

## 1. Partner actually applied

This report applies fleet01/B14 r33, commit `669ed75ada3772bcc3d6deba5bdf87aa284f23f7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B14/20260923T091621Z-fleet01-B14-QFORM-r33/REPORT.md`, blob `8402e5a3f4f0b01dc087bcba536b17c2573781ad`.

Write
[
c_E={1over2sin^2(1/2)}
]
and
[
Omega(y)=
egin{cases}
c_Ey(2+log(1/y)),&0<yle1,\
log y+2c_E,&yge1.
end{cases}
]
The partner proves that (Omega) is increasing and concave, and that a probability law (mu) satisfying
[
|widehatmu(t)|lemin{1,K/|t|}
]
obeys
[
sup_xintlog_+{Aover|x-r|},dmu(r)leOmega(AK).
]
It also proves the physical-pair compiler
[
|p_Q|_infty
leinf_{y>0}left{
4sqrt{Koverkappa y}+D^{-1/2}Omega(y)
ight},
]
where (D=|det B|) and (kappa=s_{min}(B)) for the actual indefinite physical pair.

## 2. Arbitrary measurable affine-fiber compiler

### Theorem 2.1

Let ((Theta,pi)) be any probability space and let (mu_	heta) be a measurable probability kernel on (mathbb R). Assume that for almost every (	heta)
[
|widehat{mu_	heta}(t)|
lemin{1,K(	heta)/|t|},
qquad t
e0,
]
where (K:Theta	o[0,infty]) is measurable and
[
overline K:=int K(	heta),dpi(	heta)<infty.
]
Let
[
mu=intmu_	heta,dpi(	heta).
]
Then, for every (A>0),
[
oxed{
sup_xintlog_+{Aover|x-r|},dmu(r)
leOmega(Aoverline K).
}
]

This remains true if each conditional law is translated by an arbitrary measurable (b(	heta)). It also remains true for subprobability disintegrations after using the unnormalized perspective (mOmega(AK/m)).

### Proof

For each fixed (x), Tonelli and the partner theorem give
[
intlog_+{Aover|x-r|},dmu(r)
=
int_Thetaleft[
intlog_+{Aover|x-r|},dmu_	heta(r)
ight]dpi(	heta)
le
int_ThetaOmega(AK(	heta)),dpi(	heta).
]
Concavity of (Omega) and Jensen yield
[
int_ThetaOmega(AK(	heta)),dpi(	heta)
leOmegaleft(Aint K,dpiight).
]
Taking the supremum over (x) proves the claim. A translation multiplies the conditional Fourier transform by a unimodular phase and therefore changes neither the hypothesis nor the bound.

No countable partition, attained extremal fiber, support diameter, moment, or worst normalized fiber constant is used.

## 3. Physical-pair consequence with averaged critical cost

Under the actual physical-pair hypotheses of the partner theorem, if the remainder law is the above measurable mixture, then
[
oxed{
|p_Q|_infty
le
inf_{y>0}
left{
4sqrt{overline Koverkappa y}
+D^{-1/2}Omega(y)
ight}.
}
]
Thus conditioning-generated affine terms and arbitrary remote outside fibers are paid by the averaged unnormalized budget (overline K), not by (operatorname*{ess,sup}K(	heta)).

For the target-valid family in fleet01/B14 r33,
[
Q_{m,gamma}
=2U_1U_2+(a_m^TV)^2+(b_m^TV)^2
+2gamma(c_m^TV)Z,
]
the conditional rank-two bank estimate has (K(	heta)=4pi) for every outside realization, while (D=kappa=P=1). The continuum theorem therefore applies to any measurable disintegration of the law of (Z), including uncountably many fibers, and the partner’s optimized inequality gives
[
oxed{
|p_{Q_{m,gamma}}|_infty
le
2+sin(1/2)^{-2}+log(16pi)
<10.269.
}
]
This holds uniformly in (mge2), (gammainmathbb R), arbitrary fragmented or unbounded cap-one product laws, all fiber translations, and with no moment assumptions.

## 4. Cap-preserving approximation without renormalization

### Theorem 4.1

Let (f) be any probability density on (mathbb R) with (0le fle1). There exist compactly supported smooth probability densities (f_R) with (0le f_Rle1) and
[
|f_R-f|_1	o0.
]

### Proof

Let
[
m_R=int_{-R}^R f(x),dx.
]
Choose an interval (J_R) of length (1-m_R), disjoint from ([-R,R]), and set
[
g_R=f,1_{[-R,R]}+1_{J_R}.
]
Then (g_R) has mass one, (0le g_Rle1), compact support, and
[
|g_R-f|_1le2(1-m_R)	o0.
]
Let (ho_arepsilon) be a smooth compactly supported probability kernel and put
[
f_R=g_R*ho_{arepsilon_R},
]
with (arepsilon_Rdownarrow0) chosen so that
(|g_R*ho_{arepsilon_R}-g_R|_1le1/R).
Convolution preserves mass and the (L^infty) cap, so (f_R) has all asserted properties.

### Product and polynomial transfer

For independent coordinates with densities (f_i), approximate each (f_i) as above. For fixed finite (n),
[
left|igotimes_i f_{i,R}-igotimes_i f_iight|_{m TV}
le {1over2}sum_i|f_{i,R}-f_i|_1	o0.
]
Pushforward under any measurable polynomial (Q) contracts total variation. Hence every uniform interval estimate
[
Pr{Q(X^{(R)})in I}le C|I|
]
passes with exactly the same constant to the original rough product law. This argument does not evaluate an arbitrary density version on a level surface and has no interval-boundary issue.

The same proof works uniformly for affine families
[
x^TBx+ell(	heta)^Tx+r(	heta)
]
because the total-variation comparison is performed before the polynomial pushforward.

## 5. What this closes and what remains

The combination of Theorems 2.1 and 4.1 gives a zero-loss route:

1. prove the geometric or Fourier estimate for smooth compact cap-one inputs;
2. retain each outside fiber as an unnormalized measure;
3. average its critical budget before applying the concave logarithmic compiler;
4. pass to arbitrary fragmented and unbounded product laws in total variation.

The remaining full-target obstruction is structural, not measure-theoretic: the bare condition (s_3(A)ge1) still must yield either an actual paid physical pair plus a remainder with finite averaged critical budget, or another paid physical certificate. Kernel leakage remains explicit; this result does not translate away a kernel component or treat a dense quadratic remainder as a small random error.

## Pins

- Assignment card blob: `46b1d3db2ffb7759153a7209cd4cc34071e8c362`.
- Request blob: `165c570ecb4dcc6299c38fc3298771e4a8339dac`.
- Memory protocol blob: `0d902d56688f4b5c575f5b921ddf9f6709e88312`.
- Latest observed brain main before publication: `630fe0329adf06d7b587064b2c763befb4e9d0bf`.
- Status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.
