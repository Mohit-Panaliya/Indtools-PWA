var d=(n,r,o)=>new Promise((s,t)=>{var i=e=>{try{a(o.next(e))}catch(c){t(c)}},l=e=>{try{a(o.throw(e))}catch(c){t(c)}},a=e=>e.done?s(e.value):Promise.resolve(e.value).then(i,l);a((o=o.apply(n,r)).next())});import{m,o as p,q as w,t as h,v as f}from"./index-B0WKmJOq.js";import"./frappe-ui-CYDlfguv.js";/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */const u=()=>{const n=window;n.addEventListener("statusTap",()=>{m(()=>{const r=n.innerWidth,o=n.innerHeight,s=document.elementFromPoint(r/2,o/2);if(!s)return;const t=p(s);t&&new Promise(i=>w(t,i)).then(()=>{h(()=>d(void 0,null,function*(){t.style.setProperty("--overflow","hidden"),yield f(t,300),t.style.removeProperty("--overflow")}))})})})};export{u as startStatusTap};
//# sourceMappingURL=status-tap-DA2Tgw-2.js.map
