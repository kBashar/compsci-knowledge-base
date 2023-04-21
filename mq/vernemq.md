### Auth using Database  
1. On the diversity Plugin `plugins.vmq_diversity = on`
2. Off file based Authentication
   ```yml
    plugins.vmq_passwd = off
    plugins.vmq_acl = off
   ```
3. Add releted config values
   ```yml
    vmq_diversity.auth_postgres.enabled = on
    vmq_diversity.postgres.host = 127.0.0.1
    vmq_diversity.postgres.port = 5432
    vmq_diversity.postgres.user = vernemq
    vmq_diversity.postgres.password = vernemq
    vmq_diversity.postgres.database = vernemq_db
    vmq_diversity.postgres.password_hash_method = crypt
   ```
4. Install crypt extension for password hashing. We can do this in pgadmin using query tool.

   ```sql
   CREATE EXTENSION pgcrypto;
   ```
5. Create a table for ACL
   ```sql
   CREATE TABLE vmq_auth_acl
 (
   mountpoint character varying(10) NOT NULL,
   client_id character varying(128) NOT NULL,
   username character varying(128) NOT NULL,
   password character varying(128),
   publish_acl json,
   subscribe_acl json,
   CONSTRAINT vmq_auth_acl_primary_key PRIMARY KEY (mountpoint, client_id, username)
 );
 ```
 6. 