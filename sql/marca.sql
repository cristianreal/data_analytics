-- Crear la tabla marca
CREATE TABLE marca (
    id INTEGER PRIMARY KEY,
    marca VARCHAR(255) NOT NULL
);

-- Insertar los datos
INSERT INTO marca (id, marca) VALUES
(1, 'Diageo Americas'),
(2, 'Heaven Hill Brands'),
(3, 'Sazerac Co., Inc.'),
(4, 'Sage Beverages'),
(5, 'MHW Ltd'),
(6, 'White Rock Distilleries, Inc.'),
(7, 'Pernod Ricard USA/Austin Nichols'),
(8, 'Edrington Group USA LLC'),
(9, 'Luxco-St Louis'),
(10, 'WILLIAM GRANT AND SONS, INC.'),
(11, 'Kwik Imports'),
(12, 'Constellation Wine Company, Inc.'),
(13, 'Bacardi U.S.A., Inc.'),
(14, 'Moet Hennessy USA, Inc.'),
(15, 'Levecke Corp'),
(16, 'Yahara Bay Distillers, Inc'),
(17, 'The Patron Spirits Company'),
(18, 'E AND J GALLO WINERY'),
(19, 'Sazerac North America'),
(20, 'B. United International'),
(21, 'Proximo'),
(22, 'ALLIED DOMECQ SPIRITS AND WINE USA'),
(23, 'Jim Beam Brands'),
(24, 'Shaw Ross International Importers LL'),
(25, 'Campari(skyy)'),
(26, 'Seagram Americas'),
(27, 'United Distillers USA'),
(28, 'Brown-Forman Corporation'),
(29, 'Dehner Distillery'),
(30, 'Frank-lin Distillers Products Ltd.'),
(31, 'REMY COINTREAU USA         .'),
(32, 'WILDMAN AND SONS, F.'),
(33, 'Sidney Frank Importing Co.'),
(34, 'Better Beverage Importers'),
(35, 'Blavod Extreme Spirits USA, Inc.'),
(36, 'Mccormick Distilling Company'),
(37, 'Prestige Wine and Spirits Group'),
(38, 'Laird And Company'),
(39, 'Phillips Beverage Company'),
(40, 'Castle Brands'),
(41, '3 Badge Mixology'),
(42, 'Disaronno International LLC'),
(43, 'Luxco-Cleveland'),
(44, 'Hood River Distillers, Inc.'),
(45, 'Nolet Spirits USA'),
(46, 'Carillon Importers Ltd.'),
(47, 'Gemini Spirits'),
(48, 'Palm Bay Imports, Inc.'),
(49, 'A Hardy / U.S.A., Ltd.'),
(50, 'Aiko Importers Inc'),
(51, 'The Wine Group'),
(52, 'Wilson Daniels Ltd.'),
(53, 'Cruzan International, Inc.'),
(54, 'Swiss Cellars'),
(55, 'Western Spirits Beverage Co. LLC'),
(56, 'Cedar Ridge Vineyards,LLC'),
(57, 'Prost Beverage Company'),
(58, 'Serralles USA'),
(59, 'Montana Distillers, Inc.'),
(60, 'Park Street Imports-Duke Spirits'),
(61, 'Four Roses Distillery'),
(62, 'High West Distillery'),
(63, 'Anchor Distilling (PREISS IMPORTS)'),
(64, 'Millennium Import Company'),
(65, 'Prairie Creek Beverages LLC'),
(66, 'Aveniu Brands'),
(67, 'Jesse James Distilling Company'),
(68, 'Chatham Imports,inc'),
(69, 'Imperial Brands, Inc.'),
(70, 'Alive Spirits'),
(71, 'A. Smith Bowman Distillery Inc.'),
(72, 'Domecq Importers Inc.'),
(73, 'Charles Jacquin Et. Cie., Inc.'),
(74, 'Kobrand Corporation'),
(75, 'Breckenridge Distillery'),
(76, 'Duggan''s Distillers Products Corp'),
(77, 'Mango Bottling, Inc.'),
(78, 'Anheuser-Busch/Longtail Libations'),
(79, 'Bad Bear Enterprises'),
(80, 'Mississippi River Distilling Co.'),
(81, 'Cooperspiritsinternational'),
(82, 'Three Rangers'),
(83, 'Artisan Grain Distillery'),
(84, 'Iowa Distilling Company'),
(85, 'Broadbent Distillery'),
(86, 'Honey Creek Distillery'),
(87, 'Blaum Bros. Distilling Co.'),
(88, 'Ole Smoky Distillery, LLC'),
(89, 'Windy Hill Spirits'),
(90, 'Dry Fly Distilling'),
(91, 'Homestead American Whiskey'),
(92, 'Rogue Ales and Spirits'),
(93, 'Panther Distillery'),
(94, 'Patriarch Distillers'),
(95, 'High West Distillery, LLC'),
(96, '3-Oaks Distillery, LLC'),
(97, 'Bishop Wines & Spirits'),
(98, 'W. J. Deutsch And Sons, Ltd.'),
(99, 'Shand Import LLC'),
(100, 'Paddington Corporation, The'),
(101, 'Classic Wine Imports'),
(102, 'Paterno Imports, Ltd.'),
(103, 'NWS, Inc DBA Consolidated Dist'),
(104, 'TY KU, LLC'),
(105, '209, Ltd'),
(106, 'Planet 10 Spirits'),
(107, 'Foley Family Wines, Inc.'),
(108, 'Stoli Group'),
(109, 'Quadro Group LLC'),
(110, 'Firestarter Spirits Inc.'),
(111, 'Russian Standard Vodka, USA'),
(112, 'Klin Spirits, LLC'),
(113, 'Piedmont Distillers'),
(114, 'Black Rock Spirits'),
(115, 'Dakota Spirits Distillery'),
(116, 'Blue Angel Spirits LLC'),
(117, 'Distilling Head'),
(118, 'Cooper''s Chase Distillery'),
(119, 'Royal World Spirits'),
(120, 'Koenig Distillery'),
(121, 'Trinchero Family Estates'),
(122, 'High Plains Inc'),
(123, 'Marsalle Company'),
(124, 'Better Brands Bev Co'),
(125, 'Square One Organic Spirits'),
(126, 'Swell Liquor LLC'),
(127, 'World Wide Wine & Spirit Importers'),
(128, 'Sovereign Brands'),
(129, 'Fifth Generation Inc.'),
(130, 'Minhas Micro Distillery'),
(131, 'Koan, Inc.'),
(132, 'Spirits Of The USA'),
(133, 'Stern Beverage'),
(134, 'M.S. Walker, Inc.'),
(135, 'Niche Import Co.'),
(136, 'Carriage House Imports, Ltd.'),
(137, 'Lapham Import Co'),
(138, 'Dana Wine & Spirits Importers'),
(139, '3-D Spirits, Inc.'),
(140, 'Modern Spirits'),
(141, 'Werner Distilling, LLC'),
(142, 'International Beverage Co., Inc.'),
(143, 'Paradise Distilling Company'),
(144, 'Winebow, Inc.'),
(145, 'Nicholas Enterprises'),
(146, 'Austin, Nichols & Co., Inc.'),
(147, 'Anchor Distilling Co'),
(148, 'Grand Prix Beverage LLC'),
(149, 'National Brokers'),
(150, 'Gaetano Specialties, Ltd.'),
(151, 'International Beverage Holdings USA'),
(152, 'Urban Brands And Spirits'),
(153, 'American Vintage Beverage'),
(154, 'Royal Products Int''l, Inc.'),
(155, 'Stellar Importing Company, LLC'),
(156, 'Park Street Imports-Berentzen'),
(157, 'Whyte and Machay(Americas) Limited,L'),
(158, 'Specialty Spirits Imports'),
(159, 'Jinro America, Inc'),
(160, 'McKenzie River Corporation'),
(161, 'Surville Enterprises Corp'),
(162, 'ASDSpirits, LLC'),
(163, 'Harbrew Imports'),
(164, 'Park Street Imports-Voli'),
(165, 'Tyfield Imp. D/B/A Masterpieces'),
(166, 'Capstone International Inc'),
(167, 'Biagio Cru And Estate Wines, LLC'),
(168, 'Bacmar International'),
(169, 'VBJ Beverages LLC'),
(170, 'Paulaner USA'),
(171, 'maDIKwe USA, Inc.'),
(172, 'Speakeasy Spirits, LLC'),
(173, 'Gunsandmore.info'),
(174, 'Banfi Products Corp.'),
(175, 'Drinks Americas'),
(176, 'Santa Fe Tequila Company'),
(177, 'St. George Spirit, Inc'),
(178, 'Wine Intelligence'),
(179, 'Liquor Group Wholesale'),
(180, 'Nestor Imports, Inc.'),
(181, 'Stephen Augustus Imports'),
(182, 'Park Street Imports-House Spirits'),
(183, 'Domaine Select Wine Estates'),
(184, 'Clear Creek Distillery'),
(185, 'CVI Brands'),
(186, 'Koloa Rum Company'),
(187, 'Spirit Imports, Inc.'),
(188, 'Bendistillery'),
(189, 'The Country Vintner'),
(190, 'Park Street Imports-Sweet Revenge'),
(191, 'Domaine Charbay'),
(192, 'Itsko Imports Inc'),
(193, 'North Texas Distillers'),
(194, 'Marsalle Company/Stoller Warehouse'),
(195, 'Willett Distillery'),
(196, 'Kindred Spirits Of North America'),
(197, 'Tequilas Premium Inc.'),
(198, 'Hillrock Estate Distillery LLC'),
(199, 'Win It Too Inc/Global Beer Network'),
(200, 'Dreyfus, Ashby Co.'),
(201, 'Distillerie Stock U.S.A., Ltd.'),
(202, 'Ste. Michelle Wine Estates'),
(203, 'Behn Of North America, LLC'),
(204, 'Sierra Nevada Brewing Company'),
(205, 'D & V International, Inc.'),
(206, 'Vital Beverages'),
(207, 'Pacific Edge Wine & Spirits'),
(208, 'Total Beverage Solutions'),
(209, 'Park Street Imports- Caballeros'),
(210, 'SANS WINE AND SPIRITS CO'),
(211, 'H A P LLC'),
(212, 'Boston Beer Company'),
(213, '888 Imports'),
(214, 'Van Gogh Imports'),
(215, 'Goose Island Beer Co'),
(216, 'Heartland Wine And Spirits Group'),
(217, 'Summit Brewing Company'),
(218, 'PARTIDA TEQUILA'),
(219, 'Admiral Imports'),
(220, 'Diageo Chateau & Estates Wines Co.'),
(221, 'Woody Creek Distillers'),
(222, 'Duvel Moortgat USA'),
(223, 'Artisanal Imports'),
(224, 'Boz Spirits'),
(225, 'Impex Beverages Inc'),
(226, 'North Shore Distillery, LLC.'),
(227, 'Vanberg & Dewulf'),
(228, 'Great Lakes Liquor Company'),
(229, 'Five Star Wine & Spirits'),
(230, 'Belukus Marketing, Inc.'),
(231, 'Frank Pesce Int''l Group LLC, The'),
(232, 'Phoenix Imports Ltd.'),
(233, 'Merchant Du Vin Corporation'),
(234, 'Evaton, Inc.'),
(235, 'Seashore Marketing Group'),
(236, 'Spaten North America, Inc.'),
(237, 'Bmc Imports'),
(238, 'High Energy Holdings, LLC'),
(239, 'Dorado, Pizzorni & Sons, LLC'),
(240, 'Black Diamond Spirits LLC'),
(241, 'AIG Wine & Spirits DBA Mezzaluna Sp'),
(242, 'Dreyfus Ashby, Inc.'),
(243, 'Winery Exchange'),
(244, 'Shelton Brothers'),
(245, 'Adamba Imports Int''l, Inc.'),
(246, 'The Old Mill Brand Wines & Spirits,'),
(247, 'Tanteo Tequila'),
(248, 'Wetten Importers, Inc.'),
(249, 'Flying Dog Brewery'),
(250, 'Bardenheier Wine Cellars'),
(251, 'Post Familie Winery'),
(252, 'North Coast Brewing Co'),
(253, 'Stanley Stawski Distributing Co.'),
(254, 'Unibrew USA, Inc.'),
(255, 'Burrell Beverage'),
(256, 'Bell''s Brewery, Inc.'),
(257, 'Manneken-brussel Imports, Inc.'),
(258, 'Doyna Ltd'),
(259, 'Leatherbee Distillers'),
(260, 'Boulevard Brewing Company'),
(261, 'Ti Beverage Group, Ltd'),
(262, 'Haas Brothers'),
(263, 'Francoliusa'),
(264, 'Fire Tail Brands Llc'),
(265, 'Robert Kacher Selections'),-- Continuación de las inserciones para la tabla marca

