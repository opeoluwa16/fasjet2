import json

with open('/home/claude/fasjet-classic/images_b64.json') as f:
    IMG = json.load(f)

NAV = '''<header>
  <div class="container nav-row">
    <a href="index.html" class="nav-logo"><span class="bolt">&#9889;</span>FASJET SOLUTIONS</a>
    <nav class="nav-links">
      {links}
    </nav>
    <div class="nav-call">
      <a href="tel:+2348062220222" class="phone-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.362 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
        0806 222 0222
      </a>
    </div>
    <button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <div class="container mobile-menu" id="mobileMenu">
    {mlinks}
    <a href="tel:+2348062220222">Call 0806 222 0222</a>
  </div>
</header>'''

def nav(active):
    pages = [('index.html','Home','home'),('about.html','About','about'),('services.html','Services','services'),
             ('projects.html','Projects','projects'),('contact.html','Contact','contact')]
    links = '\n      '.join(f'<a href="{h}"{" class=\"active\"" if k==active else ""}>{l}</a>' for h,l,k in pages)
    mlinks = '\n    '.join(f'<a href="{h}">{l}</a>' for h,l,k in pages)
    return NAV.format(links=links, mlinks=mlinks)

FOOTER = '''<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><span class="bolt">&#9889;</span>FASJET SOLUTIONS</div>
        <p style="font-size:14px; line-height:1.7; max-width:34ch;">Industrial electrical works and network infrastructure for refineries, power plants, and heavy industry across Nigeria.</p>
      </div>
      <div class="footer-col">
        <h4>Navigate</h4>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="projects.html">Projects</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Get in touch</h4>
        <a href="tel:+2348062220222">0806 222 0222</a>
        <a href="https://wa.me/2348062220222" target="_blank" rel="noopener">WhatsApp us</a>
        <a href="mailto:fasjetsolutions@gmail.com">fasjetsolutions@gmail.com</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Fasjet Solutions. All rights reserved.</span>
      <span>Refineries &middot; Power Plants &middot; Heavy Industry &middot; Telecom &amp; Network Infrastructure</span>
    </div>
  </div>
</footer>'''

