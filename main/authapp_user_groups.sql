create table authapp_user_groups
(
    id       integer not null
        primary key autoincrement,
    user_id  bigint  not null
        references authapp_user
            deferrable initially deferred,
    group_id integer not null
        references auth_group
            deferrable initially deferred
);

create index authapp_user_groups_group_id_361087d7
    on authapp_user_groups (group_id);

create index authapp_user_groups_user_id_aad8a001
    on authapp_user_groups (user_id);

create unique index authapp_user_groups_user_id_group_id_532435ff_uniq
    on authapp_user_groups (user_id, group_id);

