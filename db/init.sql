-- Enable required extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--------------------------------------------------
-- USERS
--------------------------------------------------

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR,
    email VARCHAR UNIQUE,
    password VARCHAR,
    is_expert BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

--------------------------------------------------
-- ARTICLES
--------------------------------------------------

CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR,
    source_url TEXT,
    source_name VARCHAR,
    author_name VARCHAR,
    content_html TEXT,
    short_summary TEXT,
    first_image_url TEXT,
    difficulty VARCHAR,
    type VARCHAR,
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

--------------------------------------------------
-- TAGS
--------------------------------------------------

CREATE TABLE tags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR,
    slug VARCHAR UNIQUE
);

--------------------------------------------------
-- TOPICS
--------------------------------------------------

CREATE TABLE topics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR,
    slug VARCHAR UNIQUE
);

--------------------------------------------------
-- ARTICLE <-> TAG  (N:N)
--------------------------------------------------

CREATE TABLE article_tags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(id) ON DELETE CASCADE
);

--------------------------------------------------
-- ARTICLE <-> TOPIC (N:N)
--------------------------------------------------

CREATE TABLE article_topics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE
);

--------------------------------------------------
-- USER EXPERTISE (TAGS)
--------------------------------------------------

CREATE TABLE user_tag_expertise (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(id) ON DELETE CASCADE
);

--------------------------------------------------
-- USER EXPERTISE (TOPICS)
--------------------------------------------------

CREATE TABLE user_topic_expertise (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE
);

--------------------------------------------------
-- USER FOLLOWS (TAGS)
--------------------------------------------------

CREATE TABLE user_tag_follows (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(id) ON DELETE CASCADE,
    followed_at TIMESTAMP
);

--------------------------------------------------
-- USER FOLLOWS (TOPICS)
--------------------------------------------------

CREATE TABLE user_topic_follows (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE,
    followed_at TIMESTAMP
);

--------------------------------------------------
-- LIBRARIES
--------------------------------------------------

CREATE TABLE libraries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR,
    visibility VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

--------------------------------------------------
-- LIBRARY <-> ARTICLES (N:N)
--------------------------------------------------

CREATE TABLE library_articles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    library_id UUID REFERENCES libraries(id) ON DELETE CASCADE,
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    added_at TIMESTAMP
);