BASE_CSS = '''
:root{
  --bg:#080b12; --bg-alt:#0d121c; --navy-deep:#0a1420;
  --orange:#ff6b35; --orange-deep:#e8541c; --cyan:#5ac8ff;
  --white:#ffffff; --text-soft:#9fb0c3; --text-softer:#6d7d90;
  --glass:rgba(255,255,255,0.03); --glass-line:rgba(255,255,255,0.09); --glass-hover:rgba(255,107,53,0.5);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif; color:var(--text-soft); background:var(--bg); overflow-x:hidden; -webkit-font-smoothing:antialiased;}
img{max-width:100%; display:block;}
a{color:inherit; text-decoration:none;}
h1,h2,h3,h4{font-family:'Archivo',sans-serif; font-weight:800; line-height:1.08; letter-spacing:-0.01em; color:var(--white);}
.container{max-width:1180px; margin:0 auto; padding:0 24px;}
section{padding:90px 0; position:relative;}
@media(max-width:760px){ section{padding:56px 0;} }

.btn{display:inline-flex; align-items:center; gap:10px; padding:15px 28px; border-radius:6px; font-weight:700; font-size:14px; transition:transform 0.25s ease, background 0.25s ease, border-color 0.25s ease;}
.btn-orange{background:var(--orange); color:#0a0d12;}
.btn-orange:hover{background:var(--orange-deep); transform:translateY(-2px);}
.btn-ghost{background:transparent; color:var(--white); border:2px solid rgba(255,255,255,0.18);}
.btn-ghost:hover{border-color:var(--orange); color:var(--orange);}

/* nav */
header{position:sticky; top:0; z-index:100; background:var(--navy-deep); border-bottom:1px solid rgba(255,255,255,0.08);}
.nav-row{display:flex; align-items:center; justify-content:space-between; padding:16px 0;}
.nav-logo{display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:800; font-size:18px; color:#fff;}
.nav-logo .bolt{color:var(--orange); font-size:22px;}
.nav-links{display:flex; align-items:center; gap:32px;}
.nav-links a{color:rgba(255,255,255,0.78); font-size:14.5px; font-weight:600; transition:color 0.2s ease;}
.nav-links a:hover, .nav-links a.active{color:var(--orange);}
.nav-call .phone-btn{background:var(--orange); color:#0a0d12; padding:11px 20px; border-radius:6px; font-weight:700; font-size:14px; display:flex; align-items:center; gap:8px;}
.nav-toggle{display:none; flex-direction:column; gap:5px; cursor:pointer; background:none; border:none; padding:6px;}
.nav-toggle span{width:24px; height:2px; background:#fff;}
.mobile-menu{display:none; flex-direction:column; gap:4px; padding:12px 0 20px;}
.mobile-menu a{color:rgba(255,255,255,0.85); font-size:15px; font-weight:600; padding:10px 0; border-top:1px solid rgba(255,255,255,0.08);}
@media(max-width:900px){ .nav-links,.nav-call{display:none;} .nav-toggle{display:flex;} .mobile-menu.open{display:flex;} }

/* footer */
footer{background:var(--navy-deep); color:rgba(255,255,255,0.6); padding:56px 0 28px;}
.footer-grid{display:grid; grid-template-columns:1.4fr 1fr 1fr; gap:40px; padding-bottom:36px; border-bottom:1px solid rgba(255,255,255,0.08);}
@media(max-width:760px){ .footer-grid{grid-template-columns:1fr; gap:28px;} }
.footer-logo{display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:800; font-size:18px; color:#fff; margin-bottom:14px;}
.footer-logo .bolt{color:var(--orange);}
.footer-col h4{color:#fff; font-size:13.5px; letter-spacing:0.05em; text-transform:uppercase; margin-bottom:16px;}
.footer-col a{display:block; font-size:14px; padding:6px 0; color:rgba(255,255,255,0.6); transition:color 0.2s ease;}
.footer-col a:hover{color:var(--orange);}
.footer-bottom{display:flex; justify-content:space-between; padding-top:22px; font-size:13px; flex-wrap:wrap; gap:10px;}

/* background fx */
.fx-glow-a{position:absolute; width:560px; height:560px; border-radius:50%; pointer-events:none; background:radial-gradient(circle, rgba(255,107,53,0.14), transparent 70%);}
.fx-glow-b{position:absolute; width:480px; height:480px; border-radius:50%; pointer-events:none; background:radial-gradient(circle, rgba(90,200,255,0.09), transparent 70%);}
.fx-dot{position:absolute; border-radius:50%; pointer-events:none; animation:fxPulse 3.2s ease-in-out infinite;}
@keyframes fxPulse{0%,100%{opacity:0.25; transform:scale(1);} 50%{opacity:0.9; transform:scale(1.4);}}
.fx-alt{background:var(--bg-alt);}

/* reveal system */
.eyebrow2{
  display:flex; align-items:center; gap:14px; font-size:12.5px; font-weight:700;
  letter-spacing:0.16em; color:var(--orange); margin-bottom:18px; text-transform:uppercase;
  opacity:0; transform:translateY(16px); transition:opacity 0.7s ease, transform 0.7s ease;
}
.eyebrow2::after{content:""; width:46px; height:2px; background:linear-gradient(90deg,var(--orange),transparent);}
.reveal.is-in .eyebrow2{opacity:1; transform:translateY(0);}
.rv-head h1, .rv-head h2{opacity:0; transform:translateY(20px); transition:opacity 0.8s ease 0.1s, transform 0.8s ease 0.1s;}
.reveal.is-in .rv-head h1, .reveal.is-in .rv-head h2{opacity:1; transform:translateY(0);}
.rv-head p{opacity:0; transform:translateY(16px); transition:opacity 0.8s ease 0.2s, transform 0.8s ease 0.2s; color:var(--text-soft); margin-top:16px; font-size:15.5px; line-height:1.7;}
.reveal.is-in .rv-head p{opacity:1; transform:translateY(0);}
.accent{color:var(--orange);}

.glass-card{
  position:relative; border-radius:14px; background:var(--glass); border:1px solid var(--glass-line);
  box-shadow:0 1px 2px rgba(0,0,0,0.3), 0 14px 30px rgba(0,0,0,0.3);
  opacity:0; transform:translateY(26px);
  transition:opacity 0.7s ease, transform 0.7s ease, border-color 0.35s ease, box-shadow 0.35s ease;
}
.glass-card.is-in{opacity:1; transform:translateY(0);}
.glass-card:hover{transform:translateY(-6px); border-color:var(--glass-hover); box-shadow:0 1px 2px rgba(0,0,0,0.35), 0 18px 40px rgba(0,0,0,0.4), 0 0 30px rgba(255,107,53,0.16);}

.icon-glass{padding:34px 26px;}
.icon-glass .ic{width:38px; height:38px; margin-bottom:18px; color:var(--orange);}
.icon-glass h3{color:#fff; font-size:16.5px; margin-bottom:10px;}
.icon-glass p{color:var(--text-soft); font-size:13.5px; line-height:1.6;}
.icon-glass .arrow-dot{
  position:absolute; right:18px; bottom:18px; width:30px; height:30px; border-radius:50%;
  background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.14);
  display:flex; align-items:center; justify-content:center; transition:background 0.3s ease, border-color 0.3s ease, transform 0.3s ease;
}
.glass-card:hover .arrow-dot{background:var(--orange); border-color:var(--orange); transform:rotate(45deg);}
.icon-glass .arrow-dot svg{width:13px; height:13px; color:#fff;}

.card-grid2{display:grid; grid-template-columns:repeat(3,1fr); gap:22px; margin-top:0;}
@media(max-width:900px){ .card-grid2{grid-template-columns:repeat(2,1fr);} }
@media(max-width:600px){ .card-grid2{grid-template-columns:1fr;} }

/* photo split */
.split2{display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center;}
@media(max-width:900px){ .split2{grid-template-columns:1fr;} }
.split2-photo{
  position:relative; border-radius:14px; overflow:hidden; aspect-ratio:4/3.3;
  border:1px solid var(--glass-line); box-shadow:0 1px 2px rgba(0,0,0,0.3), 0 20px 44px rgba(0,0,0,0.4);
  opacity:0; transform:translateY(24px); transition:opacity 0.8s ease, transform 0.8s ease;
}
.reveal.is-in .split2-photo{opacity:1; transform:translateY(0);}
.split2-photo img{width:100%; height:100%; object-fit:cover; filter:saturate(0.9) brightness(0.85);}
.checklist2{display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:26px 0;}
@media(max-width:560px){ .checklist2{grid-template-columns:1fr;} }
.checklist2 li{list-style:none; display:flex; align-items:flex-start; gap:10px; font-size:14px; color:#dbe4ee; font-weight:600;}
.checklist2 svg{width:18px; height:18px; flex-shrink:0; margin-top:2px; color:var(--orange);}

/* page banner */
.pbanner{background:var(--bg); padding:70px 0 60px; text-align:left; overflow:hidden;}
.pbanner .container{position:relative; z-index:2;}
.pbanner h1{font-size:clamp(2rem,4vw,3rem);}
.pbanner p{color:var(--text-soft); margin-top:12px; font-size:15px;}

/* cta banner */
.cta2{background:var(--bg-alt); text-align:center; overflow:hidden;}
.cta2 h2{font-size:clamp(1.7rem,3vw,2.4rem); margin-bottom:14px;}
.cta2 p{color:var(--text-soft); margin-bottom:26px; font-size:15.5px;}

/* contact */
.contact-grid2{display:grid; grid-template-columns:1fr 1.2fr; gap:40px; margin-top:0;}
@media(max-width:900px){ .contact-grid2{grid-template-columns:1fr;} }
.contact-info2{padding:34px 30px;}
.contact-info2 h3{font-size:17px; margin-bottom:20px;}
.contact-row2{display:flex; align-items:flex-start; gap:14px; padding:15px 0; border-top:1px solid rgba(255,255,255,0.08);}
.contact-row2:first-of-type{border-top:none;}
.contact-row2 .ic{width:19px; height:19px; color:var(--orange); flex-shrink:0; margin-top:2px;}
.contact-row2 .label{font-size:11px; text-transform:uppercase; letter-spacing:0.08em; color:var(--text-softer);}
.contact-row2 .val{font-size:14.5px; font-weight:700; margin-top:2px; color:#fff;}
.contact-form2{padding:32px;}
.form-row3{display:flex; gap:14px; flex-wrap:wrap;}
.contact-form2 input, .contact-form2 textarea{
  flex:1 1 220px; background:rgba(255,255,255,0.03); border:1px solid var(--glass-line); border-radius:8px;
  padding:13px 15px; font-family:'Inter',sans-serif; font-size:14px; color:#fff; outline:none; resize:vertical;
  transition:border-color 0.2s ease;
}
.contact-form2 input::placeholder, .contact-form2 textarea::placeholder{color:var(--text-softer);}
.contact-form2 input:focus, .contact-form2 textarea:focus{border-color:var(--orange);}
.contact-form2 form{display:flex; flex-direction:column; gap:14px; margin-top:16px;}
.contact-form2 button{align-self:flex-start; border:none; cursor:pointer; font-family:'Inter',sans-serif;}

/* hero */
.hero2{padding:90px 0 100px;}
.hero2 .split2{align-items:center;}
.hero2 h1{font-size:clamp(2.2rem,4.4vw,3.5rem);}
.hero2-badge{
  position:absolute; bottom:18px; left:18px; z-index:3; background:rgba(8,11,18,0.75); backdrop-filter:blur(6px);
  border:1px solid var(--glass-hover); padding:14px 18px; border-radius:10px;
}
.hero2-badge strong{display:block; font-size:20px; color:#fff; font-family:'Archivo',sans-serif;}
.hero2-badge span{font-size:11.5px; color:var(--text-soft);}
'''

