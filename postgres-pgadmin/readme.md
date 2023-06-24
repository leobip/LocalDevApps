# Install, Config Postgres DB & PgAdmin

ref's:
    - <https://hub.docker.com/_/postgres>
    - <https://hub.docker.com/r/dpage/pgadmin4>

- Add how to use secrets...

- Apply the workloads, either one by one or all in one step. (Inside the posgres folder)
  - All:
    - ```kubectl apply -f .```
  - One by One (Recomended):
    - ```kubectl apply -f postgres-vol.yaml```
    - ```kubectl apply -f postgres-deploy.yaml```

- The yaml allready has the NodePorts especs:
  - Postgres: 30432
  - PgAdmin: 30432

- NOTE: Encode password for Secret
  - ```echo  'postgres' | base64```
  - cG9zdGdyZXMK
  
  - Decode:
  - ```echo  'cG9zdGdyZXMK' | base64 decode```

### Run Queries to Tests

  ```sql
    CREATE TABLE users (
      id SERIAL PRIMARY KEY NOT NULL,
      email          VARCHAR(255)    NOT NULL,
      password       CHAR(32)     NOT NULL
    );

    INSERT INTO 
    users (email, password) 
    VALUES
    ('alfa@example.com', MD5('alfa')),
    ('beta@example.com', MD5('beta'));

    SELECT * FROM users;
  ```
