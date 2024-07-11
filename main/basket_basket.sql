create table basket_basket
(
    id               integer          not null
        primary key autoincrement,
    quantity         integer unsigned not null,
    create_timestamp datetime         not null,
    update_timestamp datetime         not null,
    user_id          bigint           not null
        references authapp_user
            deferrable initially deferred,
    product_id       bigint           not null
        references mainapp_exhibits
            deferrable initially deferred,
    check ("quantity" >= 0)
);

create index basket_basket_product_id_838af4d3
    on basket_basket (product_id);

create index basket_basket_user_id_64ce4265
    on basket_basket (user_id);

