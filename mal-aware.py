import streamlit as st
from streamlit_lottie import st_lottie 
import requests as rq
from PIL import Image
# EDA Packages
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
# DB
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# mengambil gambar dari lottie
def load_lottieurl(url):
    r = rq.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# *****************************************************************************
# ------------------------------ HALAMAN UTAMA --------------------------------

# *****************************************************************************
def main_page():

    lottie_pic = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_ewya1ucg.json")

    st.sidebar.markdown("# Serambi Konten :house:")
    
    # mengatur ukuran huruf secara fleksibel
    st.markdown("""
    <style>
    .small-font {
        font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- ANCAMAN KEJAHATAN SIBER -----------------------
    st.markdown("<h1 style='text-align: center; color: white;'>Ancaman Kejahatan Siber dalam Bertransaksi <i>Online</i></h1>", unsafe_allow_html=True)
    st_lottie(lottie_pic, height=300)

    st.markdown("""<h2 class='small-font'; style='text-align: center; color: white;'> Tahukah kamu? Seiring berkembanganya ilmu pengetahuan dan teknologi, 
        segala aktivitas masyarakat kini lebih mudah dilakukan karena adanya 
        internet. Salah satunya adalah dalam hal bertransaksi, baik melalui 
        dompet digital (<i>e-wallet</i>), uang elektronik (<i>e-money</i>), maupun perbankan 
        elektronik (<i>e-banking</i>). Mulai dari pesan makanan, berbelanja kebutuhan 
        hidup seperti pakaian, elektronik dan sebagainya kini lebih mudah dilakukan 
        secara <i>online</i>. </h2>""", unsafe_allow_html=True) 

    st.markdown("""<h2 class='small-font'; style='text-align: center; color: white;'> Namun, apakah setiap orang betul-betul paham tentang transaksi 
        <i>online?</i> Nah, kalau belum tahu, yuk kita simak beberapa bahasan yang perlu kamu pahami tentang transaksi 
        <i>online</i>. Klik tombol-tombol di samping kiri, ya!</h2>""", unsafe_allow_html=True) 

# *****************************************************************************
# ------------------------------ HALAMAN 2 ------------------------------------

# *****************************************************************************
def page2():
    st.markdown("<h1 style='text-align: left; color: yellow;'> Bertransaksi Via Daring 💸 </h1>", unsafe_allow_html=True)
    st.sidebar.markdown("# Bertransaksi Via Daring :money_with_wings:")

    # mengatur ukuran huruf secara fleksibel
    st.markdown("""
    <style>
    .small-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # mengatur format hyperlink
    st.write("""
    <style>
    a:link {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:visited {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:hover {
        color: yellow;
        background-color: transparent;
        text-decoration: underline;
    }
    a:active {
        color: pink;
        background-color: transparent;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- DEFINISI TRANSAKSI ONLINE ----------
    st.markdown("<h2 style='text-align: left; color: lime;'> Definisi Transaksi <i>Online</i> </h2>", unsafe_allow_html=True)

    st.markdown("""<h3 class='small-font'; style='text-align: justify; color: white ;'> Dikutip dari laman <a href='https://humas.amikompurwokerto.ac.id/pengertian-transaksi-online/'>Humas dan Kerjasama Universitas Amikom Purwokerto (2022)</a>, transaksi <i>online</i> adalah salah satu metode pembayaran yang memungkinkan kegiatan transaksi dilakukan secara daring, baik untuk membeli produk atau jasa, berinvestasi, maupun menggunakan jasa perbankan. Namun, transaksi <i>online</i> masih saja kerap disamakan dengan transaksi digital walaupun keduanya memiliki kemiripan. Lantas, apa yang membedakan transaksi <i>online</i> dan digital? Simak yuk penjelasan berikut. </h3>""", unsafe_allow_html=True) 

    st.markdown("""<h3 class='small-font'; style='text-align: justify; color: white ;'> Menurut <a href='https://www.jurnal.id/id/blog/transaksi-digital-dalam-perkembangan-bisnis-online/'>Jurnal Entrepreneur Mekari</a>, transaksi <i>online</i> adalah metode pembayaran yang difasilitasi oleh penyedia layanan pembayaran (<i>payment gateway</i>) melalui jaringan/koneksi internet. Sedangkan transaksi digital adalah jenis pembayaran yang bisa dilakukan secara <i>online</i> (terhubung dengan jaringan internet) dan dengan menggunakan perangkat dalam bentuk aplikasi ataupun <i>website</i> penyedia jasa. Transaksi digital mengubah cara pembayaran tunai (<i>cash</i>) menjadi non-tunai (<i>cashless</i>).
    </h3>""", unsafe_allow_html=True) 

    # ---------- BEBERAPA CONTOH TRANSAKSI ONLINE ----------
    st.markdown("<h2 style='text-align: left; color: lime;'> Beberapa Contoh Transaksi <i>Online</i> </h2>", unsafe_allow_html=True)
    trans_on = st.selectbox("", ("Top up Pulsa", "Pembayaran Tagihan Listrik, Air, Telepon, Hingga Iuran BPJS", "Pembelian Kebutuhan Hidup", "Pemesanan Makanan/Kendaraan Online", "Berlangganan Layanan Hiburan"))
    if trans_on == "Top up Pulsa":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'> Suatu hari, kamu sedang menelepon teman, tiba-tiba sambungannya terputus. Ternyata pulsa habis dan kamu segera membuka aplikasi jasa operator seluler pilihanmu untuk membelinya dengan menggunakan salah satu metode pembayaran digital yang tersedia. Dalam hal ini berarti kamu telah melakukan <i>top up</i>. Istilah <i>top up</i> dalam bahasa Inggris berarti isi ulang. </h4>", unsafe_allow_html=True)
        with col2:
            lottie_pic = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_vyeonnoq.json")
            st_lottie(lottie_pic, height=250)     
    elif trans_on == "Pembayaran Tagihan Listrik, Air, Telepon, Hingga Iuran BPJS":
        col1, col2 = st.columns(2)
        with col1:
            lottie_pic = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_j9wgtpiy.json")
            st_lottie(lottie_pic, height=250)
        with col2:
            st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'> Jika biasanya kamu harus pergi langsung ke tempat pembayaran tagihan kebutuhan rumah seperti listrik, air, dan telepon, hingga iuran BPJS, kini kamu bisa menghemat waktu dan tenaga untuk melakukannya. Cukup dengan modal ponsel, paket data, dan uang elektronik, ataupun layanan perbankan digital pilihanmu, semua tanggungan tersebut bisa dengan cepat diselesaikan. Tentunya, harus terhubung dulu dengan internet, ya! </h4>", unsafe_allow_html=True)        
    elif trans_on == "Pembelian Kebutuhan Hidup":
        st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'> Suka belanja <i>online?</i> Bukan rahasia lagi kalau kebutuhan hidup kita pada saat ini bisa didapatkan dari banyak <i>marketplace</i> yang tersedia, yang tentunya juga menawarkan berbagai metode pembayaran secara <i>online</i>. Debit atau kredit, semuanya bisa dilakukan hanya dalam hitungan detik.</h4>", unsafe_allow_html=True)
        lottie_pic = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_57TxAX.json")
        st_lottie(lottie_pic, height=250)
    elif trans_on == "Pemesanan Makanan/Kendaraan Online":
        col1, col2 = st.columns(2)
        with col1:
            lottie_pic = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lx3owv1m.json")
            st_lottie(lottie_pic, height=250)
        with col2:
            lottie_pic = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_bhgw5v82.json")
            st_lottie(lottie_pic, height=250)
        st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Bayangkan, kamu sedang kelaparan, sibuk memilih makanan di aplikasi ponselmu, dan masih harus menyiapkan sejumlah uang tunai (yang bisa saja kamu lupa menaruhnya di mana). Beruntung jika uang elektronikmu masih memenuhi. Karena dengan begitu, kamu tidak perlu merasa direpotkan oleh hal yang terakhir dan hanya langsung memanfaatkan teknologi pembayaran secara daring. Cara transaksi seperti ini berlaku juga lho, ya, jika kamu ingin memesan kendaraan <i>online</i>. </h4>", unsafe_allow_html=True)
    elif trans_on == "Berlangganan Layanan Hiburan":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Layanan hiburan seperti film dan musik biasanya menawarkan pelanggannya untuk berlangganan dengan berbagai pilihan waktu, mulai dari harian, mingguan, bulanan, hingga tahunan. Kamu sebagai pelanggan bebas memilih dan bebas menentukan kapan berhenti berlangganan dengan menggunakan metode pembayaran digital pilihanmu.</h4>", unsafe_allow_html=True)
        with col2:
            lottie_pic = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_cszx2npa.json")
            st_lottie(lottie_pic, height=250)

# *****************************************************************************
# ------------------------------ HALAMAN 3 ------------------------------------

# *****************************************************************************
def page3():
    st.markdown("<h1 style='text-align: left; color: yellow;'> Serangan Kejahatan Siber dalam Bertransaksi <i>Online</i> 😈</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("# Serangan Kejahatan Siber dalam Bertransaksi Online :smiling_imp:")

    # mengatur ukuran huruf secara fleksibel
    st.markdown("""
    <style>
    .small-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""<h4 class='small-font'; style='text-align: justify; color: white;'>Meskipun terkesan mudah dan nyaman, risiko kejahatan seperti penipuan hingga pencurian data pribadi masih saja kerap terjadi dan perlu kita waspadai. Terutama dalam menggunakan internet untuk bertransaksi <i>online</i>. Berikut beberapa serangan dalam bertransaksi <i>online</i> yang harus kita waspadai.  
    </h4>""", unsafe_allow_html=True)

    # ---------- HACKING & CRACKING ----------
    st.markdown("<h3 style='text-align: left; color: lime;'> 1. <i>Hacking</i> (Peretasan) dan <i>Cracking</i> (Pembajakan)</h3>", unsafe_allow_html=True)
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Seiring dengan meningkatnya tren dalam berbelanja <i>online</i>, platform <i>e-commerce</i> dan <i>internet banking</i> kerap menjadi sasaran dalam upaya peretasan maupun pembajakan yang berujung pada pencurian data, pemerasan hingga penipuan yang dilakukan oleh oknum tak bertanggung jawab.</h4>""", unsafe_allow_html=True)
    lottie_pic = load_lottieurl("https://assets10.lottiefiles.com/temp/lf20_9EuvAt.json")
    st_lottie(lottie_pic, height=250)
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Berdasarkan aktivitas kejahatan yang dilakukan, para pelaku biasanya melancarkan aksinya melalui beberapa cara sebagai berikut:</h4>""", unsafe_allow_html=True)
    hacking = st.selectbox("", ("Kebocoran Kode OTP", "Pharming", "Sniffing"))
    if hacking == "Kebocoran Kode OTP":
        st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'><i>One Time Password</i> atau yang disingkat OTP merupakan sebuah <i>password</i> kode yang muncul pada saat pendaftaran/pembaharuan sebuah akun dan mengaktifkan keamanan <i>Two Factor Authentication</i> (TFA). Namun, apabila kode OTP tersebut bocor/dimiliki penjahat siber, hal besar yang kemungkinan terjadi ialah pembajakan akun transaksi <i>online</i> milik korban. Oleh karena itu, jangan sekali-kali untuk membagikan kode OTP kepada orang lain.</h4>", unsafe_allow_html=True)
    elif hacking == "Pharming":
        st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Modus ini biasanya dilakukan dengan mengarahkan korbannya ke situs web palsu yang dibuat seolah-olah mirip dengan domain yang biasa diakses korban. Penipu biasanya memasang <i>malware</i> untuk meretas akun milik korban (seperti WhatsApp).</h4>", unsafe_allow_html=True)
    elif hacking == "Sniffing":
        st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Modus ini dilakukan dengan cara meretas akun milik korban untuk mengumpulkan informasi secara ilegal lewat jaringan perangkat, Pelaku akan mengakses aplikasi yang menyimpan data/informasi penting milik korban. Biasanya terjadi ketika korban sedang mengakses Wi-Fi publik terlebih dahulu untuk kegiatan bertransaksi <i>online</i>.</h4>", unsafe_allow_html=True)
    
    # ---------- PHISHING ----------
    st.markdown("<h3 style='text-align: left; color: lime;'> 2. <i>Phishing</i> (Penipuan)</h3>", unsafe_allow_html=True)    
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Modus ini dilakukan pelaku dengan pencurian data sensitif untuk mengakses akun milik korban. Biasanya pelaku menyamar/mengaku sebagai lembaga resmi/entitas yang bisa dipercaya.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Berikut adalah contoh ilustrasi dari <i>phishing</i>.</h4>", unsafe_allow_html=True)     
  
    image=Image.open('phishing.png')
    new_image = image.resize((800, 600))
    st.image(new_image, caption='Sumber: https://www.pngitem.com')
  
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'>Ada beberapa jenis <i>phishing</i> yang umum dikenal, yaitu <i style='color : cyan'>deceptive phishing</i> (melalui <i>email</i>, pelaku mengaku kenal dengan korban atau menyamar seolah-olah perwakilan dari suatu lembaga resmi agar korban melakukan sesuatu yang dimintanya, seperti data pribadi dan penggantian kata sandi), <i style='color:cyan'>smishing</i> (singkatan dari SMS <i>phishing</i>, yaitu <i>phising</i> yang dilakukan melalui SMS), <i style='color:cyan'>vishing</i> (singkatan dari <i>voice phishing</i>, yaitu <i>phising</i> yang dilakukan melalui telepon), <i style='color:cyan'>spear phishing</i> (<i>phising</i> yang menargetkan orang atau perusahaan tertentu), dan <i style='color:cyan'>whaling</i> (singkatan dari <i>whale phising</i> yang menargetkan orang dengan kedudukan yang tinggi seperti direktur dan CEO perusahaan).</h4>", unsafe_allow_html=True)

    # ---------- CARDING ----------
    st.markdown("<h3 style='text-align: left; color: lime;'> 3. <i>Carding</i> (Penipuan)</h3>", unsafe_allow_html=True)    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        image=Image.open('carding.png')
        st.image(image, caption='Sumber: https://www.pngwing.com')
    with col3:
        st.write('')
    st.markdown("<h4 class='small-font'; style='text-align: justify; color: white;'><i>Carding</i> adalah sebuah bentuk kejahatan yang memanfaatkan data kartu debit atau kredit orang lain yang diperoleh secara ilegal untuk melakukan transaksi/belanja <i>online</i>. Hal ini bisa terjadi karena kegiatan transaksi yang dilakukan tidak membutuhkan kartu fisik dan hanya mengandalkan data dari kartu debit/kredit korban. Biasanya, pelaku akan mencari dan mendapatkan data-data dari kartu debit atau kredit tersebut melalui pencatatan data-data sensitif oleh oknum pada <i>merchant</i>, <i>marketing</i> palsu ataupun dari kartu hilang.</h4>", unsafe_allow_html=True)

    # ---------- MONEY MULE ----------
    st.markdown("<h3 style='text-align: left; color: lime;'> 4. <i>Money Mule</i> (Kurir Pencucian Uang)</h3>", unsafe_allow_html=True)
    st.markdown("""<h4 class='small-font'; style='text-align: justify; color: white;'> <i>Money mule</i> merupakan salah satu modus kejahatan digital yang dilakukan pelaku dengan cara meminta korban untuk menerima sejumlah uang ke rekeningnya dan akan menerima komisi apabila korban mentransfer kembali ke rekening penerima lain. Hal ini biasa dilakukan pelaku dengan maksud menghilangkan jejak agar sulit dilacak dengan sistem standar bank. Gambar di bawah ini merupakan ilustrasi dari <i>money mule</i>.
    </h4>""", unsafe_allow_html=True)
    st.write(" ")
    image=Image.open('moneymule.png')
    new_image = image.resize((800, 600))
    st.image(new_image, caption='Sumber: https://www.pngitem.com')
    st.write(" ")
    st.markdown("""<h4 class='small-font'; style='text-align: justify; color: white;'> Sampai sini sudah paham kan apa itu transaksi <i>online</i>, bedanya dengan transaksi digital hingga serangan-serangan yang mungkin terjadi dalam transaksi <i>online?</i> Yuk! Sadari lebih dini dan segera laporkan apabila terjadi indikasi penipuan/kejahatan dalam transaksi <i>online</i>. Jangan sampai kita menjadi salah satu korban dari para penjahat siber di masa yang akan datang.  
    </h4>""", unsafe_allow_html=True)
    st.markdown("""<h4 class='small-font'; style='text-align: justify; color: white;'>Lalu, Apa saja yang harus kita lakukan agar terhindar dari serangan kejahatan siber terutama dalam bertransaksi <i>online?</i> Jangan Panik! Mari kita simak tips-tipsnya di halaman berikut.</h4>""", unsafe_allow_html=True)
    
    st.write(" ")
    st.write(" ")
    
    # mengatur format hyperlink
    st.write("""
    <style>
    a:link {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:visited {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:hover {
        color: cyan;
        background-color: transparent;
        text-decoration: underline;
    }
    a:active {
        color: pink;
        background-color: transparent;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- SUMBER ----------
    st.markdown("<h4 style='text-align: left; color: cyan;'> Sumber: </h4>", unsafe_allow_html=True)
    st.markdown("https://www.bpkn.go.id/posts/show/id/1653")
    st.markdown("https://www.cnbcindonesia.com/tech/20220620143838-37-348602/bahaya-carding-mengintai-nasabah-bank-modus-apa-itu")
    st.markdown("https://finance.detik.com/berita-ekonomi-bisnis/d-5847301/5-modus-penipuan-terbaru-saat-transaksi-digital-awas-jadi-korban") 
    st.markdown("https://finansial.bisnis.com/read/20220507/90/1530596/ini-jenis-jenis-kejahatan-digital-perbankan-dan-tips-menghindarinya/All")
    st.markdown("https://www.helixstorm.com/blog/x-types-of-phishing-attacks-to-watch-out-for/")
    st.markdown("https://heylawedu.id/blog/bahaya-cyber-crime-money-mule-meningkat-kala-pandemi")
    st.markdown("https://www.itworks.id/33042/kejahatan-keuangan-model-money-mule-diprediksi-meningkat-di-2020-2021.html")
    st.markdown("https://katadata.co.id/desysetyowati/digital/617a779d735ca/bssn-ungkap-cara-hacker-bobol-sistem-bank-fintech")
    st.markdown("https://money.kompas.com/read/2021/12/08/141427226/ini-daftar-modus-penipuan-terbaru-saat-transaksi-digital?page=all")
    st.markdown("https://www.ocbcnisp.com/id/article/2021/05/31/phising-adalah")
    st.markdown("https://www.pngitem.com/middle/ThmTJ_money-mules-01-money-mule-hd-png-download/")
    st.markdown("https://www.pngwing.com/en/free-png-dchmb/download")

# *****************************************************************************
# ------------------------------ HALAMAN 4 ------------------------------------

# *****************************************************************************
def page4():
    st.markdown("<h1 style='text-align: left; color: yellow;'>Tips Mencegah Kejahatan Siber dalam Bertransaksi Online 💡</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("# Tips Mencegah Kejahatan Siber dalam Bertransaksi Online :bulb:")

    # mengatur ukuran huruf secara fleksibel
    st.markdown("""
    <style>
    .small-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # mengatur format hyperlink
    st.write("""
    <style>
    a:link {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:visited {
        color: pink;
        background-color: transparent;
        text-decoration: none;
    }
    a:hover {
        color: cyan;
        background-color: transparent;
        text-decoration: underline;
    }
    a:active {
        color: pink;
        background-color: transparent;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

     # ---------- GAMBAR TIPS ----------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        image=Image.open('tips.png')
        st.image(image, caption='Sumber: https://fakfakkab.go.id')
    with col3:
        st.write(" ")

     # ---------- NARASI TIPS ----------
    st.markdown("""<h4 class='small-font'; style='text-align: justify; color: white;'>Badan Siber dan Sandi Negara (BSSN), pada Februari 2019 telah menerbitkan sebuah buku yang berisi sejumlah tips dan informasi agar masyarakat tetap aman dan nyaman dalam menjelajah dunia siber, 
        tak terkecuali dalam bertransaksi <i>online</i>. Buku dapat diunduh pada tautan <a href='https://fakfakkab.go.id/wp-content/uploads/2019/04/Buku-Tips-BSSN-2019-tte-1.pdf'>Tips Singkat & Praktis di Dunia Siber</a>. Berikut beberapa hal yang harus kita perhatikan untuk menjaga keamanan selama melakukan transaksi <i>online</i>, seperti:
        </h4>""", unsafe_allow_html=True)
    st.markdown("""<ol>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Periksalah tujuan nomor rekening sebelum melakukan transaksi. Pastikan bahwa nama dan nomor rekening tujuan penerima transfer adalah benar. Jika ragu, kamu bisa mengunjungi situs cekrekening.id. yang dirilis oleh Kemkominfo.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Hindari penawaran yang terlalu menggiurkan, karena bisa jadi penipuan atau penawaran palsu.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Berhati-hatilah dengan <i>typosquatting</i> atau URL palsu. Jika ragu mengklik tautan di <i>email</i>, pastikan lihat terlebih dahulu kemana tujuan URL sebenarnya.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Gunakan <i>password</i> yang cukup aman, panjang dan kompleks.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Pastikan jaringan nirkabel yang terhubung aman. Hati-hati dengan penggunaan Wi-Fi publik/VPN gratis/ponsel orang lain yang memiliki tingkat kerentanan pada <i>mobile payment.</i></h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Pasang anti virus dan rutin perbarui agar terlindungi dari virus/<i>malware</i> dan kegiatan bertransaksi <i>online</i> (<i>internet banking</i>) menjadi aman.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Pastikan <i>log out</i> saat transaksi <i>online</i> (<i>internet banking</i>) selesai dilakukan.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Simpan bukti transaksi. Hal ini berguna untuk menelusuri jika terjadi kesalahan dalam transaksi.</h4></li>
        <li class='small-font'; style='color:yellow'><h4 class='small-font'; style='text-align: justify; color: white;'>Segera laporkan kepada pihak berwajib apabila terjadi transaksi yang tidak dikenal.</h4></li>
        </ol>
        """, unsafe_allow_html=True)

    # ---------- SUMBER PELENGKAP ----------
    st.markdown("<h4 style='text-align: left; color: cyan;'> Sumber Pelengkap: </h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: pink;'> Hendarsyah, D. (2012). Keamanan Layanan Internet Banking Dalam Transaksi Perbankan. IQTISHADUNA: Jurnal Ilmiah Ekonomi Kita, 1(1), 12-33. Dapat diakses pada: <a href='https://doi.org/10.46367/iqtishaduna.v1i1.2'>https://doi.org/10.46367/iqtishaduna.v1i1.2</a></h6>", unsafe_allow_html=True)

# *****************************************************************************
# ------------------------------- HALAMAN 5 -----------------------------------

# *****************************************************************************

def page5():

    def check_password():
        """Returns `True` if the user had a correct password."""

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if (
                st.session_state["username"] in st.secrets["passwords"]
                and st.session_state["password"]
                == st.secrets["passwords"][st.session_state["username"]]
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # don't store username + password
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False
        
        if "password_correct" not in st.session_state:
            # First run, show inputs for username + password.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            return False
        elif not st.session_state["password_correct"]:
            # Password not correct, show input + error.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 User not known or password incorrect")
            return False
        else:
            # Password correct.
            return True

    st.sidebar.markdown("# Berkontribusi Bersama Kami :memo:")

    # Functions

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')

    def create_table_guest():
        c.execute('CREATE TABLE IF NOT EXISTS blogtableguest(author TEXT,title TEXT,article TEXT,postdate DATE)')

    def add_data(author, title, article, postdate):
        c.execute('INSERT INTO blogtable(author, title, article, postdate) VALUES(?,?,?,?)',(author, title, article, postdate))
        conn.commit()

    def add_data_guest(author, title, article, postdate):
        c.execute('INSERT INTO blogtableguest(author, title, article, postdate) VALUES(?,?,?,?)',(author, title, article, postdate))
        conn.commit()

    def view_all_notes():
        c.execute('SELECT * FROM blogtable')
        data = c.fetchall()
        return data

    def view_guest():
        c.execute('SELECT * FROM blogtableguest')
        data = c.fetchall()
        return data

    def view_all_titles():
        c.execute('SELECT DISTINCT title FROM blogtable')
        data = c.fetchall()
        return data

    def get_blog_by_title(title):
        c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
        data = c.fetchall()
        return data

    def get_blog_by_author(author):
        c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
        data = c.fetchall()
        return data

    def delete_data(title):
        c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
        c.execute('DELETE FROM blogtableguest WHERE title="{}"'.format(title))
        conn.commit()

    # Layout Templates
    # html_temp = """
    # <div style="background-color:{};padding:10px;border-radius:10px">
    # <h1 style="color:{};text-align:center;">Simple Blog </h1>
    # </div>
    # """

    title_temp ="""
    <div style="background-color:  #196f3d;padding:10px;border-radius:25px;margin:10px;">
        <br/>
        <center><img src="https://flyclipart.com/thumb2/account-avatar-head-human-male-man-people-person-profile-873990.png" alt="Avatar" style="width:70px; height:65px; border-radius: 50%;" ></center>
        <h3 style="color:yellow;text-align:center;">{}</h3>
        <h5 style="color:orange;text-align:center;">Penulis: {}</h5>
    </div>
    """
    article_temp = """
    <div style="background-color: #196f3d;padding:10px;border-radius:5px;margin:10px;">
        <br/>
        <center><img src="https://flyclipart.com/thumb2/account-avatar-head-human-male-man-people-person-profile-873990.png" alt="Avatar" style="width:70px; height:65px; border-radius: 50%;" ></center>
        <h3 style="color:yellow;text-align:center;">{}</h3>
        <h5 style="color:orange;text-align:center;">Penulis: {}</h5>
        <h5 style="color:orange;text-align:center;">Tanggal Dikirim: {}</h5>
    </div>
    """
    head_message_temp = """
    <div style="background-color: #196f3d;padding:10px,border-radius:5px;margin:10px;">
        <br/>
        <center><img src="https://flyclipart.com/thumb2/account-avatar-head-human-male-man-people-person-profile-873990.png" alt="Avatar" style="width:70px; height:65px; border-radius: 50%;" ></center>
        <h3 style="color:yellow;text-align:center;">{}</h3>
        <h5 style="color:orange;text-align:center;">Penulis: {}</h5>
        <h5 style="color:orange;text-align:center;">Tanggal Dikirim: {}</h5>
    </div>
    """
    full_message_temp = """
    <div style="background-color:  #7dcea0  ;overflow-x: auto; padding:10px,border-radius:5px;margin:10px;">
        <h5 style="text-align:justify;color:black;padding:10px">{}</h5>
    </div>
    """


    def main():
        """A Simple CRUD Blog"""
        #st.title("Simple Blog")

        #menu = ["Home", "View Posts", "Add Posts", "Search", "Manage Blog"]
        menu = ["Tambah Artikel (Tamu)", "Tambah Artikel (Admin)", "Daftar Artikel", "Lihat Artikel", "Cari", "Lain-lain"]
        choice = st.sidebar.selectbox("Menu", menu)

        def header(url):
            st.markdown(f'<p style="background-color:#120967;color:#fefa06;font-size:17px;border-radius:5%;">{url}</p>', unsafe_allow_html=True)

            
        if choice == "Tambah Artikel (Tamu)":
            st.markdown("<h3 style='text-align: center; color: yellow;'>Kamu punya konten lain tentang transaksi <i>online</i> atau keamanan siber yang ingin dibagikan? Yuk, ikut berkontribusi bersama kami dengan menuliskan kontenmu sendiri. 📝</h3>", unsafe_allow_html=True)
            st.write(" ")
            with st.container():
                st.markdown("<h3 style='text-align: left; color: lime;'>Tambah Artikel</h3>", unsafe_allow_html=True)
                create_table_guest()
                #st.markdown("<p style='color:blue'>Masukkan Nama Penulis<p>", unsafe_allow_html=True)
                blog_author = st.text_input("Masukkan Nama Penulis", max_chars=50)
                blog_title = st.text_input("Masukkan Judul Artikel")
                blog_article = st.text_area("Tulis Artikel Di Sini", height=200) #bisa ditambah height=100
                blog_post_date = st.date_input("Tanggal")
                if st.button("Tambah"):
                    add_data_guest(blog_author,blog_title,blog_article,blog_post_date)
                    header('Artikel: "{}" disimpan'.format(blog_title))

        elif choice == "Tambah Artikel (Admin)":
            if check_password():
                st.markdown("<h3 style='text-align: center; color: yellow;'>Tambah Artikel (Admin) 📝</h3>", unsafe_allow_html=True)
                st.write(" ")
                with st.container():
                    #st.markdown("<h3 style='text-align: left; color: lime;'>Tambah Artikel</h3>", unsafe_allow_html=True)
                    create_table()
                    #st.markdown("<p style='color:blue'>Masukkan Nama Penulis<p>", unsafe_allow_html=True)
                    blog_author = st.text_input("Masukkan Nama Penulis", max_chars=50)
                    blog_title = st.text_input("Masukkan Judul Artikel")
                    blog_article = st.text_area("Tulis Artikel Di Sini", height=200) #bisa ditambah height=100
                    blog_post_date = st.date_input("Tanggal")
                    if st.button("Tambah"):
                        add_data(blog_author,blog_title,blog_article,blog_post_date)
                        header('Artikel: "{}" disimpan'.format(blog_title))

        elif choice == "Daftar Artikel":
            #st.subheader("Home")  
            menu = ["Artikel Pilihan", "Artikel Tamu"]
            choices = st.sidebar.selectbox("Menu", menu)
            if choices == "Artikel Pilihan":
                st.markdown("<h3 style='text-align: left; color: lime;'>Daftar Artikel</h3>", unsafe_allow_html=True)
                result = view_all_notes()
                #st.write(result)
                for i in result:
                    b_author = i[0]
                    b_title = i[1]
                    b_article = str(i[2])[0:30]
                    b_post_date = i[3]
                    #st.write(i[0]) #save data (menyimpan dan menampilkan data)
                    st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date),unsafe_allow_html=True)
            elif choices == "Artikel Tamu":
                if check_password():
                    st.markdown("<h3 style='text-align: left; color: lime;'>Daftar Artikel</h3>", unsafe_allow_html=True)
                    result = view_guest()
                    #st.write(result)
                    for i in result:
                        b_author = i[0]
                        b_title = i[1]
                        b_article = str(i[2])[0:30]
                        b_post_date = i[3]
                        #st.write(i[0]) #save data (menyimpan dan menampilkan data)
                        st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date),unsafe_allow_html=True)

        elif choice == "Lihat Artikel":
            st.markdown("<h3 style='text-align: left; color: lime;'>Lihat Artikel</h3>", unsafe_allow_html=True)
            all_titles = [i[0] for i in view_all_titles()]
            postlist = st.sidebar.selectbox("Lihat Artikel", all_titles)
            post_result = get_blog_by_title(postlist)
            for i in post_result:
                b_author = i[0]
                b_title = i[1]
                b_article = i[2]
                b_post_date = i[3]
                st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
                st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)


        elif choice == "Cari":
            st.markdown("<h3 style='text-align: left; color: lime;'>Cari Artikel</h3>", unsafe_allow_html=True)
            search_term = st.text_input('Cari Artikel Berdasarkan Judul atau Penulis')
            search_choice = st.radio("Pilih Cari Berdasarkan:", ("judul","penulis"))
            
            if st.button("Cari"):
                if search_choice == "judul":
                    article_result = get_blog_by_title(search_term)
                elif search_choice == "penulis":
                    article_result = get_blog_by_author(search_term)

                for i in article_result:
                    b_author = i[0]
                    b_title = i[1]
                    b_article = i[2]
                    b_post_date = i[3]
                    st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
                    st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)

        elif choice == "Lain-lain":
            st.markdown("<h3 style='text-align: left; color: lime;'>Penghapusan & Data Artikel</h3>", unsafe_allow_html=True)

            result = view_all_notes()
            clean_db = pd.DataFrame(result,columns=["Penulis","Judul","Artikel","Tanggal"])
            

            if check_password():
                st.dataframe(clean_db)
                unique_titles = [i[0] for i in view_all_titles()]
                delete_blog_by_title = st.selectbox("Judul Artikel yang Dipilih", unique_titles)

                if st.button("Hapus"):
                    delete_data(delete_blog_by_title)
                    st.warning("Artikel Dihapus: '{}'".format(delete_blog_by_title))

            new_df = clean_db

            if st.checkbox("Metrik"):
                new_df['Panjang Karakter'] = new_df['Artikel'].str.len()
                st.dataframe(new_df)

                st.subheader("Statistik Penulis")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                new_df["Penulis"].value_counts().plot(kind='bar')
                st.pyplot()

                st.subheader("Statistik Penulis")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                new_df["Penulis"].value_counts().plot.pie(autopct="%.2f%%")
                st.pyplot()

            # if st.checkbox("Word Cloud"):
            #     st.subheader("Generate Word Cloud")
            #     #text = new_df['Articles'].iloc[0]
            #     text = ','.join(new_df['Articles'])
            #     wordcloud = WordCloud().generate(text)
            #     plt.imshow(wordcloud,interpolation='bilinear')
            #     plt.axis("off")
            #     st.pyplot()

            # if st.checkbox("BarH Plot"):
            #     st.subheader("Length of Articles")
            #     new_df = clean_db
            #     new_df['Length'] = new_df['Articles'].str.len()
            #     barh_plot = new_df.plot.barh(x='Author',y='Length',figsize=(20,10))
            #     st.pyplot()

    if __name__ == '__main__':
        main()


# *****************************************************************************
# --------------------------- HALAMAN 6 (TERAKHIR) ----------------------------

# *****************************************************************************
def page6():
    # mengatur ukuran huruf secara fleksibel
    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Membuat huruf pertama lebih besar (warna lime)
    st.markdown("""
    <style>
    p::first-letter {
      font-size: 150%;
      color: #00FF00; 
    }
    </style>
    """, unsafe_allow_html=True)

    # membaca kode css dari file "style.css" (template untuk memperbagus tampilan kotak kritik & saran)
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")

    st.markdown("<h1 style='text-align: center; color: white;'> Terima Kasih Sudah Membaca! 😄 </h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'> Semoga informasi yang kami sampaikan bermanfaat. </h2>", unsafe_allow_html=True)
    lottie_pic = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_oft66j9r.json")
    st_lottie(lottie_pic, height=250)
    st.markdown("<h3 style='text-align: center; color: yellow;'> Konten dan <i>web apps</i> ini dibuat oleh Kelompok MAL(a)ware sebagai proyek akhir dari Pelatihan <i>Women in Tech: Cybersecurity and Python</i> yang diselenggarakan oleh Digitalent Kemkominfo tahun 2022.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: yellow;'>Kelompok MAL(a)ware beranggotakan kami bertiga: </h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<p class='big-font'; style='text-align: center; color: white;'> Mariska Putri Nur Hidayah </p>", unsafe_allow_html=True)
        #st.markdown("<h3 style='text-align: center; color: yellow;'>(1463161100-1229)</h3>", unsafe_allow_html=True)
    with col2:
        st.markdown("<p class='big-font'; style='text-align: center; color: white;'> Anna Amandha </p>", unsafe_allow_html=True)   
        #st.markdown("<h3 style='text-align: center; color: yellow;'>(1463161100-1195)</h3>", unsafe_allow_html=True)
    with col3:
        st.markdown("<p class='big-font'; style='text-align: center; color: white;'> Lia Dwi Apriesty </p>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center; color: yellow;'>(1463161100-1229) ----- (1463161100-1195) ----- (1463161100-1208)</h4>", unsafe_allow_html=True)
    
    with st.container():
        st.write("---")
        st.markdown("<h2 style='color:lime'>Apa kamu punya kritik dan saran? Sampaikan di bawah ini, ya!</h2>", unsafe_allow_html=True)
        st.write("##")

    # --------------- TEMPLATE DARI FORMSUBMIT (KOTAK KRITIK & SARAN) ---------------
    contact_form = """
    <form action="https://formsubmit.co/anna.amandha@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nama" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Ketik pesanmu di sini" required></textarea>
     <button type="submit">Kirim</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        lottie_pic = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_pw5a608o.json")
        st_lottie(lottie_pic, height=250)

# *****************************************************************
# --------------- DICTIONARY UNTUK NAVIGASI HALAMAN ---------------

# *****************************************************************
page_names_to_funcs = {
    "Beranda": main_page,
    "Transaksi Online": page2,
    "Serangan Kejahatan Siber dalam Bertransaksi Online": page3,
    "Tips Mencegah Kejahatan Siber dalam Bertransaksi Online": page4,
    "Berkontribusi Bersama Kami": page5,
    "Akhir Halaman": page6,
}

# memuat logo Kelompok MAL-ware dari cooltext.com
#st.sidebar.markdown('<center> <a href="https://picasion.com/gl/g8mc/"><img src="https://i.picasion.com/gl/92/g8mc.gif" width="272" height="61" border="0" alt="https://picasion.com/gl/g8mc/" /></a><br /><a href="https://picasion.com/gl/g8mc/"></a> </center>', unsafe_allow_html=True)
st.sidebar.markdown('<center> <a href="https://cooltext.com"><img src="https://images.cooltext.com/5615367.png" width="290" height="72" alt="MAL(a)ware" /></a></a> </center>', unsafe_allow_html=True)

st.sidebar.markdown(" ")
st.sidebar.markdown(" ")

selected_page = st.sidebar.radio("Pilih halaman", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
