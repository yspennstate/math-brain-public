SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B03, 2026-09-24T11:15:23Z.
attacking: the first gap in account01/B03 r43 — retain arbitrary deterministic cross-couplings from the twisted hyperbolic pair into the physical slope hub by inserting the pair amplitude inside the hub Plancherel transform.

# Pair-to-hub cross-coupling compiler

## Status

**NEW SUPPORTING THEOREM / NEW STRICT FULL-TARGET CHAMBER / COMPLETED ACCOUNT01/B03 RESULT APPLIED AT AN ACTUAL INEQUALITY / FULL QFORM OPEN.**

The unrestricted universal bounded-density conjecture remains open. This report proves a new product-coordinate branch with a continuous (C_0) density and an explicit linear small-ball estimate. Continuity is asserted only in this branch.

No pointwise law-uniform quadratic decay, post-rotation independence, arbitrary-joint coarea estimate, conditional projection-density cap, or separation of dependent sum/difference coordinates is used.

## 1. Input from the completed account01/B03 theorem

The newest completed account01/B03 theorem used here is commit
`c1cf228922430b7ced03008f8aa1b5aa41032a08`,
`QFORM-B03-TWISTED-PAIR-SLOPE-HUB-v1`.

Its pair estimate, equation (3.10), says that if (R,V) are independent with density caps (L,N), (eta
e0), and
[
T=F(R)+2eta RV+cV^2+dV,
]
where (F) may depend arbitrarily on (R), then
[
 |phi_T(t)|^2le min!left{1,rac{pi LN}{|eta|,|t|}ight}.
 	ag{1.1}
]
The estimate is uniform in (F,c,d). That uniformity is the exact feature used below.

## 2. Main theorem

### Theorem `QFORM-B03-PAIR-IN-HUB-PLANCHEREL-v1`

Let (kge2). Let (R,V,U_1,dots,U_k) be mutually independent real variables. Assume (R,V) have density caps (L,N), and each (U_j) has density cap one. Put (U=(U_1,dots,U_k)).

Let (Y) be independent of ((R,V,U)), and suppose the random vector (ell(Y)inmathbb R^k) has a marginal Lebesgue density bounded by (K). No independence among the coordinates of (ell(Y)), and no independence between (ell(Y)) and (H(Y)), is assumed.

Fix a symmetric (k	imes k) matrix (C), vectors (a,binmathbb R^k), constants (eta
e0,c,dinmathbb R), an arbitrary measurable (F:mathbb R	omathbb R), and an arbitrary measurable (H). Define
[
egin{aligned}
Q={}&F(R)+2eta RV+cV^2+dV\
&+U^TCU+2R,a^TU+2V,b^TU\
&+2U^Tell(Y)+H(Y).
end{aligned}
	ag{2.1}
]
Set
[
D=k+1,qquad alpha=rac{LNK}{|eta|}.
	ag{2.2}
]
Then, for every (t
e0),
[
oxed{
 |phi_Q(t)|^2
 le min{1,pi^Dalpha |t|^{-D}}.
}
	ag{2.3}
]
Consequently,
[
oxed{
 |p_Q|_inftyle rac{D}{D-2}alpha^{1/D},
 qquad
 Pr(Qin I)le rac{D}{D-2}alpha^{1/D}|I|.
}
	ag{2.4}
]
Moreover (p_Qin C_0(mathbb R)). In the critical case (k=2),
[
oxed{
 |p_Q|_inftyle
 3left(rac{LNK}{|eta|}ight)^{1/3}.
}
	ag{2.5}
]

The whole-output negative-half collision integral also obeys
[
oxed{
 int_{mathbb R}|t|^{-1/2}|phi_Q(t)|^2,dt
 le rac{8D}{2D-1}sqrt{pi},
      alpha^{1/(2D)}.
}
	ag{2.6}
]

### Proof

For fixed (uinmathbb R^k), define the twisted pair amplitude
[
A_t(u)=mathbb E_{R,V}exp! left(itleft[
 F(R)+2eta RV+cV^2+dV
 +2R,a^Tu+2V,b^Tuight]ight).
	ag{2.7}
]
Apply account01/B03 equation (1.1) with
[
F_u(R)=F(R)+2R,a^Tu,qquad d_u=d+2b^Tu.
]
Its uniformity gives the actual inequality
[
oxed{
 |A_t(u)|^2le
 min!left{1,rac{pi LN}{|eta|,|t|}ight}
 quad	ext{for every }u.
}
	ag{2.8}
]
Thus the pair-to-hub cross-couplings have not been discarded; they have become a uniformly bounded multiplier in the original physical (U)-variables.

