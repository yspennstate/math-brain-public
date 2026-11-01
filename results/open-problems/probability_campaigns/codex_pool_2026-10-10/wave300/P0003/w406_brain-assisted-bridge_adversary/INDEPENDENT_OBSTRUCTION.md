# Independent obstruction: the vertex relation has cycle modes

Worker w406, 2026-10-10. This derivation was written before opening w405's proof. Independent review by w407 is pending. This is an obstruction to a proposed implication, not a counterexample to the SAW conjecture or to the actual path-sum observable.

Duminil-Copin--Smirnov, arXiv:1007.0575v2, Definition 1 and Lemma 1, use the critical fugacity x_c=(2+sqrt(2))^(-1/2), spin 5/8, and the relation

    L_v F := sum_{e incident to v} (m_e-v) F(m_e) = 0.

Here m_e is the midpoint of edge e, and the lattice domain contains all midpoints emanating from its vertex set. The path-sum definition is an additional constraint; the vertex relation is only a linear consequence of that definition.

## Exact cycle-space statement (submitted proof, unreviewed)

Let G=(V,E_int) be a finite connected honeycomb graph inside a lattice domain, and prescribe F=0 on all boundary half-edges. Orient each internal edge e from u_e to v_e, put d_e=v_e-u_e != 0, and set X_e=(d_e/2)F(m_e). Then L_v F is the oriented incidence sum of X at v. Therefore

    L F=0  iff  B X=0,
    dim_C ker L = |E_int|-|V|+1.

Indeed the diagonal change of variables is invertible. The complex incidence matrix B has rank |V|-1: its row sum is zero, and the columns of a spanning tree have rank |V|-1, by successively eliminating leaves. Thus every internal cycle supplies a nonzero solution with zero boundary data. For a connected plane embedding this dimension is also the number of bounded faces, by Euler's formula.

## A single hexagon, with all constants

Choose an interior regular hexagonal face of side length delta>0 with counterclockwise vertices v_j (j modulo 6), directed edge increments d_j=v_{j+1}-v_j, and midpoints m_j=(v_j+v_{j+1})/2. Define

    N_delta(m_j)=delta/d_j, j=0,...,5;
    N_delta(m)=0 on every other midpoint.

At vertex v_j the two nonzero terms are

    (m_j-v_j)N_delta(m_j)=delta/2,
    (m_{j-1}-v_j)N_delta(m_{j-1})=-delta/2.

The third incident term is zero. Every other vertex has only zero terms. Hence L_v N_delta=0 at every vertex, and N_delta vanishes on the domain boundary. Since |d_j|=delta, ||N_delta||_infty=1.

Successive increments satisfy d_{j+1}=exp(i*pi/3)d_j. Consequently

    |N_delta(m_{j+1})-N_delta(m_j)|=1,
    |m_{j+1}-m_j|=sqrt(3)*delta/2.

For mesh sizes tending to zero, with the selected faces in a fixed compact interior set, this uniformly bounded family is not equicontinuous. Any local Hölder estimate with constants C, alpha>0 independent of delta would require 1 <= C*(sqrt(3)*delta/2)^alpha, which eventually fails. Also the constant field 1 satisfies L_v 1=0, so 1+N_delta has the same boundary value 1 and the same normalization at every boundary midpoint as the constant solution. These facts disprove uniqueness and automatic uniform regularity for the vertex relation with boundary data alone.

The oriented face circulation is sum_j d_j N_delta(m_j)=6*delta. A condition on additional face circulations, an energy/regularity estimate, or another global condition selecting the true path-sum could rule out this mode. None is proved here for critical SAW.

## Exact missing premise to audit

To infer locally uniform analytic convergence from the vertex relation, a proof must supply a condition that suppresses the cycle kernel and establishes a compactness estimate for the *actual normalized SAW observable*. Boundedness plus fixed boundary values is insufficient. Whether a second discrete relation, a quantitative energy estimate, or a suitable global path-sum estimate supplies it remains open in this attempt. Even analytic observable convergence alone would still need a path-law tightness and identification argument for P0003.

NEXT: Compare this kernel with the full retrieved theorem and w405's most important bridge; require the proof to name the assumption that excludes it.
