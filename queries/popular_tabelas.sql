INSERT INTO estados (sigla, nome)
VALUES ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins');
INSERT INTO cidades (nome, estado_id)
VALUES ('Rio Branco', 1),
    ('Maceió', 2),
    ('Macapá', 3),
    ('Manaus', 4),
    ('Salvador', 5),
    ('Fortaleza', 6),
    ('Brasília', 7),
    ('Vitória', 8),
    ('Goiânia', 9),
    ('São Luís', 10),
    ('Cuiabá', 11),
    ('Campo Grande', 12),
    ('Belo Horizonte', 13),
    ('Belém', 14),
    ('João Pessoa', 15),
    ('Curitiba', 16),
    ('Recife', 17),
    ('Teresina', 18),
    ('Rio de Janeiro', 19),
    ('Natal', 20),
    ('Porto Alegre', 21),
    ('Porto Velho', 22),
    ('Boa Vista', 23),
    ('Florianópolis', 24),
    ('São Paulo', 25),
    ('Aracaju', 26),
    ('Palmas', 27),
    ('Guarulhos', 25),
    ('Osasco', 25),
    ('Barueri', 25),
    ('Carapicuíba', 25),
    ('Itapevi', 25),
    ('Jandira', 25),
    ('Santana de Parnaíba', 25),
    ('Cajamar', 25),
    ('Caieiras', 25),
    ('Franco da Rocha', 25),
    ('Francisco Morato', 25),
    ('Mairiporã', 25),
    ('Embu das Artes', 25),
    ('Embu-Guaçu', 25),
    ('Cotia', 25),
    ('Itapecerica da Serra', 25),
    ('Taboão da Serra', 25),
    ('Vargem Grande Paulista', 25),
    ('Arujá', 25),
    ('Itaquaquecetuba', 25),
    ('Mogi das Cruzes', 25),
    ('Poá', 25),
    ('Suzano', 25),
    ('Santa Isabel', 25),
    ('Ferraz de Vasconcelos', 25),
    ('Santo André', 25),
    ('São Bernardo do Campo', 25),
    ('São Caetano do Sul', 25),
    ('Diadema', 25),
    ('Mauá', 25),
    ('Ribeirão Pires', 25),
    ('Rio Grande da Serra', 25),
    ('Jundiaí', 25),
    ('Campinas', 25),
    ('Piracicaba', 25),
    ('Piracaia', 25),
    ('Praia Grande', 25),
    ('Mongaguá', 25);
INSERT INTO entidades (
        nome,
        fundacao,
        cidade_id,
        telefone,
        criado_em,
        url,
        email
    )
VALUES (
        'Lar da Mamãe Clory',
        '1969-01-01 00:00:00+00',
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        '(11) 4109-2773',
        NOW(),
        'https://www.mamaeclory.org.br/',
        'diretoria@mamaeclory.org.br'
    ),
    (
        'Instituto Jésue - Acolhimento para Moradores de Rua',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'Santo André'
        ),
        '(11) 93342-3793',
        NOW(),
        'https://www.institutojesue.org.br/contatos/',
        'lefj@lejf.org.br'
    ),
    (
        'CIHESEL',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Paulo'
        ),
        '(11) 2091-3772',
        NOW(),
        'https://cihesel.ong.br/',
        'contato@cihesel.ong.br'
    ),
    (
        'Instituição Anjos da Leste de São Paulo',
        '2013-01-01 00:00:00+00',
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Paulo'
        ),
        '(11) 95052-2407',
        NOW(),
        'https://www.anjosdaleste.org.br/',
        NULL
    ),
    (
        'Sindbeneficente - Subsede São Bernardo do Campo',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        '(11) 2598-7479',
        NOW(),
        'https://sindbeneficente.org.br/',
        NULL
    ),
    (
        'Casa Solidária Paulicéia',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Núcleo Assistencial Assunção',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Projeto Comunitário Rudge Ramos',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Rede de Apoio Vila São Pedro',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Bernardo do Campo'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Centro Social Piraporinha',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'Diadema'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Projeto Acolher Centro Diadema',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'Diadema'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Casa Fraterna Vila Conceição',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'Diadema'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Núcleo Esperança Santo André',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'Santo André'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    ),
    (
        'Rede Beneficente Tatuapé',
        NULL,
        (
            SELECT id
            FROM cidades
            WHERE nome = 'São Paulo'
        ),
        NULL,
        NOW(),
        NULL,
        NULL
    );

INSERT INTO itens_estoque (
        entidade_id,
        produto,
        categoria,
        quantidade_atual,
        quantidade_necessaria,
        unidade,
        atualizado_em
    )
VALUES
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Arroz',
        'alimento_nao_perecivel',
        50.0,
        200.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Feijão',
        'alimento_nao_perecivel',
        40.0,
        180.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Macarrão',
        'alimento_nao_perecivel',
        30.0,
        150.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Açúcar',
        'alimento_nao_perecivel',
        20.0,
        120.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Óleo de soja',
        'alimento_nao_perecivel',
        15.0,
        80.0,
        'L',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Café',
        'alimento_nao_perecivel',
        10.0,
        40.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Leite em pó',
        'alimento_nao_perecivel',
        25.0,
        100.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Farinha de trigo',
        'alimento_nao_perecivel',
        18.0,
        60.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Fubá',
        'alimento_nao_perecivel',
        12.0,
        50.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Milho em conserva',
        'alimento_nao_perecivel',
        30.0,
        90.0,
        'un',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Detergente',
        'limpeza',
        40.0,
        100.0,
        'un',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Desinfetante',
        'limpeza',
        20.0,
        60.0,
        'L',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'Lar da Mamãe Clory'
        ),
        'Sabão em pó',
        'limpeza',
        25.0,
        80.0,
        'kg',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Produto multiuso',
        'limpeza',
        15.0,
        50.0,
        'L',
        NOW()
    ),
    (
        (
            SELECT id
            FROM entidades
            WHERE nome = 'CIHESEL'
        ),
        'Água sanitária',
        'limpeza',
        10.0,
        40.0,
        'L',
        NOW()
    );