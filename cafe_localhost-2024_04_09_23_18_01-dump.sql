--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    status uuid,
    start_order character varying(255) NOT NULL,
    end_order character varying(255) NOT NULL,
    createdat timestamp without time zone DEFAULT now() NOT NULL,
    updatedat timestamp without time zone DEFAULT now() NOT NULL,
    deletedat timestamp without time zone
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- Name: role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name character varying(255)
);


ALTER TABLE public.role OWNER TO postgres;

--
-- Name: shift; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shift (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    date_shift character varying(255) NOT NULL,
    start_shift character varying(255) NOT NULL,
    end_shift character varying(255) NOT NULL,
    createdat timestamp without time zone DEFAULT now() NOT NULL,
    updatedat timestamp without time zone DEFAULT now() NOT NULL,
    deletedat timestamp without time zone
);


ALTER TABLE public.shift OWNER TO postgres;

--
-- Name: shift_order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shift_order (
    id_shift uuid,
    id_order uuid
);


ALTER TABLE public.shift_order OWNER TO postgres;

--
-- Name: shift_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shift_user (
    id_shift uuid,
    id_user uuid
);


ALTER TABLE public.shift_user OWNER TO postgres;

--
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.status (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name character varying(255)
);


ALTER TABLE public.status OWNER TO postgres;

--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    role uuid,
    createdat timestamp without time zone DEFAULT now() NOT NULL,
    updatedat timestamp without time zone DEFAULT now() NOT NULL,
    deletedat timestamp without time zone,
    password character varying(255) NOT NULL,
    status character varying(255) NOT NULL,
    name character varying(255)
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."order" (id, status, start_order, end_order, createdat, updatedat, deletedat) FROM stdin;
7f07f217-7416-4488-b2b8-29a6a7849729	b86e7fc4-ddb6-4e0f-915c-2553814933cc	00:00	00:00	2024-04-09 20:54:53.950359	2024-04-09 20:54:53.950359	\N
2fc0fe70-5bf9-4bf7-b73d-0a97498de7f1	b86e7fc4-ddb6-4e0f-915c-2553814933cc	00:00	00:00	2024-04-09 20:57:12.880859	2024-04-09 20:57:12.880859	\N
db2d626c-0abe-4dac-bf2f-a2c07359be70	a1cbdf32-1c8e-41a5-bdc4-3a385eda7b4a	00:00	00:00	2024-04-09 20:55:10.560711	2024-04-09 20:55:10.560711	\N
30463885-d85a-4b51-9c39-c547e13bb266	62eb4cf5-47d0-4252-ae9a-15d5234fcf76	2024-04-08 20:23:24.804445	2024-04-09 20:23:24.804445	2024-04-08 20:23:24.804445	2024-04-08 20:23:24.804445	\N
8396078c-a6ef-43c5-b396-3ef5d60326ab	28dfc37c-3ce4-444e-8b8a-6f390ddf1f98	00:00	00:00	2024-04-09 20:54:53.495871	2024-04-09 20:54:53.495871	\N
\.


--
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.role (id, name) FROM stdin;
851e3ee5-4887-43ec-970d-9136f4afd1b8	Администратор
e5ca06c1-ed12-4691-ace3-835223f3e6eb	Повар
4f6798ff-8832-4b6e-a937-3d1b817e8325	Клиент
2eee9fc2-eb82-440c-af11-cd2353e9699b	Официант
\.


--
-- Data for Name: shift; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shift (id, date_shift, start_shift, end_shift, createdat, updatedat, deletedat) FROM stdin;
11d6e641-bf34-4acd-9ce5-d9f9432b32b4	01/01/2024	1	2	2024-04-09 19:32:59.137575	2024-04-09 19:32:59.137575	\N
1e0179f8-a121-4789-a45e-e93c32605861	0	00:00	00:00	2024-04-09 22:53:02.778686	2024-04-09 22:53:02.778686	\N
3a499327-0a84-41fb-9a78-336f9fbc148b	0	00:00	00:00	2024-04-09 22:53:53.90306	2024-04-09 22:53:53.90306	\N
c1c2db60-4853-44c6-91e4-27c7a3221383	0	00:00	00:00	2024-04-09 22:54:29.099724	2024-04-09 22:54:29.099724	\N
b2bc4354-78a0-4e05-b964-c4f9f9242049	0	00:00	00:00	2024-04-09 22:54:44.877958	2024-04-09 22:54:44.877958	\N
fc754936-0ba4-4900-8762-6d82168d0e97	0	00:00	00:00	2024-04-09 22:55:42.167195	2024-04-09 22:55:42.167195	\N
bbd0554c-2b06-48b3-b829-c22d699d4baa	0	00:00	00:00	2024-04-09 22:56:16.006861	2024-04-09 22:56:16.006861	\N
e8673478-0ccb-469e-a515-37c313d6f66b	0	00:00	00:00	2024-04-09 22:56:42.893854	2024-04-09 22:56:42.893854	\N
863df4b5-ec1c-48c3-840d-e43e924471aa	0	00:00	00:00	2024-04-09 22:57:18.659504	2024-04-09 22:57:18.659504	\N
d32a45c5-1272-4e68-a75a-172d0f54cecf	0	00:00	00:00	2024-04-09 22:57:54.025454	2024-04-09 22:57:54.025454	\N
\.


