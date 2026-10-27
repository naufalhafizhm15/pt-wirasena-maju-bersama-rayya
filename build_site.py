#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static Site Generator for PT. Wirasena Maju Bersama Rayya
Design System: Google Stitch `taste-design` (Anti-Vibe-Coded Architectural B2B Standard)
- Fonts: Outfit (Display), Plus Jakarta Sans (Body), JetBrains Mono (Specs/Numbers)
- Palette: Canvas White (#F9FAFB), Pure Surface (#FFFFFF), Charcoal Ink (#18181B),
           Muted Steel (#71717A), Whisper Border (#E4E4E7), Wirasena Forest Accent (#2D7A3E)
- Hero: Asymmetric Split with Inline Image Typography, zero text-over-image overlap
- Layout: 1px structural Swiss grid, 2-column asymmetric zig-zag product showcase, border-top ledgers
- Strictly Banned: Emojis, Inter font, 3-column equal cards, neon glows, overlapping text, fake metrics
"""

import os

BASE_DIR = "/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya"


def render_head(title, description, keywords, canonical_file, extra_schema=""):
    canonical_url = (
        f"https://wirasenamajubersama.com/{canonical_file}"
        if canonical_file != "index.html"
        else "https://wirasenamajubersama.com/"
    )
    return f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="author" content="PT. Wirasena Maju Bersama Rayya" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <link rel="canonical" href="{canonical_url}" />

  <!-- Local SEO Geo Meta Tags Cikarang Selatan, Bekasi -->
  <meta name="geo.region" content="ID-JB" />
  <meta name="geo.placename" content="Cikarang Selatan, Kabupaten Bekasi, Jawa Barat" />
  <meta name="geo.position" content="-6.3425;107.1264" />
  <meta name="ICBM" content="-6.3425, 107.1264" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="id_ID" />
  <meta property="og:site_name" content="PT. Wirasena Maju Bersama Rayya" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="assets/social-media-kit/banner-facebook-cover.png?v=6" />

  <link rel="icon" type="image/png" href="assets/images/logo-avatar.png?v=6" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            display: ['Outfit', 'sans-serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          }},
          colors: {{
            canvas: '#F9FAFB',
            surface: '#FFFFFF',
            ink: '#18181B',
            steel: '#71717A',
            rule: '#E4E4E7',
            accent: '#2D7A3E',
            accentDark: '#236030'
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      background-color: #F9FAFB;
      color: #18181B;
    }}
    .spring-transition {{
      transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.35s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.25s ease, border-color 0.25s ease;
    }}
    .tactile-btn:active {{
      transform: translateY(-1px) scale(0.99);
    }}
    .inline-pill-img {{
      display: inline-block;
      vertical-align: middle;
      height: 0.82em;
      width: 1.65em;
      object-fit: cover;
      border-radius: 9999px;
      border: 1px solid #E4E4E7;
      margin: 0 0.12em;
    }}
    @media (max-width: 767px) {{
      .inline-pill-img {{
        height: 0.75em;
        width: 1.4em;
      }}
    }}
  </style>

  <!-- JSON-LD @graph Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": ["LocalBusiness", "Organization"],
        "@id": "https://wirasenamajubersama.com/#organization",
        "name": "PT. Wirasena Maju Bersama Rayya",
        "alternateName": [
          "Supplier Kebutuhan Pabrik Cikarang Bekasi",
          "Pabrik Carton Box & Impraboard Cikarang",
          "Supplier Electrical Mechanical Pabrik Bekasi"
        ],
        "url": "https://wirasenamajubersama.com",
        "logo": "https://wirasenamajubersama.com/assets/images/logo-trans.png",
        "description": "{description}",
        "telephone": "+62-21-84990200",
        "email": "marketing@wirasenamajubersama.com",
        "taxID": "96.434.539.2-447.000",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Jl. Bah Kilong Kp. Kandang, RT.004 RW.002, Desa Sukadami, Kec. Cikarang Selatan",
          "addressLocality": "Kabupaten Bekasi",
          "addressRegion": "Jawa Barat",
          "postalCode": "17530",
          "addressCountry": "ID"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": -6.3425,
          "longitude": 107.1264
        }},
        "areaServed": ["Cikarang Selatan", "Cikarang Pusat", "Cikarang Barat", "MM2100", "Jababeka", "EJIP", "Delta Silicon", "Lippo Cikarang", "Bekasi", "Karawang"]
      }}{extra_schema}
    ]
  }}
  </script>
</head>
"""


def render_navbar(active_page="index.html"):
    def nav_item(page, label):
        is_active = active_page == page
        cls = (
            "text-ink font-semibold border-b-2 border-accent pb-1"
            if is_active
            else "text-steel hover:text-ink spring-transition"
        )
        return f'<a href="{page}" class="{cls} text-sm">{label}</a>'

    return f"""<body class="bg-canvas text-ink font-sans antialiased selection:bg-accent selection:text-white overflow-x-hidden">

  <!-- Structural Sticky Navigation Bar (Stitch taste-design: 1px border, zero clutter) -->
  <header class="w-full sticky top-0 z-50 bg-surface/95 backdrop-blur-md border-b border-rule">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-8 h-20 flex items-center justify-between gap-6">
      
      <!-- Brand Identity -->
      <a href="index.html" class="flex items-center gap-3.5 shrink-0 group">
        <img src="assets/images/logo-trans.png?v=6" alt="PT. Wirasena Maju Bersama Rayya" class="h-11 w-auto object-contain" />
        <div class="border-l border-rule pl-3.5">
          <span class="font-display font-bold text-base sm:text-lg tracking-tight text-ink block leading-none">
            PT. Wirasena Maju Bersama Rayya
          </span>
          <span class="font-mono text-[11px] text-steel tracking-tight block mt-1">
            CIKARANG SELATAN, BEKASI &mdash; B2B SUPPLIER &amp; MANUFACTURING
          </span>
        </div>
      </a>

      <!-- Desktop Navigation -->
      <nav class="hidden lg:flex items-center gap-7">
        {nav_item("index.html", "Beranda")}
        {nav_item("supplier-electrical-mechanical.html", "Electrical & Mechanical")}
        {nav_item("pabrik-carton-box-impraboard.html", "Carton Box & Impraboard")}
        {nav_item("jasa-fabrikasi-trolley.html", "Fabrikasi Trolley")}
        {nav_item("artikel-seo.html", "Jurnal Teknis")}
        <a href="#kontak-rfq" class="text-steel hover:text-ink text-sm spring-transition">Kontak &amp; Email Divisi</a>
      </nav>

      <!-- Single Calibrated Primary Action + Search Trigger -->
      <div class="hidden sm:flex items-center gap-3 shrink-0">
        <button onclick="toggleSearchDrawer()" class="px-3.5 py-2 border border-rule bg-canvas hover:border-ink text-xs font-mono text-steel hover:text-ink rounded-[6px] flex items-center gap-2 spring-transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/>
          </svg>
          <span>Cari Part / Katalog</span>
        </button>
        <a href="#kontak-rfq" class="tactile-btn bg-accent hover:bg-accentDark text-white font-display font-semibold text-xs tracking-wide px-5 py-2.5 rounded-[6px] spring-transition">
          Kirim RFQ
        </a>
      </div>

      <!-- Mobile Menu Trigger -->
      <div class="flex items-center gap-2 lg:hidden">
        <button onclick="toggleSearchDrawer()" aria-label="Cari Katalog" class="p-2.5 border border-rule rounded-[6px] text-ink">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/>
          </svg>
        </button>
        <button onclick="document.getElementById('mobile-nav').classList.toggle('hidden')" aria-label="Menu Navigasi" class="p-2.5 border border-rule rounded-[6px] text-ink">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Collapse Menu -->
    <div id="mobile-nav" class="hidden lg:hidden bg-surface border-b border-rule px-6 py-5 space-y-3 text-sm">
      <a href="index.html" class="block py-1.5 font-semibold text-ink border-b border-rule">01 &mdash; Beranda Utama</a>
      <a href="supplier-electrical-mechanical.html" class="block py-1.5 text-steel hover:text-ink border-b border-rule">02 &mdash; Supplier Electrical, Mechanical &amp; Pneumatics</a>
      <a href="pabrik-carton-box-impraboard.html" class="block py-1.5 text-steel hover:text-ink border-b border-rule">03 &mdash; Pabrik Carton Box, Impraboard &amp; Rubber</a>
      <a href="jasa-fabrikasi-trolley.html" class="block py-1.5 text-steel hover:text-ink border-b border-rule">04 &mdash; Jasa Fabrikasi Storage Trolley &amp; Welding</a>
      <a href="artikel-seo.html" class="block py-1.5 text-steel hover:text-ink border-b border-rule">05 &mdash; Jurnal Teknis &amp; Panduan Pengadaan</a>
      <a href="#kontak-rfq" class="block py-1.5 font-semibold text-accent">06 &mdash; Kontak &amp; 4 Email Divisi</a>
    </div>
  </header>

  <!-- Quick Catalog Search Drawer -->
  <div id="search-drawer" class="hidden fixed inset-0 z-50 bg-ink/40 backdrop-blur-xs flex items-start justify-center pt-24 px-4">
    <div class="bg-surface w-full max-w-2xl border border-rule rounded-[8px] shadow-xl overflow-hidden">
      <div class="px-5 py-3.5 border-b border-rule flex items-center justify-between">
        <span class="font-mono text-xs uppercase text-steel">Pencarian Cepat Katalog Kebutuhan Pabrik</span>
        <button onclick="toggleSearchDrawer()" class="font-mono text-sm text-steel hover:text-ink px-2 py-0.5 border border-rule rounded-[4px]">ESC</button>
      </div>
      <div class="p-5">
        <label for="drawer-search-input" class="block text-xs font-medium text-ink mb-2">Nama Barang / Spesifikasi Teknis</label>
        <input id="drawer-search-input" type="text" oninput="filterDrawerItems(this.value)" placeholder="Ketik: sensor, plc, bearing, pneumatic, carton box, impraboard, trolley, majun..." class="w-full border border-rule bg-canvas px-4 py-3 text-sm rounded-[6px] focus:outline-none focus:border-accent" />
        <div class="mt-4 divide-y divide-rule max-h-72 overflow-y-auto">
          <a href="supplier-electrical-mechanical.html#electrical" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="electrical alat listrik plc sensor inverter vfd mcb contactor relay kabel panel">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-01</span>
              <span class="text-sm font-medium text-ink">Electrical &amp; Automation (PLC, Sensor, Inverter, MCB, Contactor)</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
          <a href="supplier-electrical-mechanical.html#mechanical" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="mechanical sparepart mesin bearing v-belt pulley gearbox dinamo roller conveyor cutting tools endmill">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-02</span>
              <span class="text-sm font-medium text-ink">Mechanical &amp; Cutting Tools (Bearing, Belt, Gearbox, Endmill)</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
          <a href="supplier-electrical-mechanical.html#pneumatics" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="pneumatic solenoid valve air cylinder fitting selang pu frl safety k3 sarung tangan kain majun cleaning">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-03</span>
              <span class="text-sm font-medium text-ink">Pneumatics, Safety K3 &amp; Factory Consumables (Valve, Cylinder, Majun)</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
          <a href="pabrik-carton-box-impraboard.html#carton-box" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="carton box kardus pabrik karton boks single double triple wall die cut b-flute c-flute">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-04</span>
              <span class="text-sm font-medium text-ink">Carton Box Custom &amp; Die-Cut Box (Single / Double / Triple Wall)</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
          <a href="pabrik-carton-box-impraboard.html#impraboard" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="impraboard box pp corrugated sekat partisi esd antistatic plastik hdpe ldpe pe foam rubber">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-05</span>
              <span class="text-sm font-medium text-ink">Box Impraboard Custom, Partisi ESD, Plastik HDPE/LDPE &amp; Rubber</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
          <a href="jasa-fabrikasi-trolley.html" class="drawer-item flex items-center justify-between py-3 px-2 hover:bg-canvas spring-transition" data-kw="fabrikasi storage trolley stainless besi rak pipa fifo meja kerja las welding pagar mesin">
            <div>
              <span class="font-mono text-[11px] text-accent mr-2">CAT-06</span>
              <span class="text-sm font-medium text-ink">Fabrikasi Storage Trolley Stainless/Besi, Rak FIFO &amp; Fence Welding</span>
            </div>
            <span class="font-mono text-xs text-steel">&rarr;</span>
          </a>
        </div>
      </div>
    </div>
  </div>
"""


def render_footer():
    return """
  <!-- CONTACT, RFQ & 4 OFFICIAL DIVISION EMAILS (Architectural Ledger) -->
  <section id="kontak-rfq" class="border-t border-rule bg-surface">
    <div class="max-w-[1360px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-rule">
      
      <!-- Left Column: Company Coordinates & 4 Official Division Emails -->
      <div class="lg:col-span-7 p-6 sm:p-12 border-b lg:border-b-0 lg:border-r border-rule">
        <div class="font-mono text-xs text-accent uppercase tracking-wider mb-3">
          DIRECT PROCUREMENT &amp; RFQ DESK
        </div>
        <h2 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight mb-4">
          Hubungi Divisi Terkait PT. Wirasena Maju Bersama Rayya
        </h2>
        <p class="text-steel text-sm leading-relaxed max-w-[62ch] mb-8">
          Untuk mempercepat proses penawaran harga (Request for Quotation), persetujuan spesifikasi kualitas (QC), maupun penjadwalan pengiriman ke kawasan industri Cikarang, Bekasi, dan Karawang, silakan hubungi alamat email resmi divisi kami di bawah ini.
        </p>

        <!-- 4 Division Emails Ledger (1px Structural Grid) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 border-t border-l border-rule mb-8">
          <a href="mailto:info@wirasenamajubersama.com" class="p-4 border-r border-b border-rule hover:bg-canvas spring-transition block">
            <span class="font-mono text-[11px] text-steel block mb-1">01 / ADMINISTRASI &amp; UMUM</span>
            <span class="font-mono text-xs sm:text-sm font-semibold text-ink">info@wirasenamajubersama.com</span>
          </a>
          <a href="mailto:marketing@wirasenamajubersama.com?subject=Request%20for%20Quotation%20(RFQ)%20-%20PT.%20Wirasena%20Maju%20Bersama%20Rayya" class="p-4 border-r border-b border-rule hover:bg-canvas spring-transition block">
            <span class="font-mono text-[11px] text-accent font-semibold block mb-1">02 / PENAWARAN HARGA (RFQ)</span>
            <span class="font-mono text-xs sm:text-sm font-semibold text-ink">marketing@wirasenamajubersama.com</span>
          </a>
          <a href="mailto:quality@wirasenamajubersama.com" class="p-4 border-r border-b border-rule hover:bg-canvas spring-transition block">
            <span class="font-mono text-[11px] text-steel block mb-1">03 / QUALITY CONTROL (QC/QA)</span>
            <span class="font-mono text-xs sm:text-sm font-semibold text-ink">quality@wirasenamajubersama.com</span>
          </a>
          <a href="mailto:delivery@wirasenamajubersama.com" class="p-4 border-r border-b border-rule hover:bg-canvas spring-transition block">
            <span class="font-mono text-[11px] text-steel block mb-1">04 / LOGISTIK &amp; PENGIRIMAN</span>
            <span class="font-mono text-xs sm:text-sm font-semibold text-ink">delivery@wirasenamajubersama.com</span>
          </a>
        </div>

        <!-- Address & Legal Metadata -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 pt-4 border-t border-rule text-xs">
          <div>
            <span class="font-mono text-[11px] text-steel block mb-1">LOKASI PABRIK &amp; WORKSHOP</span>
            <p class="text-ink leading-relaxed">
              Jl. Bah Kilong Kp. Kandang, RT.004/RW.002, Sukadami, Cikarang Selatan, Kab. Bekasi, Jawa Barat 17530
            </p>
          </div>
          <div>
            <span class="font-mono text-[11px] text-steel block mb-1">TELEPON / FAX KANTOR</span>
            <a href="tel:02184990200" class="font-mono text-sm font-semibold text-ink hover:text-accent">(021) 8499 0200</a>
            <span class="block text-steel mt-1">Senin &ndash; Sabtu (Jam Operasional)</span>
          </div>
          <div>
            <span class="font-mono text-[11px] text-steel block mb-1">IDENTITAS PAJAK (PKP)</span>
            <span class="font-mono text-ink font-medium block">NPWP: 96.434.539.2-447.000</span>
            <span class="text-steel block mt-1">Cikarang Selatan, Bekasi</span>
          </div>
        </div>
      </div>

      <!-- Right Column: Quick RFQ Dispatch Form + Map -->
      <div class="lg:col-span-5 p-6 sm:p-12 bg-canvas flex flex-col justify-between">
        <div>
          <div class="font-mono text-xs text-steel uppercase mb-2">FAST RFQ DISPATCH</div>
          <h3 class="font-display text-xl font-bold text-ink mb-5">
            Kirim Daftar Kebutuhan Barang via WhatsApp Business
          </h3>
          <form onsubmit="submitRfqToWa(event)" class="space-y-4">
            <div>
              <label for="rfq-company" class="block text-xs font-medium text-ink mb-1.5">Nama Perusahaan / Pabrik</label>
              <input id="rfq-company" type="text" required placeholder="Contoh: PT. Maju Manufaktur Indonesia" class="w-full bg-surface border border-rule rounded-[6px] px-3.5 py-2.5 text-sm focus:outline-none focus:border-accent" />
            </div>
            <div>
              <label for="rfq-category" class="block text-xs font-medium text-ink mb-1.5">Kategori Pengadaan</label>
              <select id="rfq-category" class="w-full bg-surface border border-rule rounded-[6px] px-3.5 py-2.5 text-sm focus:outline-none focus:border-accent">
                <option value="Electrical, Mechanical & Pneumatics">Electrical, Mechanical &amp; Pneumatics</option>
                <option value="Carton Box & Impraboard Custom">Carton Box &amp; Impraboard Custom</option>
                <option value="Fabrikasi Storage Trolley & Welding">Fabrikasi Storage Trolley &amp; Welding</option>
                <option value="Safety K3, Cleaning & Consumables">Safety K3, Cleaning &amp; Consumables</option>
              </select>
            </div>
            <div>
              <label for="rfq-items" class="block text-xs font-medium text-ink mb-1.5">Spesifikasi Barang / Ukuran / Qty</label>
              <textarea id="rfq-items" rows="3" required placeholder="Tulis nama part, ukuran LxWxH, atau spesifikasi yang dibutuhkan..." class="w-full bg-surface border border-rule rounded-[6px] px-3.5 py-2.5 text-sm focus:outline-none focus:border-accent"></textarea>
            </div>
            <button type="submit" class="tactile-btn w-full bg-accent hover:bg-accentDark text-white font-display font-semibold text-xs uppercase tracking-wider py-3.5 px-6 rounded-[6px] spring-transition">
              Kirim Permintaan Penawaran (WhatsApp Business)
            </button>
          </form>
        </div>

        <div class="mt-6 pt-6 border-t border-rule">
          <iframe
            title="Peta Lokasi PT. Wirasena Maju Bersama Rayya Cikarang Selatan"
            src="https://www.google.com/maps?q=-6.3425,107.1264&hl=id&z=14&output=embed"
            class="w-full h-44 border border-rule rounded-[6px]"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>

    </div>
  </section>

  <!-- ARCHITECTURAL FOOTER -->
  <footer class="border-t border-rule bg-ink text-white">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 pb-10 border-b border-white/15">
        <div class="md:col-span-5">
          <div class="flex items-center gap-3 mb-4">
            <img src="assets/images/logo-footer-white.png?v=6" alt="PT. Wirasena Maju Bersama Rayya" class="h-10 w-auto object-contain" />
            <span class="font-display font-bold text-lg tracking-tight">PT. Wirasena Maju Bersama Rayya</span>
          </div>
          <p class="text-xs text-zinc-400 leading-relaxed max-w-sm">
            Mitra manufaktur kemasan industri (Carton Box, Impraboard, Synthetic Rubber), Jasa Fabrikasi Trolley &amp; Konstruksi Las, serta General Supplier Electrical, Mechanical, Pneumatics &amp; Safety K3 di Cikarang Selatan, Kabupaten Bekasi.
          </p>
        </div>
        <div class="md:col-span-4">
          <span class="font-mono text-[11px] text-zinc-400 uppercase block mb-3">Halaman Spesifikasi Produk</span>
          <ul class="space-y-2 text-xs text-zinc-300">
            <li><a href="supplier-electrical-mechanical.html" class="hover:text-white">Supplier Electrical, Mechanical &amp; Pneumatics</a></li>
            <li><a href="pabrik-carton-box-impraboard.html" class="hover:text-white">Pabrik Carton Box, Impraboard &amp; Rubber</a></li>
            <li><a href="jasa-fabrikasi-trolley.html" class="hover:text-white">Jasa Fabrikasi Storage Trolley &amp; Welding</a></li>
            <li><a href="artikel-seo.html" class="hover:text-white">Jurnal Teknis &amp; Panduan Pengadaan Pabrik</a></li>
            <li><a href="social-preview.html" class="hover:text-white">Digital Presence &amp; Social Media Kit Preview</a></li>
          </ul>
        </div>
        <div class="md:col-span-3">
          <span class="font-mono text-[11px] text-zinc-400 uppercase block mb-3">Hubungi Kami</span>
          <p class="font-mono text-xs text-zinc-300">Telp/Fax: (021) 8499 0200</p>
          <p class="font-mono text-xs text-zinc-300 mt-1">marketing@wirasenamajubersama.com</p>
          <p class="text-xs text-zinc-400 mt-3">
            Kawasan Layanan: MM2100, Jababeka, EJIP, Hyundai, Delta Silicon, Lippo Cikarang, Bekasi &amp; Karawang.
          </p>
        </div>
      </div>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-zinc-400 font-mono">
        <span>&copy; 2026 PT. WIRASENA MAJU BERSAMA RAYYA. ALL RIGHTS RESERVED.</span>
        <span>NPWP: 96.434.539.2-447.000 &mdash; CIKARANG SELATAN, BEKASI 17530</span>
      </div>
    </div>
  </footer>

  <!-- Minimal Tactile WhatsApp Business Trigger (Bottom Right) -->
  <div class="fixed bottom-5 right-5 z-40">
    <a href="https://wa.me/622184990200?text=Halo%20Tim%20Marketing%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20minta%20penawaran%20harga%20(RFQ)%20kebutuhan%20pabrik:" target="_blank" rel="noopener" class="tactile-btn bg-ink hover:bg-accent text-white border border-white/15 shadow-lg px-4 py-3 rounded-[6px] flex items-center gap-2.5 spring-transition">
      <span class="w-2 h-2 rounded-full bg-[#25D366]"></span>
      <span class="font-mono text-xs font-medium">WhatsApp Business Desk</span>
    </a>
  </div>

  <script>
    function toggleSearchDrawer() {
      const el = document.getElementById('search-drawer');
      if (!el) return;
      el.classList.toggle('hidden');
      if (!el.classList.contains('hidden')) {
        setTimeout(() => {
          const inp = document.getElementById('drawer-search-input');
          if (inp) inp.focus();
        }, 50);
      }
    }

    function filterDrawerItems(q) {
      const query = (q || '').toLowerCase().trim();
      document.querySelectorAll('.drawer-item').forEach(row => {
        const kw = (row.getAttribute('data-kw') || '') + ' ' + row.innerText.toLowerCase();
        row.style.display = (!query || kw.includes(query)) ? 'flex' : 'none';
      });
    }

    function filterInlineMatrix(q, cat) {
      const query = (q !== null ? q : (document.getElementById('matrix-search')?.value || '')).toLowerCase().trim();
      const activeCat = cat || window.currentMatrixCat || 'all';
      window.currentMatrixCat = activeCat;

      document.querySelectorAll('.matrix-filter-btn').forEach(btn => {
        if (btn.getAttribute('data-cat') === activeCat) {
          btn.className = 'matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-ink text-white spring-transition';
        } else {
          btn.className = 'matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-surface border border-rule text-steel hover:text-ink spring-transition';
        }
      });

      document.querySelectorAll('.matrix-row').forEach(row => {
        const rowCat = row.getAttribute('data-cat');
        const rowText = (row.getAttribute('data-kw') || '') + ' ' + row.innerText.toLowerCase();
        const matchCat = (activeCat === 'all' || rowCat === activeCat);
        const matchQuery = (!query || rowText.includes(query));
        row.style.display = (matchCat && matchQuery) ? '' : 'none';
      });
    }

    function submitRfqToWa(e) {
      e.preventDefault();
      const comp = document.getElementById('rfq-company').value.trim();
      const cat = document.getElementById('rfq-category').value;
      const items = document.getElementById('rfq-items').value.trim();
      const msg = `Halo Tim Marketing PT. Wirasena Maju Bersama Rayya,\\n\\nKami dari *${comp}* ingin meminta penawaran harga (RFQ):\\n- Kategori: ${cat}\\n- Kebutuhan: ${items}\\n\\nMohon informasi harga dan estimasi pengirimannya. Terima kasih.`;
      window.open(`https://wa.me/622184990200?text=${encodeURIComponent(msg)}`, '_blank');
    }
  </script>
</body>
</html>
"""


def build_index_page():
    title = "Supplier Kebutuhan Pabrik Cikarang & Bekasi | PT. Wirasena Maju Bersama Rayya — Electrical, Mechanical, Carton Box & Fabrikasi"
    description = "PT. Wirasena Maju Bersama Rayya: General Supplier Kebutuhan Pabrik (Electrical, Mechanical, Pneumatics, Safety K3), Produsen Carton Box & Impraboard Custom, serta Jasa Fabrikasi Trolley di Cikarang Selatan, Bekasi."
    keywords = "supplier kebutuhan pabrik terdekat, general supplier pabrik cikarang bekasi, supplier alat listrik industri terdekat, supplier sparepart mesin pabrik, vendor mechanical electrical bekasi, pabrik carton box cikarang bekasi, supplier box impraboard custom, jasa fabrikasi trolley pabrik"

    body = """
  <!-- ASYMMETRIC SPLIT HERO WITH INLINE IMAGE TYPOGRAPHY (Stitch taste-design Section 4: Zero overlapping text!) -->
  <section class="border-b border-rule bg-surface">
    <div class="max-w-[1360px] mx-auto grid grid-cols-1 lg:grid-cols-12 border-x border-rule">
      
      <!-- Left 7 Columns: Editorial Headline with Inline Visual Punctuation -->
      <div class="lg:col-span-7 p-6 sm:p-12 lg:p-16 flex flex-col justify-between border-b lg:border-b-0 lg:border-r border-rule">
        <div>
          <div class="flex items-center gap-3 font-mono text-xs text-steel mb-6">
            <span class="text-accent font-semibold">CIK-BKS / ID-17530</span>
            <span>&mdash;</span>
            <span>GENERAL TRADING, PACKAGING &amp; METAL FABRICATION</span>
          </div>

          <h1 class="font-display font-bold text-ink tracking-tight leading-[1.14]" style="font-size: clamp(2rem, 3.8vw, 3.35rem);">
            Mitra Pengadaan Pabrik
            <img src="assets/images/trading-electrical-mechanical.png" alt="Electrical & Mechanical Supply" class="inline-pill-img" />
            Electrical &amp; Mechanical, Manufaktur
            <img src="assets/images/product-carton-box.png" alt="Carton Box Manufacturing" class="inline-pill-img" />
            Carton Box &amp; Impraboard, serta Fabrikasi
            <img src="assets/images/fabrication-trolley-stainless.png" alt="Storage Trolley Fabrication" class="inline-pill-img" />
            Trolley Industri di Cikarang.
          </h1>

          <p class="text-steel text-base leading-[1.75] max-w-[62ch] mt-6">
            PT. Wirasena Maju Bersama Rayya mendukung rantai pasok pabrik di Cikarang, Bekasi, dan Karawang melalui pengadaan suku cadang <strong>Electrical, Mechanical, Pneumatics &amp; Safety K3</strong>, produksi langsung <strong>Carton Box &amp; Box Impraboard Custom</strong> dengan 5 mesin in-house, serta bengkel <strong>Fabrikasi Trolley &amp; Konstruksi Las</strong>.
          </p>
        </div>

        <!-- Single Primary CTA + Direct Search Input -->
        <div class="mt-10 pt-8 border-t border-rule flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <a href="#kontak-rfq" class="tactile-btn bg-accent hover:bg-accentDark text-white font-display font-semibold text-sm px-7 py-3.5 rounded-[6px] text-center spring-transition">
            Minta Penawaran Harga (RFQ)
          </a>
          <a href="#katalog-spesifikasi" class="px-6 py-3.5 border border-rule bg-canvas hover:border-ink text-ink font-mono text-xs rounded-[6px] text-center spring-transition">
            Telusuri Matriks Spesifikasi &darr;
          </a>
        </div>
      </div>

      <!-- Right 5 Columns: Clean Spatial Visual & Specification Ledger (Zero Overlapping Text) -->
      <div class="lg:col-span-5 bg-canvas flex flex-col justify-between">
        <div class="p-6 sm:p-8 border-b border-rule bg-surface">
          <div class="flex items-center justify-between font-mono text-[11px] text-steel mb-3">
            <span>FACILITY &amp; PRODUCTION LINE</span>
            <span>SUKADAMI, CIKARANG SELATAN</span>
          </div>
          <div class="aspect-[16/10] overflow-hidden rounded-[6px] border border-rule bg-canvas">
            <img id="hero-showcase-img" src="assets/images/machine-1-cutting-creasing.png" alt="Fasilitas Produksi PT. Wirasena Maju Bersama Rayya" class="w-full h-full object-cover spring-transition" />
          </div>
          <div class="mt-3 flex items-center justify-between gap-2">
            <span id="hero-showcase-label" class="font-mono text-xs text-ink font-medium">
              01 / Mesin Produksi Carton Box &amp; Die-Cut In-House
            </span>
            <div class="flex items-center gap-1.5">
              <button onclick="setHeroPreview(0)" class="font-mono text-[11px] px-2 py-1 border border-rule bg-canvas hover:border-ink rounded-[4px]">01</button>
              <button onclick="setHeroPreview(1)" class="font-mono text-[11px] px-2 py-1 border border-rule bg-canvas hover:border-ink rounded-[4px]">02</button>
              <button onclick="setHeroPreview(2)" class="font-mono text-[11px] px-2 py-1 border border-rule bg-canvas hover:border-ink rounded-[4px]">03</button>
            </div>
          </div>
        </div>

        <!-- 3 Core Division Index Rows -->
        <div class="divide-y divide-rule">
          <a href="supplier-electrical-mechanical.html" class="p-5 sm:px-8 flex items-center justify-between hover:bg-surface spring-transition group">
            <div>
              <span class="font-mono text-[11px] text-accent block">DIV-01 / MRO &amp; GENERAL TRADING</span>
              <span class="font-display font-semibold text-sm text-ink group-hover:text-accent">Supplier Electrical, Mechanical, Pneumatics &amp; Safety K3</span>
            </div>
            <span class="font-mono text-xs text-steel group-hover:translate-x-1 spring-transition">&rarr;</span>
          </a>
          <a href="pabrik-carton-box-impraboard.html" class="p-5 sm:px-8 flex items-center justify-between hover:bg-surface spring-transition group">
            <div>
              <span class="font-mono text-[11px] text-accent block">DIV-02 / PACKAGING MANUFACTURING</span>
              <span class="font-display font-semibold text-sm text-ink group-hover:text-accent">Pabrik Carton Box Custom, Box Impraboard &amp; Synthetic Rubber</span>
            </div>
            <span class="font-mono text-xs text-steel group-hover:translate-x-1 spring-transition">&rarr;</span>
          </a>
          <a href="jasa-fabrikasi-trolley.html" class="p-5 sm:px-8 flex items-center justify-between hover:bg-surface spring-transition group">
            <div>
              <span class="font-mono text-[11px] text-accent block">DIV-03 / METAL FABRICATION</span>
              <span class="font-display font-semibold text-sm text-ink group-hover:text-accent">Jasa Fabrikasi Storage Trolley Stainless/Besi &amp; Welding</span>
            </div>
            <span class="font-mono text-xs text-steel group-hover:translate-x-1 spring-transition">&rarr;</span>
          </a>
        </div>
      </div>

    </div>
  </section>

  <script>
    const heroPreviews = [
      { img: 'assets/images/machine-1-cutting-creasing.png', label: '01 / Mesin Produksi Carton Box & Die-Cut In-House' },
      { img: 'assets/images/trading-tools.png', label: '02 / Pengadaan Sparepart Mechanical, Electrical & Workshop Tools' },
      { img: 'assets/images/fabrication-welding.png', label: '03 / Workshop Fabrikasi Trolley Stainless & Konstruksi Las' }
    ];
    function setHeroPreview(idx) {
      const item = heroPreviews[idx];
      if (!item) return;
      document.getElementById('hero-showcase-img').src = item.img;
      document.getElementById('hero-showcase-label').innerText = item.label;
    }
  </script>

  <!-- 2-COLUMN ASYMMETRIC ZIG-ZAG PRODUCT SHOWCASE (Stitch taste-design Section 6: No 3-column equal card grids!) -->
  <section class="border-b border-rule bg-canvas">
    <div class="max-w-[1360px] mx-auto border-x border-rule">
      
      <!-- Section Header -->
      <div class="p-6 sm:p-12 border-b border-rule bg-surface flex flex-col md:flex-row md:items-end justify-between gap-6">
        <div>
          <span class="font-mono text-xs text-accent uppercase block mb-2">CORE CAPABILITIES &amp; PRODUCT LINES</span>
          <h2 class="font-display text-2xl sm:text-4xl font-bold text-ink tracking-tight">
            Tiga Lini Utama Penunjang Operasional Pabrik
          </h2>
        </div>
        <p class="text-steel text-sm max-w-md leading-relaxed">
          Seluruh pengadaan barang dan produksi manufaktur dikerjakan sesuai spesifikasi gambar kerja (drawing) maupun part number yang diminta oleh tim Purchasing &amp; Engineering.
        </p>
      </div>

      <!-- Zig-Zag Row 01: Electrical, Mechanical & Pneumatics -->
      <div class="grid grid-cols-1 lg:grid-cols-12 border-b border-rule bg-surface">
        <div class="lg:col-span-5 p-6 sm:p-10 border-b lg:border-b-0 lg:border-r border-rule flex items-center justify-center bg-white">
          <img src="assets/images/studio-pneumatics.png?v=6" alt="Supplier Alat Listrik Industri, Mechanical & Pneumatics Cikarang" class="w-full max-h-[300px] object-contain" />
        </div>
        <div class="lg:col-span-7 p-6 sm:p-12 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-xs text-steel mb-4">
              <span class="text-accent font-semibold">LINE 01 — GENERAL TRADING &amp; MRO SUPPLY</span>
              <span>ALL ITEMS AS REQUESTED BY BUYER</span>
            </div>
            <h3 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight mb-4">
              Supplier Electrical, Mechanical, Komponen Pneumatics &amp; Safety K3
            </h3>
            <p class="text-steel text-sm leading-relaxed max-w-[62ch] mb-6">
              Menyuplai kebutuhan perawatan mesin pabrik (Maintenance, Repair &amp; Operations) dengan respons penawaran cepat untuk mengurangi potensi downtime produksi.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 border-t border-l border-rule text-xs">
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">ELECTRICAL &amp; AUTOMATION</span>
                <span class="text-steel mt-0.5 block">PLC, Sensor Proximity/Photoelectric, Inverter VFD, MCB, Contactor, Relay, Kabel Panel</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">MECHANICAL &amp; TRANSMISSION</span>
                <span class="text-steel mt-0.5 block">Bearing, V-Belt, Timing Belt, Pulley, Gearbox, Dinamo Motor, Roller Conveyor, Cutting Tools</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">PNEUMATIC SYSTEM</span>
                <span class="text-steel mt-0.5 block">Solenoid Valve, Air Cylinder, FRL Filter Regulator, Fitting One-Touch, Selang PU/Nylon</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">SAFETY K3 &amp; CONSUMABLES</span>
                <span class="text-steel mt-0.5 block">Sepatu &amp; Helm Safety, Sarung Tangan, Kain Majun Jahit, Cleaning Supplies, Pest Control, ATK</span>
              </div>
            </div>
          </div>
          <div class="mt-8 flex flex-wrap items-center gap-4">
            <a href="supplier-electrical-mechanical.html" class="tactile-btn bg-ink hover:bg-accent text-white font-display font-semibold text-xs px-6 py-3 rounded-[6px] spring-transition">
              Buka Katalog Electrical &amp; Mechanical &rarr;
            </a>
          </div>
        </div>
      </div>

      <!-- Zig-Zag Row 02 (Reversed Asymmetric): Carton Box, Impraboard & Rubber -->
      <div class="grid grid-cols-1 lg:grid-cols-12 border-b border-rule bg-surface">
        <div class="lg:col-span-7 p-6 sm:p-12 border-b lg:border-b-0 lg:border-r border-rule flex flex-col justify-between order-2 lg:order-1">
          <div>
            <div class="flex items-center justify-between font-mono text-xs text-steel mb-4">
              <span class="text-accent font-semibold">LINE 02 — IN-HOUSE PACKAGING MANUFACTURING</span>
              <span>5 PRODUCTION MACHINES</span>
            </div>
            <h3 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight mb-4">
              Pabrik Carton Box Custom, Box Impraboard, Plastik Industri &amp; Rubber
            </h3>
            <p class="text-steel text-sm leading-relaxed max-w-[62ch] mb-6">
              Diproduksi langsung di fasilitas kami menggunakan lini mesin Cutting &amp; Creasing, Automatic/Semi Folder Glue, Rotary Sloter, dan Rotary Die Cut untuk menjamin presisi ukuran dan ketepatan waktu pengiriman.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 border-t border-l border-rule text-xs">
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">CORRUGATED CARTON BOX</span>
                <span class="text-steel mt-0.5 block">Single Wall, Double Wall, Triple Wall (B/C/CB Flute), Die-Cut Box &amp; Safety Glass Box</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">IMPRABOARD &amp; PARTITION</span>
                <span class="text-steel mt-0.5 block">PP Corrugated Box Custom (2mm&ndash;6mm), Sekat Partisi Presisi, Layer Pad &amp; Box ESD Anti-Static</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">PLASTIC, FOAM &amp; TAPE</span>
                <span class="text-steel mt-0.5 block">Plastik HDPE, LDPE, Anti-Static Bag, Stretch Film, PE Foam, Protection Sheet, Masking Tape</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">TECHNICAL RUBBER &amp; GLASS</span>
                <span class="text-steel mt-0.5 block">Synthetic Rubber, Chloroprene Rubber, Rubber Molded, Rubber Foot, Tempered Glass</span>
              </div>
            </div>
          </div>
          <div class="mt-8 flex flex-wrap items-center gap-4">
            <a href="pabrik-carton-box-impraboard.html" class="tactile-btn bg-ink hover:bg-accent text-white font-display font-semibold text-xs px-6 py-3 rounded-[6px] spring-transition">
              Buka Spesifikasi Carton Box &amp; Impraboard &rarr;
            </a>
          </div>
        </div>
        <div class="lg:col-span-5 p-6 sm:p-10 flex items-center justify-center bg-white order-1 lg:order-2">
          <img src="assets/images/studio-impraboard.png?v=6" alt="Pabrik Carton Box & Box Impraboard Custom Cikarang" class="w-full max-h-[300px] object-contain" />
        </div>
      </div>

      <!-- Zig-Zag Row 03: Storage Trolley & Industrial Welding -->
      <div class="grid grid-cols-1 lg:grid-cols-12 bg-surface">
        <div class="lg:col-span-5 p-6 sm:p-10 border-b lg:border-b-0 lg:border-r border-rule flex items-center justify-center bg-white">
          <img src="assets/images/studio-trolley-fabrication.png?v=6" alt="Jasa Fabrikasi Storage Trolley Stainless & Besi Pabrik Bekasi" class="w-full max-h-[300px] object-contain" />
        </div>
        <div class="lg:col-span-7 p-6 sm:p-12 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-xs text-steel mb-4">
              <span class="text-accent font-semibold">LINE 03 — CUSTOM METAL FABRICATION</span>
              <span>STAINLESS SUS 304/201 &amp; CARBON STEEL</span>
            </div>
            <h3 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight mb-4">
              Jasa Fabrikasi Storage Trolley, Rak Pipa FIFO &amp; Konstruksi Las Industri
            </h3>
            <p class="text-steel text-sm leading-relaxed max-w-[62ch] mb-6">
              Pengerjaan fabrikasi logam presisi sesuai drawing teknik pabrik untuk kebutuhan material handling, perakitan (assembly), dan pagar pengaman mesin produksi.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 border-t border-l border-rule text-xs">
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">CUSTOM STORAGE TROLLEY</span>
                <span class="text-steel mt-0.5 block">Trolley Stainless Steel &amp; Besi Hollow Powder Coating dengan Roda Heavy-Duty Caster PU/Nylon</span>
              </div>
              <div class="p-3.5 border-r border-b border-rule">
                <span class="font-mono text-[11px] text-ink font-semibold block">FIFO RACK &amp; FENCE WELDING</span>
                <span class="text-steel mt-0.5 block">Rak Pipa FIFO Roller Track, Meja Kerja Produksi, Jigs, serta Pagar Pengaman Mesin (Fence Welding)</span>
              </div>
            </div>
          </div>
          <div class="mt-8 flex flex-wrap items-center gap-4">
            <a href="jasa-fabrikasi-trolley.html" class="tactile-btn bg-ink hover:bg-accent text-white font-display font-semibold text-xs px-6 py-3 rounded-[6px] spring-transition">
              Buka Layanan Fabrikasi Trolley &amp; Las &rarr;
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- INTERACTIVE SPECIFICATION MATRIX (Border-Top Architectural Table for Purchasing Buyers) -->
  <section id="katalog-spesifikasi" class="border-b border-rule bg-surface">
    <div class="max-w-[1360px] mx-auto border-x border-rule p-6 sm:p-12">
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-8 border-b border-rule">
        <div>
          <span class="font-mono text-xs text-accent uppercase block mb-2">PROCUREMENT SPECIFICATION INDEX</span>
          <h2 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight">
            Cari &amp; Filter Katalog Kebutuhan Pabrik
          </h2>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <input id="matrix-search" type="text" oninput="filterInlineMatrix(this.value, null)" placeholder="Ketik nama barang (misal: bearing, sensor, impraboard, trolley)..." class="w-full sm:w-72 border border-rule bg-canvas px-3.5 py-2 text-xs rounded-[6px] focus:outline-none focus:border-accent" />
          <div class="flex flex-wrap gap-1.5">
            <button onclick="filterInlineMatrix(null, 'all')" data-cat="all" class="matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-ink text-white spring-transition">SEMUA</button>
            <button onclick="filterInlineMatrix(null, 'me')" data-cat="me" class="matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-surface border border-rule text-steel hover:text-ink spring-transition">ELECTRICAL &amp; ME</button>
            <button onclick="filterInlineMatrix(null, 'pkg')" data-cat="pkg" class="matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-surface border border-rule text-steel hover:text-ink spring-transition">PACKAGING</button>
            <button onclick="filterInlineMatrix(null, 'fab')" data-cat="fab" class="matrix-filter-btn font-mono text-xs px-3.5 py-2 rounded-[6px] bg-surface border border-rule text-steel hover:text-ink spring-transition">FABRIKASI</button>
          </div>
        </div>
      </div>

      <!-- Border-Top Architectural Ledger Rows -->
      <div class="divide-y divide-rule">
        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="me" data-kw="electrical plc sensor proximity photoelectric inverter vfd mcb contactor relay kabel panel listrik industri">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-01 / ME</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Electrical &amp; Automation Parts</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">PLC, Sensor Photoelectric &amp; Proximity, Inverter VFD, Power Supply, MCB, MCCB, Magnetic Contactor, Relay, Kabel Kontrol &amp; Panel</div>
          <div class="md:col-span-2 md:text-right">
            <a href="supplier-electrical-mechanical.html#electrical" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>

        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="me" data-kw="mechanical sparepart mesin bearing v-belt pulley sprocket gearbox dinamo roller conveyor cutting tools endmill drill">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-02 / ME</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Mechanical &amp; Cutting Tools</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">Bearing (Ball/Roller/Linear), V-Belt, Timing Belt, Pulley, Gearbox, Dinamo Motor, Roller Conveyor, Endmill, Drill Bit, Insert Bubut</div>
          <div class="md:col-span-2 md:text-right">
            <a href="supplier-electrical-mechanical.html#mechanical" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>

        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="me" data-kw="pneumatic solenoid valve air cylinder fitting selang pu frl safety k3 apd sarung tangan kain majun cleaning">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-03 / ME</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Pneumatics, Safety K3 &amp; Majun</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">Solenoid Valve, Air Cylinder, Air Unit FRL, Fitting, Selang PU, Helm &amp; Sepatu Safety, Sarung Tangan, Kain Majun, Chemical &amp; Cleaning</div>
          <div class="md:col-span-2 md:text-right">
            <a href="supplier-electrical-mechanical.html#pneumatics" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>

        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="pkg" data-kw="carton box kardus pabrik karton boks single double triple wall die cut b-flute c-flute">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-04 / PKG</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Corrugated Carton Box Custom</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">Carton Box RSC, Overlap &amp; Die-Cut Custom (Single Wall, Double Wall, Triple Wall — B/C/E/CB Flute) &amp; Carton Box Safety Glass</div>
          <div class="md:col-span-2 md:text-right">
            <a href="pabrik-carton-box-impraboard.html#carton-box" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>

        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="pkg" data-kw="impraboard box pp corrugated sekat partisi esd antistatic plastik hdpe ldpe pe foam lakban masking tape rubber">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-05 / PKG</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Impraboard Box, Plastic &amp; Rubber</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">Box Impraboard &amp; Sekat Partisi Custom (Standar/ESD), Plastik HDPE/LDPE, PE Foam, Masking Tape, Synthetic &amp; Molded Rubber</div>
          <div class="md:col-span-2 md:text-right">
            <a href="pabrik-carton-box-impraboard.html#impraboard" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>

        <div class="matrix-row py-5 grid grid-cols-1 md:grid-cols-12 gap-4 items-center" data-cat="fab" data-kw="fabrikasi storage trolley stainless besi rak pipa fifo meja kerja las welding pagar mesin">
          <div class="md:col-span-2 font-mono text-xs text-accent">SPEC-06 / FAB</div>
          <div class="md:col-span-3 font-display font-bold text-base text-ink">Storage Trolley &amp; Metal Fabrication</div>
          <div class="md:col-span-5 text-xs text-steel leading-relaxed">Custom Storage Trolley (Stainless Steel SUS 304/201 &amp; Besi Hollow), Rak Pipa FIFO, Meja Kerja Produksi &amp; Fence Welding</div>
          <div class="md:col-span-2 md:text-right">
            <a href="jasa-fabrikasi-trolley.html" class="font-mono text-xs font-semibold text-ink hover:text-accent underline underline-offset-4">Spesifikasi &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- IN-HOUSE PRODUCTION MACHINERY & VERIFIED INDUSTRIAL CLIENTS -->
  <section class="border-b border-rule bg-canvas">
    <div class="max-w-[1360px] mx-auto border-x border-rule p-6 sm:p-12">
      <div class="mb-8">
        <span class="font-mono text-xs text-accent uppercase block mb-2">IN-HOUSE MANUFACTURING EQUIPMENT</span>
        <h2 class="font-display text-2xl sm:text-3xl font-bold text-ink tracking-tight">
          5 Lini Mesin Produksi Carton Box &amp; Kemasan Industri
        </h2>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 border-t border-l border-rule bg-surface mb-12">
        <div class="p-4 border-r border-b border-rule">
          <span class="font-mono text-[11px] text-steel block mb-2">M-01 / CUTTING</span>
          <img src="assets/images/machine-1-cutting-creasing.png" alt="Cutting and Creasing Machine" class="w-full h-36 object-cover rounded-[4px] border border-rule mb-3" />
          <h3 class="font-display font-bold text-sm text-ink">Cutting &amp; Creasing Machine</h3>
        </div>
        <div class="p-4 border-r border-b border-rule">
          <span class="font-mono text-[11px] text-steel block mb-2">M-02 / AUTO GLUE</span>
          <img src="assets/images/machine-2b-auto-folder-glue.png" alt="Automatic Folder Glue Machine" class="w-full h-36 object-cover rounded-[4px] border border-rule mb-3" />
          <h3 class="font-display font-bold text-sm text-ink">Automatic Folder Glue</h3>
        </div>
        <div class="p-4 border-r border-b border-rule">
          <span class="font-mono text-[11px] text-steel block mb-2">M-03 / SEMI GLUE</span>
          <img src="assets/images/machine-3-semi-folder-glue.png" alt="Semi Folder Glue Machine" class="w-full h-36 object-cover rounded-[4px] border border-rule mb-3" />
          <h3 class="font-display font-bold text-sm text-ink">Semi Folder Glue</h3>
        </div>
        <div class="p-4 border-r border-b border-rule">
          <span class="font-mono text-[11px] text-steel block mb-2">M-04 / SLOTER</span>
          <img src="assets/images/machine-4-rotary-sloter.png" alt="Rotary Sloter Machine" class="w-full h-36 object-cover rounded-[4px] border border-rule mb-3" />
          <h3 class="font-display font-bold text-sm text-ink">Rotary Sloter Machine</h3>
        </div>
        <div class="p-4 border-r border-b border-rule sm:col-span-2 lg:col-span-1">
          <span class="font-mono text-[11px] text-steel block mb-2">M-05 / DIE CUT</span>
          <img src="assets/images/machine-5-rotary-die-cut.png" alt="Rotary Die Cut Machine" class="w-full h-36 object-cover rounded-[4px] border border-rule mb-3" />
          <h3 class="font-display font-bold text-sm text-ink">Rotary Die Cut Machine</h3>
        </div>
      </div>

      <!-- Verified Industrial Partners Ledger (Zero PT Sharp!) -->
      <div class="border border-rule bg-surface p-6 sm:p-8">
        <div class="font-mono text-xs text-steel uppercase mb-4">
          MITRA PELANGGAN MANUFAKTUR YANG TELAH KAMI LAYANI
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 border-t border-l border-rule font-mono text-xs text-ink">
          <div class="p-3.5 border-r border-b border-rule">PT. Jaya Refrigeration Equipment (Midea)</div>
          <div class="p-3.5 border-r border-b border-rule">PT. Indorama Ventures</div>
          <div class="p-3.5 border-r border-b border-rule">PT. Yasunli Abadi Utama</div>
          <div class="p-3.5 border-r border-b border-rule">PT. Skyworth Industry Indonesia</div>
          <div class="p-3.5 border-r border-b border-rule">PT. Daijo Industrial</div>
          <div class="p-3.5 border-r border-b border-rule">PT. Nusantara Inti Solusindo</div>
          <div class="p-3.5 border-r border-b border-rule sm:col-span-2">PT. EPS Indonesia</div>
        </div>
      </div>
    </div>
  </section>
"""
    return render_head(title, description, keywords, "index.html") + render_navbar("index.html") + body + render_footer()


def build_subpage(filename, code_tag, title, description, keywords, h1_text, intro_text, sections):
    rows_html = ""
    for idx, s in enumerate(sections, 1):
        spec_items = "".join([
            f'<div class="p-3 border-r border-b border-rule text-xs"><span class="font-mono text-accent mr-1.5">0{i}</span> <span class="text-ink font-medium">{sp}</span></div>'
            for i, sp in enumerate(s["specs"], 1)
        ])
        rows_html += f"""
        <div id="{s['id']}" class="grid grid-cols-1 lg:grid-cols-12 border-b border-rule bg-surface">
          <div class="lg:col-span-5 p-6 sm:p-10 border-b lg:border-b-0 lg:border-r border-rule flex items-center justify-center bg-white">
            <img src="{s['img']}" alt="{s['name']}" class="w-full max-h-[280px] object-contain" />
          </div>
          <div class="lg:col-span-7 p-6 sm:p-12 flex flex-col justify-between">
            <div>
              <span class="font-mono text-xs text-accent block mb-2">ITEM 0{idx} — {s['code']}</span>
              <h2 class="font-display text-2xl font-bold text-ink tracking-tight mb-3">{s['name']}</h2>
              <p class="text-steel text-sm leading-relaxed max-w-[62ch] mb-6">{s['desc']}</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 border-t border-l border-rule mb-6">
                {spec_items}
              </div>
            </div>
            <div class="flex flex-wrap items-center gap-3">
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20minta%20penawaran%20harga%20(RFQ)%20untuk%20{s['wa_topic']}" target="_blank" rel="noopener" class="tactile-btn bg-accent hover:bg-accentDark text-white font-display font-semibold text-xs px-6 py-3 rounded-[6px] spring-transition">
                Minta Penawaran (RFQ) via WhatsApp
              </a>
              <a href="mailto:marketing@wirasenamajubersama.com?subject=RFQ%20-%20{s['wa_topic']}" class="px-5 py-3 border border-rule bg-canvas hover:border-ink text-ink font-mono text-xs rounded-[6px] spring-transition">
                marketing@wirasenamajubersama.com
              </a>
            </div>
          </div>
        </div>
        """

    body = f"""
  <section class="border-b border-rule bg-surface">
    <div class="max-w-[1360px] mx-auto border-x border-rule p-6 sm:p-12 lg:p-16">
      <div class="font-mono text-xs text-accent mb-3">{code_tag}</div>
      <h1 class="font-display text-3xl sm:text-5xl font-bold text-ink tracking-tight max-w-4xl leading-[1.15]">
        {h1_text}
      </h1>
      <p class="text-steel text-base leading-relaxed max-w-[65ch] mt-5">
        {intro_text}
      </p>
    </div>
  </section>

  <section class="bg-canvas">
    <div class="max-w-[1360px] mx-auto border-x border-rule">
      {rows_html}
    </div>
  </section>
"""
    return render_head(title, description, keywords, filename) + render_navbar(filename) + body + render_footer()


def build_articles_page():
    filename = "artikel-seo.html"
    title = "Jurnal Teknis & Panduan Pengadaan Pabrik Cikarang Bekasi | PT. Wirasena Maju Bersama Rayya"
    description = "Jurnal teknis pengadaan kebutuhan pabrik, panduan spesifikasi Carton Box & Impraboard, serta daftar suku cadang Electrical, Mechanical & Pneumatics di Cikarang Bekasi."
    keywords = "panduan pengadaan pabrik, spesifikasi carton box single double wall, box impraboard esd, daftar sparepart electrical mechanical pabrik, supplier pabrik terdekat cikarang"

    body = """
  <section class="border-b border-rule bg-surface">
    <div class="max-w-[1360px] mx-auto border-x border-rule p-6 sm:p-12 lg:p-16">
      <div class="font-mono text-xs text-accent mb-3">TECHNICAL PROCUREMENT JOURNAL</div>
      <h1 class="font-display text-3xl sm:text-5xl font-bold text-ink tracking-tight max-w-4xl leading-[1.15]">
        Jurnal Teknis &amp; Referensi Pengadaan Kebutuhan Pabrik
      </h1>
      <p class="text-steel text-base leading-relaxed max-w-[65ch] mt-5">
        Referensi spesifikasi teknis untuk tim Purchasing, PPIC, dan Maintenance pabrik di kawasan industri Cikarang, Bekasi, dan Karawang.
      </p>
    </div>
  </section>

  <section class="bg-canvas">
    <div class="max-w-[1360px] mx-auto border-x border-rule divide-y divide-rule bg-surface">
      
      <article class="p-6 sm:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-3 font-mono text-xs text-steel">
          <span class="text-accent font-semibold block">DOC-01 — 2026-10-27</span>
          <span class="block mt-1">PACKAGING ENGINEERING</span>
        </div>
        <div class="lg:col-span-9">
          <h2 class="font-display text-xl sm:text-2xl font-bold text-ink mb-3">
            Standar Pemilihan Flute &amp; Ketebalan Dinding Carton Box (Single, Double &amp; Triple Wall) untuk Pengiriman Industri
          </h2>
          <p class="text-steel text-sm leading-relaxed max-w-[65ch] mb-4">
            Pemilihan struktur gelombang kertas (B-Flute, C-Flute, E-Flute, atau kombinasi CB-Flute) menentukan daya tahan tumpukan (Box Compression Test) saat barang disimpan di gudang maupun dikirim antar pabrik. Fasilitas PT. Wirasena Maju Bersama Rayya mengoperasikan 5 mesin produksi in-house untuk menjamin presisi lipatan (creasing) dan kekuatan perekatan (folder glue).
          </p>
          <a href="pabrik-carton-box-impraboard.html" class="font-mono text-xs font-semibold text-accent hover:underline">Lihat Spesifikasi Carton Box &rarr;</a>
        </div>
      </article>

      <article class="p-6 sm:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-3 font-mono text-xs text-steel">
          <span class="text-accent font-semibold block">DOC-02 — 2026-10-25</span>
          <span class="block mt-1">MRO &amp; ELECTRICAL SUPPLY</span>
        </div>
        <div class="lg:col-span-9">
          <h2 class="font-display text-xl sm:text-2xl font-bold text-ink mb-3">
            Daftar Komponen Electrical, Mechanical &amp; Pneumatics Kritis untuk Mencegah Downtime Lini Produksi
          </h2>
          <p class="text-steel text-sm leading-relaxed max-w-[65ch] mb-4">
            Ketersediaan suku cadang seperti Sensor Proximity/Photoelectric, Magnetic Contactor, Inverter VFD, Bearing kecepatan tinggi, V-Belt, hingga Solenoid Valve dan Air Cylinder sangat krusial bagi tim Maintenance pabrik. Layanan General Trading kami menyediakan pengadaan satu pintu sesuai part number dan merek yang diminta buyer.
          </p>
          <a href="supplier-electrical-mechanical.html" class="font-mono text-xs font-semibold text-accent hover:underline">Lihat Katalog Electrical &amp; Mechanical &rarr;</a>
        </div>
      </article>

      <article class="p-6 sm:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-3 font-mono text-xs text-steel">
          <span class="text-accent font-semibold block">DOC-03 — 2026-10-22</span>
          <span class="block mt-1">RETURNABLE PACKAGING &amp; HANDLING</span>
        </div>
        <div class="lg:col-span-9">
          <h2 class="font-display text-xl sm:text-2xl font-bold text-ink mb-3">
            Efisiensi Sirkulasi Komponen Otomotif &amp; Elektronik Menggunakan Box Impraboard Partisi ESD dan Storage Trolley
          </h2>
          <p class="text-steel text-sm leading-relaxed max-w-[65ch] mb-4">
            Penggunaan Box Impraboard (PP Corrugated) bersekat yang dipadukan dengan Custom Storage Trolley Stainless/Besi meminimalkan risiko goresan maupun kerusakan elektrostatik (ESD) pada komponen presisi di lantai produksi.
          </p>
          <a href="jasa-fabrikasi-trolley.html" class="font-mono text-xs font-semibold text-accent hover:underline">Lihat Spesifikasi Trolley &amp; Fabrikasi &rarr;</a>
        </div>
      </article>

    </div>
  </section>
"""
    return render_head(title, description, keywords, filename) + render_navbar(filename) + body + render_footer()


def main():
    # 1. index.html
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index_page())

    # 2. supplier-electrical-mechanical.html
    me_sections = [
        {
            "id": "electrical",
            "code": "ELECTRICAL & AUTOMATION",
            "name": "Supplier Alat Listrik Industri & Panel Otomasi Pabrik",
            "img": "assets/images/studio-electrical-mechanical.png?v=6",
            "desc": "Pengadaan komponen kelistrikan industri, sensor otomasi, dan instrumen panel kontrol untuk kebutuhan Maintenance & Engineering pabrik di Cikarang dan Bekasi.",
            "specs": [
                "PLC, Inverter (VFD), Power Supply, Timer, Counter & Temperature Controller",
                "Sensor Photoelectric, Proximity, Limit Switch, Push Button & Pilot Lamp",
                "MCB, MCCB, Magnetic Contactor, Thermal Overload Relay & Kabel Kontrol",
                "Peralatan Listrik Industri, Lampu Highbay Gudang & Aksesoris Panel"
            ],
            "wa_topic": "Alat%20Listrik%20Industri%20dan%20Electrical"
        },
        {
            "id": "mechanical",
            "code": "MECHANICAL & CUTTING TOOLS",
            "name": "Supplier Sparepart Mesin, Bearing, Transmisi & Perkakas Teknik",
            "img": "assets/images/trading-tools.png",
            "desc": "Suplai suku cadang mekanikal mesin produksi, komponen transmisi penggerak, serta perkakas bengkel (cutting tools & hand tools) sesuai part number buyer.",
            "specs": [
                "Bearing (Ball, Roller, Linear, Pillow Block), V-Belt, Timing Belt & Pulley",
                "Gearbox, Elektro Motor Dinamo, Roller Conveyor, Coupling & Mechanical Seal",
                "Cutting Tools: Endmill Carbide, Drill Bit, Tap, Dies & Insert Bubut CNC",
                "Hand Tools, Kunci Torsi, Gerinda & Alat Ukur Presisi Workshop"
            ],
            "wa_topic": "Sparepart%20Mechanical%20dan%20Cutting%20Tools"
        },
        {
            "id": "pneumatics",
            "code": "PNEUMATICS, SAFETY K3 & CONSUMABLES",
            "name": "Supplier Komponen Pneumatics, Alat Safety K3 & Kain Majun Pabrik",
            "img": "assets/images/studio-pneumatics.png?v=6",
            "desc": "Pengadaan komponen sistem udara bertekanan (Pneumatics) serta perlengkapan keselamatan kerja (APD K3) dan bahan habis pakai operasional pabrik.",
            "specs": [
                "Solenoid Valve, Air Cylinder, Air Filter Regulator Lubricator (FRL) & Pressure Gauge",
                "One-Touch Fitting, Speed Controller, Quick Coupler & Selang PU / Nylon",
                "Alat Safety K3: Sepatu Safety, Helm Proyek, Kacamata, Masker, Earplug & Sarung Tangan",
                "Kain Majun Jahit/Putih, Chemical Maintenance, Pest Control, Cleaning & Office Supplies"
            ],
            "wa_topic": "Komponen%20Pneumatics%20dan%20Safety%20K3"
        }
    ]
    with open(os.path.join(BASE_DIR, "supplier-electrical-mechanical.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "supplier-electrical-mechanical.html",
            "DIVISION 01 — GENERAL TRADING & FACTORY MRO SUPPLY",
            "Supplier Alat Listrik Industri, Sparepart Mechanical & Pneumatics Cikarang | PT. Wirasena Maju Bersama Rayya",
            "Supplier kebutuhan pabrik terdekat di Cikarang & Bekasi: Alat Listrik Industri (PLC, Sensor, Inverter, Contactor), Sparepart Mechanical (Bearing, Belt, Gearbox), Pneumatics & Safety K3.",
            "supplier kebutuhan pabrik terdekat, supplier alat listrik industri terdekat, supplier sparepart mesin pabrik, vendor mechanical electrical bekasi, supplier pneumatic cikarang",
            "Supplier Electrical, Mechanical, Pneumatics & Safety K3 Pabrik",
            "Melayani pengadaan barang operasional dan perawatan mesin pabrik (All items are as requested by the buyer) dengan pengiriman cepat ke kawasan industri Cikarang, Bekasi, dan Karawang.",
            me_sections
        ))

    # 3. pabrik-carton-box-impraboard.html
    pkg_sections = [
        {
            "id": "carton-box",
            "code": "CORRUGATED CARTON BOX MANUFACTURING",
            "name": "Pabrik Carton Box Custom & Die-Cut Box Skala Industri",
            "img": "assets/images/studio-carton-box.png?v=6",
            "desc": "Produksi langsung Carton Box ukuran custom dan Die-Cut Box menggunakan 5 mesin in-house (Cutting & Creasing, Auto/Semi Folder Glue, Rotary Sloter, Rotary Die Cut).",
            "specs": [
                "Single Wall, Double Wall & Triple Wall (B-Flute, C-Flute, E-Flute, CB-Flute)",
                "Model Regular Slotted Container (RSC), Overlap Box, Top-Bottom & Die-Cut Presisi",
                "Carton Box Safety Glass & Kemasan Pelindung Produk Elektronik/Otomotif",
                "Kualitas Kertas Kraft & Medium Terbaik dengan Pengiriman Tepat Waktu (On-Time Delivery)"
            ],
            "wa_topic": "Produksi%20Carton%20Box%20Custom"
        },
        {
            "id": "impraboard",
            "code": "PP CORRUGATED & RETURNABLE PACKAGING",
            "name": "Produsen Box Impraboard Custom & Sekat Partisi (Standar / ESD)",
            "img": "assets/images/studio-impraboard.png?v=6",
            "desc": "Pembuatan Box Impraboard (PP Hollow Sheet) lengkap dengan sekat partisi presisi, layer pad, siku penguat, dan varian Anti-Static (ESD) untuk sirkulasi komponen.",
            "specs": [
                "Ketebalan Material Impraboard 2mm, 3mm, 4mm, 5mm hingga 6mm",
                "Sekat Partisi Custom (Divider) Dilapisi PE Foam / Flocking untuk Komponen Sensitif",
                "Tersedia Varian Conductive / Anti-Static (ESD) & Berbagai Pilihan Warna",
                "Tahan Air, Ringan, Kuat & Dapat Digunakan Berulang Kali (Returnable Box)"
            ],
            "wa_topic": "Box%20Impraboard%20Custom"
        },
        {
            "id": "rubber-plastic",
            "code": "INDUSTRIAL PLASTIC, TAPE & SYNTHETIC RUBBER",
            "name": "Suplai Plastik Industri (HDPE/LDPE), PE Foam, Tape & Synthetic Rubber",
            "img": "assets/images/studio-tape-rubber.png?v=6",
            "desc": "Penyediaan material pengemasan pelindung serta fabrikasi karet teknik (Synthetic Rubber & Molded Rubber) untuk kebutuhan industri manufaktur.",
            "specs": [
                "Plastic Packing HDPE, LDPE, LLDPE Stretch Film, PE Foam & Anti-Static Bag",
                "Masking Tape, OPP Lakban Industri, Adhesive Tape, Protection & Acrylic Sheet",
                "Fabrication Synthetic Rubber, Chloroprene Rubber, Rubber Molded & Rubber Foot",
                "Tempered Glass & Kaca Pengaman Industri Sesuai Spesifikasi"
            ],
            "wa_topic": "Plastik%20Packing%20Tape%20dan%20Synthetic%20Rubber"
        }
    ]
    with open(os.path.join(BASE_DIR, "pabrik-carton-box-impraboard.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "pabrik-carton-box-impraboard.html",
            "DIVISION 02 — IN-HOUSE PACKAGING & RUBBER MANUFACTURING",
            "Pabrik Carton Box Custom & Box Impraboard Cikarang Bekasi | PT. Wirasena Maju Bersama Rayya",
            "Pabrik Carton Box custom, Die-Cut Box, Box Impraboard sekat partisi, Plastik HDPE/LDPE, PE Foam, Masking Tape & Synthetic Rubber di Cikarang Selatan, Bekasi.",
            "pabrik carton box cikarang bekasi, supplier kardus pabrik terdekat, supplier box impraboard custom, plastik packing hdpe ldpe, synthetic rubber pabrik",
            "Pabrik Carton Box Custom, Box Impraboard & Kemasan Industri",
            "Didukung fasilitas 5 mesin produksi karton boks modern di Cikarang Selatan untuk menyuplai kebutuhan kemasan pabrik dengan standar kualitas presisi dan harga kompetitif.",
            pkg_sections
        ))

    # 4. jasa-fabrikasi-trolley.html
    fab_sections = [
        {
            "id": "storage-trolley",
            "code": "STAINLESS & STEEL MATERIAL HANDLING",
            "name": "Jasa Pembuatan Custom Storage Trolley Stainless Steel & Besi",
            "img": "assets/images/studio-trolley-fabrication.png?v=6",
            "desc": "Fabrikasi Storage Trolley, Parts Trolley, dan Hand Trolley sesuai gambar kerja (custom drawing) untuk kelancaran distribusi komponen di lantai pabrik.",
            "specs": [
                "Pilihan Material Stainless Steel (SUS 304 / SUS 201) atau Besi Hollow Finishing Cat/Powder Coating",
                "Roda Heavy-Duty Industrial Caster (Polyurethane / Nylon / Rubber) Lengkap dengan Rem",
                "Dimensi Rak, Kapasitas Beban (Kg) & Sekat Disesuaikan Penuh dengan Komponen Pabrik",
                "Konstruksi Kokoh, Las Rapi & Presisi untuk Pemakaian Jangka Panjang"
            ],
            "wa_topic": "Fabrikasi%20Custom%20Storage%20Trolley"
        },
        {
            "id": "welding-fifo",
            "code": "INDUSTRIAL WELDING & WORKSTATION",
            "name": "Fabrikasi Rak Pipa FIFO, Meja Kerja Produksi & Fence Welding",
            "img": "assets/images/fabrication-welding.png",
            "desc": "Layanan pengelasan dan konstruksi logam industri untuk perlengkapan lini perakitan (assembly) serta pagar pengaman mesin pabrik.",
            "specs": [
                "Pembuatan Rak Pipa FIFO (Roller Track / Placon) untuk Sistem First-In First-Out",
                "Meja Kerja Produksi (Workstation), Jig Frame & Alat Bantu Lini Perakitan",
                "Fence Welding: Pagar Pengaman Mesin (Machine Guarding), Handrail & Partisi Area Pabrik",
                "Layanan Survey Ukuran & Pengiriman Langsung ke Pabrik di Cikarang & Bekasi"
            ],
            "wa_topic": "Jasa%20Fabrikasi%20Las%20dan%20Rak%20FIFO"
        }
    ]
    with open(os.path.join(BASE_DIR, "jasa-fabrikasi-trolley.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "jasa-fabrikasi-trolley.html",
            "DIVISION 03 — CUSTOM INDUSTRIAL METAL FABRICATION",
            "Jasa Fabrikasi Storage Trolley Stainless & Bengkel Las Industri Cikarang | PT. Wirasena Maju Bersama Rayya",
            "Jasa fabrikasi pabrik terdekat di Cikarang & Bekasi: pembuatan Custom Storage Trolley Stainless/Besi, Rak Pipa FIFO, Meja Kerja Produksi & Fence Welding industri.",
            "jasa fabrikasi pabrik terdekat, pembuatan trolley stainless pabrik, bengkel las industri bekasi, fabrikasi storage trolley cikarang",
            "Jasa Fabrikasi Storage Trolley, Rak FIFO & Konstruksi Las Industri",
            "Pengerjaan fabrikasi logam dan trolley material handling sesuai gambar teknik (custom drawing) untuk mendukung efisiensi dan keselamatan kerja di lini produksi.",
            fab_sections
        ))

    # 5. artikel-seo.html
    with open(os.path.join(BASE_DIR, "artikel-seo.html"), "w", encoding="utf-8") as f:
        f.write(build_articles_page())

    print("Successfully built all 5 pages with Google Stitch taste-design (Anti-Vibe-Coded) standard!")


if __name__ == "__main__":
    main()
