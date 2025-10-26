-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: login
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `checking`
--

DROP TABLE IF EXISTS `checking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `checking` (
  `userName` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checking`
--

LOCK TABLES `checking` WRITE;
/*!40000 ALTER TABLE `checking` DISABLE KEYS */;
/*!40000 ALTER TABLE `checking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coursedetails`
--

DROP TABLE IF EXISTS `coursedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursedetails` (
  `nICOrPassportNum` varchar(50) DEFAULT NULL,
  `it_level3` tinyint(1) DEFAULT NULL,
  `english_level3` tinyint(1) DEFAULT NULL,
  `softwareEng` tinyint(1) DEFAULT NULL,
  `cyberSecurity` tinyint(1) DEFAULT NULL,
  `networking` tinyint(1) DEFAULT NULL,
  `management` tinyint(1) DEFAULT NULL,
  KEY `nICOrPassportNum` (`nICOrPassportNum`),
  CONSTRAINT `coursedetails_ibfk_1` FOREIGN KEY (`nICOrPassportNum`) REFERENCES `register` (`nICOrPassportNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursedetails`
--

LOCK TABLES `coursedetails` WRITE;
/*!40000 ALTER TABLE `coursedetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `coursedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `userName` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `nICOrPassportNum` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userName`),
  KEY `fk_login_register` (`nICOrPassportNum`),
  CONSTRAINT `fk_login_register` FOREIGN KEY (`nICOrPassportNum`) REFERENCES `register` (`nICOrPassportNum`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('artha','artha2025','200433');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `nICOrPassportNum` varchar(50) NOT NULL,
  `memberShipType` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `bod` date DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `civelStatuse` varchar(50) DEFAULT NULL,
  `ifUnderEighteen` tinyint(1) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `mobileNumber` varchar(50) DEFAULT NULL,
  `homeNumber` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nICOrPassportNum`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('200433','Student','Mr.','Artha','2005-01-01','Male','Single',1,'Colombo','0771234567','0111234567','artha@example.com');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password_hash` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'artha','fdc29c90530930dc49830cfde455bad8$0f4f13c5312440cd5fa770fa1af4bb879f0c95fd89453a7934a8d191e69b6de2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-26  7:35:34
