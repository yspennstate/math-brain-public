#!/usr/bin/env bash
set -euo pipefail
MODE="${1:-profile}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cat >"$TMP/profile_scan.py" <<'PYSCAN'
from fractions import Fraction
M=[0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256]
target=Fraction(89,60)
sur=[]
for a in range(1,17):
 for b in range(a,17):
  for c in range(b,17):
   d=16-a-b-c
   if d<c or d<1: continue
   s=sum(Fraction(k*k,M[k]) for k in (a,b,c,d))
   if s<target: sur.append(((a,b,c,d),s))
large=[p for p,s in sur if p[-1]>10]
assert len(sur)==33
assert large==[(1,1,2,12),(1,1,3,11),(1,2,2,11)]
large_all=[]
for a in range(1,17):
 for b in range(a,17):
  for c in range(b,17):
   d=16-a-b-c
   if d<c or d<=10: continue
   s=sum(Fraction(k*k,M[k]) for k in (a,b,c,d))
   large_all.append((s/Fraction(5), (a,b,c,d)))
large_all.sort()
assert large_all[:4]==[(Fraction(323,1100),(1,1,2,12)),(Fraction(2309,7850),(1,2,2,11)),(Fraction(33716,113825),(1,1,3,11)),(Fraction(1412,4725),(1,1,1,13))]
best=None; bp=None
def rec(rem,mn,q,p):
 global best,bp
 if q==0:
  if rem: return
  s=sum(Fraction(k*k,M[k]) for k in p)
  if best is None or s<best: best,bp=s,tuple(p)
  return
 for k in range(mn,rem+1):
  if rem-k<k*(q-1): break
  rec(rem-k,k,q-1,p+[k])
for q in range(5,17): rec(16,1,q,[])
assert best==Fraction(89,60) and bp==(1,1,2,4,8)
checks=[((1,1,2,12),172,Fraction(1279,860)),((1,2,2,11),149,Fraction(2253,1490)),((1,1,3,11),149,Fraction(32892,21605))]
for p,repl,want in checks:
 vals=[]
 for i,k in enumerate(p): vals.append(Fraction(k*k,repl if i==3 else M[k]))
 assert sum(vals)==want and want>target
