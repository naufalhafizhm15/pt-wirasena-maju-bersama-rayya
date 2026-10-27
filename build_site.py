#!/usr/bin/env python3
"""
Static Site Generator (v16 - Flawless Mobile & Responsive Layout)
PT. Wirasena Maju Bersama Rayya

Mobile & Responsive Polish per Naufal's feedback:
1. Zero Horizontal Overflow: Strict overflow-x-hidden, responsive padding (p-4/p-5 on mobile, p-8/p-12 on desktop).
2. Mobile Hero:
   - Balanced typography (text-2xl sm:text-4xl lg:text-5xl) with word-break safeguards.
   - "Poin Under Button" Glass Bar now supports smooth horizontal touch-scrolling chips on mobile and clean 5-column grid on desktop.
   - Stats grid uses clean card tiles (grid-cols-2 sm:grid-cols-3 lg:grid-cols-6) with crisp borders.
3. Section 2 ("Mengapa Memilih PT. Wirasena?"):
   - Value icons scale proportionally (w-12 h-12 on mobile with w-6 h-6 svg, w-16 h-16 on desktop).
   - Compact gap-3.5 on mobile so text has generous breathing room and never squishes.
4. Section 3 ("5 Mesin In-House"):
   - Padding scaled to p-5 sm:p-10 rounded-2xl sm:rounded-3xl.
   - All decorative blurs contained with pointer-events-none.
5. Section 4 ("Solusi Utama"):
   - Category pill tabs feature native mobile horizontal scroll chips (no messy wrapping).
   - Card paddings and image heights optimized for mobile viewports.
6. Section 5 ("Fitur & Spesifikasi Andalan"):
   - 2-Column checkmark specifications now adapt to 1-column on compact mobile and 2-column on tablet/desktop.
7. Section 6 ("Accordion"):
   - Clean touch targets and flexible titles that never break flex layout.
8. Section 7 ("26+ Mitra Industri"):
   - Responsive client tiles with flex-wrap badges.
9. Subpages:
   - All specification tables safely wrapped in overflow-x-auto min-w-full containers.
"""

import os
import re

OUT_DIR = "/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya"


def get_head(title, description, canonical_slug, extra_schema=""):
    url = f"https://wirasenamajubersama.com/{canonical_slug}" if canonical_slug else "https://wirasenamajubersama.com/"
    return f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="supplier pabrik, supplier kebutuhan pabrik terdekat, general supplier pabrik cikarang bekasi, supplier alat listrik industri terdekat, supplier sparepart mesin &amp; pneumatic pabrik, supplier alat safety K3 &amp; cleaning pabrik, supplier kardus pabrik terdekat, pabrik carton box cikarang bekasi, supplier box impraboard custom, supplier lakban &amp; plastik wrapping pabrik, jasa fabrikasi pabrik terdekat, pembuatan trolley stainless &amp; besi pabrik, bengkel las &amp; fabrikasi industri bekasi" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" type="image/png" href="assets/images/logo-avatar.png?v=19" />

  <!-- Anti-Cache Meta Tags (Forces fresh reload on mobile browsers & WhatsApp) -->
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://wirasenamajubersama.com/assets/images/logo-trans.png?v=19" />
  <meta property="og:locale" content="id_ID" />

  <!-- Google Fonts: Montserrat (TransTRACK modern bold) + Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            wira: {{
              dark: '#0B1512',
              forest: '#122620',
              accent: '#165B33',
              accentHover: '#114728',
              emerald: '#057A55',
              emeraldLight: '#DEF7EC',
              canvas: '#F9FAFB',
              surface: '#FFFFFF',
              border: '#E5E7EB',
              muted: '#6B7280',
              ink: '#111928'
            }}
          }},
          fontFamily: {{
            heading: ['"Montserrat"', 'sans-serif'],
            sans: ['"Inter"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }}
        }}
      }}
    }}
  </script>

  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    html, body {{
      overflow-x: hidden !important;
      width: 100%;
      background-color: #FFFFFF;
      color: #111928;
      -webkit-font-smoothing: antialiased;
    }}
    .pill-btn {{
      border-radius: 9999px;
      transition: all 0.2s ease-in-out;
    }}
    .pill-btn:hover {{
      transform: translateY(-1px);
    }}
    .glass-bar {{
      background: rgba(18, 38, 32, 0.78);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.14);
    }}
    .spec-table th, .spec-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #E5E7EB;
      text-align: left;
      vertical-align: top;
    }}
    .spec-table tr:last-child td {{
      border-bottom: none;
    }}
    .tab-btn.active {{
      background-color: #165B33;
      color: #FFFFFF;
      border-color: #165B33;
      box-shadow: 0 4px 12px rgba(22, 91, 51, 0.25);
    }}
    /* Hide scrollbars for native chip carousels */
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
    details > summary {{
      list-style: none;
    }}
    details > summary::-webkit-details-marker {{
      display: none;
    }}
  </style>

  <!-- JSON-LD LocalBusiness Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "Organization"],
    "name": "PT. Wirasena Maju Bersama Rayya",
    "alternateName": ["Supplier Pabrik Cikarang", "General Supplier Pabrik Bekasi", "Supplier Kebutuhan Pabrik Terdekat"],
    "description": "Supplier kebutuhan pabrik terdekat di Cikarang & Bekasi untuk Carton Box Custom, Impraboard Box, Alat Listrik Industri, Mekanikal, Pneumatik, Safety K3, dan Fabrikasi Storage Trolley.",
    "url": "https://wirasenamajubersama.com",
    "telephone": "+62-21-84990200",
    "email": "info@wirasenamajubersama.com",
    "taxID": "96.434.539.2-447.000",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Jl. Bah Kilong Kp. Kandang RT.004/002, Desa Sukadami, Kec. Cikarang Selatan",
      "addressLocality": "Kabupaten Bekasi",
      "addressRegion": "Jawa Barat",
      "postalCode": "17530",
      "addressCountry": "ID"
    }},
    "knowsAbout": [
      "Supplier Pabrik",
      "Supplier Kebutuhan Pabrik Terdekat",
      "Pabrik Corrugated Carton Box Custom",
      "Box Impraboard PP Sekat Partisi",
      "Alat Listrik Industri & Panel MRO",
      "Sparepart Mesin & Pneumatic",
      "Jasa Fabrikasi Storage Trolley"
    ]
  }}
  </script>
  {extra_schema}
</head>
"""


def get_navbar(active_page="home", transparent_hero=False):
    nav_bg = "bg-white/95 backdrop-blur-md border-b border-wira-border text-wira-ink" if not transparent_hero else "bg-wira-dark/90 backdrop-blur-md border-b border-white/10 text-white"
    link_color = "text-slate-700 hover:text-wira-accent" if not transparent_hero else "text-slate-200 hover:text-white"
    active_color = "text-wira-accent font-bold" if not transparent_hero else "text-emerald-400 font-bold"

    def nav_class(page):
        return active_color if active_page == page else link_color

    return f"""
<body class="font-sans antialiased selection:bg-wira-accent selection:text-white">

  <!-- MAIN STICKY NAVBAR -->
  <header class="sticky top-0 z-50 {nav_bg} transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-20 gap-3">
        
        <!-- Brand Logo & Identity -->
        <a href="index.html" class="flex items-center gap-2.5 sm:gap-3.5 shrink-0 group">
          <img src="assets/images/logo-trans.png?v=19" alt="PT. Wirasena Maju Bersama Rayya" class="h-9 sm:h-12 w-auto object-contain bg-white rounded-lg p-1 shadow-sm shrink-0" />
          <div class="max-w-[190px] sm:max-w-none">
            <span class="font-heading font-extrabold text-xs sm:text-base lg:text-lg block leading-tight tracking-tight truncate sm:whitespace-normal">
              PT. Wirasena Maju Bersama Rayya
            </span>
            <span class="text-[10px] sm:text-[11px] text-slate-400 block font-heading font-medium tracking-wide truncate">
              Packaging &bull; Supply Chain &bull; Fabrication
            </span>
          </div>
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="hidden lg:flex items-center gap-7 font-heading text-sm" aria-label="Menu Utama">
          <a href="index.html" class="{nav_class('home')} transition-colors">Beranda</a>

          <!-- Dropdown Katalog Solusi -->
          <div class="relative group">
            <button type="button" class="flex items-center gap-1.5 py-2 font-medium {nav_class('katalog' if active_page in ['trading','packaging','fabrikasi'] else '')}">
              <span>Katalog Solusi</span>
              <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>
            <div class="invisible opacity-0 group-hover:visible group-hover:opacity-100 transition-all duration-150 absolute left-0 top-full w-80 bg-white text-wira-ink border border-wira-border rounded-2xl shadow-xl py-2.5 z-50">
              <a href="index.html#solusi-utama" class="block px-5 py-2.5 hover:bg-slate-50 border-b border-slate-100">
                <span class="font-heading font-bold text-xs text-wira-accent block">Semua Lini Solusi &rarr;</span>
                <span class="text-[11px] text-slate-500">Ringkasan produk manufaktur &amp; pengadaan</span>
              </a>
              <a href="pabrik-carton-box-impraboard.html" class="block px-5 py-2.5 hover:bg-slate-50">
                <span class="font-heading font-bold text-xs text-wira-ink block">Carton Box &amp; Box Impraboard</span>
                <span class="text-[11px] text-slate-500">Kardus custom single/double wall &amp; sekat partisi</span>
              </a>
              <a href="supplier-electrical-mechanical.html" class="block px-5 py-2.5 hover:bg-slate-50">
                <span class="font-heading font-bold text-xs text-wira-ink block">Electrical, Mechanical &amp; Pneumatik</span>
                <span class="text-[11px] text-slate-500">Komponen panel, bearing, perkakas &amp; safety APD</span>
              </a>
              <a href="jasa-fabrikasi-trolley.html" class="block px-5 py-2.5 hover:bg-slate-50">
                <span class="font-heading font-bold text-xs text-wira-ink block">Fabrikasi Storage Trolley &amp; Las</span>
                <span class="text-[11px] text-slate-500">Trolley stainless/besi, rak pipa FIFO &amp; meja QC</span>
              </a>
            </div>
          </div>

          <a href="index.html#mengapa-memilih" class="{link_color} font-medium transition-colors">Keunggulan</a>
          <a href="index.html#fasilitas-mesin" class="{link_color} font-medium transition-colors">Mesin In-House</a>
          <a href="index.html#mitra-industri" class="{link_color} font-medium transition-colors">Mitra Pabrik</a>
          <a href="#kontak-rfq" class="{link_color} font-medium transition-colors">Kontak &amp; RFQ</a>
        </nav>

        <!-- CTA Buttons (Pill shape ala TransTRACK) -->
        <div class="hidden sm:flex items-center gap-3 shrink-0">
          <a href="#kontak-rfq" class="pill-btn bg-wira-accent hover:bg-wira-accentHover text-white font-heading font-bold text-xs sm:text-sm px-5 py-2.5 sm:px-6 sm:py-3 shadow-md transition flex items-center gap-2">
            <span>Minta Penawaran</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
            </svg>
          </a>
        </div>

        <!-- Mobile Drawer Toggle -->
        <button id="mobile-menu-btn" type="button" aria-label="Buka Menu Navigasi" class="lg:hidden p-2 rounded-xl border border-white/20 text-current hover:bg-white/10 transition">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
          </svg>
        </button>

      </div>
    </div>

    <!-- Mobile Drawer Overlay -->
    <div id="mobile-drawer" class="hidden lg:hidden bg-white text-wira-ink border-t border-wira-border px-5 pt-4 pb-6 space-y-2 shadow-2xl">
      <a href="index.html" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-bold hover:bg-slate-50">Beranda</a>
      <a href="pabrik-carton-box-impraboard.html" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50">Carton Box Custom &amp; Impraboard</a>
      <a href="supplier-electrical-mechanical.html" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50">Electrical, Mechanical &amp; Pneumatik</a>
      <a href="jasa-fabrikasi-trolley.html" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50">Fabrikasi Storage Trolley &amp; Las</a>
      <a href="index.html#fasilitas-mesin" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50">5 Mesin Produksi In-House</a>
      <a href="index.html#mitra-industri" class="mobile-nav-link block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50">Mitra Pabrik Manufaktur</a>
      <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5">
        <a href="#kontak-rfq" class="mobile-nav-link pill-btn text-center py-3 bg-wira-accent text-white font-heading font-bold text-xs shadow-md">
          Minta Penawaran Harga (WhatsApp)
        </a>
        <a href="tel:+622184990200" class="pill-btn text-center py-2.5 border border-slate-300 text-xs font-semibold text-slate-700">
          Telepon: (021) 8499 0200
        </a>
      </div>
    </div>
  </header>
