-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for absensi
DROP DATABASE IF EXISTS `absensi`;
CREATE DATABASE IF NOT EXISTS `absensi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `absensi`;

-- Dumping structure for table absensi.mahasiswa
DROP TABLE IF EXISTS `mahasiswa`;
CREATE TABLE IF NOT EXISTS `mahasiswa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(150) NOT NULL,
  `kelas` varchar(50) NOT NULL,
  `matkul` varchar(150) NOT NULL,
  `NIM` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table absensi.mahasiswa: ~1 rows (approximately)
REPLACE INTO `mahasiswa` (`id`, `nama`, `kelas`, `matkul`, `NIM`) VALUES
	(2, 'Muhammad Yusuf', '5I', 'Pemrograman Lanjut', 2213010468),
	(3, 'Satria Tabah Raharja', '5I', 'Pemrograman Lanjut', 2213010504),
	(4, 'Arya Saultanaya', '5I', 'Pemrograman Lanjut', 2213010484),
	(5, 'Irhash Zim Zam D.P', '5I', 'Pemrograman Lanjut', 2213010494);

-- Dumping structure for table absensi.pengguna
DROP TABLE IF EXISTS `pengguna`;
CREATE TABLE IF NOT EXISTS `pengguna` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_pengguna` varchar(150) NOT NULL,
  `kata_sandi` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nama_pengguna` (`nama_pengguna`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table absensi.pengguna: ~1 rows (approximately)
REPLACE INTO `pengguna` (`id`, `nama_pengguna`, `kata_sandi`) VALUES
	(1, 'yusuf', '$2b$12$gC6ZtYWPIIG3f68/HTKJEeOL.B4058bRXY7oIl0ZFWe.oXJ4E19XC');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
