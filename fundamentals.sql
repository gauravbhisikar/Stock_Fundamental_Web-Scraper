PGDMP     7    ,                x            fundamentals    12.1    12.1                 0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16418    fundamentals    DATABASE     �   CREATE DATABASE fundamentals WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
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
    index bigint NOT NULL
);
 $   DROP TABLE public.fundamental_data;
       public         heap    postgres    false           