var _=(p,i,d)=>new Promise((l,a)=>{var t=s=>{try{n(d.next(s))}catch(r){a(r)}},c=s=>{try{n(d.throw(s))}catch(r){a(r)}},n=s=>s.done?l(s.value):Promise.resolve(s.value).then(t,c);n((d=d.apply(p,i)).next())});import{a as v}from"./axios-CRcK6pnT.js";import{_ as y,r as w,o as h,l as k,c as x,a as e,t as o,F as j,m as L,e as b}from"./index-BAFYT2am.js";const B="/assets/kbc/frontend/media/silver.png",E="/assets/kbc/frontend/media/gold.jpg",F="/assets/kbc/frontend/media/bronze.jpg",z={class:"min-h-screen bg-gradient-to-br from-[#0f2027] via-[#203a43] to-[#2c5364] text-white py-10 px-4 font-['Poppins']"},C={class:"flex flex-wrap justify-center items-end gap-10 mb-16 animate-slide-in"},D={class:"flex flex-col items-center space-y-2"},I={class:"bg-white/10 px-4 py-1 rounded-full text-sm font-semibold"},K={class:"text-blue-300 text-xs font-semibold"},M={class:"flex flex-col items-center space-y-3 relative"},N={class:"bg-yellow-300 text-black px-4 py-1 rounded-full font-bold text-sm"},P={class:"text-yellow-100 text-sm font-bold"},S={class:"flex flex-col items-center space-y-2"},T={class:"bg-orange-400 text-black px-3 py-1 rounded-full text-sm font-semibold"},V={class:"text-orange-200 text-sm font-semibold"},q={class:"max-w-2xl mx-auto space-y-4"},A={class:"flex items-center gap-4"},G={class:"text-lg font-bold text-gray-300"},H={class:"font-medium"},J={class:"text-green-300 font-semibold"},O={__name:"Leaderboard",setup(p){const i=w([]),d=()=>_(this,null,function*(){try{const a=yield v.get("/api/method/kbc.api.leaderboard.get_leaderboard");i.value=a.data.message||[]}catch(a){console.error("Error fetching leaderboard:",a)}});h(()=>{d()});const l=k(()=>i.value.slice(0,3));return(a,t)=>{var c,n,s,r,u,f;return b(),x("div",z,[t[7]||(t[7]=e("h1",{class:"text-5xl font-extrabold text-center text-yellow-300 mb-14 animate-slide-in glow-text tracking-wider"}," 👑 KBC Leaderboard ",-1)),e("div",C,[e("div",D,[t[0]||(t[0]=e("img",{src:B,class:"w-20 h-20 rounded-full bg-white border-4 border-slate-300 shadow-md"},null,-1)),e("div",I,"🥈 "+o(((c=l.value[1])==null?void 0:c.player_name)||"---"),1),e("div",K,"🏅 "+o(((n=l.value[1])==null?void 0:n.total_points)||0),1),t[1]||(t[1]=e("div",{class:"bg-gray-600 w-28 h-28 flex items-center justify-center text-xl font-bold rounded-t-xl podium-glass"},"2",-1))]),e("div",M,[t[2]||(t[2]=e("div",{class:"absolute -top-10 text-4xl animate-bounce"},"👑",-1)),t[3]||(t[3]=e("img",{src:E,class:"w-24 h-24 rounded-full border-4 border-yellow-400 shadow-2xl animate-pulse"},null,-1)),e("div",N,"🥇 "+o(((s=l.value[0])==null?void 0:s.player_name)||"---"),1),e("div",P,"🏅 "+o(((r=l.value[0])==null?void 0:r.total_points)||0),1),t[4]||(t[4]=e("div",{class:"bg-yellow-500 w-32 h-36 flex items-center justify-center text-3xl font-extrabold rounded-t-xl podium-glass"},"1",-1))]),e("div",S,[t[5]||(t[5]=e("img",{src:F,class:"w-20 h-20 rounded-full border-4 border-orange-400 shadow-md"},null,-1)),e("div",T,"🥉 "+o(((u=l.value[2])==null?void 0:u.player_name)||"---"),1),e("div",V,"🏅 "+o(((f=l.value[2])==null?void 0:f.total_points)||0),1),t[6]||(t[6]=e("div",{class:"bg-gray-700 w-24 h-24 flex items-center justify-center text-xl font-bold rounded-t-xl podium-glass"},"3",-1))])]),e("div",q,[(b(!0),x(j,null,L(i.value.slice(3),(m,g)=>(b(),x("div",{key:m.player_id,class:"flex items-center justify-between backdrop-blur-md bg-white/10 hover:bg-white/20 transition-all duration-200 px-4 py-3 rounded-xl shadow-lg"},[e("div",A,[e("span",G,o(g+4),1),e("span",H,o(m.player_name),1)]),e("div",J,"🏅 "+o(m.total_points),1)]))),128))])])}}},W=y(O,[["__scopeId","data-v-f3b8d1b0"]]);export{W as default};
