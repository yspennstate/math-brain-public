# fleet01 / B12 — QFORM additional-eigenvalue control

Run: `20260923T124910Z-fleet01-B12-QFORM-auto11-r2`

Status: **PROVED_SUPPORTING_STABILITY_FULL_TARGET_OPEN**

Native-brain status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval/writeback is not native learned-memory ingestion.

## Exact programme target

For independent real random variables `X_i` with densities `0<=f_i<=1`, and real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal density bound for `Q=X^TAX`, or give a counterexample. The theorem below is a supporting stability result. It never rotates the independent input coordinates and never treats a quadratic remainder as an independent convolution.

## New theorem: QFORM-BILATERAL-ABSOLUTE-ENERGY-NUCLEAR-TAIL-v1

Let `E=E^T` be any real symmetric matrix and let `I,J` be disjoint sets of ORIGINAL coordinates. Put

`R=E[I,J]`.

Write the spectral decomposition

`E=V Theta V^T`,

with orthonormal columns in `V`, and define `|E|=V|Theta|V^T`. Define the physical absolute spectral energies

`a_I(E)=tr(P_I |E| P_I)=sum_k |theta_k| ||P_I v_k||_2^2`,

`a_J(E)=tr(P_J |E| P_J)=sum_k |theta_k| ||P_J v_k||_2^2`.

Then

`boxed: ||R||_{S_1} <= sqrt(a_I(E) a_J(E)).`                              (1)

Consequently, for every integer `p>=0`,

`boxed: s_{p+1}(R) <= sqrt(a_I(E)a_J(E))/(p+1).`                           (2)

This is a linear-in-reserve tail dilution. Signs of all eigenvalues of `E` are irrelevant, and globally huge eigenvalues are inexpensive whenever their weighted physical mass is small on at least one of the two banks.

### Proof of (1)

Set

`C_I=P_I V |Theta|^(1/2)`, `C_J=P_J V |Theta|^(1/2)`,

and let `S=sgn(Theta)`, so `||S||op<=1`. Then exactly

`R=C_I S C_J^T`.

Schatten Hölder gives

`||C_I S C_J^T||_{S_1} <= ||C_I||_{S_2} ||S C_J^T||_{S_2}
                         <= ||C_I||_F ||C_J||_F`.

But

`||C_I||_F^2=tr(P_I|E|P_I)=a_I(E)`,

and similarly for `J`. This proves (1). Since

`(p+1)s_{p+1}(R) <= sum_{j=1}^{p+1}s_j(R) <= ||R||_{S_1}`,

(2) follows.

### Sharpness

The constant in (2) is sharp for every `p`. Take `|I|=|J|=p+1` and

`E=[[0,d I],[d I,0]]`, `d>0`.

Then `|E|=d I`, hence

`a_I(E)=a_J(E)=(p+1)d`,

while `R=dI` and `s_{p+1}(R)=d`. Equality holds in (2).

## Profile refinement

Let the eigenvalues of the positive semidefinite compressions

`G_I=P_I|E|P_I`, `G_J=P_J|E|P_J`

be decreasing:

`mu^I_1>=mu^I_2>=...`, `mu^J_1>=mu^J_2>=...`.

Then for every `p>=0`,

`boxed: s_{p+1}(R) <= min_{a+b=p+2} sqrt(mu^I_a mu^J_b).`                 (3)

Proof: factor `R=C_I S C_J^T`. For fixed `a,b`, let `C_I^{(a-1)}` and `(SC_J^T)^{(b-1)}` be best rank-`a-1` and rank-`b-1` operator-norm approximations. The matrix

`C_I^{(a-1)}SC_J^T + (C_I-C_I^{(a-1)})(SC_J^T)^{(b-1)}`

has rank at most `a+b-2=p`, and the residual equals

`(C_I-C_I^{(a-1)})(SC_J^T-(SC_J^T)^{(b-1)})`,

whose norm is at most

`s_a(C_I)s_b(C_J)=sqrt(mu^I_a mu^J_b)`.

Eckart--Young gives (3). Thus one may replace the right side of (2) by the minimum of the nuclear-energy bound and the profile bound.

## Compiler with the completed fleet02/B12 reserve theorem

