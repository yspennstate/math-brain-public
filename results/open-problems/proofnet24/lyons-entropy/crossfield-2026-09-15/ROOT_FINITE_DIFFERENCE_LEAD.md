# A signed determinant finite-difference formulation

Coordinator lead, 15 September 2026. This exact reformulation is not a positivity theorem and is not asserted to be historically new. It suggests connections to multivariate divided differences and spectral-shift formulas for future creative assignments.

For a Hermitian matrix J, set F(J)=det(J)log|det(J)|, with value zero on det(J)=0. Let D_i act by D_i F(J)=F(J)−F(J−e_i e_i*). For a strict contraction 0<K<I, every complementary atom matrix K−I_T is invertible and

    p_{T^c}=(-1)^|T| det(K−I_T)>0.

The occupation entropy therefore satisfies exactly

    H(K)=−D_1 D_2 ... D_n F(K)
        =−Σ_{T⊆[n]} (-1)^|T| det(K−I_T)log|det(K−I_T)|.   (1)

For a fixed Hermitian A, differentiation is legitimate at each of these finitely many nonsingular vertices. If Q=K−I_T and Y=Q^-1,

    D_A² F(Q)=det(Q){(2+log|det Q|)(tr(YA))²
                         −(1+log|det Q|)tr((YA)²)}.      (2)

To see (2), write d=det Q. Then F''=(1+log|d|)d''+(d')²/d, d'=d tr(YA), and d''=d[(tr YA)²−tr((YA)²)]. Substitution gives the displayed formula. Since the signed determinant weights p sum to one independently of K, E_p[(tr YA)²−tr((YA)²)]=0. Applying (2) to (1) consequently recovers

    −H''=E_p (tr YA)²
          +E_p log p [(tr YA)²−tr((YA)²)].                (3)

The key possible bridge is a sign theorem for the complete coordinate finite difference of the matrix-direction Hessian of det(J)log|det(J)|. Replacing this finite difference by an ordinary integral over the coordinate cube requires care: K−diag(x) can be singular inside the cube, and high derivatives of F can be distributions. No unqualified differentiation through these singularities is justified here.

Potential next work: construct a correct spectral-shift or distributional divided-difference representation of the combined expression, with a positive measure after the determinant cancellations. Individual resolvent integrands already have known sign obstructions in the prior campaign, so any useful representation must retain the entire compensated expression.
