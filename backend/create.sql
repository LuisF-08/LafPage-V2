-- public.clientes definição

-- Drop table

-- DROP TABLE public.clientes;

CREATE TABLE public.clientes (
	id serial4 NOT NULL,
	nome varchar(255) NULL,
	whatsapp varchar(20) NULL,
	email varchar(80) NULL,
	cnpj text NULL,
	criado_em timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT clientes_pkey PRIMARY KEY (id)
);

-- public.pedidos definição

-- Drop table

-- DROP TABLE public.pedidos;

CREATE TABLE public.pedidos (
	id serial4 NOT NULL,
	id_cliente int4 NULL,
	cnpj varchar(14) NULL,
	empresa_ou_grupo varchar(255) NULL,
	numero_pedido int4 NULL,
	nota_fiscal int4 NULL,
	codigo_produto int4 NULL,
	nome_produto varchar(255) NULL,
	valor_total numeric(20, 2) NULL,
	quantidade int4 NULL,
	solicitado timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT pedidos_pkey PRIMARY KEY (id),
	CONSTRAINT pedidos_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.clientes(id)
);

-- public.sac_formulario definição

-- Drop table

-- DROP TABLE public.sac_formulario;

CREATE TABLE public.sac_formulario (
	id serial4 NOT NULL,
	nome text NULL,
	email text NULL,
	contato text NULL,
	nota_fiscal varchar(20) NULL,
	assunto text NULL,
	problema text NULL,
	descricao text NULL,
	situacao varchar(20) DEFAULT 'enviado'::character varying NULL,
	data_solicitado timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	arquivo text NULL,
	CONSTRAINT sac_formulario_pkey PRIMARY KEY (id)
);

CREATE TABLE public.sac_itens (
	id serial4 NOT NULL,
	formulario_id int4 NOT NULL,
	produto_id int4 NULL,
	nome_produto text NULL,
	quantidade_original int4 NULL,
	quantidade_devolucao int4 NULL,
	CONSTRAINT sac_itens_pkey PRIMARY KEY (id),
	CONSTRAINT fk_formulario FOREIGN KEY (formulario_id) REFERENCES public.sac_formulario(id) ON DELETE CASCADE
);