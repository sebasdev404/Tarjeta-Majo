/* ===========================================================
   Invitación XVI · María José Perdomo Trujillo
   Lógica: portada, cuenta regresiva, calendario, WhatsApp,
   animaciones, mariposas y música.
   =========================================================== */

/* ---- nombre del invitado (?nombre=) ---- */
(function(){
  var n=new URLSearchParams(location.search).get('nombre');
  if(n){var g=document.getElementById('coverGuest');
    document.getElementById('coverGuestName').textContent=n.trim();g.hidden=false;}
})();

/* ---- fecha del evento ---- */
var EVENT=new Date('2026-09-12T19:00:00-05:00');

/* ---- abrir invitación (animación de sobre) ---- */
(function(){
  var cover=document.getElementById('cover'),btn=document.getElementById('openBtn'),
      env=document.getElementById('envelope'),cap=document.querySelector('.cover-cap'),
      a=document.getElementById('bgAudio'),mb=document.getElementById('musicBtn');
  function abrir(){
    if(!env||env.classList.contains('open'))return;
    env.classList.add('open');                       // 1) se abre la solapa y sube la carta
    a.play().then(function(){mb.classList.add('playing')}).catch(function(){});
    if(btn)btn.style.opacity='0';
    if(cap)cap.style.opacity='0';
    setTimeout(function(){                            // 2) se desvanece el sobre -> invitación
      cover.classList.add('open');document.body.classList.remove('locked');
    },1600);
    setTimeout(function(){cover.style.display='none'},2800);
  }
  if(btn)btn.addEventListener('click',abrir);
  if(env)env.addEventListener('click',abrir);
})();

/* ---- botón "Desliza para ver más" ---- */
(function(){
  var sm=document.getElementById('scrollMore');
  if(sm)sm.addEventListener('click',function(){
    var hero=document.querySelector('.hero'),next=hero&&hero.nextElementSibling;
    if(next)next.scrollIntoView({behavior:'smooth',block:'start'});
  });
})();

/* ---- cuenta regresiva ---- */
(function(){
  var d=document.getElementById('cd-d'),h=document.getElementById('cd-h'),
      m=document.getElementById('cd-m'),s=document.getElementById('cd-s');
  function p(n){return(n<10?'0':'')+n}
  function t(){var df=EVENT-new Date();
    if(df<=0){d.textContent='00';h.textContent='00';m.textContent='00';s.textContent='00';return;}
    var x=Math.floor(df/1000);
    d.textContent=Math.floor(x/86400);h.textContent=p(Math.floor(x%86400/3600));
    m.textContent=p(Math.floor(x%3600/60));s.textContent=p(x%60);}
  t();setInterval(t,1000);
})();

/* ---- WhatsApp ---- */
(function(){
  var msg='¡Hola! Confirmo mi asistencia a los XVI de María José el 12 de septiembre. 🦋';
  var t=encodeURIComponent(msg);
  document.getElementById('waBtn').href='https://wa.me/573157843568?text='+t;
  document.getElementById('waBtn2').href='https://wa.me/573175110288?text='+t;
})();

/* ---- reveal scroll ---- */
(function(){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('show');io.unobserve(e.target);}})},{threshold:.2});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
})();

/* ---- mariposas ---- */
(function(){
  var f=document.getElementById('field')||(function(){var d=document.createElement('div');d.className='field';d.id='field';document.body.appendChild(d);return d;})();
  var N=window.innerWidth<480?9:13;
  for(var i=0;i<N;i++){
    var el=document.createElement('div');el.className='bf';
    var size=18+(i*7)%30;
    el.style.width=size+'px';el.style.height=size+'px';
    el.style.left=((i*7.6)%95)+'%';
    el.style.animationDuration=(12+(i*3)%14)+'s';
    el.style.animationDelay=(-(i*2.1))+'s';
    var sym=(i%3===0)?'#bf-gold':'#bf'; /* 1 de cada 3 dorada */
    el.innerHTML='<svg viewBox="0 0 100 100" style="width:100%;height:100%"><use href="'+sym+'"/></svg>';
    f.appendChild(el);
  }
})();

/* ---- destellos / brillos de fondo ---- */
(function(){
  var c=document.createElement('div');c.className='sparkles';document.body.appendChild(c);
  var N=window.innerWidth<480?11:18;
  for(var i=0;i<N;i++){
    var s=document.createElement('div');s.className='spark';
    var sz=6+(i*5)%12;
    s.style.width=sz+'px';s.style.height=sz+'px';
    s.style.left=((i*6.3)%96)+'%';
    s.style.top=((i*13.7)%92)+'%';
    s.style.animationDuration=(3.4+(i*2)%4)+'s';
    s.style.animationDelay=(-(i*1.3))+'s';
    s.style.color=(i%2)?'#c4a25f':'#9cc1e6';
    s.innerHTML='<svg viewBox="0 0 24 24" style="width:100%;height:100%"><use href="#spark"/></svg>';
    c.appendChild(s);
  }
})();

/* ---- música ---- */
(function(){
  var b=document.getElementById('musicBtn'),a=document.getElementById('bgAudio');
  b.addEventListener('click',function(){
    if(a.paused){a.play().then(function(){b.classList.add('playing')}).catch(function(){b.title='Agrega "musica.mp3" en esta carpeta';});}
    else{a.pause();b.classList.remove('playing');}
  });
})();