Let the ACTUAL final original-coordinate cross block have the decomposition

`M_final=M_0+L+R+T`,

where

`M_0=A_0[I,J]`, `rank L<=r`, `R=E[I,J]`, `||T||op<=delta`.

The completed partner theorem `QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1` from fleet02/B12 states, for `q+r<=d=min(|I|,|J|)`,

`s_q(M_final) >= max_{0<=p<=d-r-q}[s_{q+r+p}(M_0)-s_{p+1}(R)]-delta.`

Combining it with (2), define

`Gamma_q = max_{0<=p<=d-r-q} [s_{q+r+p}(M_0)
           -sqrt(a_I(E)a_J(E))/(p+1)]-delta`.                              (4)

Then

`boxed: s_q(M_final)>=Gamma_q.`                                            (5)

The arbitrary-magnitude packet `L` costs only rank; the residual signed spectral cloud `E` is charged by a product of its two physical absolute energies, divided linearly by reserve depth; and the fully nonseparable dense tail `T` is paid only at the matrix level through `delta`.

For the density problem take `q=5`. If `Gamma_5>0`, the completed D5 theorem on the ACTUAL original-coordinate cross block gives a continuous density and

`boxed: ||p_{X^T A X}||_infinity <= 5 sqrt(2e)/Gamma_5.`                  (6)

Same-bank curvature, outside couplings and affine terms are unrestricted by the D5 receiver.

### Fixed-reserve corollary

If `s_N(M_0)>=kappa` for some `N>=r+5`, choose `p=N-r-5`. Then

`boxed: s_5(M_final) >= kappa-delta
        -sqrt(a_I(E)a_J(E))/(N-r-4).`                                      (7)

Whenever the right side is positive, substitute it into (6).

This is complementary to the partner's Frobenius dilution `||R||F/sqrt(N-r-4)`: (7) can be much smaller when large global eigenvalues carry little absolute spectral mass on one physical bank. It is also sharp from only `(a_I,a_J,p)` by the block-off-diagonal equality example above.

## Threshold form: smaller and larger added eigenvalues

Suppose an added spectral cloud is split into a chosen large packet `S_G` and a residual packet

`E=sum_{k in B} theta_k v_k v_k^T`.

If `rank(S_G[I,J])<=r`, every magnitude and sign in `S_G` disappears from (4). If additionally `|theta_k|<=h` on the residual packet, put

`lambda_I=sum_{k in B}||P_Iv_k||^2`, `lambda_J=sum_{k in B}||P_Jv_k||^2`.

Then

`a_I(E)<=h lambda_I`, `a_J(E)<=h lambda_J`,

so

`s_{p+1}(E[I,J]) <= h sqrt(lambda_I lambda_J)/(p+1)`.                     (8)

Thus arbitrarily many smaller eigenvalues of either sign can be diluted by reserve depth and physical footprint, while arbitrarily large modes of either sign are free whenever their physical cross footprint has low rank.

## Actual partner application: one unbounded packet + 59 independently signed residual replacements + dense noise

Take two original-coordinate banks `I,J`, each of size 64, with bases `e_j,f_j`. Add two collections of spectator coordinates. On the whole `+2` baseline eigenspace define

`g_j=(e_j+f_j)/sqrt(2)`,

and on the negative eigenspace define

`q_j=(e_j-f_j)/sqrt(2)`.

Let

`A_0=[[0,2I_64],[2I_64,0]] direct_sum 2 I_(m+59)`.

Then every `g_j` and every spectator has eigenvalue `+2`, and every `q_j` has eigenvalue `-2`.

### Free packet

Let `W=span{g_64,h_1,...,h_m}` and choose any fixed orthonormal basis `w_0,...,w_m` of `W`. For completely arbitrary real amplitudes `tau_a`, add

`S_G=sum_a tau_a w_a w_a^T`.

This literally replaces the corresponding baseline eigenvalues `2` by `2+tau_a`. Every `I`-projection of a vector in `W` is collinear with `e_64`, and every `J`-projection is collinear with `f_64`; hence

`rank(S_G[I,J])<=1`,                                                       (9)

uniformly in `m` and in all amplitudes. These are arbitrarily many truly unbounded signed replacements at no amplitude cost.

