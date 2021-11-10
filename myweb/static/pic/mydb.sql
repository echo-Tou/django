/*
SQLyog Community v13.1.1 (32 bit)
MySQL - 5.7.26 : Database - mydb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mydb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mydb`;

/*Table structure for table `myapp_users` */

DROP TABLE IF EXISTS `myapp_users`;

CREATE TABLE `myapp_users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint(3) unsigned NOT NULL DEFAULT '20',
  `phone` varchar(16) DEFAULT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `myapp_users` */

insert  into `myapp_users`(`id`,`name`,`age`,`phone`,`addtime`) values 
(1,'张三',20,'123456789','2020-07-10 16:40:59.383102'),
(3,'小李',30,'11111111111','2020-07-10 16:57:50.858488'),
(4,'张无忌',20,'12345678987','2020-07-12 15:08:22.038862'),
(5,'张翠山',42,'65432123456','2020-07-12 15:08:41.801860'),
(6,'张三丰',68,'11111111111','2020-07-12 15:09:05.693055'),
(7,'赵敏',19,'87654321','2020-07-12 15:09:27.583129'),
(8,'金毛狮王',46,'65432345','2020-07-12 15:09:49.597420'),
(9,'周芷若',20,'65432345','2020-07-12 15:10:21.221583'),
(10,'周伯通',66,'123454321','2020-07-12 15:10:47.958007'),
(11,'杨逍',48,'43215678','2020-07-12 15:12:25.804395'),
(12,'灭绝师太',56,'65432345','2020-07-12 15:13:00.431101'),
(13,'殷素素',36,'134321432','2020-07-12 15:13:39.792760'),
(14,'小昭',21,'67895432','2020-07-12 15:14:02.664351'),
(15,'杨不悔',24,'56889454','2020-07-12 15:14:27.265644'),
(16,'成昆',46,'65447678','2020-07-12 15:14:55.367330'),
(17,'张颂',22,'12345678987','2020-07-12 15:15:34.877605'),
(18,'张惠霖',26,'87654321','2020-07-12 15:16:03.106977'),
(19,'赵欣',22,'65432323','2020-07-12 15:16:20.289868'),
(20,'周晓栋',24,'46215678','2020-07-12 15:16:44.804475'),
(21,'周宏伟',25,'95432345','2020-07-12 15:17:01.101785'),
(22,'张璐璐',26,'32123456','2020-07-12 15:17:16.819163'),
(23,'周文涛',22,'65432345','2020-07-12 15:18:14.547387');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;