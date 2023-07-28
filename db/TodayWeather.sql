-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        8.0.22 - MySQL Community Server - GPL
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 테이블 study.w_clouds 구조 내보내기
DROP TABLE IF EXISTS `w_clouds`;
CREATE TABLE IF NOT EXISTS `w_clouds` (
  `seq` bigint NOT NULL COMMENT 'key',
  `w_all` int NOT NULL,
  KEY `FK_w_info_TO_w_cloud` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_cloud` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_coord 구조 내보내기
DROP TABLE IF EXISTS `w_coord`;
CREATE TABLE IF NOT EXISTS `w_coord` (
  `seq` bigint NOT NULL COMMENT 'key',
  `lon` varchar(10) NOT NULL,
  `lat` varchar(10) NOT NULL,
  KEY `FK_w_info_TO_w_coord` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_coord` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_info 구조 내보내기
DROP TABLE IF EXISTS `w_info`;
CREATE TABLE IF NOT EXISTS `w_info` (
  `seq` bigint NOT NULL AUTO_INCREMENT,
  `base` varchar(30) DEFAULT NULL,
  `visibility` int DEFAULT NULL,
  `dt` varchar(12) NOT NULL,
  `timezone` varchar(5) DEFAULT NULL,
  `id` varchar(10) DEFAULT NULL,
  `w_name` varchar(20) NOT NULL,
  `cod` int DEFAULT NULL,
  PRIMARY KEY (`seq`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_main 구조 내보내기
DROP TABLE IF EXISTS `w_main`;
CREATE TABLE IF NOT EXISTS `w_main` (
  `seq` bigint NOT NULL COMMENT 'key',
  `temp` float NOT NULL,
  `feels_like` float NOT NULL,
  `temp_min` float NOT NULL,
  `temp_max` float NOT NULL,
  `pressure` int NOT NULL,
  `humidity` int NOT NULL,
  `sea_level` int DEFAULT NULL,
  `grnd_level` int DEFAULT NULL,
  KEY `FK_w_info_TO_w_main` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_main` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_sys 구조 내보내기
DROP TABLE IF EXISTS `w_sys`;
CREATE TABLE IF NOT EXISTS `w_sys` (
  `seq` bigint NOT NULL COMMENT 'key',
  `w_type` int NOT NULL,
  `id` int NOT NULL,
  `country` varchar(10) NOT NULL,
  `sunrise` varchar(12) NOT NULL,
  `sunset` varchar(12) NOT NULL,
  KEY `FK_w_info_TO_w_sys` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_sys` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_weather 구조 내보내기
DROP TABLE IF EXISTS `w_weather`;
CREATE TABLE IF NOT EXISTS `w_weather` (
  `seq` bigint NOT NULL COMMENT 'key',
  `id` int NOT NULL,
  `main` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  `icon` varchar(20) NOT NULL,
  KEY `FK_w_info_TO_w_weather` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_weather` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 study.w_wind 구조 내보내기
DROP TABLE IF EXISTS `w_wind`;
CREATE TABLE IF NOT EXISTS `w_wind` (
  `seq` bigint NOT NULL COMMENT 'key',
  `speed` float NOT NULL,
  `deg` int NOT NULL,
  `gust` float DEFAULT '0',
  KEY `FK_w_info_TO_w_wind` (`seq`),
  CONSTRAINT `FK_w_info_TO_w_wind` FOREIGN KEY (`seq`) REFERENCES `w_info` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
