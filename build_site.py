#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static Site Generator for PT. Wirasena Maju Bersama Rayya
Visual Architecture: Authentic B2B Corporate Industrial Design (Trimitra Packaging Cikarang style)
SEO Architecture: Multi-Page Keyword-Targeted Landing Pages + Schema.org @graph + Buyer Search Psychology
"""

import os

BASE_DIR = "/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya"


def render_head(title, description, keywords, canonical_file, extra_schema=""):
    canonical_url = f"https://wirasenamajubersama.com/{canonical_file}" if canonical_file != "index.html" else "https://wirasenamajubersama.com/"
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
  <meta property="og:site_name" content="PT. Wirasena Maju Bersama Rayya — Supplier Kebutuhan Pabrik &amp; Carton Box Cikarang" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="assets/social-media-kit/banner-facebook-cover.png?v=5" />

  <link rel="icon" type="image/png" href="assets/images/logo-avatar.png?v=5" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            heading: ['Montserrat', 'sans-serif'],
            sans: ['"Open Sans"', 'sans-serif']
          }},
          colors: {{
            tmc: {{
              navy: '#1B2559',
              navyDark: '#131B42',
              green: '#61B836',
              greenDark: '#4E9A28',
              charcoal: '#4A4A4A',
              lightGray: '#F7F8F9'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    .section-line-title {{
      display: flex;
      align-items: center;
      text-align: center;
      color: #4A4A4A;
    }}
    .section-line-title::before,
    .section-line-title::after {{
      content: '';
      flex: 1;
      border-bottom: 1px solid #E2E5E9;
    }}
    .section-line-title:not(:empty)::before {{
      margin-right: 2rem;
    }}
    .section-line-title:not(:empty)::after {{
      margin-left: 2rem;
    }}
    .wa-doodle-bg {{
      background-color: #E5DDD5;
      background-image: radial-gradient(#CFC7BE 1px, transparent 1px), radial-gradient(#CFC7BE 1px, #E5DDD5 1px);
      background-size: 24px 24px;
      background-position: 0 0, 12px 12px;
    }}
  </style>

  <!-- JSON-LD @graph Structured Data for Google Rich Results -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": ["LocalBusiness", "Organization"],
        "@id": "https://wirasenamajubersama.com/#organization",
        "name": "PT. Wirasena Maju Bersama Rayya",
        "alternateName": [
          "WMB Cikarang",
          "Supplier Kebutuhan Pabrik Cikarang Bekasi",
          "Pabrik Carton Box & Impraboard Cikarang",
          "Supplier Electrical Mechanical Pabrik Bekasi"
        ],
        "url": "https://wirasenamajubersama.com",
        "logo": "https://wirasenamajubersama.com/assets/images/logo-trans.png",
        "image": "https://wirasenamajubersama.com/assets/images/hero-banner-1.jpg",
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
        "areaServed": ["Cikarang Selatan", "Cikarang Pusat", "Cikarang Barat", "Cikarang Utara", "MM2100", "Jababeka", "EJIP", "Delta Silicon", "Lippo Cikarang", "Bekasi", "Karawang"],
        "contactPoint": [
          {{
            "@type": "ContactPoint",
            "telephone": "+62-21-84990200",
            "contactType": "customer service",
            "email": "info@wirasenamajubersama.com",
            "availableLanguage": ["Indonesian", "English"]
          }},
          {{
            "@type": "ContactPoint",
            "telephone": "+62-21-84990200",
            "contactType": "sales",
            "email": "marketing@wirasenamajubersama.com",
            "availableLanguage": ["Indonesian", "English"]
          }},
          {{
            "@type": "ContactPoint",
            "telephone": "+62-21-84990200",
            "contactType": "technical support",
            "email": "quality@wirasenamajubersama.com",
            "availableLanguage": ["Indonesian"]
          }},
          {{
            "@type": "ContactPoint",
            "telephone": "+62-21-84990200",
            "contactType": "package tracking",
            "email": "delivery@wirasenamajubersama.com",
            "availableLanguage": ["Indonesian"]
          }}
        ]
      }}{extra_schema}
    ]
  }}
  </script>
</head>
"""


