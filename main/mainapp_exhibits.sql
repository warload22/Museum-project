create table mainapp_exhibits
(
    id           integer      not null
        primary key autoincrement,
    name         varchar(128) not null,
    image        varchar(100) not null,
    descriptions text,
    category_id  bigint       not null
        references mainapp_exhibitscategories
            deferrable initially deferred
);

create index mainapp_exhibits_category_id_c54cc410
    on mainapp_exhibits (category_id);

