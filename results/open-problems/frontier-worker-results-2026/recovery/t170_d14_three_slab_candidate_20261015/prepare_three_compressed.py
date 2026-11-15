from pathlib import Path
H=Path(__file__).resolve().parent
s=(H/'t170_three_window_pilot.cpp').read_text(encoding='utf-8').replace('C<=128','C<=256')
start=s.index(' std::ofstream out(')
s=s[:start]+''' const long long scale=1099511627776LL;
 long long alpha0=std::min(scale,(long long)std::ceil(gain*scale)+1024);
 std::ofstream out(argv[3]);assert(out);out.precision(17);out<<"{\\\"dimension\\\":"<<d<<",\\\"cap\\\":"<<C<<",\\\"width\\\":3,\\\"scale\\\":"<<scale<<",\\\"alpha0_units\\\":"<<alpha0<<",\\\"gain_estimate\\\":"<<gain<<",\\\"last_change\\\":"<<change<<",\\\"sweeps\\\":"<<sweeps<<",\\\"base_bias\\\":[";
 bool first=true;for(double z:h){if(!first)out<<",";first=false;out<<(long long)std::llround(z*scale);}out<<"]}\\n";
 std::cout<<"Discovery compressed base ONLY, d="<<d<<" C="<<C<<" gain="<<gain<<" sweeps="<<sweeps<<" change="<<change<<std::endl;
}
'''
p=H/'t170_three_compressed.cpp';assert not p.exists();p.write_text(s,encoding='utf-8')
s=(H/'build_t067_independent_fusion.py').read_text(encoding='utf-8').replace('T067_INDEPENDENT_FUSION','T170_THREE_COMPRESSED').replace('t067_independent_fusion','t170_three_compressed')
p=H/'build_three_compressed.py';assert not p.exists();p.write_text(s,encoding='utf-8')