"""


def get_footer_and_scripts():
    return """
  <!-- SECTION 8: CONTACT & FAST WHATSAPP RFQ -->
  <section id="kontak-rfq" class="py-12 sm:py-20 bg-wira-canvas border-t border-wira-border overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-10">
        <p class="font-heading text-xs font-bold text-wira-accent uppercase tracking-wider mb-2">Konsultasi Cepat B2B</p>
        <h2 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight">
          Minta Penawaran Harga (RFQ)
        </h2>
        <p class="text-slate-600 text-xs sm:text-base mt-2">
          Kirim rincian kebutuhan Anda, gambar kerja (drawing), atau daftar part yang dicari. Tim kami siap merespon cepat via WhatsApp dan Email resmi.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Left: Official Company Contacts -->
        <div class="lg:col-span-5 bg-white border border-wira-border rounded-2xl sm:rounded-[28px] p-5 sm:p-8 shadow-sm space-y-6">
          <div class="flex items-center gap-3 pb-5 border-b border-slate-100">
            <img src="assets/images/logo-trans.png?v=19" alt="PT. Wirasena Maju Bersama Rayya" class="h-10 w-auto object-contain shrink-0" />
            <div>
              <h3 class="font-heading font-bold text-sm text-wira-ink">PT. Wirasena Maju Bersama Rayya</h3>
              <p class="text-[11px] font-mono text-emerald-600 font-semibold">NPWP: 96.434.539.2-447.000</p>
            </div>
          </div>

          <div class="space-y-4 text-xs sm:text-sm">
            <div>
              <span class="text-slate-400 font-medium block text-xs">Alamat Workshop &amp; Gudang:</span>
              <p class="text-slate-700 font-medium mt-0.5 leading-relaxed">
                Jl. Bah Kilong Kp. Kandang RT.004/002, Desa Sukadami, Kec. Cikarang Selatan, Kabupaten Bekasi, Jawa Barat 17530
              </p>
            </div>

            <div>
              <span class="text-slate-400 font-medium block text-xs">Telepon / Fax Kantor:</span>
              <a href="tel:+622184990200" class="text-wira-ink font-mono font-bold text-sm hover:text-wira-accent">
                (021) 8499 0200
              </a>
            </div>

            <div class="pt-3 border-t border-slate-100">
              <span class="text-slate-400 font-medium block text-xs mb-2">4 Email Resmi Terintegrasi:</span>
              <div class="space-y-2">
                <div class="p-2.5 bg-slate-50 rounded-xl flex items-center justify-between gap-2">
                  <div class="min-w-0">
                    <span class="text-[10px] font-bold text-wira-accent block uppercase">Marketing &amp; RFQ</span>
                    <a href="mailto:marketing@wirasenamajubersama.com" class="font-mono text-xs text-wira-ink font-semibold hover:underline truncate block">marketing@wirasenamajubersama.com</a>
                  </div>
                  <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full shrink-0">Primary</span>
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl min-w-0">
                  <span class="text-[10px] font-bold text-slate-500 block uppercase">Korespondensi Umum</span>
                  <a href="mailto:info@wirasenamajubersama.com" class="font-mono text-xs text-wira-ink hover:underline truncate block">info@wirasenamajubersama.com</a>
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl min-w-0">
                  <span class="text-[10px] font-bold text-slate-500 block uppercase">Sample &amp; Quality Control</span>
                  <a href="mailto:quality@wirasenamajubersama.com" class="font-mono text-xs text-wira-ink hover:underline truncate block">quality@wirasenamajubersama.com</a>
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl min-w-0">
                  <span class="text-[10px] font-bold text-slate-500 block uppercase">Jadwal Pengiriman (Delivery DO)</span>
                  <a href="mailto:delivery@wirasenamajubersama.com" class="font-mono text-xs text-wira-ink hover:underline truncate block">delivery@wirasenamajubersama.com</a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Interactive Quick RFQ Form -->
        <div class="lg:col-span-7 bg-white border border-wira-border rounded-2xl sm:rounded-[28px] p-5 sm:p-10 shadow-sm">
          <div class="flex items-center gap-2 mb-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
            <span class="font-heading font-bold text-xs uppercase tracking-wider text-slate-500">Form Permintaan Harga</span>
          </div>
          <h3 class="font-heading text-lg sm:text-2xl font-extrabold text-wira-ink mb-1">
            Hubungi WhatsApp Marketing Langsung
          </h3>
          <p class="text-xs sm:text-sm text-slate-600 mb-5 leading-relaxed">
            Pesan cepat tanpa ribet. Masukkan detail barang atau kustomisasi yang dibutuhkan, lalu form akan langsung membuka WhatsApp tim marketing kami.
          </p>

          <form onsubmit="submitRFQ(event)" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="rfq-name" class="block font-heading text-xs font-bold text-slate-700 mb-1.5">Nama Anda</label>
                <input id="rfq-name" type="text" required placeholder="Contoh: Hendra (Purchasing)" class="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 text-xs sm:text-sm rounded-xl border border-wira-border bg-slate-50/50 text-wira-ink focus:bg-white focus:border-wira-accent outline-none transition" />
              </div>
              <div>
                <label for="rfq-company" class="block font-heading text-xs font-bold text-slate-700 mb-1.5">Nama Pabrik / Perusahaan</label>
                <input id="rfq-company" type="text" required placeholder="Contoh: PT. Manufaktur Cikarang" class="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 text-xs sm:text-sm rounded-xl border border-wira-border bg-slate-50/50 text-wira-ink focus:bg-white focus:border-wira-accent outline-none transition" />
              </div>
            </div>

            <div>
              <label for="rfq-cat" class="block font-heading text-xs font-bold text-slate-700 mb-1.5">Lini Produk / Layanan</label>
              <select id="rfq-cat" class="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 text-xs sm:text-sm rounded-xl border border-wira-border bg-slate-50/50 text-wira-ink focus:bg-white focus:border-wira-accent outline-none transition font-medium">
                <option value="Carton Box Custom & Impraboard Box">Carton Box Custom (Kardus Single/Double Wall) &amp; Impraboard</option>
                <option value="Alat Listrik, Panel & Otomasi PLC">Alat Listrik Industri, Komponen Panel &amp; Otomasi PLC</option>
                <option value="Suku Cadang Mekanikal, Bearing & Tools">Suku Cadang Mekanikal, Transmisi, Bearing &amp; Cutting Tools</option>
                <option value="Komponen Pneumatik, Selang & Valve">Komponen Pneumatik, Silinder Udara &amp; Solenoid Valve</option>
                <option value="Fabrikasi Storage Trolley & Rak FIFO">Fabrikasi Storage Trolley Stainless/Besi &amp; Rak Pipa FIFO</option>
                <option value="Safety APD, Kain Majun & Lakban">Safety K3 (APD), Kain Majun Mesin &amp; Lakban Industri</option>
                <option value="Pengadaan Terintegrasi Multi-Kategori">Pengadaan Terintegrasi (Beberapa Lini Sekaligus)</option>
              </select>
            </div>

            <div>
              <label for="rfq-specs" class="block font-heading text-xs font-bold text-slate-700 mb-1.5">Rincian Barang / Ukuran (P x L x T) / Estimasi Kebutuhan</label>
              <textarea id="rfq-specs" rows="3" required placeholder="Contoh: Butuh Carton Box Double Wall ukuran 40x30x25 cm qty 500 pcs, dan MCB Schneider 3P 20A qty 10 pcs..." class="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 text-xs sm:text-sm rounded-xl border border-wira-border bg-slate-50/50 text-wira-ink focus:bg-white focus:border-wira-accent outline-none transition"></textarea>
            </div>

            <button type="submit" class="pill-btn w-full bg-wira-accent hover:bg-wira-accentHover text-white font-heading font-bold text-xs sm:text-sm py-3.5 sm:py-4 px-6 shadow-lg transition flex items-center justify-center gap-2">
              <span>Kirim Permintaan Harga ke WhatsApp Marketing</span>
              <svg class="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
              </svg>
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>

  <!-- DARK ROUNDED FOOTER (TransTRACK Style, rounded-3xl at top) -->
  <footer class="bg-wira-dark text-white pt-12 sm:pt-16 pb-10 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 sm:gap-10 pb-10 border-b border-white/10">
        
        <!-- Col 1: Identity & Legal -->
        <div class="lg:col-span-5 space-y-3 sm:space-y-4">
          <div class="flex items-center gap-3">
            <img src="assets/images/logo-footer-white.png?v=19" alt="PT. Wirasena Maju Bersama Rayya" class="h-9 sm:h-10 w-auto object-contain shrink-0" />
            <div>
              <span class="font-heading font-extrabold text-sm sm:text-base text-white block">PT. Wirasena Maju Bersama Rayya</span>
              <span class="font-mono text-[11px] text-emerald-400">NPWP: 96.434.539.2-447.000 (PKP)</span>
            </div>
          </div>
          <p class="text-slate-400 text-xs leading-relaxed max-w-md">
            Mitra resmi pengadaan industri terintegrasi di Cikarang Selatan, Bekasi. Produsen Carton Box Custom, Box Impraboard, General Supplier Electrical &amp; Mechanical, serta Bengkel Fabrikasi Storage Trolley.
          </p>
          <div class="text-[11px] text-slate-400 pt-1 space-y-0.5">
            <p><strong class="text-slate-200">Direktur Perusahaan:</strong> Rony Yuniawan</p>
            <p><strong class="text-slate-200">Lokasi:</strong> Sukadami, Cikarang Selatan, Kab. Bekasi 17530</p>
          </div>
        </div>

        <!-- Col 2: Navigation Links -->
        <div class="lg:col-span-3 space-y-2.5">
          <h4 class="font-heading font-bold text-xs uppercase tracking-wider text-emerald-400">
            Katalog Produk &amp; Layanan
          </h4>
          <ul class="space-y-2 text-xs text-slate-300">
            <li><a href="pabrik-carton-box-impraboard.html" class="hover:text-white transition">Carton Box &amp; Box Impraboard</a></li>
            <li><a href="supplier-electrical-mechanical.html" class="hover:text-white transition">Alat Listrik, Panel &amp; PLC</a></li>
            <li><a href="supplier-electrical-mechanical.html#mechanical" class="hover:text-white transition">Sparepart Mekanikal &amp; Bearing</a></li>
            <li><a href="supplier-electrical-mechanical.html#pneumatics" class="hover:text-white transition">Komponen Pneumatik &amp; Valve</a></li>
            <li><a href="jasa-fabrikasi-trolley.html" class="hover:text-white transition">Fabrikasi Storage Trolley</a></li>
            <li><a href="jasa-fabrikasi-trolley.html#welding-fifo" class="hover:text-white transition">Rak Pipa FIFO &amp; Jasa Las</a></li>
          </ul>
        </div>

        <!-- Col 3: Industrial Coverage -->
        <div class="lg:col-span-4 space-y-2.5">
          <h4 class="font-heading font-bold text-xs uppercase tracking-wider text-emerald-400">
            Area Jangkauan Pengiriman
          </h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            Pengiriman armada sendiri tepat waktu melayani kawasan industri utama:
          </p>
          <div class="flex flex-wrap gap-1.5 text-[10px] text-slate-300">
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">Jababeka</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">EJIP</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">MM2100</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">Lippo Cikarang</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">Delta Silicon</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">GIIC Deltamas</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">Hyundai</span>
            <span class="px-2 py-0.5 bg-white/5 border border-white/10 rounded-full">KIIC &amp; Karawang</span>
          </div>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-500 text-center sm:text-left">
        <p>&copy; 2026 PT. Wirasena Maju Bersama Rayya. All Rights Reserved.</p>
        <p class="font-mono">Resmi Berbadan Hukum &bull; PKP &bull; Cikarang Selatan</p>
      </div>

    </div>
  </footer>

  <!-- FLOATING WHATSAPP PILL BUTTON (Mobile-friendly compact size) -->
  <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20tanya%20harga%20produk%20pabrik:" target="_blank" rel="noopener" class="pill-btn fixed bottom-4 right-4 sm:bottom-5 sm:right-5 z-50 bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-bold text-xs px-4 py-3 sm:px-5 sm:py-3.5 shadow-2xl flex items-center gap-2 transition">
    <svg class="w-4 h-4 sm:w-5 sm:h-5 fill-current shrink-0" viewBox="0 0 24 24">
      <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
    </svg>
    <span>Tanya Harga WA</span>
  </a>

  <!-- SCRIPTS -->
  <script>
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');
    if (mobileBtn && mobileDrawer) {
      mobileBtn.addEventListener('click', () => {
        mobileDrawer.classList.toggle('hidden');
      });
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', () => {
          mobileDrawer.classList.add('hidden');
        });
      });
    }

    function submitRFQ(e) {
      e.preventDefault();
      const name = document.getElementById('rfq-name').value.trim();
      const comp = document.getElementById('rfq-company').value.trim();
      const cat = document.getElementById('rfq-cat').value;
      const specs = document.getElementById('rfq-specs').value.trim();
      const msg = `Halo PT. Wirasena Maju Bersama Rayya,\\n\\nSaya *${name}* dari *${comp}* ingin meminta penawaran harga (RFQ):\\n- Kategori: ${cat}\\n- Rincian Barang / Kebutuhan:\\n${specs}\\n\\nMohon informasi ketersediaan, harga dan jadwal pengirimannya. Terima kasih.`;
      window.open(`https://wa.me/622184990200?text=${encodeURIComponent(msg)}`, '_blank');
    }

    // Solution tab filter
    function filterSolutions(cat, btn) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.solution-card').forEach(card => {
        if (cat === 'all' || card.dataset.cat === cat) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }

    // TransTRACK Logo Slider Controller (Auto-Slide, Navigation Arrows & Clickable Dots)
    let currentLogoSlide = 0;
    const totalLogoSlides = 4;
    let logoInterval = null;

    function goToLogoSlide(idx) {
      currentLogoSlide = (idx + totalLogoSlides) % totalLogoSlides;
      const track = document.getElementById('logo-track');
      if (track) {
        track.style.transform = `translateX(-${currentLogoSlide * 100}%)`;
      }
      const dots = document.querySelectorAll('.dot-indicator');
      dots.forEach((dot, i) => {
        if (i === currentLogoSlide) {
          dot.className = 'dot-indicator block w-2.5 h-2.5 rounded-full bg-wira-accent ring-2 ring-emerald-300 transition-all duration-300';
        } else {
          dot.className = 'dot-indicator block w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-slate-400 transition-all duration-300';
        }
      });
    }

    function nextLogoSlide() {
      goToLogoSlide(currentLogoSlide + 1);
    }

    function prevLogoSlide() {
      goToLogoSlide(currentLogoSlide - 1);
    }

    function startLogoAutoPlay() {
      if (!logoInterval) {
        logoInterval = setInterval(() => {
          goToLogoSlide(currentLogoSlide + 1);
        }, 3200);
      }
    }

    function stopLogoAutoPlay() {
      if (logoInterval) {
        clearInterval(logoInterval);
        logoInterval = null;
      }
    }

    const sliderEl = document.getElementById('logo-slider-container');
    if (sliderEl) {
      startLogoAutoPlay();
      sliderEl.addEventListener('mouseenter', stopLogoAutoPlay);
      sliderEl.addEventListener('mouseleave', startLogoAutoPlay);

      // Mobile Touch Swipe Handling
      let touchStartX = 0;
      let touchEndX = 0;
      sliderEl.addEventListener('touchstart', e => {
        touchStartX = e.touches[0].clientX;
        stopLogoAutoPlay();
      }, { passive: true });

      sliderEl.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].clientX;
        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 40) {
          if (diff > 0) nextLogoSlide();
          else prevLogoSlide();
        }
        startLogoAutoPlay();
      }, { passive: true });
    }
  </script>