def render_navbar(active_page="index.html"):
    def nav_style(page):
        if active_page == page:
            return "text-tmc-navy font-bold border-b-2 border-tmc-green pb-1"
        return "text-[#333333] hover:text-tmc-green font-semibold transition"

    prod_active = "text-tmc-navy font-bold border-b-2 border-tmc-green pb-1" if active_page in [
        "pabrik-carton-box-impraboard.html",
        "supplier-electrical-mechanical.html",
        "jasa-fabrikasi-trolley.html",
    ] else "text-[#333333] hover:text-tmc-green font-semibold transition"

    return f"""<body class="bg-white text-[#4A4A4A] font-sans antialiased overflow-x-hidden">

  <!-- Clean White Corporate Header (Trimitra Cikarang Style) -->
  <header class="w-full sticky top-0 z-50 bg-white shadow-[0_2px_10px_rgba(0,0,0,0.06)]">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 h-20 sm:h-24 flex items-center justify-between">
      
      <!-- Left: Corporate Brand Logo (tmc / wmb horizontal style) -->
      <a href="index.html" class="flex items-center gap-3 group shrink-0">
        <img src="assets/images/logo-trans.png?v=5" alt="PT. Wirasena Maju Bersama Rayya - Supplier Pabrik Cikarang" class="h-12 sm:h-14 w-auto object-contain" />
        <div class="flex flex-col leading-none">
          <div class="flex items-baseline tracking-tight font-heading">
            <span class="text-2xl sm:text-[32px] font-extrabold text-tmc-navy">wmb</span>
            <span class="text-2xl sm:text-[32px] font-light text-tmc-green ml-0.5">rayya</span>
          </div>
          <span class="text-[11px] sm:text-[13px] font-medium text-tmc-green tracking-wide -mt-0.5">wirasena cikarang</span>
        </div>
      </a>

      <!-- Right: Search Icon + Clean Uppercase Menu Links -->
      <div class="hidden lg:flex items-center gap-7 text-[13px] font-heading tracking-wide uppercase">
        <button onclick="toggleSearchModal()" title="Cari Barang Kebutuhan Pabrik" class="text-[#333333] hover:text-tmc-green p-1.5 transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/>
          </svg>
        </button>

        <a href="index.html" class="{nav_style('index.html')}">HOME</a>
        <a href="index.html#tentang-kami" class="text-[#333333] hover:text-tmc-green font-semibold transition">TENTANG KAMI</a>

        <!-- Dropdown PRODUK KAMI -->
        <div class="relative group py-6">
          <button class="{prod_active} flex items-center gap-1.5 uppercase">
            <span>PRODUK KAMI</span>
            <svg class="w-3.5 h-3.5 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/>
            </svg>
          </button>
          <div class="absolute left-0 top-full w-72 bg-white shadow-xl border-t-2 border-tmc-green py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-150 z-50">
            <a href="pabrik-carton-box-impraboard.html" class="block px-5 py-2.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:text-tmc-green border-b border-gray-100">
              CARTON BOX &amp; PACKAGING
            </a>
            <a href="pabrik-carton-box-impraboard.html#impraboard" class="block px-5 py-2.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:text-tmc-green border-b border-gray-100">
              IMPRABOARD BOX &amp; PARTISI
            </a>
            <a href="supplier-electrical-mechanical.html" class="block px-5 py-2.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:text-tmc-green border-b border-gray-100">
              ELECTRICAL &amp; MECHANICAL PABRIK
            </a>
            <a href="supplier-electrical-mechanical.html#pneumatics" class="block px-5 py-2.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:text-tmc-green border-b border-gray-100">
              PNEUMATICS &amp; SAFETY K3
            </a>
            <a href="jasa-fabrikasi-trolley.html" class="block px-5 py-2.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:text-tmc-green">
              STORAGE TROLLEY &amp; FABRIKASI LAS
            </a>
          </div>
        </div>

        <a href="artikel-seo.html" class="{nav_style('artikel-seo.html')}">INFO</a>
        <a href="#kontak-kami" class="text-[#333333] hover:text-tmc-green font-semibold transition">KONTAK KAMI</a>
      </div>

      <!-- Mobile Hamburger & Search -->
      <div class="flex items-center gap-2 lg:hidden">
        <button onclick="toggleSearchModal()" aria-label="Cari Produk" class="p-2 text-gray-700 hover:text-tmc-green">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/>
          </svg>
        </button>
        <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" aria-label="Menu" class="p-2 text-gray-700 hover:text-tmc-green">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Dropdown Navigation -->
    <div id="mobile-menu" class="hidden lg:hidden bg-white border-t border-gray-200 px-6 py-4 space-y-2.5 font-heading text-xs uppercase tracking-wider">
      <a href="index.html" class="block py-2 font-bold text-tmc-navy border-b border-gray-100">HOME</a>
      <a href="index.html#tentang-kami" class="block py-2 font-semibold text-gray-700 border-b border-gray-100">TENTANG KAMI</a>
      <div class="py-1 border-b border-gray-100">
        <span class="block text-[11px] font-bold text-tmc-green mb-1.5">PRODUK KAMI:</span>
        <a href="pabrik-carton-box-impraboard.html" class="block py-1.5 pl-3 text-gray-600 hover:text-tmc-green">• Carton Box &amp; Impraboard</a>
        <a href="supplier-electrical-mechanical.html" class="block py-1.5 pl-3 text-gray-600 hover:text-tmc-green">• Electrical, Mechanical &amp; Pneumatics</a>
        <a href="jasa-fabrikasi-trolley.html" class="block py-1.5 pl-3 text-gray-600 hover:text-tmc-green">• Storage Trolley &amp; Fabrikasi Las</a>
      </div>
      <a href="artikel-seo.html" class="block py-2 font-semibold text-gray-700 border-b border-gray-100">INFO &amp; ARTIKEL</a>
      <a href="#kontak-kami" class="block py-2 font-semibold text-gray-700">KONTAK KAMI</a>
    </div>
  </header>

  <!-- Search Modal Overlay (Activated by Search Icon in Navbar) -->
  <div id="search-modal" class="hidden fixed inset-0 z-50 bg-black/60 flex items-start justify-center pt-24 px-4">
    <div class="bg-white w-full max-w-2xl rounded-lg shadow-2xl overflow-hidden border border-gray-200">
      <div class="p-4 sm:p-5 flex items-center justify-between border-b border-gray-100">
        <span class="font-heading text-xs font-bold uppercase tracking-wider text-tmc-navy">Cari Produk / Kebutuhan Pabrik</span>
        <button onclick="toggleSearchModal()" class="text-gray-400 hover:text-gray-700 text-xl font-bold leading-none">&times;</button>
      </div>
      <div class="p-5">
        <input id="global-search-input" type="text" oninput="filterGlobalCatalog(this.value)" placeholder="Ketik barang yang dicari (contoh: carton box, impraboard, sensor, bearing, pneumatic, trolley, majun)..." class="w-full border border-gray-300 rounded px-4 py-3 text-sm focus:outline-none focus:border-tmc-green" />
        <div id="global-search-results" class="mt-4 max-h-64 overflow-y-auto divide-y divide-gray-100 text-sm">
          <a href="pabrik-carton-box-impraboard.html" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="carton box kardus karton boks single double triple wall die cut kemasan">
            <span class="font-semibold text-gray-800">Carton Box Custom &amp; Die Cut Box</span>
            <span class="text-xs text-tmc-green font-semibold">Packaging →</span>
          </a>
          <a href="pabrik-carton-box-impraboard.html#impraboard" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="impraboard box plastik berongga pp corrugated sekat partisi esd antistatic">
            <span class="font-semibold text-gray-800">Impraboard Box &amp; Sekat Partisi Custom</span>
            <span class="text-xs text-tmc-green font-semibold">Packaging →</span>
          </a>
          <a href="supplier-electrical-mechanical.html" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="electrical alat listrik industri plc sensor inverter mcb contactor relay kabel panel">
            <span class="font-semibold text-gray-800">Alat Listrik Industri (PLC, Sensor, Inverter, Contactor, MCB)</span>
            <span class="text-xs text-tmc-green font-semibold">Electrical →</span>
          </a>
          <a href="supplier-electrical-mechanical.html#mechanical" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="mechanical sparepart mesin bearing v-belt pulley gearbox dinamo roller conveyor cutting tools">
            <span class="font-semibold text-gray-800">Sparepart Mechanical (Bearing, V-Belt, Gearbox, Cutting Tools)</span>
            <span class="text-xs text-tmc-green font-semibold">Mechanical →</span>
          </a>
          <a href="supplier-electrical-mechanical.html#pneumatics" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="pneumatic solenoid valve air cylinder fitting selang pu frl safety k3 sarung tangan kain majun">
            <span class="font-semibold text-gray-800">Komponen Pneumatics, Safety K3 &amp; Kain Majun Pabrik</span>
            <span class="text-xs text-tmc-green font-semibold">General Supply →</span>
          </a>
          <a href="jasa-fabrikasi-trolley.html" class="search-item flex items-center justify-between py-2.5 px-2 hover:bg-gray-50" data-keywords="fabrikasi storage trolley stainless besi rak pipa fifo meja kerja las welding pagar mesin">
            <span class="font-semibold text-gray-800">Jasa Fabrikasi Storage Trolley, Rak FIFO &amp; Welding</span>
            <span class="text-xs text-tmc-green font-semibold">Fabrikasi →</span>
          </a>
        </div>
      </div>
    </div>
  </div>
"""


