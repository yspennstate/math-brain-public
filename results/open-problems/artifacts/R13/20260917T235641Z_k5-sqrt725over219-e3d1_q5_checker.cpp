#include <bits/stdc++.h>
using namespace std; using A5=array<int,5>;
struct St{uint16_t mask; A5 v; int norm2; vector<double> score10;};
#ifndef CP
#define CP 219
#endif
#ifndef CQ
#define CQ 725
#endif
static const int M[17]={0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256};
vector<A5>S(16),W10,W20,W30; vector<St> states; unordered_map<int,vector<int>> by_key; set<int> needed[14]; vector<vector<uint16_t>> mask_cache(17);
__int128 gcd128(__int128 a,__int128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){auto r=a%b;a=b;b=r;}return a;}
long long lcmll(long long a,long long b){return a/std::gcd(a,b)*b;}
void genW(vector<A5>&W,int D){for(int a=1;a<=D-4;a++)for(int b=1;b<=D-a-3;b++)for(int c=1;c<=D-a-b-2;c++)for(int d=1;d<=D-a-b-c-1;d++){int e=D-a-b-c-d;if(e>=1)W.push_back({a,b,c,d,e});}}
pair<long long,long long> cert_term(const A5&v,int k,const A5&w,int D){long long L=1,N=0;for(int x:w)L=lcmll(L,x);for(int j=0;j<5;j++)N+=1LL*v[j]*v[j]*(L/w[j]);if(!N)return{LLONG_MAX/4,1};long long a=1LL*k*k*L,b=1LL*D*N,g=std::gcd(a,b);return{a/g,b/g};}
double fterm(const A5&v,int k,const A5&w,int D){double z=0;for(int j=0;j<5;j++)z+=(double)D*v[j]*v[j]/w[j];return (double)k*k/z;}
void add_state(int k,uint16_t m,const A5&v,int n){St x{m,v,n,{}};x.score10.resize(W10.size());for(int i=0;i<(int)W10.size();i++)x.score10[i]=fterm(v,k,W10[i],10);int id=states.size();states.push_back(move(x));by_key[k*65536+(int)m].push_back(id);}
void gen_states(int k){vector<int>c(k);function<void(int,int)>rec=[&](int p,int z){if(p==k){uint16_t m=0;for(int x:c)m|=(uint16_t)(1u<<x);for(int sb=0;sb<(1<<(k-1));sb++){A5 v=S[c[0]];for(int t=1;t<k;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}int n=0;for(int x:v)n+=x*x;if(needed[k].count(n))add_state(k,m,v,n);}return;}for(int x=z;x<=16-(k-p);x++){c[p]=x;rec(p+1,x+1);}};rec(0,0);}
struct Prof{array<int,5> k;}; vector<Prof> profiles;
pair<__int128,__int128> sumFrac(const array<int,5>&K,int replace=-1,int rn=0){__int128 a=0,b=1;for(int i=0;i<5;i++){int den=(i==replace?rn:M[K[i]]);a=a*den+(__int128)K[i]*K[i]*b;b*=den;auto g=gcd128(a,b);a/=g;b/=g;}return{a,b};}
bool exact_cert(const array<int,5>&ids,const array<int,5>&K,const vector<A5>&W,int wi,int D){__int128 a=0,b=1;for(int r=0;r<5;r++){auto [p,q]=cert_term(states[ids[r]].v,K[r],W[wi],D);if(p>=LLONG_MAX/8)return true;a=a*q+(__int128)p*b;b*=q;auto g=gcd128(a,b);a/=g;b/=g;}return a*CQ>=(__int128)CP*b;}
int main(){
 for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}
 for(int k=1;k<=16;k++)for(unsigned m=1;m<65536;m++)if(__builtin_popcount(m)==k)mask_cache[k].push_back((uint16_t)m);
 genW(W10,10);genW(W20,20);genW(W30,30);
 vector<vector<int>>E(14);E[1]={5};E[2]={4,8,12,16};E[3]={5,13,21,29};for(int n=0;n<=48;n+=4)E[4].push_back(n);for(int n=5;n<=61;n+=8)E[5].push_back(n);for(int n=0;n<=80;n+=4)E[6].push_back(n);for(int n=5;n<=101;n+=8)E[7].push_back(n);for(int n=0;n<=112;n+=4)E[8].push_back(n);E[8].push_back(128);for(int n=5;n<=133;n+=8)E[9].push_back(n);for(int n=0;n<=144;n+=4)E[10].push_back(n);for(int n=5;n<=157;n+=8)E[11].push_back(n);for(int n=0;n<=176;n+=4)E[12].push_back(n);for(int n=5;n<=189;n+=8)E[13].push_back(n);
 for(int a=1;a<=16;a++)for(int b=a;b<=16;b++)for(int c=b;c<=16;c++)for(int d=c;d<=16;d++){int e=16-a-b-c-d;if(e<d||e<1)continue;array<int,5>K={a,b,c,d,e};auto [x,y]=sumFrac(K);if(x*CQ<(__int128)5*CP*y)profiles.push_back({K});}
 cerr<<"target="<<CP<<"/"<<CQ<<" profiles="<<profiles.size()<<"\n";for(auto P:profiles){for(int z:P.k)cerr<<z<<",";cerr<<" ";}cerr<<"\n";
 for(auto P:profiles){auto K=P.k;for(int r=0;r<5;r++){__int128 a=0,b=1;for(int i=0;i<5;i++)if(i!=r){a=a*M[K[i]]+(__int128)K[i]*K[i]*b;b*=M[K[i]];auto g=gcd128(a,b);a/=g;b/=g;}for(int n:E[K[r]])if(n>0){__int128 x=a*n+(__int128)K[r]*K[r]*b,y=b*n;if(x*CQ<(__int128)5*CP*y)needed[K[r]].insert(n);}}}
 int maxk=0;for(auto P:profiles)for(int k:P.k)maxk=max(maxk,k);for(int k=1;k<=maxk;k++){gen_states(k);cerr<<"k="<<k<<" need="<<needed[k].size()<<" totalstates="<<states.size()<<"\n";}
 long long N=0,uniq=0,u20=0,u30=0;unordered_map<string,unsigned char>cache;cache.reserve(3000000);
 for(auto P:profiles){auto K=P.k; long long N0=N; array<uint16_t,5> ms{}; array<int,5> ids{};
   function<bool(int,uint16_t,int)> dfs=[&](int r,uint16_t used,int prevMask)->bool{
     if(r==4){uint16_t m=(uint16_t)(0xFFFFu^used);if(__builtin_popcount((unsigned)m)!=K[4])return true;if(K[4]==K[3]&&m<=prevMask)return true;auto it=by_key.find(K[4]*65536+(int)m);if(it==by_key.end())return true;ms[4]=m;for(int id:it->second){ids[4]=id;N++;
       string key;key.reserve(30);for(int z:K)key.push_back((char)z);for(int rr=0;rr<5;rr++)for(int j=0;j<5;j++)key.push_back((char)(states[ids[rr]].v[j]*states[ids[rr]].v[j]));auto ic=cache.find(key);if(ic!=cache.end()){if(ic->second==0)return false;continue;}uniq++;
       double best=-1;int wi=-1;for(int z=0;z<(int)W10.size();z++){double q=0;for(int rr=0;rr<5;rr++)q+=fterm(states[ids[rr]].v,K[rr],W10[z],10);if(q>best){best=q;wi=z;}}bool ok=exact_cert(ids,K,W10,wi,10);if(!ok)for(int z=0;z<(int)W10.size()&&!ok;z++)ok=exact_cert(ids,K,W10,z,10);unsigned char lvl=10;
       if(!ok){u20++;best=-1;wi=-1;for(int z=0;z<(int)W20.size();z++){double q=0;for(int rr=0;rr<5;rr++)q+=fterm(states[ids[rr]].v,K[rr],W20[z],20);if(q>best){best=q;wi=z;}}ok=exact_cert(ids,K,W20,wi,20);if(!ok)for(int z=0;z<(int)W20.size()&&!ok;z++)ok=exact_cert(ids,K,W20,z,20);lvl=20;}
       if(!ok){u30++;best=-1;wi=-1;for(int z=0;z<(int)W30.size();z++){double q=0;for(int rr=0;rr<5;rr++)q+=fterm(states[ids[rr]].v,K[rr],W30[z],30);if(q>best){best=q;wi=z;}}ok=exact_cert(ids,K,W30,wi,30);if(!ok)for(int z=0;z<(int)W30.size()&&!ok;z++)ok=exact_cert(ids,K,W30,z,30);lvl=30;}
       if(!ok){cerr<<"FAIL profile ";for(int z:K)cerr<<z<<",";cerr<<" N="<<N<<" uniq="<<uniq<<" squares ";for(int rr=0;rr<5;rr++){cerr<<"[";for(int j=0;j<5;j++)cerr<<states[ids[rr]].v[j]*states[ids[rr]].v[j]<<",";cerr<<"]";}cerr<<"\n";cache.emplace(key,0);return false;}cache.emplace(key,lvl);
     }return true;}
     int k=K[r];for(uint16_t m:mask_cache[k]){if(used&m)continue;if(r>0&&K[r]==K[r-1]&&m<=prevMask)continue;auto it=by_key.find(k*65536+(int)m);if(it==by_key.end())continue;ms[r]=m;for(int id:it->second){ids[r]=id;if(!dfs(r+1,used|m,m))return false;}}return true;};
   if(!dfs(0,0,-1))return 2; cerr<<"done ";for(int z:K)cerr<<z<<",";cerr<<" configs="<<(N-N0)<<" total="<<N<<" uniq="<<uniq<<" u20="<<u20<<" u30="<<u30<<"\n";
 }
 cout<<"PASS q5 target="<<CP<<"/"<<CQ<<" profiles="<<profiles.size()<<" configs="<<N<<" uniq="<<uniq<<" u20="<<u20<<" u30="<<u30<<"\n";
}
