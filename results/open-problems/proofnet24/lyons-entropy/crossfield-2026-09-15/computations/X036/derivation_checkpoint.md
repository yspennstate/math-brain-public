# Quantitative derivation checkpoint

The proof is now analytic, pending transcription and finite identity checks.

Let m=κ²/8, r=|v1|²+|v2|²≤m, R=|v1v2|², q=a(1−a), δ=2a−1, D=vv*. Both conditional pairs F1=B−(1−a)D and F0=B+aD stay strict.

For a two-site kernel J=(u,c;c*,v), with u,v in [κ/2,1−κ/2], s=|c|²≤m²/4, write H2=h(u)+h(v)−I(u,v,s). Its mutual-information derivative is λ=log[(u(1−v)+s)((1−u)v+s)/(((1−u)(1−v)−s)(uv−s))]. Every interpolated atom is ≥m. Consequently λ≥16s, ||I_dd||≤12s²/m³ and ||I_ds||≤4sqrt(2)s/m². Young's inequality gives

    −H2''[E] ≥ 2(E11²+E22²)+16s|E12|².

The exact gradient secant has G12=ℓ v1 conjugate(v2), where ℓ=(1−a)λ(F1)+aλ(F0) and 0≤ℓ≤4R/m≤m. Its diagonal entries obey 3ri≤Gii≤5ri/κ. Thus G≥2diag(r1,r2), uniformly when one ri vanishes.

Set W=wv*+vw*, dotD=W/sqrt(q)+αδD/q, M=C+αD and N=M12+δ dotD12. The conditional metric gives

    −H'' ≥ 2|Mdiag|²+16qR|N|²+α²/q+4Σri|wi|²−2α tr(GC).

After expressing Cdiag=Mdiag−αdiag(D), C12=N−αD12−δ dotD12, all α² terms in 2α tr(GC) have a favorable sign. Three Young bounds leave

    −H'' ≥ |Mdiag|²+8qR|N|²+2Σri|wi|²+α²/(2q).

The scalar loss is at most 25/1024+1/2048+1/524288<1/2, with no rate ratios. Undoing the shear yields

    −H'' ≥ (1/4)[α²/q+C11²+C22²+Σri|wi|²+qR|C12|²].

This proves all nine modes strictly if R>0. At R=0 the stated degeneracy agrees with disconnection of the measured graph. The raw Frobenius gap is at least qR/8.
