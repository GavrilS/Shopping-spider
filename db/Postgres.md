# Instructions:
- url: https://hub.docker.com/_/postgres
https://betterprogramming.pub/connect-from-local-machine-to-postgresql-docker-container-f785f00461a7
- start a postgres instance command:
docker run --name postgres-db -p 5432:5432 -v postgres_volume:/postgres-db -e POSTGRES_PASSWORD={secret_password} -e POSTGRES_USER={secret_user} -d postgres

#
docker run --name postgres-db -p 5432:5432 -v postgres_volume:/home/vagrant/docker_images/mounts/postgresql/postgres-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgres
#

- connect to the postgres container to execute commands:
#
docker exec -it <container_id> bash
#
- postgresql commands to create necessary infrastructure:
Example:
#
CREATE DATABASE <db_name>;
#
To exit postgres terminal run '\q'
To exit postgres container run 'exit'

# To interact with postgresql from the server we need a tool: PSQL(CLI), PgAdmin,...
- Install PSQL on Ubuntu:
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
#
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
#

- Connect to postgres with psql:
#
psql -h localhost -p 5432 -U postgres -W
\l -> list dbs
\q -> exit psql
\c <db_name> -> connect to a db
\dt -> list tables
#
CREATE DATABASE <db_name>;
CREATE USER gavril WITH PASSWORD 'gavril';
GRANT ALL PRIVILEGES ON DATABASE e_commerce to gavril;
#
- Create tables:
#
CREATE TABLE IF NOT EXISTS user_searches (
    user_id INT GENERATED ALWAYS AS IDENTITY,
    search_term VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    site VARCHAR(150),
    PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS items(
    item_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    search_term VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_link VARCHAR(255) NOT NULL,
    product_price FLOAT8 NOT NULL,
    date DATE NOT NULL,
    brand VARCHAR(100),
    site VARCHAR(150),
    PRIMARY KEY(item_id),
    CONSTRAINT fk_searches
        FOREIGN KEY(user_id)
            REFERENCES user_searches(user_id)
);
#
