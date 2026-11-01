#!/usr/bin/env python3
"""
R13 exact checker: five-column, at-most-five-row Kunisky/NAE template ceiling.
All acceptance tests are exact; no floating-point comparison is used.
"""
from itertools import product, combinations_with_replacement, permutations
from math import isqrt
from fractions import Fraction
from collections import Counter
import json, zlib, base64
import sympy as sp

FULL=(1<<16)-1
SUPPORTS=[m for m in range(1,32) if m.bit_count()>=2]
PERMS=list(permutations(range(5)))

def perm_mask(mask,p):
    out=0
    for j in range(5):
        if (mask>>j)&1: out |= 1<<p[j]
    return out
PERM_MAPS=[[perm_mask(m,p) for m in range(32)] for p in PERMS]

def canon_tuple(tup):
    return min(tuple(sorted(mp[m] for m in tup)) for mp in PERM_MAPS)

SIGNS=[(1,)+tail for tail in product((-1,1), repeat=4)]
ORIENT_COVS={m:[] for m in SUPPORTS}
for sm in SUPPORTS:
    inds=[j for j in range(5) if (sm>>j)&1]
    anchor,rest=inds[0],inds[1:]
    for tail in product((-1,1), repeat=len(rest)):
        t=[0]*5; t[anchor]=1
        for j,v in zip(rest,tail): t[j]=v
        cov=0
        for k,s in enumerate(SIGNS):
            vals=[t[j]*s[j] for j in inds]
            if all(v==vals[0] for v in vals): cov |= 1<<k
        ORIENT_COVS[sm].append(cov)
    assert len(set(ORIENT_COVS[sm]))==len(ORIENT_COVS[sm])

def coverable(tup):
    # Conservative: repeated supports may reuse an orientation. Thus every
    # actual distinct-row template cover is included.
    states={0}
    for sm in tup:
        states={u|c for u in states for c in ORIENT_COVS[sm]}
    return FULL in states

ALL_CANON=set()
for r in range(2,6):
    for tup in combinations_with_replacement(SUPPORTS,r):
        ALL_CANON.add(canon_tuple(tup))
COVERABLE={t for t in ALL_CANON if coverable(t)}
TOP=(7,11,13,30,30)
assert TOP in COVERABLE

