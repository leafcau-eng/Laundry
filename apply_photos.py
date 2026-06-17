import re

path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = []

old = """.disc-badge { position:absolute; top:14px; right:14px; background:var(--accent); color:white; font-size:10px; font-weight:700; padding:3px 8px; border-radius:100px; }"""
new = old + """

/* PHOTO PLACEHOLDER */
.photo-placeholder { background:repeating-linear-gradient(45deg,rgba(26,58,143,0.04) 0,rgba(26,58,143,0.04) 10px,transparent 10px,transparent 20px); border:2px dashed rgba(26,58,143,0.3); border-radius:var(--radius); display:flex; align-items:center; justify-content:center; text-align:center; }
.photo-ph-inner { display:flex; flex-direction:column; align-items:center; gap:4px; padding:16px; }
.photo-ph-icon { font-size:28px; opacity:0.5; }
.photo-ph-text { font-size:13px; font-weight:700; color:var(--ink-muted); }
.photo-ph-size { font-size:11px; color:var(--ink-muted); opacity:0.7; }
.photo-hero { width:100%; aspect-ratio:4/3; margin-bottom:18px; }
.photo-keunggulan { width:100%; aspect-ratio:21/9; margin-bottom:20px; }
.lokasi-foto-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:20px; }
.photo-lokasi { aspect-ratio:4/3; }
@media (max-width:640px){ .lokasi-foto-grid{ grid-template-columns:1fr; } }
.photo-thumb { width:100%; aspect-ratio:1/1; margin-bottom:10px; }
.photo-thumb .photo-ph-icon { font-size:20px; }
.photo-thumb .photo-ph-text { font-size:10px; }
.photo-thumb .photo-ph-inner { padding:8px; }"""
replacements.append((old, new))

old = """    <div class="hero-right fu2">
      <div class="hero-card">"""
new = """    <div class="hero-right fu2">
      <div class="photo-placeholder photo-hero">
        <div class="photo-ph-inner">
          <span class="photo-ph-icon">📷</span>
          <span class="photo-ph-text">Upload Foto Disini</span>
          <span class="photo-ph-size">Foto Before-After / Tim Kerja · 1200×900px · WebP · max 400KB</span>
        </div>
      </div>
      <div class="hero-card">"""
replacements.append((old, new))

old = """    <div class="sec-title">Kenapa Pilih Kami?</div>
    <div class="ung-grid" id="ung-grid"></div>"""
new = """    <div class="sec-title">Kenapa Pilih Kami?</div>
    <div class="photo-placeholder photo-keunggulan">
      <div class="photo-ph-inner">
        <span class="photo-ph-icon">📷</span>
        <span class="photo-ph-text">Upload Foto Disini</span>
        <span class="photo-ph-size">Foto Mesin Laundry / Workshop · 1600×700px · WebP · max 400KB</span>
      </div>
    </div>
    <div class="ung-grid" id="ung-grid"></div>"""
replacements.append((old, new))

old = """    <div class="sec-title">Temukan Kami</div>
    <div class="kontak-grid" id="kontak-grid"></div>"""
new = """    <div class="sec-title">Temukan Kami</div>
    <div class="lokasi-foto-grid">
      <div class="photo-placeholder photo-lokasi">
        <div class="photo-ph-inner">
          <span class="photo-ph-icon">📷</span>
          <span class="photo-ph-text">Upload Foto Disini</span>
          <span class="photo-ph-size">Tampak Depan Toko · 800×600px</span>
        </div>
      </div>
      <div class="photo-placeholder photo-lokasi">
        <div class="photo-ph-inner">
          <span class="photo-ph-icon">📷</span>
          <span class="photo-ph-text">Upload Foto Disini</span>
          <span class="photo-ph-size">Suasana Dalam / Area Penerimaan · 800×600px</span>
        </div>
      </div>
    </div>
    <div class="kontak-grid" id="kontak-grid"></div>"""
replacements.append((old, new))

old = 'nama:"Karpet Permadani",  harga:15000,  unit:"m²",    diskon:true,  special:false },'
new = 'nama:"Karpet Permadani",  harga:15000,  unit:"m²",    diskon:true,  special:false, foto:true },'
replacements.append((old, new))

old = 'nama:"Sofa Ruang Tamu",  harga:60000,  unit:"unit",  diskon:false, special:false },'
new = 'nama:"Sofa Ruang Tamu",  harga:60000,  unit:"unit",  diskon:false, special:false, foto:true },'
replacements.append((old, new))

old = 'nama:"Cuci Springbed",   harga:85000,  unit:"meter", diskon:false, special:false },'
new = 'nama:"Cuci Springbed",   harga:85000,  unit:"meter", diskon:false, special:false, foto:true },'
replacements.append((old, new))

old = """q('price-grid').innerHTML = CONFIG.layanan.map(l => `
  <div class="price-card">
    ${l.diskon ? '<div class="disc-badge">-20%</div>' : ''}
    <div class="price-icon">${l.icon}</div>
    <div class="price-name">${l.nama}</div>"""
new = """q('price-grid').innerHTML = CONFIG.layanan.map(l => `
  <div class="price-card">
    ${l.diskon ? '<div class="disc-badge">-20%</div>' : ''}
    ${l.foto
      ? `<div class="photo-placeholder photo-thumb"><div class="photo-ph-inner"><span class="photo-ph-icon">📷</span><span class="photo-ph-text">Foto Hasil</span></div></div>`
      : `<div class="price-icon">${l.icon}</div>`
    }
    <div class="price-name">${l.nama}</div>"""
replacements.append((old, new))

for i, (old, new) in enumerate(replacements, 1):
    if old not in html:
        raise SystemExit(f"ANCHOR #{i} TIDAK DITEMUKAN")
    if html.count(old) > 1:
        raise SystemExit(f"ANCHOR #{i} GANDA")
    html = html.replace(old, new)
    print(f"Patch #{i} OK")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Semua placeholder foto berhasil ditambahkan")
