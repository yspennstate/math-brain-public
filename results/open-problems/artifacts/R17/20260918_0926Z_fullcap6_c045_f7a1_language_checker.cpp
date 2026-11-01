#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
static constexpr int AL=30;
struct Fac { uint64_t a=0,b=0; uint8_t al=0,bl=0; };
static Fac F[AL];
static void initF(){
 for(int z=0;z<AL;z++){int c=z/15,l=z%15-7,b=1-c; Fac f; int pa=0,pb=0;
   auto pusha=[&](int x){ if(x) f.a|=1ULL<<pa; pa++; };
   auto pushb=[&](int x){ if(x) f.b|=1ULL<<pb; pb++; };
   if(l>=0){for(int i=0;i<l;i++) pusha(b); pusha(c); pushb(c);} else {pusha(c); for(int i=0;i<-l;i++) pushb(b); pushb(c);} f.al=pa;f.bl=pb;F[z]=f;
 }
}
static inline bool def_code(uint64_t code,int r){uint8_t w[6]; for(int i=r-1;i>=0;i--){w[i]=code%AL;code/=AL;} uint64_t A=0,B=0;int al=0,bl=0;for(int i=0;i<r;i++){auto &f=F[w[i]];A|=f.a<<al;B|=f.b<<bl;al+=f.al;bl+=f.bl;}uint64_t full=bl==64?~0ULL:((1ULL<<bl)-1);uint64_t m1=B,m0=(~B)&full,S=0;for(int i=0;i<al;i++){uint64_t m=((A>>i)&1)?m1:m0;uint64_t x=m|S,y=(S<<1)|1;S=x&~(x-y);}return __builtin_popcountll(S)>r;}
struct Bits{vector<uint64_t>v;Bits(){}Bits(uint64_t n):v((n+63)/64){}inline void set(uint64_t i){v[i>>6]|=1ULL<<(i&63);}inline bool get(uint64_t i)const{return (v[i>>6]>>(i&63))&1;}};
static vector<uint8_t> compw(vector<uint8_t>w){for(auto&z:w){int c=z/15,l=int(z%15)-7;z=(1-c)*15+l+7;}return w;}
static vector<uint8_t> swapw(vector<uint8_t>w){for(auto&z:w){int c=z/15,l=int(z%15)-7;z=c*15+(-l)+7;}return w;}
struct Node{array<int,AL> nx;int fail=0;bool out=false;int par=-1;uint8_t pch=0;Node(){nx.fill(-1);}};
struct Sig{array<int,AL+1>a; bool operator==(Sig const&o)const{return a==o.a;}};
struct SH{size_t operator()(Sig const&s)const noexcept{uint64_t h=1469598103934665603ULL;for(int x:s.a){h^=(uint32_t)(x+0x9e3779b9);h*=1099511628211ULL;}return h;}};
int main(){initF(); omp_set_num_threads(min(8,omp_get_max_threads()));
 uint64_t pw[7]={1};for(int r=1;r<=6;r++)pw[r]=pw[r-1]*AL;
 vector<Bits>D(7);for(int r=2;r<=5;r++){D[r]=Bits(pw[r]);
#pragma omp parallel for schedule(static)
  for(long long cc=0;cc<(long long)pw[r];cc++)if(def_code((uint64_t)cc,r))D[r].set((uint64_t)cc);
  cerr<<"D"<<r<<" done\n";
 }
 vector<pair<uint8_t,uint64_t>> base;uint64_t cnt[7]={0};
 for(int r=2;r<=5;r++){for(uint64_t code=0;code<pw[r];code++)if(D[r].get(code)){bool minv=true;if(r>2){uint64_t pref=code/AL,suf=code%pw[r-1];if(D[r-1].get(pref)||D[r-1].get(suf))minv=false;}if(minv){cnt[r]++;base.push_back({(uint8_t)r,code});}}}
 cerr<<"base counts "<<cnt[2]<<" "<<cnt[3]<<" "<<cnt[4]<<" "<<cnt[5]<<"\n";
 int nt=omp_get_max_threads();vector<vector<uint64_t>> loc(nt);
#pragma omp parallel
 {int tid=omp_get_thread_num();auto &v=loc[tid];v.reserve(1000000);
#pragma omp for schedule(static)
  for(long long cc=0;cc<(long long)pw[6];cc++){uint64_t code=(uint64_t)cc;uint64_t pref=code/AL,suf=code%pw[5];if(D[5].get(pref)||D[5].get(suf))continue;if(def_code(code,6))v.push_back(code);} }
 size_t n6=0;for(auto&v:loc)n6+=v.size();vector<uint64_t>six;six.reserve(n6);for(auto&v:loc)six.insert(six.end(),v.begin(),v.end());sort(six.begin(),six.end());cnt[6]=six.size();cerr<<"FULLCAP7_MIN6_COUNT="<<cnt[6]<<"\n";
 auto transcode=[&](uint64_t code,bool comp,bool sw){uint8_t d[6];for(int i=5;i>=0;i--){int z=code%AL;code/=AL;int c=z/15,l=z%15-7;if(comp)c=1-c;if(sw)l=-l;d[i]=c*15+(l+7);}uint64_t out=0;for(int i=0;i<6;i++)out=out*AL+d[i];return out;};
 for(uint64_t z:six){if(!binary_search(six.begin(),six.end(),transcode(z,true,false))||!binary_search(six.begin(),six.end(),transcode(z,false,true))){cerr<<"six symmetry fail\n";return 3;}}cerr<<"six symmetry done\n";
 size_t totalp=base.size()+six.size();vector<Node>nd;nd.reserve(totalp*2);nd.emplace_back();auto insertw=[&](const uint8_t*w,int r){int q=0;for(int i=0;i<r;i++){int a=w[i];if(nd[q].nx[a]<0){nd[q].nx[a]=nd.size();nd.emplace_back();nd.back().par=q;nd.back().pch=a;}q=nd[q].nx[a];}nd[q].out=true;};
 for(auto [r,code]:base){uint8_t w[6];for(int i=r-1;i>=0;i--){w[i]=code%AL;code/=AL;}insertw(w,r);}for(uint64_t code:six){uint8_t w[6];for(int i=5;i>=0;i--){w[i]=code%AL;code/=AL;}insertw(w,6);}cerr<<"trie nodes="<<nd.size()<<"\n";
 queue<int>qu;for(int a=0;a<AL;a++){int q=nd[0].nx[a];if(q>=0)qu.push(q);else nd[0].nx[a]=0;}while(!qu.empty()){int r=qu.front();qu.pop();nd[r].out|=nd[nd[r].fail].out;for(int a=0;a<AL;a++){int s=nd[r].nx[a];if(s>=0){nd[s].fail=nd[nd[r].fail].nx[a];qu.push(s);}else nd[r].nx[a]=nd[nd[r].fail].nx[a];}}
 vector<int>safe,si(nd.size(),-1);safe.reserve(nd.size());for(int q=0;q<(int)nd.size();q++)if(!nd[q].out){si[q]=safe.size();safe.push_back(q);}int sink=safe.size(),N=sink+1;cerr<<"safe="<<sink<<"\n";
 vector<array<int,AL>>T(N);for(int i=0;i<sink;i++){int q=safe[i];for(int a=0;a<AL;a++){int r=nd[q].nx[a];T[i][a]=nd[r].out?sink:si[r];}}T[sink].fill(sink);vector<int>cls(N);cls[sink]=1;int oldk=2;
 while(1){unordered_map<Sig,int,SH>M;M.reserve(N*2);vector<int>nc(N);int k=0;for(int q=0;q<N;q++){Sig s;s.a[0]=(q==sink);for(int a=0;a<AL;a++)s.a[a+1]=cls[T[q][a]];auto[it,ins]=M.emplace(s,k);if(ins)k++;nc[q]=it->second;}cls.swap(nc);cerr<<"classes="<<k<<"\n";if(k==oldk)break;oldk=k;}
 int classes=*max_element(cls.begin(),cls.end())+1,sinkc=cls[sink];vector<int>cmap(classes,-1),rep(classes,-1);int dk=0;for(int c=0;c<classes;c++)if(c!=sinkc)cmap[c]=dk++;for(int q=0;q<sink;q++)if(rep[cls[q]]<0)rep[cls[q]]=q;vector<array<int32_t,AL>>TR(dk);for(int c=0;c<classes;c++)if(c!=sinkc){int i=cmap[c],q=rep[c];for(int a=0;a<AL;a++){int cc=cls[T[q][a]];TR[i][a]=(cc==sinkc)?-1:cmap[cc];}}int START=cmap[cls[si[0]]];
 auto wordOf=[&](int safidx){int node=safe[safidx];vector<uint8_t>w;while(node){w.push_back(nd[node].pch);node=nd[node].par;}reverse(w.begin(),w.end());return w;};auto walk=[&](const vector<uint8_t>&w){int q=0;for(auto a:w)q=nd[q].nx[a];return q;};vector<uint32_t>CM(dk),SM(dk);for(int c=0;c<classes;c++)if(c!=sinkc){int i=cmap[c];auto ww=wordOf(rep[c]);int qc=walk(compw(ww)),qs=walk(swapw(ww));if(nd[qc].out||nd[qs].out){cerr<<"auto reject\n";return 5;}CM[i]=cmap[cls[si[qc]]];SM[i]=cmap[cls[si[qs]]];}
 for(int i=0;i<dk;i++){if(CM[CM[i]]!=(uint32_t)i||SM[SM[i]]!=(uint32_t)i||CM[SM[i]]!=SM[CM[i]]){cerr<<"involution fail\n";return 6;}for(int a=0;a<AL;a++){int c=a/15,l=a%15-7,ac=(1-c)*15+l+7,as=c*15+(-l)+7;int t=TR[i][a],tc=TR[CM[i]][ac],ts=TR[SM[i]][as];if(!((t<0&&tc<0)||(t>=0&&tc==(int)CM[t]))||!((t<0&&ts<0)||(t>=0&&ts==(int)SM[t]))){cerr<<"equiv fail i="<<i<<" a="<<a<<"\n";return 7;}}}
 cout<<"R17 C045 complete cap7 length<=6 deficiency language checker\nmin_deficient_2="<<cnt[2]<<"\nmin_deficient_3="<<cnt[3]<<"\nmin_deficient_4="<<cnt[4]<<"\nmin_deficient_5="<<cnt[5]<<"\nmin_deficient_6="<<cnt[6]<<"\npatterns_total="<<totalp<<"\naho_nodes="<<nd.size()<<"\nsafe_aho_nodes="<<safe.size()<<"\nminimized_nonrejecting_states="<<dk<<"\nstart="<<START<<"\nEXACT_FULL_CAP7_MIN6_COUNT_PASS\nEXACT_SYMMETRY_CLOSURE_PASS\nEXACT_DFA_MINIMIZATION_PASS\nALL_EXACT_CHECKS_PASS\n";
 ofstream f("/mnt/data/c045_dfa.h");f<<"#pragma once\nstatic constexpr int DFAK="<<dk<<",DFAAL="<<AL<<",DFASTART="<<START<<";\nstatic const int32_t DFATR[DFAK][DFAAL]={\n";for(auto&r:TR){f<<"{";for(int a=0;a<AL;a++){if(a)f<<',';f<<r[a];}f<<"},\n";}f<<"};\nstatic const uint32_t DFACM[DFAK]={";for(int i=0;i<dk;i++){if(i)f<<',';f<<CM[i];}f<<"};\n";
}
