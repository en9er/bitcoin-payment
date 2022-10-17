create table wallet_wallet
(
    id             integer      not null
        primary key autoincrement,
    is_activated   bool         not null,
    address        varchar(256) not null
        unique,
    public_key     varchar(256) not null,
    addiction_info varchar(256)
);

