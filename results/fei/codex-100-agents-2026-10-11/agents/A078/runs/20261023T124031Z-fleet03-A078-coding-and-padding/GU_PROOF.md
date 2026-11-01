# Exact GU effect of actual Boolean parity padding

Current target: for every Boolean f prove G(f)<=a I(f)+b U(f) with dimension-independent finite a and0<=b<1. This stage freezes(a,b)=(0,0) on the explicitly specified padded family; it makes NO universal GU or FEI claim. The original private ORDER.md and complete GU_LASER_FOCUS_20261014.md were retrieved during this stage, superseding the older broad stream note where necessary. The companion affine-bank proof is an entropy ledger, not a proved GU payment. Its symbol U_v is a profile allocation; the U in this document is the actual upper-set potential.

## 1. Exact zero-erasure U drift, with every terminal mass retained

For an actual Boolean f let p(S)=fhat(S)^2 and pi(S)=sum_(T containing S)p(T). Define U=sum_(p(S)>0)p(S)log2(pi(S)/p(S)). Suppose a physical coordinate i has NO occupied Fourier pair S,S+i: fhat(S)fhat(S+i)=0 for every S not containing i. This is exactly zero true spectral erasure at i.

The actual child Fourier coefficients are fhat(S)+/-fhat(S+i). Because at most one term is nonzero, both child squared spectra equal the injective pushforward of parent p under rho_i(S)=S without i. No parent mass, including the empty row, is omitted. Parent containment implies containment after projection, so

 pi_child(rho_i(S))>=pi_parent(S).

Consequently the exact SIGNED query decrement is

 Delta_i U=-sum_(p(S)>0) p(S)log2[pi_child(rho_i(S))/pi_parent(S)]<=0. (1)

The two complete child potentials agree. Every numerator and denominator in(1) is at least p(S)>0; zero rows are absent by convention, not divided by zero. Constants give0 directly. These are actual Boolean restrictions, not arbitrary spectral-law children. No fresh source budget or absolute-value clipping is used.

This is an explicitly sufficient zero-price U-drift STEP: GIVEN U(g)<=K I(g) for both actual children,

 U(f)<=average U(child)<=K average I(child)=K[I(f)-Inf_i(f)]<=K I(f). (2)

Equation(2) retains its complete terminal hypotheses. It does not assert that they hold for arbitrary Boolean children, nor that every function has a zero-erasure coordinate. No external GU-to-FEI reduction is invoked here.

## 2. Every Boolean function has a GU-easy actual parity lift

For EVERY Boolean f on n>=1 physical bits, define the actual Boolean function

 F(x,z)=f(x+z*1), addition in F2.                  (3)

This is systematic coding [Id|1], not a formal spectrum construction. Its Fourier rows are (S,|S| mod2) with original coefficient fhat(S), and all other rows are zero. Hence all occupied rows have EVEN physical cardinality. Every physical coordinate, including z, has zero erasure and obeys(1). Thus EXACTLY

 G(F)=-sum_i C_i(F)<=0, C_i(F)>=0.               (4)

The frozen GU pair(0,0) is proved for this entire family, all dimensions and all biases. The more general systematic code[Id|P] has this property whenever EVERY original row of P is nonzero: deleting any physical column preserves code rank, so its projection is injective on occupied Fourier rows. Partial row coverage need not satisfy G<=0.

The physical identities are

 H(F)=H(f), I_xi(F)=I_i(f),
 I_z(F)=Pr[f(x)!=f(x+1)]=sum_(|S| odd)p(S)=theta_odd,
 I(F)=I(f)+theta_odd<=2I(f).                     (5)

The last bound uses odd |S|>=1; constants are handled directly. Added influence is counted, not discarded. Upper-set potential has the exact normalization correction

 U(f)-U(F)=sum_(|S| odd,p(S)>0) p(S)log2[pi_f(S)/pi_f,odd(S)]>=0, (6)

where pi_f,odd(S)=sum_(T containing S,|T| odd)p(T)>=p(S). For even S no added tag constraint is present. Under any systematic code, pi_code is the sum over original supersets satisfying the extra parity-tag containment, so U(code)<=U(base). Equation(6) preserves the full correction rather than treating entropy-preserving relabeling as U-preserving.

## 3. Why root GU tests cannot certify FEI on this family

If FEI with constant C were proved on ALL functions of form(3), then(5) would give H(f)<=2C I(f) for EVERY original Boolean f. Conversely full FEI trivially covers the class. Thus the GU-easy family is FEI-hard up to factor2, even though its root GU inequality is already true with(a,b)=(0,0).

This is NOT a contradiction to the universal GU reduction. That reduction also requires GU for the arbitrary restricted children. Revealing z in(3) leaves f or its translated truth table; both have EXACTLY U(f). The negative credit(6) must be retained, and the unresolved arbitrary terminal certificate remains. A hypothetical genuine FEI counterfamily could be parity-lifted with H/I losing at most factor2, while every lifted root still has G<=0. No actual FEI counterfamily is supplied by this conditional transformation.

The shortest universal step is therefore the FIRST nonzero-erasure physical query after peeling the code, paying its exact signed GU increment with the actual inherited upper-set correction and complete child U. Testing more fully covered parity-coded roots for positive GU residual is vacuous by(4).

## 4. Explicit all-parameter Boolean family with exact G,I,U,H

For every even k>=2 take b_k(x)=(-1)^(sum_(j=0..k/2-1) x_(2j)x_(2j+1)) and F_k(x,z)=b_k(x+z*1). The two-bit quadratic sign has four Walsh magnitudes1/2; tensoring proves all2^k base magnitudes2^(-k/2). The actual physical squared spectrum of F_k is therefore uniform on the even-parity subspace of k+1 labels. Direct counting gives

 H(F_k)=k,
 I(F_k)=(k+1)/2,
 U(F_k)=(k-1)/2,
 Delta_i U(F_k)=-1/2 for EVERY physical i,
 G(F_k)=-(k+1)/2.                                (7)

Indeed each occupied even row S has |S|<=k, and pi(S)/p(S)=2^(k-|S|); the mean row weight is(k+1)/2. Every child projects bijectively onto all k-bit labels, where U=k/2. Thus G/I=-1, U/I=(k-1)/(k+1) tends to1 and H/I=2k/(k+1) tends to2. These are exact analytic formulas for actual Boolean functions, not fits. They distinguish GU residual, U/I and H/I as required by B16. They are not a disproof of FEI.

Scope guard: a three-input partially covered systematic lift of the two-bit NAND sign, with parity column1, has G=1,U=1,I=3/2,H=2. This refutes only the omitted-row version of(a,b)=(0,0); it is not a failure of any finite universal admissible pair.
