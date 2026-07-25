/* ===========================================================
   Invitación XV · María José Perdomo Trujillo
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
    spawnBurst();                                    //    salen mariposas volando del sobre
    if(window.__playMusic)window.__playMusic();      // arranca la música (gesto del usuario)
    if(btn)btn.style.opacity='0';
    if(cap)cap.style.opacity='0';
    setTimeout(function(){                            // 2) se desvanece el sobre -> invitación
      cover.classList.add('open');document.body.classList.remove('locked');
    },2700);
    setTimeout(function(){cover.style.display='none'},3900);
  }
  /* estallido de mariposas que salen del sobre al abrir */
  function spawnBurst(){
    var host=document.getElementById('envBurst');if(!host)return;
    var syms=['#bf','#bf-gold'],N=16;
    for(var i=0;i<N;i++){
      var b=document.createElement('div');b.className='bfly';
      var ang=(Math.PI*2)*(i/N)+(Math.random()*0.5-0.25);
      var dist=90+Math.random()*150;
      b.style.setProperty('--bx',(Math.cos(ang)*dist).toFixed(0)+'px');
      b.style.setProperty('--by',(Math.sin(ang)*dist-70).toFixed(0)+'px'); // sesgo hacia arriba
      b.style.setProperty('--br',(Math.random()*140-70).toFixed(0)+'deg');
      b.style.animation='burst '+(1.1+Math.random()*0.9).toFixed(2)+'s ease-out forwards';
      b.style.animationDelay=(Math.random()*0.18).toFixed(2)+'s';
      b.innerHTML='<svg viewBox="0 0 100 100"><use href="'+syms[i%2]+'"/></svg>';
      host.appendChild(b);
    }
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
  var msg='¡Hola! Confirmo mi asistencia a los XV de María José el 12 de septiembre. 🦋';
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
  var N=window.innerWidth<480?13:19;
  for(var i=0;i<N;i++){
    var el=document.createElement('div');el.className='bf';
    var size=34+(i*9)%52;
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
  var N=window.innerWidth<480?14:22;
  for(var i=0;i<N;i++){
    var s=document.createElement('div');s.className='spark';
    var sz=11+(i*5)%18;
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

/* ---- pétalos cayendo ---- */
(function(){
  var c=document.createElement('div');c.className='petals';document.body.appendChild(c);
  var cols=['#bcd6ef','#e7d3a1','#d7e6f5','#f0dca6','#a7c8e8'];
  var N=window.innerWidth<480?9:14;
  for(var i=0;i<N;i++){
    var p=document.createElement('div');p.className='petal';
    var w=13+(i*4)%16;
    p.style.width=w+'px';p.style.height=(w+3)+'px';
    p.style.left=((i*10.5)%98)+'%';
    p.style.background=cols[i%cols.length];
    p.style.animationDuration=(9+(i*2)%8)+'s';
    p.style.animationDelay=(-(i*1.7))+'s';
    c.appendChild(p);
  }
})();

/* ---- galería: clic para ampliar (lightbox) ---- */
(function(){
  var lb=document.getElementById('lightbox');if(!lb)return;
  var img=lb.querySelector('img');
  document.querySelectorAll('.photo img').forEach(function(el){
    el.addEventListener('click',function(){
      if(el.style.display==='none')return;               // si es placeholder, no abrir
      img.src=el.currentSrc||el.src;lb.classList.add('show');
    });
  });
  lb.addEventListener('click',function(){lb.classList.remove('show');img.src='';});
})();

/* ---- música: usa "musica.mp3" si existe; si no, la canción de YouTube ---- */
(function(){
  var VIDEO_ID='BDwEyfgClF4';               // canción elegida (YouTube)
  var btn=document.getElementById('musicBtn');
  var audio=document.getElementById('bgAudio');
  var mode=null;                            // 'mp3' | 'yt'
  var yt=null, ytReady=false, ytWant=false;

  function setPlaying(on){ if(btn) btn.classList.toggle('playing', !!on); }

  /* --- YouTube (reproductor oculto) --- */
  function loadYT(){
    if(window.YT && window.YT.Player){ initYT(); return; }
    if(document.getElementById('ytapi')) return;
    var t=document.createElement('script'); t.id='ytapi';
    t.src='https://www.youtube.com/iframe_api';
    document.head.appendChild(t);
    window.onYouTubeIframeAPIReady=initYT;
  }
  function initYT(){
    if(yt) return;
    yt=new YT.Player('ytPlayer',{
      width:'200', height:'200', videoId:VIDEO_ID,
      playerVars:{controls:0,disablekb:1,loop:1,playlist:VIDEO_ID,playsinline:1,rel:0,modestbranding:1},
      events:{
        onReady:function(){ ytReady=true; if(ytWant) ytPlay(); },
        onStateChange:function(e){
          if(e.data===YT.PlayerState.ENDED){ yt.seekTo(0); yt.playVideo(); }
          setPlaying(e.data===YT.PlayerState.PLAYING);
        }
      }
    });
  }
  function ytPlay(){
    if(!ytReady){ ytWant=true; loadYT(); return; }
    try{ yt.unMute(); yt.setVolume(75); yt.playVideo(); }catch(e){}
  }
  function ytToggle(){
    if(!yt){ ytPlay(); return; }
    var s=yt.getPlayerState();
    if(s===YT.PlayerState.PLAYING) yt.pauseVideo(); else ytPlay();
  }

  /* --- iniciar al abrir el sobre --- */
  window.__playMusic=function(){
    audio.play().then(function(){ mode='mp3'; setPlaying(true); })
      .catch(function(){ mode='yt'; ytPlay(); });   // no hay mp3 -> YouTube
  };

  /* --- botón flotante para pausar/reanudar --- */
  if(btn) btn.addEventListener('click',function(){
    if(mode==='mp3'){ if(audio.paused){audio.play();setPlaying(true);} else {audio.pause();setPlaying(false);} return; }
    if(mode==='yt'){ ytToggle(); return; }
    window.__playMusic();
  });

  /* --- iniciar la música lo antes posible --- */
  function autoStart(){ try{ window.__playMusic(); }catch(e){} }
  autoStart();                                  // intento inmediato (si el navegador lo permite)
  // respaldo: al primer gesto del usuario en cualquier parte de la página
  ['pointerdown','touchstart','click','keydown','scroll'].forEach(function(ev){
    window.addEventListener(ev, function once(){ autoStart(); }, {once:true, passive:true});
  });
})();
