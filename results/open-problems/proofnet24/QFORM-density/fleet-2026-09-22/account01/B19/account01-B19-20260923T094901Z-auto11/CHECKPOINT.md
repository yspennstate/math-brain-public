SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T09:49:01Z.
attacking: the extreme-coloop grouped-third-source residue; replace the partner's specially aligned square-plus-hyperbola endpoint by a sign-complete three-independent-grouped-scalar receiver, then identify the genuinely remaining same-bank near-null obstruction.

# Substantive checkpoint

The current account02/B19 r31 endpoint has an exact target stress family with three genuinely independent product-derived scalar projections Y1,Y2,Y3, each with density cap <=sqrt(e), and core

    M_m = [[a_m,0,0],[0,0,1],[0,1,0]],
    a_m=m/sqrt(m-1),

so Q=a_m Y1^2+2Y2Y3 and s_min(M_m)=1.  r31 already pays this family by a special third-square/hyperbolic theorem.  The intended upgrade is to remove that special alignment.

Lemma under assembly: if S=(S1,S2,S3) has mutually independent scalar coordinates with density caps <=K, B=B^T is 3x3 and s_min(B)>=sigma>0, and l is arbitrary, then S^T B S+l.S+c has a density with

    ||p||_infinity <= 128 sqrt(2) K^2 / sigma.

Proof split after scaling K=1, sigma=1:

(1) If max_i |B_ii|>=1/4, use QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1 on the full physical 3x3 matrix.  Here the spectral frame is I_3, so c_i=1 and |det B|>=1.  Thus

    ||p||_infinity <=128 (|B_ii| |det B|)^(-1/4)
                     <=128 sqrt(2).

(2) If every |B_ii|<1/4, then ||B e_j||>=1 for every j.  Hence for any j,

    sum_{i!=j} B_ij^2 >15/16,

so one off-diagonal entry satisfies |B_ij|>=sqrt(15/32).  The principal pair P={i,j} is automatically indefinite because

    det B_PP = B_ii B_jj-B_ij^2
             <1/16-15/32=-13/32.

Moreover by Weyl applied to [[0,B_ij],[B_ij,0]] plus diag(B_ii,B_jj),

    kappa:=s_min(B_PP)>=sqrt(15/32)-1/4=:kappa_0>0.

The completed logarithmic physical-pair theorem applies to this exact-rank-three 3-variable form, with global spectral lower scale s=1, D=|det B_PP|>=13/32, and kappa>=kappa_0, giving

    ||p||_infinity
      <=8 sqrt(5) [(13/32) kappa_0]^(-1/4)
      <128 sqrt(2).

Scaling S -> K S and B -> B/K^2, followed by B -> B/sigma, yields the stated 128 sqrt(2) K^2/sigma bound.  All signatures are included: the large-diagonal branch uses the orientation-free scalar-pivot theorem; the all-small-diagonal branch forces an indefinite pair.  No post-rotation independence is used.

For the partner r31 family, K=sqrt(e), sigma=1, so this already gives the robust alignment-free bound 128 sqrt(2)e.  Applying the sharper completed account03/B16 exact-Schur-null theorem to the actual ordering (Y,U,V)=(Y2,Y3,Y1) gives

    b=a_m, delta=0, det B=-a_m,

hence

    ||p_Q||_infinity <=4 e a_m^(-1/2)
       =4e [epsilon(1-epsilon)]^(1/4)
       <sqrt(2)e  for m>=65.

This improves the partner's special-family <2e bound and, more importantly, shows that the analytic endpoint does not need exact square-plus-hyperbola alignment once a full three-independent-scalar grouped core is exposed.  The remaining debt is structural: in a generic extreme-coloop survivor, force such a rank-three grouped scalar core (or an already-paid exit), or handle the genuinely same-bank near-null third curvature without inventing independence.
