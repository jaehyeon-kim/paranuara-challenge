CREATE SCHEMA paranuara;
GRANT ALL ON SCHEMA paranuara TO devuser;

-- change search_path on a connection-level
SET search_path TO paranuara;

-- change search_path on a database-level
ALTER database "devdb" SET search_path TO paranuara;