def render_footer_and_wa():
    return """
  <!-- Kontak & Form Penawaran Cepat (Sebelum Footer Hijau) -->
  <section id="kontak-kami" class="py-16 bg-[#F7F8F9] border-t border-gray-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="mb-12">
        <h2 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
          KONTAK KAMI
        </h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        <!-- Info Alamat & 4 Email Divisi -->
        <div class="lg:col-span-6 space-y-6">
          <div>
            <h3 class="font-heading text-lg font-bold text-tmc-navy uppercase tracking-wide">
              PT. WIRASENA MAJU BERSAMA RAYYA
            </h3>
            <p class="text-sm text-gray-600 mt-2 leading-relaxed">
              General Supplier Kebutuhan Pabrik (Electrical, Mechanical, Pneumatics, Safety K3), Produsen Carton Box &amp; Impraboard Custom, serta Jasa Fabrikasi Trolley Industri di Cikarang Selatan, Kabupaten Bekasi.
            </p>
          </div>

          <div class="bg-white p-6 border border-gray-200 shadow-sm space-y-3 text-sm">
            <p class="text-gray-700">
              <strong class="text-tmc-navy font-heading uppercase text-xs block mb-0.5">Alamat Pabrik &amp; Workshop:</strong>
              Jl. Bah Kilong Kp. Kandang, RT.004 RW.002, Desa Sukadami, Kec. Cikarang Selatan, Kabupaten Bekasi, Jawa Barat 17530
            </p>
            <p class="text-gray-700">
              <strong class="text-tmc-navy font-heading uppercase text-xs block mb-0.5">Telepon / Fax Kantor:</strong>
              <a href="tel:02184990200" class="hover:text-tmc-green font-semibold">(021) 8499 0200</a> &nbsp;|&nbsp; NPWP: 96.434.539.2-447.000
            </p>
          </div>

          <!-- 4 Email Resmi Divisi -->
          <div class="bg-white p-6 border border-gray-200 shadow-sm">
            <h4 class="font-heading text-xs font-bold uppercase tracking-wider text-tmc-navy mb-3">
              Alamat Email Resmi Per Divisi:
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <a href="mailto:info@wirasenamajubersama.com" class="p-3 border border-gray-200 hover:border-tmc-green transition block">
                <span class="text-[10px] font-bold uppercase text-gray-400 block">1. Email Utama Perusahaan</span>
                <span class="font-bold text-tmc-navy">info@wirasenamajubersama.com</span>
              </a>
              <a href="mailto:marketing@wirasenamajubersama.com?subject=Permintaan%20Penawaran%20Harga%20(RFQ)%20-%20PT.%20Wirasena%20Maju%20Bersama%20Rayya" class="p-3 border border-gray-200 hover:border-tmc-green transition block">
                <span class="text-[10px] font-bold uppercase text-tmc-green block">2. Divisi Marketing &amp; RFQ</span>
                <span class="font-bold text-tmc-navy">marketing@wirasenamajubersama.com</span>
              </a>
              <a href="mailto:quality@wirasenamajubersama.com" class="p-3 border border-gray-200 hover:border-tmc-green transition block">
                <span class="text-[10px] font-bold uppercase text-gray-400 block">3. Divisi Quality Control (QC)</span>
                <span class="font-bold text-tmc-navy">quality@wirasenamajubersama.com</span>
              </a>
              <a href="mailto:delivery@wirasenamajubersama.com" class="p-3 border border-gray-200 hover:border-tmc-green transition block">
                <span class="text-[10px] font-bold uppercase text-gray-400 block">4. Divisi Pengiriman (Delivery)</span>
                <span class="font-bold text-tmc-navy">delivery@wirasenamajubersama.com</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Google Maps Embed Cikarang Selatan -->
        <div class="lg:col-span-6 bg-white p-3 border border-gray-200 shadow-sm">
          <iframe
            title="Lokasi Pabrik PT. Wirasena Maju Bersama Rayya Cikarang Selatan"
            src="https://www.google.com/maps?q=-6.3425,107.1264&hl=id&z=14&output=embed"
            class="w-full h-[360px] border-0"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </div>
  </section>

  <!-- SOLID GREEN CORPORATE FOOTER (Exact Trimitra Cikarang Style) -->
  <footer class="bg-tmc-green text-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8 py-14">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-10 items-start">
        
        <!-- Column 1: White Logo + Certification/Commitment Box -->
        <div class="md:col-span-5 flex flex-col items-start">
          <div class="flex items-center gap-3.5 mb-5">
            <img src="assets/images/logo-footer-white.png?v=5" alt="PT. Wirasena Maju Bersama Rayya" class="h-16 w-auto object-contain" />
            <div class="leading-none">
              <div class="font-heading text-3xl font-extrabold tracking-tight text-white">
                wmb <span class="font-light">rayya</span>
              </div>
              <span class="text-xs tracking-wider text-white/90">wirasena cikarang</span>
            </div>
          </div>

          <!-- Bordered Quality Box (Matches Trimitra ISO/Sedex Box) -->
          <div class="border border-white/80 px-5 py-4 max-w-xs">
            <div class="text-[10px] font-heading uppercase tracking-widest text-white/90 mb-2 text-center">
              — OUR QUALITY COMMITMENT —
            </div>
            <div class="flex items-center justify-between gap-4 border-t border-white/40 pt-2.5">
              <div class="text-center">
                <span class="font-heading font-extrabold text-sm block">BEST QUALITY</span>
                <span class="text-[10px] text-white/85">QC Terstandarisasi</span>
              </div>
              <div class="h-8 w-px bg-white/40"></div>
              <div class="text-center">
                <span class="font-heading font-extrabold text-sm block">ON TIME</span>
                <span class="text-[10px] text-white/85">Delivery Kawasan</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Column 2: Company Name & Address -->
        <div class="md:col-span-4 text-sm">
          <h3 class="font-heading font-bold text-base uppercase tracking-wider text-white">
            PT. WIRASENA MAJU BERSAMA RAYYA
          </h3>
          <div class="w-10 h-0.5 bg-white my-3"></div>
          <p class="leading-relaxed text-white/95">
            Jl. Bah Kilong Kp. Kandang, RT.004/002, Desa Sukadami, Kec. Cikarang Selatan, Bekasi, Jawa Barat 17530
          </p>
          <p class="mt-3 text-white/95">
            Telp/Fax: (021) 8499 0200<br />
            Email: marketing@wirasenamajubersama.com
          </p>
        </div>

        <!-- Column 3: CONNECT WITH US Social Circles -->
        <div class="md:col-span-3">
          <h3 class="font-heading font-bold text-base uppercase tracking-wider text-white">
            CONNECT WITH US:
          </h3>
          <div class="w-10 h-0.5 bg-white my-3"></div>
          <div class="flex items-center gap-3.5 mt-4">
            <!-- Instagram -->
            <a href="social-preview.html" title="Instagram PT. Wirasena Maju Bersama Rayya" class="w-11 h-11 rounded-full bg-white text-tmc-green hover:scale-105 transition flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
            <!-- WhatsApp -->
            <button onclick="toggleWaWidget()" title="WhatsApp Business PT. Wirasena Maju Bersama Rayya" class="w-11 h-11 rounded-full bg-white text-tmc-green hover:scale-105 transition flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
              </svg>
            </button>
            <!-- LinkedIn -->
            <a href="social-preview.html" title="LinkedIn PT. Wirasena Maju Bersama Rayya" class="w-11 h-11 rounded-full bg-white text-tmc-green hover:scale-105 transition flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
            </a>
            <!-- Email -->
            <a href="mailto:marketing@wirasenamajubersama.com" title="Email Marketing PT. Wirasena Maju Bersama Rayya" class="w-11 h-11 rounded-full bg-white text-tmc-green hover:scale-105 transition flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
            </a>
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom Dark Charcoal Copyright Bar -->
    <div class="bg-[#4A4A4A] text-white/90 py-3.5 text-xs">
      <div class="max-w-6xl mx-auto px-4 sm:px-8 flex flex-col sm:flex-row items-center justify-between gap-2">
        <p>Copyright 2026 &copy; <strong>PT. Wirasena Maju Bersama Rayya</strong></p>
        <div class="flex items-center gap-4 text-[11px] text-gray-300">
          <a href="pabrik-carton-box-impraboard.html" class="hover:text-white">Carton Box</a>
          <span>|</span>
          <a href="supplier-electrical-mechanical.html" class="hover:text-white">Electrical &amp; Mechanical</a>
          <span>|</span>
          <a href="jasa-fabrikasi-trolley.html" class="hover:text-white">Fabrikasi Trolley</a>
          <span>|</span>
          <a href="social-preview.html" class="hover:text-white">Preview Kit Sosmed</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- AUTHENTIC WHATSAPP CHAT POPUP WIDGET (Matches Trimitra Screenshot 1-4!) -->
  <div class="fixed bottom-5 right-5 z-50 flex flex-col items-end">
    <!-- Popup Box (Open by default on desktop or toggled) -->
    <div id="wa-chat-box" class="w-[300px] sm:w-[320px] rounded-lg shadow-[0_8px_30px_rgba(0,0,0,0.22)] overflow-hidden mb-3 border border-gray-200">
      <!-- Top Dark Teal WA Header -->
      <div class="bg-[#095E54] text-white px-4 py-3 flex items-center justify-between">
        <span class="font-sans text-sm font-semibold tracking-wide">Wirasena Cikarang</span>
        <button onclick="toggleWaWidget()" aria-label="Tutup Chat" class="text-white/80 hover:text-white text-lg leading-none font-bold">&times;</button>
      </div>
      <!-- Middle WA Doodle Pattern + Incoming Green Bubble -->
      <div class="wa-doodle-bg px-4 py-6 min-h-[150px] flex flex-col justify-start">
        <div class="bg-[#DCF8C6] text-[#303030] text-[13px] px-3.5 py-2.5 rounded-lg rounded-tl-none shadow-sm max-w-[85%] leading-snug">
          Chat dengan Tim Kami Segera
        </div>
      </div>
      <!-- Bottom White Bar with Green Pill Button -->
      <div class="bg-white px-4 py-3">
        <a href="https://wa.me/622184990200?text=Halo%20Tim%20Marketing%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20minta%20penawaran%20harga%20(RFQ)%20kebutuhan%20pabrik:" target="_blank" rel="noopener" class="w-full bg-[#2AD466] hover:bg-[#22b855] text-white font-semibold text-xs py-2.5 px-4 rounded-full flex items-center justify-center gap-2 shadow-sm transition">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771z"/>
          </svg>
          <span>WhatsApp Us</span>
        </a>
      </div>
    </div>

    <!-- Floating Round Green WA Button -->
    <button onclick="toggleWaWidget()" aria-label="Buka WhatsApp" class="w-14 h-14 rounded-full bg-[#25D366] hover:bg-[#20b858] text-white shadow-xl flex items-center justify-center transition transform hover:scale-105">
      <svg class="w-8 h-8 fill-current" viewBox="0 0 24 24">
        <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
      </svg>
    </button>
  </div>

  <!-- Interactive Scripts (Hero Slider, Search Modal, Machine Tour Modal, WA Toggle) -->
  <script>
    function toggleWaWidget() {
      const box = document.getElementById('wa-chat-box');
      if (box) box.classList.toggle('hidden');
    }

    function toggleSearchModal() {
      const modal = document.getElementById('search-modal');
      if (!modal) return;
      modal.classList.toggle('hidden');
      if (!modal.classList.contains('hidden')) {
        setTimeout(() => {
          const inp = document.getElementById('global-search-input');
          if (inp) inp.focus();
        }, 50);
      }
    }

    function filterGlobalCatalog(query) {
      const q = (query || '').toLowerCase().trim();
      const items = document.querySelectorAll('.search-item');
      items.forEach(item => {
        const kw = (item.getAttribute('data-keywords') || '') + ' ' + item.innerText.toLowerCase();
        item.style.display = (!q || kw.includes(q)) ? 'flex' : 'none';
      });
    }

    // Full-Bleed Hero Slider Logic
    let currentSlide = 0;
    function showSlide(index) {
      const slides = document.querySelectorAll('.hero-slide');
      const dots = document.querySelectorAll('.hero-dot');
      if (!slides.length) return;
      currentSlide = (index + slides.length) % slides.length;
      slides.forEach((s, i) => {
        if (i === currentSlide) {
          s.classList.remove('opacity-0', 'pointer-events-none');
          s.classList.add('opacity-100');
        } else {
          s.classList.add('opacity-0', 'pointer-events-none');
          s.classList.remove('opacity-100');
        }
      });
      dots.forEach((d, i) => {
        d.className = i === currentSlide
          ? 'hero-dot w-3 h-3 rounded-full bg-tmc-green transition'
          : 'hero-dot w-3 h-3 rounded-full bg-white/60 hover:bg-white transition';
      });
    }

    function nextSlide() { showSlide(currentSlide + 1); }
    function prevSlide() { showSlide(currentSlide - 1); }

    document.addEventListener('DOMContentLoaded', () => {
      if (document.querySelectorAll('.hero-slide').length > 1) {
        setInterval(nextSlide, 5500);
      }
    });

    // Company Profile Video-Style Interactive Machine Tour
    const machineSlides = [
      { img: 'assets/images/machine-1-cutting-creasing.png', title: '1/5 — Cutting & Creasing Machine (Produksi Carton Box Presisi)' },
      { img: 'assets/images/machine-2b-auto-folder-glue.png', title: '2/5 — Automatic Folder Glue Machine (Kecepatan Tinggi)' },
      { img: 'assets/images/machine-3-semi-folder-glue.png', title: '3/5 — Semi Folder Glue Machine (Custom Box Skala Industri)' },
      { img: 'assets/images/machine-4-rotary-sloter.png', title: '4/5 — Rotary Sloter Machine (Slotting & Scoring Kardus Pabrik)' },
      { img: 'assets/images/machine-5-rotary-die-cut.png', title: '5/5 — Rotary Die Cut Machine (Die-Cut Box Presisi Tinggi)' }
    ];
    let machineIdx = 0;
    function cycleMachineTour() {
      machineIdx = (machineIdx + 1) % machineSlides.length;
      const imgEl = document.getElementById('cp-tour-img');
      const capEl = document.getElementById('cp-tour-caption');
      if (imgEl && capEl) {
        imgEl.src = machineSlides[machineIdx].img;
        capEl.innerText = machineSlides[machineIdx].title;
      }
    }
  </script>
</body>
</html>
"""


