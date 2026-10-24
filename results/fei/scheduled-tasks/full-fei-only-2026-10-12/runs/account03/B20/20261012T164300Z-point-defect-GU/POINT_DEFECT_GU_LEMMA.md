# GU on point defects and their disjoint tensor products

Status: AUTHOR-PROVED, INDEPENDENT REVIEW PENDING; full FEI remains OPEN. This is a new independent GU-family calculation, not the earlier safety-held B20 proof.

For n>=1 let f_n(x)=1-2*1{x=(+1,...,+1)} on {-1,+1}^n. Set t_n=2^(1-n), A(t)=-2(1-t)^2 log_2(1-t) for 0<=t<1, A(1)=0. Write p(S)=fhat(S)^2, pi(S)=sum_{T superset S}p(T),
U(f)=sum_{S:p(S)>0}p(S)log_2(pi(S)/p(S)), I(f)=sum_S |S|p(S), and G(f)=sum_i[U(f)-(U(f_{i,+})+U(f_{i,-}))/2].
For n>=2,
  U(f_n)=A(t_n)+n*t_n*(1-t_n),
  I(f_n)=n*t_n,
  G(f_n)/I(f_n)=1+(n-2)t_n+[A(t_n)-A(2t_n)/2]/t_n.
For n=1, U=G=0 and I=1.

THEOREM. On all signed/translated/permuted point defects and all finite tensor products of these on disjoint coordinate blocks, the sharp universal GU constant is
  K_point=(1+9 log_2(16/9))/4 = 2.1176687467547968...,
attained by a three-bit point defect. No claim that this K holds for arbitrary Boolean functions.

Proof.
1. For f_n, hat f(empty)=1-t_n and hat f(S)=-t_n for every nonempty S (the sign of the nonempty coefficient may depend on the chosen defect point, but squares do not). For S nonempty, pi(S)=2^(n-|S|)t_n^2. Thus every nonempty S contributes t_n^2(n-|S|) to U. Summing gives sum_{S nonempty}(n-|S|)=n(2^(n-1)-1). The empty contribution is A(t_n). Hence U=A(t_n)+n*t_n*(1-t_n). Similarly I=n*2^(n-1)*t_n^2=n*t_n.
2. Fixing x_i=+1 yields f_{n-1}; fixing x_i=-1 yields a constant. Therefore Delta_i U(f_n)=U(f_n)-U(f_{n-1})/2, and the displayed ratio follows on substituting t_{n-1}=2t_n. For n=1 both restrictions are constants and G=0.
3. On 0<=s<1, A''(s)=-(2/ln2)(3+2 ln(1-s)) >= -6/ln2. The derivative extends continuously to s=1, and the lower curvature bound remains valid under integration. For 0<=t<=1/2,
 A(t)-A(2t)/2 = (1/2)int_0^t[A'(u)-A'(u+t)]du <= 3t^2/ln2.
Consequently G(f_n)/I(f_n) <= 1+(n-2+3/ln2)2^(1-n).
For n>=4 the positive correction is decreasing in n, since (n-1+c)/(2(n-2+c))<1 for c=3/ln2 and n>=4. Its maximum is (2+3/ln2)/8 < 1 (using ln2>1/2). Hence G/I<2 whenever n>=4.
4. The exact n=2 value is 2. For n=3 it is K_point. K_point>2 follows from log_2(16/9)>7/9, equivalently 16^9>2^7*9^9 (68719476736>49589822592). Thus the maximum among all n is attained at n=3.
5. If f=prod_j f_j on disjoint blocks, its squared Fourier law factorizes. Consequently pi_f factors, U(f)=sum_j U(f_j), I(f)=sum_j I(f_j), and physical restriction in one block changes only that block's U. Thus G(f)=sum_j G(f_j). For nonconstant factors, G/I is the I-weighted average of factor ratios, bounded by K_point, and equality is attained by a three-bit factor. Constant factors are harmless.

This is an all-n analytic bound for one infinite family, not GU for arbitrary Boolean f and not an FEI proof. Numerical diagnostics are self-checks, not proof. Literature novelty UNKNOWN. Independent reviewer required.