import streamlit as st

# Mengatur konfigurasi halaman agar menggunakan layout lebar dan menghilangkan padding atas
st.set_page_config(layout="wide", page_title="Toko Online Keren", page_icon="🛒")

# --- TEMPLATE HTML, CSS, DAN SCHEMA.ORG ---
# Semua kode untuk tampilan dan struktur ada di dalam string ini.
html_template = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>EMPIRE88: Supplier Gaming Resmi Terpercaya Saat Ini</title>
     <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
     <meta name="robots" content="index, follow"/>
     <meta name="aplus-auto-exp" content="[{&#34;filter&#34;:&#34;exp-tracking=suggest-official-store&#34;,&#34;logkey&#34;:&#34;/lzdse.result.os_impr&#34;,&#34;props&#34;:[&#34;href&#34;],&#34;tag&#34;:&#34;a&#34;}]"/>
     <meta name="og:url" content="https://empire88.streamlit.app/"/>
     <meta name="og:title" content="EMPIRE88: Supplier Gaming Resmi Terpercaya Saat Ini"/>
     <meta name="og:type" content="product"/>
     <meta name="og:description" content="Empire88 adalah supplier games online yang terbaik dan permainan viral masa kini. Menang hari ini bersama Empire88!"/>
    <meta name="description" content="EMPIRE88 adalah supplier gaming online resmi yang terpercaya saat ini. Menangkan games seru bersama Empire88 sekarang juga!">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <meta name="keywords"content="empire88, empire88 login, empire 88, empire88 slot" />
    <meta name="og:image" content="https://i.postimg.cc/XY7mv48T/empire88.png"/>
    <link rel="manifest" href="https://g.lazcdn.com/g/lzdfe/pwa-assets/5.0.7/manifest/id.json"/>
    <link rel="shortcut icon" href="https://i.postimg.cc/7Ys6XDdh/empire88logo.png"/>
    <link rel="canonical" href="https://empire88.streamlit.app/"/>
    <meta name="google-site-verification" content="cfCvR9YF9dnuqprCRWeL8rE_X8Oh2ez2Uvza_oS1rd8" />
    <link rel="amphtml" href="https://empire88streamlit.b-cdn.net" />
    <!-- Schema.org untuk SEO -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Toko Online Keren",
      "url": "https://empire88.streamlit.app/",
      "logo": "https://i.postimg.cc/7Ys6XDdh/empire88logo.png",
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+62-384-2348-4322",
        "contactType": "customer service"
      },
      "sameAs": [
        "https://www.facebook.com/empire88",
        "https://www.instagram.com/empire88"
      ]
    }
    </script>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "url": "https://empire88.streamlit.app/",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://empire88.streamlit.app/?s={search_term_string}",
            "query-input": "required name=search_term_string"
        }
    }
    </script>

    <style>
        /* Reset dan Font Dasar */
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }

        /* Sembunyikan UI bawaan Streamlit */
        iframe {
            display: none;
        }
        
        /* Navbar Utama */
        .navbar {
            background-color: #ffffff;
            padding: 0 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 1000;
            height: 80px;
        }
        .logo {
            display: flex;
            align-items: center;
        }
        .logo img {
            height: 40px;
        }
        .nav-links {
            display: flex;
            gap: 30px;
        }
        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #EE4D2D;
        }
        .auth-buttons {
            display: flex;
            gap: 15px;
        }
        .auth-buttons .btn {
            text-decoration: none;
            padding: 12px 32px;
            border-radius: 5px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s;
            border: 2px solid #EE4D2D;
        }
        .btn-primary {
            background-color: #EE4D2D;
            color: #ffffff;
        }
        .btn-primary:hover {
            background-color: #d73a1a;
            border-color: #d73a1a;
        }
        .btn-secondary {
            background-color: transparent;
            color: #EE4D2D;
        }
        .btn-secondary:hover {
            background-color: #ffeee9;
        }

        /* Hero Section */
        .hero {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 50px 5%;
            background-color: #fff;
            gap: 50px;
            min-height: calc(100vh - 80px - 100px); /* vh - navbar - footer */
        }
        .hero-text {
            max-width: 500px;
        }
        .hero-text h1 {
            font-size: 48px;
            line-height: 1.2;
            color: #EE4D2D;
            margin-bottom: 20px;
        }
        .hero-text p {
            font-size: 18px;
            margin-bottom: 30px;
        }
        .hero-image img {
            max-width: 100%;
            width: 500px; /* Ukuran gambar utama bisa disesuaikan */
            height: auto;
            border-radius: 10px;
        }

        /* Product Section */
        .products {
            padding: 50px 5%;
        }
        .products h2 {
            text-align: center;
            font-size: 32px;
            margin-bottom: 40px;
            color: #EE4D2D;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px;
        }
        .product-card {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
            text-align: left;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }
        .product-card img {
            width: 100%;
            height: 220px;
            object-fit: cover;
        }
        .product-info {
            padding: 15px;
        }
        .product-name {
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 10px;
            height: 40px; /* Untuk meratakan tinggi nama produk */
        }
        .product-price {
            font-size: 18px;
            font-weight: 700;
            color: #EE4D2D;
        }

        /* Footer */
        .footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px 5%;
            margin-top: 50px;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero {
                flex-direction: column;
                text-align: center;
            }
            .nav-links {
                display: none; /* Sembunyikan link nav di mobile untuk simplisitas */
            }
        }
        @media (max-width: 480px) {
             .auth-buttons .btn {
                padding: 8px 16px;
                font-size: 14px;
            }
            .hero-text h1 {
                font-size: 36px;
            }
        }

    </style>
</head>
<body>
    <header class="navbar">
        <div class="logo">
            <img src="https://i.postimg.cc/7Ys6XDdh/empire88logo.png" alt="Logo Toko Online Keren">
        </div>
        <nav class="nav-links">
            <a href="https://cutt.ly/Zeyl9GaN">Kategori</a>
            <a href="https://cutt.ly/Zeyl9GaN">Promo Hari Ini</a>
            <a href="https://cutt.ly/Zeyl9GaN">Produk Digital</a>
            <a href="https://cutt.ly/Zeyl9GaN">Bantuan</a>
        </nav>

    </header>

    <main>
        <section class="hero">
            <div class="hero-text">
                <h1>EMPIRE88: Supplier Gaming Resmi Terpercaya Saat Ini</h1>
                <p>EMPIRE88 adalah supplier gaming online resmi yang terpercaya saat ini. Menangkan games seru bersama Empire88 sekarang juga!</p>
            </div>
                                <div>
            <a href="https://cutt.ly/Zeyl9GaN"><button>Login</button></a>
            <a href="https://cutt.ly/Zeyl9GaN"><button>Daftar</button></a>
        </div>
            <div class="hero-image">
                <!-- Gambar utama 800x800, akan diskalakan oleh CSS -->
                <img src="https://i.postimg.cc/XY7mv48T/empire88.png" alt="Produk unggulan toko online">
            </div>
                    <div>
            <a href="https://cutt.ly/Zeyl9GaN"><button>Login</button></a>
            <a href="https://cutt.ly/Zeyl9GaN"><button>Daftar</button></a>
        </div>
        </section>

    <footer class="footer">
        <p>&copy; 2025 Empire88. Semua Hak Cipta Dilindungi.</p>
    </footer>

</body>
</html>
"""

# Render template HTML ke aplikasi Streamlit
st.markdown(html_template, unsafe_allow_html=True)

# Sembunyikan UI Streamlit default seperti header dan footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
