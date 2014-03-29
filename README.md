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
	The Wonderful 101
	http://s11.postimg.org/xjy2jtm6b/the_wonderful_101_logo.png
	http://venturebeat.files.wordpress.com/2013/05/the-wonderful-101.jpg
	http://stickskills.com/wp-content/uploads/2013/01/The-Wonderful-101.jpg

	Call of Duty 4
	http://www.maclife.com/files/u220903/call_of_duty_4_modern_warfare_620px.png
	http://cdn.macrumors.com/article-new/2012/06/NewImage32.png
	http://img3.wikia.nocookie.net/__cb20120604062555/callofduty/images/7/7e/Operation_Kingfish_2013_group_crop.png

	Grand Theft Auto III
	http://www.slashgear.com/wp-content/uploads/2011/12/gta_3_android_0.png
	http://cdn.appstorm.net/ipad.appstorm.net/files/2011/12/gtaIII_2.png
	http://www.gouranga.com/images/gta3/gta3_394.jpg
	
	Sonic Advance
	http://img841.imageshack.us/img841/5249/s2built002.png
	http://img.youtube.com/vi/WTwA1O3eumk/0.jpg
	http://www.friendcodes.com/blog/wp-content/uploads/2013/12/Sonic-Advance-2-Review.png

	Super Smash Bros. Melee
	http://img.gamefaqs.net/box/0/8/7/14087_front.jpg
	http://faqsmedia.ign.com/faqs/image/ali1mg_ssbm_010.jpg
	http://www.technologytell.com/gaming/files/2013/07/smash-bros.-melee.jpg


	Xenoblade Chronicles
	http://upload.wikimedia.org/wikipedia/en/d/d9/Xenoblade_box_artwork.png
	http://www.vgchartz.com/games/pics/xenoblade-chronicles-958102.jpg
	http://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Xenoblade-Landscape.jpg/280px-Xenoblade-Landscape.jpg

	Metal Gear
	http://upload.wikimedia.org/wikipedia/en/b/bd/Metal_Gear_cover.jpg
	http://static.giantbomb.com/uploads/original/0/4648/2019227-solid.jpg
	http://einfogames.com/hub/files/2014/02/nes-metal-gear-jeu.jpg


	Doom 64
	http://img1.wikia.nocookie.net/__cb20080510223920/doom/images/b/b7/Doom_64-box-cover.jpg
	http://www.pixlbit.com/media/products/6773/57131.jpg
	http://colinappleby.com/Photos/Doom%2064.jpg


	Final Fantasy XIII
	http://img3.wikia.nocookie.net/__cb20120614005423/finalfantasy/images/9/94/Final_Fantasy_XIII_Logo.jpg
	http://86bb71d19d3bcb79effc-d9e6924a0395cb1b5b9f03b7640d26eb.r91.cf1.rackcdn.com/wp-content/uploads/2010/03/final-fantasy-xiii-ps3-theme-unlockable-artwork.jpg
	http://fc06.deviantart.net/fs51/i/2009/330/1/f/Final_Fantasy_XIII_characters_by_Cloudfan174.png

                          ~model and REST api reference~
	
	
	
	
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
	
this is the link to our google doc that holds the paper:

https://docs.google.com/document/d/1YaXqNVdTBHkTBSDSvb2_0uz8N0mo7ZR1ursiFVS61Dw/edit?usp=sharing
