SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T00:50:45Z.
attacking: a zero-diagonal physical hyperbola plus aggregate residual two-volume, with the whole-copy time estimate kept dependence-safe and the hyperbola coefficient cancelled against a fourth-order Schur/Cauchy-Binet volume.

# Early calculation: half-Riesz hyperbola peel and fourth-order cancellation

Status: substantive calculation in progress; full QFORM remains OPEN.

Let U,V be independent real variables with densities f,g<=1. For w!=0 the product W=UV has density

k_W(w)=integral_R f(u)g(w/u) du/|u|.

Split at |u|=sqrt(|w|). On |u|>=sqrt(|w|), use g<=1 and int f=1 to get <=|w|^(-1/2). On |u|<sqrt(|w|), substitute v=w/u; then |v|>sqrt(|w|), and use f<=1 and int g=1 to get the same bound. Hence

k_W(w)<=2|w|^(-1/2).

Therefore for mu!=0,

p_{2mu UV}(y)<=sqrt(2)|mu|^(-1/2)|y|^(-1/2).

The same statement is uniform under arbitrary shifts of U,V. Consequently, if W0 is an arbitrary background independent of U,V and

Q=2mu(U+a(W0))(V+b(W0))+S(W0),

then mixture of the conditional densities gives

||p_Q||_infinity <= sqrt(2)|mu|^(-1/2) H_{1/2}(S),
H_{1/2}(S):=sup_s E|S-s|^(-1/2).

Apply account01/B03 r30, QFORM-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1, to a physical cut of S with

Z2=e2(MM^T)>0.

That theorem gives both the dependence-safe whole-copy estimate

int |t|^(-1/2)|phi_S(t)|^2 dt
 <= (16/3)sqrt(2pi)(2e)^(1/4) Z2^(-1/8)

and the translation-uniform one-copy half-Riesz estimate

H_{1/2}(S)<=8(2e)^(1/4) Z2^(-1/8).

Hence

||p_Q||_infinity
 <= 8sqrt(2)(2e)^(1/4)|mu|^(-1/2) Z2^(-1/8)
 =17.275717919798065... |mu|^(-1/2) Z2^(-1/8).

Now let H={h1,h2} be a genuine physical pair of a symmetric A with A_h1h1=A_h2h2=0 and A_h1h2=mu!=0. Let S_A be the Schur complement on K=H^c. Define the ordered disjoint fourth-order overlap mass

F4(H)=sum_{I,J subset K, |I|=|J|=2, I cap J=empty} det A_{H union I, H union J}^2.

Since det A_HH=-mu^2, the block determinant identity gives

det A_{H union I,H union J}=(-mu^2) det (S_A)_{I,J},

so F4(H)=mu^4 E0_2(S_A), where E0_2 is the sum of squared disjoint 2x2 minors of S_A. For a uniformly random original-coordinate cut L|R of K,

E Z2((S_A)_{L,R})=E0_2(S_A)/16=F4(H)/(16mu^4).

Thus some cut has Z2>=F4(H)/(16mu^4), and the preceding density bound cancels mu exactly:

||p_Q||_infinity
 <=16(2e)^(1/4) F4(H)^(-1/8)
 =24.43155458191034... F4(H)^(-1/8).

The corresponding residual whole-copy time estimate on that cut is

int |t|^(-1/2)|phi_S(t)|^2 dt
 <= (16sqrt(2)/3)sqrt(2pi)(2e)^(1/4)|mu|^(1/2)F4(H)^(-1/8)
 =28.869202001543517... |mu|^(1/2)F4(H)^(-1/8).

This is a new aggregate-before-inversion branch: a small physical hyperbola coefficient is harmless if the associated disjoint fourth-order Schur volume stays at universal scale. Continuity is not claimed.
