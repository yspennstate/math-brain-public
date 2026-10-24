# A logarithmic potential that works for identical-block NAND

Status: proved restricted composition statement, self-checked; novelty UNVERIFIED. It does not bound an arbitrary initial Boolean function, and is not a full FEI proof. The unequal-block gap in Section 4 is subsequently resolved by `UNEQUAL_NAND_CONTRACTION_2026-09-18.md`, using a different complement-invariant potential. The historical failed potential and derivation here are retained.

This records a second approach after the positive-power majorants were refuted. It retains the exact logarithm and shows where an actual amortized estimate works and where its extension fails.

## 1. Definitions and exact recursion

For an indicator A with mean 0<alpha<1, Fourier coefficients c_S and singletons t_i, write

    K_A=sum_edges min(c_S^2,c_T^2) |log_2(c_S^2/c_T^2)|,
    Q_A=sum_i t_i^2,
    I_A=I(1-2A)=4 sum_S |S| c_S^2,
    r_A=K_A/I_A,  z_A=Q_A/I_A.

Zero-endpoint edges contribute zero. Since Q_A is part of the degree-weighted sum, 0<=z_A<=1/4. No unateness assumption is needed.

Let A'=1-product_{j=1}^k A(x^(j)) for k>=2 identical copies on disjoint variables, p=alpha^k. Homogeneity of the edge cost and Parseval's total indicator mass alpha give

    K_product=k alpha^(k-1) K_A,
    I_A'=k alpha^(k-1) I_A,
    Q_A'=k alpha^(2k-2) Q_A.

For completeness, the influence formula follows either by conditioning on all other blocks being one, or by summing |S| times the product Fourier masses. The singletons of A' are -alpha^(k-1)t_i in each block, proving the Q formula.

Every nonempty coefficient of an indicator is bounded in absolute value by both its mean and its complementary mean: |E A chi_S|<=E A, and E A chi_S=-E(1-A)chi_S. Thus before and after complementation, the singleton squared mass is no larger than the squared empty coefficient. Only empty-singleton edges change. Their exact correction is

    K_A'=k alpha^(k-1)K_A
       +2k alpha^(2k-2)Q_A log_2[(1-alpha^k)/alpha^k].  (1)

Consequently, putting w=alpha^(k-1),

    z_A'=w z_A,
    r_A'=r_A+2w z_A log_2[(1-alpha^k)/alpha^k].        (2)

## 2. A genuine telescoping bound

The potential

    P(A)=r_A+[4/ln(2)]z_A

does not increase under this operation, even if the integer arity k>=2 changes at every stage.

Proof. The logarithm in (2) is at most k log_2(1/alpha). Let t=-(k-1)ln(alpha)>0, so w=exp(-t). Then

    2k w log_2(1/alpha)
      =[2k/((k-1)ln2)] t exp(-t)
      <=[2k/((k-1)ln2)](1-exp(-t))
      <=[4/ln2](1-w).

The middle inequality follows from exp(t)>=1+t, whose proof is that exp(t)-1-t has value and derivative zero at t=0 and nonnegative second derivative. Multiply by z_A>=0 and use (2). This proves P(A')<=P(A).

After any finite sequence of such compositions,

    K_{A_d}/I_{A_d}
      <= K_{A_0}/I_{A_0}+[4/ln2]Q_{A_0}/I_{A_0}
      <= K_{A_0}/I_{A_0}+1/ln2.                      (3)

The seed term is NOT uniformly bounded by this argument. Also K_A is the unnormalized indicator functional, not K(1-2A); replacing one by the other without accounting for the empty coefficient is invalid. Thus (3) only controls growth along this specified composition operation.

## 3. Why the same potential does not extend to arbitrary unequal blocks

For A'=1-product_j A_j with means alpha_j, p=product_j alpha_j, and w_j=p/alpha_j, the exact formulas instead read

    K_A'=sum_j w_j K_{A_j}+2 log_2[(1-p)/p] sum_j w_j^2 Q_{A_j},
    I_A'=sum_j w_j I_{A_j},
    Q_A'=sum_j w_j^2 Q_{A_j}.                         (4)

They follow from the same product-mass and empty-coefficient argument. A proposed unnormalized inequality

    K_A'+c Q_A' <= sum_j w_j [K_{A_j}+c Q_{A_j}]

fails for every c. Take A_2 identically one, and choose nonconstant A_1 with alpha_1<1/2 and Q_{A_1}>0, for example the indicator of all zeros on two bits. Then A'=1-A_1, w_1=1, Q_A'=Q_{A_1}, while

    K_A'-K_{A_1}=2 Q_{A_1} log_2[(1-alpha_1)/alpha_1]>0.

This is an explicit obstruction, not evidence that a more suitable potential cannot work. In particular complementation merely negates the Boolean output 1-2A and changes none of its squared coefficients; the failure above is partly an artifact of using an unnormalized indicator potential.

## 4. A complement-invariant correction, and its unresolved product term

Define

    U(A)=K_A-2Q_A log_2(alpha).

Equation (1) for complementation alone gives U(1-A)=U(A). More explicitly,

    U(A)=sum_edges not touching empty min(c_S^2,c_T^2)|log_2(c_S^2/c_T^2)|
          +sum_i [-t_i^2 log_2(t_i^2)],

which is nonnegative. For an unequal product (and its complement), direct substitution in (4) gives

    U(A')=sum_j w_j U(A_j)
       +2 sum_j w_j Q_{A_j}
          [(1-w_j)log_2(alpha_j)-w_j log_2(w_j)].       (5)

The bracket has a nonpositive first term and a nonnegative second term. Dropping the first term can lose the compensation needed to sum costs through a tree. No dimension-free bound for the accumulated correction, covering arbitrary Boolean seeds and general non-product structure, has been proved here.

Equation (5) is retained as a concrete candidate identity, not as a theorem closing FEI. General arbitrary Boolean functions do not come supplied with a disjoint-product construction, so even a successful read-once composition estimate would leave the main conjecture open.
