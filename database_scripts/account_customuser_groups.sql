create table account_customuser_groups
(
    id            integer not null
        primary key autoincrement,
    customuser_id integer not null
        references account_customuser
            deferrable initially deferred,
    group_id      integer not null
        references auth_group
            deferrable initially deferred
);

create index account_customuser_groups_customuser_id_b6c60904
    on account_customuser_groups (customuser_id);

create unique index account_customuser_groups_customuser_id_group_id_7e51db7b_uniq
    on account_customuser_groups (customuser_id, group_id);

create index account_customuser_groups_group_id_2be9f6d7
    on account_customuser_groups (group_id);

