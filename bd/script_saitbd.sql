-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sait_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sait_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sait_db` DEFAULT CHARACTER SET utf8 ;
USE `sait_db` ;

-- -----------------------------------------------------
-- Table `sait_db`.`tipo_sw`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`tipo_sw` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`periodo_pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`periodo_pago` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `f_inicio` DATE NOT NULL,
  `f_termino` DATE NOT NULL,
  `f_corte` DATE NOT NULL,
  `f_pago` DATE NOT NULL,
  `periodo` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`marca` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`proveedor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `rfc` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `marca` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_proveedor_marca_idx` (`marca` ASC)  ,
  CONSTRAINT `fk_proveedor_marca`
    FOREIGN KEY (`marca`)
    REFERENCES `sait_db`.`marca` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`software`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`software` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `version` FLOAT NOT NULL,
  `vigencia` DATE NOT NULL,
  `f_compra` DATE NOT NULL,
  `tipo` INT NOT NULL,
  `pago` INT NOT NULL,
  `proveedor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tiposw_sw_idx` (`tipo` ASC)  ,
  INDEX `fk_sw_periodo_idx` (`pago` ASC)  ,
  INDEX `fk_sw_proveedor_idx` (`proveedor` ASC)  ,
  CONSTRAINT `fk_tiposw_sw`
    FOREIGN KEY (`tipo`)
    REFERENCES `sait_db`.`tipo_sw` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sw_periodo`
    FOREIGN KEY (`pago`)
    REFERENCES `sait_db`.`periodo_pago` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sw_proveedor`
    FOREIGN KEY (`proveedor`)
    REFERENCES `sait_db`.`proveedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`servicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`servicios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `caracteristicas` TEXT NOT NULL,
  `pago` INT NOT NULL,
  `proveedor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_servicio_periodo_idx` (`pago` ASC)  ,
  INDEX `fk_servicios_marca_idx` (`proveedor` ASC)  ,
  CONSTRAINT `fk_servicio_periodo`
    FOREIGN KEY (`pago`)
    REFERENCES `sait_db`.`periodo_pago` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_servicios_marca`
    FOREIGN KEY (`proveedor`)
    REFERENCES `sait_db`.`proveedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`activos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`activos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `caracteristica` TEXT NOT NULL,
  `marca` INT NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `no_serie` VARCHAR(50) NOT NULL,
  `garantia` INT NOT NULL,
  `pago` INT NOT NULL,
  `proveedor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_activo_periodo_idx` (`pago` ASC)  ,
  INDEX `fk_activo_marca_idx` (`proveedor` ASC)  ,
  CONSTRAINT `fk_activo_periodo`
    FOREIGN KEY (`pago`)
    REFERENCES `sait_db`.`periodo_pago` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_activo_marca`
    FOREIGN KEY (`proveedor`)
    REFERENCES `sait_db`.`proveedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`empresa` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `rfc` VARCHAR(45) NOT NULL,
  `razon_social` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`pais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`estado` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `pais` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estado_pais_idx` (`pais` ASC)  ,
  CONSTRAINT `fk_estado_pais`
    FOREIGN KEY (`pais`)
    REFERENCES `sait_db`.`pais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`ciudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`ciudad` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `estado` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ciudad_estado_idx` (`estado` ASC)  ,
  CONSTRAINT `fk_ciudad_estado`
    FOREIGN KEY (`estado`)
    REFERENCES `sait_db`.`estado` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`sucursal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`sucursal` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `ciudad` INT NOT NULL,
  `cp` VARCHAR(15) NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `rfc` VARCHAR(45) NOT NULL,
  `razon_social` VARCHAR(45) NOT NULL,
  `empresa` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sucursal_ciudad_idx` (`ciudad` ASC)  ,
  INDEX `fk_sucursal_empresa_idx` (`empresa` ASC)  ,
  CONSTRAINT `fk_sucursal_ciudad`
    FOREIGN KEY (`ciudad`)
    REFERENCES `sait_db`.`ciudad` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sucursal_empresa`
    FOREIGN KEY (`empresa`)
    REFERENCES `sait_db`.`empresa` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`contacto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`contacto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `tipo` TINYINT NOT NULL,
  `proveedor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_contacto_proveedor_idx` (`proveedor` ASC)  ,
  CONSTRAINT `fk_contacto_proveedor`
    FOREIGN KEY (`proveedor`)
    REFERENCES `sait_db`.`proveedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`facturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`facturas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `archivo` TEXT NOT NULL,
  `proveedor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_factura_proveedor_idx` (`proveedor` ASC)  ,
  CONSTRAINT `fk_factura_proveedor`
    FOREIGN KEY (`proveedor`)
    REFERENCES `sait_db`.`proveedor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sait_db`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sait_db`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(15) NULL,
  `correo` VARCHAR(45) NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  `sucursal` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_usuario_sucursal_idx` (`sucursal` ASC)  ,
  CONSTRAINT `fk_usuario_sucursal`
    FOREIGN KEY (`sucursal`)
    REFERENCES `sait_db`.`sucursal` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
