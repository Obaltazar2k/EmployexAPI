-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: employex
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `aplicacion`
--

DROP TABLE IF EXISTS `aplicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aplicacion` (
  `Aprobado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `AplicacionID` int NOT NULL AUTO_INCREMENT,
  `IndependienteID` int DEFAULT NULL,
  `OfertadetrabajoID` int DEFAULT NULL,
  `Usuariocorreo` varchar(100) NOT NULL,
  PRIMARY KEY (`AplicacionID`),
  KEY `FK_Aplicacion_Independiente` (`IndependienteID`),
  KEY `FK_Aplicacion_OfertaDeTrabajo` (`OfertadetrabajoID`),
  CONSTRAINT `FK_Aplicacion_Independiente` FOREIGN KEY (`IndependienteID`) REFERENCES `independiente` (`IndependienteID`),
  CONSTRAINT `FK_Aplicacion_OfertaDeTrabajo` FOREIGN KEY (`OfertadetrabajoID`) REFERENCES `ofertadetrabajo` (`OfertadetrabajoID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `certificacion`
--

DROP TABLE IF EXISTS `certificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certificacion` (
  `Credencialurl` varchar(512) DEFAULT NULL,
  `Empresaemisora` varchar(50) DEFAULT NULL,
  `Fechacaducidad` date DEFAULT NULL,
  `Fechaexpedicion` date DEFAULT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `CertificacionID` int NOT NULL AUTO_INCREMENT,
  `IndependienteID` int NOT NULL,
  PRIMARY KEY (`CertificacionID`),
  KEY `FK_Certificacion_Independiente` (`IndependienteID`),
  CONSTRAINT `FK_Certificacion_Independiente` FOREIGN KEY (`IndependienteID`) REFERENCES `independiente` (`IndependienteID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `educacion`
--

DROP TABLE IF EXISTS `educacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `educacion` (
  `Descripcion` varchar(512) DEFAULT NULL,
  `Disciplina` varchar(50) DEFAULT NULL,
  `Fechafin` date DEFAULT NULL,
  `Fechainicio` date DEFAULT NULL,
  `Promedio` float DEFAULT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `Universidad` varchar(50) DEFAULT NULL,
  `EducacionID` int NOT NULL AUTO_INCREMENT,
  `IndependienteID` int NOT NULL,
  PRIMARY KEY (`EducacionID`),
  KEY `FK_Educacion_Independiente` (`IndependienteID`),
  CONSTRAINT `FK_Educacion_Independiente` FOREIGN KEY (`IndependienteID`) REFERENCES `independiente` (`IndependienteID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `experiencialaboral`
--

DROP TABLE IF EXISTS `experiencialaboral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencialaboral` (
  `Cargoactual` tinyint(1) DEFAULT NULL,
  `Fechafin` date DEFAULT NULL,
  `Fechainicio` date DEFAULT NULL,
  `Nombreempresa` varchar(50) DEFAULT NULL,
  `Sector` varchar(50) DEFAULT NULL,
  `Tipoempleo` varchar(50) DEFAULT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `Ubicacion` varchar(50) DEFAULT NULL,
  `ExperiencialaboralID` int NOT NULL AUTO_INCREMENT,
  `IndependienteID` int NOT NULL,
  PRIMARY KEY (`ExperiencialaboralID`),
  KEY `FK_Experiencialaboral_Independiente` (`IndependienteID`),
  CONSTRAINT `FK_Experiencialaboral_Independiente` FOREIGN KEY (`IndependienteID`) REFERENCES `independiente` (`IndependienteID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `independiente`
--

DROP TABLE IF EXISTS `independiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `independiente` (
  `Apellidos` varchar(50) DEFAULT NULL,
  `Aptitud` varchar(50) DEFAULT NULL,
  `Descripcionpersonal` varchar(512) DEFAULT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Ocupacion` varchar(50) DEFAULT NULL,
  `IndependienteID` int NOT NULL AUTO_INCREMENT,
  `Usuariocorreo` varchar(100) NOT NULL,
  PRIMARY KEY (`IndependienteID`),
  KEY `FK_Independiente_Usuario` (`Usuariocorreo`),
  CONSTRAINT `FK_Independiente_Usuario` FOREIGN KEY (`Usuariocorreo`) REFERENCES `usuario` (`Usuariocorreo`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `media` (
  `File` mediumblob,
  `MediaID` int NOT NULL AUTO_INCREMENT,
  `SeccionID` int DEFAULT NULL,
  `OfertadetrabajoID` int DEFAULT NULL,
  `Usuariocorreo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`MediaID`),
  KEY `FK_Media_Seccion` (`SeccionID`),
  KEY `FK_Media_Ofertadetrabajo` (`OfertadetrabajoID`),
  KEY `FK_Media_Usuario` (`Usuariocorreo`),
  CONSTRAINT `FK_Media_Ofertadetrabajo` FOREIGN KEY (`OfertadetrabajoID`) REFERENCES `ofertadetrabajo` (`OfertadetrabajoID`),
  CONSTRAINT `FK_Media_Seccion` FOREIGN KEY (`SeccionID`) REFERENCES `seccion` (`SeccionID`),
  CONSTRAINT `FK_Media_Usuario` FOREIGN KEY (`Usuariocorreo`) REFERENCES `usuario` (`Usuariocorreo`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ofertadetrabajo`
--

DROP TABLE IF EXISTS `ofertadetrabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ofertadetrabajo` (
  `Cargo` varchar(50) DEFAULT NULL,
  `Descripcion` varchar(512) DEFAULT NULL,
  `Etiqueta` varchar(50) DEFAULT NULL,
  `Tipoempleo` varchar(50) DEFAULT NULL,
  `Ubicacion` varchar(50) DEFAULT NULL,
  `OfertadetrabajoID` int NOT NULL AUTO_INCREMENT,
  `Usuariocorreo` varchar(100) NOT NULL,
  PRIMARY KEY (`OfertadetrabajoID`),
  KEY `FK_OfertaDeTrabajo_Usuario` (`Usuariocorreo`),
  CONSTRAINT `FK_OfertaDeTrabajo_Usuario` FOREIGN KEY (`Usuariocorreo`) REFERENCES `usuario` (`Usuariocorreo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `organizacion`
--

DROP TABLE IF EXISTS `organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organizacion` (
  `Acercade` varchar(512) DEFAULT NULL,
  `Codigopostal` int DEFAULT NULL,
  `Emailcontacto` varchar(100) DEFAULT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Nombrecontact` varchar(50) DEFAULT NULL,
  `Sector` varchar(50) DEFAULT NULL,
  `Sitioweb` varchar(512) DEFAULT NULL,
  `Telefonocontacto` varchar(50) DEFAULT NULL,
  `OrganizacionID` int NOT NULL AUTO_INCREMENT,
  `Usuariocorreo` varchar(100) NOT NULL,
  PRIMARY KEY (`OrganizacionID`),
  KEY `FK_Organizacion_Usuario` (`Usuariocorreo`),
  CONSTRAINT `FK_Organizacion_Usuario` FOREIGN KEY (`Usuariocorreo`) REFERENCES `usuario` (`Usuariocorreo`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seccion`
--

DROP TABLE IF EXISTS `seccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seccion` (
  `Descripcion` varchar(512) DEFAULT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `SeccionID` int NOT NULL AUTO_INCREMENT,
  `IndependienteID` int DEFAULT NULL,
  PRIMARY KEY (`SeccionID`),
  KEY `FK_Seccion_Independiente` (`IndependienteID`),
  CONSTRAINT `FK_Seccion_Independiente` FOREIGN KEY (`IndependienteID`) REFERENCES `independiente` (`IndependienteID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `Ciudad` varchar(50) DEFAULT NULL,
  `Contrasenia` varchar(512) DEFAULT NULL,
  `Correo` varchar(50) DEFAULT NULL,
  `Fotoperfil` int DEFAULT NULL,
  `Pais` varchar(50) DEFAULT NULL,
  `Usuariocorreo` varchar(100) NOT NULL,
  `ValidationToken` varchar(50) DEFAULT NULL,
  `Validated` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Usuariocorreo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-17 14:54:41