### Residual packet with arbitrarily prescribed amplitude ranges

For `j=1,...,59`, fix any finite number `M_j>0`, however large. Let `s_j` be distinct spectator eigenvectors and set

`alpha_j^2=min{1, 2/(59 M_j)}`,

`z_j=alpha_j g_j + sqrt(1-alpha_j^2) s_j`.

The `z_j` are orthonormal baseline `+2` eigenvectors. For arbitrary coefficients

`|sigma_j|<=M_j`

of either sign, add

`E=sum_{j=1}^{59} sigma_j z_j z_j^T`.

This literally replaces those 59 eigenvalues `2` by `2+sigma_j`. Since

`||P_Iz_j||^2=||P_Jz_j||^2=alpha_j^2/2`,

each mode contributes at most `1/59` to either physical absolute energy. Therefore

`a_I(E)<=1`, `a_J(E)<=1`.                                                  (10)

The ranges `M_j` may be chosen arbitrarily large before the fixed directions `z_j` are set; after that, the estimate is uniform over all signs and all coefficients in those ranges, including arbitrarily small coefficients.

Finally add any symmetric dense `T` with

`||T||op<=1/4`.                                                            (11)

For `M_0=2I_64`, use the completed fleet02/B12 theorem with

`r=1`, `q=5`, `p=58`.

Equation (2) and (10) give the actual residual inequality

`s_59(E[I,J]) <= 1/59`.                                                     (12)

Hence the partner reserve theorem gives

`s_5(M_final) >= s_64(M_0)-s_59(E[I,J])-1/4
               >= 2-1/59-1/4
               =409/236`.                                                  (13)

The completed D5 receiver now gives the continuous density bound

`boxed: ||p_Q||_infinity <= 5 sqrt(2e)/(409/236)
        =1180 sqrt(2e)/409
        =6.72699241634378... .`                                            (14)

This is uniform in `m`, in every unbounded free amplitude `tau_a`, in all 59 independently signed residual replacements within arbitrarily prescribed finite ranges, and in every dense tail satisfying (11).

### Exact target-class verification

Before `T`, all 64 vectors `q_j` are untouched eigenvectors with eigenvalue `-2`. Therefore the pre-tail matrix has at least 64 eigenvalues at most `-2`, independently of every replacement above. By min--max/Weyl, after adding `T` with norm at most `1/4`, at least 64 eigenvalues are at most `-7/4`. Thus every matrix in this family lies in the exact owner target class with a large margin.

## Relation to the immediately preceding B12 half-energy theorem

The preceding fleet01/B12 run proved the sharp Frobenius half-energy bridge

`||E[I,J]||F <= ||E||F/sqrt(2)`

and combined it with the partner's `1/sqrt(p+1)` reserve dilution. The new inequality (1) changes mechanism: it controls the cross **nuclear norm** by the geometric mean of the two physical `|E|` energies, producing the sharp `1/(p+1)` singular-tail dilution. The two bounds are complementary, and one may always use their minimum.

## What remains open

This does **not** prove the unrestricted QFORM conjecture. The missing structural implication remains: starting only from `s_3(A)>=1`, force an original-coordinate cut with enough singular-value reserve and either (i) low-rank physical footprint for the largest hostile spectral packet plus small bilateral absolute energy for the remainder, or (ii) one of the already-paid D5/ridge/grouped-bank/hub/localized-core/Schur exits. The live correction families rule out simply asserting a universal good small principal block or universal rank-three cross cut.

Continuity is proved in the scope of this theorem through the D5 receiver; unrestricted continuity remains open.

## Partner and source provenance

Completed partner theorem actually used:

- repository: `yspennstate/math-open-problems`
- commit: `64268d2bee76cd374e2bf1a34868e0e6a1b7e84d`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T115313Z-fleet02-B12-qform-r33/REPORT.md`
- result: `QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1`.

Completed D5 receiver actually used:

- repository: `yspennstate/math-open-problems`
- commit: `e5f71d79eff325201dd0274053d20268ce65b837`
- path: `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`
- result: `||p_Q||inf <=5 sqrt(2e) Z_5^(-1/10)`, hence `<=5 sqrt(2e)/s_5(M)`.