def build_index_page():
    title = "Supplier Kebutuhan Pabrik Cikarang Bekasi | PT. Wirasena Maju Bersama Rayya — Carton Box, Impraboard, Electrical Mechanical"
    description = "PT. Wirasena Maju Bersama Rayya merupakan perusahaan manufaktur & general supplier pabrik di Cikarang Bekasi: Carton Box, Impraboard, Electrical Mechanical, Pneumatics, Safety K3 & Fabrikasi Trolley."
    keywords = "supplier kebutuhan pabrik terdekat, general supplier pabrik cikarang bekasi, supplier alat listrik industri terdekat, supplier sparepart mesin pabrik, vendor mechanical electrical bekasi, pabrik carton box cikarang, jual impraboard cikarang, jasa fabrikasi trolley pabrik"

    body = f"""
  <!-- FULL-BLEED PHOTO HERO SLIDER WITH SOLID NAVY BOX ON RIGHT (Exact Trimitra Screenshot 1 Layout!) -->
  <section class="relative w-full h-[460px] sm:h-[540px] lg:h-[580px] bg-gray-900 overflow-hidden">
    
    <!-- Slide 1: Carton Box & Packaging Manufacturing -->
    <div class="hero-slide opacity-100 transition-opacity duration-700 absolute inset-0">
      <img src="assets/images/hero-banner-1.jpg?v=5" alt="Produsen Carton Box, Impraboard & Supplier Kebutuhan Pabrik Cikarang" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-black/20"></div>
      <div class="absolute inset-0 max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 flex items-center justify-end">
        <div class="bg-tmc-navy/95 text-white rounded-2xl px-7 sm:px-12 py-9 sm:py-12 max-w-xl shadow-2xl text-center">
          <h1 class="font-heading text-xl sm:text-2xl md:text-[28px] font-bold uppercase leading-[1.4] tracking-wide">
            PRODUSEN CARTON BOX, IMPRABOARD &amp; SUPPLIER KEBUTUHAN PABRIK TERPERCAYA DI CIKARANG
          </h1>
        </div>
      </div>
    </div>

    <!-- Slide 2: Electrical, Mechanical & Factory Supplies -->
    <div class="hero-slide opacity-0 pointer-events-none transition-opacity duration-700 absolute inset-0">
      <img src="assets/images/hero-banner-2.jpg?v=5" alt="Supplier Alat Listrik Industri, Sparepart Mechanical & Pneumatics Cikarang Bekasi" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-black/20"></div>
      <div class="absolute inset-0 max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 flex items-center justify-end">
        <div class="bg-tmc-navy/95 text-white rounded-2xl px-7 sm:px-12 py-9 sm:py-12 max-w-xl shadow-2xl text-center">
          <h2 class="font-heading text-xl sm:text-2xl md:text-[28px] font-bold uppercase leading-[1.4] tracking-wide">
            SUPPLIER ALAT LISTRIK INDUSTRI, SPAREPART MECHANICAL, PNEUMATICS &amp; SAFETY K3 PABRIK
          </h2>
        </div>
      </div>
    </div>

    <!-- Slide 3: Industrial Fabrication & Welding -->
    <div class="hero-slide opacity-0 pointer-events-none transition-opacity duration-700 absolute inset-0">
      <img src="assets/images/hero-banner-3.jpg?v=5" alt="Jasa Fabrikasi Storage Trolley Stainless & Konstruksi Las Industri Cikarang" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-black/20"></div>
      <div class="absolute inset-0 max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 flex items-center justify-end">
        <div class="bg-tmc-navy/95 text-white rounded-2xl px-7 sm:px-12 py-9 sm:py-12 max-w-xl shadow-2xl text-center">
          <h2 class="font-heading text-xl sm:text-2xl md:text-[28px] font-bold uppercase leading-[1.4] tracking-wide">
            JASA FABRIKASI STORAGE TROLLEY STAINLESS, RAK PIPA FIFO &amp; KONSTRUKSI LAS INDUSTRI
          </h2>
        </div>
      </div>
    </div>

    <!-- Slider Controls (Arrows & Dots) -->
    <button onclick="prevSlide()" aria-label="Slide Sebelumnya" class="absolute left-4 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/35 hover:bg-black/60 text-white flex items-center justify-center transition">
      &#10094;
    </button>
    <button onclick="nextSlide()" aria-label="Slide Berikutnya" class="absolute right-4 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/35 hover:bg-black/60 text-white flex items-center justify-center transition">
      &#10095;
    </button>
    <div class="absolute bottom-5 left-1/2 -translate-x-1/2 flex items-center gap-2.5">
      <button onclick="showSlide(0)" aria-label="Slide 1" class="hero-dot w-3 h-3 rounded-full bg-tmc-green transition"></button>
      <button onclick="showSlide(1)" aria-label="Slide 2" class="hero-dot w-3 h-3 rounded-full bg-white/60 hover:bg-white transition"></button>
      <button onclick="showSlide(2)" aria-label="Slide 3" class="hero-dot w-3 h-3 rounded-full bg-white/60 hover:bg-white transition"></button>
    </div>
  </section>

  <!-- SECTION: TENTANG KAMI (Exact Trimitra Screenshot 2 Layout!) -->
  <section id="tentang-kami" class="pt-14 pb-6 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <h2 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
        TENTANG KAMI
      </h2>
    </div>
  </section>

  <section class="bg-[#F7F8F9] py-14 sm:py-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
        
        <!-- Left Column: Corporate Description + Solid Navy Button -->
        <div class="lg:col-span-6">
          <h3 class="font-heading text-2xl sm:text-[28px] font-normal text-[#555555] uppercase tracking-wide mb-6">
            PT. WIRASENA MAJU BERSAMA RAYYA
          </h3>
          <p class="text-[#666666] text-[15px] leading-[2.1] mb-8">
            PT. Wirasena Maju Bersama Rayya merupakan perusahaan manufaktur dan <em>general supplier</em> di Cikarang, Bekasi yang bergerak di bidang pembuatan kemasan <strong>Carton Box</strong>, <strong>Impraboard Box</strong>, pengadaan barang <strong>Electrical &amp; Mechanical</strong>, <strong>Pneumatics</strong>, <strong>Safety K3</strong>, serta <strong>Jasa Fabrikasi Trolley Industri</strong>.
          </p>
          <a href="#fasilitas-mesin" class="inline-block bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs tracking-wider px-8 py-3.5 transition shadow-sm">
            Tentang Kami
          </a>
        </div>

        <!-- Right Column: Company Profile Facility Player (Matches Screenshot 2 Video Box) -->
        <div class="lg:col-span-6">
          <div onclick="cycleMachineTour()" class="relative rounded overflow-hidden shadow-lg cursor-pointer group bg-black aspect-video">
            <img id="cp-tour-img" src="assets/images/machine-1-cutting-creasing.png" alt="Fasilitas Mesin Produksi PT. Wirasena Maju Bersama Rayya" class="w-full h-full object-cover opacity-90 group-hover:scale-105 transition duration-500" />
            <div class="absolute inset-0 bg-gradient-to-b from-black/65 via-transparent to-black/70"></div>

            <!-- Top Video-Style Title Bar -->
            <div class="absolute top-3.5 left-4 right-4 flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-white p-1 flex items-center justify-center shrink-0 shadow">
                <img src="assets/images/logo-avatar.png?v=5" alt="WMB" class="w-full h-full object-contain" />
              </div>
              <div class="text-white leading-tight truncate">
                <div class="font-heading text-sm sm:text-base font-semibold truncate">Company Profile PT. Wirasena Maju Bersama Rayya</div>
                <div class="text-[11px] text-white/80">Wirasena Cikarang • Klik untuk lihat 5 Mesin Produksi</div>
              </div>
            </div>

            <!-- Center Play / Next Machine Button -->
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="w-16 h-11 rounded-xl bg-[#FF0000]/90 group-hover:bg-[#FF0000] text-white flex items-center justify-center shadow-xl transition transform group-hover:scale-110">
                <svg class="w-6 h-6 fill-current ml-0.5" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z"/>
                </svg>
              </div>
            </div>

            <!-- Bottom Machine Caption Bar -->
            <div class="absolute bottom-3 left-4 right-4 flex items-center justify-between text-white text-xs">
              <span id="cp-tour-caption" class="font-medium bg-black/50 px-3 py-1 rounded">
                1/5 — Cutting &amp; Creasing Machine (Produksi Carton Box Presisi)
              </span>
              <span class="text-[11px] text-white/80 hidden sm:inline">Klik gambar untuk ganti mesin &rarr;</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SECTION: PRODUK KAMI (Exact Trimitra Screenshot 3 Layout — 2-Column Studio Product Showcase + MORE Pill Button!) -->
  <section id="produk-kami" class="py-16 sm:py-20 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      
      <div class="mb-16">
        <h2 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
          PRODUK KAMI
        </h2>
      </div>

      <!-- 2-Column Clean White Studio Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-20 max-w-5xl mx-auto">
        
        <!-- Product 1: Carton Box & Packaging -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Carton Box &amp; Die Cut Box
          </h3>
          <a href="pabrik-carton-box-impraboard.html" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-carton-box.png?v=5" alt="Pabrik Carton Box Custom Cikarang Bekasi" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="pabrik-carton-box-impraboard.html" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

        <!-- Product 2: Impraboard Box & Partisi -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Impraboard Box &amp; Partition
          </h3>
          <a href="pabrik-carton-box-impraboard.html#impraboard" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-impraboard.png?v=5" alt="Supplier Box Impraboard Custom Cikarang Bekasi" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="pabrik-carton-box-impraboard.html#impraboard" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

        <!-- Product 3: Electrical & Mechanical Supply -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Electrical &amp; Mechanical Supply
          </h3>
          <a href="supplier-electrical-mechanical.html" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-electrical-mechanical.png?v=5" alt="Supplier Alat Listrik Industri & Sparepart Mechanical Pabrik" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="supplier-electrical-mechanical.html" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

        <!-- Product 4: Pneumatics & Factory Supplies -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Pneumatics &amp; Safety K3
          </h3>
          <a href="supplier-electrical-mechanical.html#pneumatics" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-pneumatics.png?v=5" alt="Supplier Komponen Pneumatic & Alat Safety K3 Pabrik Cikarang" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="supplier-electrical-mechanical.html#pneumatics" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

        <!-- Product 5: Adhesive Tape, Plastic & Rubber -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Masking Tape, Plastic &amp; Rubber
          </h3>
          <a href="pabrik-carton-box-impraboard.html#rubber-plastic" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-tape-rubber.png?v=5" alt="Supplier Lakban Industri, Plastik HDPE LDPE & Synthetic Rubber" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="pabrik-carton-box-impraboard.html#rubber-plastic" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

        <!-- Product 6: Storage Trolley & Welding Fabrication -->
        <div class="flex flex-col items-center text-center">
          <h3 class="font-heading text-xl sm:text-[23px] font-normal text-[#4A4A4A] mb-6">
            Storage Trolley &amp; Fabrication
          </h3>
          <a href="jasa-fabrikasi-trolley.html" class="block w-full max-w-[420px] mb-6 group">
            <img src="assets/images/studio-trolley-fabrication.png?v=5" alt="Jasa Fabrikasi Storage Trolley Stainless & Besi Pabrik Bekasi" class="w-full h-[270px] object-contain mx-auto group-hover:scale-105 transition duration-300" />
          </a>
          <a href="jasa-fabrikasi-trolley.html" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-9 py-3 rounded-full transition shadow-sm">
            MORE
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- FASILITAS MESIN & MITRA PELANGGAN (Clean Corporate Strip) -->
  <section id="fasilitas-mesin" class="py-16 bg-[#F7F8F9] border-t border-gray-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="mb-12">
        <h2 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
          FASILITAS MESIN &amp; MITRA INDUSTRI
        </h2>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-5 mb-12">
        <div class="bg-white border border-gray-200 p-3 text-center shadow-sm">
          <img src="assets/images/machine-1-cutting-creasing.png" alt="Cutting & Creasing Machine" class="w-full h-36 object-cover mb-3" />
          <h4 class="font-heading text-xs font-bold uppercase text-tmc-navy">Cutting &amp; Creasing</h4>
        </div>
        <div class="bg-white border border-gray-200 p-3 text-center shadow-sm">
          <img src="assets/images/machine-2b-auto-folder-glue.png" alt="Automatic Folder Glue" class="w-full h-36 object-cover mb-3" />
          <h4 class="font-heading text-xs font-bold uppercase text-tmc-navy">Auto Folder Glue</h4>
        </div>
        <div class="bg-white border border-gray-200 p-3 text-center shadow-sm">
          <img src="assets/images/machine-3-semi-folder-glue.png" alt="Semi Folder Glue" class="w-full h-36 object-cover mb-3" />
          <h4 class="font-heading text-xs font-bold uppercase text-tmc-navy">Semi Folder Glue</h4>
        </div>
        <div class="bg-white border border-gray-200 p-3 text-center shadow-sm">
          <img src="assets/images/machine-4-rotary-sloter.png" alt="Rotary Sloter Machine" class="w-full h-36 object-cover mb-3" />
          <h4 class="font-heading text-xs font-bold uppercase text-tmc-navy">Rotary Sloter</h4>
        </div>
        <div class="bg-white border border-gray-200 p-3 text-center shadow-sm col-span-2 sm:col-span-1">
          <img src="assets/images/machine-5-rotary-die-cut.png" alt="Rotary Die Cut Machine" class="w-full h-36 object-cover mb-3" />
          <h4 class="font-heading text-xs font-bold uppercase text-tmc-navy">Rotary Die Cut</h4>
        </div>
      </div>

      <!-- Mitra Pelanggan (Zero PT Sharp!) -->
      <div class="bg-white border border-gray-200 p-6 sm:p-8 text-center shadow-sm">
        <p class="font-heading text-xs font-bold uppercase tracking-widest text-gray-400 mb-5">
          DIPERCAYA OLEH PERUSAHAAN MANUFAKTUR DI CIKARANG, BEKASI &amp; INDONESIA
        </p>
        <div class="flex flex-wrap items-center justify-center gap-x-8 gap-y-3 font-heading text-xs sm:text-sm font-bold text-tmc-navy">
          <span>PT. JAYA REFRIGERATION EQUIPMENT (MIDEA)</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. INDORAMA VENTURES</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. YASUNLI ABADI UTAMA</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. SKYWORTH INDUSTRY INDONESIA</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. DAIJO INDUSTRIAL</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. NUSANTARA INTI SOLUSINDO</span>
          <span class="text-gray-300">&bull;</span>
          <span>PT. EPS INDONESIA</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION: ARTIKEL KAMI / INFO (Exact Trimitra Screenshot 4 Layout!) -->
  <section class="py-16 sm:py-20 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        
        <!-- Left Column (1/3 width): Title, Text & Navy INFO Button -->
        <div class="lg:col-span-4">
          <h2 class="font-heading text-2xl sm:text-[26px] font-normal text-[#4A4A4A] uppercase tracking-wide mb-4">
            ARTIKEL KAMI
          </h2>
          <p class="text-[#666666] text-sm leading-[2] mb-7">
            Dapatkan informasi dan berita terbaru seputar pengadaan kebutuhan pabrik, komponen electrical mechanical, kemasan carton box &amp; impraboard, serta fabrikasi industri.
          </p>
          <a href="artikel-seo.html" class="inline-block bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-widest px-8 py-3.5 transition shadow-sm">
            INFO
          </a>
        </div>

        <!-- Right Column (2/3 width): 2 Split Horizontal Article Cards (Matches Screenshot 4) -->
        <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-7">
          
          <!-- Article Card 1 -->
          <article class="bg-white border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.08)] flex flex-col sm:flex-row overflow-hidden">
            <div class="sm:w-5/12 relative min-h-[220px] bg-gray-100 shrink-0">
              <img src="assets/images/product-carton-box.png" alt="Carton Box & Impraboard Industri" class="w-full h-full object-cover" />
              <div class="absolute top-3 left-3 bg-white text-gray-700 text-center px-2.5 py-1 shadow text-xs font-heading">
                <span class="font-bold block text-sm leading-none">27</span>
                <span class="text-[10px]">Okt</span>
              </div>
            </div>
            <div class="sm:w-7/12 p-5 flex flex-col justify-between">
              <div>
                <h3 class="font-heading text-sm font-bold text-[#4A4A4A] uppercase leading-snug hover:text-tmc-green transition">
                  <a href="artikel-seo.html">PANDUAN MEMILIH CARTON BOX &amp; IMPRABOARD UNTUK INDUSTRI</a>
                </h3>
                <div class="w-8 h-0.5 bg-gray-200 my-3"></div>
                <p class="text-xs text-[#666666] leading-relaxed">
                  Carton box dan box impraboard adalah komponen krusial untuk melindungi kualitas produk manufaktur selama proses pengiriman dan penyimpanan gudang [...]
                </p>
              </div>
            </div>
          </article>

          <!-- Article Card 2 -->
          <article class="bg-white border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.08)] flex flex-col sm:flex-row overflow-hidden">
            <div class="sm:w-5/12 relative min-h-[220px] bg-gray-100 shrink-0">
              <img src="assets/images/trading-electrical-mechanical.png" alt="Supplier Electrical Mechanical Pabrik Terdekat" class="w-full h-full object-cover" />
              <div class="absolute top-3 left-3 bg-white text-gray-700 text-center px-2.5 py-1 shadow text-xs font-heading">
                <span class="font-bold block text-sm leading-none">25</span>
                <span class="text-[10px]">Okt</span>
              </div>
            </div>
            <div class="sm:w-7/12 p-5 flex flex-col justify-between">
              <div>
                <h3 class="font-heading text-sm font-bold text-[#4A4A4A] uppercase leading-snug hover:text-tmc-green transition">
                  <a href="artikel-seo.html">DAFTAR KEBUTUHAN ELECTRICAL, MECHANICAL &amp; PNEUMATIC PABRIK</a>
                </h3>
                <div class="w-8 h-0.5 bg-gray-200 my-3"></div>
                <p class="text-xs text-[#666666] leading-relaxed">
                  Kecepatan pengadaan komponen electrical, sensor, bearing, hingga pneumatic sangat menentukan kelancaran operasional mesin produksi di kawasan industri [...]
                </p>
              </div>
            </div>
          </article>

        </div>

      </div>
    </div>
  </section>
"""
    return render_head(title, description, keywords, "index.html") + render_navbar("index.html") + body + render_footer_and_wa()


