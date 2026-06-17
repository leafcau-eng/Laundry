import re

path = "index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

css_anchor = """.disc-badge { position:absolute; top:14px; right:14px; background:var(--accent); color:white; font-size:10px; font-weight:700; padding:3px 8px; border-radius:100px; }"""

css_new = css_anchor + """

/* BEFORE AFTER SLIDER */
.before-after{
  position:relative;
  width:100%;
  aspect-ratio:4/3;
  overflow:hidden;
  border-radius:var(--radius);
  margin-bottom:18px;
  box-shadow:var(--shadow);
}

.before-after img{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  object-fit:cover;
  pointer-events:none;
}

.before-img{
  z-index:1;
}

.after-wrap{
  position:absolute;
  inset:0;
  width:50%;
  overflow:hidden;
  z-index:2;
}

.after-img{
  width:100%;
}

.slider-line{
  position:absolute;
  top:0;
  bottom:0;
  left:50%;
  width:3px;
  background:#fff;
  transform:translateX(-50%);
  z-index:3;
}

.slider-handle{
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  width:46px;
  height:46px;
  border-radius:50%;
  background:#fff;
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow:0 4px 20px rgba(0,0,0,.2);
  z-index:4;
  font-size:18px;
}

.ba-label{
  position:absolute;
  bottom:16px;
  padding:6px 14px;
  border-radius:999px;
  background:rgba(0,0,0,.6);
  color:#fff;
  font-size:12px;
  font-weight:700;
  z-index:4;
}

.ba-before{ left:16px; }
.ba-after{ right:16px; }

.ba-range{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  opacity:0;
  cursor:ew-resize;
  z-index:5;
}
"""

if css_anchor not in html:
    raise SystemExit("CSS anchor tidak ditemukan")

html = html.replace(css_anchor, css_new)

old = """    <div class="hero-right fu2">
      <img src="https://i.ibb.co.com/4ZzXkDzV/1781702053284.png"
           class="photo-hero"
           style="object-fit:contain;border-radius:var(--radius);display:block;">
      <div class="hero-card">"""

new = """    <div class="hero-right fu2">

      <div class="before-after">
        <img src="images/karpet-before.webp" class="before-img" alt="Karpet sebelum dicuci">

        <div class="after-wrap">
          <img src="images/karpet-after.webp" class="after-img" alt="Karpet sesudah dicuci">
        </div>

        <div class="slider-line"></div>
        <div class="slider-handle">↔</div>

        <div class="ba-label ba-before">SEBELUM</div>
        <div class="ba-label ba-after">SESUDAH</div>

        <input type="range" class="ba-range" min="0" max="100" value="50">
      </div>

      <div class="hero-card">"""

if old not in html:
    raise SystemExit("Hero anchor tidak ditemukan")

html = html.replace(old, new)

script = """

document.querySelectorAll('.before-after').forEach(slider => {
  const range = slider.querySelector('.ba-range');
  const wrap = slider.querySelector('.after-wrap');
  const line = slider.querySelector('.slider-line');
  const handle = slider.querySelector('.slider-handle');

  function update() {
    const value = range.value + '%';
    wrap.style.width = value;
    line.style.left = value;
    handle.style.left = value;
  }

  range.addEventListener('input', update);
  update();
});
"""

if "</body>" not in html:
    raise SystemExit("Tag </body> tidak ditemukan")

html = html.replace("</body>", f"<script>{script}</script>\n</body>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Before-after slider berhasil dipasang")
