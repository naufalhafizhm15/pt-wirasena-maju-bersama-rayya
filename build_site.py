#!/usr/bin/env python3
"""
Static Site Generator (v10 - Clean Visual Product Catalog, No 'Panduan Buyer', 100% Verified Clean Images)
PT. Wirasena Maju Bersama Rayya

Changes in v10 per Naufal's feedback:
1. Removed 'Panduan Buyer' from all navigation menus and footers.
2. Redesigned 'Katalog Produk' from a text-heavy 9-row table into a clean, visual, scannable Product Catalog Grid using crisp, un-watermarked product photos and concise spec tags (no wall of text).
3. Zero 'Divisi' jargon, zero broken images (auto-verified against disk), zero PT Sharp, zero Heavy Duty Racking.
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" type="image/png" href="assets/images/logo-avatar.png?v=14" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://wirasenamajubersama.com/assets/images/logo-trans.png?v=14" />
  <meta property="og:locale" content="id_ID" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            wira: {{
              ink: '#111816',
              forest: '#16302B',
              green: '#2E7D32',
              greenHover: '#236327',
              canvas: '#F7F8F7',
              stone: '#EEF1EF',
              border: '#D8E0DC'
            }}
          }},
          fontFamily: {{
            heading: ['"Plus Jakarta Sans"', 'sans-serif'],
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
      overflow-x: hidden;
      width: 100%;
      background-color: #FFFFFF;
      color: #111816;
      -webkit-font-smoothing: antialiased;
    }}
    input:focus, select:focus, textarea:focus, button:focus-visible, a:focus-visible {{
      outline: 2px solid #2E7D32;
      outline-offset: 1px;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #D8E0DC;
      text-align: left;
      vertical-align: top;
    }}
    .spec-table tr:last-child td {{
      border-bottom: none;
    }}
    .cat-btn.active {{
      background-color: #16302B;
      color: #FFFFFF;
      border-color: #16302B;
    }}
    .product-card {{
      transition: border-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .product-card:hover {{
      border-color: #2E7D32;
      transform: translateY(-2px);
      box-shadow: 0 10px 24px -10px rgba(22, 48, 43, 0.12);
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
    "description": "Supplier pabrik Cikarang & Bekasi untuk Carton Box Custom, Impraboard Box, Alat Listrik, Mekanikal, Pneumatik, Safety K3, dan Fabrikasi Storage Trolley.",
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
    }}
  }}
  </script>
  {extra_schema}
</head>
"""


def get_navbar(active_page):
    def nav_style(page):
        if active_page == page:
            return "text-wira-green font-semibold border-b-2 border-wira-green py-5 text-sm whitespace-nowrap"
        return "text-slate-700 hover:text-wira-ink font-medium py-5 text-sm transition-colors whitespace-nowrap"

    return f"""
<body class="font-sans antialiased selection:bg-wira-green selection:text-white">

  <!-- TOP UTILITY BAR -->
  <div class="bg-wira-forest text-white text-xs border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-3">
        <span class="text-slate-200">Sukadami, Cikarang Selatan, Kab. Bekasi 17530</span>
        <span class="hidden md:inline text-white/30">|</span>
        <span class="hidden md:inline font-mono text-[11px] text-emerald-300">NPWP: 96.434.539.2-447.000</span>
      </div>
      <div class="flex items-center gap-4 ml-auto">
        <a href="mailto:marketing@wirasenamajubersama.com" class="hover:text-emerald-300 transition hidden sm:inline">
          marketing@wirasenamajubersama.com
        </a>
        <span class="hidden sm:inline text-white/30">|</span>
        <a href="tel:+622184990200" class="font-mono font-medium hover:text-emerald-300 transition">
          Telp: (021) 8499 0200
        </a>
      </div>
    </div>
  </div>

  <!-- STICKY NAVIGATION HEADER (Clean, zero 'Panduan Buyer') -->
  <header class="sticky top-0 z-50 bg-white border-b border-wira-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-20 gap-4">
        
        <!-- Brand Logo & Name -->
        <a href="index.html" class="flex items-center gap-3 shrink-0">
          <img src="assets/images/logo-trans.png?v=14" alt="PT. Wirasena Maju Bersama Rayya" class="h-11 sm:h-12 w-auto object-contain shrink-0" />
          <div class="hidden sm:block">
            <span class="font-heading font-bold text-base lg:text-lg text-wira-ink block leading-tight">
              PT. Wirasena Maju Bersama Rayya
            </span>
            <span class="text-xs text-slate-500 block">
              Supplier Pabrik, Carton Box &amp; Fabrikasi Cikarang
            </span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center gap-7" aria-label="Menu Utama">
          <a href="index.html" class="{nav_style('home')}">Beranda</a>

          <!-- Dropdown Katalog Produk -->
          <div class="relative group">
            <button type="button" class="flex items-center gap-1.5 {nav_style('katalog' if active_page in ['trading','packaging','fabrikasi'] else '')}">
              <span>Katalog Produk</span>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:rotate-180 transition-transform" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>
            <div class="invisible opacity-0 group-hover:visible group-hover:opacity-100 transition-all duration-150 absolute left-0 top-full w-80 bg-white border border-wira-border rounded-lg shadow-lg py-2 z-50">
              <a href="index.html#katalog-produk" class="block px-4 py-2.5 hover:bg-wira-canvas border-b border-wira-border">
                <span class="font-heading font-bold text-xs text-wira-green block">Semua Katalog Produk &rarr;</span>
                <span class="text-[11px] text-slate-500">Lihat &amp; cari seluruh kategori barang</span>
              </a>
              <a href="pabrik-carton-box-impraboard.html" class="block px-4 py-2.5 hover:bg-wira-canvas">
                <span class="font-heading font-semibold text-xs text-wira-ink block">Carton Box Custom &amp; Impraboard</span>
                <span class="text-[11px] text-slate-500">Kardus Single/Double Wall, Sekat &amp; Rubber</span>
              </a>
              <a href="supplier-electrical-mechanical.html" class="block px-4 py-2.5 hover:bg-wira-canvas">
                <span class="font-heading font-semibold text-xs text-wira-ink block">Alat Listrik, Mekanikal &amp; Pneumatik</span>
                <span class="text-[11px] text-slate-500">Komponen Panel, PLC, Bearing, Tools, Safety K3</span>
              </a>
              <a href="jasa-fabrikasi-trolley.html" class="block px-4 py-2.5 hover:bg-wira-canvas">
                <span class="font-heading font-semibold text-xs text-wira-ink block">Fabrikasi Storage Trolley &amp; Las</span>
                <span class="text-[11px] text-slate-500">Trolley Stainless/Besi, Rak Pipa FIFO &amp; Meja Kerja</span>
              </a>
            </div>
          </div>

          <a href="index.html#fasilitas-mesin" class="text-slate-700 hover:text-wira-ink font-medium py-5 text-sm transition-colors whitespace-nowrap">Mesin Produksi</a>
          <a href="index.html#pelanggan" class="text-slate-700 hover:text-wira-ink font-medium py-5 text-sm transition-colors whitespace-nowrap">Pelanggan</a>
          <a href="#kontak-rfq" class="text-slate-700 hover:text-wira-ink font-medium py-5 text-sm transition-colors whitespace-nowrap">Hubungi Kami</a>
        </nav>

        <!-- Primary Action Button -->
        <div class="hidden sm:flex items-center gap-2.5 shrink-0">
          <a href="#kontak-rfq" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs sm:text-sm px-4 py-2.5 rounded-md transition whitespace-nowrap">
            Minta Penawaran Harga
          </a>
        </div>

        <!-- Mobile Menu Button -->
        <button id="mobile-menu-btn" type="button" aria-label="Buka Menu Navigasi" aria-expanded="false" class="lg:hidden inline-flex items-center justify-center w-11 h-11 rounded-md border border-wira-border text-wira-ink hover:bg-wira-canvas">
          <svg id="icon-bars" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
          </svg>
          <svg id="icon-close" class="w-5 h-5 hidden" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>

      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobile-drawer" class="hidden lg:hidden bg-white border-t border-wira-border px-4 pt-3 pb-5 space-y-1">
      <a href="index.html" class="block px-3 py-2.5 rounded-md text-sm font-semibold text-wira-ink hover:bg-wira-canvas">
        Beranda Utama
      </a>
      <a href="pabrik-carton-box-impraboard.html" class="block px-3 py-2.5 rounded-md text-sm font-medium text-slate-700 hover:bg-wira-canvas">
        Carton Box Custom &amp; Impraboard
      </a>
      <a href="supplier-electrical-mechanical.html" class="block px-3 py-2.5 rounded-md text-sm font-medium text-slate-700 hover:bg-wira-canvas">
        Alat Listrik, Mekanikal, Pneumatik &amp; K3
      </a>
      <a href="jasa-fabrikasi-trolley.html" class="block px-3 py-2.5 rounded-md text-sm font-medium text-slate-700 hover:bg-wira-canvas">
        Fabrikasi Storage Trolley &amp; Las
      </a>
      <a href="index.html#fasilitas-mesin" class="mobile-close-link block px-3 py-2.5 rounded-md text-sm font-medium text-slate-700 hover:bg-wira-canvas">
        Mesin Produksi Kami
      </a>
      <div class="pt-3 mt-2 border-t border-wira-border grid grid-cols-2 gap-2">
        <a href="tel:+622184990200" class="text-center py-2.5 px-3 rounded-md border border-wira-border text-xs font-semibold text-wira-ink">
          Telp (021) 8499 0200
        </a>
        <a href="#kontak-rfq" class="mobile-close-link text-center py-2.5 px-3 rounded-md bg-wira-green text-white text-xs font-semibold">
          Minta Penawaran
        </a>
      </div>
    </div>
  </header>
"""


