SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T13:45:08Z.
attacking: the >=3/4 physical-hub-leverage survivor by grouping the whole two-dimensional hub projection before Fourier/Pluecker inversion, and isolating the exact anchored aggregate that remains.

# Early substantive checkpoint — high-hub anchor reduction

Full QFORM remains OPEN. This checkpoint records two exact inequalities and one explicit remaining analytic implication; no post-rotation independence, moment/support assumption, or pointwise quadratic stationary-phase bound is used.

## 1. Heavy-row projection cap

Let P be an m x 2 real matrix with P^T P=I_2 and let h be a physical row with eta=||p_h||_2^2>0. For independent cap-one coordinates X_H, put Y=P^T X_H. Then

    ||p_Y||_infinity <= sqrt(e/eta).

Proof. Rotate only the deterministic coefficient plane so p_h=(sqrt(eta),0). Writing the remaining two columns as u,v gives u.v=0, ||u||^2=1-eta and ||v||=1. Thus, up to an orthogonal change in the two-dimensional output variable,

    Y=(sqrt(eta) X_h + u^T X_R, v^T X_R).

Let V=v^T X_R. The completed affine-fiber BL projection theorem gives ||p_V||_infinity<=sqrt(e). The variable sqrt(eta)X_h is independent of X_R and has density cap eta^(-1/2). Therefore convolution only in the first coordinate gives, for a.e. (a,b),

    p_Y(a,b)
      <= eta^(-1/2) p_V(b)
      <= sqrt(e/eta).

At eta=1 this is simply the product pair (X_h,V); the same estimate holds. No independence between u^T X_R and v^T X_R is asserted.

Consequently, if k is a leaf coordinate independent of H, the three-dimensional grouped row projection (P^T X_H,X_k) has the same density cap sqrt(e/eta).

## 2. Actual rank-three singleton consequence

For the rank-two hub/star A[H,I]=P C^T, let

    M_k=A[H union {k}, I\{k}],
    Gamma_k=product of its three nonzero singular values.

Whenever Gamma_k>0, the proof of QFORM-GROUPED-CROSS-RANK-r-SMOOTHING-v1 may be run with the actual left projection cap above instead of the generic e^(3/2) cap. The right scaled rank-three projection has density cap <=e^(3/2)/Gamma_k. Hence

    ||p_Q||_infinity
      <=3 [sqrt(e/eta) * e^(3/2)/Gamma_k]^(1/3)
      =3 e^(2/3) eta^(-1/6) Gamma_k^(-1/3).

The characteristic function is L^1, so this singleton branch has a continuous density and the same coefficient multiplies interval length.

In particular, in the concentrated-singleton branch of account03/B09 r32,

    Gamma_k^2 >= (27/512) G_*,

and eta>=3/4 gives the uniform numerical consequence

    ||p_Q||_infinity
      <= 3 e^(2/3) (3/4)^(-1/6) (512/27)^(1/6) G_*^(-1/6)
      <10.011 G_*^(-1/6).

This improves the prior 13.317 coefficient in precisely the very-high-hub-leverage concentrated-singleton chamber.

## 3. Exact anchored aggregate in the diffuse-singleton chamber

Use the Bernoulli compiler from r32. It returns a literal original-coordinate cut with selected 3x3-minor mass

    W(S)>= (27/256) G_*.

The selected row triples are {a,b,k}, with a,b physical hub rows and k a moved leaf. Their squared determinant weights factor as

    det(P[{a,b},:])^2 * d_(k,J)^2.

The squared 2x2 Pluecker weights of P sum to one, and the total weight of hub pairs containing h equals the row leverage eta:

    sum_(b != h) det(P[{h,b},:])^2 = eta.

Therefore the subfamily whose physical hub pair contains the fixed heavy row h has EXACT mass

    W_h(S)=eta W(S).

Thus for eta>=3/4,

    W_h(S) >= (81/1024) G_*.

This is dimension-free and uses a literal physical anchor; no individual minor is selected or reciprocated.

The remaining analytic debt is now precise: prove a vector-valued grouped 2+1 selected-subvolume Fourier/BL inequality which consumes the two-dimensional hub projection jointly (using ||p_(P^T X_H)||_infinity<=sqrt(e/eta)) and the fixed-anchor mass W_h, rather than charging the physical row h a scalar selected-minor marginal alpha_h=1. The q-dependent scalar-row theorem stops at alpha<3/4 and therefore cannot by itself pay this endpoint. This is an analytic-interface gap, not evidence of concentration of the grouped hub law.

## 4. Compatibility check with the designated account04/B09 theorem

A target-valid high-leverage example is obtained from

    P rows = (sqrt(.8),0), (sqrt(.1),1/sqrt(2)), (sqrt(.1),-1/sqrt(2)),

leaf C rows (ordered k,1,2,3) = (0,0),(1,0),(0,1),(0,0), and D[k,3]=D[3,k]=1. The full 7x7 symmetric coefficient matrix [[0,PC^T],[CP^T,D]] has spectrum {-1,-1,-1,0,1,1,1}; the maximum hub leverage is .8. The literal physical cross block with rows {h,b1,k} and columns {1,2,3} has

    |det K|=sqrt(2/5).

The completed designated-partner theorem QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1 therefore applies at the actual inequality

    ||p_Q||_infinity <=3 |det K|^(-1/3)
                       =3 (5/2)^(1/6)
                       <3.495,

with continuous density and the same linear interval bound.

This example is beyond the old eta<3/4 selected-row gate and confirms that high hub leverage itself is not an obstruction when a literal rank-three cross packet is present.
