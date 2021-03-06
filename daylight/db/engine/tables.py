'''SQL to initialize daylight's relational database tables.
'''

from daylight.db.models import AllowedTags


_QUERIES = {
    'init_user_table': '''
    create table if not exists users(
        id serial primary key,
        email varchar(255) unique not null,
        password_hash varchar(255) not null,
        join_date timestamp not null
    );
    ''',

    'init_registration_request_table': '''
    create table if not exists registration_requests(
        email varchar(255) primary key,
        password_hash varchar(128) not null,
        created timestamp not null,
        token varchar(32) unique not null
    );
    ''',

    'init_match_table': '''
    create table if not exists matches(
        first_user integer not null,
        second_user integer not null,
        match_date timestamp not null,
        
        foreign key (first_user) references users (id),
        foreign key (second_user) references users (id),

        unique (second_user, first_user),

        primary key (first_user, second_user)
    );
    ''',
    
    'init_likes_relation_table': '''
    create table if not exists likes_relation(
        from_user integer not null,
        to_user integer not null,
        send_date timestamp not null,

        foreign key (from_user) references users (id),
        foreign key (to_user) references users (id),

        primary key (from_user, to_user)
    );
    ''',

    'init_profile_table': '''
    create table if not exists profiles(
        owner serial primary key,
        display_name varchar(64) not null,
        pronouns varchar(32) not null,
        profile_photo integer,
        biography text not null,
        account_type smallint not null,

        foreign key (owner) references users (id),
        foreign key (profile_photo) references photos (id),

        check (account_type = 1 or account_type = 2)
    );
    ''',

    'init_tag_table': '''
    create table if not exists tags(
        tag varchar(32) primary key
    );
    ''',

    'init_profile_tag_relation_table': '''
    create table if not exists profile_tag_relation(
        profile integer not null,
        tag varchar(32) not null,

        foreign key (profile) references profiles (owner),
        foreign key (tag) references tags (tag)
    );
    ''',

    'init_photo_table': '''
    create table if not exists photos(
        id serial primary key,
        image_source varchar(255) unique not null,
        owner integer not null,
        upload_date timestamp not null,

        foreign key (owner) references users (id)
    );
    ''',

    'init_man_masc_account_type_table': '''
    create table if not exists man_masc_account_type(
        owner serial primary key,
        num_ratings integer default 0,
        respectfulness_score integer default 0,
        knowledgeable_score integer default 0,
        supportiveness_score integer default 0,

        foreign key (owner) references users (id)
    );
    ''',

    'init_woman_femme_account_type_table': '''
    create table if not exists woman_femme_account_type(
        owner serial primary key,

        foreign key (owner) references users (id)
    );
    '''
}

INIT_TAG_QUERY = '''
    insert into tags (tag)
    values (%s)
    on conflict (tag) do nothing;
'''

def create_tables(db_conn):
    '''Execute each query to initialize all datbase tables.
    '''

    order = [
        'init_user_table',
        'init_registration_request_table',
        'init_match_table',
        'init_likes_relation_table',
        'init_photo_table',
        'init_profile_table',
        'init_tag_table',
        'init_profile_tag_relation_table',
        'init_man_masc_account_type_table',
        'init_woman_femme_account_type_table'
    ]

    for query in order:
        db_conn.execute(_QUERIES[query])

    for tag in AllowedTags:
        db_conn.execute(INIT_TAG_QUERY, (tag.tag,))

    return True
