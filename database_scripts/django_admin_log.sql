create table django_admin_log
(
    id              integer           not null
        primary key autoincrement,
    action_time     datetime          not null,
    object_id       text,
    object_repr     varchar(200)      not null,
    change_message  text              not null,
    content_type_id integer
        references django_content_type
            deferrable initially deferred,
    user_id         integer           not null
        references account_customuser
            deferrable initially deferred,
    action_flag     smallint unsigned not null,
    check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