# 1504 exact rational dual certificates, compressed only to keep this artifact
# compact. Each integer vector w sums to 100 and means alpha=w/100.
B85='c-n<sS+eaW4BU`E%nWOJmHlrc$7q&~Zsk-ex!q<ElMoX8`}eP0<-hA+yRUZt_xq3M|My=?y~^*uiu`f^Ik$^`8UgIS)X%`petKDSglNh!Tw*xRI?othAzV@bKN*+%$9aBJ10ark!7q*9&%phGf0^%JYFFw8HsVV4O3A>x$m>_LU+J%L*`(7Qq6y0UgMR-WSG8!y8tvb@Y__`{&S(u$C9C_I4$b@94Ly>yLVh}8g!T{}rj0y0!*5rFmODh#8Qn$77yNVs3~2aq!EZfnsnJA<?sTjB78);a^p~y?@xaF8TrZb$i%@8uBN~4@LUe}cick>oHwv;SdxG<b2VZcB;TFRAj^Px;ao!-VGrU5$M0r!jdr`1RERljE{|vVf4khw~a}38t3k6nUffXF$XE-W(J9fYpOQgkhYH^)fT&ETmnp1vtf@d+A(T8ESKRC>Gon-YaV^O**Y@!DavUQk2f)97w{Zd{}*W^EX{YN9P+W*$vgsM|o2Hul?+AydK)xb-1g=d1e?8mU&*Ne4@Vc~=@{cPHM=mu~T_*tc|V&J_ld@Dzd*6jf9F+4(eH+%r60PeEN?ioZO&=?>~Xsc>qr7iB(Tm}Vc_v`uXrnDbxJ$J+1!X^H?Av_Sa1&79vTG<+7W1Qg;!!w3g2t#8W;K7R0qY7(@46O&Jtp_&)t6c9ruO<V-(3pF6y7%X|#S?1EYbW0>n>n-=eEux^W@Mp4g<t>RZdz;L$U4J~^>BcTft5nMrD7$9D%VymKj9vKJz{vq@Cx%*YVjwWg0E$&w>zfxsKQwf%(QG@SbFfJx$$Ii86FQlZD&|Gx^`;=J}o>1Zm+KR!zVZQ16Dh4tY^xndjBe&`ekbeTI1e1J-K(&6&LDATk!|jCJs8%87>IpPSo_ZCGCBHMF|Hu8yMRA45t82_p!m#Ewg2%7Hf`BOp^}V<PV`qqwLJ5!<WeIS?oN{tpakj6U2kt$~7bR2hV@t#o%@lc<}iLzCz*tA^Z*g((KP@Sq5P<!P6f}$G3!R=H9(Wu!O=B+%p)n9d8do>;*vZMQGAE&uF%dld$oq^GyGFrhd8Si)qH&11GeA)hG3NH3#PyE*f5!6AsMY06!DW3*S|1f;-v4{QdjB9q@tQ6P_JD1%Ha?;T6I#qR(&&;LO->RWl8S+wQcx!=t|#3u5DqH!k<EPs)x^wFYGEVvYCavSeFbnK$RVPd(-HB~;^i!`;DIx>WX^!tC8QTpe6>;=WU4>=g9*vTdHRPn_YwTel56$*IlT=hrLznm1VoII%VP4HuqeoW4tT1<{diH%An&M12s%G`O>#7FMJDr{Oi9zZ&H~xZ4IL+XD3F=j-a=s$n;|78&GwEc6%LV|c{yjNui+YJ`8nv@#%U23b9}XVp{sPa?~;R@GDb#;1kD=BROVRM#ACt*p`<9pLQX9>YUK@&(WM>lMP#9G&6h;1s~SRzH<(`28ZAnPA3wI_R`8%X6n&{nxqbY@01K8RgG#kKqx+Glmz!17Ir=k>>$UXBaAt)*Z7q$<>1|xW#af;Ss|#hF1uKM9y#u;C7Tqi>ut?Dz~`GEv|BltK8x$x46pvSmhqqsmFEdah-Zxrykd-$8{RVI*qu{BQEra3q9gOkGRnDSm+s-YR09Saj9lps&y>YinCpDwkyomeQJ;}-Ezn2renG(`0(j6^|xqLt)+v-4tG9XTk{54^S(_egHJbMw_2^eZRq38jGJ|vxH_W(xLUY{u->tCYnB>pZ#%;yhGz_~5H2Zzle7=)+BJkC1IrHV;ypnL&Fz<l?7<=LX9K5Hh#`CMy-q*cp8p)STU$FxZp$-d6aE`*b0?<vxkI+u0X_|$uI%s?<0VD-BfR=kj2<yv%^+z0=-WM`IpfukL*z`RC1d^=?ihJnuB~XZkzKvI>FvB#g`z)jb#Re>QLgraNt2lmJgi)^Ue-699W2Ym&fCK?hMz{MzrL`|Mp~U6yqP?~1)F5|RZ}NAq=vp)uVwop9a5iR*&h7hY33f@NRmXV?GCh&Ji|rTsakR4Mv~!X1%?~R0PZn7Vt679z1)c#8!PeG4&KX704F_!s)cv0GPb3W2<==tw#Kln(PDX`5|7zFjv?8>Eh-fX><rHsULhPw1d5GIs+r|!?;+p|ZZSM!c*gJwVW`sqZpS*cxX`GE2k?mD8N(}tp<|!nsLJD5<q;Qp#DyMlp+{V*c`Vh8vz>9aGtPD$vt4nzD{g}oX6rD61Rw5IeLKpUKfe4^ErwR-jP4nap)xr}PDdvVBouR0y)K_eIs0*twt)qAMJFpO=-tDe<sd`MtdELm4s(#vjBak!8DQj_XSQMdN)g^d|4n(%n%*v-{$4->xNws-vxXtO`|nT7>5m!fN*><*tOHzLF!ZxCoC3HV<=#Z4*!rK=H~<HU{Yu?-sk4WZs#JNyg^N|b;4PA0JN(-H_fPWh7Re;o7ai*S4ew%q*7-Tosb?>7WEhdX6Bsc(V|az|uGR@o$7&^Mi=X5!H}*1~76x#MvW+Ezhk*e+VtB^z3gL3ca3s&;l$1*>krLOb#C0lhol0Ejc`Wpdvz>9aGtPD$vt4nzD{i6{W?PP3zC>+Xz81-HT!V_)oE6+@>m{=I{TVP`X&lFi_z?$ij^Pr+^E4rfAMqJJw~_b}pWu3wYK<jQV~Nzb$~EZjh0nCka9F2ytW%5Y)Z#j|xRqO6<rY`D#Z_)`E4NT0r^Tnl>qCjxhZ3(3C0-v&ygrn8eJJtz;K!py;zH-R&^a!2j!Si%#Bw}GgsWDGSFIASS{n`}9Zw;rMXkh(T8S66!lx(!9F=MvOSR%`SDft%vn}^2TRKHKei)~F9KqpQ+P>D(cAOzwJVUm4j%)E8*Wx*@#gkY&j-3_{jusD&77vaV_x^V5{VneOE$;m-?%wU#y<6P9Tim@{+`Zee8@8|;YB8uko@9r1ig`>elpVl9Sx&NpfYvbGKz0ZR*&bxKk>JDiCA)R3#EL7i;!3Qz66-X-LAY=DVLE;o)LsMXkEhfycJ(_oh|6(N=^T<XFY@%(hz{4Wfz$x2a2+^4y$!76b^2o+YZh(>7MD(db;QkfP`8Qeh?_6iRm;ITX6E(v5^JG4dfW&`y=01#SYm=fT-hSQwYpfm8j;Qy-q<Z4ahLwkK~6dn0`ZAL-DXT}Y($)*dgyf3RxfAMCNEfG0sw9nuJUz#8r*%Ynrt8I+M?$k!^7k)$EpBB#M&9A2A>=522LuRT#nfRkzNef1!VEaAObm7_Y<Ls%)9o*CtP*7sr;r92J`kAR&Ku9nV#UPFDy`A0)(qjsil0E2_7*#V|aydkvNE~o!vPe5996A)eRyNoe;^tES$|%3bvQB?<K*ur?Btk86NtYfbI(It|qW>u3r(rfM^eO6BA4DFyDHZBWl0kcFeZL**0;E|4cV7RXfHH6PyBg91A_-Y=?HZ|ALiA{R{pMTLvU3?_htCEaMCPwV;3BdZid9`Z9In;{x!KfV&-BluWu3eaU#Xc;aCX;axU$eI~WxZebPLwSP8qHGtq8!q!X;pij8R@Ce~@$8ZYZrNaQT78otu4TDj)x?}OG+bbu%unu0hJFYHS*<cYLs2IR5b81y<@WMT)KTO-;OBM+THM=kSdCvM6@&^wK7af23IA&Y8@)GtGzG$su*p)kNUwD^#H)YGFH!ab{AoG0Lnw2|-lkTdI-Alm<<Io;lMg9YXZ8|Xi`1yBtgpAr8?Ec&s<sisTt+H&Zq+5cfwgRjp+KE6xQ{c$9Y`=I26A1;w5MPC)MYLlermJPXO`v9d6(Q5DL=yv8r^E4HB98R*c#-dStfwm=s~8RYo-bfC>95!K{SO>h+&n&JBM#)e1#b?=KvXRM^xsoZ^$|}7U$zID@GRT7Nv2_#rhVHa<32E*zCJjR^GRWx2+g#P8@udAnkW?Xei2ms^V4{?`I3%*e)_kadDxE>0%11Z9ZsQnaN|RM;iBmQ-W*OU2;okItPEtBc3tyGbl&Ov6@Sl4%n45sE(dQpJIP~6*SYnpzR1AE`69tKj%&MW+UAJ~>kh7_>Flz=VO?3ORvq3=)$bQRBrwvr7$dIq!*4uAxC#L*W<^TsMzk9{r4^jH25859x$kq;@U((y+GTyi#lby>M+k#d&T!IQYF=88fnuW~YIL9MThpq9970uDBHh75i@TaqaS#;5yTOHq7FJ<)+M`D9+xRSW^WY2aF+4(8#|FMjg@qmnXAAdZp?h4a9+#?X$NNus1%;+CrsLOPoyM_F1fD*`QXS!P$8eHJ%ipYb>1EVa$RLvLzWgScbU8HVkZwArn>?uCrDyGD;_e1=mp<7gfAO6DdH*C4tl72btpX6p$OnXvES53j)ypLinE4hj8{c-m#q&1bq^RP32u~5-w82WPcuPz>T(sn*(?mL8AvHQX5NIa_4Un94nz4a8d)#6-2Pu8F(rLz>bXbLD@%)Xp=lO*jgPu`Hwt5ZU7x8DE4o?w2aYIn>k_K?FvxLO`2NZTIp(zr`w3+pUBAXU)s`Xh=7lr#6)|)_$K!)&TaTX#a;PE7Q+1H3@oc7CmTbS_z8cWFPbONrwDvpqO=Z1vr2!)k<5Oum8VH(qMaY9%kgwLL+w#Jlz$7Oo~-|L>5vs3~0z}Z$IThHk1^h+RgQvx>}$(aNUQ7~SY#ntXUn@B9e)nM4)n<^Az-maJJ26Xbx=R7Z1=RPjmN$6-B6CXw+TD-V?THfWr4^8XSf1M1huL`!;FIlH|!~&;xW~_tLI}vg=vqXIp%E9TK2uH7YxgQF4<$L3AG2GZz8a-zGA%l!gyo$XTO=j|JuB>6klJ2=}ILi_8Er&C3i(U1MBpo<g>j)CE$>W2d=7DVn^7Y_zvAhXQPc_JBf90XZVbwRBF=6~wi1}9v>yH%5{TCszr3wgE)_Br@%c>PY6GIs++u1jE6GIp?ZpX;CnX<EQ?IyOcj%iF!zzsEu>4Q*&u;=9N3DXd=6SUlXjdsQ2<k<LTF|^1QCr7#O4$M*3W(bU&v`y~a@0VEpD%drBi^$D(kGyZEs3L>z<>MjzVo+U)u^fTxN(3YCFzA69a%PSKDW1_~s!8tD9T|ho@A-D;?!bWF533yH@?wbA3k+M8#41O*F$UkxcogfvmUOGxBcm8&ZgC<fk5(K6pq6CM=+bN-LoKUgUzm^lP$Sn?Q7yj8vDhpNjO7S)l!J<9eiM=`G5IwXS-)9i8ZTa4S;RHSI+{GA#lpxUjPH4eTxMnZ{>nv+_#n{b2rLYmcV2`fvqpIfqp+<H<$e2N7QQVWW~Sw`C}K#*Gaz4$!gnHq;{Hy7?yH39^#f0`20XZ#8p-YLya@2kBey7|%Mn;kFnQiiPRmWdzKlzb1NK;7ukX1I8=tlgY&xij8@(^_y^u7ESd4FmOnm9)^o%0sN&B=;&mqa27*sk?s-Dq!V#mYd<QZrar{^`^47ykz7Z`nLgoOMT0i#xspwFO@fY<cmlx=l}Bu5AAN;Thk^uGvbisfriUxk=bjc>w|YHWgU4>IST33%rt6Ks2x&ud%}GdJ({kJc{c?p<JH&k#4A1pYO*V`O={1k#wEP~<+*uCLf-Lj9{0%5C6~hd2&E$M&*NS1$v>7oyyzl*2Ve5$~OZoz@DIF2Tc_fGs9=!A@dqo}o@cyWh|xw%nCWVyeC=DxcP2V|_8QVVF%(GN(c}5{4&KIdUGK<)pI&40~>_vFJ1*BH-B&ULV{pFHX9jmkF;@(!t%01TStrUOEzzA#~T=bWetN)J#c^m{`o&3#rL0I*E}SgYQIrU1Y<IEJbuCA|z1oUqZt0geu3^<FlOX19l^0dIBB|VN;ZM9(1C0BcXf3G+BJ4u%sHpZHkgP6+04=jLzY9P1_Zh{S;`9a*OMdUR}Q@sbv<F17q;=j}axeXG~V2kdZt?b)5Dd!AsVZ>F(BMLW&4EY4>U@ME49eA6IApL`Ihp;7>A;F{FQ2xBW}92Z#vv-m>Z{lFia|zh_<E13(_>qas-rr%n|ap3zKI%SRe&!ut}2x<&ZLG?pjG+W^Vii;=O|mtpVNUrF$kcO)bkMw?*eS!6x|dvNlFD6%@hDwcfLDWaDxV!YB&GfMkr3>nT%Uw_5~@$0}OZqHa!mCq#j(3%Kd7(AzZ6L1|wWggE<JOka@h0#2N_Ltc|uE30`-O%=x@Sd@ZqtW!jsItLikI@%Hc9_7h;*zK0P-8Dn*W}~)OzL#;1#M<}obMGcEBhJWsFFNm8O`7$4H^c_@Kxbq0P9h54cq<B;Z>9VXHB|H^t|#W&sb(*O|G0>Ci)|RHV^BwB7-jjhC(b~%Hfyh`-4F@EZ>mCaySp86Hd+_32-~PPPRL+j^ifRDQ_{PPcck0?~V6RpJv`0?~%OBWYJ%hkR=zMdswgUd8)t{6HF!9Q=#GaZYRpF3Y~HLeG+`9Z_El+KN9CQiB)zc<ecp6#Z{aV7R|?2<FB%-xM^{+dQFvW1@Eq!FJin0tg@~6-UC+IRwN<3@)+lhXq8PtL{J(>cbkH0t}^UqQmD@F?5!tMQRu%edt!#YY&E+&ngEtlCe2*uTAUo4_S^%)E019cQJk1eYzJIx)jUC6t=gPEUPbEy6||yjhhxY~OxR76XQ=*gV2FDtTnMrpLBFx%k0`3BOi<JE5@t5fB;w(0_Ka$VmsJ9)s7%}~lCMZHO;)|WQ$=N}RM6yVQnY6w5PVH|5+j0bk*Z&v+qMW_5z==$`P6?ghPX6?$tyXA4hiU9o2jC!@DS*(s!hkWrRLY~D!R%+rLUr^9Cqhb^b8(n`Be<vciLOx-E15BN8eGAP+xj(6+Ppyepb;lxSStpC@<&K-hHR*sHvAKTt(3!!g2|isH{(%JLlnh-8Y-nBC0H~mGS9u^|Vg23v87I7H0Nl7g+NYgzHQGF$lc1Fgu2R)X1M@sTU!58nVh_b56&HB)TCKUj_5DQMRu5Nj>hs1T(2OV`RZGr6=_!n?qP$vp<4wGShwCMa7IRs?>p@Dw5o=YG!A5B&Y|vZa334Gt+gvk1ci25T6XV0WUSr7&66Ve~i-ft_+_78@{Sm9m&oX)by?lCGLBt4&qFoy;JSV@T&5c#EnxrFnlp|&&Y0mP;WcHmg}n&U0St#=Fw%Vl5u%*^6cii_u}>e>XnB^_4puA$Ect6kPQ_OmP=rm2f)5?b~;Dgr>{J;pD}JbCeL%7@#%4Sf#u`-q<x|v-BRIMR!)4;4#Gp1XLN8aOP#`!x@S<dBZsYJ$0)aPlQu&m%hD;=OK5XMmZcN?d?--WGX`2`I8e5D#+2uQ{mv-M(up@RRJSwAvUG}jSN~unabzp*ri?6$Cwd|HL7ZjzJos{ESwKOrLPqioi3EgDC|eHa@|f_I1II|_Wx?druqNB71^~o7SM(K?KVD>^z*m|za-m!j#WC|9VW?*<3f#n@-GqmF)`A_Slxxs1?^@8y(L9)jde@?g?~y4rKjM_}8dHuE7%C20>gC}Pe?4P(N#gkp(<Jcub;5hn(YLx8NJKiwe_%KQdflL*v5QC6un%8AG^IY19y(^RDgU+P2pCO*&8j;4(2rkm!>QGI=%B_y{@<#r5BvNDh({?)Lx(L6DdTcD1}0$%+Ut9K#{tuqXA6dXUIX#=!k778Vkm|RJFK^)Z}5z@NAGz9@zbv0RiTa6LqDG(SKK)9XYu}k$`2>qEY2NJx?!aw?=kYo^7t^{FDo5+a`E{6ioa*GDd9$X_!0)Wgc*n*AHj~%+yJ7>Rx>|w?z+D`harSy3EX*;f0=RUCov)d^={|@$;zj2@8;e=9p23M+01<GixJ?|`w4e4qGwEwIQ9O5xDz2g$%Nq_Z#+eKgZt27NjHN-UdKSmB-c3dK1R;=nbV=)#~?V_HG?0>K##r4bxe66gW&4m8N(}tVa~`5>%|btO@SP@L3qz5GkS3ZHQO1jd8kJ)q`ze&b$$hdq%w`r_!W$d3RE{j1A%@PTuJ+*vG^5?Gd#4sx-Ato#u;9^o7oARU%@!T$yCc$Y#ggBuV7%zhE12=swfOM2d^mGxK#64swuL<+BOGA+0HoIb<B3f>C!70XE?~#VFn34<cGs(`p?Z`eCG&m!Kz-Jk<qkLy!Q*9f%d*c_r0h|3>f4_mN1@A4M-%IWiD&|2nl#j3uo53s=<SVWm2e@uSXH(9SBwwv<jmNVKG^T=~fdbCRv9AMlh{u*T_L>)Hj1P(L`=)uUu#~|Ij40cV$E<tZM?n3xlUu&?r6#%V?|p@`a=*>ob8?R3g~M!q<jK8?_iOs<a97VkBQV-spX#k<spv$xAIY&yXVGnf>h<)TeGN$M6Jvu?uVYL0Fsu5V|AqQbhz?%EgL5?yrU)oAS&h!qfGK#kxNe%+Sj>2erY4FWa%$Gi2urt}eDkD69sDkG<N68AG;l-8il=W6DONzh^3XR0PWbk+`>Gu&RDzIgB(YtOg0?J<cht2D?sqkI`&)gUMQXhH;1EnV@)akULz+KrIR9o8kqQ^gzb>=EYcHCug6!kdb5<OsoAXC$LI8Pi+Po+C8f#j)n3CEqW;7h<-5^4;5f6M=1EN5k>&quAEag(QF1tp0Uh;_IXS{UVR=*m(pCZGqht!gi|FDH|eVvvj8_^nO?fY05olAQ7=b<u0SzRj*%1Z^|N&h8~Sx9a8S#BwvqRtU@`&P@PuyiSnm{uq+o9N8u}S1uu1}<83OH>(Yw-Oq7E&(P@^~o`^?{TCr9!Onhq1DF+8D363w{XGh_Uf#N@UFmxtvE<kyz)+76!rhaM$&FUQbNDSZZp4*i-^%&<05I~B^CN_Zb%HNmArKdY2UbNplsF_M&blW>F~8}FNIcpYJQQ#pJZ?DTkMB$0W2H3~a-fThTrB9YNdRkG`U$}uCuN}GH!is>74tFU7%Y5V$_1}~HubFo!v92qL@);yz|maQL*!AkwtP@-Ki-UT?nbCK|6=;yCAsNDia5}|kP)`R9lk@@{CuffsFIIkt&NrzTWuvKoy&~`-QVm$Q2RoIKy$7q^zPXx?;z6Yv+#hc2R9D_p^&kQwlj8{38_rvz7y38U#d#!~xtt5wWOrjjpOwXt?>kQ+fIQ08dcn_Vu@OJ1Ys9+Gi^=5hX1{%Y;I1l|06&#D$phPCvf=)9%7O{+0Qd;ImCS8hQF6?B29C+Ewd53-w3#&Tak}U7LL@CfAan3Gmap-5U;Do?NC5j0f%yC;+wU}Jxz>QTLBPY`o-8U9_iw<clp9y)ANT2DR(c<>5d}$fC_wa;ilJJtQe6JbGX<WV#e+W`c&B>}R#TlE^@cUwUk_!y&_<CsajQl4<EY`_f2gZadeH#AOJ)_C~Xn6Ifi1X1TQCBC)#&2aaVR(X^2>{_$OfeDz!Iu(L@raPvJ`M!aAQTn_7es^eZ@xW44sXEo&`wmm5A1yJjcZg^ex_n1&rto+x=IiIco@pt`eP6Mept+qQxY3zHt4ahKg5ysA@^rx^PiQ?a@3tjq}en6sI0tf&kWOf^p-Z$-YI)V6-!=6<DX+RKIK4%(Bc{WPsWgPG<Ptq-ZH~hv0<Y_KWB#BxY^Sb^`Kcukdq)FSaDU+^Tvners$v~h@{TVO&WBlQ<6Go&W=HfOTb8Cq6M>v6_>b0avyc&XuKe&<pZ;sF~q>yO^6^frVRV>(a)Q#6g)*H$KV0^J&E$6&n@eLZMXhsRr;S*=`!4IDn{{)WeVz-6m`pJz({7%@l_cz5RwlPWX3d0O7c}1G7z$lT_OgLgiN`-7-}dCX8@9ix<ng$$!nVFX?~39Y3AYsBbl`;Ie9I=`n~G9{POq3Fm+uv4|4zF^>Mib$omV9@k|ud(2wz<zB8;b3$>j($beEUhRV=n2e>x_=I~6H?3g~KoTw*VNmR`65GU%I>Gh<KBnH-i9$OurAg8`If_CUv{;J%~s<jYtqOMg4rjS{AXWUec;TftL*;^&VMY>kSxIIHvB>QznUIxU1X19!p7j<nyFtSj$MkiXQ_1J0R89;{UTwRm#GScwGCMRFl%D45Ryq2%4=&yMC)O;?YzXpsUR`cR#)+UR@qEmz~#*%g`-Zn3e)-i*|SpFIX+5;eYH)&=}GYY;Ks_BcLOT<sPc464IpGJ?VUKf%lAY~{epULz?CAmzNloO11P8KvL1~}CMCIg#3PiO;iJ)tSbU2v?Ys}wu~@3evnS(}=2?S*i|?3ZlqxC?KLc>Q;eA-15S)opl&n33?T!0a`Fp|r8wz8Rv8;r(1mGn98Z8bejTQO5drq-x4~5x__}dwn)j_zuVAHxxoCCQMXz1I*Aj{g^ONIx*mr6BO2~u==__Xf>sJ3PoK&SB;B-P`X6BS+lHAhTQsR!*iM9BI24CyoyuARPrm8B8M0OWl2!xfuir#u}T-6W0=4=9d4b>qxPToJ|^?3z1+vRR12AB?emoP8l^k&JMZ;my-emQcsVqguT-R8Q!c6zi(JDUX2hp6WNOkjFQF9K?$}$=5<k(MPafPt!BY+Kjd7`n(@A<gPLj;~)^MpNnL`yt1w>aRmue_Enc~`~(1e0^Tdc7wZvDHsRo^a1oyBI<yrW99W3iYKJ!$VWY>k>ocM+w(D1}v7+JU_&Q!c`Q5p9c`<*tm=2*~OZilq8Ww-mVng8H_l$XSW>I!95vHBLg0023xzZ}SIDVYze`ifYDY<ib~|=~=hwved!_5$W=E-kWk?{toWp9_M=@fW7CXp(9d0uI?T>rsREl|Ik4rD(lOpo<|7ln5h@c?@_T&9mjSJ6S~1MB{HIi3Ehy#DY*9!<3IiJ{)H*QhiLWnmMq$&3#cxy<SIz~iefBm0j{TK<izj3kpsME6scww_ee#U(#&|?>KW_U(CXgD_Z9BLIxu1_ZguiDtOFw!0sZm}Lp4WXTe4x$<9?LOp2s~yJxFpZPcV*z!I(jMZNUx-bu$pQYJS&+V+L8A(=}UGoxj?5PprINeTzWfb&|+JC`$^VT^SWcca7aUmS?yJIx06THJWL+tfqGH2<7O;cjGgq$U`3}Q&re37a{r4^56g1-&cM'
raw=zlib.decompress(base64.b85decode(B85.encode()))
CERTS={tuple(p):tuple(w) for p,w in json.loads(raw)}
assert set(CERTS)==COVERABLE-{TOP}
assert all(sum(w)==100 and all(x>=0 for x in w) and len(w)==len(p)
           for p,w in CERTS.items())

