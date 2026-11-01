#include <bits/stdc++.h>
using namespace std;
using A5=array<int,5>; using A4=array<int,4>;
struct St{uint16_t m;A5 v;int n;vector<double> f;};
const int M[17]={0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256};
vector<A5>S(16),W10,W20; vector<St> st; unordered_map<int,vector<int>> by; set<int> obs[11],need[11];
__int128 g128(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;}
long long lc(long long a,long long b){return a/std::gcd(a,b)*b;}
pair<long long,long long> term(const A5&v,int k,const A5&w,int D){long long L=1,N=0;for(int x:w)L=lc(L,x);for(int j=0;j<5;j++)N+=1LL*v[j]*v[j]*(L/w[j]);if(!N)return{LLONG_MAX/4,1};long long a=1LL*k*k*L,b=1LL*D*N,g=std::gcd(a,b);return{a/g,b/g};}
bool exact(const vector<int>&ix,const A4&k,const vector<A5>&W,int wi,int D){__int128 a=0,b=1;for(int r=0;r<4;r++){auto [p,q]=term(st[ix[r]].v,k[r],W[wi],D);if(p>=LLONG_MAX/8)return true;a=a*q+(__int128)p*b;b*=q;auto g=g128(a,b);a/=g;b/=g;}return a*24>=(__int128)7*b;}
double tf(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return (double)k*k/z;}
void add(int k,uint16_t m,const A5&v,int n){St x{m,v,n,{}};x.f.resize(W10.size());for(int i=0;i<(int)W10.size();i++)x.f[i]=tf(v,k,W10[i],10);int id=st.size();st.push_back(move(x));by[k*65536+(int)m].push_back(id);}
void gen(int k){vector<int>c(k);function<void(int,int)>R=[&](int p,int z){if(p==k){uint16_t m=0;for(int x:c)m|=(uint16_t)(1u<<x);for(int sb=0;sb<(1<<(k-1));sb++){A5 v=S[c[0]];for(int t=1;t<k;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}int n=0;for(int x:v)n+=x*x;obs[k].insert(n);if(need[k].count(n))add(k,m,v,n);}return;}for(int x=z;x<=16-(k-p);x++){c[p]=x;R(p+1,x+1);}};R(0,0);}
vector<uint16_t> masks(int k){vector<uint16_t>v;for(unsigned m=1;m<65536;m++)if(__builtin_popcount(m)==k)v.push_back((uint16_t)m);return v;}
int main(){
 for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}
 for(int a=1;a<=6;a++)for(int b=1;b<=10-a-2;b++)for(int c=1;c<=10-a-b-1;c++)for(int d=1;d<=10-a-b-c;d++){int e=10-a-b-c-d;if(e>=1)W10.push_back({a,b,c,d,e});}
 for(int a=1;a<=16;a++)for(int b=1;b<=20-a-2;b++)for(int c=1;c<=20-a-b-1;c++)for(int d=1;d<=20-a-b-c;d++){int e=20-a-b-c-d;if(e>=1)W20.push_back({a,b,c,d,e});}
 assert(W10.size()==126&&W20.size()==3876);
 vector<set<int>>E(11);E[1]={5};E[2]={4,8,12,16};E[3]={5,13,21,29};E[4]={0,4,8,12,16,20,24,28,32,36,40,44,48};E[5]={5,13,21,29,37,45,53,61};E[6]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80};E[7]={5,13,21,29,37,45,53,61,69,77,85,93,101};E[8]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,128};E[9]={5,13,21,29,37,45,53,61,69,77,85,93,101,109,117,125,133};E[10]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,144};
 vector<A4>P;for(int a=1;a<=16;a++)for(int b=a;b<=16;b++)for(int c=b;c<=16;c++){int d=16-a-b-c;if(d<c||d<1)continue;int K[4]={a,b,c,d};__int128 x=0,y=1;for(int r=0;r<4;r++){x=x*M[K[r]]+(__int128)K[r]*K[r]*y;y*=M[K[r]];auto g=g128(x,y);x/=g;y/=g;}if(x*24<(__int128)35*y)P.push_back({a,b,c,d});}assert(P.size()==30);for(auto p:P)assert(p[3]<=10);
 for(auto p:P)for(int r=0;r<4;r++){int k=p[r];__int128 x=0,y=1;for(int i=0;i<4;i++)if(i!=r){x=x*M[p[i]]+(__int128)p[i]*p[i]*y;y*=M[p[i]];auto g=g128(x,y);x/=g;y/=g;}for(int n:E[k])if(n>0)if((x*n+(__int128)k*k*y)*24<(__int128)35*y*n)need[k].insert(n);}
 for(int k=1;k<=10;k++){gen(k);assert(obs[k]==E[k]);assert(*obs[k].rbegin()==M[k]);}
 assert(7*3<24); assert((__int128)35*60<(__int128)89*24);
 long long N=0,fail10=0,use20=0,full20=0;
 for(auto K:P){vector<set<int>>A(4);for(int r=0;r<4;r++){__int128 x=0,y=1;for(int i=0;i<4;i++)if(i!=r){x=x*M[K[i]]+(__int128)K[i]*K[i]*y;y*=M[K[i]];auto g=g128(x,y);x/=g;y/=g;}for(int n:E[K[r]])if(n>0)if((x*n+(__int128)K[r]*K[r]*y)*24<(__int128)35*y*n)A[r].insert(n);}auto m0=masks(K[0]),m1=masks(K[1]),m2=masks(K[2]);
  for(uint16_t a:m0){auto p0=by.find(K[0]*65536+a);if(p0==by.end())continue;for(uint16_t b:m1){if(a&b||K[1]==K[0]&&b<=a)continue;auto p1=by.find(K[1]*65536+b);if(p1==by.end())continue;for(uint16_t c:m2){if((a|b)&c||K[2]==K[1]&&c<=b)continue;uint16_t d=0xFFFFu^(a|b|c);if(__builtin_popcount((unsigned)d)!=K[3]||K[3]==K[2]&&d<=c)continue;auto p2=by.find(K[2]*65536+c),p3=by.find(K[3]*65536+d);if(p2==by.end()||p3==by.end())continue;
   for(int i0:p0->second)if(A[0].count(st[i0].n))for(int i1:p1->second)if(A[1].count(st[i1].n))for(int i2:p2->second)if(A[2].count(st[i2].n))for(int i3:p3->second)if(A[3].count(st[i3].n)){N++;vector<int>ix={i0,i1,i2,i3};double best=-1;int wi=-1;for(int z=0;z<(int)W10.size();z++){double q=st[i0].f[z]+st[i1].f[z]+st[i2].f[z]+st[i3].f[z];if(q>best){best=q;wi=z;}}bool ok=exact(ix,K,W10,wi,10);if(!ok){fail10++;for(int z=0;z<(int)W10.size()&&!ok;z++)ok=exact(ix,K,W10,z,10);}if(!ok){use20++;best=-1;wi=-1;for(int z=0;z<(int)W20.size();z++){double q=tf(st[i0].v,K[0],W20[z],20)+tf(st[i1].v,K[1],W20[z],20)+tf(st[i2].v,K[2],W20[z],20)+tf(st[i3].v,K[3],W20[z],20);if(q>best){best=q;wi=z;}}ok=exact(ix,K,W20,wi,20);if(!ok){full20++;for(int z=0;z<(int)W20.size()&&!ok;z++)ok=exact(ix,K,W20,z,20);}}if(!ok)return 2;}
  }}}
 }
 assert(N==4765830&&fail10==1920&&use20==1920&&full20==0);
 cout<<"R13 K5 <= sqrt(24/7) exact checker\n"<<"target_c=7/24\n"<<"target_T_squared=24/7\n"<<"four_row_profiles="<<P.size()<<"\n"<<"oriented_four_row_configurations="<<N<<"\n"<<"weights_D10="<<W10.size()<<"\n"<<"weights_D20="<<W20.size()<<"\n"<<"configs_requiring_D20="<<use20<<"\n"<<"q_ge_5_exact_lower=89/60\n"<<"q_ge_5_target_total_cap=35/24\n"<<"R13_K5_SQRT24OVER7_EXACT_PASS\n";
}
