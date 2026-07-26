import openpyxl
import urllib.parse
import json

BASE_URL = "https://tarjeta-majo.vercel.app"

wb = openpyxl.load_workbook(r"C:\Users\SebasDev\Desktop\Tarjeta Majo\LISTADO INVITADOS POR TAJETA MAJO.xlsx")
ws = wb.active

links = []
for row in ws.iter_rows(min_row=2, values_only=True):
    invitado, num, tarjeta = (str(c).strip() if c is not None else "" for c in row)
    if tarjeta:
        count = num if num and num.replace(".0","").isdigit() else "1"
        links.append({
            "nombre": tarjeta.strip(),
            "invitados": int(float(count))
        })

wb.close()

# Ordenar alfabéticamente
links.sort(key=lambda x: x["nombre"].lower())

data_json = json.dumps(links, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lista de invitados · XV María José</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Pinyon+Script&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bb-50:#f5faff;
  --bb-100:#eef5fc;
  --bb-200:#dcebf9;
  --bb-300:#c2dcf2;
  --bb-400:#a7c8e8;
  --bb-500:#7ea9d6;
  --bb-600:#3f648f;
  --ink:#243240;
  --ink-soft:#46586d;
  --gold:#c4a25f;
  --gold-2:#e7d3a1;
  --gold-3:#f6efdc;
  --gold-deep:#a8863f;
  --shadow:0 12px 30px -16px rgba(40,70,110,.4);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Cormorant Garamond',serif;color:var(--ink);background:var(--bb-100);-webkit-font-smoothing:antialiased;min-height:100vh}}
.bg{{
  position:fixed;inset:0;z-index:0;
  background:
    radial-gradient(900px 520px at 50% -6%,#fff,transparent 60%),
    radial-gradient(680px 480px at 112% 18%,var(--bb-200),transparent 55%),
    radial-gradient(680px 520px at -12% 82%,var(--bb-200),transparent 55%),
    linear-gradient(180deg,var(--bb-100),#fff 45%,var(--bb-100));
}}
.watermark{{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);
  font-family:'Pinyon Script',cursive;font-size:min(80vw,800px);line-height:1;
  color:rgba(126,169,214,.045);user-select:none;white-space:nowrap;pointer-events:none;z-index:0;
}}
.header{{
  position:relative;z-index:1;text-align:center;padding:56px 20px 28px;
  background:linear-gradient(180deg,rgba(255,255,255,.85),transparent);
}}
.header .eyebrow{{font-family:'Montserrat',sans-serif;font-weight:500;letter-spacing:.4em;text-transform:uppercase;font-size:.9rem;color:var(--gold-deep)}}
.header h1{{font-family:'Pinyon Script',cursive;font-size:clamp(3.2rem,12vw,4.4rem);color:var(--bb-600);font-weight:400;margin-top:4px}}
.header .sub{{font-family:'Montserrat',sans-serif;font-weight:300;letter-spacing:.3em;text-transform:uppercase;font-size:.9rem;color:var(--ink-soft);margin-top:8px}}
.stats{{
  position:relative;z-index:1;display:flex;justify-content:center;gap:24px;padding:0 20px 24px;flex-wrap:wrap;
}}
.stat{{
  background:rgba(255,255,255,.88);border:1px solid rgba(196,162,95,.35);border-radius:10px;
  padding:16px 32px;text-align:center;min-width:160px;box-shadow:var(--shadow);
}}
.stat .n{{font-size:2.8rem;font-weight:500;color:var(--bb-600);line-height:1}}
.stat .l{{font-family:'Montserrat',sans-serif;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-soft);margin-top:4px}}

.search-bar{{
  position:relative;z-index:1;max-width:600px;margin:0 auto 22px;padding:0 20px;
}}
.search-bar input{{
  width:100%;padding:18px 24px 18px 56px;border:1px solid rgba(196,162,95,.4);border-radius:999px;
  font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--ink);
  background:rgba(255,255,255,.92);box-shadow:var(--shadow);outline:none;
  transition:border-color .3s, box-shadow .3s;
}}
.search-bar input:focus{{border-color:var(--gold);box-shadow:0 0 0 3px rgba(196,162,95,.2)}}
.search-bar svg{{
  position:absolute;left:36px;top:50%;transform:translateY(-50%);width:22px;height:22px;
  color:var(--gold-deep);pointer-events:none;
}}