print('PROFILE_SCAN_EXACT_PASS')
print('q4_survivors=33 small=30 large=' + str(large))
print('q_ge_5_exact_min=89/60 profile=(1,1,2,4,8) target_c=89/300')
print('next_large_q4_threshold=1412/4725 profile=(1,1,1,13)')
PYSCAN
cat >"$TMP/small.cpp" <<'CPP'
#include <bits/stdc++.h>
using namespace std; using A5=array<int,5>; using A4=array<int,4>;
struct St{uint16_t m;A5 v;int n;vector<double> f;};
const int M[17]={0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256};
#ifndef TP
#define TP 7
#endif
#ifndef TQ
#define TQ 24
#endif
vector<A5>S(16),W10,W20,W30; vector<St> st; unordered_map<int,vector<int>> by; set<int> obs[17],need[17];
__int128 g128(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;}
long long lc(long long a,long long b){return a/std::gcd(a,b)*b;}
pair<long long,long long> term(const A5&v,int k,const A5&w,int D){long long L=1,N=0;for(int x:w)L=lc(L,x);for(int j=0;j<5;j++)N+=1LL*v[j]*v[j]*(L/w[j]);if(!N)return{LLONG_MAX/4,1};long long a=1LL*k*k*L,b=1LL*D*N,g=std::gcd(a,b);return{a/g,b/g};}
bool exact(const vector<int>&ix,const A4&k,const vector<A5>&W,int wi,int D){__int128 a=0,b=1;for(int r=0;r<4;r++){auto [p,q]=term(st[ix[r]].v,k[r],W[wi],D);if(p>=LLONG_MAX/8)return true;a=a*q+(__int128)p*b;b*=q;auto g=g128(a,b);a/=g;b/=g;}return a*TQ>=(__int128)TP*b;}
double tf(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return (double)k*k/z;}
void add(int k,uint16_t m,const A5&v,int n){St x{m,v,n,{}};x.f.resize(W10.size());for(int i=0;i<(int)W10.size();i++)x.f[i]=tf(v,k,W10[i],10);int id=st.size();st.push_back(move(x));by[k*65536+(int)m].push_back(id);}
void gen(int k){vector<int>c(k);function<void(int,int)>R=[&](int p,int z){if(p==k){uint16_t m=0;for(int x:c)m|=(uint16_t)(1u<<x);for(int sb=0;sb<(1<<(k-1));sb++){A5 v=S[c[0]];for(int t=1;t<k;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}int n=0;for(int x:v)n+=x*x;obs[k].insert(n);if(need[k].count(n))add(k,m,v,n);}return;}for(int x=z;x<=16-(k-p);x++){c[p]=x;R(p+1,x+1);}};R(0,0);}
vector<uint16_t> masks(int k){vector<uint16_t>v;for(unsigned m=1;m<65536;m++)if(__builtin_popcount(m)==k)v.push_back((uint16_t)m);return v;}
void genW(vector<A5>&W,int D){for(int a=1;a<=D-4;a++)for(int b=1;b<=D-a-3;b++)for(int c=1;c<=D-a-b-2;c++)for(int d=1;d<=D-a-b-c-1;d++){int e=D-a-b-c-d;if(e>=1)W.push_back({a,b,c,d,e});}}
int main(){
 for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}
 genW(W10,10); genW(W20,20); genW(W30,30);
 vector<set<int>>E(17);E[1]={5};E[2]={4,8,12,16};E[3]={5,13,21,29};E[4]={0,4,8,12,16,20,24,28,32,36,40,44,48};E[5]={5,13,21,29,37,45,53,61};E[6]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80};E[7]={5,13,21,29,37,45,53,61,69,77,85,93,101};E[8]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,128};E[9]={5,13,21,29,37,45,53,61,69,77,85,93,101,109,117,125,133};E[10]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,144};
 vector<A4>P; bool large=false;for(int a=1;a<=16;a++)for(int b=a;b<=16;b++)for(int c=b;c<=16;c++){int d=16-a-b-c;if(d<c||d<1)continue;int K[4]={a,b,c,d};__int128 x=0,y=1;for(int r=0;r<4;r++){x=x*M[K[r]]+(__int128)K[r]*K[r]*y;y*=M[K[r]];auto g=g128(x,y);x/=g;y/=g;}if(x*TQ<(__int128)(5*TP)*y){if(d<=10) P.push_back({a,b,c,d}); else large=true;}}
 cerr<<"target="<<TP<<"/"<<TQ<<" profiles="<<P.size()<<" large="<<large<<"\n";
 for(auto p:P)for(int r=0;r<4;r++){int k=p[r];__int128 x=0,y=1;for(int i=0;i<4;i++)if(i!=r){x=x*M[p[i]]+(__int128)p[i]*p[i]*y;y*=M[p[i]];auto g=g128(x,y);x/=g;y/=g;}for(int n:E[k])if(n>0)if((x*n+(__int128)k*k*y)*TQ<(__int128)(5*TP)*y*n)need[k].insert(n);}
 for(int k=1;k<=10;k++){gen(k);}
 if((__int128)89*TQ < (__int128)60*5*TP){cerr<<"q>=5 barrier failed\n";return 4;}
 long long N=0,fail10=0,use20=0,use30=0,full30=0;
 for(auto K:P){vector<set<int>>A(4);for(int r=0;r<4;r++){__int128 x=0,y=1;for(int i=0;i<4;i++)if(i!=r){x=x*M[K[i]]+(__int128)K[i]*K[i]*y;y*=M[K[i]];auto g=g128(x,y);x/=g;y/=g;}for(int n:E[K[r]])if(n>0)if((x*n+(__int128)K[r]*K[r]*y)*TQ<(__int128)(5*TP)*y*n)A[r].insert(n);}auto m0=masks(K[0]),m1=masks(K[1]),m2=masks(K[2]);
  for(uint16_t a:m0){auto p0=by.find(K[0]*65536+a);if(p0==by.end())continue;for(uint16_t b:m1){if(a&b||K[1]==K[0]&&b<=a)continue;auto p1=by.find(K[1]*65536+b);if(p1==by.end())continue;for(uint16_t c:m2){if((a|b)&c||K[2]==K[1]&&c<=b)continue;uint16_t d=0xFFFFu^(a|b|c);if(__builtin_popcount((unsigned)d)!=K[3]||K[3]==K[2]&&d<=c)continue;auto p2=by.find(K[2]*65536+c),p3=by.find(K[3]*65536+d);if(p2==by.end()||p3==by.end())continue;
   for(int i0:p0->second)if(A[0].count(st[i0].n))for(int i1:p1->second)if(A[1].count(st[i1].n))for(int i2:p2->second)if(A[2].count(st[i2].n))for(int i3:p3->second)if(A[3].count(st[i3].n)){N++;vector<int>ix={i0,i1,i2,i3};double best=-1;int wi=-1;for(int z=0;z<(int)W10.size();z++){double q=st[i0].f[z]+st[i1].f[z]+st[i2].f[z]+st[i3].f[z];if(q>best){best=q;wi=z;}}bool ok=exact(ix,K,W10,wi,10);if(!ok){fail10++;for(int z=0;z<(int)W10.size()&&!ok;z++)ok=exact(ix,K,W10,z,10);}if(!ok){use20++;best=-1;wi=-1;for(int z=0;z<(int)W20.size();z++){double q=tf(st[i0].v,K[0],W20[z],20)+tf(st[i1].v,K[1],W20[z],20)+tf(st[i2].v,K[2],W20[z],20)+tf(st[i3].v,K[3],W20[z],20);if(q>best){best=q;wi=z;}}ok=exact(ix,K,W20,wi,20);if(!ok)for(int z=0;z<(int)W20.size()&&!ok;z++)ok=exact(ix,K,W20,z,20);}if(!ok){use30++;best=-1;wi=-1;for(int z=0;z<(int)W30.size();z++){double q=tf(st[i0].v,K[0],W30[z],30)+tf(st[i1].v,K[1],W30[z],30)+tf(st[i2].v,K[2],W30[z],30)+tf(st[i3].v,K[3],W30[z],30);if(q>best){best=q;wi=z;}}ok=exact(ix,K,W30,wi,30);if(!ok){full30++; for(int z=0;z<(int)W30.size()&&!ok;z++)ok=exact(ix,K,W30,z,30);}}if(!ok){cerr<<"FAIL config N="<<N<<" K="<<K[0]<<","<<K[1]<<","<<K[2]<<","<<K[3]<<"\n";return 2;}}
  }}}
 }
 cout<<"PASS target_c="<<TP<<"/"<<TQ<<" profiles="<<P.size()<<" configs="<<N<<" fail10="<<fail10<<" use20="<<use20<<" use30="<<use30<<" full30="<<full30<<" W30="<<W30.size()<<"\n";
}
CPP
cat >"$TMP/large11212.cpp" <<'CPP'
#include <bits/stdc++.h>
using namespace std; using A5=array<int,5>;
#ifndef TP
#define TP 2309
#endif
#ifndef TQ
#define TQ 7850
#endif
vector<A5>S,W10,W20,W30;
__int128 gcd128(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;}
long long lcmll(long long a,long long b){return a/std::gcd(a,b)*b;}
pair<long long,long long> term(const A5&v,int k,const A5&w,int D){long long L=1,N=0;for(int x:w)L=lcmll(L,x);for(int j=0;j<5;j++)N+=1LL*v[j]*v[j]*(L/w[j]);long long a=1LL*k*k*L,b=1LL*D*N,g=std::gcd(a,b);return{a/g,b/g};}
bool exact(const array<A5,4>&V,const vector<A5>&W,int wi,int D){int K[4]={1,1,2,12};__int128 a=0,b=1;for(int r=0;r<4;r++){auto [p,q]=term(V[r],K[r],W[wi],D);a=a*q+(__int128)p*b;b*=q;auto g=gcd128(a,b);a/=g;b/=g;}return a*TQ >= (__int128)TP*b;}
double tf(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return (double)k*k/z;}
void genW(vector<A5>&W,int D){for(int a=1;a<=D-4;a++)for(int b=1;b<=D-a-3;b++)for(int c=1;c<=D-a-b-2;c++)for(int d=1;d<=D-a-b-c-1;d++){int e=D-a-b-c-d;W.push_back({a,b,c,d,e});}}
int nrm(const A5&v){int n=0;for(int x:v)n+=x*x;return n;}
int main(){S.resize(16);for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}genW(W10,10);genW(W20,20);genW(W30,30);
 unordered_map<unsigned,vector<A5>> V12; long long total12=0;
 for(unsigned mask=0;mask<65536;mask++) if(__builtin_popcount(mask)==12){vector<int> c; for(int i=0;i<16;i++)if(mask>>i&1)c.push_back(i); auto &vv=V12[mask]; for(int sb=0;sb<(1<<11);sb++){A5 v=S[c[0]];for(int t=1;t<12;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];} if(nrm(v)==176)vv.push_back(v);} total12+=vv.size();}
 cerr<<"total max V12="<<total12<<" avg="<<(double)total12/1820<<"\n";
 long long N=0, fail10=0,use20=0,use30=0;
 for(int a=0;a<16;a++)for(int b=a+1;b<16;b++){
   unsigned used=(1u<<a)|(1u<<b);
   vector<int> rem;for(int x=0;x<16;x++)if(!(used>>x&1))rem.push_back(x);
   for(int ii=0;ii<(int)rem.size();ii++)for(int jj=ii+1;jj<(int)rem.size();jj++){
     int c=rem[ii],d=rem[jj]; unsigned pm=(1u<<c)|(1u<<d); unsigned m12=0xFFFFu ^ (used|pm);
     auto &L=V12[m12]; if(L.empty())continue;
     for(int sg: {-1,1}){A5 vp=S[c];for(int j=0;j<5;j++)vp[j]+=sg*S[d][j];if(nrm(vp)!=16)continue;
       for(auto &v12:L){array<A5,4> V={S[a],S[b],vp,v12};N++;
         double best=-1;int wi=-1;for(int z=0;z<(int)W10.size();z++){double q=tf(V[0],1,W10[z],10)+tf(V[1],1,W10[z],10)+tf(V[2],2,W10[z],10)+tf(V[3],12,W10[z],10);if(q>best){best=q;wi=z;}}
         bool ok=exact(V,W10,wi,10);if(!ok){fail10++;for(int z=0;z<(int)W10.size()&&!ok;z++)ok=exact(V,W10,z,10);} 
         if(!ok){use20++;best=-1;wi=-1;for(int z=0;z<(int)W20.size();z++){double q=tf(V[0],1,W20[z],20)+tf(V[1],1,W20[z],20)+tf(V[2],2,W20[z],20)+tf(V[3],12,W20[z],20);if(q>best){best=q;wi=z;}}ok=exact(V,W20,wi,20);if(!ok)for(int z=0;z<(int)W20.size()&&!ok;z++)ok=exact(V,W20,z,20);}
         if(!ok){use30++;best=-1;wi=-1;for(int z=0;z<(int)W30.size();z++){double q=tf(V[0],1,W30[z],30)+tf(V[1],1,W30[z],30)+tf(V[2],2,W30[z],30)+tf(V[3],12,W30[z],30);if(q>best){best=q;wi=z;}}ok=exact(V,W30,wi,30);if(!ok)for(int z=0;z<(int)W30.size()&&!ok;z++)ok=exact(V,W30,z,30);}
         if(!ok){cerr<<"FAIL N="<<N<<" a,b,c,d="<<a<<","<<b<<","<<c<<","<<d<<"\n"; for(auto &v:V){for(int x:v)cerr<<x<<",";cerr<<" n="<<nrm(v)<<"\n";}return 2;}
       }
     }
   }
 }
 cout<<"PASS large 1,1,2,12 target="<<TP<<"/"<<TQ<<" configs="<<N<<" fail10="<<fail10<<" use20="<<use20<<" use30="<<use30<<"\n";
}
CPP
cat >"$TMP/large12211.cpp" <<'CPP'
#include <bits/stdc++.h>
using namespace std; using A5=array<int,5>;
#ifndef TP
#define TP 33716
#endif
#ifndef TQ
#define TQ 113825
#endif
vector<A5>S,W10,W20; __int128 G(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;} long long L(long long a,long long b){return a/std::gcd(a,b)*b;}
pair<long long,long long> term(const A5&v,int k,const A5&w,int D){long long l=1,n=0;for(int x:w)l=L(l,x);for(int j=0;j<5;j++)n+=1LL*v[j]*v[j]*(l/w[j]);long long a=1LL*k*k*l,b=1LL*D*n,g=std::gcd(a,b);return{a/g,b/g};}
bool ex(const array<A5,4>&V,const vector<A5>&W,int wi,int D){int K[4]={1,2,2,11};__int128 a=0,b=1;for(int r=0;r<4;r++){auto[p,q]=term(V[r],K[r],W[wi],D);a=a*q+(__int128)p*b;b*=q;auto g=G(a,b);a/=g;b/=g;}return a*TQ>=(__int128)TP*b;}
double tf(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return (double)k*k/z;}
void gw(vector<A5>&W,int D){for(int a=1;a<=D-4;a++)for(int b=1;b<=D-a-3;b++)for(int c=1;c<=D-a-b-2;c++)for(int d=1;d<=D-a-b-c-1;d++)W.push_back({a,b,c,d,D-a-b-c-d});}
int nr(const A5&v){int n=0;for(int x:v)n+=x*x;return n;}
int main(){S.resize(16);for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}gw(W10,10);gw(W20,20);
 unordered_map<unsigned,vector<A5>> V11; long long tv=0;for(unsigned mask=0;mask<65536;mask++)if(__builtin_popcount(mask)==11){vector<int>c;for(int i=0;i<16;i++)if(mask>>i&1)c.push_back(i);auto& vv=V11[mask];for(int sb=0;sb<(1<<10);sb++){A5 v=S[c[0]];for(int t=1;t<11;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}if(nr(v)==157)vv.push_back(v);}tv+=vv.size();}cerr<<"V11 max total="<<tv<<"\n";
 long long N=0,f10=0,u20=0;for(int a=0;a<16;a++){unsigned ua=1u<<a;vector<int>r;for(int x=0;x<16;x++)if(x!=a)r.push_back(x);for(int i=0;i<(int)r.size();i++)for(int j=i+1;j<(int)r.size();j++){int b=r[i],c=r[j];unsigned p1=(1u<<b)|(1u<<c);for(int i2=0;i2<(int)r.size();i2++)for(int j2=i2+1;j2<(int)r.size();j2++){int d=r[i2],e=r[j2];unsigned p2=(1u<<d)|(1u<<e);if(p1&p2||p2<=p1)continue;unsigned m11=0xFFFFu^(ua|p1|p2);if(__builtin_popcount(m11)!=11)continue;auto &LL=V11[m11];if(LL.empty())continue;for(int s1:{-1,1}){A5 v1=S[b];for(int z=0;z<5;z++)v1[z]+=s1*S[c][z];if(nr(v1)!=16)continue;for(int s2:{-1,1}){A5 v2=S[d];for(int z=0;z<5;z++)v2[z]+=s2*S[e][z];if(nr(v2)!=16)continue;for(auto&v11:LL){array<A5,4>V={S[a],v1,v2,v11};N++;double best=-1;int wi=0;for(int z=0;z<(int)W10.size();z++){double q=tf(V[0],1,W10[z],10)+tf(V[1],2,W10[z],10)+tf(V[2],2,W10[z],10)+tf(V[3],11,W10[z],10);if(q>best){best=q;wi=z;}}bool ok=ex(V,W10,wi,10);if(!ok){f10++;for(int z=0;z<(int)W10.size()&&!ok;z++)ok=ex(V,W10,z,10);}if(!ok){u20++;best=-1;wi=0;for(int z=0;z<(int)W20.size();z++){double q=tf(V[0],1,W20[z],20)+tf(V[1],2,W20[z],20)+tf(V[2],2,W20[z],20)+tf(V[3],11,W20[z],20);if(q>best){best=q;wi=z;}}ok=ex(V,W20,wi,20);if(!ok)for(int z=0;z<(int)W20.size()&&!ok;z++)ok=ex(V,W20,z,20);}if(!ok){cerr<<"FAIL N="<<N<<"\n";return 2;}}}}}}}
 cout<<"PASS 1,2,2,11 target="<<TP<<"/"<<TQ<<" configs="<<N<<" f10="<<f10<<" u20="<<u20<<"\n";
}
CPP
cat >"$TMP/large11311.cpp" <<'CPP'
#include <bits/stdc++.h>
using namespace std;using A5=array<int,5>;
#ifndef TP
#define TP 89
#endif
#ifndef TQ
#define TQ 300
#endif
vector<A5>S,W10,W20;__int128 G(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;}long long L(long long a,long long b){return a/std::gcd(a,b)*b;}
pair<long long,long long> term(const A5&v,int k,const A5&w,int D){long long l=1,n=0;for(int x:w)l=L(l,x);for(int j=0;j<5;j++)n+=1LL*v[j]*v[j]*(l/w[j]);long long a=1LL*k*k*l,b=1LL*D*n,g=std::gcd(a,b);return{a/g,b/g};}
bool ex(const array<A5,4>&V,const vector<A5>&W,int wi,int D){int K[4]={1,1,3,11};__int128 a=0,b=1;for(int r=0;r<4;r++){auto[p,q]=term(V[r],K[r],W[wi],D);a=a*q+(__int128)p*b;b*=q;auto g=G(a,b);a/=g;b/=g;}return a*TQ>=(__int128)TP*b;}
double tf(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return(double)k*k/z;}void gw(vector<A5>&W,int D){for(int a=1;a<=D-4;a++)for(int b=1;b<=D-a-3;b++)for(int c=1;c<=D-a-b-2;c++)for(int d=1;d<=D-a-b-c-1;d++)W.push_back({a,b,c,d,D-a-b-c-d});}int nr(const A5&v){int n=0;for(int x:v)n+=x*x;return n;}
int main(){S.resize(16);for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}gw(W10,10);gw(W20,20);unordered_map<unsigned,vector<A5>>V11;long long tv=0;for(unsigned mask=0;mask<65536;mask++)if(__builtin_popcount(mask)==11){vector<int>c;for(int i=0;i<16;i++)if(mask>>i&1)c.push_back(i);auto&vv=V11[mask];for(int sb=0;sb<(1<<10);sb++){A5 v=S[c[0]];for(int t=1;t<11;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}if(nr(v)==157)vv.push_back(v);}tv+=vv.size();}cerr<<"V11="<<tv<<"\n";
 long long N=0,f10=0,u20=0;for(int a=0;a<16;a++)for(int b=a+1;b<16;b++){unsigned u=(1u<<a)|(1u<<b);vector<int>r;for(int x=0;x<16;x++)if(!(u>>x&1))r.push_back(x);for(int i=0;i<(int)r.size();i++)for(int j=i+1;j<(int)r.size();j++)for(int k=j+1;k<(int)r.size();k++){int c=r[i],d=r[j],e=r[k];unsigned tm=(1u<<c)|(1u<<d)|(1u<<e);unsigned m11=0xFFFFu^(u|tm);auto&LL=V11[m11];if(LL.empty())continue;for(int sb=0;sb<4;sb++){A5 vt=S[c];int s1=(sb&1)?1:-1,s2=(sb&2)?1:-1;for(int z=0;z<5;z++)vt[z]+=s1*S[d][z]+s2*S[e][z];if(nr(vt)!=29)continue;for(auto&v11:LL){array<A5,4>V={S[a],S[b],vt,v11};N++;double best=-1;int wi=0;for(int z=0;z<(int)W10.size();z++){double q=tf(V[0],1,W10[z],10)+tf(V[1],1,W10[z],10)+tf(V[2],3,W10[z],10)+tf(V[3],11,W10[z],10);if(q>best){best=q;wi=z;}}bool ok=ex(V,W10,wi,10);if(!ok){f10++;for(int z=0;z<(int)W10.size()&&!ok;z++)ok=ex(V,W10,z,10);}if(!ok){u20++;best=-1;wi=0;for(int z=0;z<(int)W20.size();z++){double q=tf(V[0],1,W20[z],20)+tf(V[1],1,W20[z],20)+tf(V[2],3,W20[z],20)+tf(V[3],11,W20[z],20);if(q>best){best=q;wi=z;}}ok=ex(V,W20,wi,20);if(!ok)for(int z=0;z<(int)W20.size()&&!ok;z++)ok=ex(V,W20,z,20);}if(!ok){cerr<<"FAIL N="<<N<<"\n";return 2;}}}}}
 cout<<"PASS 1,1,3,11 target="<<TP<<"/"<<TQ<<" configs="<<N<<" f10="<<f10<<" u20="<<u20<<"\n";
}
CPP
run_cpp(){ g++ -O3 -std=c++17 -DTP=89 -DTQ=300 "$TMP/$1.cpp" -o "$TMP/$1.bin"; "$TMP/$1.bin"; }
case "$MODE" in
 profile) python "$TMP/profile_scan.py" ;;
 small) run_cpp small ;;
 large11212) run_cpp large11212 ;;
 large12211) run_cpp large12211 ;;
 large11311) run_cpp large11311 ;;
 all) "$0" profile; "$0" small; "$0" large11212; "$0" large12211; "$0" large11311; echo R13_K5_SQRT300OVER89_EXACT_PASS ;;
 *) echo "usage: $0 {profile|small|large11212|large12211|large11311|all}" >&2; exit 64 ;;
esac
