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
-- Name: vuz; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE vuz WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';


ALTER DATABASE vuz OWNER TO postgres;

\connect vuz

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department (
    id integer NOT NULL,
    name text,
    phone text
);


ALTER TABLE public.department OWNER TO postgres;

--
-- Name: discipline; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.discipline (
    subject_code integer NOT NULL,
    subject_name text,
    hours integer,
    student_id integer
);


ALTER TABLE public.discipline OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    id integer NOT NULL,
    number_of_student_book integer,
    full_name text,
    group_name text,
    city text
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    teacher_number integer NOT NULL,
    full_name text,
    academic_degree text,
    department_id integer,
    discipline_id integer
);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department (id, name, phone) FROM stdin;
1	test	123456
2	Кафедра	1235436534
4	TestKafedra	+755235325
\.


--
-- Data for Name: discipline; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.discipline (subject_code, subject_name, hours, student_id) FROM stdin;
1	Матан	500	1
2	Русский	150	2
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (id, number_of_student_book, full_name, group_name, city) FROM stdin;
1	10000	Student	123	Киров
2	2231213	Student	1	1
3	123	Иванов Иван Иванович	102-52-00	Kirov
\.


--
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher (teacher_number, full_name, academic_degree, department_id, discipline_id) FROM stdin;
1	Преподаватель	1	1	1
2	2	2	1	1
3	Крутиков Александр Константинович	5	4	2
\.


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id);


--
-- Name: discipline discipline_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discipline
    ADD CONSTRAINT discipline_pkey PRIMARY KEY (subject_code);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: teacher teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (teacher_number);


--
-- Name: discipline discipline_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discipline
    ADD CONSTRAINT discipline_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(id);


--
-- Name: teacher teacher_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(id);


--
-- Name: teacher teacher_discipline_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_discipline_id_fkey FOREIGN KEY (discipline_id) REFERENCES public.discipline(subject_code);


--
-- PostgreSQL database dump complete
--

