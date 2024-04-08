-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bdregisters
DROP DATABASE IF EXISTS `bdregisters`;
CREATE DATABASE IF NOT EXISTS `bdregisters` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bdregisters`;

-- Volcando estructura para tabla bdregisters.cities
DROP TABLE IF EXISTS `cities`;
CREATE TABLE IF NOT EXISTS `cities` (
  `ciudad_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ciudad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bdregisters.cities: ~18 rows (aproximadamente)
DELETE FROM `cities`;
INSERT INTO `cities` (`ciudad_id`, `name`, `status`) VALUES
	(1, 'Managua', 1),
	(2, 'León', 1),
	(3, 'Granada', 1),
	(4, 'Masaya', 1),
	(5, 'Estelí', 1),
	(6, 'Jinotepe', 1),
	(7, 'Managua', 1),
	(8, 'León', 1),
	(9, 'Granada', 1),
	(10, 'Masaya', 1),
	(11, 'Estelí', 1),
	(12, 'Jinotepe', 1),
	(13, 'Managua', 1),
	(14, 'León', 1),
	(15, 'Granada', 1),
	(16, 'Masaya', 1),
	(17, 'Estelí', 1),
	(18, 'Jinotepe', 1),
	(19, 'Managua', 1),
	(20, 'León', 1),
	(21, 'Granada', 1),
	(22, 'Masaya', 1),
	(23, 'Estelí', 1),
	(24, 'Jinotepe', 1),
	(25, 'Managua', 1),
	(26, 'León', 1),
	(27, 'Granada', 1),
	(28, 'Masaya', 1),
	(29, 'Estelí', 1),
	(30, 'Jinotepe', 1),
	(31, 'Managua', 1),
	(32, 'León', 1),
	(33, 'Granada', 1),
	(34, 'Masaya', 1),
	(35, 'Estelí', 1),
	(36, 'Jinotepe', 1);

-- Volcando estructura para tabla bdregisters.employees
DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `employees_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `ciudad_id` int DEFAULT NULL,
  `jobs_id` int DEFAULT NULL,
  `salary` double DEFAULT NULL,
  `STATUS` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`employees_id`),
  KEY `ciudad_id` (`ciudad_id`),
  KEY `jobs_id` (`jobs_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `cities` (`ciudad_id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`jobs_id`) REFERENCES `jobsj` (`jobs_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bdregisters.employees: ~0 rows (aproximadamente)
DELETE FROM `employees`;

-- Volcando estructura para tabla bdregisters.jobsj
DROP TABLE IF EXISTS `jobsj`;
CREATE TABLE IF NOT EXISTS `jobsj` (
  `jobs_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`jobs_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bdregisters.jobsj: ~0 rows (aproximadamente)
DELETE FROM `jobsj`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