Let (g(u)=prod_{j=1}^k f_j(u_j)), and define
[
B_t(z)=int_{mathbb R^k}
 g(u)A_t(u)
 e^{it u^TCu}e^{i2t u^Tz},du.
	ag{2.9}
]
Independence of the original source blocks gives
[
phi_Q(t)=
mathbb E_Y!left[e^{itH(Y)}B_t(ell(Y))ight].
	ag{2.10}
]
Cauchy--Schwarz is used only on this final marginal (Y)-average:
[
|phi_Q(t)|^2
le mathbb E|B_t(ell(Y))|^2
le Kint_{mathbb R^k}|B_t(z)|^2,dz.
	ag{2.11}
]
No conditional density of (ell(Y)) given (H(Y)) is formed.

Plancherel in the genuine physical hub gives
[
int_{mathbb R^k}|B_t(z)|^2,dz
=pi^k|t|^{-k}
 int_{mathbb R^k}g(u)^2|A_t(u)|^2,du.
	ag{2.12}
]
Since (0le f_jle1) and (int f_j=1),
[
int g^2=prod_jint f_j^2le1.
	ag{2.13}
]
Combining (2.8)--(2.13),
[
|phi_Q(t)|^2
le Kpi^k|t|^{-k}
 min!left{1,rac{pi LN}{|eta|,|t|}ight}
le pi^Dalpha |t|^{-D}.
	ag{2.14}
]
Together with (|phi_Q|le1), this proves (2.3).

Writing (T_0=pialpha^{1/D}), direct integration yields
[
int_{mathbb R}|phi_Q(t)|,dt
le 2pirac{D}{D-2}alpha^{1/D}.
	ag{2.15}
]
Fourier inversion proves (p_Qin C_0) and (2.4). Similarly, splitting the integral in (2.6) at (T_0) gives
[
2int_0^{T_0}t^{-1/2}dt
+2pi^Dalphaint_{T_0}^infty t^{-D-1/2}dt
=rac{8D}{2D-1}sqrt{pi}alpha^{1/(2D)}.
]
This proves (2.6). QED.

## 3. A strict full-target example

Let
[
R,V,U_1,U_2,Y_1,Y_2
]
be six independent cap-one real variables, and set
[
oxed{
Q_*=2RV+2RU_1+2VU_2+2U_1Y_1+2U_2Y_2.
}
	ag{3.1}
]
This is (2.1) with
[
k=2,quad eta=1,quad
a=(1,0),quad b=(0,1),quad
ell(Y)=(Y_1,Y_2),
]
so (L,N,Kle1). Therefore
[
oxed{
 |p_{Q_*}|_inftyle3,qquad
 Pr(Q_*in I)le3|I|,
 qquad p_{Q_*}in C_0.
}
	ag{3.2}
]

In the coordinate order
[
Y_1-U_1-R-V-U_2-Y_2,
]
the coefficient matrix is the adjacency matrix of the path (P_6). Its eigenvalues are
[
2cos(jpi/7),qquad j=1,dots,6,
	ag{3.3}
]
so four eigenvalues have absolute value greater than one. Hence (3.1) is a strict instance of the owner's full spectral target. Unlike the preceding account01/B03 r43 example, both ends of the central hyperbolic pair couple directly and quadratically into the physical hub.

## 4. Dependence audit and remaining gap

The proof never decomposes coordinatewise independent-copy sums and differences. The identity
[
|phi_Q(t)|^2=mathbb E e^{it(Q-Q')}
]
is used only at the whole-output level in interpreting (2.6).

The theorem closes deterministic pair-to-hub cross-couplings. The remaining analytic obstruction is **environment-dependent** pair-to-hub coupling or pair twisting correlated with the slope vector (ell(Y)). In that case the multiplier (A_{t,Y}(u)) varies with the same (Y) whose marginal slope is used in (2.11), and marginal Plancherel no longer applies without a conditional density hypothesis. The next mechanism must either produce a joint operator estimate in ((u,Y)) or structurally extract a source split before conditioning.

The unrestricted universal bounded-density conjecture remains **OPEN**. Unrestricted continuity remains **OPEN**.

## 5. Source ledger

Fresh source checked: account01/B03 r43 at `c1cf228922430b7ced03008f8aa1b5aa41032a08`, with deterministic checks at `d25cba9a25e9547d84df656758d71ba8fd5fa175`. Standing Claude-review corrections and owner control remain in force. No task, schedule, notification, permission, authentication, workflow, or production-store state was changed.