# If d is the minimum row l1 norm of a template matrix with support pattern H,
# then for any alpha_i>=0, sum alpha_i=1,
# d <= F_H(alpha) := sum_j sqrt(sum_{i:j in S_i} alpha_i^2).
# We certify every non-top F_H < 177/100 by rational upper bounds on square roots.
M=10**6
worst_num=-1; worst_pat=None
for pat,w in CERTS.items():
    upper_num=0
    for j in range(5):
        q=sum(w[i]*w[i] for i,sm in enumerate(pat) if (sm>>j)&1)
        z=isqrt(q*M*M)
        if z*z < q*M*M: z+=1
        assert z*z >= q*M*M
        upper_num += z
    assert upper_num < 177*M
    if upper_num>worst_num:
        worst_num,worst_pat=upper_num,pat

sqrt=sp.sqrt
T=(2*sqrt(2)+3*sqrt(3)+2*sqrt(51+3*sqrt(6)))/13
b=1/sqrt(3); d=1/sqrt(2)
a=(T-b)/2; c=(T-d)/3
assert sp.simplify(a*a+c*c-sp.Rational(1,2))==0
den=3*a+2*c
x=sp.simplify(a/den); y=sp.simplify(c/den)
assert sp.simplify(3*x+2*y-1)==0
Ftop=sp.simplify(sqrt(3)*x + 3*sqrt(2*x*x+2*y*y) + sqrt(2)*y)
assert sp.simplify(Ftop-T)==0