def get_rfq_and_footer():
    return """
  <!-- CONTACT & QUICK QUOTATION SECTION -->
  <section id="kontak-rfq" class="py-14 sm:py-20 bg-wira-canvas border-t border-wira-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
        
        <!-- Left 6 Cols: Contact Information -->
        <div class="lg:col-span-6">
          <h2 class="font-heading text-2xl sm:text-3xl font-bold text-wira-ink tracking-tight">
            Hubungi Kami &amp; Alamat Pabrik Cikarang
          </h2>
          <p class="text-slate-600 text-sm sm:text-base mt-2 leading-relaxed">
            Punya daftar barang yang sedang dicari, ukuran kardus/impraboard, atau gambar trolley? Silakan hubungi tim kami lewat WhatsApp, telepon, atau email di bawah ini.
          </p>

          <div class="mt-6 bg-white border border-wira-border rounded-lg overflow-hidden">
            <table class="w-full text-sm spec-table">
              <tbody>
                <tr>
                  <th class="w-1/3 font-semibold text-wira-ink bg-wira-stone/50">Alamat Pabrik &amp; Gudang</th>
                  <td class="text-xs sm:text-sm text-slate-700 leading-relaxed">
                    Jl. Bah Kilong Kp. Kandang RT.004/002, Desa Sukadami, Kec. Cikarang Selatan, Kabupaten Bekasi, Jawa Barat 17530
                  </td>
                </tr>
                <tr>
                  <th class="font-semibold text-wira-ink bg-wira-stone/50">Telepon / Fax</th>
                  <td class="font-mono text-xs sm:text-sm font-semibold text-wira-ink">
                    (021) 8499 0200
                  </td>
                </tr>
                <tr>
                  <th class="font-semibold text-wira-ink bg-wira-stone/50">Email Penawaran &amp; PO</th>
                  <td>
                    <a href="mailto:marketing@wirasenamajubersama.com" class="font-mono text-xs sm:text-sm text-wira-green font-semibold hover:underline break-all">
                      marketing@wirasenamajubersama.com
                    </a>
                    <div class="text-xs text-slate-500 mt-0.5">Untuk permintaan harga (RFQ) &amp; pemesanan barang</div>
                  </td>
                </tr>
                <tr>
                  <th class="font-semibold text-wira-ink bg-wira-stone/50">Email Resmi Lainnya</th>
                  <td class="space-y-1 text-xs">
                    <div><span class="text-slate-500">Umum &amp; Vendor:</span> <a href="mailto:info@wirasenamajubersama.com" class="font-mono text-wira-ink hover:underline">info@wirasenamajubersama.com</a></div>
                    <div><span class="text-slate-500">Sample &amp; QC:</span> <a href="mailto:quality@wirasenamajubersama.com" class="font-mono text-wira-ink hover:underline">quality@wirasenamajubersama.com</a></div>
                    <div><span class="text-slate-500">Pengiriman (DO):</span> <a href="mailto:delivery@wirasenamajubersama.com" class="font-mono text-wira-ink hover:underline">delivery@wirasenamajubersama.com</a></div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Right 6 Cols: Quick Inquiry Form -->
        <div class="lg:col-span-6 bg-white border border-wira-border rounded-lg p-6 sm:p-8">
          <h3 class="font-heading text-xl font-bold text-wira-ink">
            Minta Penawaran Harga Cepat (via WhatsApp)
          </h3>
          <p class="text-xs sm:text-sm text-slate-600 mt-1 mb-5">
            Isi rincian singkat barang yang Anda butuhkan, lalu klik tombol di bawah untuk langsung terhubung ke WhatsApp Marketing kami.
          </p>

          <form onsubmit="submitRFQ(event)" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="rfq-name" class="block text-xs font-semibold text-slate-700 mb-1">Nama Anda</label>
                <input id="rfq-name" type="text" required placeholder="Contoh: Hendra (Purchasing)" class="w-full px-3.5 py-2.5 text-sm rounded-md border border-wira-border bg-white text-wira-ink" />
              </div>
              <div>
                <label for="rfq-company" class="block text-xs font-semibold text-slate-700 mb-1">Nama Perusahaan (PT/CV)</label>
                <input id="rfq-company" type="text" required placeholder="Contoh: PT. Maju Industri" class="w-full px-3.5 py-2.5 text-sm rounded-md border border-wira-border bg-white text-wira-ink" />
              </div>
            </div>

            <div>
              <label for="rfq-cat" class="block text-xs font-semibold text-slate-700 mb-1">Kategori Barang yang Dicari</label>
              <select id="rfq-cat" class="w-full px-3.5 py-2.5 text-sm rounded-md border border-wira-border bg-white text-wira-ink">
                <option value="Carton Box Custom / Impraboard Box">Carton Box Custom / Impraboard Box</option>
                <option value="Alat Listrik, Mekanikal, Pneumatik & Safety K3">Alat Listrik, Mekanikal, Pneumatik &amp; Safety K3</option>
                <option value="Fabrikasi Storage Trolley / Rak FIFO / Las">Fabrikasi Storage Trolley / Rak FIFO / Las</option>
                <option value="Pengadaan Gabungan (Beberapa Kategori)">Pengadaan Gabungan (Beberapa Kategori)</option>
              </select>
            </div>

            <div>
              <label for="rfq-specs" class="block text-xs font-semibold text-slate-700 mb-1">Rincian Barang / Ukuran / Jumlah Kebutuhan</label>
              <textarea id="rfq-specs" rows="3" required placeholder="Tulis nama barang, ukuran (P x L x T), atau kode part serta estimasi jumlah yang dibutuhkan..." class="w-full px-3.5 py-2.5 text-sm rounded-md border border-wira-border bg-white text-wira-ink"></textarea>
            </div>

            <button type="submit" class="w-full bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-sm py-3 px-5 rounded-md transition flex items-center justify-center gap-2">
              <span>Kirim Permintaan Harga ke WhatsApp</span>
              <span aria-hidden="true">&rarr;</span>
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-wira-forest text-white border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 pb-10 border-b border-white/15">
        
        <div class="lg:col-span-5">
          <div class="flex items-center gap-3 mb-3">
            <img src="assets/images/logo-footer-white.png?v=14" alt="PT. Wirasena Maju Bersama Rayya" class="h-10 w-auto object-contain" />
            <div>
              <span class="font-heading font-bold text-base text-white block">PT. Wirasena Maju Bersama Rayya</span>
              <span class="font-mono text-xs text-emerald-300">NPWP: 96.434.539.2-447.000</span>
            </div>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-md mt-2">
            Pabrik Carton Box &amp; Impraboard Box, Supplier Kebutuhan Pabrik (Electrical, Mechanical, Pneumatik, Safety K3), serta Bengkel Fabrikasi Storage Trolley di Cikarang Selatan, Bekasi.
          </p>
        </div>

        <div class="lg:col-span-4">
          <h4 class="font-heading font-semibold text-xs uppercase tracking-wider text-emerald-300 mb-3">
            Halaman Produk &amp; Layanan
          </h4>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-200">
            <li><a href="pabrik-carton-box-impraboard.html" class="hover:text-white hover:underline">Pabrik Carton Box Custom &amp; Box Impraboard</a></li>
            <li><a href="supplier-electrical-mechanical.html" class="hover:text-white hover:underline">Supplier Alat Listrik, Mekanikal, Pneumatik &amp; K3</a></li>
            <li><a href="jasa-fabrikasi-trolley.html" class="hover:text-white hover:underline">Jasa Fabrikasi Storage Trolley &amp; Rak Pipa FIFO</a></li>
          </ul>
        </div>

        <div class="lg:col-span-3">
          <h4 class="font-heading font-semibold text-xs uppercase tracking-wider text-emerald-300 mb-3">
            Area Layanan Pengiriman
          </h4>
          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Kawasan Industri Jababeka, EJIP, Lippo Cikarang, Delta Silicon, Hyundai, MM2100 Cibitung, GIIC Deltamas, Karawang (KIIC &amp; Suryacipta), hingga Jabodetabek.
          </p>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <p>&copy; 2026 PT. Wirasena Maju Bersama Rayya. Hak Cipta Dilindungi.</p>
        <p>Direktur: Rony Yuniawan &bull; Cikarang Selatan, Kabupaten Bekasi</p>
      </div>
    </div>
  </footer>

  <!-- COMPACT WHATSAPP BUTTON -->
  <div class="fixed bottom-4 right-4 z-50 flex flex-col items-end">
    <div id="wa-popup" class="hidden mb-2.5 w-72 sm:w-80 bg-white rounded-lg shadow-xl border border-wira-border overflow-hidden">
      <div class="bg-wira-forest px-4 py-3 text-white flex items-center justify-between">
        <div>
          <span class="font-heading font-bold text-xs block">Marketing PT. Wirasena</span>
          <span class="text-[11px] text-emerald-300">Respon Cepat via WhatsApp</span>
        </div>
        <button type="button" onclick="toggleWA()" aria-label="Tutup" class="text-white/80 hover:text-white p-1">
          &#10005;
        </button>
      </div>
      <div class="p-3.5 bg-wira-canvas text-xs text-slate-700 leading-relaxed border-b border-wira-border">
        Halo Bapak/Ibu, silakan kirimkan nama barang, ukuran Carton Box/Impraboard, atau foto/drawing produk yang sedang dibutuhkan.
      </div>
      <div class="p-3 bg-white">
        <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20tanya%20harga%20produk:" target="_blank" rel="noopener" class="w-full bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs py-2.5 px-4 rounded-md flex items-center justify-center gap-2 transition">
          <span>Chat WhatsApp Sekarang</span>
          <span>&rarr;</span>
        </a>
      </div>
    </div>

    <button type="button" onclick="toggleWA()" aria-label="Chat WhatsApp Marketing" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs sm:text-sm px-4 py-3 rounded-full shadow-lg flex items-center gap-2 transition">
      <svg class="w-5 h-5 fill-current shrink-0" viewBox="0 0 24 24">
        <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
      </svg>
      <span>Tanya Harga via WA</span>
    </button>
  </div>

  <!-- INTERACTIVE SCRIPTS -->
  <script>
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');
    const iconBars = document.getElementById('icon-bars');
    const iconClose = document.getElementById('icon-close');

    if (mobileBtn && mobileDrawer) {
      mobileBtn.addEventListener('click', () => {
        const isHidden = mobileDrawer.classList.contains('hidden');
        mobileDrawer.classList.toggle('hidden');
        iconBars.classList.toggle('hidden', isHidden);
        iconClose.classList.toggle('hidden', !isHidden);
        mobileBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
      });
      document.querySelectorAll('.mobile-close-link').forEach(el => {
        el.addEventListener('click', () => {
          mobileDrawer.classList.add('hidden');
          iconBars.classList.remove('hidden');
          iconClose.classList.add('hidden');
        });
      });
    }

    function toggleWA() {
      const popup = document.getElementById('wa-popup');
      if (popup) popup.classList.toggle('hidden');
    }

    function submitRFQ(e) {
      e.preventDefault();
      const name = document.getElementById('rfq-name').value.trim();
      const company = document.getElementById('rfq-company').value.trim();
      const cat = document.getElementById('rfq-cat').value;
      const specs = document.getElementById('rfq-specs').value.trim();
      const msg = `Halo PT. Wirasena Maju Bersama Rayya,\\n\\nSaya ingin meminta penawaran harga (RFQ):\\n- Nama: ${name}\\n- Perusahaan: ${company}\\n- Kategori: ${cat}\\n- Rincian Kebutuhan:\\n${specs}\\n\\nMohon informasi harga dan estimasi waktu pengerjaan/pengiriman. Terima kasih.`;
      window.open(`https://wa.me/622184990200?text=${encodeURIComponent(msg)}`, '_blank');
    }

    // Product Catalog Filter
    let activeCategory = 'all';
    function filterByCategory(catCode, btnEl) {
      activeCategory = catCode;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      runCatalogFilter();
    }

    function quickSearchTerm(term) {
      const input = document.getElementById('part-search-input');
      if (input) {
        input.value = term;
        activeCategory = 'all';
        document.querySelectorAll('.cat-btn').forEach(b => {
          b.classList.toggle('active', b.dataset.cat === 'all');
        });
        runCatalogFilter();
        const target = document.getElementById('katalog-produk');
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function runCatalogFilter() {
      const input = document.getElementById('part-search-input');
      const query = input ? input.value.toLowerCase().trim() : '';
      const cards = document.querySelectorAll('.catalog-item');
      let visibleCount = 0;

      cards.forEach(card => {
        const catMatch = (activeCategory === 'all') || (card.dataset.cat === activeCategory);
        const textMatch = !query || card.dataset.keywords.toLowerCase().includes(query) || card.innerText.toLowerCase().includes(query);
        if (catMatch && textMatch) {
          card.classList.remove('hidden');
          visibleCount++;
        } else {
          card.classList.add('hidden');
        }
      });

      const emptyBox = document.getElementById('catalog-empty-state');
      if (emptyBox) {
        emptyBox.classList.toggle('hidden', visibleCount > 0);
      }
    }
  </script>
</body>
</html>
"""


