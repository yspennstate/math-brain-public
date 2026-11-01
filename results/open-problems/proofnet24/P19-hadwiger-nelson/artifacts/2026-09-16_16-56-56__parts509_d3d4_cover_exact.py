#!/usr/bin/env python3
"""Exact self-check for P19 Parts-509 d^2 in {3,4} terminal relation census.

Source coordinates: md-amer/hadwiger-nelson-e5/v509e2442.vtx at pinned commit
6d5ac08491f7cadbebd7d5b79e3f825d08eedf7b, Git blob
be867848302657c36aa51481292a0a2e7390fca4.

The embedded coordinate payload is an LF-normalized copy of the 509 public points.
The checker reconstructs the public CRLF/no-final-newline byte stream and verifies its
Git blob SHA exactly, denests the only two nested radicals by exact identities,
converts every coordinate to Q(sqrt(3),sqrt(5),sqrt(11)) with common denominator 96,
and enumerates squared distances by integer arithmetic only.

The embedded certificate is seven explicit proper 5-colorings. The checker verifies
every coloring against all 2442 exact unit-distance edges and verifies that every
exact squared-distance-3 or squared-distance-4 pair has unequal terminal colors in
at least one certificate coloring. Thus no such pair is forced equal in every
5-coloring of the original 509-vertex, 2442-edge Parts graph.
"""
import base64,zlib,hashlib,math
from fractions import Fraction
import sympy

