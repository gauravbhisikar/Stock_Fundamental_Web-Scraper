PGDMP                         x            fundamentals    12.3    12.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16418    fundamentals    DATABASE     �   CREATE DATABASE fundamentals WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE fundamentals;
                postgres    false            �            1259    24675    fundamental_data    TABLE       CREATE TABLE public.fundamental_data (
    index bigint,
    date date,
    ticker text,
    c_mc bigint,
    c_cp numeric,
    c_52h numeric,
    c_52l numeric,
    c_bv numeric,
    c_pe numeric,
    c_dy numeric,
    c_roce numeric,
    c_roe numeric,
    c_sg3 numeric,
    c_fv numeric,
    c_roa numeric,
    c_atr numeric,
    c_pbv numeric,
    c_debt numeric,
    c_ph numeric,
    c_pleg numeric,
    c_pg numeric,
    c_pat numeric,
    c_pts numeric,
    c_enpv bigint,
    c_peg_r numeric,
    c_cr numeric,
    c_dte numeric,
    c_icr numeric,
    c_itr numeric,
    c_dpr numeric,
    c_qr numeric,
    pros text,
    cons text,
    s_bv numeric,
    s_pe numeric,
    s_roce numeric,
    s_roe numeric,
    s_sg3 numeric,
    s_roa numeric,
    s_atr numeric,
    s_pbv numeric,
    s_debt numeric,
    s_pg numeric,
    s_pat numeric,
    s_pts numeric,
    s_enpv bigint,
    s_peg_r numeric,
    s_cr numeric,
    s_dte numeric,
    s_icr numeric,
    s_itr numeric,
    s_dpr numeric,
    s_qr numeric
);
 $   DROP TABLE public.fundamental_data;
       public         heap    postgres    false            �
          0    24675    fundamental_data 
   TABLE DATA           �  COPY public.fundamental_data (index, date, ticker, c_mc, c_cp, c_52h, c_52l, c_bv, c_pe, c_dy, c_roce, c_roe, c_sg3, c_fv, c_roa, c_atr, c_pbv, c_debt, c_ph, c_pleg, c_pg, c_pat, c_pts, c_enpv, c_peg_r, c_cr, c_dte, c_icr, c_itr, c_dpr, c_qr, pros, cons, s_bv, s_pe, s_roce, s_roe, s_sg3, s_roa, s_atr, s_pbv, s_debt, s_pg, s_pat, s_pts, s_enpv, s_peg_r, s_cr, s_dte, s_icr, s_itr, s_dpr, s_qr) FROM stdin;
    public          postgres    false    203   ;
       �
      x������ � �     