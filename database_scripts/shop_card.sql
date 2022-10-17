create table shop_card
(
    id            integer          not null
        primary key autoincrement,
    image         varchar(100)     not null,
    title         varchar(128)     not null,
    description   varchar(512)     not null,
    price         real             not null,
    favorite      integer unsigned not null,
    views         integer unsigned not null,
    slug          varchar(50)      not null
        unique,
    category_id   integer
        references shop_category
            deferrable initially deferred,
    creator_id    integer
        references account_customuser
            deferrable initially deferred,
    owner_id      integer
        references account_customuser
            deferrable initially deferred,
    creation_time datetime         not null,
    check ("favorite" >= 0),
    check ("views" >= 0)
);

create index shop_card_category_id_96835da3
    on shop_card (category_id);

create index shop_card_creator_id_b5d81653
    on shop_card (creator_id);

create index shop_card_owner_id_e5d6ed39
    on shop_card (owner_id);