--
-- Data for Name: shift_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shift_order (id_shift, id_order) FROM stdin;
\.


--
-- Data for Name: shift_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shift_user (id_shift, id_user) FROM stdin;
11d6e641-bf34-4acd-9ce5-d9f9432b32b4	c2a4305b-b7f9-404c-8c8a-dae9384e2e4f
1e0179f8-a121-4789-a45e-e93c32605861	c2a4305b-b7f9-404c-8c8a-dae9384e2e4f
\.


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.status (id, name) FROM stdin;
66ce9494-d5b8-4341-a737-ce7f7f814d8a	test2
b86e7fc4-ddb6-4e0f-915c-2553814933cc	Принят
a1cbdf32-1c8e-41a5-bdc4-3a385eda7b4a	Оплачен
28dfc37c-3ce4-444e-8b8a-6f390ddf1f98	Готов
62eb4cf5-47d0-4252-ae9a-15d5234fcf76	Готовится
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, role, createdat, updatedat, deletedat, password, status, name) FROM stdin;
c2a4305b-b7f9-404c-8c8a-dae9384e2e4f	851e3ee5-4887-43ec-970d-9136f4afd1b8	2024-04-07 23:33:44.680302	2024-04-07 23:33:44.680302	\N	gfdgdfg	Работает	user
dbf63350-92da-40f7-9cf4-86a392d9cf1a	e5ca06c1-ed12-4691-ace3-835223f3e6eb	2024-04-07 23:55:24.153377	2024-04-07 23:55:24.153377	\N	123	Уволен	admin
f324ee6a-3761-45b1-93aa-27e86481e27e	2eee9fc2-eb82-440c-af11-cd2353e9699b	2024-04-09 17:40:40.918417	2024-04-09 17:40:40.918417	\N	111	Работает	ivan
736b353b-6990-4b59-a6bc-a53ddbf52d38	851e3ee5-4887-43ec-970d-9136f4afd1b8	2024-04-09 21:48:16.821692	2024-04-09 21:48:16.821692	\N	1231	Работает	1231
25a6cd20-e53a-4ad8-9d7d-8b4eb9c85b06	851e3ee5-4887-43ec-970d-9136f4afd1b8	2024-04-07 23:34:39.759796	2024-04-07 23:34:39.759796	\N	889988	Уволен	admin2
285c7c10-c1bb-4780-895a-66eacbad9ab9	e5ca06c1-ed12-4691-ace3-835223f3e6eb	2024-04-07 23:56:27.221175	2024-04-07 23:56:27.221175	\N	123	Уволен	user2
129a692a-a229-41ee-a886-da0a4638d66c	851e3ee5-4887-43ec-970d-9136f4afd1b8	2024-04-09 22:04:52.45949	2024-04-09 22:04:52.45949	\N	123	Работает	US
ef94a5bc-8b1d-4f34-9040-6fe05b84b481	851e3ee5-4887-43ec-970d-9136f4afd1b8	2024-04-09 22:05:18.986319	2024-04-09 22:05:18.986319	\N	123	Работает	USESR
\.


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- Name: role role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);


--
-- Name: shift shift_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift
    ADD CONSTRAINT shift_pkey PRIMARY KEY (id);


--
-- Name: status status_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pk UNIQUE (name);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (id);


--
-- Name: status unique_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT unique_name UNIQUE (name);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: order order_status_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_status_fkey FOREIGN KEY (status) REFERENCES public.status(id);


--
-- Name: shift_order shift_order_id_order_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift_order
    ADD CONSTRAINT shift_order_id_order_fkey FOREIGN KEY (id_order) REFERENCES public."order"(id);


--
-- Name: shift_order shift_order_id_shift_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift_order
    ADD CONSTRAINT shift_order_id_shift_fkey FOREIGN KEY (id_shift) REFERENCES public.shift(id);


--
-- Name: shift_user shift_user_id_shift_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift_user
    ADD CONSTRAINT shift_user_id_shift_fkey FOREIGN KEY (id_shift) REFERENCES public.shift(id);


--
-- Name: shift_user shift_user_id_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift_user
    ADD CONSTRAINT shift_user_id_user_fkey FOREIGN KEY (id_user) REFERENCES public."user"(id);


--
-- Name: user user_role_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_role_fkey FOREIGN KEY (role) REFERENCES public.role(id);


--
-- PostgreSQL database dump complete
--

