create table account_customuser_user_permissions
(
    id            integer not null
        primary key autoincrement,
    customuser_id integer not null
        references account_customuser
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index account_customuser_user_permissions_customuser_id_03bcc114
    on account_customuser_user_permissions (customuser_id);

create unique index account_customuser_user_permissions_customuser_id_permission_id_650e378f_uniq
    on account_customuser_user_permissions (customuser_id, permission_id);

create index account_customuser_user_permissions_permission_id_f4aec423
    on account_customuser_user_permissions (permission_id);