# Exact attaining matrix from the preceding R13 obstruction.
A=[
 [0,a,0,a,b],
 [-a,0,0,a,-b],
 [a,a,0,0,-b],
 [-c,c,-d,-c,0],
 [-c,c,d,-c,0],
]
for row in A:
    assert sp.simplify(sum(sp.Abs(v) for v in row)-T)==0
for j in range(5):
    assert sp.simplify(sum(A[i][j]**2 for i in range(5))-1)==0
astar_supports=tuple(sorted(sum((1<<j) for j,v in enumerate(row) if v!=0) for row in A))
assert canon_tuple(astar_supports)==TOP
for s in SIGNS:
    vals=[sp.simplify(sum(row[j]*s[j] for j in range(5))) for row in A]
    assert any(sp.simplify(v-T)==0 or sp.simplify(v+T)==0 for v in vals)

# Elementary exact separation: sqrt2>7/5, sqrt3>17/10,
# sqrt6>12/5, sqrt(51+3sqrt6)>38/5, hence T>231/130>177/100.
assert 2*25 > 49
assert 3*100 > 17*17
assert 6*25 > 12*12
assert Fraction(51,1)+3*Fraction(12,5) > Fraction(38,5)**2
assert Fraction(231,130) > Fraction(177,100)

print("ALL_CANON_SUPPORT_PATTERNS",len(ALL_CANON))
print("COVERABLE_CANON_SUPPORT_PATTERNS",len(COVERABLE))
print("COVERABLE_BY_ROW_COUNT",dict(sorted(Counter(map(len,COVERABLE)).items())))
print("TOP_SUPPORT_PATTERN",TOP)
print("NON_TOP_CERTIFICATES",len(CERTS))
print("WORST_NON_TOP_RATIONAL_UPPER_NUM_OVER_1E6",worst_num,worst_pat)
print("WORST_NON_TOP_F_UPPER",f"{worst_num}/{100*M}")
print("STRICT_BARRIER","all non-top < 177/100 < T")
print("T_EXACT",T)
print("R13_K5_TEMPLATE_CEILING_EXACT_PASS")
