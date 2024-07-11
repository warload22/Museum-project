create table authapp_user_user_permissions
(
    id            integer not null
        primary key autoincrement,
    user_id       bigint  not null
        references authapp_user
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index authapp_user_user_permissions_permission_id_ea3ff82e
    on authapp_user_user_permissions (permission_id);

create index authapp_user_user_permissions_user_id_fb111ce4
    on authapp_user_user_permissions (user_id);

create unique index authapp_user_user_permissions_user_id_permission_id_d73ed934_uniq
    on authapp_user_user_permissions (user_id, permission_id);