def build_index():
    head = get_head(
        "PT. Wirasena Maju Bersama Rayya | Supplier Pabrik, Carton Box & Fabrikasi Cikarang",
        "Supplier pabrik Cikarang & Bekasi untuk Carton Box Custom, Box Impraboard, Alat Listrik & Mekanikal, Pneumatik, Safety K3, dan Fabrikasi Storage Trolley.",
        ""
    )
    nav = get_navbar("home")

    body = """
  <main>
    <!-- HERO SECTION -->
    <section class="bg-wira-canvas border-b border-wira-border py-10 sm:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
          
          <!-- Left 7 Columns -->
          <div class="lg:col-span-7">
            <p class="text-xs sm:text-sm font-semibold text-wira-green mb-2">
              Mitra Pengadaan &amp; Produksi Kebutuhan Pabrik di Cikarang, Bekasi &amp; Karawang
            </p>
            <h1 class="font-heading text-2xl sm:text-4xl lg:text-[40px] font-extrabold text-wira-ink tracking-tight leading-[1.18]">
              Pabrik Carton Box &amp; Impraboard, Supplier Alat Listrik &amp; Mekanikal, hingga Fabrikasi Trolley.
            </h1>
            <p class="text-slate-700 text-sm sm:text-base mt-3.5 leading-relaxed max-w-2xl">
              Tidak perlu repot membuka PO ke banyak tempat. <strong>PT. Wirasena Maju Bersama Rayya</strong> memproduksi langsung kemasan <em>Carton Box &amp; Impraboard</em> (dengan 5 mesin in-house), mengerjakan fabrikasi <em>Storage Trolley</em>, sekaligus menyuplai suku cadang <em>Electrical, Mechanical, Pneumatik &amp; Safety K3</em> sesuai permintaan pabrik Anda.
            </p>

            <!-- Instant Search Bar -->
            <div class="mt-6 bg-white p-2 rounded-lg border border-wira-border shadow-sm max-w-2xl">
              <form onsubmit="event.preventDefault(); document.getElementById('katalog-produk').scrollIntoView({behavior:'smooth'});" class="flex flex-col sm:flex-row gap-2">
                <input
                  id="hero-quick-input"
                  type="text"
                  oninput="const el=document.getElementById('part-search-input'); if(el){el.value=this.value; runCatalogFilter();}"
                  placeholder="Cari produk: Carton Box, Impraboard, Contactor, Pneumatik, Trolley, Majun..."
                  class="flex-1 px-3.5 py-2.5 text-sm text-wira-ink bg-white rounded-md border border-transparent focus:border-wira-green"
                />
                <button type="submit" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs sm:text-sm px-5 py-2.5 rounded-md transition shrink-0">
                  Cari Produk
                </button>
              </form>
            </div>

            <!-- Quick Product Shortcuts -->
            <div class="mt-3 flex flex-wrap items-center gap-2 text-xs">
              <span class="text-slate-500 font-medium">Paling sering dicari:</span>
              <button type="button" onclick="quickSearchTerm('carton box')" class="px-2.5 py-1 bg-white border border-wira-border rounded hover:border-wira-green text-wira-ink font-medium transition">Carton Box Custom</button>
              <button type="button" onclick="quickSearchTerm('impraboard')" class="px-2.5 py-1 bg-white border border-wira-border rounded hover:border-wira-green text-wira-ink font-medium transition">Box Impraboard Sekat</button>
              <button type="button" onclick="quickSearchTerm('electrical')" class="px-2.5 py-1 bg-white border border-wira-border rounded hover:border-wira-green text-wira-ink font-medium transition">Alat Listrik &amp; PLC</button>
              <button type="button" onclick="quickSearchTerm('pneumatic')" class="px-2.5 py-1 bg-white border border-wira-border rounded hover:border-wira-green text-wira-ink font-medium transition">Komponen Pneumatik</button>
              <button type="button" onclick="quickSearchTerm('trolley')" class="px-2.5 py-1 bg-white border border-wira-border rounded hover:border-wira-green text-wira-ink font-medium transition">Storage Trolley</button>
            </div>
          </div>

          <!-- Right 5 Columns: Real Factory Machine Photo -->
          <div class="lg:col-span-5">
            <figure class="bg-white border border-wira-border rounded-lg overflow-hidden shadow-sm">
              <img
                src="assets/images/machine-2b-auto-folder-glue.png?v=14"
                alt="Mesin Produksi Carton Box PT. Wirasena Maju Bersama Rayya di Cikarang Selatan"
                class="w-full h-64 sm:h-72 object-cover"
              />
              <figcaption class="p-4 bg-white border-t border-wira-border flex items-center justify-between gap-4 text-xs">
                <div>
                  <strong class="font-heading text-wira-ink block">Pabrik &amp; Gudang di Cikarang Selatan</strong>
                  <span class="text-slate-600">Didukung 5 lini mesin produksi kardus in-house</span>
                </div>
                <a href="#fasilitas-mesin" class="font-heading font-semibold text-wira-green hover:underline shrink-0">
                  Lihat Mesin &rarr;
                </a>
              </figcaption>
            </figure>
          </div>

        </div>
      </div>
    </section>

    <!-- VISUAL PRODUCT CATALOG (Clean, scannable, crisp un-watermarked product images, concise spec pills) -->
    <section id="katalog-produk" class="py-14 sm:py-18 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Catalog Header & Search -->
        <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-wira-border">
          <div>
            <h2 class="font-heading text-2xl sm:text-3xl font-bold text-wira-ink tracking-tight">
              Katalog Produk &amp; Layanan Pabrik
            </h2>
            <p class="text-slate-600 text-sm sm:text-base mt-1">
              Pilih kategori barang di bawah ini atau klik <strong>Tanya Harga</strong> untuk langsung berkonsultasi via WhatsApp.
            </p>
          </div>

          <div class="w-full sm:w-72">
            <input
              id="part-search-input"
              type="text"
              oninput="runCatalogFilter()"
              placeholder="Ketik nama barang..."
              class="w-full px-3.5 py-2 text-xs sm:text-sm rounded-md border border-wira-border bg-wira-canvas text-wira-ink"
            />
          </div>
        </div>

        <!-- Category Filter Buttons -->
        <div class="flex flex-wrap gap-2 py-5">
          <button type="button" data-cat="all" onclick="filterByCategory('all', this)" class="cat-btn active px-4 py-2 rounded-md border border-wira-border text-xs font-heading font-semibold text-slate-700 transition">
            Semua Produk (9)
          </button>
          <button type="button" data-cat="packaging" onclick="filterByCategory('packaging', this)" class="cat-btn px-4 py-2 rounded-md border border-wira-border text-xs font-heading font-semibold text-slate-700 transition">
            Carton Box &amp; Impraboard
          </button>
          <button type="button" data-cat="teknik" onclick="filterByCategory('teknik', this)" class="cat-btn px-4 py-2 rounded-md border border-wira-border text-xs font-heading font-semibold text-slate-700 transition">
            Alat Listrik, Mekanikal &amp; Pneumatik
          </button>
          <button type="button" data-cat="fabrikasi" onclick="filterByCategory('fabrikasi', this)" class="cat-btn px-4 py-2 rounded-md border border-wira-border text-xs font-heading font-semibold text-slate-700 transition">
            Trolley &amp; Las Pabrik
          </button>
          <button type="button" data-cat="safety" onclick="filterByCategory('safety', this)" class="cat-btn px-4 py-2 rounded-md border border-wira-border text-xs font-heading font-semibold text-slate-700 transition">
            Safety K3, Majun &amp; Lakban
          </button>
        </div>

        <!-- Clean 3-Column Visual Product Grid (Uses crisp, un-watermarked original images!) -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-2">

          <!-- 1. Carton Box Custom -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="packaging" data-keywords="carton box kardus corrugated single wall double wall triple wall b flute c flute e flute rsc die cut kardus custom pabrik">
            <div>
              <a href="pabrik-carton-box-impraboard.html#carton-box" class="block h-52 bg-wira-canvas border-b border-wira-border overflow-hidden">
                <img src="assets/images/product-carton-box.png?v=14" alt="Produksi Carton Box Custom Cikarang" class="w-full h-full object-cover" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Produksi In-House</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="pabrik-carton-box-impraboard.html#carton-box" class="hover:text-wira-green">
                    Carton Box Custom (Kardus Industri)
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Kardus kemasan pabrik sesuai ukuran (P x L x T), ketebalan gelombang, dan cetak logo perusahaan.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Single / Double / Triple Wall</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">B / C / BC Flute</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Boks A1 &amp; Die-Cut</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="pabrik-carton-box-impraboard.html#carton-box" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20Carton%20Box%20Custom:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 2. Box Impraboard & Sekat Partisi -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="packaging" data-keywords="impraboard pp corrugated box plastik berongga sekat partisi danpla returnable box esd antistatic">
            <div>
              <a href="pabrik-carton-box-impraboard.html#impraboard" class="block h-52 bg-white border-b border-wira-border p-3 flex items-center justify-center overflow-hidden">
                <img src="assets/images/product-impraboard-box.png?v=14" alt="Box Impraboard & Sekat Partisi Custom" class="max-h-full max-w-full object-contain" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Kemasan Sirkulasi Pabrik</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="pabrik-carton-box-impraboard.html#impraboard" class="hover:text-wira-green">
                    Box Impraboard &amp; Sekat Partisi
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Boks plastik PP berongga tahan air untuk sirkulasi komponen antar-lini produksi lengkap dengan sekat anti-gores.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Tebal 2mm – 6mm</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Sekat + Busa EVA</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Tersedia Anti-Statis (ESD)</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="pabrik-carton-box-impraboard.html#impraboard" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20Box%20Impraboard:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 3. Fabrikasi Storage Trolley -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="fabrikasi" data-keywords="fabrikasi storage trolley stainless steel sus 304 besi hollow parts trolley roda caster pu material handling">
            <div>
              <a href="jasa-fabrikasi-trolley.html#storage-trolley" class="block h-52 bg-white border-b border-wira-border p-3 flex items-center justify-center overflow-hidden">
                <img src="assets/images/fabrication-trolley-blue.png?v=14" alt="Fabrikasi Storage Trolley Stainless & Besi" class="max-h-full max-w-full object-contain" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Bengkel Fabrikasi Logam</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="jasa-fabrikasi-trolley.html#storage-trolley" class="hover:text-wira-green">
                    Storage Trolley Stainless &amp; Besi
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Pembuatan kereta dorong komponen (<em>Parts Trolley</em>) sesuai gambar kerja (<em>drawing</em>) atau survei ukuran di pabrik Anda.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">SUS 304 / Besi Hollow</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Powder Coating</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Roda Caster PU Heavy-Duty</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="jasa-fabrikasi-trolley.html#storage-trolley" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20konsultasi%20pembuatan%20Storage%20Trolley:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 4. Alat Listrik & Panel Otomasi -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="teknik" data-keywords="electrical alat listrik komponen panel mcb mccb contactor relay plc inverter sensor proximity limit switch kabel skun">
            <div>
              <a href="supplier-electrical-mechanical.html#electrical" class="block h-52 bg-wira-canvas border-b border-wira-border overflow-hidden">
                <img src="assets/images/trading-electrical-mechanical.png?v=14" alt="Supplier Alat Listrik Industri & Panel PLC" class="w-full h-full object-cover" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Electrical &amp; Automation</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="supplier-electrical-mechanical.html#electrical" class="hover:text-wira-green">
                    Alat Listrik Industri, Panel &amp; PLC
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Suplai komponen perawatan panel listrik dan sensor otomasi mesin sesuai nomor seri yang diminta tim Maintenance.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">MCB, MCCB &amp; Contactor</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">PLC, Inverter &amp; Sensor</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Kabel &amp; Aksesoris Panel</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="supplier-electrical-mechanical.html#electrical" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Daftar Barang &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20barang%20Electrical:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 5. Suku Cadang Mekanikal & Perkakas -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="teknik" data-keywords="mechanical sparepart mesin bearing pillow block v-belt rantai chain sprocket pulley gear perkakas hand tools cutting tools mata bor endmill">
            <div>
              <a href="supplier-electrical-mechanical.html#mechanical" class="block h-52 bg-wira-canvas border-b border-wira-border overflow-hidden">
                <img src="assets/images/trading-tools.png?v=14" alt="Sparepart Mekanikal, Bearing & Perkakas Teknik" class="w-full h-full object-cover" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Mechanical &amp; Tooling</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="supplier-electrical-mechanical.html#mechanical" class="hover:text-wira-green">
                    Sparepart Mekanikal &amp; Cutting Tools
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Pengadaan komponen transmisi mekanis mesin dan alat perkakas bengkel untuk operasional pemeliharaan pabrik.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Bearing &amp; Pillow Block</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">V-Belt, Rantai &amp; Pulley</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Mata Bor, Endmill &amp; Baut</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="supplier-electrical-mechanical.html#mechanical" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Daftar Barang &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20sparepart%20Mechanical/Tools:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 6. Komponen Pneumatik & Selang PU -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="teknik" data-keywords="pneumatic pneumatik air cylinder solenoid valve frl air filter regulator selang pu tubing fitting one touch speed controller">
            <div>
              <a href="supplier-electrical-mechanical.html#pneumatics" class="block h-52 bg-white border-b border-wira-border p-3 flex items-center justify-center overflow-hidden">
                <img src="assets/images/trading-pneumatics.png?v=14" alt="Komponen Pneumatik, Silinder, Valve & Fitting" class="max-h-full max-w-full object-contain" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Pneumatic System</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="supplier-electrical-mechanical.html#pneumatics" class="hover:text-wira-green">
                    Komponen Pneumatik &amp; Selang PU
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Suku cadang sistem udara bertekanan untuk mesin <em>assembly</em>, <em>packaging</em>, dan otomasi lini produksi.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Air Cylinder &amp; Solenoid Valve</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">FRL Filter Regulator</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Selang PU &amp; Fitting</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="supplier-electrical-mechanical.html#pneumatics" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Daftar Barang &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20komponen%20Pneumatik:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 7. Rak Pipa FIFO, Meja Kerja & Las -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="fabrikasi" data-keywords="rak pipa fifo roller track meja kerja workstation assembly fence welding pagar pengaman mesin jasa las mig tig argon">
            <div>
              <a href="jasa-fabrikasi-trolley.html#welding-fifo" class="block h-52 bg-wira-canvas border-b border-wira-border overflow-hidden">
                <img src="assets/images/fabrication-welding.png?v=14" alt="Jasa Las Industri, Rak Pipa FIFO & Meja Kerja" class="w-full h-full object-cover" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Las &amp; Konstruksi Pabrik</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="jasa-fabrikasi-trolley.html#welding-fifo" class="hover:text-wira-green">
                    Rak Pipa FIFO, Meja Kerja &amp; Las
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Pembuatan rak aliran boks FIFO, meja kerja perakitan/QC, pagar pengaman mesin (<em>fence welding</em>), dan perbaikan trolley.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Rak Roller Track FIFO</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Meja Kerja Assembly/QC</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Fence Welding (MIG/TIG)</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="jasa-fabrikasi-trolley.html#welding-fifo" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20jasa%20Rak%20FIFO%20/%20Meja%20Kerja%20/%20Las:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 8. Safety K3, Kebersihan & Kain Majun -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="safety" data-keywords="safety k3 apd sepatu safety helm sarung tangan kain majun lap mesin kebersihan cleaning">
            <div>
              <a href="supplier-electrical-mechanical.html#pneumatics" class="block h-52 bg-wira-canvas border-b border-wira-border overflow-hidden">
                <img src="assets/images/trading-cleaning-k3.png?v=14" alt="Perlengkapan Safety K3, Kain Majun & Kebersihan Pabrik" class="w-full h-full object-cover" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Consumables &amp; K3</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="supplier-electrical-mechanical.html#pneumatics" class="hover:text-wira-green">
                    Alat Safety K3, Kain Majun &amp; Kebersihan
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Suplai rutin alat pelindung diri (APD) karyawan, kain lap majun mesin daya serap tinggi, dan alat kebersihan pabrik.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Sepatu, Helm &amp; Sarung Tangan</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Kain Majun Putih/Warna</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Alat Cleaning Pabrik</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="supplier-electrical-mechanical.html#pneumatics" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Daftar Barang &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20Safety%20K3%20/%20Majun:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

          <!-- 9. Lakban Industri, Stretch Film & Synthetic Rubber -->
          <article class="catalog-item product-card bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col justify-between" data-cat="safety" data-keywords="synthetic rubber karet sintetis eva sponge epdm rubber pad bantalan anti getar masking tape opp tape lakban stretch film">
            <div>
              <a href="pabrik-carton-box-impraboard.html#rubber-tape" class="block h-52 bg-white border-b border-wira-border p-3 flex items-center justify-center overflow-hidden">
                <img src="assets/images/product-masking-tape.png?v=14" alt="Lakban Industri, Masking Tape & Synthetic Rubber" class="max-h-full max-w-full object-contain" />
              </a>
              <div class="p-5">
                <div class="text-[11px] font-semibold text-wira-green uppercase tracking-wide">Packing Tape &amp; Insulation</div>
                <h3 class="font-heading text-lg font-bold text-wira-ink mt-1">
                  <a href="pabrik-carton-box-impraboard.html#rubber-tape" class="hover:text-wira-green">
                    Lakban Industri, Stretch Film &amp; Rubber Pad
                  </a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 mt-1.5 leading-relaxed">
                  Aneka lakban pengemasan gudang, <em>stretch film roll</em>, busa pelindung EVA sponge, dan bantalan karet sintetis.
                </p>
                <div class="mt-3.5 flex flex-wrap gap-1.5">
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">OPP, Masking &amp; Double Tape</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Stretch Film &amp; Strapping</span>
                  <span class="px-2 py-1 bg-wira-canvas border border-wira-border rounded text-[11px] font-medium text-slate-700">Synthetic Rubber &amp; EVA</span>
                </div>
              </div>
            </div>
            <div class="px-5 py-3.5 bg-wira-canvas/60 border-t border-wira-border flex items-center justify-between gap-3">
              <a href="pabrik-carton-box-impraboard.html#rubber-tape" class="font-heading font-semibold text-xs text-wira-ink hover:text-wira-green">
                Lihat Spesifikasi &rarr;
              </a>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena,%20kami%20ingin%20tanya%20harga%20Lakban%20/%20Stretch%20Film%20/%20Rubber:" target="_blank" rel="noopener" class="bg-wira-green hover:bg-wira-greenHover text-white font-heading font-semibold text-xs px-3.5 py-2 rounded transition">
                Tanya Harga
              </a>
            </div>
          </article>

        </div>

        <!-- Empty Search State -->
        <div id="catalog-empty-state" class="hidden py-10 px-6 bg-wira-canvas border border-wira-border rounded-lg text-center mt-6">
          <p class="font-heading font-bold text-base text-wira-ink">Barang yang Anda cari belum tertulis di atas?</p>
          <p class="text-xs sm:text-sm text-slate-600 mt-1 mb-4">
            Kami melayani pengadaan barang pabrik sesuai permintaan pembeli (<strong>"All items are as requested by the buyer"</strong>). Silakan kirimkan nama atau foto barang tersebut ke WhatsApp kami.
          </p>
          <a href="#kontak-rfq" class="inline-block bg-wira-green text-white font-heading font-semibold text-xs px-5 py-2.5 rounded-md">
            Tanyakan Barang via Form / WhatsApp &rarr;
          </a>
        </div>

      </div>
    </section>

    <!-- 5 IN-HOUSE PRODUCTION MACHINES -->
    <section id="fasilitas-mesin" class="py-14 sm:py-18 bg-wira-canvas border-t border-wira-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-3xl mb-8">
          <h2 class="font-heading text-2xl sm:text-3xl font-bold text-wira-ink tracking-tight">
            Fasilitas Produksi: 5 Mesin Carton Box di Workshop Kami
          </h2>
          <p class="text-slate-600 text-sm sm:text-base mt-2 leading-relaxed">
            Pesanan <em>Carton Box</em> Anda diproduksi langsung di fasilitas kami di Cikarang Selatan menggunakan 5 lini mesin khusus untuk memastikan ukuran presisi dan pengiriman tepat waktu.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
          <figure class="bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col">
            <img src="assets/images/machine-1-cutting-creasing.png?v=14" alt="Mesin Cutting & Creasing Carton Box" class="w-full h-40 object-cover" />
            <figcaption class="p-4 flex-1">
              <div class="font-mono text-[11px] font-semibold text-wira-green">MESIN 01</div>
              <div class="font-heading font-bold text-sm text-wira-ink mt-0.5">Cutting &amp; Creasing</div>
              <p class="text-xs text-slate-600 mt-1">Pemotongan lembaran dan pembuatan garis lipatan presisi.</p>
            </figcaption>
          </figure>

          <figure class="bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col">
            <img src="assets/images/machine-2b-auto-folder-glue.png?v=14" alt="Mesin Automatic Folder Glue" class="w-full h-40 object-cover" />
            <figcaption class="p-4 flex-1">
              <div class="font-mono text-[11px] font-semibold text-wira-green">MESIN 02</div>
              <div class="font-heading font-bold text-sm text-wira-ink mt-0.5">Automatic Folder Glue</div>
              <p class="text-xs text-slate-600 mt-1">Pelipatan dan pengeleman kardus otomatis berkecepatan tinggi.</p>
            </figcaption>
          </figure>

          <figure class="bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col">
            <img src="assets/images/machine-3-semi-folder-glue.png?v=14" alt="Mesin Semi Folder Glue" class="w-full h-40 object-cover" />
            <figcaption class="p-4 flex-1">
              <div class="font-mono text-[11px] font-semibold text-wira-green">MESIN 03</div>
              <div class="font-heading font-bold text-sm text-wira-ink mt-0.5">Semi Folder Glue</div>
              <p class="text-xs text-slate-600 mt-1">Pengeleman kardus ukuran besar (<em>jumbo box</em>) &amp; tebal.</p>
            </figcaption>
          </figure>

          <figure class="bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col">
            <img src="assets/images/machine-4-rotary-sloter.png?v=14" alt="Mesin Rotary Sloter" class="w-full h-40 object-cover" />
            <figcaption class="p-4 flex-1">
              <div class="font-mono text-[11px] font-semibold text-wira-green">MESIN 04</div>
              <div class="font-heading font-bold text-sm text-wira-ink mt-0.5">Rotary Sloter</div>
              <p class="text-xs text-slate-600 mt-1">Pembuatan celah (<em>slot</em>) dan penutup kardus tipe RSC/A1.</p>
            </figcaption>
          </figure>

          <figure class="bg-white border border-wira-border rounded-lg overflow-hidden flex flex-col sm:col-span-2 lg:col-span-1">
            <img src="assets/images/machine-5-rotary-die-cut.png?v=14" alt="Mesin Rotary Die Cut" class="w-full h-40 object-cover" />
            <figcaption class="p-4 flex-1">
              <div class="font-mono text-[11px] font-semibold text-wira-green">MESIN 05</div>
              <div class="font-heading font-bold text-sm text-wira-ink mt-0.5">Rotary Die Cut</div>
              <p class="text-xs text-slate-600 mt-1">Pemotongan kardus bentuk khusus (<em>die-cut</em>) &amp; partisi.</p>
            </figcaption>
          </figure>
        </div>

      </div>
    </section>

    <!-- CLIENTS & FAQ -->
    <section id="pelanggan" class="py-14 sm:py-18 bg-white border-t border-wira-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          
          <!-- Left 5 Cols: Client List -->
          <div class="lg:col-span-5">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              Pelanggan Industri Kami
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-5 leading-relaxed">
              Beberapa perusahaan manufaktur yang telah mempercayakan pengadaan kemasan, fabrikasi trolley, dan barang kebutuhan pabrik kepada kami:
            </p>
            <div class="border border-wira-border rounded-lg divide-y divide-wira-border text-xs sm:text-sm font-heading font-semibold text-wira-ink">
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Jaya Refrigeration Equipment (Midea)</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Elektronik &amp; HVAC</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Indorama Ventures</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Petrokimia</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Yasunli Abadi Utama Plastik</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Injeksi Plastik</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Skyworth Industry Indonesia</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Elektronik</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Daijo Industrial</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Komponen Presisi</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Indonesiaiki</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Manufaktur</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Haeng Nam Sejahtera Indonesia</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Tableware</span>
              </div>
              <div class="px-4 py-3 flex items-center justify-between">
                <span>PT. Savindo Karya Perkasa</span>
                <span class="font-mono text-[11px] text-slate-500 font-normal">Industri</span>
              </div>
            </div>
          </div>

          <!-- Right 7 Cols: FAQ -->
          <div class="lg:col-span-7">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              Pertanyaan yang Sering Ditanyakan (FAQ)
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-5 leading-relaxed">
              Informasi praktis seputar pemesanan, pembuatan sample, hingga dokumen pajak.
            </p>

            <div class="space-y-3">
              <details class="group border border-wira-border rounded-lg bg-wira-canvas" open>
                <summary class="flex items-center justify-between cursor-pointer px-5 py-3.5 font-heading font-bold text-sm text-wira-ink">
                  <span>Apakah PT. Wirasena Maju Bersama Rayya memiliki legalitas lengkap &amp; Faktur Pajak?</span>
                  <span class="text-wira-green font-mono text-base group-open:rotate-45 transition-transform">+</span>
                </summary>
                <div class="px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-wira-border pt-3 bg-white rounded-b-lg">
                  Ya. Perusahaan kami memiliki dokumen legalitas lengkap (<strong>NPWP: 96.434.539.2-447.000</strong>) untuk keperluan registrasi vendor di perusahaan Anda, serta melayani pembelian dengan sistem PO dan tempo pembayaran (TOP) sesuai kesepakatan.
                </div>
              </details>

              <details class="group border border-wira-border rounded-lg bg-wira-canvas">
                <summary class="flex items-center justify-between cursor-pointer px-5 py-3.5 font-heading font-bold text-sm text-wira-ink">
                  <span>Bisakah memesan barang teknik yang belum tertulis di halaman katalog?</span>
                  <span class="text-wira-green font-mono text-base group-open:rotate-45 transition-transform">+</span>
                </summary>
                <div class="px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-wira-border pt-3 bg-white rounded-b-lg">
                  Sangat bisa. Kami menerapkan prinsip <strong>"All items are as requested by the buyer"</strong>. Cukup kirimkan daftar nama barang, kode seri/part, atau foto barang lama yang ingin diganti ke WhatsApp atau email <a href="mailto:marketing@wirasenamajubersama.com" class="text-wira-green underline">marketing@wirasenamajubersama.com</a>.
                </div>
              </details>

              <details class="group border border-wira-border rounded-lg bg-wira-canvas">
                <summary class="flex items-center justify-between cursor-pointer px-5 py-3.5 font-heading font-bold text-sm text-wira-ink">
                  <span>Apakah bisa minta sample Carton Box atau Impraboard terlebih dahulu?</span>
                  <span class="text-wira-green font-mono text-base group-open:rotate-45 transition-transform">+</span>
                </summary>
                <div class="px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-wira-border pt-3 bg-white rounded-b-lg">
                  Bisa. Kami menyediakan pembuatan <em>sample</em> boks agar tim QC/Engineering Anda dapat menguji kecocokan ukuran komponen dan kekuatan boks sebelum diproduksi massal.
                </div>
              </details>

              <details class="group border border-wira-border rounded-lg bg-wira-canvas">
                <summary class="flex items-center justify-between cursor-pointer px-5 py-3.5 font-heading font-bold text-sm text-wira-ink">
                  <span>Apakah melayani survei pengukuran ke pabrik untuk pembuatan Trolley?</span>
                  <span class="text-wira-green font-mono text-base group-open:rotate-45 transition-transform">+</span>
                </summary>
                <div class="px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-wira-border pt-3 bg-white rounded-b-lg">
                  Ya. Jika Anda belum memiliki gambar kerja (<em>drawing</em>), tim kami siap datang melakukan pengukuran langsung ke pabrik Anda di area Cikarang, Bekasi, dan sekitarnya.
                </div>
              </details>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>
"""
    return head + nav + body + get_rfq_and_footer()


