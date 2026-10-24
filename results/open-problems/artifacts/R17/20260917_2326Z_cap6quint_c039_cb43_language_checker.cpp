#include <bits/stdc++.h>
using namespace std;
struct Node{array<int,26> nx; int fail=0; bool out=false; int par=-1; uint8_t pch=0; Node(){nx.fill(-1);} };
static inline pair<string,string> mp(int c,int l){int b=1-c; string a,d; if(l>=0){a.append(l,char('0'+b)); a.push_back(char('0'+c)); d.push_back(char('0'+c));} else {a.push_back(char('0'+c)); d.append(-l,char('0'+b)); d.push_back(char('0'+c));} return {a,d};}
static inline int lcsbit(const string&a,const string&b){uint64_t mask[2]={0,0}; for(int j=0;j<(int)b.size();++j) mask[b[j]-'0']|=1ULL<<j; uint64_t S=0; for(char ch:a){uint64_t x=mask[ch-'0']|S; uint64_t y=(S<<1)|1ULL; S=x & ~(x-y);} return __builtin_popcountll(S);}
static inline bool deficient(const vector<uint8_t>&w){string a,b; a.reserve(40);b.reserve(40);for(uint8_t z:w){int c=z/13,l=int(z%13)-6;auto p=mp(c,l);a+=p.first;b+=p.second;}return lcsbit(a,b)>(int)w.size();}
static inline vector<uint8_t> compw(vector<uint8_t>w){for(auto &z:w){int c=z/13,l=int(z%13)-6;z=uint8_t((1-c)*13+(l+6));}return w;}
static inline vector<uint8_t> swapw(vector<uint8_t>w){for(auto &z:w){int c=z/13,l=int(z%13)-6;z=uint8_t(c*13+((-l)+6));}return w;}
struct ArrHash{size_t operator()(array<int,27> const&a) const noexcept{uint64_t h=1469598103934665603ULL;for(int x:a){h^=(uint32_t)(x+0x9e3779b9);h*=1099511628211ULL;}return (size_t)h;}};
int main(){
 vector<vector<uint8_t>> patterns; vector<uint64_t> cnt(6);
 for(int r=2;r<=5;r++){
   uint64_t total=1;for(int i=0;i<r;i++)total*=26;
   vector<uint8_t>w(r);
   for(uint64_t code=0;code<total;code++){
     uint64_t q=code;for(int i=r-1;i>=0;i--){w[i]=q%26;q/=26;}
     if(!deficient(w))continue;
     bool minimal=true;
     if(r>2){vector<uint8_t> p(w.begin(),w.end()-1),s(w.begin()+1,w.end()); if(deficient(p)||deficient(s))minimal=false;}
     if(minimal){cnt[r]++;patterns.push_back(w);}
   }
   cerr<<"r="<<r<<" minimal="<<cnt[r]<<" cumulative="<<patterns.size()<<"\n";
 }
 if(cnt[2]!=100 || cnt[3]!=1908 || cnt[4]!=26124 || cnt[5]!=286796){cerr<<"COUNT_MISMATCH\n";return 3;}
 for(int r=2;r<=3;r++){
   int K=50; uint64_t total=1;for(int i=0;i<r;i++)total*=K; vector<int> vals;for(int c=0;c<2;c++)for(int l=-12;l<=12;l++)vals.push_back(c*100+(l+50));
   vector<uint8_t> wc(r),wcap(r);
   for(uint64_t code=0;code<total;code++){
     uint64_t q=code;for(int i=r-1;i>=0;i--){int vv=vals[q%K];q/=K;int c=vv/100,l=(vv%100)-50;int z=max(-6,min(6,l));wcap[i]=uint8_t(c*13+(z+6));}
     q=code; string a,b; vector<pair<int,int>> ww(r);for(int i=r-1;i>=0;i--){int vv=vals[q%K];q/=K;int c=vv/100,l=(vv%100)-50;ww[i]={c,l};}
     for(auto [c,l]:ww){auto p=mp(c,l);a+=p.first;b+=p.second;}
     bool dtrue=lcsbit(a,b)>r; bool dcap=deficient(wcap); if(dtrue!=dcap){cerr<<"CAP_REG_FAIL\n";return 4;}
   }
 }
 vector<Node> nd;nd.reserve(400000);nd.emplace_back();
 for(auto const&p:patterns){int q=0;for(uint8_t a:p){if(nd[q].nx[a]<0){nd[q].nx[a]=nd.size();nd.emplace_back();nd.back().par=q;nd.back().pch=a;}q=nd[q].nx[a];}nd[q].out=true;}
 queue<int> qu;
 for(int a=0;a<26;a++){int q=nd[0].nx[a];if(q>=0){nd[q].fail=0;qu.push(q);}else nd[0].nx[a]=0;}
 while(!qu.empty()){int r=qu.front();qu.pop();nd[r].out=nd[r].out||nd[nd[r].fail].out;for(int a=0;a<26;a++){int s=nd[r].nx[a];if(s>=0){nd[s].fail=nd[nd[r].fail].nx[a];qu.push(s);}else nd[r].nx[a]=nd[nd[r].fail].nx[a];}}
 vector<int> safe,si(nd.size(),-1);for(int q=0;q<(int)nd.size();q++)if(!nd[q].out){si[q]=safe.size();safe.push_back(q);}int sink=safe.size(),N=sink+1;
 vector<array<int,26>> T(N);for(int i=0;i<sink;i++){int q=safe[i];for(int a=0;a<26;a++){int r=nd[q].nx[a];T[i][a]=nd[r].out?sink:si[r];}}T[sink].fill(sink);
 vector<int> cls(N,0);cls[sink]=1;int oldk=2;
 while(true){unordered_map<array<int,27>,int,ArrHash> mpmap;mpmap.reserve(N*2);vector<int> nc(N);int k=0;for(int q=0;q<N;q++){array<int,27> sig;sig[0]=(q==sink);for(int a=0;a<26;a++)sig[a+1]=cls[T[q][a]];auto [it,ins]=mpmap.emplace(sig,k);if(ins)k++;nc[q]=it->second;}cls.swap(nc);cerr<<"Moore classes="<<k<<"\n";if(k==oldk)break;oldk=k;}
 int K=*max_element(cls.begin(),cls.end())+1, sinkc=cls[sink];if(K!=5188){cerr<<"MIN_STATE_MISMATCH K="<<K<<"\n";return 5;}
 vector<int> cmap(K,-1),rep(K,-1);int dk=0;for(int c=0;c<K;c++)if(c!=sinkc)cmap[c]=dk++;if(dk!=5187)return 6;for(int q=0;q<sink;q++)if(rep[cls[q]]<0)rep[cls[q]]=q;
 vector<array<int16_t,26>> TR(dk);for(int c=0;c<K;c++)if(c!=sinkc){int i=cmap[c],q=rep[c];for(int a=0;a<26;a++){int cc=cls[T[q][a]];TR[i][a]=(cc==sinkc)?-1:cmap[cc];}}
 int START=cmap[cls[si[0]]];
 auto wordOf=[&](int safidx){int node=safe[safidx];vector<uint8_t>w;while(node){w.push_back(nd[node].pch);node=nd[node].par;}reverse(w.begin(),w.end());return w;};
 auto walk=[&](const vector<uint8_t>&w){int q=0;for(uint8_t a:w)q=nd[q].nx[a];return q;};
 vector<uint16_t> CM(dk),SM(dk);int fixedC=0,fixedS=0;
 for(int c=0;c<K;c++)if(c!=sinkc){int i=cmap[c];auto w=wordOf(rep[c]);int qc=walk(compw(w)),qs=walk(swapw(w));if(nd[qc].out||nd[qs].out){cerr<<"AUTO_REJECT\n";return 7;}CM[i]=cmap[cls[si[qc]]];SM[i]=cmap[cls[si[qs]]];}
 for(int i=0;i<dk;i++){if(CM[CM[i]]!=i||SM[SM[i]]!=i||CM[SM[i]]!=SM[CM[i]]){cerr<<"AUTO_FAIL\n";return 8;}fixedC+=CM[i]==i;fixedS+=SM[i]==i;for(int a=0;a<26;a++){int c=a/13,l=a%13-6;int ac=(1-c)*13+(l+6),as=c*13+((-l)+6);int t=TR[i][a],tc=TR[CM[i]][ac],ts=TR[SM[i]][as];if(!((t<0&&tc<0)||(t>=0&&tc==CM[t])) || !((t<0&&ts<0)||(t>=0&&ts==SM[t]))){cerr<<"EQ_FAIL\n";return 9;}}}
 cout<<"R17 C039 exact cap-6 length<=5 deficiency language checker\n";
 cout<<"cap6_symbols=26\n"<<"deficient_pair_classes="<<cnt[2]<<"\nminimal_deficient_triple_classes="<<cnt[3]<<"\nminimal_deficient_quadruple_classes="<<cnt[4]<<"\nminimal_deficient_quintuple_classes="<<cnt[5]<<"\nforbidden_patterns_total="<<patterns.size()<<"\n";
 cout<<"aho_total_nodes="<<nd.size()<<"\naho_nonrejecting_nodes="<<safe.size()<<"\nminimized_total_states_including_reject="<<K<<"\nminimized_nonrejecting_states="<<dk<<"\ncomplement_fixed_safe_states="<<fixedC<<"\nswap_fixed_safe_states="<<fixedS<<"\nstart_state="<<START<<"\n";
 cout<<"EXACT_CAP6_PAIR_TRIPLE_WIDE_REGRESSION_PASS\nEXACT_DFA_MINIMIZATION_PASS\nEXACT_COMPLEMENT_AUTOMORPHISM_PASS\nEXACT_SWAP_AUTOMORPHISM_PASS\nALL_EXACT_CHECKS_PASS\n";
 ofstream f("c039_dfa5187.h");f<<"#pragma once\nstatic constexpr int DFAK=5187, DFAAL=26, DFASTART="<<START<<";\nstatic const int16_t DFATR[DFAK][DFAAL] = {\n";for(auto const&r:TR){f<<"  {";for(int a=0;a<26;a++){if(a)f<<',';f<<r[a];}f<<"},\n";}f<<"};\nstatic const uint16_t DFACM[DFAK] = {";for(int i=0;i<dk;i++){if(i)f<<',';f<<CM[i];}f<<"};\nstatic const uint16_t DFASM[DFAK] = {";for(int i=0;i<dk;i++){if(i)f<<',';f<<SM[i];}f<<"};\n";
}
