# Bent-edit test of the joint singleton payment

Natural logarithms. This is a narrow stress test of the already pending A066 singleton price, not a new universal-payment candidate. Let m>=1, N=2^(2m), A=2^-m, d=1/N=A^2, and take the actual Boolean quadratic bent sign

g_m(x)=(-1)^(sum_{j=1}^m x_(2j-1)x_(2j)), x in {0,1}^(2m).

Its Walsh coefficients are +/-A, with counts n_+=(N+2^m)/2 and n_-=(N-2^m)/2. The constant coefficient is +A and g_m(0)=1. For one fresh sign coordinate z define

F_m(z,x)=g_m(x)-(1-z)1_{x=0}.

Only the child z=-1 has its all-zero vertex flipped. Thus F_m is Boolean; its derivative in z is 1_{x=0}; Inf_z=d, hat F({z})=d. Every data coordinate has influence 1/2+d: bent g has influence 1/2, and its flipped child gains one undirected pivotal edge incident to the all-zero vertex, changing its influence by 2d. Hence I(F_m)=m+(2m+1)d. The trivial entropy bound H_bits(F_m)<=2m+1 gives H_bits/I<=2+1/m, so this family is not an unbounded FEI-ratio family. For each residual set T its coefficient pair is a_T=hat g(T)-d, c_T=d. Define the exact row channel

c(a,b)=((a+b)^2 ln((a+b)^2/(a^2+b^2))+(a-b)^2 ln((a-b)^2/(a^2+b^2)))/2.

Then the nonempty-context channel and singleton level bill are

C_z^+=(n_+-1)c(A-d,d)+n_- c(A+d,d),
ell_z=d^2 ln(1/d^2).                                               (1)

The empty residual row is precisely one positive row. It must be removed before adding ell_z; using the full channel instead would be an accounting error.

## An all-m obstruction to coefficient two

Writing q=a^2+b^2 and r=2ab/q, the row channel is q g(r), where g(r)=((1+r)ln(1+r)+(1-r)ln(1-r))/2. Since g''(r)=1/(1-r^2)>=1 and g(0)=g'(0)=0, g(r)>=r^2/2. Consequently

c(a,b)>=2a^2 b^2/(a^2+b^2)>=2b^2-2b^4/a^2                     (2)

for a!=0. Here |a_T|>=A-d=A(1-A)>0. Summing (2) over N-1 nonempty residual rows and dividing by d gives

(C_z^++ell_z)/d
 >=2+2d[ln(1/d)-2/(1-A)].                                       (3)

For every m>=2, ln(1/d)=2m ln2>2/(1-2^-m). At m=2 this follows already from ln2>2/3; the left side increases with m and the right side decreases. Thus every member with m>=2 has

C_z^++ell_z>2 Inf_z.                                            (4)

This disproves ONLY a proposed coefficient-two joint singleton strengthening; it does not contradict the proved coefficient beta=2+2/e^2. A minimal member of this family has five variables (m=2). Its rational-log interval from the exact formula (1) certifies (C_z^++ell_z)/Inf_z>217/100, without a floating-point sign decision. Thus any universal joint paid-fragment constant must exceed 2.17; the pending proved upper constant is about 2.27067. No global optimality claim follows from this family.

The upper row price c(a,b)<=2b^2 yields

(C_z^++ell_z)/d<=2-2d+2d ln(1/d).

Together with (3) this proves the ratio tends to 2 from above as m tends to infinity. Therefore a fixed positive improvement below 2 is impossible, while the sharper finite peak is a separate scalar/realizability issue. No sharp global optimum is asserted.

## Exact oriented erasure versus paid charge on the same row

For a physical singleton, use the actual complete residual law r_i(T)=p_T+p_(T+i) and derivative law mu_i(T)=p_(T+i)/Inf_i. The oriented bill M_i=sum_T p_(T+i)ln(r_i(T)/p_(T+i)) equals Inf_i ln(1/Inf_i)-Inf_i D(mu_i||r_i). Its nonempty-row version is M_i^+. This is the A096 normalized conditional-edge reference, not a fresh claim or payment.

For the bent-edit family,

M_z^+=(n_+-1)d^2 ln(((A-d)^2+d^2)/d^2)
       +n_- d^2 ln(((A+d)^2+d^2)/d^2).                           (5)

It is not small uniformly: M_z^+/d=ln(1/d)+O(A) as m grows, with the explicit bound |M_z^+/d-2m ln2|<=8A for m>=2. To justify it, write the row likelihood as d^-1[(1 +/- A)^2+d]. For A<=1/4, these bracket factors differ from one by at most (5/2)A<=5/8; hence their logarithms have absolute value at most (20/3)A, using |ln(1+u)|<=|u|/(1-|u|). The weights of nonempty rows sum to 1-d. Omitting the empty row therefore changes the leading ln(1/d) term by d ln(1/d)<=A ln2<(7/10)A, since m2^-m<=1/2 for m>=2. The total error is at most [(20/3)+(7/10)]A<8A. Equation (5) concerns the selected fresh-coordinate bill only; other core coordinates and the terminal bent/edited core remain. The universal root sum M/I is not shown unbounded, and the selected-coordinate divergence does not refute the existential good-coordinate rule. Bent leaves have growing total influence.

This family simultaneously makes the channel price nearly 2d, retains a strictly positive level correction, and carries an unbounded oriented erasure rate at the selected coordinate. Thus choosing a coordinate merely because its derivative mean saturates |hat f({i})|<=Inf_i does not pay the residual. The first unsupported universal line remains the actual retained-core KL lower bound or an owned global erasure/stopping-tree payment. Further work must select/price the residual, rather than simplify the paid fragment to coefficient two.

The weighted aggregate is nevertheless harmless on this diagnostic. Let L=sum_i e_i ln(1/e_i), so M=L-I D_joint<=L by nonnegativity of the actual normalized KL divergence. Data influences equal 1/2+d and their logarithms are at most ln2. The fresh contribution is d ln(1/d)=2md ln2. Therefore L/I<=[1+(2m-1)d/I]ln2<=(1+2d)ln2<=(9/8)ln2 for m>=2. This uses the same physical I, not separate budgets for the rare coordinate and data core. It shows explicitly why an arbitrarily expensive selected coordinate is not a refutation of the global normalized-reference mechanism. NEXT is a global or child-certified selection/payment of that actual reference for arbitrary seeds, not a uniform lower bound on every coordinate's refund.