.actions{{
  position:relative;z-index:1;display:flex;justify-content:center;gap:14px;padding:0 20px 24px;flex-wrap:wrap;
}}
.btn{{
  display:inline-flex;align-items:center;gap:8px;
  font-family:'Montserrat',sans-serif;font-weight:500;letter-spacing:.2em;text-transform:uppercase;
  font-size:.7rem;text-decoration:none;cursor:pointer;
  border:1px solid var(--gold);border-radius:999px;padding:12px 28px;
  background:linear-gradient(180deg,#fff,var(--gold-3));color:var(--gold-deep);transition:.3s;
}}
.btn:hover{{background:var(--gold);color:#fff}}
.btn.primary{{background:var(--bb-600);color:#fff;border-color:var(--bb-600)}}
.btn.primary:hover{{background:var(--bb-500);border-color:var(--bb-500)}}

.container{{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 20px 80px}}

.card{{
  background:linear-gradient(180deg,rgba(255,255,255,.94),rgba(255,255,255,.8));
  border:1px solid rgba(196,162,95,.35);border-radius:12px;padding:20px 24px;
  margin-bottom:12px;box-shadow:var(--shadow);position:relative;display:flex;align-items:center;gap:18px;
  transition:opacity .3s, transform .3s;
}}
.card.hidden{{display:none}}
.card .badge{{
  flex:0 0 auto;width:60px;height:60px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-family:'Montserrat',sans-serif;font-weight:600;font-size:1.2rem;
  background:var(--bb-600);color:var(--gold-2);
  box-shadow:0 4px 12px -4px rgba(63,100,143,.45);
}}
.card .info{{flex:1;min-width:0}}
.card .info .name{{font-size:2rem;color:var(--ink);font-weight:500;line-height:1.3}}
.card .info .url{{display:block;font-size:1rem;color:var(--bb-500);word-break:break-all;margin-top:6px;font-family:'Montserrat',sans-serif}}
.card .info .url a{{color:var(--bb-500);text-decoration:none}}
.card .info .url a:hover{{text-decoration:underline;color:var(--bb-600)}}
.card .btns{{display:flex;gap:8px;flex:0 0 auto}}
.card .btns a,.card .btns button{{
  width:44px;height:44px;border-radius:50%;border:1px solid rgba(196,162,95,.3);
  display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;
  background:rgba(255,255,255,.9);color:var(--bb-600);transition:.25s;font-size:0;
}}
.card .btns a:hover,.card .btns button:hover{{background:var(--gold);color:#fff;border-color:var(--gold)}}
.card .btns svg{{width:20px;height:20px}}
.card .btns .copied{{background:#25d366!important;color:#fff!important;border-color:#25d366!important}}

.modal-overlay{{
  position:fixed;inset:0;z-index:100;background:rgba(36,50,64,.6);backdrop-filter:blur(3px);
  display:none;align-items:center;justify-content:center;padding:24px;
}}
.modal-overlay.show{{display:flex}}
.modal{{
  background:var(--bb-50);border:1px solid var(--gold);border-radius:14px;
  padding:40px 32px;max-width:480px;width:100%;box-shadow:0 30px 60px -30px rgba(0,0,0,.5);
  position:relative;
}}
.modal h2{{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:2.2rem;color:var(--ink);margin-bottom:20px}}
.modal .field{{margin-bottom:18px}}
.modal .field label{{display:block;font-family:'Montserrat',sans-serif;font-size:.75rem;letter-spacing:.26em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:6px}}
.modal .field input{{
  width:100%;padding:14px 18px;border:1px solid rgba(196,162,95,.4);border-radius:8px;
  font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--ink);
  background:#fff;outline:none;transition:border-color .3s;
}}
.modal .field input:focus{{border-color:var(--gold)}}
.modal .modal-actions{{display:flex;gap:12px;justify-content:flex-end;margin-top:24px}}
.modal .close-btn{{
  position:absolute;top:14px;right:18px;background:none;border:0;
  font-size:2rem;cursor:pointer;color:var(--ink-soft);line-height:1;
}}

.empty{{text-align:center;padding:50px 20px;color:var(--ink-soft);font-size:1.6rem}}

footer{{
  position:relative;z-index:1;text-align:center;padding:28px 20px 48px;
  font-family:'Montserrat',sans-serif;font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink-soft);
}}

@media (max-width:600px){{
  .card{{flex-wrap:wrap;padding:16px 18px}}
  .card .btns{{width:100%;justify-content:flex-end}}
  .stat{{min-width:110px;padding:12px 18px}}
  .stat .n{{font-size:2.2rem}}
}}

/* pantalla de login */
.login-screen{{
  position:fixed;inset:0;z-index:200;background:var(--bb-100);
  display:flex;align-items:center;justify-content:center;padding:20px;
}}
.login-box{{
  background:rgba(255,255,255,.95);border:1px solid var(--gold);border-radius:14px;
  padding:40px 32px;max-width:380px;width:100%;text-align:center;box-shadow:0 30px 60px -30px rgba(0,0,0,.4);
}}
.login-icon{{color:var(--bb-600);margin-bottom:10px}}
.login-icon svg{{width:48px;height:48px}}
.login-title{{font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:var(--ink);font-weight:500}}
.login-sub{{font-family:'Montserrat',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-soft);margin:8px 0 18px}}
.login-input{{
  width:100%;padding:14px 18px;border:1px solid rgba(196,162,95,.4);border-radius:8px;
  font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:var(--ink);background:#fff;
  outline:none;transition:border-color .3s;text-align:center;
}}
.login-input:focus{{border-color:var(--gold)}}
.login-error{{font-family:'Montserrat',sans-serif;font-size:.55rem;color:#c0392b;margin-top:10px;min-height:20px}}
</style>
</head>
<body>
<div class="bg"><span class="watermark">MJ</span></div>

<!-- Pantalla de login -->
<div class="login-screen" id="loginScreen">
  <div class="login-box">
    <div class="login-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
    </div>
    <div class="login-title">Acceso restringido</div>
    <div class="login-sub">Ingresa la contrase\u00f1a para administrar los invitados</div>
    <input class="login-input" type="password" id="loginPwd" placeholder="Contrase\u00f1a" autocomplete="off">
    <button class="btn primary" id="loginBtn" style="width:100%;justify-content:center;margin-top:12px">Entrar</button>
    <div class="login-error" id="loginError"></div>
  </div>
</div>

<div class="header">
  <div class="eyebrow">XV años · María José</div>
  <h1>Lista de invitados</h1>
  <div class="sub">12 de septiembre · 2026 · Hacienda Santa Clara</div>
</div>

<div class="stats" id="stats"></div>

<div class="search-bar">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/></svg>
  <input type="text" id="searchInput" placeholder="Buscar por nombre de tarjeta..." autocomplete="off">
</div>

<div class="actions">
  <button class="btn primary" id="addBtn">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><path d="M12 5v14M5 12h14"/></svg>
    Nueva tarjeta
  </button>
  <button class="btn" id="exportBtn">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
    Exportar
  </button>
</div>

<div class="container" id="list"></div>

<!-- Modal nueva tarjeta -->
<div class="modal-overlay" id="modal">
  <div class="modal">
    <button class="close-btn" id="modalClose">&times;</button>
    <h2>Nueva tarjeta</h2>
    <div class="field">
      <label>Nombre de la tarjeta</label>
      <input type="text" id="modalNombre" placeholder="Ej: Familia Pérez">
    </div>
    <div class="field">
      <label>Invitados</label>
      <input type="number" id="modalInvitados" placeholder="Ej: 4" min="1" value="1">
    </div>
    <div class="modal-actions">
      <button class="btn" id="modalCancel">Cancelar</button>
      <button class="btn primary" id="modalSave">Crear tarjeta</button>
    </div>
  </div>
</div>

<footer>Hecho con cariño para los XV de María José &middot; <span id="footerCount"></span></footer>

<script>
var BASE = {json.dumps(BASE_URL)};
var DATA = {data_json};

/* ---- protecci\u00f3n con contrase\u00f1a ---- */
(function(){{
  var PWD='majo123';
  var s=new URLSearchParams(location.search);
  if(s.get('pwd')===PWD){{try{{sessionStorage.setItem('mj_auth','1');}}catch(e){{}}}}
  var auth=false;
  try{{auth=sessionStorage.getItem('mj_auth')==='1';}}catch(e){{}}
  if(!auth){{
    document.getElementById('loginScreen').style.display='flex';
    var inp=document.getElementById('loginPwd');
    var err=document.getElementById('loginError');
    function check(){{
      if(inp.value===PWD){{
        try{{sessionStorage.setItem('mj_auth','1');}}catch(e){{}}
        document.getElementById('loginScreen').style.display='none';
        document.querySelectorAll('.header,.stats,.search-bar,.actions,.container,footer').forEach(function(el){{
          el.style.display='';
        }});
        render('');
      }}else{{
        err.textContent='Contrase\u00f1a incorrecta';
        inp.value='';inp.focus();
      }}
    }}
    document.getElementById('loginBtn').addEventListener('click',check);
    inp.addEventListener('keydown',function(e){{if(e.key==='Enter')check()}});
    inp.focus();
    document.querySelectorAll('.header,.stats,.search-bar,.actions,.container,footer').forEach(function(el){{
      el.style.display='none';
    }});
  }}else{{
    document.getElementById('loginScreen').style.display='none';
  }}
}})();

function loadSaved(){{
  try{{var d=localStorage.getItem('mj_tarjetas');if(d){{var p=JSON.parse(d);if(Array.isArray(p)&&p.length)DATA=p;}}}}catch(e){{}}
}}
function saveData(){{
  try{{localStorage.setItem('mj_tarjetas',JSON.stringify(DATA));}}catch(e){{}}
}}

loadSaved();
/* solo ordenar si es la primera vez (sin datos guardados) */
if(!localStorage.getItem('mj_tarjetas')){{
  DATA.sort(function(a,b){{return a.nombre.toLowerCase().localeCompare(b.nombre.toLowerCase())}});
}}

function render(q){{
  q=(q||'').toLowerCase().trim();
  var html='',count=0,totalInv=0;
  DATA.forEach(function(d,i){{
    var match=!q||d.nombre.toLowerCase().indexOf(q)!==-1;
    if(!match)return;
    count++;totalInv+=d.invitados;
    var url=BASE+'/?nombre='+encodeURIComponent(d.nombre)+'&invitados='+d.invitados;
    var wa='https://wa.me/?text='+encodeURIComponent(url+'\\n\\n\\u2728 Con mucha ilusi\\u00f3n te comparto la invitaci\\u00f3n a mis XV a\\u00f1os. Ser\\u00e1 una noche m\\u00e1gica llena de sue\\u00f1os, mariposas y momentos especiales. \\u00a1Me encantar\\u00eda que est\\u00e9s ah\\u00ed para celebrarlo juntos! \\u00a1Te espero con todo mi coraz\\u00f3n! \\ud83e\\udd8b\\u2728');
    html+='<div class="card" data-index="'+i+'">'+
      '<div class="badge">'+d.invitados+'</div>'+
      '<div class="info"><div class="name">'+esc(d.nombre)+'</div>'+
      '<span class="url"><a href="'+url+'" target="_blank">'+esc(url)+'</a></span></div>'+
      '<div class="btns">'+
        '<a href="'+wa+'" target="_blank" title="Enviar por WhatsApp">'+
          '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'+
        '</a>'+
        '<a href="'+url+'" target="_blank" title="Abrir invitaci\\u00f3n">'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'+
        '</a>'+
        '<button onclick="copiar('+i+',this)" title="Copiar link">'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'+
        '</button>'+
        '<button onclick="eliminar('+i+',this)" title="Eliminar tarjeta">'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>'+
        '</button>'+
      '</div></div>';
  }});
  document.getElementById('list').innerHTML=html||'<div class="empty">No se encontraron tarjetas</div>';
  document.getElementById('stats').innerHTML=
    '<div class="stat"><div class="n">'+count+'</div><div class="l">Tarjetas</div></div>'+
    '<div class="stat"><div class="n">'+totalInv+'</div><div class="l">Invitados</div></div>';
  document.getElementById('footerCount').textContent=count+' tarjetas · '+totalInv+' invitados';
}}

function esc(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}

function copiar(i,btn){{
  var url=BASE+'/?nombre='+encodeURIComponent(DATA[i].nombre)+'&invitados='+DATA[i].invitados;
  if(navigator.clipboard){{navigator.clipboard.writeText(url);}}else{{return}}
  btn.classList.add('copied');
  var orig=btn.innerHTML;
  btn.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="16" height="16"><polyline points="20 6 9 17 4 12"/></svg>';
  setTimeout(function(){{btn.classList.remove('copied');btn.innerHTML=orig;}},1800);
}}

function eliminar(i,btn){{
  if(!confirm('\\u00bfEliminar "'+DATA[i].nombre+'"?'))return;
  DATA.splice(i,1);
  saveData();
  render(document.getElementById('searchInput').value);
}}

/* buscar */
document.getElementById('searchInput').addEventListener('input',function(){{
  render(this.value);
}});

/* modal */
var modal=document.getElementById('modal');
document.getElementById('addBtn').addEventListener('click',function(){{
  document.getElementById('modalNombre').value='';
  document.getElementById('modalInvitados').value='1';
  modal.classList.add('show');
  setTimeout(function(){{document.getElementById('modalNombre').focus();}},100);
}});
function cerrarModal(){{modal.classList.remove('show')}}
document.getElementById('modalClose').addEventListener('click',cerrarModal);
document.getElementById('modalCancel').addEventListener('click',cerrarModal);
modal.addEventListener('click',function(e){{if(e.target===modal)cerrarModal()}});

document.getElementById('modalSave').addEventListener('click',function(){{
  var nom=document.getElementById('modalNombre').value.trim();
  var inv=parseInt(document.getElementById('modalInvitados').value,10)||1;
  if(!nom){{alert('Escribe el nombre de la tarjeta');document.getElementById('modalNombre').focus();return}}
  DATA.unshift({{nombre:nom,invitados:inv}});
  saveData();
  cerrarModal();
  render(document.getElementById('searchInput').value);
}});

/* cerrar modal con Enter */
document.getElementById('modalInvitados').addEventListener('keydown',function(e){{
  if(e.key==='Enter')document.getElementById('modalSave').click();
}});
document.getElementById('modalNombre').addEventListener('keydown',function(e){{
  if(e.key==='Enter')document.getElementById('modalInvitados').focus();
}});

/* exportar */
document.getElementById('exportBtn').addEventListener('click',function(){{
  var q=document.getElementById('searchInput').value.toLowerCase().trim();
  var txt='LISTA DE INVITADOS - XV Mar\\u00eda Jos\\u00e9\\n';
  txt+='================================\\n\\n';
  DATA.forEach(function(d,i){{
    var match=!q||d.nombre.toLowerCase().indexOf(q)!==-1;
    if(!match)return;
    var url=BASE+'/?nombre='+encodeURIComponent(d.nombre)+'&invitados='+d.invitados;
    txt+=d.invitados+' inv. - '+d.nombre+'\\n'+url+'\\n\\n';
  }});
  var ta=document.createElement('textarea');
  ta.value=txt;
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  alert('Lista copiada al portapapeles');
}});

/* render inicial */
render('');
</script>
</body>
</html>"""

with open(r"C:\Users\SebasDev\Desktop\Tarjeta Majo\links_invitacion.html", "w", encoding="utf-8") as f:
    f.write(html)

total_invitados = sum(l["invitados"] for l in links)
print(f"OK - {len(links)} tarjetas, {total_invitados} invitados")
print("links_invitacion.html generado con buscador y creador de tarjetas")