</body>
</html>
"""


def build_index():
    head = get_head(
        "Supplier Pabrik Cikarang Bekasi &amp; Pabrik Kemasan Karton | PT. Wirasena",
        "Supplier kebutuhan pabrik terdekat di Cikarang &amp; Bekasi. Pengadaan cepat alat listrik industri, sparepart mesin mechanical, pneumatic, APD K3, pabrik kardus carton box custom, dan fabrikasi trolley.",
        ""
    )
    nav = get_navbar("home", transparent_hero=True)

    body = """
  <main>
    <!-- SECTION 1: CINEMATIC DARK HERO (TransTRACK Style, Mobile-Tuned) -->
    <section class="relative bg-wira-dark text-white pt-10 pb-16 sm:pt-20 sm:pb-28 overflow-hidden">
      <!-- TransTRACK Cinematic Industrial Packaging Plant & Machine Floor Background -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-65" style="background-image: url('assets/images/wirasena-factory-hero-bg.jpg?v=19');"></div>
      <!-- Vignette and dark gradient overlay for text readability -->
      <div class="absolute inset-0 bg-gradient-to-b from-[#0B1512]/80 via-[#0B1512]/50 to-[#070D0B] opacity-95 pointer-events-none"></div>
      <div class="absolute inset-0 bg-[radial-gradient(#165B33_1px,transparent_1px)] [background-size:24px_24px] opacity-10 pointer-events-none"></div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center flex flex-col items-center">
        
        <!-- Punchy TransTRACK-Style Outcome Headline (Responsive font sizes) -->
        <h1 class="font-heading font-extrabold text-2xl sm:text-4xl lg:text-6xl text-white tracking-tight leading-[1.2] max-w-5xl break-words">
          Solusi Pengadaan &amp; Manufaktur Industri untuk <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-green-300">Efisiensi Operasional</span> Pabrik yang Lebih Baik
        </h1>

        <!-- Subheadline (Actionable, Outcome-Driven) -->
        <p class="font-sans text-slate-300 text-xs sm:text-base lg:text-xl max-w-3xl mt-4 sm:mt-5 leading-relaxed font-normal">
          Dengan <strong>PT. Wirasena Maju Bersama Rayya</strong>, sederhanakan pengadaan kemasan <em>Carton Box</em> &amp; <em>Impraboard</em> (5 mesin in-house), fabrikasi <em>Storage Trolley</em>, hingga suku cadang <em>Electrical &amp; Mechanical</em> dalam satu pintu terpercaya.
        </p>

        <!-- TransTRACK Main Buttons (Pill Shapes: Solid Accent + Light Border) -->
        <div class="mt-6 sm:mt-8 flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 w-full sm:w-auto">
          <a href="#kontak-rfq" class="pill-btn w-full sm:w-auto bg-wira-accent hover:bg-wira-accentHover text-white font-heading font-bold text-xs sm:text-base px-6 py-3.5 sm:px-8 sm:py-4 shadow-xl flex items-center justify-center gap-2">
            <span>Minta Penawaran Harga</span>
            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
            </svg>
          </a>
          <a href="#solusi-utama" class="pill-btn w-full sm:w-auto bg-white/10 hover:bg-white/20 text-white border border-white/20 font-heading font-semibold text-xs sm:text-base px-6 py-3.5 sm:px-7 sm:py-4 backdrop-blur-md flex items-center justify-center gap-2">
            <span>Eksplor Katalog Solusi</span>
            <svg class="w-4 h-4 text-slate-300 shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/>
            </svg>
          </a>
        </div>

        <!-- TransTRACK "Poin Under Button" Glass Bar (Mobile Horizontal Touch Carousel & Desktop 5-Grid) -->
        <div class="mt-8 sm:mt-10 w-full max-w-4xl glass-bar rounded-2xl p-3 sm:p-5 shadow-2xl">
          <div class="flex overflow-x-auto no-scrollbar sm:grid sm:grid-cols-5 gap-2.5 sm:gap-4 text-center">
            
            <div class="p-2 sm:p-3 rounded-xl bg-white/5 border border-white/5 flex flex-col items-center shrink-0 w-36 sm:w-auto">
              <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-1 font-bold text-[11px] sm:text-xs">01</span>
              <span class="font-heading font-bold text-[11px] sm:text-xs text-white whitespace-nowrap">5 Mesin In-House</span>
              <span class="text-[10px] text-slate-400 mt-0.5">Pabrik Sendiri</span>
            </div>

            <div class="p-2 sm:p-3 rounded-xl bg-white/5 border border-white/5 flex flex-col items-center shrink-0 w-36 sm:w-auto">
              <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-1 font-bold text-[11px] sm:text-xs">02</span>
              <span class="font-heading font-bold text-[11px] sm:text-xs text-white whitespace-nowrap">Satu Pintu PO</span>
              <span class="text-[10px] text-slate-400 mt-0.5">Hemat Waktu</span>
            </div>

            <div class="p-2 sm:p-3 rounded-xl bg-white/5 border border-white/5 flex flex-col items-center shrink-0 w-36 sm:w-auto">
              <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-1 font-bold text-[11px] sm:text-xs">03</span>
              <span class="font-heading font-bold text-[11px] sm:text-xs text-white whitespace-nowrap">Custom Drawing</span>
              <span class="text-[10px] text-slate-400 mt-0.5">Presisi Ukuran</span>
            </div>

            <div class="p-2 sm:p-3 rounded-xl bg-white/5 border border-white/5 flex flex-col items-center shrink-0 w-36 sm:w-auto">
              <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-1 font-bold text-[11px] sm:text-xs">04</span>
              <span class="font-heading font-bold text-[11px] sm:text-xs text-white whitespace-nowrap">Respon &amp; Sample</span>
              <span class="text-[10px] text-slate-400 mt-0.5">Uji Coba QC</span>
            </div>

            <div class="p-2 sm:p-3 rounded-xl bg-white/5 border border-white/5 flex flex-col items-center shrink-0 w-36 sm:w-auto">
              <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-1 font-bold text-[11px] sm:text-xs">05</span>
              <span class="font-heading font-bold text-[11px] sm:text-xs text-white whitespace-nowrap">Armada Sendiri</span>
              <span class="text-[10px] text-slate-400 mt-0.5">Tepat Jadwal</span>
            </div>

          </div>
        </div>

        <!-- TransTRACK-Style Bottom Stats Grid (Mobile-friendly 2-col tiles) -->
        <div class="mt-10 sm:mt-14 w-full pt-8 sm:pt-10 border-t border-white/10 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4 text-center">
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-white">5 Unit</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">Mesin In-House</div>
          </div>
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-emerald-400">26+</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">Mitra Manufaktur</div>
          </div>
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-white">300+</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">SKU Teknik &amp; K3</div>
          </div>
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-emerald-400">1 Pintu</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">Kemudahan PO</div>
          </div>
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-white">100%</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">Standar Mutu QC</div>
          </div>
          <div class="p-3 bg-white/5 rounded-2xl border border-white/5">
            <div class="font-heading font-extrabold text-2xl sm:text-4xl text-emerald-400">Direct</div>
            <div class="text-[11px] text-slate-400 mt-0.5 font-heading">Kirim Sendiri</div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION 2: MENGAPA MEMILIH PT. WIRASENA? (TransTRACK Split Layout, Mobile-Proportional Badges) -->
    <section id="mengapa-memilih" class="py-12 sm:py-20 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Left Visual Card (rounded-2xl sm:rounded-[28px]) -->
          <div class="lg:col-span-5">
            <div class="relative rounded-2xl sm:rounded-[28px] bg-gradient-to-b from-[#122620] to-[#0A1612] p-5 sm:p-8 text-white overflow-hidden shadow-xl border border-emerald-950">
              <div class="absolute -right-10 -bottom-10 w-60 h-60 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
              
              <div class="relative z-10 space-y-4 sm:space-y-6">
                <span class="inline-block px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider">
                  Workshop Cikarang Selatan
                </span>
                <h3 class="font-heading font-extrabold text-xl sm:text-3xl text-white leading-tight">
                  Dedikasi Penuh untuk Kelancaran Lini Produksi Pabrik Anda
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                  Kami mengintegrasikan pabrikasi kemasan karton boks, suplai barang habis pakai (MRO), dan bengkel pengelasan logam presisi di bawah satu bendera resmi berlegalitas lengkap.
                </p>

                <!-- Workshop Visual Snapshot -->
                <div class="rounded-xl sm:rounded-2xl overflow-hidden border border-white/10 shadow-md">
                  <img src="assets/images/machine-2b-auto-folder-glue.png?v=19" alt="Mesin Produksi Automatic Folder Glue PT Wirasena" class="w-full h-44 sm:h-52 object-cover" />
                </div>

                <div class="p-3 sm:p-4 rounded-xl bg-white/5 border border-white/10 flex items-center justify-between text-xs">
                  <div>
                    <span class="text-slate-400 block text-[10px] sm:text-[11px]">Kapasitas Produksi:</span>
                    <strong class="text-emerald-300 font-heading text-xs sm:text-sm">5 Lini Mesin In-House</strong>
                  </div>
                  <a href="#fasilitas-mesin" class="pill-btn px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-heading font-bold text-xs">
                    Cek Mesin &rarr;
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: 5 Value Rows with Proportional Badges -->
          <div class="lg:col-span-7 space-y-6 sm:space-y-8">
            <div>
              <p class="font-heading text-xs font-bold text-wira-accent uppercase tracking-wider mb-1.5">Keunggulan Operasional</p>
              <h2 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight">
                Mengapa Memilih <span class="text-wira-accent">PT. Wirasena?</span>
              </h2>
            </div>

            <div class="space-y-4 sm:space-y-6">
              
              <!-- Point 1 -->
              <div class="flex items-start gap-3.5 sm:gap-5">
                <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl sm:rounded-2xl bg-wira-accent text-white flex items-center justify-center shrink-0 shadow-md">
                  <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-heading font-bold text-sm sm:text-xl text-wira-ink">Terintegrasi Satu Pintu PO</h3>
                  <p class="text-slate-600 text-xs sm:text-sm mt-1 leading-relaxed">
                    Gabungkan kebutuhan kemasan <em>Carton Box</em>, fabrikasi <em>Storage Trolley</em>, hingga suku cadang <em>Electrical &amp; Mechanical</em> cukup lewat satu vendor resmi berfaktur pajak lengkap.
                  </p>
                </div>
              </div>

              <!-- Point 2 -->
              <div class="flex items-start gap-3.5 sm:gap-5">
                <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl sm:rounded-2xl bg-emerald-100 text-wira-accent flex items-center justify-center shrink-0">
                  <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-heading font-bold text-sm sm:text-xl text-wira-ink">Fasilitas Mesin In-House Mandiri</h3>
                  <p class="text-slate-600 text-xs sm:text-sm mt-1 leading-relaxed">
                    Didukung 5 lini mesin produksi kardus (<em>Folder Glue, Rotary Sloter, Die Cut</em>) dan bengkel las sendiri di Cikarang Selatan untuk jaminan harga tangan pertama dan jadwal pasti.
                  </p>
                </div>
              </div>

              <!-- Point 3 -->
              <div class="flex items-start gap-3.5 sm:gap-5">
                <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl sm:rounded-2xl bg-wira-accent text-white flex items-center justify-center shrink-0 shadow-md">
                  <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-heading font-bold text-sm sm:text-xl text-wira-ink">Kustomisasi Dimensi &amp; Drawing Presisi</h3>
                  <p class="text-slate-600 text-xs sm:text-sm mt-1 leading-relaxed">
                    Bebas memesan ketebalan gelombang kardus, partisi busa EVA, sekat boks Impraboard ESD, hingga dimensi trolley sesuai <em>engineering drawing</em> part pabrik Anda.
                  </p>
                </div>
              </div>

              <!-- Point 4 -->
              <div class="flex items-start gap-3.5 sm:gap-5">
                <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl sm:rounded-2xl bg-emerald-100 text-wira-accent flex items-center justify-center shrink-0">
                  <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-heading font-bold text-sm sm:text-xl text-wira-ink">Respon Cepat &amp; Fasilitas Sample</h3>
                  <p class="text-slate-600 text-xs sm:text-sm mt-1 leading-relaxed">
                    Permintaan harga (RFQ) dan pembuatan <em>sample mockup</em> dilayani sigap agar tim Purchasing, QC, dan Produksi Anda dapat menguji kecocokan tanpa menunggu lama.
                  </p>
                </div>
              </div>

              <!-- Point 5 -->
              <div class="flex items-start gap-3.5 sm:gap-5">
                <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl sm:rounded-2xl bg-wira-accent text-white flex items-center justify-center shrink-0 shadow-md">
                  <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.948c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-heading font-bold text-sm sm:text-xl text-wira-ink">Pengiriman Armada Sendiri &amp; Fleksibel</h3>
                  <p class="text-slate-600 text-xs sm:text-sm mt-1 leading-relaxed">
                    Didukung armada kendaraan operasional milik sendiri untuk menjamin barang tiba langsung ke <em>receiving line</em> atau gudang pabrik di Cikarang, Karawang, dan Jabodetabek.
                  </p>
                </div>
              </div>

            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 3: FULL-WIDTH BRAND BANNER FOR 5 IN-HOUSE MACHINES (Mobile-Optimized Padding) -->
    <section id="fasilitas-mesin" class="py-10 sm:py-16 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="rounded-2xl sm:rounded-3xl bg-wira-forest text-white p-5 sm:p-10 lg:p-12 shadow-2xl relative overflow-hidden">
          <div class="absolute -right-20 -top-20 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
          
          <div class="relative z-10 text-center max-w-3xl mx-auto mb-8 sm:mb-10">
            <span class="inline-block px-3 py-1 rounded-full bg-white/10 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider mb-2.5">
              Bukti Fasilitas Pabrik Mandiri
            </span>
            <h2 class="font-heading text-xl sm:text-3xl lg:text-4xl font-extrabold text-white tracking-tight">
              Fasilitas Produksi: 5 Lini Mesin In-House di Workshop Kami
            </h2>
            <p class="text-slate-300 text-xs sm:text-base mt-2 leading-relaxed">
              Bukan sekadar perantara (calo). Pesanan <em>Carton Box</em> Anda diproduksi langsung di workshop Sukadami, Cikarang Selatan dengan 5 lini mesin khusus untuk menjamin ukuran presisi, kekuatan tumpuk, dan harga tangan pertama.
            </p>
          </div>

          <!-- 5 Machine Photo Cards with Floating White Caption Bars -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3.5 sm:gap-4">
            
            <!-- Machine 1 -->
            <div class="group relative rounded-xl sm:rounded-2xl overflow-hidden bg-white/10 border border-white/15 flex flex-col justify-between shadow-lg">
              <div class="h-40 sm:h-44 overflow-hidden">
                <img src="assets/images/machine-1-cutting-creasing.png?v=19" alt="Mesin Cutting & Creasing Carton Box" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              </div>
              <div class="p-3 bg-white text-wira-ink text-left">
                <span class="text-[10px] font-mono font-bold text-wira-accent block uppercase">Mesin 01</span>
                <strong class="font-heading font-bold text-xs block text-wira-ink">Cutting &amp; Creasing</strong>
                <span class="text-[11px] text-slate-500 block leading-tight mt-0.5">Pemotongan lembaran &amp; lipatan presisi</span>
              </div>
            </div>

            <!-- Machine 2 -->
            <div class="group relative rounded-xl sm:rounded-2xl overflow-hidden bg-white/10 border border-white/15 flex flex-col justify-between shadow-lg">
              <div class="h-40 sm:h-44 overflow-hidden">
                <img src="assets/images/machine-2b-auto-folder-glue.png?v=19" alt="Mesin Auto Folder Glue" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              </div>
              <div class="p-3 bg-white text-wira-ink text-left">
                <span class="text-[10px] font-mono font-bold text-wira-accent block uppercase">Mesin 02</span>
                <strong class="font-heading font-bold text-xs block text-wira-ink">Auto Folder Glue</strong>
                <span class="text-[11px] text-slate-500 block leading-tight mt-0.5">Pelipatan &amp; lem otomatis cepat</span>
              </div>
            </div>

            <!-- Machine 3 -->
            <div class="group relative rounded-xl sm:rounded-2xl overflow-hidden bg-white/10 border border-white/15 flex flex-col justify-between shadow-lg">
              <div class="h-40 sm:h-44 overflow-hidden">
                <img src="assets/images/machine-3-semi-folder-glue.png?v=19" alt="Mesin Semi Folder Glue" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              </div>
              <div class="p-3 bg-white text-wira-ink text-left">
                <span class="text-[10px] font-mono font-bold text-wira-accent block uppercase">Mesin 03</span>
                <strong class="font-heading font-bold text-xs block text-wira-ink">Semi Folder Glue</strong>
                <span class="text-[11px] text-slate-500 block leading-tight mt-0.5">Pengeleman boks jumbo &amp; tebal</span>
              </div>
            </div>

            <!-- Machine 4 -->
            <div class="group relative rounded-xl sm:rounded-2xl overflow-hidden bg-white/10 border border-white/15 flex flex-col justify-between shadow-lg">
              <div class="h-40 sm:h-44 overflow-hidden">
                <img src="assets/images/machine-4-rotary-sloter.png?v=19" alt="Mesin Rotary Sloter" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              </div>
              <div class="p-3 bg-white text-wira-ink text-left">
                <span class="text-[10px] font-mono font-bold text-wira-accent block uppercase">Mesin 04</span>
                <strong class="font-heading font-bold text-xs block text-wira-ink">Rotary Sloter</strong>
                <span class="text-[11px] text-slate-500 block leading-tight mt-0.5">Pembuatan celah &amp; penutup kardus</span>
              </div>
            </div>

            <!-- Machine 5 -->
            <div class="group relative rounded-xl sm:rounded-2xl overflow-hidden bg-white/10 border border-white/15 flex flex-col justify-between shadow-lg sm:col-span-2 lg:col-span-1">
              <div class="h-40 sm:h-44 overflow-hidden">
                <img src="assets/images/machine-5-rotary-die-cut.png?v=19" alt="Mesin Rotary Die Cut" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              </div>
              <div class="p-3 bg-white text-wira-ink text-left">
                <span class="text-[10px] font-mono font-bold text-wira-accent block uppercase">Mesin 05</span>
                <strong class="font-heading font-bold text-xs block text-wira-ink">Rotary Die Cut</strong>
                <span class="text-[11px] text-slate-500 block leading-tight mt-0.5">Potong bentuk custom &amp; partisi</span>
              </div>
            </div>

          </div>

          <div class="mt-6 sm:mt-8 pt-5 border-t border-white/15 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-center sm:text-left">
            <span class="text-slate-300">Siap menerima pesanan rutin maupun tender pengadaan kemasan karton pabrik.</span>
            <a href="pabrik-carton-box-impraboard.html" class="pill-btn px-5 py-2.5 bg-white text-wira-forest hover:bg-slate-100 font-heading font-bold transition text-xs shrink-0">
              Lihat Spesifikasi Lengkap Carton Box &rarr;
            </a>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 4: SOLUSI UTAMA (Native Mobile Scroll Chips + Visual Cards) -->
    <section id="solusi-utama" class="py-12 sm:py-20 bg-wira-canvas overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
          <p class="font-heading text-xs font-bold text-wira-accent uppercase tracking-wider mb-1.5">Lini Layanan Industri</p>
          <h2 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight">
            Solusi Utama <span class="text-wira-accent">PT. Wirasena</span>
          </h2>
          <p class="text-slate-600 text-xs sm:text-base mt-2">
            Pilih kategori solusi di bawah ini untuk melihat kemampuan suplai dan fasilitas manufaktur kami.
          </p>

          <!-- Native Mobile Scroll Chips -->
          <div class="mt-5 flex items-center justify-start sm:justify-center gap-2 overflow-x-auto no-scrollbar pb-2 -mx-4 px-4 sm:mx-0 sm:px-0 sm:flex-wrap">
            <button type="button" onclick="filterSolutions('all', this)" class="tab-btn active pill-btn px-4 py-2 font-heading text-xs font-bold bg-white text-slate-700 border border-slate-200 transition shrink-0">
              Semua Solusi
            </button>
            <button type="button" onclick="filterSolutions('packaging', this)" class="tab-btn pill-btn px-4 py-2 font-heading text-xs font-bold bg-white text-slate-700 border border-slate-200 transition shrink-0">
              Carton Box &amp; Impraboard
            </button>
            <button type="button" onclick="filterSolutions('teknik', this)" class="tab-btn pill-btn px-4 py-2 font-heading text-xs font-bold bg-white text-slate-700 border border-slate-200 transition shrink-0">
              Electrical, Mechanical &amp; Pneumatik
            </button>
            <button type="button" onclick="filterSolutions('fabrikasi', this)" class="tab-btn pill-btn px-4 py-2 font-heading text-xs font-bold bg-white text-slate-700 border border-slate-200 transition shrink-0">
              Fabrikasi Trolley &amp; Las
            </button>
            <button type="button" onclick="filterSolutions('safety', this)" class="tab-btn pill-btn px-4 py-2 font-heading text-xs font-bold bg-white text-slate-700 border border-slate-200 transition shrink-0">
              Safety K3, Majun &amp; Lakban
            </button>
          </div>
        </div>

        <!-- 2x2 Grid of Large Solution Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
          
          <!-- Card 1: Carton Box & Impraboard -->
          <div class="solution-card bg-white border border-wira-border rounded-2xl sm:rounded-[28px] overflow-hidden shadow-sm hover:shadow-md transition flex flex-col justify-between" data-cat="packaging">
            <div>
              <div class="h-48 sm:h-64 bg-slate-100 overflow-hidden relative">
                <img src="assets/images/product-carton-box.png?v=19" alt="Produksi Carton Box Custom" class="w-full h-full object-cover" />
                <span class="absolute top-3 left-3 pill-btn px-3 py-1 bg-wira-dark/80 text-white font-heading text-[10px] font-bold backdrop-blur-md">
                  In-House Factory
                </span>
              </div>
              <div class="p-5 sm:p-8">
                <span class="text-xs font-heading italic text-wira-accent font-semibold block mb-1">Custom Industrial Packaging</span>
                <h3 class="font-heading font-extrabold text-lg sm:text-xl text-wira-ink">Produksi Corrugated Carton Box &amp; Box Impraboard</h3>
                <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                  Lindungi produk manufaktur Anda dengan boks kardus <em>Single/Double Wall</em> berdaya tahan tumpuk tinggi, cetak logo flexo, dan boks plastik berongga Impraboard tahan air untuk sirkulasi antar-lini.
                </p>
                <div class="mt-4 flex flex-wrap gap-1.5 sm:gap-2 text-[10px] sm:text-[11px] text-slate-600">
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">B-Flute, C-Flute, BC-Flute</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Die-Cut &amp; Partisi Sekat</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Impraboard ESD Anti-Statis</span>
                </div>
              </div>
            </div>
            <div class="px-5 sm:px-8 py-3.5 bg-slate-50/70 border-t border-slate-100 flex items-center justify-between">
              <a href="pabrik-carton-box-impraboard.html" class="font-heading font-bold text-xs text-wira-accent hover:underline">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20Carton%20Box:" target="_blank" rel="noopener" class="pill-btn px-4 py-2 bg-wira-accent text-white font-heading font-bold text-xs">
                Tanya Harga
              </a>
            </div>
          </div>

          <!-- Card 2: Electrical, Mechanical & Pneumatics -->
          <div class="solution-card bg-white border border-wira-border rounded-2xl sm:rounded-[28px] overflow-hidden shadow-sm hover:shadow-md transition flex flex-col justify-between" data-cat="teknik">
            <div>
              <div class="h-48 sm:h-64 bg-slate-100 overflow-hidden relative">
                <img src="assets/images/trading-electrical-mechanical.png?v=19" alt="Pengadaan Komponen Listrik & Mesin" class="w-full h-full object-cover" />
                <span class="absolute top-3 left-3 pill-btn px-3 py-1 bg-wira-dark/80 text-white font-heading text-[10px] font-bold backdrop-blur-md">
                  MRO Supply Chain
                </span>
              </div>
              <div class="p-5 sm:p-8">
                <span class="text-xs font-heading italic text-wira-accent font-semibold block mb-1">MRO &amp; Automation Parts</span>
                <h3 class="font-heading font-extrabold text-lg sm:text-xl text-wira-ink">Alat Listrik Industri, Mekanikal &amp; Pneumatik</h3>
                <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                  Pengadaan suku cadang pemeliharaan mesin pabrik (MRO): komponen panel (MCB, Contactor, PLC), bearing transmisi, silinder pneumatik, solenoid valve, dan cutting tools sesuai nomor seri part.
                </p>
                <div class="mt-4 flex flex-wrap gap-1.5 sm:gap-2 text-[10px] sm:text-[11px] text-slate-600">
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Panel MCB, Contactor &amp; PLC</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Bearing &amp; V-Belt Transmisi</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Air Cylinder &amp; Fitting PU</span>
                </div>
              </div>
            </div>
            <div class="px-5 sm:px-8 py-3.5 bg-slate-50/70 border-t border-slate-100 flex items-center justify-between">
              <a href="supplier-electrical-mechanical.html" class="font-heading font-bold text-xs text-wira-accent hover:underline">
                Lihat Daftar Barang &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20barang%20Electrical/Mechanical:" target="_blank" rel="noopener" class="pill-btn px-4 py-2 bg-wira-accent text-white font-heading font-bold text-xs">
                Tanya Harga
              </a>
            </div>
          </div>

          <!-- Card 3: Storage Trolley & Fabrication -->
          <div class="solution-card bg-white border border-wira-border rounded-2xl sm:rounded-[28px] overflow-hidden shadow-sm hover:shadow-md transition flex flex-col justify-between" data-cat="fabrikasi">
            <div>
              <div class="h-48 sm:h-64 bg-slate-50 p-4 flex items-center justify-center relative">
                <img src="assets/images/fabrication-trolley-blue.png?v=19" alt="Fabrikasi Storage Trolley Stainless Besi" class="max-h-full max-w-full object-contain" />
                <span class="absolute top-3 left-3 pill-btn px-3 py-1 bg-wira-dark/80 text-white font-heading text-[10px] font-bold backdrop-blur-md">
                  Metal Fabrication
                </span>
              </div>
              <div class="p-5 sm:p-8">
                <span class="text-xs font-heading italic text-wira-accent font-semibold block mb-1">Material Handling &amp; Lean</span>
                <h3 class="font-heading font-extrabold text-lg sm:text-xl text-wira-ink">Fabrikasi Storage Trolley &amp; Rak Pipa FIFO</h3>
                <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                  Pembuatan kereta dorong komponen (<em>parts trolley</em>), rak aliran FIFO dengan roller track, meja kerja perakitan/QC, serta pagar pengaman mesin (<em>fence welding</em>) sesuai gambar teknik pabrik.
                </p>
                <div class="mt-4 flex flex-wrap gap-1.5 sm:gap-2 text-[10px] sm:text-[11px] text-slate-600">
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">SUS 304 &amp; Besi Hollow</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Finishing Powder Coating</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Roda Heavy-Duty PU Caster</span>
                </div>
              </div>
            </div>
            <div class="px-5 sm:px-8 py-3.5 bg-slate-50/70 border-t border-slate-100 flex items-center justify-between">
              <a href="jasa-fabrikasi-trolley.html" class="font-heading font-bold text-xs text-wira-accent hover:underline">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20konsultasi%20pembuatan%20Trolley:" target="_blank" rel="noopener" class="pill-btn px-4 py-2 bg-wira-accent text-white font-heading font-bold text-xs">
                Tanya Harga
              </a>
            </div>
          </div>

          <!-- Card 4: Safety K3 & Consumables -->
          <div class="solution-card bg-white border border-wira-border rounded-2xl sm:rounded-[28px] overflow-hidden shadow-sm hover:shadow-md transition flex flex-col justify-between" data-cat="safety">
            <div>
              <div class="h-48 sm:h-64 bg-slate-100 overflow-hidden relative">
                <img src="assets/images/trading-cleaning-k3.png?v=19" alt="Safety APD, Kain Majun & Lakban" class="w-full h-full object-cover" />
                <span class="absolute top-3 left-3 pill-btn px-3 py-1 bg-wira-dark/80 text-white font-heading text-[10px] font-bold backdrop-blur-md">
                  Consumables &amp; Safety
                </span>
              </div>
              <div class="p-5 sm:p-8">
                <span class="text-xs font-heading italic text-wira-accent font-semibold block mb-1">Daily Plant Supplies</span>
                <h3 class="font-heading font-extrabold text-lg sm:text-xl text-wira-ink">Safety APD, Kain Majun &amp; Lakban Industri</h3>
                <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                  Pengadaan rutin perlengkapan keselamatan kerja (sepatu safety, helm, sarung tangan), kain majun katun daya serap tinggi untuk pembersihan mesin, serta aneka lakban OPP &amp; stretch film.
                </p>
                <div class="mt-4 flex flex-wrap gap-1.5 sm:gap-2 text-[10px] sm:text-[11px] text-slate-600">
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Sepatu &amp; Helm Safety</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">Kain Majun Putih / Warna</span>
                  <span class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-full font-medium">OPP Tape &amp; Stretch Film</span>
                </div>
              </div>
            </div>
            <div class="px-5 sm:px-8 py-3.5 bg-slate-50/70 border-t border-slate-100 flex items-center justify-between">
              <a href="supplier-electrical-mechanical.html#pneumatics" class="font-heading font-bold text-xs text-wira-accent hover:underline">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20Safety%20K3%20/%20Majun:" target="_blank" rel="noopener" class="pill-btn px-4 py-2 bg-wira-accent text-white font-heading font-bold text-xs">
                Tanya Harga
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 5: FITUR & SPESIFIKASI ANDALAN (Responsive 1-col on mobile, 2-col on desktop) -->
    <section id="spesifikasi-andalan" class="py-12 sm:py-20 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14">
          <p class="font-heading text-xs font-bold text-wira-accent uppercase tracking-wider mb-1.5">Spesifikasi Detail</p>
          <h2 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight">
            Fitur &amp; Spesifikasi Andalan <span class="text-wira-accent">PT. Wirasena</span>
          </h2>
          <p class="text-slate-600 text-xs sm:text-base mt-2">
            Standar teknis manufaktur presisi yang siap disesuaikan dengan permintaan divisi engineering dan QC pabrik Anda.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 sm:gap-10">
          
          <!-- Showcase Card 1: Carton Box & Impraboard -->
          <div class="bg-slate-50 border border-wira-border rounded-2xl sm:rounded-[32px] p-5 sm:p-8 shadow-sm flex flex-col justify-between">
            <div>
              <div class="rounded-xl sm:rounded-2xl overflow-hidden h-48 sm:h-64 bg-white border border-slate-200 mb-5 shadow-sm">
                <img src="assets/images/product-carton-box.png?v=19" alt="Carton Box & Impraboard Packaging" class="w-full h-full object-cover" />
              </div>
              <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Industrial Packaging</span>
              <h3 class="font-heading font-extrabold text-xl sm:text-2xl text-wira-ink mt-1 mb-3">
                Spesifikasi Carton Box &amp; Box Impraboard
              </h3>

              <!-- Responsive Specification Checklists -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 sm:gap-3.5 pt-1">
                
                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Single Wall (3 Ply)</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Double Wall (5 Ply Heavy)</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">B-Flute &amp; C-Flute</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">BC-Flute Kombinasi</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Custom Rotary Die-Cut</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Box Impraboard Sekat PP</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Partisi Sekat + EVA Foam</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Tersedia Tipe ESD (Anti-Statis)</span>
                </div>

              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-200 flex items-center justify-between">
              <span class="text-[11px] sm:text-xs text-slate-500 font-medium">Bisa request sample boks</span>
              <a href="pabrik-carton-box-impraboard.html" class="pill-btn px-4 py-2 bg-wira-accent hover:bg-wira-accentHover text-white font-heading font-bold text-xs">
                Detail Kemasan &rarr;
              </a>
            </div>
          </div>

          <!-- Showcase Card 2: Fabrication & Welding -->
          <div class="bg-slate-50 border border-wira-border rounded-2xl sm:rounded-[32px] p-5 sm:p-8 shadow-sm flex flex-col justify-between">
            <div>
              <div class="rounded-xl sm:rounded-2xl overflow-hidden h-48 sm:h-64 bg-white border border-slate-200 mb-5 shadow-sm flex items-center justify-center p-3">
                <img src="assets/images/fabrication-trolley-blue.png?v=19" alt="Fabrikasi Storage Trolley" class="max-h-full max-w-full object-contain" />
              </div>
              <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Metal &amp; Workshop</span>
              <h3 class="font-heading font-extrabold text-xl sm:text-2xl text-wira-ink mt-1 mb-3">
                Spesifikasi Fabrikasi Storage Trolley &amp; Las
              </h3>

              <!-- Responsive Specification Checklists -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 sm:gap-3.5 pt-1">
                
                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Stainless Steel SUS 304</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Besi Hollow &amp; Plat Mild Steel</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Cat Oven Powder Coating</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Roda Caster PU Heavy-Duty</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Rak Aliran Pipa FIFO Roller</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Meja Kerja Assembly &amp; QC</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Pengelasan Presisi TIG / MIG</span>
                </div>

                <div class="flex items-center gap-2.5">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                  </span>
                  <span class="text-xs font-heading font-semibold text-slate-800">Fence Welding Pagar Mesin</span>
                </div>

              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-200 flex items-center justify-between">
              <span class="text-[11px] sm:text-xs text-slate-500 font-medium">Bisa survei ukuran ke pabrik</span>
              <a href="jasa-fabrikasi-trolley.html" class="pill-btn px-4 py-2 bg-wira-accent hover:bg-wira-accentHover text-white font-heading font-bold text-xs">
                Detail Fabrikasi &rarr;
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 6: INTERACTIVE ACCORDION (Clean touch targets) -->
    <section class="py-12 sm:py-20 bg-wira-canvas border-t border-wira-border overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
          
          <!-- Left Visual -->
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-[28px] overflow-hidden bg-gradient-to-b from-wira-forest to-wira-dark text-white p-6 sm:p-8 relative shadow-xl">
              <div class="space-y-4">
                <span class="inline-block px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider">
                  Kebutuhan Lintas Sektor
                </span>
                <h3 class="font-heading font-extrabold text-xl sm:text-3xl text-white leading-tight">
                  Solusi Efisiensi Pengadaan untuk Berbagai Sektor Operasi Pabrik
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                  Setiap sektor industri memiliki regulasi dan tantangan material handling yang unik. Kami menyesuaikan spesifikasi barang dan pengiriman agar sejalan dengan standar operasional pabrik Anda.
                </p>

                <div class="pt-3">
                  <img src="assets/images/machine-4-rotary-sloter.png?v=19" alt="Operasional Pabrik PT Wirasena" class="rounded-xl w-full h-40 sm:h-48 object-cover border border-white/10 shadow" />
                </div>

                <div class="pt-2 flex items-center gap-2 text-xs text-slate-400">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 shrink-0"></span>
                  <span>Mendukung Lean Manufacturing &amp; 5S Lantai Produksi</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Accordion List -->
          <div class="lg:col-span-7 space-y-3.5">
            
            <!-- Accordion 1 -->
            <details class="group bg-white border border-wira-border rounded-xl sm:rounded-2xl overflow-hidden shadow-sm" open>
              <summary class="flex items-center justify-between cursor-pointer p-4 sm:p-5 font-heading font-bold text-xs sm:text-base text-wira-ink">
                <span>1. Industri Otomotif &amp; Komponen Presisi (Tier 1 &amp; Tier 2)</span>
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 group-open:rotate-180 transition-transform shrink-0 ml-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
                </span>
              </summary>
              <div class="px-4 sm:px-5 pb-5 text-xs sm:text-sm text-slate-600 border-t border-slate-100 pt-3.5 space-y-2">
                <p>Mendukung aliran komponen perakitan dengan kemasan returnable boks Impraboard anti-gores, partisi busa EVA, serta Parts Trolley heavy-duty berspesifikasi presisi.</p>
                <div class="font-heading font-semibold text-wira-accent text-[11px] sm:text-xs pt-1">
                  Solusi Utama: <span class="font-normal text-slate-700">Box Impraboard Sekat, Parts Trolley SUS 304, Cutting Tools CNC, Bearing Transmisi</span>
                </div>
              </div>
            </details>

            <!-- Accordion 2 -->
            <details class="group bg-white border border-wira-border rounded-xl sm:rounded-2xl overflow-hidden shadow-sm">
              <summary class="flex items-center justify-between cursor-pointer p-4 sm:p-5 font-heading font-bold text-xs sm:text-base text-wira-ink">
                <span>2. Industri Elektronik, Peralatan Rumah Tangga &amp; HVAC</span>
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 group-open:rotate-180 transition-transform shrink-0 ml-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
                </span>
              </summary>
              <div class="px-4 sm:px-5 pb-5 text-xs sm:text-sm text-slate-600 border-t border-slate-100 pt-3.5 space-y-2">
                <p>Memenuhi standar proteksi tinggi dari muatan statis dan benturan fisik untuk unit pendingin, perakitan panel, dan komponen sensitif.</p>
                <div class="font-heading font-semibold text-wira-accent text-[11px] sm:text-xs pt-1">
                  Solusi Utama: <span class="font-normal text-slate-700">Corrugated Carton Box A1 &amp; Die-Cut, Kemasan Anti-Static ESD, Meja Kerja QC, Sensor Otomasi &amp; PLC</span>
                </div>
              </div>
            </details>

            <!-- Accordion 3 -->
            <details class="group bg-white border border-wira-border rounded-xl sm:rounded-2xl overflow-hidden shadow-sm">
              <summary class="flex items-center justify-between cursor-pointer p-4 sm:p-5 font-heading font-bold text-xs sm:text-base text-wira-ink">
                <span>3. Industri Injeksi Plastik &amp; Moulding</span>
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 group-open:rotate-180 transition-transform shrink-0 ml-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
                </span>
              </summary>
              <div class="px-4 sm:px-5 pb-5 text-xs sm:text-sm text-slate-600 border-t border-slate-100 pt-3.5 space-y-2">
                <p>Menyuplai wadah penampung part plastik hasil cetakan, sistem pneumatik pemindah part robotik, dan kardus packing pengiriman distributor.</p>
                <div class="font-heading font-semibold text-wira-accent text-[11px] sm:text-xs pt-1">
                  Solusi Utama: <span class="font-normal text-slate-700">Carton Box Double Wall, Silinder Pneumatik &amp; Valve, Lakban OPP, Kain Majun Mesin</span>
                </div>
              </div>
            </details>

            <!-- Accordion 4 -->
            <details class="group bg-white border border-wira-border rounded-xl sm:rounded-2xl overflow-hidden shadow-sm">
              <summary class="flex items-center justify-between cursor-pointer p-4 sm:p-5 font-heading font-bold text-xs sm:text-base text-wira-ink">
                <span>4. Divisi Maintenance (MRO) &amp; Engineering Pabrik</span>
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 group-open:rotate-180 transition-transform shrink-0 ml-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
                </span>
              </summary>
              <div class="px-4 sm:px-5 pb-5 text-xs sm:text-sm text-slate-600 border-t border-slate-100 pt-3.5 space-y-2">
                <p>Pengadaan darurat maupun berkala untuk perbaikan mesin line breakdown, pergantian kontaktor panel, bearing aus, hingga pengelasan pagar pembatas mesin.</p>
                <div class="font-heading font-semibold text-wira-accent text-[11px] sm:text-xs pt-1">
                  Solusi Utama: <span class="font-normal text-slate-700">Komponen Listrik Schneider/Mitsubishi, Solenoid SMC/Festo, Perkakas Torsi, Fence Welding</span>
                </div>
              </div>
            </details>

            <!-- Accordion 5 -->
            <details class="group bg-white border border-wira-border rounded-xl sm:rounded-2xl overflow-hidden shadow-sm">
              <summary class="flex items-center justify-between cursor-pointer p-4 sm:p-5 font-heading font-bold text-xs sm:text-base text-wira-ink">
                <span>5. Divisi Warehouse, PPIC &amp; Logistik Pengiriman</span>
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 group-open:rotate-180 transition-transform shrink-0 ml-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
                </span>
              </summary>
              <div class="px-4 sm:px-5 pb-5 text-xs sm:text-sm text-slate-600 border-t border-slate-100 pt-3.5 space-y-2">
                <p>Memastikan sistem FIFO berjalan mulus tanpa kemacetan boks, barang terpacking rapi tahan guncangan, dan logistik pengiriman aman.</p>
                <div class="font-heading font-semibold text-wira-accent text-[11px] sm:text-xs pt-1">
                  Solusi Utama: <span class="font-normal text-slate-700">Rak Pipa FIFO Placon, Stretch Film Roll, Lakban Lantai 5S, Heavy Caster Wheel</span>
                </div>
              </div>
            </details>

          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 7: TRANSTRACK-STYLE COMPANIES / MITRA SECTION -->
    <section id="mitra-industri" class="relative py-16 sm:py-24 bg-white overflow-hidden">
      <!-- Dotted World Map Background (TransTRACK Style) -->
      <div class="absolute inset-0 flex items-center justify-center pointer-events-none opacity-20">
        <img src="assets/images/map-dots.svg?v=19" alt="Peta Jaringan Kemitraan Pabrik" class="w-full max-w-5xl h-auto object-contain" />
      </div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        
        <!-- TransTRACK Headline (Montserrat Bold 48px) -->
        <h2 class="font-heading font-bold text-3xl sm:text-5xl text-wira-ink tracking-tight">
          <span class="text-wira-accent">26+ Perusahaan</span> Bergabung &amp; Bermitra
        </h2>
        <p class="font-sans text-slate-500 text-xs sm:text-base mt-2 max-w-2xl mx-auto">
          Terima kasih atas kepercayaan perusahaan-perusahaan manufaktur terkemuka di kawasan Cikarang, Bekasi, dan sekitarnya
        </p>

        <!-- TransTRACK Multi-Slide Carousel Container (Auto-play, Touch-Swipe & Clickable Dots) -->
        <div class="relative w-full max-w-6xl mx-auto mt-10 sm:mt-14" id="logo-slider-container">
          
          <!-- Prev / Next Floating Arrows -->
          <button type="button" onclick="prevLogoSlide()" aria-label="Slide Sebelumnya" class="absolute -left-2 sm:-left-6 top-1/2 -translate-y-1/2 z-10 w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/90 hover:bg-white text-slate-700 shadow-md border border-slate-200 flex items-center justify-center transition-all hover:scale-105">
            <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5"/>
            </svg>
          </button>

          <button type="button" onclick="nextLogoSlide()" aria-label="Slide Berikutnya" class="absolute -right-2 sm:-right-6 top-1/2 -translate-y-1/2 z-10 w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/90 hover:bg-white text-slate-700 shadow-md border border-slate-200 flex items-center justify-center transition-all hover:scale-105">
            <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5"/>
            </svg>
          </button>

          <!-- Overflow Mask -->
          <div class="overflow-hidden py-4 px-2">
            <!-- Sliding Track -->
            <div id="logo-track" class="flex transition-transform duration-700 ease-out" style="transform: translateX(0%);">
              
              <!-- SLIDE 0 (6 Logos Frame) -->
              <div class="w-full shrink-0 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 sm:gap-8 items-center justify-items-center px-2">
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-midea.svg?v=19" alt="PT. Jaya Refrigeration (Midea)" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-indorama.svg?v=19" alt="PT. Indorama Ventures" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-yasunli.png?v=19" alt="PT. Yasunli Abadi Utama" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-skyworth.svg?v=19" alt="PT. Skyworth Industry Indonesia" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-daijo.png?v=19" alt="PT. Daijo Industrial" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-nis.png?v=19" alt="PT. Nusantara Inti Solusindo" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
              </div>

              <!-- SLIDE 1 (Next Batch Frame) -->
              <div class="w-full shrink-0 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 sm:gap-8 items-center justify-items-center px-2">
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-eps.png?v=19" alt="PT. EPS Indonesia" class="max-h-10 sm:max-h-12 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-hns.png?v=19" alt="PT. Haeng Nam Sejahtera" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-midea.svg?v=19" alt="PT. Jaya Refrigeration (Midea)" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-indorama.svg?v=19" alt="PT. Indorama Ventures" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-yasunli.png?v=19" alt="PT. Yasunli Abadi Utama" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-skyworth.svg?v=19" alt="PT. Skyworth Industry Indonesia" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
              </div>

              <!-- SLIDE 2 (Next Batch Frame) -->
              <div class="w-full shrink-0 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 sm:gap-8 items-center justify-items-center px-2">
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-daijo.png?v=19" alt="PT. Daijo Industrial" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-nis.png?v=19" alt="PT. Nusantara Inti Solusindo" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-eps.png?v=19" alt="PT. EPS Indonesia" class="max-h-10 sm:max-h-12 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-hns.png?v=19" alt="PT. Haeng Nam Sejahtera" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-midea.svg?v=19" alt="PT. Jaya Refrigeration (Midea)" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-indorama.svg?v=19" alt="PT. Indorama Ventures" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
              </div>

              <!-- SLIDE 3 (Next Batch Frame) -->
              <div class="w-full shrink-0 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 sm:gap-8 items-center justify-items-center px-2">
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-yasunli.png?v=19" alt="PT. Yasunli Abadi Utama" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-skyworth.svg?v=19" alt="PT. Skyworth Industry Indonesia" class="max-h-9 sm:max-h-11 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-daijo.png?v=19" alt="PT. Daijo Industrial" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-nis.png?v=19" alt="PT. Nusantara Inti Solusindo" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-eps.png?v=19" alt="PT. EPS Indonesia" class="max-h-10 sm:max-h-12 max-w-full object-contain" />
                </div>
                <div class="w-32 sm:w-36 h-14 sm:h-18 flex items-center justify-center transition-transform hover:scale-110 duration-200">
                  <img src="assets/images/clients/logo-hns.png?v=19" alt="PT. Haeng Nam Sejahtera" class="max-h-11 sm:max-h-13 max-w-full object-contain" />
                </div>
              </div>

            </div>
          </div>

        </div>

        <!-- TransTRACK Pagination Dots (Frame 1597884253: Clickable Buttons with Active Indicator) -->
        <div class="mt-6 sm:mt-8 flex items-center justify-center gap-1.5" id="slider-dots">
          <button type="button" onclick="goToLogoSlide(0)" class="p-2 cursor-pointer group" aria-label="Lihat Slide 1">
            <span class="dot-indicator block w-2.5 h-2.5 rounded-full bg-wira-accent ring-2 ring-emerald-300 transition-all duration-300"></span>
          </button>
          <button type="button" onclick="goToLogoSlide(1)" class="p-2 cursor-pointer group" aria-label="Lihat Slide 2">
            <span class="dot-indicator block w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-slate-400 transition-all duration-300"></span>
          </button>
          <button type="button" onclick="goToLogoSlide(2)" class="p-2 cursor-pointer group" aria-label="Lihat Slide 3">
            <span class="dot-indicator block w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-slate-400 transition-all duration-300"></span>
          </button>
          <button type="button" onclick="goToLogoSlide(3)" class="p-2 cursor-pointer group" aria-label="Lihat Slide 4">
            <span class="dot-indicator block w-2.5 h-2.5 rounded-full bg-slate-300 hover:bg-slate-400 transition-all duration-300"></span>
          </button>
        </div>

        <!-- Quality & Standard Commitment Banner -->
        <div class="mt-12 sm:mt-16 p-5 sm:p-8 rounded-2xl sm:rounded-3xl bg-slate-50 border border-wira-border text-center max-w-4xl mx-auto">
          <span class="text-xs font-heading italic text-wira-accent font-semibold block mb-1">Komitmen pada Standar Mutu Industri</span>
          <h3 class="font-heading font-extrabold text-lg sm:text-2xl text-wira-ink">
            Jaminan Presisi Ukuran, Pengiriman Tepat Waktu &amp; Legalitas PKP
          </h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-2 max-w-2xl mx-auto leading-relaxed">
            Didukung proses Quality Control (QC) ketat di workshop Cikarang Selatan, faktur pajak resmi lengkap, serta komitmen pengiriman langsung menggunakan armada mandiri.
          </p>

          <div class="mt-5 sm:mt-6 flex flex-col sm:flex-row items-center justify-center gap-2.5 sm:gap-4 text-xs font-heading font-bold text-wira-ink">
            <div class="w-full sm:w-auto flex items-center justify-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200 shadow-xs">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shrink-0"></span>
              <span>Resmi Berbadan Hukum PT &amp; PKP</span>
            </div>
            <div class="w-full sm:w-auto flex items-center justify-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200 shadow-xs">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shrink-0"></span>
              <span>4 Email Divisi Terintegrasi</span>
            </div>
            <div class="w-full sm:w-auto flex items-center justify-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200 shadow-xs">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shrink-0"></span>
              <span>Fasilitas Sample Uji Coba</span>
            </div>
          </div>
        </div>

      </div>
    </section>
  </main>
"""
    return head + nav + body + get_footer_and_scripts()


def build_trading():
    head = get_head(
        "Supplier Kebutuhan Pabrik Terdekat: Alat Listrik &amp; Sparepart Mesin Cikarang | PT. Wirasena",
        "Supplier alat listrik industri, sparepart mesin &amp; pneumatic pabrik terdekat di Cikarang &amp; Bekasi. Pengadaan MCB, PLC, inverter, kabel, fitting pneumatic Festo SMC, dan alat safety K3 pabrik.",
        "supplier-electrical-mechanical.html"
    )
    nav = get_navbar("trading")
    body = """
  <main>
    <section class="bg-wira-dark text-white py-10 sm:py-20 relative overflow-hidden">
      <!-- Cinematic Industrial Background -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-40" style="background-image: url('assets/images/wirasena-factory-hero-bg.jpg?v=19');"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#0B1512] via-[#0E201B]/90 to-[#070D0B] opacity-90 pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <span class="inline-block px-3 py-1 rounded-full bg-white/10 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider mb-2.5">
          MRO &amp; Automation Supply
        </span>
        <h1 class="font-heading font-extrabold text-2xl sm:text-4xl lg:text-5xl text-white tracking-tight max-w-4xl leading-tight">
          Supplier Barang Electrical, Mechanical, Pneumatik &amp; Safety K3
        </h1>
        <p class="text-slate-300 text-xs sm:text-base mt-2.5 max-w-3xl leading-relaxed">
          Satu pintu pengadaan suku cadang pemeliharaan mesin (MRO) dan perlengkapan pabrik untuk kawasan industri Jababeka, EJIP, MM2100, Lippo Cikarang, Delta Silicon, GIIC Deltamas, hingga Karawang.
        </p>
      </div>
    </section>

    <section class="py-10 sm:py-20 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12 sm:space-y-16">
        
        <!-- 1. Electrical -->
        <div id="electrical" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start pb-10 sm:pb-14 border-b border-wira-border">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-slate-100">
              <img src="assets/images/trading-electrical-mechanical.png?v=19" alt="Komponen Listrik Industri & Panel" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Electrical &amp; Automation</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              1. Komponen Listrik Industri &amp; Otomasi Panel
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Pengadaan komponen panel kontrol, distribusi daya, inverter, dan sensor otomasi mesin sesuai nomor seri/spesifikasi dari tim Maintenance &amp; Engineering.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Proteksi &amp; Switchgear</th>
                    <td class="text-slate-700">MCB (1P/3P), MCCB, ELCB, Magnetic Contactor, Thermal Overload Relay (TOR), Fuse</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Otomasi &amp; Kontrol</th>
                    <td class="text-slate-700">Unit PLC, Inverter / VFD Drive, Switching Power Supply 24VDC, Timer Relay, Temperature Controller</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Sensor Industri</th>
                    <td class="text-slate-700">Proximity Sensor (Inductive/Capacitive), Photoelectric, Limit Switch, Rotary Encoder, Thermocouple</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Instalasi Panel</th>
                    <td class="text-slate-700">Kabel NYAF/NYYHY, Kabel Kontrol Shielded, Kabel Duct, Skun Kabel, Push Button, Pilot Lamp LED</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Mechanical -->
        <div id="mechanical" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start pb-10 sm:pb-14 border-b border-wira-border">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-slate-100">
              <img src="assets/images/trading-tools.png?v=19" alt="Sparepart Mekanikal & Cutting Tools" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Mechanical &amp; Tooling</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              2. Suku Cadang Mekanikal, Transmisi &amp; Cutting Tools
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Suplai komponen transmisi mekanik pabrik, bearing presisi, serta perkakas potong untuk workshop maintenance dan machining CNC.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Bearing &amp; Pillow Block</th>
                    <td class="text-slate-700">Deep Groove Ball Bearing, Spherical/Tapered Roller Bearing, Pillow Block (UCP/UCF), Linear Guide</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Transmisi Daya</th>
                    <td class="text-slate-700">V-Belt (Tipe A/B/C/SPZ/SPA), Timing Belt, Roller Chain (RS40–RS100), Sprocket, Pulley, Coupling</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Cutting Tools</th>
                    <td class="text-slate-700">Carbide Insert CNC, Endmill HSS/Carbide, Mata Bor Twist Drill, Tap &amp; Dies, Mata Gerinda Potong</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Hardware &amp; Seal</th>
                    <td class="text-slate-700">Baut &amp; Mur Baja Grade 8.8 / 10.9 / Stainless SUS 304, Oil Seal NBR, O-Ring Kit, Kunci Torsi</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. Pneumatics & Safety K3 -->
        <div id="pneumatics" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-white p-4 flex items-center justify-center">
              <img src="assets/images/trading-pneumatics.png?v=19" alt="Komponen Pneumatik & APD K3" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Pneumatics &amp; Consumables</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              3. Komponen Pneumatik, Safety K3 (APD) &amp; Kain Majun
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Suku cadang sistem udara bertekanan untuk mesin otomasi assembly, perlengkapan APD keselamatan kerja, dan kain majun daya serap tinggi.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Sistem Pneumatik</th>
                    <td class="text-slate-700">Air Cylinder, Solenoid Valve, Air Filter Regulator (FRL), Selang PU (4-12mm), Fitting One-Touch</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Safety APD (K3)</th>
                    <td class="text-slate-700">Sepatu Safety (Steel Toe), Helm Proyek, Sarung Tangan Nitrile/Katun/Las, Kacamata Safety, Masker</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Kain Majun Pabrik</th>
                    <td class="text-slate-700">Kain Majun Putih &amp; Majun Warna (Jahit Tumpuk / Lembaran Polos) bersih tanpa kawat dan serap oli</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Lakban Kemasan</th>
                    <td class="text-slate-700">OPP Tape Bening/Cokelat, Masking Tape, Double Tape Foam, Stretch Film Roll, Floor Marking Tape 5S</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </div>
    </section>
  </main>
"""
    return head + nav + body + get_footer_and_scripts()


def build_packaging():
    head = get_head(
        "Supplier Kardus Pabrik Terdekat &amp; Pabrik Carton Box Cikarang Bekasi | PT. Wirasena",
        "Supplier kardus pabrik terdekat dan pabrik corrugated carton box custom serta impraboard box berpartisi di Cikarang &amp; Bekasi. Didukung 5 mesin in-house harga langsung pabrik.",
        "pabrik-carton-box-impraboard.html"
    )
    nav = get_navbar("packaging")
    body = """
  <main>
    <section class="bg-wira-dark text-white py-10 sm:py-20 relative overflow-hidden">
      <!-- Cinematic Industrial Background -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-40" style="background-image: url('assets/images/wirasena-factory-hero-bg.jpg?v=19');"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#0B1512] via-[#0E201B]/90 to-[#070D0B] opacity-90 pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <span class="inline-block px-3 py-1 rounded-full bg-white/10 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider mb-2.5">
          In-House Packaging Factory
        </span>
        <h1 class="font-heading font-extrabold text-2xl sm:text-4xl lg:text-5xl text-white tracking-tight max-w-4xl leading-tight">
          Pabrik Corrugated Carton Box Custom &amp; Box Impraboard
        </h1>
        <p class="text-slate-300 text-xs sm:text-base mt-2.5 max-w-3xl leading-relaxed">
          Didukung 5 lini mesin produksi kardus di workshop Cikarang Selatan, kami memproduksi kemasan kardus industri dan boks plastik berongga (PP Corrugated) sesuai ukuran dan beban tumpukan pabrik Anda.
        </p>
      </div>
    </section>

    <section class="py-10 sm:py-20 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12 sm:space-y-16">
        
        <!-- 1. Carton Box -->
        <div id="carton-box" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start pb-10 sm:pb-14 border-b border-wira-border">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-slate-100">
              <img src="assets/images/product-carton-box.png?v=19" alt="Pabrik Corrugated Carton Box Custom" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">In-House Manufacturing</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              1. Corrugated Carton Box Custom (Kardus Industri)
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Diproduksi dengan mesin <em>Cutting &amp; Creasing, Auto/Semi Folder Glue, Rotary Sloter,</em> dan <em>Rotary Die Cut</em> mandiri untuk memastikan presisi dimensi part.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Konstruksi Dinding</th>
                    <td class="text-slate-700"><strong>Single Wall</strong> (3 Ply), <strong>Double Wall</strong> (5 Ply), <strong>Triple Wall</strong> (7 Ply untuk kargo berat)</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Tipe Gelombang (Flute)</th>
                    <td class="text-slate-700">B-Flute (~3mm), C-Flute (~4mm), E-Flute (~1.5mm), serta kombinasi BC-Flute / EB-Flute</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Komposisi Kertas</th>
                    <td class="text-slate-700">Kraft Liner (K125, K150, K200, K275) &amp; Corrugating Medium (M125, M150)</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Model &amp; Finishing</th>
                    <td class="text-slate-700">Boks Standar A1 (RSC), Die-Cut Box, Partisi/Sekat Kardus, Layer Pad, Cetak Logo Flexo 1-3 Warna</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Impraboard -->
        <div id="impraboard" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start pb-10 sm:pb-14 border-b border-wira-border">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-white p-4 flex items-center justify-center">
              <img src="assets/images/product-impraboard-box.png?v=19" alt="Box Impraboard PP Sekat Partisi" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Returnable Packaging</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              2. Box Impraboard (PP Corrugated) &amp; Sekat Partisi
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Wadah plastik berongga ramah lingkungan yang tahan air, kuat untuk ratusan kali siklus sirkulasi antar-pabrik, dan melindungi komponen dari gesekan.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Ketebalan Sheet</th>
                    <td class="text-slate-700">Polypropylene (PP) Hollow Sheet 2mm, 3mm, 4mm, 5mm, hingga 6mm</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Sekat / Partition</th>
                    <td class="text-slate-700">Partisi interlocking presisi, opsi pelapis busa EVA / Spunbond anti-gores part krom/halus</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Penguat Rangka</th>
                    <td class="text-slate-700">Wire frame kawat baja atas, corner plastik stacking, handle grip, card holder</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Varian ESD &amp; Warna</th>
                    <td class="text-slate-700">Tersedia Tipe Konduktif / Anti-Static (ESD Hitam), Biru, Abu-abu, Hijau, Kuning, Merah</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. Rubber & Tape -->
        <div id="rubber-tape" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-white p-4 flex items-center justify-center">
              <img src="assets/images/product-masking-tape.png?v=19" alt="Synthetic Rubber & Lakban" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Cushioning &amp; Tape</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              3. Synthetic Rubber Pad, EVA Sponge &amp; Lakban Industri
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Bantalan karet sintetis peredam getaran mesin serta busa pelindung kemasan yang dipotong presisi (custom die-cut).
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Material Rubber</th>
                    <td class="text-slate-700">Synthetic Rubber Sheet, EPDM Sponge, Neoprene, Nitrile (NBR) tahan minyak dan oli</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Busa Cushioning</th>
                    <td class="text-slate-700">EVA Foam / EVA Sponge lembaran &amp; die-cut partisi, PE Foam Sheet &amp; Roll</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Tape Pengemasan</th>
                    <td class="text-slate-700">OPP Tape Bening/Cokelat, Masking Tape, Double Tape Tissue/Foam, Floor Marking Tape 5S</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </div>
    </section>
  </main>
