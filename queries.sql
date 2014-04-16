-- Get the video games that do not have an ESRB rating of M, but have an another valid ESRB rating. --
select title, ESRB_Rating
    from idb_game
    where ESRB_Rating != 'M' and ESRB_Rating != 'N/A';

-- Get the video games that appear on more than one platform. --
select title, count(*)
    from idb_game inner join idb_game_platforms
    where idb_game.id = idb_game_platforms.game_id
    group by id
    having count(*) > 1;

-- Get the video games that were created by now defunct developers. --                     
select title, genre, publisher
    from idb_game
    where developer_id in (select idb_developer.id
                               from idb_developer
                               where status = 'Defunct');

-- Get the platforms in which only one developer in the database has worked on. --       
select name, manufacturer
    from idb_platform
    where id in (select platform_id
                     from idb_developer_platforms
                     group by platform_id
                     having count(platform_id) = 1);
                                         
-- Get the developers that created a game during the 6th generation of consoles. --
select name, status
    from idb_developer
    where id in (select developer_id
                     from idb_developer_platforms
                     where platform_id in (select id
                                               from idb_platform
                                               where generation = 6));
