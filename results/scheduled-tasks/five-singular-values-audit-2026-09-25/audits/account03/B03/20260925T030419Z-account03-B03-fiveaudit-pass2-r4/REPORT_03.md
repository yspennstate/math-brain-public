## Lines 222-270

C08 remains a literal false clause at line 222: zero-beta factors need not be "at most one." Example n=3,d=2,U=(e1,e2),W=e3 gives beta_1=beta_2=0.

The repair is local: drop all zero-beta factors. For beta_i=0, w_i=0, so each factor is fiber-variable independent and at most one. The retained positive-beta rows still satisfy the Brascamp-Lieb frame identity. The e^{d/2} projection cap and all downstream constants remain unchanged.

After that repair, Lemma 3.2(b) follows by thin SVD with Jacobian sqrt(det(BB^T)). Lemma 3.3 also passes: the difference density is <=1, m=floor(p/2)>=p/4, the Fourier exponent comparison has the right direction, the even power is an integrable characteristic function, and the scalar projection bound gives the stated constant.

The crossing-volume definitions match Cauchy-Binet. Lemma 4.2's entropy bound is Jensen plus the fact that each squarefree m-subset monomial occurs m! times in (sum alpha_i)^m.

## External checks

BGKS Theorem 2.1 was checked at statement level and has the bilinear-plus-affine bounded-density form described. The sqrt(2)K one-dimensional projection attribution is supported by an independent source explicitly deriving it from Rogozin plus Ball. RV/LPP and BCCT/CLL subject descriptions and bibliography metadata were also checked.
