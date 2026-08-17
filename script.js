const search=document.querySelector("#search"), year=document.querySelector("#year");
const cards=[...document.querySelectorAll(".name-card")];
function filter(){
 const q=search.value.toLowerCase().trim(), y=year.value;
 cards.forEach(c=>{
   const okName=c.dataset.name.toLowerCase().includes(q);
   const okYear=y==="all"||c.dataset.year===y;
   c.style.display=okName&&okYear?"flex":"none";
 });
}
search.addEventListener("input",filter); year.addEventListener("change",filter);

const modal=document.querySelector("#modal"), modalName=document.querySelector("#modalName");
cards.forEach(c=>c.addEventListener("click",()=>{
 modalName.textContent=c.dataset.name;
 modal.classList.add("open"); modal.setAttribute("aria-hidden","false");
}));
document.querySelector("#close").addEventListener("click",()=>{modal.classList.remove("open");modal.setAttribute("aria-hidden","true")});
modal.addEventListener("click",e=>{if(e.target===modal) modal.classList.remove("open")});
