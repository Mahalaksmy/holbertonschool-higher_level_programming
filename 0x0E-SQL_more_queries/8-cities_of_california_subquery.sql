-- Cities of California
-- This is a script that lists all the cities that can be found in the database
SELECT id, name FROM cities WHERE state_id = 1 ORDER by id ASC;
