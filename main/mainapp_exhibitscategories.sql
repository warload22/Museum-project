create table mainapp_exhibitscategories
(
    id           integer     not null
        primary key autoincrement,
    descriptions text,
    name         varchar(64) not null
);