COORD_PAYLOAD='c-pO7%aZH54czA|X6a*|E)PXf8hyuIrp`wsmEEoUdu+)MiNvcNFUKYc0w91!!}Is|@2~Iw{^Rcx>R0;u>tFx=&p%7~^Xrm_-(RP4-ah#Ah3%`H*RO8t=f`KS<#?=4?dp7)et+dlf7)ewe0#!hmiAAIF#TqdCMak1a;GY&Vy(yA3sA2ES3B6&5ygSh#_;2}cGxDm5SpF}<E81acs0Q3X`^4a6-$3y-6?WcYVQ}}wwQNz@3#n7c6MOtg*exm4m$)@v;1M%LUa8V?blF0zHftgsu&$c+!p(NWG-n)>#b1R<V)vGYNYGZtC6y#xHV;GGHGNgEa6$c>aivytP;#1<J0Ey-8RiLlloiX)1%%5Q_H9on@VPAb3-t7js4oEJ~=aK8m^g3(8}YM#h>-#kujPglBuvCgv>$dcgjTNSmmKlRhbFzEgv4VzM2K6r(t$k^Jtq)<^}Dt3`U`12%1CUIRO2eSU(w5*pUmH;W8VgV#wG#3RghjC^=hMIrONjp2P<`hYwzX;cPRT?m{d_I>npvFKh)d_}~JBwMB(Y7+-o^_R68+`&SPe{A_M}vxkj~l}`keSsm~jK||Jh3HUl_9GuE<ttiHSw5qobmJo=EMTfSi77qOu7W@ufsX`%xws2ViicqpaE-cs;Ov@x@wTqPkeT;)Ub7{`h9jnvj=QbM|eb3OYg^%{k;Lc<+7~04(A(f>JT)Si{Ouv<kpk`sCpcDoe8s)4g4z@B~?N&owTsvzc*tgoZfTPo~MNR<(W7BXP%|$R%nai3@^NpUcGryOSk_oLUNpMmPIG3kjdv*J^o*m=VGsW7}Gsj*SDB@L2%Ad>NMZIvq{m;v7yFklr{r+)L-wsv|y;mWJ77B0e3im^A*y%3Dh8pW3%Vc0HB*n$|Z8aK>GjR7AY|q;HK56<lPYuLVl`y#7{!)=M*y(v@2R;;f9sC?=MF>I=#aIvb0y97Mp-}DMRY%76$EVw|T+a_m|IT~T=Y_UXgSIMHvS+3nn@O^sEZNhM>}!D}+!b=(aVQipcygvl`^uJW%d_7*7VJ^Q50A!bKspT2QYAW8bwHuj8RU+=mF}np_^RSDFm92uw*rJU0zfu^pm;@u`#3{Z5@a<-N6=m9y<J;j!@0fN*!7rJ?2KJQXvLy0exXOXxpL^`YW+&$BP{f|SO|HmuU=vqVw5Yw1BEQaxbL*Y=Ww$C)@F`rXrNki?N~M)H9AsV4NI(;#SIl8nE?wiLBvAL_Fy>L;$%BVOZ@m8N1LOAhQC#$FTfq|FsWmo?b#Fen;(xsBMME8r8^sX5LM?!|G}aE*k30|9D!l)+0Eabef1ffM0FX=m_T+}JX&Wf^&;@KDnz)=9Lte2H`$PWQ&EVNc;~Q+N935sEmX$Ve>lOw;+gE3OT476{e0~SpFL(Q5_M2S-XS+|bE8XY|BEg8;})#SLLgoU&8;D-CNf0!RI-wJxlp8Tu`s8HYy`wMxQ~4BANj)K%3@*R#~71ha4Ux*iyb1}m21;Jba`)7C*_ejmSx?{W%E&;=qf#ip;XRfhGyr*(>{U~KEf!AnVW&iiL{!NvL-h@FQDN+Epe6(nVQ(K9i)cGvqeDfh9pS&9S1GHU*`$q@4-Q?U7sOeFg#L*iIOE*jnNTw7<zx}bY<xi{}lh_k{i=x3aIhXvaQnWC5TE5Z2OKvkL@17oA8*J*t$wBb}12g74COGxstzJT5L?=HHV`;Wck+X_2k5-I9;5YG#qIXY<0T-59r5<92vJbqm>}D<!qrSzuSL7z|&H~>Za)sa7X_$KgGY3h(I-(VmgpnM{aiid5isukw;75?$%Q-7KtDoj__4r=mgCUk_ec_N7z&M?$rGug0VvTsgTf$j7(>1FCK@NHud)X<AtwVe_HZ!y6atcUa56mx`oy4qPafLOS|)Sew=PwmaVw%G2xJ(cD=4%Uc%Br*s_(aTdI8QXzspq(M#62?2Nw`^;+ENwTi-Nqbr|w`gLxCVUuuO_vBgDMS|I{)qbPm`y+1VUjMw}<RevoeFc9mtA$U&dmwy~m}-P(P*j7X8)C{4y5YX)a+N+`PCtkA{=CG^&G~llQTpYSr)EQHHo)Gola5Y2y5rzo0MeCV?O4N6j&3;`XC)ZZJ{W}vxdP5xG)`jR-xEn5g$mxq_LfM7{INWebXmJRqREo-NU4!Lk`yZ?+e%=}G?l&o{R}v(7x&!TNJ{TYie>f5Do8s68HxK|kk;c${2k3|HS%9kVgwnX<~^cfy&nOg?(AW1g}v7@CHL4uQ9?+9{@OUN;cZDCgy>!(-j5(hQWVXJ@nUXv_FBfILcmqgvLzGMF7SJl@NoqYqmBoDBsgGI{2!^{|8xR|osv7PHu!PKgqmJY_uP(CE9&m-GB~*W5K~M4(r=(dEvKy@wV1kcZeoU=nASXpLh4!PcxSwM=jJ{2cV5fr^4`OpRXHyycLcsfE5vJOo}Peld9#YmYL0I&*qDJTC2=WBxY#*n;K~BwC(GQ797GM_RfN_MupTVoDR73syYCL+z;Mc&XNdG><T{=*lKp&^39)+y>wEs=ENV+#LXWK+y5*}==txj!-k0^KZ5^$xW=Km;Nkp_{l?2fb^!X@=Ved^KA;d=vX7lviZb8EBo|B6YrQ^VyH-!>s&pq&ZJEy<Veuym<-WBBc!Bbp_YAa|&&0Yi3r_DVl-yqhDb5EN>1;vSskk;=8x92!1xf1Mb5_xBvc1|JMnIUFVgmh-;^dytc4(FU=oHNCz3pcTtGOjmW0^CKIOH5uaf<+dStV@6_PBzJ>(x5ua7bOkd<61)4MWZq9S+c||AiYEX@aj|ZtGO=GE?xzp%1bEEe~k-^&^tg!hEZX4H9&~KY_W)j9w2QcKy}-L_7-$oW-BnGitMZf*;<GT@r?!FBY5v+IYMTO8Vm+V#8yVw_8xrwCgI%7?C!fCd(VfGCvQ*Ic6j?C9RT|RaBl$T3V5}BPS=-0%`MgSr9f-T^?b=_Y~}Da^^2$nPCo<`1gjx4PV2xr+ZlbPefDvWHWM30W1KdO);Mk53VZLTnoM6oVw~1D;s1}<@U|p+u#1oM=rBj7FntWc$1pcLdq37>#sDuN>D_L&8QH)Z*`&b8CdJ20i2i6poM)x@YzVP|7W~1P16^VRI#CY67*d4cr>a9Dd9xI!iIPk@5xgXS+((ii!TctN-|`tyf-M9^7vf_TB18%h)FeDI5fnH1#&Ms3QVjP?g?oSS{{VeI%R>'
COLOR_PAYLOAD='c-nQDS#kqO2t@yV3Lk;({%0Gx1<9jlCLEHrbXOISBnh%#`;FiFJpTUY=kfjf`@}!b`8->H?|nr+kNkY*&%>W@?77<d-u(Qp=QHbTP3u?RXU}u=b@|-qx}y4fe^&BdYgX9x@_C=VUdo!#>1X{pXJG$)KKs6}XPxhE-+QBX{hs3cN%ZT~<9o+=ta`6_)~~jG?;n4S&#SGO@2ovxy^Hle-rrZpr~10mNyoZ;R-MQOUR$3pWQofn>-$P5i1yytTkYNK^}P37ua)AJvSrR{+Ue`>Xb%*k7wxq{ipis<ofFZYD4M*?9bLYzK8?3`LJ>)Lf8tj1L(0eVy5y~DOQT;~M?SIUVAnf`yjKY!%Q^y~xJ<qj9&5cFJFL+h{p{_3)77O@m3;mA`!Pjj&=&oAvvzWDa60%%Wz$%f?fKL>ZjO&%LQE3M>dOpv@If}H_E5kM!y1e|^Et%_6Sq(%3?o$g!tr`{A4W@^U{N)>e=SetY5_yzO9Q`}GX1W}vv{+~uAL`G=q++V>0B<P43`hK3Ko`Z-*^p*nW3(CCf0ZGP65%&Xd(V6t(0IsQ+9i=Mk@@NFtsOocNarjzbn-OmyM|iRDZMBbTMI`O0+m%i%k9+hECl#xjc+fhjsnLqJTsfr{A*%Q0hX4!S{u`v#&QX^RmmZ^f&X@_a@eGWMqM3Hzyr7mTXR0SgH$K<5JbaV40sd4ClBqY1Uu9CMTrcl~h9g3unty1%$c~?qVU<-_))JG~8;Eiq`6cRV#^eY@|y0?AX)55Cs+pu-2X^Q2o~)Qv@cz*BgbpZ?bkyX&sB|m>Mbt`6*Gk42UqXPl;3Jo)S(>40*ZLbYBSTi}J0H2F5jICgZRiWl$=UwadRHzd9<!C=Ob_@d(tm(R2<i5@OUqH22H}R8Vp3b3z>$s*Neirc=7A>O{kkSDPJ!*`#XuSruAPZi#Hm!!Cu)9Clxg8#s-DHC*|+{xUH{sZtq~a{w1x^T~LVH3g5~95C_5>T#EsS+7iIFEL;Wh08oHuZApIogYFM71qUX!2@}^0h6Y6_{8ykv)+WB5;6mtEP-*Cw%@w$s;sME?Noo4GI6o}AbFW04=XwJP=T{<*GO$ly|9&f_i~(>^~<Dj$Xcn27wCo(9Dmu?UpYfwEu0`upH`>mEp<4nV)u+8<(JYWCgnz+ao{^p4GkT0s-{j{4OJlZ9O&E%x;2z9f0=LSOD38jO&`jnMBOlSr?*!%WPV7im9P}*)K@8NU%ehqVP#o}3a^xLdun#$C7hI0!61A4=>W1FzTcJDd)z9t-Q;%mqa3zZFKDXi5LmYy-I=SqbJU&fo;VqCO;k3EHf9qQN5ma$v{;H$H?K;IqoKB^;%s2nG+{VU3*u-@Q(t07j~BdbomU1PVrP84;pl+;)O9}$NR@5y+p?Xb$4F)f*kJYa=5!+R%W{Ugz**Jm(}Z>YAAO(;DfNm#p1HyDf+70@_3P%K>eml@cXD}YJ{Rc0O&nCv0NZ8f$;3cER*Gm~QsH8m5N5VY6?!yNRV&3ih3`B$y>qgZD%gCp(}jmnv@<*E6NkcC#kZNi98Jw1P?VtwT&iyEv}yb0Jh>H^96EGxzz16^-VBte^M&c`exJ%CKa)jQ^c)q|h0mRhQBCiZwa&TOdypFf2;Zt!Cu)JYmY*r~RidkZ6PTeYa`9}S2Q9=YUtE-@_blbUpE+Ut&%~0Qv7wuHsG{WpcKePg`c<)<+N?rNWsxg(sV;hX(=fL+sQnZ&TwKXnmLWC<22Wwfg}pnQ^w-?f(CIsHUh*QjX%!rM{W{35Q`H=d@9Mh^)4}EXLjBpPgu%1R8VRKr(t3VoXNgW=XJRRIGOr9hDe;kKk{;^X;%JbqodL!O%=LEK<j^#MnwT&3xvU#FQ(}f4`sHK$&DF?nF3I!Dgro8%Du%u0NeQjP366smSa(<7k%#l>s(?cBGl^LIP_>Y0Tz!K>0h@4HVDJ(<a?Y0M;8xXgs%M8wHg{JMIg~VKfSZS<jx}FX3jQ9)3Q|A+09QeD;{'
lf=zlib.decompress(base64.b85decode(COORD_PAYLOAD))
assert lf.endswith(b'\n')
remote=lf[:-1].replace(b'\n',b'\r\n')
blob=hashlib.sha1(b'blob '+str(len(remote)).encode()+b'\0'+remote).hexdigest()
assert len(remote)==26023
assert blob=='be867848302657c36aa51481292a0a2e7390fca4'
text=lf.decode()
# Exact denesting. RHS are positive real numbers, so matching squares identifies roots.
s33,s55,s15=sympy.sqrt(33),sympy.sqrt(55),sympy.sqrt(15)
assert sympy.simplify(((s55-s15)/2)**2-sympy.Rational(5,2)*(7-s33))==0
assert sympy.simplify(((s55+s15)/2)**2-sympy.Rational(5,2)*(7+s33))==0
text=text.replace('Sqrt[(5*(7 - Sqrt[33]))/2]','(Sqrt[55]-Sqrt[15])/2')
text=text.replace('Sqrt[(5*(7 + Sqrt[33]))/2]','(Sqrt[55]+Sqrt[15])/2')

