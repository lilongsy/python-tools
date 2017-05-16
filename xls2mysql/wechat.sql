CREATE TABLE IF NOT EXISTS `iqilu_wechat` (
  `wid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `wechat` varchar(255) NOT NULL,
  `wechatname` varchar(255) NOT NULL,
  `catid` int(10) unsigned NOT NULL,
  `status` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`wid`),
  UNIQUE KEY `wechatname` (`wechatname`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