def build_trading():
    head = get_head(
        "Supplier Barang Electrical, Mechanical, Pneumatik & K3 Cikarang | PT. Wirasena",
        "Supplier pabrik terdekat di Cikarang & Bekasi untuk pengadaan barang Electrical, Mechanical, Komponen Pneumatik, Cutting Tools, APD Safety K3, dan Kain Majun.",
        "supplier-electrical-mechanical.html"
    )
    nav = get_navbar("trading")
    body = """
  <main>
    <section class="bg-wira-canvas border-b border-wira-border py-10 sm:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-xs sm:text-sm font-semibold text-wira-green mb-2">
          Katalog Pengadaan Barang Pabrik (MRO Supply)
        </p>
        <h1 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight max-w-4xl leading-tight">
          Supplier Barang Electrical, Mechanical, Pneumatik &amp; Safety K3
        </h1>
        <p class="text-slate-700 text-sm sm:text-base mt-3 max-w-3xl leading-relaxed">
          Melayani pengadaan suku cadang perawatan mesin (MRO) dan barang habis pakai untuk pabrik di kawasan industri Jababeka, EJIP, MM2100, Lippo Cikarang, Delta Silicon, GIIC Deltamas, hingga Karawang.
        </p>
      </div>
    </section>

    <section class="py-12 sm:py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">

        <!-- 1. Electrical -->
        <div id="electrical" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-12 border-b border-wira-border">
          <div class="lg:col-span-4">
            <div class="bg-wira-canvas border border-wira-border rounded-lg overflow-hidden h-56">
              <img src="assets/images/trading-electrical-mechanical.png?v=14" alt="Supplier Komponen Listrik & Otomasi Pabrik" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              1. Komponen Listrik Industri (Electrical) &amp; Otomasi Panel
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Pengadaan komponen panel kontrol, distribusi daya, dan sensor otomasi mesin sesuai spesifikasi yang diminta.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Proteksi &amp; Switching</th>
                    <td>MCB (1P/3P), MCCB, ELCB, Magnetic Contactor, Thermal Overload Relay (TOR), Fuse &amp; Holder</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Otomasi &amp; Kontrol</th>
                    <td>Unit PLC, Inverter / VFD Drive, Power Supply Switching 24VDC, Timer Relay, Temperature Controller</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Sensor Industri</th>
                    <td>Inductive &amp; Capacitive Proximity Sensor, Photoelectric Sensor, Limit Switch, Rotary Encoder, Thermocouple</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Instalasi &amp; Panel</th>
                    <td>Kabel NYY, NYAF, NYYHY, Kabel Kontrol Shielded, Kabel Duct, Skun Kabel, Push Button, Pilot Lamp LED</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Mechanical -->
        <div id="mechanical" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-12 border-b border-wira-border">
          <div class="lg:col-span-4">
            <div class="bg-wira-canvas border border-wira-border rounded-lg overflow-hidden h-56">
              <img src="assets/images/trading-tools.png?v=14" alt="Supplier Mechanical Sparepart & Cutting Tools" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              2. Suku Cadang Mekanikal, Transmisi &amp; Cutting Tools
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Suplai suku cadang mekanis mesin produksi serta perkakas potong untuk workshop <em>maintenance</em> dan <em>tooling</em>.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Bearing &amp; Unit</th>
                    <td>Deep Groove Ball Bearing, Spherical/Tapered Roller Bearing, Pillow Block (UCP/UCF/UCFL), Linear Motion</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Transmisi Daya</th>
                    <td>V-Belt (Tipe A/B/C/SPZ/SPA/SPB), Timing Belt, Roller Chain (RS40–RS100), Sprocket, Pulley &amp; Coupling</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Cutting Tools</th>
                    <td>Carbide Insert CNC, Endmill Carbide/HSS, Mata Bor (Twist Drill), Tap &amp; Dies, Mata Gerinda Potong/Poles</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Perkakas &amp; Baut</th>
                    <td>Kunci Momen/Torsi, Kaliper Digital/Sigmat, Baut &amp; Mur Baja 8.8 / 10.9 / Stainless SUS 304, Oil Seal &amp; O-Ring</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. Pneumatics & Safety K3 -->
        <div id="pneumatics" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-4">
            <div class="bg-white border border-wira-border rounded-lg p-4 flex items-center justify-center h-56">
              <img src="assets/images/trading-pneumatics.png?v=14" alt="Komponen Pneumatik, Safety K3 & Kain Majun" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              3. Komponen Pneumatik, Safety K3 (APD) &amp; Kain Majun
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Pengadaan sistem pneumatik mesin serta kebutuhan rutin barang habis pakai (<em>consumables</em>) pabrik.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Komponen Pneumatik</th>
                    <td>Silinder Pneumatik, Solenoid Valve, Air Filter Regulator (FRL), Selang PU (4mm–12mm), Fitting One-Touch</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Safety Equipment (K3)</th>
                    <td>Sepatu Safety (Steel Toe), Helm Proyek, Sarung Tangan Katun/Bintik/Nitrile/Las, Masker, Kacamata Safety</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Kain Majun &amp; Wiper</th>
                    <td>Kain Majun Putih &amp; Majun Warna (Jahit Tumpuk / Lembaran Tanpa Sambungan) bersih dan daya serap tinggi</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Lakban &amp; Kemasan</th>
                    <td>OPP Tape Bening/Cokelat, Masking Tape, Double Tape, Lakban Lantai (Floor Marking), Stretch Film Roll</td>
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
    return head + nav + body + get_rfq_and_footer()


def build_packaging():
    head = get_head(
        "Pabrik Carton Box Custom & Impraboard Box Cikarang Bekasi | PT. Wirasena",
        "Produsen Corrugated Carton Box Custom (Single, Double, Triple Wall), Box Impraboard (PP Corrugated) Sekat Partisi, dan Synthetic Rubber di Cikarang.",
        "pabrik-carton-box-impraboard.html"
    )
    nav = get_navbar("packaging")
    body = """
  <main>
    <section class="bg-wira-canvas border-b border-wira-border py-10 sm:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-xs sm:text-sm font-semibold text-wira-green mb-2">
          Katalog Produksi Kemasan Industri (In-House Manufacturing)
        </p>
        <h1 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight max-w-4xl leading-tight">
          Pabrik Corrugated Carton Box Custom, Box Impraboard &amp; Synthetic Rubber
        </h1>
        <p class="text-slate-700 text-sm sm:text-base mt-3 max-w-3xl leading-relaxed">
          Didukung 5 unit mesin produksi kardus di workshop Cikarang Selatan, kami memproduksi kemasan <em>Corrugated Carton Box</em> dan <em>PP Corrugated (Impraboard) Box</em> sesuai ukuran dan standar beban tumpuk pabrik Anda.
        </p>
      </div>
    </section>

    <section class="py-12 sm:py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">

        <!-- 1. Carton Box -->
        <div id="carton-box" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-12 border-b border-wira-border">
          <div class="lg:col-span-4">
            <div class="bg-wira-canvas border border-wira-border rounded-lg overflow-hidden h-60">
              <img src="assets/images/product-carton-box.png?v=14" alt="Pabrik Carton Box Custom Cikarang" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              1. Spesifikasi Corrugated Carton Box Custom
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Diproduksi menggunakan mesin <em>Cutting &amp; Creasing, Automatic/Semi Folder Glue, Rotary Sloter</em>, dan <em>Rotary Die Cut</em> milik sendiri.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Konstruksi Dinding</th>
                    <td><strong>Single Wall</strong> (3 Ply), <strong>Double Wall</strong> (5 Ply), <strong>Triple Wall</strong> (7 Ply untuk kargo berat/ekspor)</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Tipe Gelombang (Flute)</th>
                    <td>B-Flute (~3mm), C-Flute (~4mm), E-Flute (~1.5mm), serta kombinasi CB-Flute / EB-Flute</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Komposisi Kertas</th>
                    <td>Kraft Liner (K125, K150, K200, K275) &amp; Corrugating Medium (M125, M150) sesuai kebutuhan beban</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Model &amp; Aksesoris</th>
                    <td>Boks A1 (RSC), Die-Cut Box, Top-Bottom Box, Partisi/Sekat Kardus, Layer Pad, Cetak Flexo 1–3 Warna</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Impraboard -->
        <div id="impraboard" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-12 border-b border-wira-border">
          <div class="lg:col-span-4">
            <div class="bg-white border border-wira-border rounded-lg p-4 flex items-center justify-center h-60">
              <img src="assets/images/product-impraboard-box.png?v=14" alt="Pabrik Impraboard Box & Sekat Partisi" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              2. Spesifikasi Box Impraboard (PP Corrugated) &amp; Partisi
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Solusi wadah plastik berongga (<em>returnable packaging</em>) yang tahan air, awet untuk sirkulasi ratusan siklus, dan melindungi komponen dari gesekan.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Ketebalan Lembaran</th>
                    <td>Polypropylene (PP) Hollow Sheet 2mm, 3mm, 4mm, 5mm, hingga 6mm</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Sekat / Partition</th>
                    <td>Partisi interlocking presisi (bisa dilapisi EVA Foam / Kain Spunbond untuk komponen sensitif goresan)</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Penguat &amp; Aksesoris</th>
                    <td>Rangka kawat baja (Wire Frame), Siku Corner Plastik untuk <em>stacking</em>, Handle Grip, Label Holder, Velcro</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Pilihan Warna &amp; ESD</th>
                    <td>Biru, Hitam (tersedia varian Anti-Static / Conductive ESD), Abu-abu, Kuning, Hijau, Merah, Putih</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. Synthetic Rubber -->
        <div id="rubber-tape" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-4">
            <div class="bg-white border border-wira-border rounded-lg p-4 flex items-center justify-center h-60">
              <img src="assets/images/product-masking-tape.png?v=14" alt="Synthetic Rubber & Industrial Tape" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              3. Synthetic Rubber Pad, EVA Sponge &amp; Lakban Industri
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Bantalan karet sintetis peredam getaran dan busa pelindung kemasan yang dipotong presisi (<em>custom die-cut</em>).
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Material Rubber</th>
                    <td>Synthetic Rubber Sheet/Pad, EPDM Sponge, Neoprene, Nitrile Rubber (NBR) tahan oli &amp; panas</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Material Cushioning</th>
                    <td>EVA Foam / EVA Sponge (berbagai tingkat kekerasan/density), PE Foam Sheet &amp; Roll</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Industrial Tapes</th>
                    <td>Masking Tape, Double Tape Tissue/Foam, OPP Tape Packaging, Cloth Tape &amp; Floor Marking Tape</td>
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
    return head + nav + body + get_rfq_and_footer()