CIRCUIT_SVG = '''<svg class="fx-circuit" viewBox="0 0 1200 700" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute; inset:0; opacity:0.12; pointer-events:none;">
  <g stroke="#ff6b35" stroke-width="1" fill="none">
    <path d="M0 120 H260 L300 160 H520"/>
    <path d="M0 480 H180 L220 440 H460 L500 480 H760"/>
    <circle cx="300" cy="160" r="3" fill="#ff6b35" stroke="none"/>
    <circle cx="520" cy="160" r="3" fill="#ff6b35" stroke="none"/>
  </g>
  <g stroke="#5ac8ff" stroke-width="1" fill="none">
    <path d="M1200 90 H940 L900 130 H700"/>
    <path d="M1200 560 H1000 L960 600 H820 L780 560 H620"/>
    <circle cx="940" cy="90" r="3" fill="#5ac8ff" stroke="none"/>
  </g>
</svg>'''

def fx_layer(glow_a_pos, glow_b_pos, dots):
    dots_html = ''.join(
        f'<div class="fx-dot" style="width:{s}px;height:{s}px;{p}background:{c};animation-delay:{d}s;"></div>'
        for s,p,c,d in dots
    )
    return f'''<div class="fx-glow-a" style="{glow_a_pos}"></div>
  <div class="fx-glow-b" style="{glow_b_pos}"></div>
  {CIRCUIT_SVG}
  {dots_html}'''

