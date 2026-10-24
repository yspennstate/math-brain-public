#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
using boost::multiprecision::cpp_rational;
struct RPoint{cpp_rational x,v;};
struct Seg{cpp_rational l,u,C,S; int idx,typ;};
struct Line{cpp_rational A,B,C;};
static string rs(const cpp_rational& x){ std::ostringstream o; o<<x; return o.str(); }
static long double ld(const cpp_rational& x){ return x.convert_to<long double>(); }
static cpp_rational mn(const cpp_rational&a,const cpp_rational&b){return a<b?a:b;}
static cpp_rational mx(const cpp_rational&a,const cpp_rational&b){return a>b?a:b;}

struct Result{cpp_rational best,bx,by,bH,bL; long long cells=0,cands=0; int bix=-1,biy=-1;};

static bool feasible(const cpp_rational& x,const cpp_rational& y,const Seg&sx,const Seg&sy,bool aleb){
 if(x<sx.l||x>sx.u||y<sy.l||y>sy.u)return false;
 if(11*x+9*y<8640||11*x+9*y>9600)return false;
 if(9*x+11*y<9600||9*x+11*y>10560)return false;
 if(aleb){ if(x+y<960)return false; }
 else { if(x+y>960)return false; }
 return true;
}

static Result solveCells(const vector<Seg>&xs,const vector<Seg>&ys,long long P,long long Q,bool aleb){
 cpp_rational AH0,AHx,AHy,AL0,ALx,ALy,T=cpp_rational(12480LL*Q+28800LL*P);
 if(aleb){
   AH0=cpp_rational(86400LL*Q+96000LL*P); AHx=cpp_rational(-(99LL*Q+90LL*P)); AHy=cpp_rational(-(81LL*Q+110LL*P));
   AL0=cpp_rational(-105600LL*Q+96000LL*P); ALx=cpp_rational(121LL*Q-90LL*P); ALy=cpp_rational(99LL*Q-110LL*P);
 } else {
   AH0=cpp_rational(86400LL*Q-96000LL*P); AHx=cpp_rational(-(99LL*Q-110LL*P)); AHy=cpp_rational(-(81LL*Q-90LL*P));
   AL0=cpp_rational(-105600LL*Q-96000LL*P); ALx=cpp_rational(121LL*Q+110LL*P); ALy=cpp_rational(99LL*Q+90LL*P);
 }
 Result R; bool have=false;
 for(int i=0;i<(int)xs.size();++i){ const auto&sx=xs[i];
  for(int j=0;j<(int)ys.size();++j){ const auto&sy=ys[j];
   if(11*sx.u+9*sy.u<8640||11*sx.l+9*sy.l>9600)continue;
   if(9*sx.u+11*sy.u<9600||9*sx.l+11*sy.l>10560)continue;
   if(aleb){ if(sx.u+sy.u<960)continue; } else { if(sx.l+sy.l>960)continue; }
   R.cells++;
   vector<Line> ls={{1,0,sx.l},{1,0,sx.u},{0,1,sy.l},{0,1,sy.u},{11,9,8640},{11,9,9600},{9,11,9600},{9,11,10560},{1,1,960}};
   cpp_rational hC=AH0+sy.C,hx=AHx,hy=AHy+sy.S;
   cpp_rational lC=AL0+sx.C,lx=ALx+sx.S,ly=ALy;
   auto test=[&](const cpp_rational&x,const cpp_rational&y){
     if(!feasible(x,y,sx,sy,aleb))return; R.cands++;
     cpp_rational H=hC+hx*x+hy*y,L=lC+lx*x+ly*y,V=mn(H,L);
     if(!have||V>R.best){have=true;R.best=V;R.bx=x;R.by=y;R.bH=H;R.bL=L;R.bix=i;R.biy=j;}
   };
   for(int a=0;a<(int)ls.size();++a)for(int b=a+1;b<(int)ls.size();++b){
     cpp_rational det=ls[a].A*ls[b].B-ls[b].A*ls[a].B; if(det==0)continue;
     cpp_rational x=(ls[a].C*ls[b].B-ls[b].C*ls[a].B)/det;
     cpp_rational y=(ls[a].A*ls[b].C-ls[b].A*ls[a].C)/det; test(x,y);
   }
   Line eq{hx-lx,hy-ly,lC-hC};
   for(const auto&q:ls){cpp_rational det=eq.A*q.B-q.A*eq.B;if(det==0)continue;cpp_rational x=(eq.C*q.B-q.C*eq.B)/det;cpp_rational y=(eq.A*q.C-q.A*eq.C)/det;test(x,y);}
  }
 }
 if(!have){cerr<<"no feasible cells\n"; exit(2);} return R;
}