def split_radicals(expr):
    syms={}
    def is_sqrt(e):
        return e.is_Pow and e.exp==sympy.Rational(1,2) and e.base.is_Integer and e.base>0
    def repl(e):
        n=int(e.base); out=sympy.Integer(1)
        for p,k in sympy.factorint(n).items():
            out*=sympy.Integer(p)**(k//2)
            if k%2:
                syms.setdefault(p,sympy.Symbol(f'_r{p}')); out*=syms[p]
        return out
    return sympy.expand(expr.replace(is_sqrt,repl)),syms

def to_field(expr):
    e,syms=split_radicals(sympy.sympify(expr)); primes=sorted(syms); gens=[syms[p] for p in primes]
    if not gens:
        r=sympy.Rational(e); return {0:Fraction(int(r.p),int(r.q))} if r else {}
    poly=sympy.Poly(e,*gens); out={}
    for monom,coef in poly.terms():
        mask=0
        for p,powr in zip(primes,monom):
            assert powr<=1
            if powr: mask|={3:1,5:2,11:4}[p]
        r=sympy.Rational(coef)
        out[mask]=out.get(mask,Fraction())+Fraction(int(r.p),int(r.q))
    return {k:v for k,v in out.items() if v}

pts=[]
for line in text.splitlines():
    body=line.strip()[1:-1]; expr=body.replace('Sqrt[','sqrt(').replace(']',')')
    depth=0; split=None
    for i,ch in enumerate(expr):
        if ch=='(': depth+=1
        elif ch==')': depth-=1
        elif ch==',' and depth==0: split=i; break
    assert split is not None
    pts.append((to_field(sympy.sympify(expr[:split])),to_field(sympy.sympify(expr[split+1:]))))
assert len(pts)==509
D=1
for fx,fy in pts:
    for q in (fx,fy):
        for v in q.values(): D=math.lcm(D,v.denominator)
assert D==96
vec=[]
for fx,fy in pts:
    vx=[0]*8; vy=[0]*8
    for k,v in fx.items(): vx[k]=v.numerator*(D//v.denominator)
    for k,v in fy.items(): vy[k]=v.numerator*(D//v.denominator)
    vec.append((tuple(vx),tuple(vy)))
primes=(3,5,11)
mult=[[None]*8 for _ in range(8)]
for a in range(8):
    for b in range(8):
        f=1
        for bit,p in enumerate(primes):
            if (a&b)>>bit&1: f*=p
        mult[a][b]=(a^b,f)

def square(v):
    out=[0]*8
    for i,ai in enumerate(v):
        if not ai: continue
        for j in range(i,8):
            aj=v[j]
            if not aj: continue
            k,f=mult[i][j]; out[k]+=ai*aj*f*(1 if i==j else 2)
    return out

def d2_num(p,q):
    dx=[a-b for a,b in zip(p[0],q[0])]; dy=[a-b for a,b in zip(p[1],q[1])]
    sx,sy=square(dx),square(dy)
    return [a+b for a,b in zip(sx,sy)]

targets={1:[],3:[],4:[]}; DD=D*D
for i in range(509):
    for j in range(i+1,509):
        d=d2_num(vec[i],vec[j])
        if any(d[k] for k in range(1,8)): continue
        if d[0] in (DD,3*DD,4*DD): targets[d[0]//DD].append((i,j))
assert len(targets[1])==2442
assert len(targets[3])==1175
assert len(targets[4])==582
edges=targets[1]
color_text=zlib.decompress(base64.b85decode(COLOR_PAYLOAD)).decode().strip().splitlines()
colors=[list(map(int,line.split())) for line in color_text]
assert len(colors)==7 and all(len(c)==509 for c in colors)
for idx,c in enumerate(colors):
    assert all(0<=x<5 for x in c)
    assert all(c[u]!=c[v] for u,v in edges), idx
pairs=targets[3]+targets[4]
uncovered=[]
for u,v in pairs:
    if not any(c[u]!=c[v] for c in colors): uncovered.append((u,v))
assert not uncovered
print('source_git_blob',blob,'remote_bytes',len(remote))
print('vertices',len(pts),'common_scale',D)
print('exact_unit_edges',len(edges))
print('exact_d2_3_pairs',len(targets[3]))
print('exact_d2_4_pairs',len(targets[4]))
print('certificate_colorings',len(colors))
print('covered_terminal_pairs',len(pairs),'uncovered',len(uncovered))
print('CLAIM P19-PARTS509-D3D4-NOFORCEEQUAL-13 PASS')
print('ALL_EXACT_CHECKS_PASSED')
