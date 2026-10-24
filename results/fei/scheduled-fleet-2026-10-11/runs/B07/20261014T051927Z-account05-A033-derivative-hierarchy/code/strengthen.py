from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'PROOF.md';s=p.read_text(encoding='utf-8')
changes={
'H(S_Y|S_X) <= 4 I_Y(F),':'H(S_Y|S_X) <= [3/2+(5/2)h2(1/10)] I_Y(F), sharply,',
'H(F) <= [8+4 log2(65/64)] I(F) < 9 I(F).':'H(F) <= [6+2 log2(65/64)] I(F) < 7 I(F).',
'The constants are not claimed sharp.':'The conditional constant is sharp at the three-bit point defect; the joint constant is not claimed sharp. Neither constant increases from the accepted single-nonfair result.',
'If N=1,m=0,':'The separately frozen code/three_endpoint.py tests all 5^8=390625 height-two rows on three physical bits, using the complete identities z_s T^2=product_i marginal_numerator_i(s_i), z=W^2 and T=sum z. Exactly 2208 nonzero product rows are admitted and NONE has two nonfair marginals. The direct-character independent implementation code/verify_three.py reconstructs the same full census and histogram. Hence N=2,m=1 is also impossible in every data dimension; every N=2 row needs m>=2. This is a complete reduced endpoint certificate, not a small-n extrapolation.\n\nIf N=1,m=0,',
'The first two lines give conditional payment at rate 4.':'More precisely H(S_Y|S_X)=Kcond/4+2e with Kcond=3/2+(5/2)b>5/2>2; therefore H(S_Y|S_X)<=Kcond I_Y, with equality for the three-bit point defect. The bound b>2/5 is certified by 10^10>2^4*9^9.',
'For every remaining nonfair row m>=1 and N<=2.':'For every remaining nonfair row m>=N and N belongs to {1,2}.',
'At c=4, put a=log2(17/16); 2a<1 since 17^2<2^9.':'At c=5/2, put a=log2(1+2^-5/2)<1/4. Squaring and simplifying the equivalent positive comparison gives sqrt(2)>11/8, certified by 128>121.',
'H(p_J)<=m+4sum q_i+2a<=4(m/2+sum q_i)<=4d_J.':'H(p_J)<=m+(5/2)sum q_i+N a\n             <=(5/2)(m/2+sum q_i)<=(5/2)d_J,\n\nbecause the difference is m/4-N a>=0 when m>=N.',
'Summing proves H(S_Y|S_X)<=4I_Y':'Summing proves H(S_Y|S_X)<=Kcond I_Y',
'                <=2m+6sum q_i+2+2l.':'',
'Put K=8+4l.':'Put K=6+2l.',
'(2+2l)(m-1)+(2+4l)sum q_i >=0.':'(1+l)(m-N)+2l sum q_i >=0.',
'4log2(65/64)<1 and K<9.':'log2(65/64)<1/4 and K<13/2<7.',
'constants, which are <9':'constants, which are <7 (Kcond<=4)'
}
for a,b in changes.items():assert a in s,a;s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