def build_subpage(filename, title, description, keywords, banner_img, banner_heading, section_title, intro_text, items):
    cards_html = ""
    for item in items:
        anchor_attr = f'id="{item["id"]}"' if item.get("id") else ""
        spec_rows = "".join([f'<li class="py-1.5 border-b border-gray-100 text-xs text-gray-600 flex items-center gap-2"><span class="text-tmc-green font-bold">&#10003;</span> {s}</li>' for s in item["specs"]])
        cards_html += f"""
        <div {anchor_attr} class="bg-white border border-gray-200 shadow-sm p-6 sm:p-8 grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
          <div class="md:col-span-5 flex items-center justify-center bg-white p-2">
            <img src="{item['img']}" alt="{item['name']}" class="w-full max-h-[260px] object-contain" />
          </div>
          <div class="md:col-span-7">
            <h3 class="font-heading text-xl font-bold text-tmc-navy uppercase tracking-wide mb-3">{item['name']}</h3>
            <div class="w-12 h-0.5 bg-tmc-green mb-4"></div>
            <p class="text-sm text-gray-600 leading-relaxed mb-4">{item['desc']}</p>
            <ul class="mb-6">
              {spec_rows}
            </ul>
            <div class="flex flex-wrap items-center gap-3">
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20tanya%20harga%20{item['wa_topic']}" target="_blank" rel="noopener" class="bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-wider px-7 py-3 rounded-full transition">
                Minta Penawaran (RFQ)
              </a>
              <a href="mailto:marketing@wirasenamajubersama.com?subject=RFQ%20-%20{item['wa_topic']}" class="border border-gray-300 hover:border-tmc-navy text-gray-700 font-heading font-semibold text-xs uppercase tracking-wider px-6 py-3 rounded-full transition">
                Kirim Email Marketing
              </a>
            </div>
          </div>
        </div>
        """

    body = f"""
  <!-- Full-Bleed Subpage Banner with Navy Box -->
  <section class="relative w-full h-[360px] sm:h-[420px] bg-gray-900 overflow-hidden">
    <img src="{banner_img}" alt="{banner_heading}" class="w-full h-full object-cover" />
    <div class="absolute inset-0 bg-black/25"></div>
    <div class="absolute inset-0 max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 flex items-center justify-end">
      <div class="bg-tmc-navy/95 text-white rounded-2xl px-7 sm:px-10 py-8 sm:py-10 max-w-xl shadow-2xl text-center">
        <h1 class="font-heading text-lg sm:text-2xl font-bold uppercase leading-snug tracking-wide">
          {banner_heading}
        </h1>
      </div>
    </div>
  </section>

  <!-- Main Subpage Content -->
  <section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="mb-10">
        <h2 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
          {section_title}
        </h2>
        <p class="text-center text-sm text-gray-600 max-w-3xl mx-auto mt-4 leading-relaxed">
          {intro_text}
        </p>
      </div>

      <div class="space-y-10">
        {cards_html}
      </div>
    </div>
  </section>
"""
    return render_head(title, description, keywords, filename) + render_navbar(filename) + body + render_footer_and_wa()


