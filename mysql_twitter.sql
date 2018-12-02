-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: root_mysql_twitter_db
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `photoblggr`
--

DROP TABLE IF EXISTS `photoblggr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `photoblggr` (
  `pic_filenames` varchar(255) NOT NULL,
  `pic_caption` varchar(255) DEFAULT NULL,
  `pic_caption_weight` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pic_filenames`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photoblggr`
--

LOCK TABLES `photoblggr` WRITE;
/*!40000 ALTER TABLE `photoblggr` DISABLE KEYS */;
INSERT INTO `photoblggr` VALUES ('C7zfYdQVAAArBFZ.jpg','whipped cream','0.895162701607'),('C8CroclU8AA7zRU.jpg','photograph','0.949197232723'),('C8deMXdUQAALLyg.jpg','helicopter rotor','0.930097818375'),('Cp4O6UHUIAAn3Il.jpg','face','0.962036788464'),('CpmbWo2VYAEwl6O.jpg','metropolitan area','0.967827677727'),('CqffqPRVIAI3ttT.jpg','beach','0.950926542282'),('CqVrHiUVYAESV0m.jpg','bag','0.967598795891'),('Cr4eWh1UkAQesA5.jpg','blue','0.968104541302'),('CrI4sB1UEAAhWD3.jpg','photograph','0.947940886021'),('CriTZrjVYAAEbrt.jpg','cameras & optics','0.876186907291'),('Cro7GnpUsAAeU_F.jpg','cat','0.994409501553'),('CrUaZmPUIAIkt0C.jpg','hair','0.97356659174'),('CruBwytVMAA_prk.jpg','surfing equipment and supplies','0.95991897583'),('CrzRRp6VMAAc3zM.jpg','clothing','0.964919626713'),('Cs7sF6AUMAAsaJ0.jpg','box','0.79189068079'),('CsDRswmVUAAhkNB.jpg','hearth','0.906330943108'),('CsnXwlCVMAAwVbP.jpg','yellow','0.933184146881'),('Csr_lplVMAAzYEe.jpg','water','0.968450367451'),('CsSm42-VUAE5g5O.jpg','communication','0.705421864986'),('Ct0gKFQUEAEBqdx.jpg','city','0.898766577244'),('CtfvaQOUAAAa5T0.jpg','black and white','0.949887871742'),('CtLD-roVYAIJaVh.jpg','black','0.956022322178'),('CuJFTnVUsAQ6AzB.jpg','bag','0.972238600254'),('CvB3zb6UEAAVfMW.jpg','shoulder','0.849931299686'),('CvZ4JaXUEAAUo_h.jpg','nature','0.944273650646'),('CwJEhtmUIAArAnx.jpg','landmark','0.957584440708'),('Cxcagi8UcAAjCTp.jpg','nature','0.959448754787'),('CxxHYA-VIAEFeUg.jpg','aurora','0.96795809269'),('Cy-n9TPUAAElamV.jpg','font','0.717556774616'),('DC9eQ-UV0AAlWBW.jpg','bird','0.973007678986'),('DDNmVefVwAAQDSa.jpg','sky','0.950167000294'),('DDxltQ1U0AA5KuS.jpg','fireworks','0.990422070026'),('DEveQr4VoAAGK7-.jpg','mountainous landforms','0.951367914677'),('DEWAiBCUAAAT7-A.jpg','dog breed','0.930243194103'),('DFb0e5YXcAI7cVh.jpg','coastal and oceanic landforms','0.920283794403'),('DGa9nWkVwAEVGzf.jpg','nature','0.950026571751'),('DGFPU9yVwAA9UB6.jpg','sky','0.892280578613'),('DGP5hFBUQAA9gsC.jpg','nature','0.94228386879'),('DGvgh63UMAAF5F5.jpg','cat','0.993183672428'),('DHPcTVoV0AAn3Ht.jpg','flower','0.987662792206'),('DI1o22_VAAE7hU4.jpg','wildlife','0.978628993034'),('DIDM1enUwAAfuEe.jpg','metropolitan area','0.990007460117'),('DJkZ6T-VAAE4CMk.jpg','landmark','0.921016812325'),('DKSbHBLUEAEkgol.jpg','water','0.953530967236'),('DLQLwX8VYAEkCRp.jpg','nature','0.950032770634'),('DMR3gEJUEAApNgH.jpg','yellow','0.920907199383'),('DNVsUa6VAAAGu6s.jpg','pumpkin','0.81947517395'),('DPCqUElV4AAtOD4.jpg','sky','0.970032334328');
/*!40000 ALTER TABLE `photoblggr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ripcurl_usa`
--

DROP TABLE IF EXISTS `ripcurl_usa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ripcurl_usa` (
  `pic_filenames` varchar(255) NOT NULL,
  `pic_caption` varchar(255) DEFAULT NULL,
  `pic_caption_weight` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pic_filenames`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ripcurl_usa`
--

LOCK TABLES `ripcurl_usa` WRITE;
/*!40000 ALTER TABLE `ripcurl_usa` DISABLE KEYS */;
INSERT INTO `ripcurl_usa` VALUES ('Dq35__xVsAA2RF_.jpg','sea','0.978053212166'),('Dqy4IbfU4AAmin9.jpg','road','0.874176025391'),('Dr7NaIiU8AEQGTF.jpg','car','0.810341238976'),('DrccHgDU4AID0f1.jpg','coast','0.961272716522'),('DrCD_ODUUAATDVT.jpg','sea','0.97477710247'),('DrHkDyLU4AAC8r9.jpg','surfing equipment and supplies','0.967471778393'),('DrlWVj2UUAApIZY.jpg','water','0.966907739639'),('DrSGPbzVYAEre84.jpg','surfing','0.96780449152'),('Drwo_MRUcAMk2pG.jpg','photograph','0.95036393404'),('Ds8b3a3UwAAIfps.jpg','text','0.954160392284'),('DsFe8iFVYAAX75R.jpg','surfing','0.961269438267'),('DsVblgmVYAA1qx6.jpg','clothing','0.948858261108'),('DszJA-SUwAE-Ema.jpg','sea','0.970032989979'),('DtDIAgfVAAAmhpF.jpg','wave','0.978753387928');
/*!40000 ALTER TABLE `ripcurl_usa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wsl`
--

DROP TABLE IF EXISTS `wsl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `wsl` (
  `pic_filenames` varchar(255) NOT NULL,
  `pic_caption` varchar(255) DEFAULT NULL,
  `pic_caption_weight` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pic_filenames`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wsl`
--

LOCK TABLES `wsl` WRITE;
/*!40000 ALTER TABLE `wsl` DISABLE KEYS */;
INSERT INTO `wsl` VALUES ('-zudl7Rla2oikb9X.jpg','mammal','0.926056206226'),('3unAmCjcNJEI7DVx.jpg','surfing equipment and supplies','0.967297792435'),('Ds_FFg5UUAAgkss.jpg','wave','0.972122430801'),('DtB6txHVAAA49DA.jpg','land vehicle','0.974024832249'),('DtCjAm9VsAEciO-.jpg','text','0.954510629177'),('DtCnnEcVAAEfrzh.jpg','wave','0.972680151463'),('DtGxUvKVAAAxtUP.jpg','wave','0.981603384018'),('Hzq2FZC8PvCM-wJm.jpg','shoulder','0.824126720428'),('ipqyKuRRktNYwBxJ.jpg','body of water','0.934936583042'),('K9mRnGFhOS2GulBo.jpg','headgear','0.685015380383'),('NjdyYU9aOvgIpvrR.jpg','surfing','0.95878714323'),('NSY1OeRENr25xQt5.jpg','wave','0.976438224316'),('P7HwLKE5aSm1ywoZ.jpg','wind wave','0.968801915646'),('QUpfnLIaBsHLUPQo.jpg','water','0.863978803158'),('RGcA7WQQRz8A7RqC.jpg','purple','0.879866778851'),('ue-JvC72Y4LX0t6j.jpg','blue','0.968305468559'),('wOqMWG2laEjqBx5h.jpg','wind wave','0.971081674099');
/*!40000 ALTER TABLE `wsl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-30 18:20:23
