SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T21:46:33Z.
attacking: a full-rank escaped-support exact rotated witness that preserves the 3sqrt(2) lower obstruction, plus a concrete near-kernel fragmentation application of the completed fleet02/B17 theorem.

# Early substantive calculation

Let

R0=(1/2)*[[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]],

k0=(1/2)*(1,-1,-1,1)^T,

n=(7,18,18)^T/sqrt(697), and B=I-2nn^T. Then R0^T R0=I3, R0^T k0=0, ||k0||=1 and B^2=I3 with signature (2,1).

The exact dense four-coordinate core is

A*=R0 B R0^T=(1/2788)*
[[-1607,95,95,1797],
 [95,1993,-795,1103],
 [95,-795,1993,1103],
 [1797,1103,1103,409]],

whose sixteen entries are nonzero and whose nonzero spectrum is {1,1,-1}.

For m blocks, stack m copies of R0/sqrt(m) into W_m, set P_m=W_m W_m^T, A_m^0=W_m B W_m^T, and stack m copies of k0/sqrt(m) into c_m. Then ||c_m||=1 and W_m^T c_m=0. For epsilon_m=m^-2 and sigma in {+1,-1}, define

Atilde_m^sigma=A_m^0+sigma epsilon_m(I-P_m).

Its spectrum is exactly {1,1,-1,sigma m^-2 (multiplicity 4m-3)}, so it is full rank and remains a target matrix. For m>=7 it is entrywise dense: the A_m^0 block entries are A*_{ab}/m; off-diagonal perturbations have magnitude at most 3/(4m^3), while 95/(2788m)>3/(4m^3); diagonal perturbations have magnitude at most 1/m^2, while 409/(2788m)>1/m^2.

Now take U_i iid Uniform[-1/2,1/2] and X_m=U+m c_m. Every physical input remains a cap-one unit-interval density, but each support center is +/-sqrt(m)/2 and hence all supports escape every fixed compact set. Also E X_i^2=m/4+1/12 -> infinity.

Writing K_m=I-P_m,

X_m^T Atilde_m^sigma X_m
=U^T A_m^0 U + sigma[1+(2/m)c_m^T U+(1/m^2)U^T K_m U].

Since ||U||<=sqrt(m),

|X_m^T Atilde_m^sigma X_m - sigma - U^T A_m^0 U|
<=2/sqrt(m)+1/m =: delta_m.

Finally W_m^T U=(1/sqrt(m)) sum_{ell=1}^m R0^T U^(ell) converges by the 3D CLT to G~N(0,I3/12). Hence U^T A_m^0 U => G^T B G. The latter has the same law as G1^2+G2^2-G3^2 and continuous density at zero equal to 3sqrt(2). The deterministic delta_m coupling therefore yields, for every h>0,

liminf_m ||p_{X_m^T Atilde_m^sigma X_m}||_infinity
>= P(|G^TBG|<=h)/(2h),

and h down to zero gives liminf >=3sqrt(2). This preserves the sharp lower obstruction after forcing full rank, entrywise density, tiny extra spectrum of either sign, and supports escaping to infinity.

Full proof and partner application follow in REPORT.md. Full unrestricted QFORM remains OPEN; continuity remains separate.