REVEAL_SCRIPT = '''
(function(){
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('mobileMenu');
  if(toggle && menu){ toggle.addEventListener('click', function(){ menu.classList.toggle('open'); }); }

  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      }
    });
  }, {threshold:0.18});

  document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });

  document.querySelectorAll('.stagger').forEach(function(group){
    var items = group.querySelectorAll('.glass-card');
    items.forEach(function(item, i){
      item.style.transitionDelay = (i * 0.09) + 's';
      io.observe(item);
    });
  });

  var form = document.getElementById('contact-form');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var name = document.getElementById('cf-name').value;
      var email = document.getElementById('cf-email').value;
      var message = document.getElementById('cf-message').value;
      var subject = encodeURIComponent('Website Enquiry from ' + name);
      var body = encodeURIComponent(message + '\\n\\nFrom: ' + name + ' (' + email + ')');
      var url = 'https://mail.google.com/mail/?view=cm&fs=1&to=fasjetsolutions@gmail.com&su=' + subject + '&body=' + body;
      window.open(url, '_blank');
    });
  }
})();
'''

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="{IMG['images/favicon-32.png']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{BASE_CSS}
</style>
</head>
<body>
'''

def tail():
    return f'<script>{REVEAL_SCRIPT}</script>\n</body>\n</html>'

print("shared module ready")