def build_articles_page():
    filename = "artikel-seo.html"
    title = "Info & Artikel Pengadaan Pabrik Cikarang Bekasi | PT. Wirasena Maju Bersama Rayya"
    description = "Informasi seputar pengadaan kebutuhan pabrik, cara memilih spesifikasi Carton Box & Impraboard, serta daftar sparepart Electrical, Mechanical & Pneumatics industri di Cikarang Bekasi."
    keywords = "artikel pengadaan pabrik, spesifikasi carton box single wall double wall, box impraboard antistatic, daftar kebutuhan electrical mechanical pabrik, supplier pabrik terdekat cikarang"

    articles = [
        {
            "date_day": "27",
            "date_mon": "Okt",
            "img": "assets/images/product-carton-box.png",
            "title": "PANDUAN MEMILIH SPESIFIKASI CARTON BOX (SINGLE, DOUBLE & TRIPLE WALL) UNTUK PABRIK",
            "body": "Dalam pengiriman barang manufaktur di kawasan industri Cikarang dan Bekasi, pemilihan ketebalan flute (B-Flute, C-Flute, CB-Flute) serta jenis dinding karton boks sangat menentukan keamanan produk. PT. Wirasena Maju Bersama Rayya memproduksi Carton Box dan Die-Cut Box custom menggunakan 5 mesin in-house (Cutting & Creasing, Auto/Semi Folder Glue, Rotary Sloter, dan Rotary Die Cut) untuk memastikan presisi ukuran dan ketepatan jadwal pengiriman."
        },
        {
            "date_day": "25",
            "date_mon": "Okt",
            "img": "assets/images/trading-electrical-mechanical.png",
            "title": "DAFTAR BARANG ELECTRICAL, MECHANICAL & PNEUMATICS YANG WAJIB TERSEDIA DI MAINTENANCE PABRIK",
            "body": "Ketika tim Purchasing atau Engineering mencari supplier kebutuhan pabrik terdekat di Cikarang, kecepatan respons untuk pengadaan komponen seperti Sensor Photoelectric/Proximity, PLC, Inverter, MCB, Contactor, Bearing, V-Belt, Solenoid Valve, hingga Air Cylinder sangat krusial untuk mencegah downtime mesin. Kami menyediakan layanan General Trading satu pintu sesuai spesifikasi merek dan part number yang diminta buyer."
        },
        {
            "date_day": "22",
            "date_mon": "Okt",
            "img": "assets/images/product-impraboard-box.png",
            "title": "KEUNGGULAN BOX IMPRABOARD & PARTISI CUSTOM UNTUK SIRKULASI KOMPONEN OTOMOTIF DAN ELEKTRONIK",
            "body": "Box Impraboard (PP Corrugated Board) dengan sekat partisi custom merupakan solusi kemasan sirkulasi (returnable packaging) yang tahan air, tahan benturan, dan tersedia dalam varian Anti-Static (ESD). Sangat ideal digunakan pada rak FIFO maupun storage trolley di lini perakitan."
        },
        {
            "date_day": "19",
            "date_mon": "Okt",
            "img": "assets/images/fabrication-trolley-stainless.png",
            "title": "STANDAR FABRIKASI STORAGE TROLLEY STAINLESS STEEL & BESI HOLLOW UNTUK LINI PRODUKSI",
            "body": "Trolley material handling dan rak pipa FIFO yang dirancang sesuai drawing teknik membantu menerapkan sistem Lean Manufacturing di lantai pabrik. Workshop fabrikasi PT. Wirasena Maju Bersama Rayya melayani pembuatan Storage Trolley, Parts Trolley, dan konstruksi las industri dengan roda heavy-duty polyurethane."
        }
    ]

    cards = ""
    for a in articles:
        cards += f"""
        <article class="bg-white border border-gray-200 shadow-sm flex flex-col md:flex-row overflow-hidden">
          <div class="md:w-4/12 relative min-h-[220px] bg-gray-100 shrink-0">
            <img src="{a['img']}" alt="{a['title']}" class="w-full h-full object-cover" />
            <div class="absolute top-3 left-3 bg-white text-gray-800 text-center px-3 py-1.5 shadow text-xs font-heading">
              <span class="font-bold block text-base leading-none">{a['date_day']}</span>
              <span class="text-[11px]">{a['date_mon']}</span>
            </div>
          </div>
          <div class="md:w-8/12 p-6 sm:p-8 flex flex-col justify-between">
            <div>
              <h2 class="font-heading text-base sm:text-lg font-bold text-tmc-navy uppercase leading-snug mb-3">{a['title']}</h2>
              <div class="w-10 h-0.5 bg-tmc-green mb-4"></div>
              <p class="text-sm text-gray-600 leading-relaxed mb-5">{a['body']}</p>
            </div>
            <div>
              <a href="https://wa.me/622184990200?text=Halo%20PT.%20Wirasena%20Maju%20Bersama%20Rayya,%20kami%20ingin%20konsultasi%20pengadaan%20pabrik" target="_blank" rel="noopener" class="inline-block bg-tmc-navy hover:bg-tmc-green text-white font-heading font-bold text-xs uppercase tracking-wider px-6 py-2.5 rounded-full transition">
                Konsultasi &amp; Minta Penawaran
              </a>
            </div>
          </div>
        </article>
        """

    body = f"""
  <section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-8">
      <div class="mb-12">
        <h1 class="section-line-title font-heading text-2xl sm:text-[28px] font-normal tracking-wide uppercase">
          INFO &amp; ARTIKEL INDUSTRI
        </h1>
      </div>
      <div class="space-y-8">
        {cards}
      </div>
    </div>
  </section>
"""
    return render_head(title, description, keywords, filename) + render_navbar(filename) + body + render_footer_and_wa()


