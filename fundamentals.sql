PGDMP         )                x            fundamentals    12.1    12.1     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16418    fundamentals    DATABASE     �   CREATE DATABASE fundamentals WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE fundamentals;
                postgres    false            �            1259    16460    fundamental_data    TABLE     �  CREATE TABLE public.fundamental_data (
    "TICKER" text,
    c_mc double precision,
    c_cp double precision,
    c_52h double precision,
    c_52l double precision,
    c_bv double precision,
    c_pe double precision,
    c_dy double precision,
    c_roce double precision,
    c_roe double precision,
    c_sg3 double precision,
    c_fv double precision,
    c_roa double precision,
    c_atr double precision,
    c_pbv double precision,
    c_debt double precision,
    c_ph double precision,
    c_pleg double precision,
    c_pg double precision,
    c_pat double precision,
    c_pts double precision,
    c_enpv double precision,
    c_peg_r double precision,
    c_cr double precision,
    c_dte double precision,
    c_icr double precision,
    c_itr double precision,
    c_dpr double precision,
    c_qr double precision,
    pros text,
    cons text,
    s_bv double precision,
    s_pe double precision,
    s_roce double precision,
    s_roe double precision,
    s_sg3 double precision,
    s_roa double precision,
    s_atr double precision,
    s_pbv double precision,
    s_debt double precision,
    s_pg double precision,
    s_pat double precision,
    s_pts double precision,
    s_enpv double precision,
    s_peg_r double precision,
    s_cr double precision,
    s_dte double precision,
    s_icr double precision,
    s_itr double precision,
    s_dpr double precision,
    s_qr double precision,
    "INDEX" bigint
);
 $   DROP TABLE public.fundamental_data;
       public         heap    postgres    false            �
          0    16460    fundamental_data 
   TABLE DATA           �  COPY public.fundamental_data ("TICKER", c_mc, c_cp, c_52h, c_52l, c_bv, c_pe, c_dy, c_roce, c_roe, c_sg3, c_fv, c_roa, c_atr, c_pbv, c_debt, c_ph, c_pleg, c_pg, c_pat, c_pts, c_enpv, c_peg_r, c_cr, c_dte, c_icr, c_itr, c_dpr, c_qr, pros, cons, s_bv, s_pe, s_roce, s_roe, s_sg3, s_roa, s_atr, s_pbv, s_debt, s_pg, s_pat, s_pts, s_enpv, s_peg_r, s_cr, s_dte, s_icr, s_itr, s_dpr, s_qr, "INDEX") FROM stdin;
    public          postgres    false    202   �       �
      x������ � �     