def build_fabrikasi():
    head = get_head(
        "Jasa Fabrikasi Storage Trolley, Rak Pipa FIFO & Las Cikarang | PT. Wirasena",
        "Bengkel fabrikasi logam di Cikarang & Bekasi untuk pembuatan Storage Trolley Stainless Steel / Besi Hollow, Rak Pipa FIFO, Meja Kerja, dan Fence Welding.",
        "jasa-fabrikasi-trolley.html"
    )
    nav = get_navbar("fabrikasi")
    body = """
  <main>
    <section class="bg-wira-canvas border-b border-wira-border py-10 sm:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-xs sm:text-sm font-semibold text-wira-green mb-2">
          Katalog Bengkel Fabrikasi Logam &amp; Pengelasan Industri
        </p>
        <h1 class="font-heading text-2xl sm:text-4xl font-extrabold text-wira-ink tracking-tight max-w-4xl leading-tight">
          Jasa Fabrikasi Storage Trolley, Rak Pipa FIFO &amp; Pengelasan Pabrik
        </h1>
        <p class="text-slate-700 text-sm sm:text-base mt-3 max-w-3xl leading-relaxed">
          Mengerjakan fabrikasi unit <em>material handling</em> dan perlengkapan lantai produksi sesuai gambar kerja (<em>engineering drawing</em>) atau hasil pengukuran tim kami di pabrik Anda.
        </p>
      </div>
    </section>

    <section class="py-12 sm:py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">

        <!-- 1. Storage Trolley -->
        <div id="storage-trolley" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-12 border-b border-wira-border">
          <div class="lg:col-span-4">
            <div class="bg-white border border-wira-border rounded-lg p-4 flex items-center justify-center h-60">
              <img src="assets/images/fabrication-trolley-blue.png?v=14" alt="Fabrikasi Storage Trolley Stainless & Besi" class="max-h-full max-w-full object-contain" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              1. Spesifikasi Fabrikasi Storage Trolley &amp; Parts Trolley
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Dirancang khusus untuk mempermudah pemindahan komponen WIP (<em>Work in Process</em>) dari gudang ke lini perakitan dengan aman dan ergonomis.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Material Rangka</th>
                    <td><strong>Stainless Steel</strong> (SUS 304 / SUS 201 anti-karat) atau <strong>Mild Steel</strong> (Besi Hollow, Pipa, Siku, Plat)</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Finishing Permukaan</th>
                    <td>Cat Oven <em>Powder Coating</em>, Cat Duco Epoxy Industrial (warna sesuai standar 5S pabrik), atau Poles Mirror/Hairline</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Spesifikasi Roda</th>
                    <td>Heavy-Duty Caster Polyurethane (PU), Nylon, atau Rubber ukuran 4&quot;, 5&quot;, 6&quot;, hingga 8&quot; (2 Hidup + 2 Rem)</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Kustomisasi Fitur</th>
                    <td>Lapisan EVA Sponge/Karet pada ambalan, Pintu Kawat Mesh, Cantolan <em>Towing Bar</em> kereta tarik pabrik</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. Welding & FIFO -->
        <div id="welding-fifo" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-4">
            <div class="bg-wira-canvas border border-wira-border rounded-lg overflow-hidden h-60">
              <img src="assets/images/fabrication-welding.png?v=14" alt="Jasa Las Industri, Rak FIFO & Fence Welding" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="lg:col-span-8">
            <h2 class="font-heading text-xl sm:text-2xl font-bold text-wira-ink">
              2. Rak Pipa FIFO, Meja Kerja Produksi &amp; Fence Welding
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1.5 mb-4">
              Pengerjaan konstruksi las presisi (MIG, TIG/Argon, SMAW) untuk fasilitas keselamatan dan efisiensi tata letak pabrik.
            </p>
            <div class="border border-wira-border rounded-lg overflow-hidden">
              <table class="w-full text-xs sm:text-sm spec-table">
                <tbody>
                  <tr>
                    <th class="w-1/3 bg-wira-stone/50 font-semibold text-wira-ink">Rak Aliran FIFO</th>
                    <td>Fabrikasi rak <em>First-In First-Out</em> menggunakan <em>placon roller track</em> untuk kelancaran sirkulasi boks Impraboard</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Meja Kerja (Workstation)</th>
                    <td>Meja perakitan (<em>assembly table</em>), meja inspeksi QC dengan gantungan lampu kerja dan alas karet anti-statis (ESD)</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Fence Welding</th>
                    <td>Pembuatan pagar pengaman mesin/robot (<em>safety machine guarding</em>), partisi kawat <em>wiremesh</em>, dan pembatas jalur forklift</td>
                  </tr>
                  <tr>
                    <th class="bg-wira-stone/50 font-semibold text-wira-ink">Layanan Rekondisi</th>
                    <td>Jasa perbaikan pengelasan, pengecatan ulang, dan penggantian roda caster untuk unit trolley lama di pabrik Anda</td>
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
    return head + nav + body + get_rfq_and_footer()


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
    print("Successfully built v10 website locally (No Panduan Buyer, Visual Product Catalog, 100% Verified Images)!")


if __name__ == "__main__":
    main()