int main(){
 const long long P=617,Q=253330,D=40LL*Q; const int M=3200,MAXH=612;
 struct A{int x,y,dh,c,m; long long H,L,R;}; vector<pair<int,int>>ps;
 for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j});
 const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&p:ex)ps.push_back({4*p[0],4*p[1]});
 const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};for(auto&p:cut)ps.push_back({p[0],p[1]});
 vector<A>as;for(auto[x,y]:ps){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,9LL*x*Q-10LL*P*m,-11LL*x*Q-10LL*P*m,9LL*y*Q-10LL*P*m});}
 vector<long long>pr(M+1),cr(M+1);int stable=-1;
 for(int h=1;h<=MAXH;++h){
  for(int k=0;k<=M;++k){long long best=0;for(auto&a:as){long long hi=a.H+((k+a.dh<=M)?pr[k+a.dh]:0);long long lo;if(k>=a.c)lo=a.L+pr[k-a.c];else{int kk=a.c-k;lo=a.R-40LL*k*Q+((kk<=M)?pr[kk]:0);}best=max(best,min(hi,lo));}cr[k]=best;}
  if(cr==pr){stable=h;break;}pr.swap(cr);
 }
 if(stable!=388){cerr<<"unexpected integer stabilization "<<stable<<"\n";return 3;}
 for(int k=0;k<2600;k++){long long drop=pr[k]-pr[k+1];if(drop<0||drop>D){cerr<<"Lipschitz integer failure\n";return 4;}}
 vector<RPoint> sm; for(int k=0;k<=961;k++)sm.push_back({cpp_rational(k),cpp_rational(pr[k])});
 auto add=[&](long long xn,long long xd,long long vn,long long vd){sm.push_back({cpp_rational(xn)/xd,cpp_rational(vn)/vd});};
 add(54287,539,2608859499400LL,539);
 add(5101287,50666,245235295844000LL,50666);
 add(728549,7238,35035158281200LL,7238);
 add(2550110,25333,122621143876000LL,25333);
 add(5100597,50666,245238467535600LL,50666);
 add(2550487,25333,122617647922000LL,25333);
 add(5100661,50666,245237819010800LL,50666);
 sort(sm.begin(),sm.end(),[](auto&a,auto&b){return a.x<b.x;}); vector<RPoint> u;for(auto z:sm){if(!u.empty()&&z.x==u.back().x){if(z.v<u.back().v)u.back().v=z.v;}else u.push_back(z);}sm.swap(u);
 for(size_t i=0;i+1<sm.size();++i){cpp_rational drop=sm[i].v-sm[i+1].v, len=sm[i+1].x-sm[i].x;if(drop<0||drop>cpp_rational(D)*len){cerr<<"sample shape violation at "<<i<<"\n";return 5;}}
 auto makeSegs=[&](int lo,int hi){vector<Seg>s;int idx=0;for(size_t i=0;i+1<sm.size();++i){auto A=sm[i],B=sm[i+1];if(B.x<=lo||A.x>=hi)continue;cpp_rational l=mx(cpp_rational(lo),A.x),u0=mn(cpp_rational(hi),B.x);if(l>=u0)continue;cpp_rational drop=A.v-B.v,bp=B.x-drop/cpp_rational(D);if(bp>A.x){cpp_rational sl=mx(l,A.x),su=mn(u0,bp);if(sl<su)s.push_back({sl,su,A.v,0,idx,0});}if(bp<B.x){cpp_rational sl=mx(l,bp),su=mn(u0,B.x);if(sl<su)s.push_back({sl,su,B.v+cpp_rational(D)*B.x,cpp_rational(-D),idx,1});}idx++;}return s;};
 vector<Seg> xs=makeSegs(0,481),ys=makeSegs(479,961);
 auto R1=solveCells(xs,ys,P,Q,true); auto R2=solveCells(xs,ys,P,Q,false); cpp_rational T=cpp_rational(12480LL*Q+28800LL*P);
 cout<<"I0130_B4_B20_B26_CRITICAL_REGION_ENVELOPE_PASS\n";
 cout<<"integer_stable_h="<<stable<<" x_segments="<<xs.size()<<" y_segments="<<ys.size()<<"\n";
 cout<<"a_le_b cells="<<R1.cells<<" candidates="<<R1.cands<<" max_gap="<<rs(R1.best-T)<<" x="<<rs(R1.bx)<<" y="<<rs(R1.by)<<" Hgap="<<rs(R1.bH-T)<<" Lgap="<<rs(R1.bL-T)<<"\n";
 cout<<"a_gt_b cells="<<R2.cells<<" candidates="<<R2.cands<<" max_gap="<<rs(R2.best-T)<<" x="<<rs(R2.bx)<<" y="<<rs(R2.by)<<" Hgap="<<rs(R2.bH-T)<<" Lgap="<<rs(R2.bL-T)<<"\n";
 if(R1.best>T){cerr<<"a<=b envelope exceeds T\n";return 6;} if(R2.best>T){cerr<<"a>b envelope exceeds T\n";return 7;}
 auto pa=[&](cpp_rational x,cpp_rational y){return cpp_rational(10)-cpp_rational(11,960)*x-cpp_rational(9,960)*y;};
 auto pb=[&](cpp_rational x,cpp_rational y){return cpp_rational(9,960)*x+cpp_rational(11,960)*y-cpp_rational(10);};
 cout<<"a_le_b_arg_action=("<<rs(pa(R1.bx,R1.by))<<","<<rs(pb(R1.bx,R1.by))<<")\n";
 cout<<"a_gt_b_arg_action=("<<rs(pa(R2.bx,R2.by))<<","<<rs(pb(R2.bx,R2.by))<<")\n";
 return 0;
}
