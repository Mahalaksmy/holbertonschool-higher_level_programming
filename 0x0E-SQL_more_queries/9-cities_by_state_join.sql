-- Cities by States
-- This is a script that list all cities contained in the database
SELECT cities.id, cities.name, states.nam FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
