#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using i128=__int128_t;
struct Act{int A,B,dh,c,m; i128 hb,lb,rb;};
struct Aff{i128 C,S;}; // C + S*t, t>=0
static string s128(i128 x){bool n=x<0;if(n)x=-x;if(x==0)return"0";string s;while(x){s.push_back(char('0'+x%10));x/=10;}if(n)s.push_back('-');reverse(s.begin(),s.end());return s;}
struct Bound{bool inf=true; i128 num=0,den=1; int typ=0,h=0,k=0,a=-1,w=-1;};
static bool frac_less(i128 a,i128 b,i128 c,i128 d){return a*d<c*b;}
static void tighten(Bound&bd,i128 C,i128 S,int typ,int h,int k,int a,int w){
 if(C<0){cerr<<"BAD inequality C<0\n"; abort();}
 if(S>=0) return; i128 den=-S,num=C; if(bd.inf||frac_less(num,den,bd.num,bd.den)){bd.inf=false;bd.num=num;bd.den=den;bd.typ=typ;bd.h=h;bd.k=k;bd.a=a;bd.w=w;}
}
static void mergeB(Bound&a,const Bound&b){if(b.inf)return; if(a.inf||frac_less(b.num,b.den,a.num,a.den))a=b;}
static bool min_less(const Aff&a,const Aff&b){return a.C<b.C || (a.C==b.C&&a.S<b.S);} // one-sided t>0
static bool max_greater(const Aff&a,const Aff&b){return a.C>b.C || (a.C==b.C&&a.S>b.S);} 
static vector<pair<int,int>> pairs654(){vector<pair<int,int>> p;for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)p.push_back({40*i,40*j});const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&x:ex)p.push_back({4*x[0],4*x[1]});const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};for(auto&x:cut)p.push_back({x[0],x[1]});return p;}
struct SymOrbit{vector<Aff> r,s; Bound bd;};
static SymOrbit solveSym(long long P,long long Q,long long r0,long long sr_t,long long R,int M,int H){
 auto ps0=pairs654(); vector<Act> as; as.reserve(ps0.size());
 for(auto [x,y]:ps0){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,(i128)(9LL*x*Q-10LL*P*m)*R,(i128)(-11LL*x*Q-10LL*P*m)*R,(i128)(9LL*y*Q-10LL*P*m)*R});}
 long long s0=R-r0; long long ss_t=-sr_t;
 vector<Aff> pr(M+1,{0,0}),ps(M+1,{0,0}),cr(M+1),cs(M+1); Bound global;
 for(int h=1;h<=H;h++){
#pragma omp parallel
  {
   Bound local; vector<Aff> mr(as.size()),ms(as.size());
#pragma omp for schedule(static)
   for(int k=0;k<=M;k++){
    for(size_t ai=0;ai<as.size();ai++){
      auto&a=as[ai]; int kh=k+a.dh;
      Aff HR{a.hb,0},HS{a.hb,0}; if(kh<=M){HR.C+=pr[kh].C;HR.S+=pr[kh].S;HS.C+=ps[kh].C;HS.S+=ps[kh].S;}
      Aff LR,LS;
      if(k>=a.c){LR={a.lb,0};LS={a.lb,0};LR.C+=pr[k-a.c].C;LR.S+=pr[k-a.c].S;LS.C+=ps[k-a.c].C;LS.S+=ps[k-a.c].S;}
      else{int kl=a.c-k-1; i128 common=(i128)-40*k*R*Q; LR={a.rb+common-(i128)40*r0*Q,(i128)-40*sr_t*Q}; LS={a.rb+common-(i128)40*s0*Q,(i128)-40*ss_t*Q}; LR.C+=ps[kl].C;LR.S+=ps[kl].S;LS.C+=pr[kl].C;LS.S+=pr[kl].S;}
      bool rh=min_less(HR,LR); Aff xr=rh?HR:LR; Aff yr=rh?LR:HR; tighten(local,yr.C-xr.C,yr.S-xr.S,1,h,k,(int)ai,-1); mr[ai]=xr;
      bool sh=min_less(HS,LS); Aff xs=sh?HS:LS; Aff ys=sh?LS:HS; tighten(local,ys.C-xs.C,ys.S-xs.S,2,h,k,(int)ai,-1); ms[ai]=xs;
    }
    Aff wr{0,0},ws{0,0}; int ir=-1,is=-1;
    for(size_t ai=0;ai<as.size();ai++){if(max_greater(mr[ai],wr)){wr=mr[ai];ir=(int)ai;} if(max_greater(ms[ai],ws)){ws=ms[ai];is=(int)ai;}}
    tighten(local,wr.C,wr.S,3,h,k,-1,ir);
    tighten(local,ws.C,ws.S,4,h,k,-1,is);
    for(size_t ai=0;ai<as.size();ai++){tighten(local,wr.C-mr[ai].C,wr.S-mr[ai].S,5,h,k,(int)ai,ir); tighten(local,ws.C-ms[ai].C,ws.S-ms[ai].S,6,h,k,(int)ai,is);}
    cr[k]=wr;cs[k]=ws;
   }
#pragma omp critical
   { mergeB(global,local); }
  }
  pr.swap(cr);ps.swap(cs);
 }
 return{move(pr),move(ps),global};
}
static void runDir(int dir){
 const long long R=309151,x0=4590331,nB=24*R,P=617,Q=253330; const int M=2600,H=612;
 long long U0=11*x0+9*nB,V0=9*x0+11*nB; long long rL=(R-U0%R)%R,rH=V0%R; long long kL=(480LL*R-U0)/R,kH=(480LL*R+V0)/R;
 long long srL=-11LL*dir, srH=9LL*dir;
 SymOrbit L=solveSym(P,Q,rL,srL,R,M,H);
 SymOrbit Hh=solveSym(P,Q,rH,srH,R,M,H);
 Bound bd; mergeB(bd,L.bd);mergeB(bd,Hh.bd);
 if(srL<0) tighten(bd,rL,srL,10,0,0,0,0); else if(srL>0) tighten(bd,R-rL,-srL,11,0,0,0,0);
 if(srH<0) tighten(bd,rH,srH,12,0,0,0,0); else if(srH>0) tighten(bd,R-rH,-srH,13,0,0,0,0);
 long long urem=((U0%R)+R)%R, vrem=((V0%R)+R)%R; long long su=11LL*dir,sv=9LL*dir;
 if(su>0) tighten(bd,R-1-urem,-su,14,0,0,0,0); else tighten(bd,urem,su,15,0,0,0,0);
 if(sv>0) tighten(bd,R-1-vrem,-sv,16,0,0,0,0); else tighten(bd,vrem,sv,17,0,0,0,0);
 i128 T=((i128)12480*Q+(i128)28800*P)*R;
 Aff HM{(i128)360*x0*Q-(i128)400*P*nB+Hh.r[kH].C-T,(i128)360*dir*Q+Hh.r[kH].S};
 Aff LM{-(i128)440*x0*Q-(i128)400*P*nB+L.r[kL].C-T,-(i128)440*dir*Q+L.r[kL].S};
 cout<<"dir="<<dir<<" Hmargin(t)="<<s128(HM.C)<<" + ("<<s128(HM.S)<<")t Lmargin(t)="<<s128(LM.C)<<" + ("<<s128(LM.S)<<")t\n";
 if(bd.inf) cout<<"basis_bound=INF\n"; else cout<<"basis_bound="<<s128(bd.num)<<"/"<<s128(bd.den)<<" = "<<(long double)stold(s128(bd.num))/(long double)stold(s128(bd.den))<<" witness typ="<<bd.typ<<" h="<<bd.h<<" k="<<bd.k<<" a="<<bd.a<<" win="<<bd.w<<"\n";
}
int main(){runDir(-1);runDir(+1);}
