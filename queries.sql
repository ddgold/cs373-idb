-- 1980's video games developed by studios with more then 1000 enployees --
select * 
    from Games inner join Developers
        where Games.developer = Developers.id
            and Developers.num_employees > 1000
            and Games.


-- Video games with multiple platforms --
select *, count(distinct name)
    from Games inner join 


select name
	from Developer
	where count(platforms) = 1;