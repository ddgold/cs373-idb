cs373-idb
=========

Developer (*companyName, yearFounded, numEmployees, status)

    ('Platinum Games', 2006, 120, 'Active')
    ('Infinity Ward', 2002, 125, 'Active')
    ('Cing', 1999, 29, 'Defunct')
    ('Rockstar Games', 1998, 900, 'Active')
    ('Dimps', 1990, 181, 'Active')
    ('HAL Laboratories', 1980, 145, 'Active')
    ('Monolith Soft', 1999, 108, 'Active')
    ('Konami', 1969, 5759, 'Active')
    ('Midway Games', 1988, 540, 'Defunct')
    ('Square Enix', 2003, 3242, 'Active')


Platform (*name, manufacturer, dateReleased, mediaFormat, generation)

    ('Wii U', 'Nintendo', 11-18-2012, 'Physical (disks) and digital', 8)
    ('Xbox 360', 'Microsoft', 11-22-2005, 'Physical (disks) and digital', 7)
    ('Nintendo DS', 'Nintendo', 11-21-2004, 'Physical (cartridges) and digital', 7)
    ('Playstation 2', Sony', 03-04-2000, 'Physical (disks)', 6)
    ('Game Boy Advance', 'Nintendo', 06-11-2001, 'Physical (cartridges)', 5)
    ('Nintendo Gamecube', 'Nintendo', 09-18-2001, 'Physical (mini-disks)', 6)
    ('Nintendo Wii', 'Nintendo', 11-19-2006, 'Physical (disks) and digital', 7)
    ('MSX', 'Microsoft', 06-16-1983, 'Physical (cartridges)', 2)
    ('Nintendo 64', 'Nintendo', 09-29-1996, 'Physical (cartridges)', 5)
    ('Playstation 3', 'Sony', 11-17-2006, 'Physical (disks) and digital', 7)


Game (*title, dateReleased, publisher, ESRB_Rating, genre)

    ('The Wonderful 101', 09-15-2013, 'Nintendo', 'T', 'Action')
    ('Call of Duty 4: Modern Warfare', 11-05-2007, 'Activision', 'M', 'First-person shooting')
    ('Hotel Dusk: Room 215', 01-22-2007, 'Nintendo', 'T', 'Point-and-click adventure')
    ('Grand Theft Auto III', 10-22-2001, 'Rockstar Games', 'M', 'Open-world action-adventure')
    ('Sonic Advance', 02-03-2002, 'THQ', 'E', 'Platformer')
    ('Super Smash Bros. Melee', 12-03-2001, 'Nintendo', 'T', 'Fighting')
    ('Xenoblade Chronicles', 04-06-2012, 'Nintendo', 'T', 'Action role-playing')
    ('Metal Gear', 07-07-1987, 'Konami', 'N/A', 'Stealth')
    ('Doom 64', 03-31-1997, 'Midway Games', 'M', 'First-person shooting')
    ('Final Fantasy XIII', 03-09-2010, 'Square Enix', 'T', 'Turn-based role-playing')


                          ~model and REST api reference~
Put: 	
Developer	
	company Name(pk)
	date Established()
	num Employees()
	status(can be default)
	
Platform
	name(pk)
	manufactorer()
	dateReleased()
	media()
	generation()

Game
	title(pk)
	dateReleased(set)
	esrb rating()
	publisher()
	genre()
	
Get:

Post:

Delete:
