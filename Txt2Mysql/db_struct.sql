CREATE TABLE IF NOT EXISTS `iqilu_keywords` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `catid` int(11) NOT NULL COMMENT '栏目id',
  `keyword` varchar(255) NOT NULL COMMENT '关键词',
  PRIMARY KEY (`id`),
  UNIQUE KEY `keyword` (`keyword`),
  KEY `catid` (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0 ;
