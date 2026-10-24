# Scalar entropy ingredient and its exact range

The controller proof uses the normalized two-point natural entropy

    Ent(a^2,b^2) = [a^2 ln(a^2/q)+b^2 ln(b^2/q)]/2,
    q=(a^2+b^2)/2.

It is zero when q=0. Otherwise put theta=(a^2-b^2)/(a^2+b^2). The entropy is q*j(theta), where j(theta)=[(1+theta)ln(1+theta)+(1-theta)ln(1-theta)]/2. On [0,1), j'(theta)=atanh(theta). For k(theta)=1-sqrt(1-theta^2), k'(theta)=theta/sqrt(1-theta^2). Both derivatives vanish at zero and k''=(1-theta^2)^(-3/2)>=j''=(1-theta^2)^(-1). Two integrations, evenness and endpoint continuity give j<=k for all theta in [-1,1]. Hence

    Ent(a^2,b^2)<= (|a|-|b|)^2/2 <=(a-b)^2/2.

No positivity of a or b is assumed; zero amplitudes are handled by continuity. Tensorization of entropy over the two independent physical controller bits, followed by summing data rows and Parseval, bounds J by2(log2 e)IC, since a one-bit Boolean derivative has squared norm one quarter of the squared amplitude difference. The same inequality bounds the row imbalance at a single data query by2(log2 e)d. This proves the scalar ingredient used in PROOF.md and reconstructs the needed A021/A025 interface without invoking their broader claims.

The final Jensen refund also avoids division by zero: v_T=3eta^2/4>0 in the singleton case, q_T>=v_T, and every seed coefficient is allowed to vanish. Finally ln2>2/3 follows from its atanh series at1/3, so c=1/ln2<3/2 with strict inequality. These are the side conditions needed for all constant comparisons in the new proof.
