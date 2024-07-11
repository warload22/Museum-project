create table authapp_user
(
    id           integer          not null
        primary key autoincrement,
    password     varchar(128)     not null,
    last_login   datetime,
    is_superuser bool             not null,
    username     varchar(150)     not null
        unique,
    first_name   varchar(150)     not null,
    last_name    varchar(150)     not null,
    email        varchar(254)     not null,
    is_staff     bool             not null,
    is_active    bool             not null,
    date_joined  datetime         not null,
    image        varchar(100)     not null,
    age          integer unsigned not null,
    check ("age" >= 0)
);