def main():
    # 1. index.html
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index_page())

    # 2. pabrik-carton-box-impraboard.html
    packaging_items = [
        {
            "id": "carton-box",
            "name": "Carton Box Custom & Die Cut Box",
            "img": "assets/images/studio-carton-box.png?v=5",
            "desc": "Produksi Carton Box ukuran custom (Regular Slotted Container / RSC, Overlap, dan Die-Cut Box) untuk kemasan industri elektronik, otomotif, plastik, dan consumer goods di Cikarang & Bekasi.",
            "specs": [
                "Pilihan Ketebalan: Single Wall, Double Wall, & Triple Wall (B/C/E/CB Flute)",
                "Didukung 5 Mesin Produksi In-House (Cutting, Creasing, Folder Glue, Sloter, Die Cut)",
                "Tersedia Carton Box Safety Glass & Tempered Glass Protection"
            ],
            "wa_topic": "Carton%20Box%20Custom"
        },
        {
            "id": "impraboard",
            "name": "Impraboard Box & Sekat Partisi Custom",
            "img": "assets/images/studio-impraboard.png?v=5",
            "desc": "Pembuatan Box Impraboard (PP Corrugated Sheet) lengkap dengan sekat partisi (divider/layer pad), siku plastik, handle, dan tipe Anti-Static (ESD) untuk komponen presisi.",
            "specs": [
                "Ketebalan Material 2mm, 3mm, 4mm, 5mm hingga 6mm dengan Berbagai Warna",
                "Desain Lipat, Sekat Presisi & Siku Penguat Beban Industri",
                "Tahan Air, Bahan Kimia Ringan & Pemakaian Berulang (Returnable Box)"
            ],
            "wa_topic": "Box%20Impraboard%20Custom"
        },
        {
            "id": "rubber-plastic",
            "name": "Masking Tape, Plastic Packing (HDPE/LDPE) & Synthetic Rubber",
            "img": "assets/images/studio-tape-rubber.png?v=5",
            "desc": "Suplai material pelindung pengemasan industri serta pembuatan komponen karet sintetis (Synthetic & Chloroprene Rubber) sesuai sampel dan spesifikasi pabrik.",
            "specs": [
                "Plastic Packing HDPE, LDPE, LLDPE Stretch Film, PE Foam & Anti-Static Bag",
                "Masking Tape, OPP Lakban Industri, Adhesive Tape & Acrylic/Protection Sheet",
                "Fabrication Synthetic Rubber, Chloroprene Rubber, Rubber Molded & Rubber Foot"
            ],
            "wa_topic": "Plastic%20Packing%20Tape%20dan%20Rubber"
        }
    ]
    with open(os.path.join(BASE_DIR, "pabrik-carton-box-impraboard.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "pabrik-carton-box-impraboard.html",
            "Pabrik Carton Box & Box Impraboard Custom Cikarang Bekasi | PT. Wirasena Maju Bersama Rayya",
            "Produsen Carton Box custom, Die Cut Box, Box Impraboard sekat partisi, Plastik HDPE/LDPE, PE Foam, Lakban, dan Synthetic Rubber di Cikarang Selatan, Bekasi.",
            "pabrik carton box cikarang bekasi, supplier kardus pabrik terdekat, jual box impraboard custom cikarang, plastik packing hdpe ldpe, synthetic rubber pabrik",
            "assets/images/hero-banner-1.jpg?v=5",
            "PABRIK CARTON BOX, IMPRABOARD & KEMASAN INDUSTRI CIKARANG",
            "PRODUK PACKAGING & RUBBER",
            "Kami memproduksi Carton Box, Box Impraboard, Plastik Industri, serta komponen Synthetic Rubber dengan standar kualitas presisi dan pengiriman tepat waktu.",
            packaging_items
        ))

    # 3. supplier-electrical-mechanical.html
    me_items = [
        {
            "id": "electrical",
            "name": "Alat Listrik Industri & Komponen Otomasi (Electrical Supply)",
            "img": "assets/images/studio-electrical-mechanical.png?v=5",
            "desc": "Pengadaan komponen kelistrikan pabrik, panel kontrol, dan sensor otomasi mesin untuk kebutuhan Maintenance (MRO) dan Engineering.",
            "specs": [
                "PLC, Inverter (VFD), Power Supply, Timer, Counter & Temperature Controller",
                "Sensor Photoelectric, Proximity, Limit Switch, Push Button & Pilot Lamp",
                "MCB, MCCB, Magnetic Contactor, Thermal Overload Relay & Kabel Industri"
            ],
            "wa_topic": "Alat%20Listrik%20Industri%20Electrical"
        },
        {
            "id": "mechanical",
            "name": "Sparepart Mesin & Workshop Tools (Mechanical Supply)",
            "img": "assets/images/trading-tools.png",
            "desc": "Suplai suku cadang mekanikal mesin produksi, transmisi industri, serta perkakas bengkel (hand tools & cutting tools) sesuai merek permintaan buyer.",
            "specs": [
                "Bearing (Ball, Roller, Linear, Pillow Block), V-Belt, Timing Belt, Pulley & Sprocket",
                "Gearbox, Elektro Motor Dinamo, Roller Conveyor, Coupling & Seal",
                "Cutting Tools (Endmill, Drill Bit, Insert Bubut), Kunci Workshop & Alat Ukur"
            ],
            "wa_topic": "Sparepart%20Mechanical%20dan%20Tools"
        },
        {
            "id": "pneumatics",
            "name": "Komponen Pneumatics, Safety K3 & Consumables Pabrik",
            "img": "assets/images/studio-pneumatics.png?v=5",
            "desc": "Pengadaan komponen sistem udara bertekanan (Pneumatics) serta perlengkapan keselamatan kerja (APD K3) dan kebersihan rutin pabrik.",
            "specs": [
                "Solenoid Valve, Air Cylinder, Air Filter Regulator Lubricator (FRL), Fitting & Selang PU",
                "Perlengkapan Safety K3: Helm, Sepatu Safety, Kacamata, Masker, Earplug & Sarung Tangan",
                "Kain Majun Jahit/Putih, Chemical Maintenance, Pest Control, Cleaning & Office Supplies"
            ],
            "wa_topic": "Pneumatics%20dan%20Safety%20K3"
        }
    ]
    with open(os.path.join(BASE_DIR, "supplier-electrical-mechanical.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "supplier-electrical-mechanical.html",
            "Supplier Alat Listrik Industri, Sparepart Mechanical & Pneumatics Cikarang | PT. Wirasena Maju Bersama Rayya",
            "Supplier kebutuhan pabrik terdekat di Cikarang & Bekasi untuk barang Electrical, Mechanical, Sparepart Mesin, Komponen Pneumatics, Cutting Tools, Safety K3 & Kain Majun.",
            "supplier kebutuhan pabrik terdekat, supplier alat listrik industri terdekat, supplier sparepart mesin pabrik, vendor mechanical electrical bekasi, supplier pneumatic cikarang",
            "assets/images/hero-banner-2.jpg?v=5",
            "SUPPLIER ELECTRICAL, MECHANICAL, PNEUMATICS & K3 PABRIK",
            "GENERAL TRADING & FACTORY SUPPLIES",
            "Satu pintu untuk pengadaan komponen Electrical, Sparepart Mechanical, Pneumatics, Perkakas Teknik, hingga perlengkapan Safety K3 pabrik Anda (All items are as requested by the buyer).",
            me_items
        ))

    # 4. jasa-fabrikasi-trolley.html
    fab_items = [
        {
            "id": "trolley-stainless",
            "name": "Custom Storage Trolley Stainless Steel & Besi Hollow",
            "img": "assets/images/studio-trolley-fabrication.png?v=5",
            "desc": "Pembuatan Storage Trolley, Trolley Rak Bertingkat, dan Hand Pallet Trolley sesuai gambar kerja (custom drawing) untuk efisiensi material handling di lini produksi.",
            "specs": [
                "Material Stainless Steel (SUS 304 / 201) atau Besi Hollow dengan Finishing Powder Coating",
                "Dilengkapi Roda Heavy Duty Caster (PU / Nylon / Rubber) dengan Rem Pengunci",
                "Ukuran Dimensi, Jumlah Rak & Sekat Disesuaikan Penuh dengan Komponen Pabrik"
            ],
            "wa_topic": "Fabrikasi%20Storage%20Trolley"
        },
        {
            "id": "welding",
            "name": "Rak Pipa FIFO, Meja Kerja Produksi & Fence Welding Industri",
            "img": "assets/images/fabrication-welding.png",
            "desc": "Layanan las industri (MIG, TIG, Argon, SMAW) dan fabrikasi konstruksi logam untuk menunjang keselamatan serta kerapian area pabrik.",
            "specs": [
                "Pembuatan Rak Pipa FIFO (Roller Track), Meja Kerja Assembly (Workstation) & Jigs",
                "Fence Welding: Pagar Pengaman Mesin (Machine Guarding), Handrail & Partisi Gudang",
                "Pengerjaan Presisi, Las Rapi & Pengiriman Tepat Waktu ke Kawasan Industri"
            ],
            "wa_topic": "Jasa%20Fabrikasi%20Las%20Industri"
        }
    ]
    with open(os.path.join(BASE_DIR, "jasa-fabrikasi-trolley.html"), "w", encoding="utf-8") as f:
        f.write(build_subpage(
            "jasa-fabrikasi-trolley.html",
            "Jasa Fabrikasi Storage Trolley Stainless & Bengkel Las Industri Cikarang | PT. Wirasena Maju Bersama Rayya",
            "Jasa fabrikasi pabrik terdekat di Cikarang & Bekasi: pembuatan Storage Trolley Stainless/Besi custom, Rak Pipa FIFO, Meja Kerja Produksi, dan Fence Welding industri.",
            "jasa fabrikasi pabrik terdekat, pembuatan trolley stainless pabrik, bengkel las industri bekasi, fabrikasi storage trolley cikarang",
            "assets/images/hero-banner-3.jpg?v=5",
            "JASA FABRIKASI STORAGE TROLLEY & KONSTRUKSI LAS INDUSTRI",
            "INDUSTRIAL METAL FABRICATION",
            "Melayani pembuatan Storage Trolley, Parts Trolley, Rak Pipa FIFO, serta pengelasan pagar pengaman mesin (Fence Welding) sesuai spesifikasi teknis pabrik Anda.",
            fab_items
        ))

    # 5. artikel-seo.html
    with open(os.path.join(BASE_DIR, "artikel-seo.html"), "w", encoding="utf-8") as f:
        f.write(build_articles_page())

    print("Successfully built authentic Trimitra-style B2B website across all 5 pages!")


if __name__ == "__main__":
    main()