(266, 'Belmont Farms Of Va., Inc'),
(267, 'Temperance Distiling Company'),
(268, 'Aha Toro Spirits Inc'),
(269, 'USB Corporation'),
(270, 'Park Street Imports-Veev'),
(271, 'Jalixco Trading Co. LLC'),
(272, 'Devotion Spirits, Inc.'),
(273, 'Intersect Beverage LLC'),
(274, 'Cracovia, Inc'),
(275, 'Majestic Distilling Co'),
(276, 'Barrel House Distilling Co.'),
(277, 'Referent Spirits'),
(278, 'Fsj Imports'),
(279, 'Park Street Imports-Few Spirits'),
(280, 'Berniko, LLC.'),
INSERT INTO marca (id, marca) VALUES
(281, 'Park Street Imports-Philadelphia Dis'),
(282, 'American Spirits Exchange'),
(283, 'Ransom Spirits LLC'),
(284, 'Phenix Brands, LLC'),
(285, 'San Luis Spirits, Inc.'),
(286, 'Park Street Imports-High Stick Vodka'),
(287, 'Iconic Brands, Inc.'),
(288, 'Bom Dia Imports dba Novo Fogo'),
(289, 'Louisiana Spirits LLC'),
(290, 'Caribbean Spirits Inc'),
(291, 'Park Street Imports-Tanteo'),
(292, 'Vodquila LLC'),
(293, 'Philly''s Premium Beverages LLC'),
(294, 'Koval Distillery'),
(295, 'Spirit of Hartford'),
(296, 'Lloyd Caruso LLC'),
(297, 'Alien Tequila Spirits Company'),
(298, 'Broadslab Distillery'),
(299, 'Journeyman Distillery LLC'),
(300, '45th Parallel Spirits'),
(301, 'Rumcoqui and Co'),
(302, 'BuzzBox Beverages'),
(303, 'Breuckelen Distilling'),
(304, 'Iowa ABD'),
(305, 'Park Street-G''Day'),
(306, 'Royal Wine Corporation'),
(307, 'Purple Valley Imports');