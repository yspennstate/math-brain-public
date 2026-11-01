#!/usr/bin/env python3
"""Exact certificate checker for P19 Parts-509 sqrt(3)-pair equality witnesses.

Source geometry: md-amer/hadwiger-nelson-e5/v509e2442.vtx at public commit
6d5ac08491f7cadbebd7d5b79e3f825d08eedf7b, Git blob
be867848302657c36aa51481292a0a2e7390fca4.

Claim checked: for every exact pair of vertices at squared distance 3 in the
original 509-vertex / 2442-edge Parts graph, at least one explicit proper
5-colouring gives the two terminals the same colour. Therefore no such pair is
forced different in every 5-colouring.

All distances are reconstructed exactly in Q(sqrt(3),sqrt(5),sqrt(11)); the
23 witness colourings are embedded below and checked edge-by-edge.
"""
import base64,zlib,hashlib,math
from fractions import Fraction
import sympy

COORD_PAYLOAD='c-pO7%aZH54czA|X6a*|E)PXf8hyuIrp`wsmEEoUdu+)MiNvcNFUKYc0w91!!}Is|@2~Iw{^Rcx>R0;u>tFx=&p%7~^Xrm_-(RP4-ah#Ah3%`H*RO8t=f`KS<#?=4?dp7)et+dlf7)ewe0#!hmiAAIF#TqdCMak1a;GY&Vy(yA3sA2ES3B6&5ygSh#_;2}cGxDm5SpF}<E81acs0Q3X`^4a6-$3y-6?WcYVQ}}wwQNz@3#n7c6MOtg*exm4m$)@v;1M%LUa8V?blF0zHftgsu&$c+!p(NWG-n)>#b1R<V)vGYNYGZtC6y#xHV;GGHGNgEa6$c>aivytP;#1<J0Ey-8RiLlloiX)1%%5Q_H9on@VPAb3-t7js4oEJ~=aK8m^g3(8}YM#h>-#kujPglBuvCgv>$dcgjTNSmmKlRhbFzEgv4VzM2K6r(t$k^Jtq)<^}Dt3`U`12%1CUIRO2eSU(w5*pUmH;W8VgV#wG#3RghjC^=hMIrONjp2P<`hYwzX;cPRT?m{d_I>npvFKh)d_}~JBwMB(Y7+-o^_R68+`&SPe{A_M}vxkj~l}`keSsm~jK||Jh3HUl_9GuE<ttiHSw5qobmJo=EMTfSi77qOu7W@ufsX`%xws2ViicqpaE-cs;Ov@x@wTqPkeT;)Ub7{`h9jnvj=QbM|eb3OYg^%{k;Lc<+7~04(A(f>JT)Si{Ouv<kpk`sCpcDoe8s)4g4z@B~?N&owTsvzc*tgoZfTPo~MNR<(W7BXP%|$R%nai3@^NpUcGryOSk_oLUNpMmPIG3kjdv*J^o*m=VGsW7}Gsj*SDB@L2%Ad>NMZIvq{m;v7yFklr{r+)L-wsv|y;mWJ77B0e3im^A*y%3Dh8pW3%Vc0HB*n$|Z8aK>GjR7AY|q;HK56<lPYuLVl`y#7{!)=M*y(v@2R;;f9sC?=MF>I=#aIvb0y97Mp-}DMRY%76$EVw|T+a_m|IT~T=Y_UXgSIMHvS+3nn@O^sEZNhM>}!D}+!b=(aVQipcygvl`^uJW%d_7*7VJ^Q50A!bKspT2QYAW8bwHuj8RU+=mF}np_^RSDFm92uw*rJU0zfu^pm;@u`#3{Z5@a<-N6=m9y<J;j!@0fN*!7rJ?2KJQXvLy0exXOXxpL^`YW+&$BP{f|SO|HmuU=vqVw5Yw1BEQaxbL*Y=Ww$C)@F`rXrNki?N~M)H9AsV4NI(;#SIl8nE?wiLBvAL_Fy>L;$%BVOZ@m8N1LOAhQC#$FTfq|FsWmo?b#Fen;(xsBMME8r8^sX5LM?!|G}aE*k30|9D!l)+0Eabef1ffM0FX=m_T+}JX&Wf^&;@KDnz)=9Lte2H`$PWQ&EVNc;~Q+N935sEmX$Ve>lOw;+gE3OT476{e0~SpFL(Q5_M2S-XS+|bE8XY|BEg8;})#SLLgoU&8;D-CNf0!RI-wJxlp8Tu`s8HYy`wMxQ~4BANj)K%3@*R#~71ha4Ux*iyb1}m21;Jba`)7C*_ejmSx?{W%E&;=qf#ip;XRfhGyr*(>{U~KEf!AnVW&iiL{!NvL-h@FQDN+Epe6(nVQ(K9i)cGvqeDfh9pS&9S1GHU*`$q@4-Q?U7sOeFg#L*iIOE*jnNTw7<zx}bY<xi{}lh_k{i=x3aIhXvaQnWC5TE5Z2OKvkL@17oA8*J*t$wBb}12g74COGxstzJT5L?=HHV`;Wck+X_2k5-I9;5YG#qIXY<0T-59r5<92vJbqm>}D<!qrSzuSL7z|&H~>Za)sa7X_$KgGY3h(I-(VmgpnM{aiid5isukw;75?$%Q-7KtDoj__4r=mgCUk_ec_N7z&M?$rGug0VvTsgTf$j7(>1FCK@NHud)X<AtwVe_HZ!y6atcUa56mx`oy4qPafLOS|)Sew=PwmaVw%G2xJ(cD=4%Uc%Br*s_(aTdI8QXzspq(M#62?2Nw`^;+ENwTi-Nqbr|w`gLxCVUuuO_vBgDMS|I{)qbPm`y+1VUjMw}<RevoeFc9mtA$U&dmwy~m}-P(P*j7X8)C{4y5YX)a+N+`PCtkA{=CG^&G~llQTpYSr)EQHHo)Gola5Y2y5rzo0MeCV?O4N6j&3;`XC)ZZJ{W}vxdP5xG)`jR-xEn5g$mxq_LfM7{INWebXmJRqREo-NU4!Lk`yZ?+e%=}G?l&o{R}v(7x&!TNJ{TYie>f5Do8s68HxK|kk;c${2k3|HS%9kVgwnX<~^cfy&nOg?(AW1g}v7@CHL4uQ9?+9{@OUN;cZDCgy>!(-j5(hQWVXJ@nUXv_FBfILcmqgvLzGMF7SJl@NoqYqmBoDBsgGI{2!^{|8xR|osv7PHu!PKgqmJY_uP(CE9&m-GB~*W5K~M4(r=(dEvKy@wV1kcZeoU=nASXpLh4!PcxSwM=jJ{2cV5fr^4`OpRXHyycLcsfE5vJOo}Peld9#YmYL0I&*qDJTC2=WBxY#*n;K~BwC(GQ797GM_RfN_MupTVoDR73syYCL+z;Mc&XNdG><T{=*lKp&^39)+y>wEs=ENV+#LXWK+y5*}==txj!-k0^KZ5^$xW=Km;Nkp_{l?2fb^!X@=Ved^KA;d=vX7lviZb8EBo|B6YrQ^VyH-!>s&pq&ZJEy<Veuym<-WBBc!Bbp_YAa|&&0Yi3r_DVl-yqhDb5EN>1;vSskk;=8x92!1xf1Mb5_xBvc1|JMnIUFVgmh-;^dytc4(FU=oHNCz3pcTtGOjmW0^CKIOH5uaf<+dStV@6_PBzJ>(x5ua7bOkd<61)4MWZq9S+c||AiYEX@aj|ZtGO=GE?xzp%1bEEe~k-^&^tg!hEZX4H9&~KY_W)j9w2QcKy}-L_7-$oW-BnGitMZf*;<GT@r?!FBY5v+IYMTO8Vm+V#8yVw_8xrwCgI%7?C!fCd(VfGCvQ*Ic6j?C9RT|RaBl$T3V5}BPS=-0%`MgSr9f-T^?b=_Y~}Da^^2$nPCo<`1gjx4PV2xr+ZlbPefDvWHWM30W1KdO);Mk53VZLTnoM6oVw~1D;s1}<@U|p+u#1oM=rBj7FntWc$1pcLdq37>#sDuN>D_L&8QH)Z*`&b8CdJ20i2i6poM)x@YzVP|7W~1P16^VRI#CY67*d4cr>a9Dd9xI!iIPk@5xgXS+((ii!TctN-|`tyf-M9^7vf_TB18%h)FeDI5fnH1#&Ms3QVjP?g?oSS{{VeI%R>'
EQ_COLOR_PAYLOAD='c-rlpYjPyH4TS&e6mtZ;?teCGS|so#s>h!2#@HLN3Pnq;ez2-YAdyIbWk2jk{HV{z&%gQk`1<+zihusj*Ka%T`}st^9{Ks2zaIX2$6lYd^WFUXTd&vbeAasWI^VO`?>L{!*Y~_XQRjVsjpS#nJHm{YumAImmwh$SXMe}P=NUMDzFzzKzh2{f9qsG8agO?R7GJN#d7l0F`o^8HI>(CF_;s#*zJKTI&Uu}yx$oJT2|Guza~wbK*IA!BpQ}F8dv*C5^{#B-xt;Tiz7p>%vh%%aD~L0D_j>EhZl3Y{9CK!^dcCr*<({kck-p|T&I}Y*FV3u8OR=6&>mw&t|E{9-Ec1xob6w|b{LD`DiX>+Lu3PmyWY6(^UOiiNt~AbbJ1d_U^V+T-AM!Iwv}M^@f#`L){!)0%)tg+09czyB+t2)4f4cgts^|Li=fiqcuC>K^K3;o$@Y?CMk8E$cSC?nzv(H0){LV`>l0<v8B7=#25Dn_gP~bWYV{q;1&)Ilz*Dcx;E+W*K3&-<0`bD(tGZ?G7zOPrF?W+YFx^rp3S8Gq#F?lY2&}7C=@e$4zv7q|Aye;Ko`L(UW6;@yStk<<-dZ_n*)~N5moq|OVqDA9J^+*Ziv-WO3qwy*Xo^WGNoTGaqw4MK|V}bWIX0Je<cg8lokuW6^jh)XGS<lx+=<M%ZU%rS@g1RniQLsdBOxJS_SgE&V80Nn4?L42iM&?16i_%}7KXY%58V-*vVC?v$;~J~4Ir|E$<HE$a>}X-QGM9C@nB(n9cl^O?VnX(R)hwYNb~ZRwuuyLc_eLSc-|V9ntU;qm_G%4J7`Bo)k6Ec|e|8+xfDi=~2%y%SQ6T!y^;oaK_3xRDLfp5$+IyCE)}qdu8X^VpDG|907GaG()tGX>Q*9^K2&vd={k>>gA1j~uXh2+R&*VA`Mj4pO_1eMT>UniUh|4&5<+C1v*mgOcgNsBXYG5_zoC{V##xcJW?7$FhtXJ9kEWM-ZT@8a@jdxs|O|q7cVW9=)mhiR|bSZe|Mfc&jfwM87hPS`Yd|4wzb)+&d=YU;I%qQYquPMy9`hYcV3?KKNWyUM(bFW6gY%3h(@t)P_D;l03ZCzwoYQKdUNXZ7QIjv((9RH8kTU$@HWd=A|!p6P1{ls<e$T|$xB>H<Z6K}M?mOMz2f=UiPRKP6F8p(~x7ba5Au^i{j_+`y;h+5eZFOUr-FkaEtm(LJa3uh3Lr<LTq)fvvP*g3~&=9kS&teG2e#$n%qXlTfovt#OAS3?xY{vF8N3cNMiUw(SNAuqYB8O`aVJt+}44B4sXss_)G=4#cp6rHILQ<%JZW;okc28GD*sy%Mbn%Q`@om8`eYuS@e2Q1q$_cIc64~;^TO-^QinZxAj1x|G{1ja2#cIKVkIpWS_PgF*{6_xR#S+lz;jum&H(b!T*+*Fnp!l5RoqBd~Hw6@_uEC}J4)_I8uA1}<Z9ltW*5Hn+)4Mzs#64zZ2kSyCUZ-aJ@93$x=K!f4a<I{<iACxo11!`5pPZL+?Z}LEIOR2R2DZ0Vng2DR(@k@QM<JSjscVc<9J{QQrtud&;0Vc~%@x(wrR=uJDrNSF!qHSiPR3S&Rj%wBGoo(MKK0P{FHY*r^Gs(iEt!Okm@)HNc8OArBKNwBUA7GTx3S4&F8ntQi<rLovD2EOn9GHWN6&ryPalW9=&imPZ<f1Hkubv~qdfVq{V`S5#vX-1Ta}Q!ez``f0m8@Do*K$#zm5C1jP1p=skvGl;a?rv$<-($r+_T#EU39|ug<{Ff*pSUTSkYhsvweq(t}K?S%`nt#FY;cy>@0e4)1ccL*nYNUcw;5CEW_Fu5Ioy<ylqdlNng6DA=7u*dG#z3n})$L*DtZ`lBniDeDA#5pbie!7vj&T5{8)_)JQPBXs+j?oh34X(ZsT?lYV8$NogM`N_uqG7Q#U$b_Nh5pzDp=<lr=cn3#)w4(bNZDWPFUS3V}+9FDxPB&9Oph`fo2VM|X+a2+Z*4pd;=9ezg~PT^GnhUB6|jQx<c5NW*g1_uMSw#x#7SED0!wnPRutd^>t36_lS4kL0fX=;Guht(NtE|r4yI7X2Aa6~)<rsdK*`7`?Eyk?@G3}a@7V!%yD&L0x<164pO2CNwjh6f@MIeI>r$?(n)-MO%abJT=Y7ot>j<WXH(|DQ99*5IS#?$(bJI?hyAM)4{<Ph=bVDHDq-c|D+-&l#0)O0I3l$`_)*#4CD{L9b(V(7@nKvRwz8cKl|}?ox*x9$?5w#wN8Y7|5s%IH_8_OLf|?DjY2_3g2^J_C8u-+*q{_R#hC>Nj=x``FZZ5bbI4szIlw=^_-cXG2hqtg^FOd7mjypmXSb>f^L_M^^P;NW}1!|pU9CCC`HA^P`Ra!OH?=Eqm!{GvgVY?mEdesA4pLsQZg#)cP4pjNPUg=;83NR5jr$OVxvhs4bfJ8)qU+T6Z4%~)qts76e5vf#vN6vLbg1L3KifKH8)XRN{LX0E&xYPXC0vpb%R1(gt4fQu^Q%4ZOm|{^hJZcneg^_aG!*7@y_#2a(9zl=IQwX&f@4^30wua0k!q*`NYBTFjm^9jxk<gV0Ad7567HmTcL>}>p-ljQ|wqzZyzmBKds*xlnBv2QdIarra)DP)eF`D$yy5Pd`YEa*!9>wzs2K|jcW`EVJIPw!WuiGzKMEkQnN5r$^!9Q`Tb-BhPp4irKW-ut3xQ!b3}&dJukyd=GB6_>5|=-#3SvQGVmeC83f|IzT%=NsOk_46%tDOsCNl<BGDVb?>*x^z0Xi*iWMybwTQsn?f0iv7_0gbf=4d#-X+&$EH8=U?Ejdan?waI;rX?C$qw)MV0Lf4`YxWP%4whq#%hSxxD2z;I7d#a6^{U8m<)Mdn;02jt<~|VRt7S46J6B;%P;8?a<JcQj5IuZR^}&%m@LsyAF;M92LjgWXmR*>H7?fT0Mxt+IY70ijE-6h`DkOT<FN8HsF17E&^j)-uzYqNaMXh3#Hz@o93i0vFgCKo(!sS1I2EX+IlRs#_9yT;(20_QhZD&Rb<<yY{?zXM&F8%Ny`dK<pb`Y;k69LLl_B|#LqE;V4NGt^r3U5?TTSE=Uu>V55^MhKDI-%UvFDI36O$}nxzjW5$D{6IsBbU}4PbY?;bw_$fkM5^u-*mMQ&PicCna^`e1qm8b*$-gHB_HUuFoG@)8GknxI)g5_!N&#r7%%}Vc#hGKnkoV(VMr`-eCj*k8{zJ6U@)hBg+0`gMu?PqD0QmimaoOZ^$DZy}6ElY3+jXjs}K!vprw)Co*PhWj=*_kB_L=r*tnGa_;^9M0f|g;wsjPiw?|YFT6%`^6<nQYlcr{c`EtrHv0Vea8bTW);^?jD9|BDTuOAmE3PHhm7Or`pm6k^I^yJLI*HhqtFwK22*$b`DiFJA*j>K6M;tZg!1xZeJ!EwgnF@KFq2D5rmj?7J7q9Y#`$V4M-3d+1gh7lRp;fg+#;;Y*@k!n5K#t42vf!&BXv7r^#FUWSh@8NI(T=rq>E>XM$wa@D41TXwE|0fg^i;;uGTB!g=uvyd`jC}z=(_oq8>Hk<hHe%z5^{ZZ;cUHb_kG0LJMm86(|&cy`#)TIRD4D3K*zW@59hpTEY}?ivFZV==I*W$cDg!rZxilltJ1iuD$}LK+5zXOz*DsQ#H3@S1iNcR{aV_QNtC9-#tIhIWpbiGkEbEd@yt`WeKk8*b!qE`%Ia-(6ee~a<fE@4&{tZhlLq>?1NHJiogzhfP3eM~%3ChA+Slh|VKc|pyg;!eq*5KrisDUtci4pPEwP0HDfSak{ib_{eR+l|pu@J9$r!3-DYcDw#D{vLyZh3Msd;S8x%H+G?)-A;>KQfES0`PfI+kEYy9<-(HAu`1!KEiF(en_ZJQsX8rHhSP(bi0LWP?iNGIO?&)#RCWp5>~RvTB%u9aNCCI$;v^HEP!KUFLozyEe#~44uItedfwssmhgfF0un5q^oCkmKZeB*+nxb=a0Tz?g9+S!3-69m+Cw-?CGOQ>4C}zr>8DwqH!ncDw<idmonkQ&s~Eim1gQETC>**YN8vUR`$r+6Zao55(l~q0%K@x)Zq`qXLVnoOV!yA+b{4S!ycBsZ&dZ!T$O)COR`yNwITSdU68)^5jwh?3(8A?7jWfFB2RYz``|;#{@#>$6|&bX(0!e&S~HzLj3>4BO%#+t_Ui?DdJWxg+8boDFEb^(pWK!#T5I^+?^UqI$!QCD2;&xW4&~&Ab9LE)P|^*>ioBsZYO;6BvG2>#Vei=aJ&KZnl`zVyLTumxDOH`23R5l4A5xo4)Wbq{5wYjfz%uuKm0Z<AtpGcADjBf3&^h6<KPDyb&lR^+)enjMA-Kw2d0(A8xvHoBP!1irW};8ZrTbjt8MWJ7yLPD9s{Y|p3*DNDJ@Uwuz7&UA?x@;xUrz~g6jsBqk}3L43Aan(Pl0{TDfvZ6ZOOo)c<t;aGVrsMYTn*u9O&YvzRKz%``Ea1A*GXAYodm=a@m2XJD;cam(b6&uEOVuowO$1Sj^h9<Gih?Ho7G{p!ZHtd&7A5?C*Mh{6;-LAIQHe)9P7)49<inv8w*8=Z}iw(1t^hvsV96qJqnHiAM&S(98XU`_CK-gUb$wy)(klr){V|*qa>-tfHD|b+M|3_F$|bGv}+C<}#*92fudd6m}Zts=kzDhJngf%6^4_Ux)0=)7@Ty%qY?0V~s^FJEv2s<N@wdqPB5HSh-Hr$>zQi0qYE~;Y3~0pgWZ)T!pc1_1cj$OhslGBX@#?+*80-$6h`9>kNCa9T_1xsR_SzsRFw652VEZTpHQb4pKg$YyK|R-~Bs@80AvcW989ScVS|^sSDJb{N9%K!b*ESc6v-rPxqG=dl5c-jUR2JzIr+h2o<RB?CR$ePua~==)1MmVVI9>!l9e%__oF`<mB4VT+-R5b<NSt4SnG$J&n2IMuPtv6v3@umfYQhJH$e&4O4ZtH~k>2+=SF=QaTo>ycA+&$ZnwmuCud=%JSyrx}!@qrLp_x-C`WQ>1w_9i>h8oCy&c6D`FtozDt&DZ~mI($A&$ljJVV$W5xVu)PE{hwUEM~hbJnzE_xvM`PJ(CblIQ6%AQH?TBw|cRQTf2X^OiXe3;~KDGKec?#7k>;ci?modzj<=+}4Ss^7R9SN)s2amC|qT(<7UWwO6%>qjPcP^rIkH?Gmw#s~kKyK&_oyc<_SiF|iAu0%)C@7|5ea5pZ0+=u6P@5YtuZd?KGk+9zHyK()syK#NrhwuA7eE+Na@a6yMK78@*`QM)Z?fL(xJ8<S7kNNhu^nCyJ{BO_yzW44M&$mAi^GkM6{M}>zzW|bOof`'
EXPECTED_COLOR_SHA256='119a6170bc58ef84a9bf056548266100ac7366d7f4a8599f61bb1a6dac4d32e5'

lf=zlib.decompress(base64.b85decode(COORD_PAYLOAD))
assert lf.endswith(b'\n')
remote=lf[:-1].replace(b'\n',b'\r\n')
blob=hashlib.sha1(b'blob '+str(len(remote)).encode()+b'\0'+remote).hexdigest()
assert len(remote)==26023
assert blob=='be867848302657c36aa51481292a0a2e7390fca4'
text=lf.decode()

# Exact denesting of the only nested radicals in the public coordinate file.
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
    body=line.strip()[1:-1]
    expr=body.replace('Sqrt[','sqrt(').replace(']',')')
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

targets={1:[],3:[]}; DD=D*D
for i in range(509):
    for j in range(i+1,509):
        d=d2_num(vec[i],vec[j])
        if any(d[k] for k in range(1,8)): continue
        if d[0] in (DD,3*DD): targets[d[0]//DD].append((i,j))
assert len(targets[1])==2442
assert len(targets[3])==1175
edges=targets[1]; d3=targets[3]

raw=zlib.decompress(base64.b85decode(EQ_COLOR_PAYLOAD))
assert hashlib.sha256(raw).hexdigest()==EXPECTED_COLOR_SHA256
colors=[list(map(int,line.split())) for line in raw.decode().strip().splitlines()]
assert len(colors)==23 and all(len(c)==509 for c in colors)
for idx,c in enumerate(colors):
    assert all(0<=x<5 for x in c), idx
    assert all(c[u]!=c[v] for u,v in edges), idx

remaining=set(d3); first_hits=[]
for c in colors:
    hit={p for p in remaining if c[p[0]]==c[p[1]]}
    first_hits.append(len(hit)); remaining-=hit
assert not remaining
assert sum(first_hits)==1175
print('source_git_blob',blob,'remote_bytes',len(remote))
print('vertices',len(pts),'common_scale',D)
print('exact_unit_edges',len(edges))
print('exact_d2_3_pairs',len(d3))
print('certificate_colorings',len(colors))
print('first_hit_counts',' '.join(map(str,first_hits)))
print('equality_covered_pairs',sum(first_hits),'uncovered',len(remaining))
print('color_certificate_sha256',EXPECTED_COLOR_SHA256)
print('CLAIM P19-PARTS509-D3-NOFORCEDDIFF-15 PASS')
print('ALL_EXACT_CHECKS_PASSED')
