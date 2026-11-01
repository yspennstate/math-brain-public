SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T03:07:01Z.
attacking: the N3 four-bank survivor — convert the disjoint star-star-core packet into a paid diffuse-tail branch or a quantitative low-tail/two-sided physical-hub alternative.

# Early substantive checkpoint

Status: new deterministic split derived; full QFORM remains OPEN. Execution context: WITHOUT_VERIFIED_BRAIN.

Incoming physical packet is fleet03/B07 r21: in the current N3/O0 survivor there are four mutually disjoint original-coordinate banks and a residual physical cross block M such that, with C,R the two star norms and F=||M||_F,

    C R F > kappa,              kappa = 1/(256 sqrt(3)).          (1)

The current volume-tail source is `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`. It supplies

    T E2 <= 3 E3,               T=sum_{j>=3}s_j(M)^2,             (2)

and, for any singular-left projection P,

    sqrt(alpha_i) <= sqrt(P_ii)
       + sqrt(3) ||(I-P)M||op/sqrt(T) sqrt(1-P_ii).               (3)

If max P_ii<=1/2 and the residual norm is <=sqrt(T)/15, the q=4/3 third-volume Fourier theorem applies.

## New calculation

Write lambda_j=s_j(M)^2, S=sum lambda_j=F^2 and T=sum_{j>=3}lambda_j. Fix 0<theta<=1/2. If T>=theta S, then

    E3(M) >= theta^2 S^3/6 = theta^2 F^6/6.                       (4)

Proof: if T<=S/2, then E2 >= (lambda_1+lambda_2)T=(S-T)T, so (2) gives E3>=T^2(S-T)/3>=theta^2 S^3/6. If T>=S/2, then lambda_1<=S-T<=S/2, hence sum lambda_j^2<=lambda_1 S<=S^2/2 and E2=(S^2-sum lambda_j^2)/2>=S^2/4. Thus E3>=TE2/3>=S^3/24>=theta^2 S^3/6.

Now define J to contain singular directions 1,2 and every j>=3 with lambda_j>T/225. There are at most 224 selected tail directions, hence |J|<=226. Let P_L and P_R be the left/right singular projections onto J. Then

    rank P_L=rank P_R<=226,
    ||(I-P_L)M||op=||M(I-P_R)||op<=sqrt(T)/15.                  (5)

Therefore, if either max_i(P_L)_ii<=1/2 or max_j(P_R)_jj<=1/2, orient the cross-block on that diffuse side. Equation (3) yields alpha<2/3, and the current q=4/3 theorem plus (4) gives

    ||p_Q||infinity
      <= (9 sqrt(3)e/2) E3(M)^(-1/6)
      <= (9 sqrt(3)e/2)(6/theta^2)^(1/6) F^(-1),                (6)

with a continuous density and arbitrary self blocks/outside couplings retained.

Finally introduce a free star threshold Lambda>0. From (1), either C R>Lambda, or F>kappa/Lambda. In the latter case, if also T>=theta F^2 and one of P_L,P_R is diffuse, (6) is the universal paid bound

    ||p_Q||infinity
      < 3456 e Lambda (6/theta^2)^(1/6).                        (7)

If the paid branch fails, one has one of the explicit structural survivors:

1. large disjoint two-star reserve C R>Lambda;
2. low total tail T<theta F^2, i.e. dist_F(M,rank<=2)<sqrt(theta)F;
3. a two-sided bounded-rank physical hub: max diag P_L>1/2 and max diag P_R>1/2 for matched singular projections of rank <=226, while the omitted cross operator has norm <=sqrt(T)/15.

At theta=1/16 and Lambda=1, the paid constant in (7) is 31910.486.

This is the first substantive checkpoint. The final report will verify constants, apply a completed fleet04 product-projection result to the large-star inequality, and refresh corrections before publication.
