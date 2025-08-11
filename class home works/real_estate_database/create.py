import sqlite3

conn = sqlite3.connect("real_estate.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists owners(
    phone_num varchar (11) primary key,
    owner_name text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists buyer(
    phone_num varchar (11) primary key,
    buyer_name text,
    date varchar(20)
)
""")


cursor.execute("""
create table if not exists apartment_buy(
    id int primary key,
    owner_name text,
    owner_phone varchar (11) references owners(phone_num),
    meter varchar (30),
    bar varchar (20),
    location varchar (150),
    price_meter bigint,
    total_price bigint,
    document text,
    elevator text,
    storage text,
    parking text,
    description text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists apartment_rent(
    id int primary key,
    owner_name text,
    owner_phone varchar (11) references owners(phone_num),
    meter varchar (30),
    bar varchar (20),
    location varchar (150),
    first_price bigint,
    month_price bigint,
    document text,
    elevator text,
    storage text,
    parking text,
    description text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists villa_buy(
    id int primary key,
    owner_name text,
    owner_phone varchar (11) references owners(phone_num),
    meter varchar (30),
    bar varchar (20),
    location varchar (150),
    price_meter bigint,
    total_price bigint,
    document text,
    elevator text,
    storage text,
    parking text,
    description text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists villa_rent(
    id int primary key,
    owner_name text,
    owner_phone varchar (11) references owners(phone_num),
    meter varchar (30),
    bar varchar (20),
    location varchar (150),
    first_price bigint,
    month_price bigint,
    document text,
    elevator text,
    storage text,
    parking text,
    description text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists land(
    id int primary key,
    owner_name text,
    owner_phone varchar (11) references owners(phone_num),
    meter varchar (30),
    bar varchar (20),
    location varchar (150),
    price_meter bigint,
    total_price bigint,
    document text,
    elevator text,
    storage text,
    parking text,
    description text,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists apartmentbuy_price_list(
    owner_phone varchar (11) references owners(phone_num),
    id int references apartment_buy(id),
    buyer_phone varchar (11) references buyer(phone_num),
    total bigint,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists apartmentrent_price_list(
    owner_phone varchar (11) references owners(phone_num),
    id int references apartment_rent(id),
    buyer_phone varchar (11) references buyer(phone_num),
    total bigint,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists villabuy_price_list(
    owner_phone varchar (11) references owners(phone_num),
    id int references villa_buy(id),
    buyer_phone varchar (11) references buyer(phone_num),
    total bigint,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists villarent_price_list(
    owner_phone varchar (11) references owners(phone_num),
    id int references villa_rent(id),
    buyer_phone varchar (11) references buyer(phone_num),
    total bigint,
    date varchar(20)
)
""")

cursor.execute("""
create table if not exists land_price_list(
    owner_phone varchar (11) references owners(phone_num),
    id int references land(id),
    buyer_phone varchar (11) references buyer(phone_num),
    total bigint,
    date varchar(20)
)
""")

conn.commit()
conn.close()