"""
    return head + nav + body + get_footer_and_scripts()


def build_fabrikasi():
    head = get_head(
        "Jasa Fabrikasi Pabrik Terdekat &amp; Trolley Industri Cikarang Bekasi | PT. Wirasena",
        "Jasa fabrikasi pabrik terdekat di Cikarang &amp; Bekasi untuk pembuatan trolley stainless &amp; besi pabrik, rak pipa FIFO lean production, dan bengkel las industri presisi.",
        "jasa-fabrikasi-trolley.html"
    )
    nav = get_navbar("fabrikasi")
    body = """
  <main>
    <section class="bg-wira-dark text-white py-10 sm:py-20 relative overflow-hidden">
      <!-- Cinematic Industrial Background -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-40" style="background-image: url('assets/images/wirasena-factory-hero-bg.jpg?v=19');"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#0B1512] via-[#0E201B]/90 to-[#070D0B] opacity-90 pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <span class="inline-block px-3 py-1 rounded-full bg-white/10 text-emerald-300 font-heading text-[10px] sm:text-xs font-bold uppercase tracking-wider mb-2.5">
          Industrial Metal Workshop
        </span>
        <h1 class="font-heading font-extrabold text-2xl sm:text-4xl lg:text-5xl text-white tracking-tight max-w-4xl leading-tight">
          Jasa Fabrikasi Storage Trolley, Rak Pipa FIFO &amp; Pengelasan Pabrik
        </h1>
        <p class="text-slate-300 text-xs sm:text-base mt-2.5 max-w-3xl leading-relaxed">
          Mengerjakan unit perlengkapan material handling lantai produksi sesuai gambar kerja (engineering drawing) atau hasil pengukuran tim teknis kami di pabrik Anda.
        </p>
      </div>
    </section>

    <section class="py-10 sm:py-20 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12 sm:space-y-16">
        
        <!-- 1. Storage Trolley -->
        <div id="storage-trolley" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start pb-10 sm:pb-14 border-b border-wira-border">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-white p-4 flex items-center justify-center">
              <img src="assets/images/fabrication-trolley-blue.png?v=19" alt="Fabrikasi Storage Trolley Stainless Besi" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Material Handling</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              1. Fabrikasi Storage Trolley &amp; Parts Trolley Pabrik
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Didesain khusus untuk pemindahan komponen WIP antar-lini perakitan secara aman, ergonomis, dan minim risiko benturan part.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Material Rangka</th>
                    <td class="text-slate-700"><strong>Stainless Steel</strong> (SUS 304 / SUS 201 anti-karat) atau <strong>Mild Steel</strong> (Besi Hollow, Pipa, Plat)</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Finishing Permukaan</th>
                    <td class="text-slate-700">Cat Oven <em>Powder Coating</em>, Cat Epoxy Duco Industrial (warna 5S pabrik), Poles Hairline</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Spesifikasi Roda</th>
                    <td class="text-slate-700">Heavy-Duty Caster Polyurethane (PU), Nylon, atau Rubber 4&quot;, 5&quot;, 6&quot;, 8&quot; (2 Hidup + 2 Rem)</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Kustomisasi Tambahan</th>
                    <td class="text-slate-700">Ambalan berlapis busa EVA / Karet, Pintu Wire Mesh, Towing Bar gandeng tarik kereta pabrik</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Welding & FIFO -->
        <div id="welding-fifo" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
          <div class="lg:col-span-5">
            <div class="rounded-2xl sm:rounded-3xl overflow-hidden border border-wira-border shadow-sm h-56 sm:h-72 bg-slate-100">
              <img src="assets/images/fabrication-welding.png?v=19" alt="Rak Pipa FIFO & Pengelasan Pabrik" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-7 space-y-3.5">
            <span class="text-xs font-heading font-bold text-wira-accent uppercase tracking-wider">Welding &amp; Construction</span>
            <h2 class="font-heading text-xl sm:text-3xl font-extrabold text-wira-ink">
              2. Rak Pipa FIFO Roller, Meja Kerja &amp; Fence Welding
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
              Konstruksi pengelasan presisi (MIG, TIG/Argon) untuk fasilitas keselamatan mesin, meja perakitan, dan rak aliran boks First-In First-Out.
            </p>
            <div class="rounded-xl sm:rounded-2xl border border-wira-border overflow-x-auto shadow-xs">
              <table class="w-full text-xs sm:text-sm spec-table min-w-[280px]">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-slate-50 font-heading font-bold text-wira-ink">Rak Aliran FIFO</th>
                    <td class="text-slate-700">Fabrikasi rak <em>First-In First-Out</em> pipa joint dengan <em>placon roller track</em> sirkulasi boks Impraboard</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Meja Kerja Workstation</th>
                    <td class="text-slate-700">Meja perakitan assembly, meja inspeksi QC dengan gantungan lampu LED dan alas matras anti-statis (ESD)</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Fence Welding</th>
                    <td class="text-slate-700">Pagar pengaman mesin/robot (safety guarding), partisi kawat mesh, dan pembatas jalur lalu lintas forklift</td>
                  </tr>
                  <tr>
                    <th class="bg-slate-50 font-heading font-bold text-wira-ink">Layanan Rekondisi</th>
                    <td class="text-slate-700">Perbaikan pengelasan trolley lama, pengecatan ulang oven, dan penggantian roda caster aus</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </div>
    </section>
  </main>
"""
    return head + nav + body + get_footer_and_scripts()


def verify_all_images(html_dict):
    missing = []
    for fname, content in html_dict.items():
        srcs = re.findall(r'<img[^>]+src="([^"?]+)', content)
        for src in srcs:
            full_path = os.path.join(OUT_DIR, src)
            if not os.path.isfile(full_path):
                missing.append((fname, src))
    if missing:
        raise FileNotFoundError(f"Missing image files referenced in HTML: {missing}")


def main():
    pages = {
        "index.html": build_index(),
        "supplier-electrical-mechanical.html": build_trading(),
        "pabrik-carton-box-impraboard.html": build_packaging(),
        "jasa-fabrikasi-trolley.html": build_fabrikasi(),
    }
    verify_all_images(pages)
    for filename, html in pages.items():
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html.strip() + "\n")
    print("Successfully built v16 website locally (Flawless Mobile & Responsive Layout)!")


if __name__ == "__main__":
    main()
