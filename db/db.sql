SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `test1` DEFAULT CHARACTER SET utf8 ;
USE `test1` ;

-- -----------------------------------------------------
-- Table `test1`.`Nombre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Nombre` (
  `idNombre` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idNombre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Apellido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Apellido` (
  `idApellido` INT NOT NULL AUTO_INCREMENT,
  `Apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idApellido`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Persona` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `Domicilio` VARCHAR(100) NULL,
  `FNacimiento` DATE NULL,
  `Nombre_idNombre` INT NOT NULL,
  `FAlta` DATE NULL,
  `Teléfono` MEDIUMINT NULL,
  PRIMARY KEY (`idPersona`),
  INDEX `fk_Persona_Nombre1_idx` (`Nombre_idNombre` ASC),
  CONSTRAINT `fk_Persona_Nombre1`
    FOREIGN KEY (`Nombre_idNombre`)
    REFERENCES `test1`.`Nombre` (`idNombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Empresa` (
  `idEmpresa` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Teléfono` MEDIUMINT NULL,
  `Persona_Contacto` INT NOT NULL,
  `CIF` VARCHAR(10) NULL,
  `Empresacol` VARCHAR(45) NULL,
  PRIMARY KEY (`idEmpresa`),
  INDEX `fk_Empresa_Persona1_idx` (`Persona_Contacto` ASC),
  CONSTRAINT `fk_Empresa_Persona1`
    FOREIGN KEY (`Persona_Contacto`)
    REFERENCES `test1`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Trabajador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Trabajador` (
  `idTrabajador` INT NOT NULL,
  `Persona` INT NOT NULL,
  `Seguridad Social` BIGINT NULL,
  PRIMARY KEY (`idTrabajador`),
  INDEX `fk_Trabajador_Persona1_idx` (`Persona` ASC),
  CONSTRAINT `fk_Trabajador_Persona1`
    FOREIGN KEY (`Persona`)
    REFERENCES `test1`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Servicio` (
  `idCliente` INT NOT NULL,
  `Persona_Servicio` INT NOT NULL,
  `Persona_Cliente` INT NULL,
  `Empresa_Cliente` INT NULL,
  `Trabajador` INT NOT NULL,
  PRIMARY KEY (`idCliente`),
  INDEX `fk_Cliente_Persona1_idx` (`Persona_Servicio` ASC),
  INDEX `fk_Servicio_Persona1_idx` (`Persona_Cliente` ASC),
  INDEX `fk_Servicio_Empresa1_idx` (`Empresa_Cliente` ASC),
  INDEX `fk_Servicio_Trabajador1_idx` (`Trabajador` ASC),
  CONSTRAINT `fk_Cliente_Persona1`
    FOREIGN KEY (`Persona_Servicio`)
    REFERENCES `test1`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servicio_Persona1`
    FOREIGN KEY (`Persona_Cliente`)
    REFERENCES `test1`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servicio_Empresa1`
    FOREIGN KEY (`Empresa_Cliente`)
    REFERENCES `test1`.`Empresa` (`idEmpresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servicio_Trabajador1`
    FOREIGN KEY (`Trabajador`)
    REFERENCES `test1`.`Trabajador` (`idTrabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Articulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Articulo` (
  `idArticulo` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Caracteristicas` VARCHAR(140) NULL,
  `Cantidad` INT NULL,
  `PrecioProveedor` FLOAT NULL,
  `PrecioCliente` FLOAT NULL,
  `Fecha de Disponibilidad` DATE NULL,
  PRIMARY KEY (`idArticulo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Proveedor` (
  `idProveedor` INT NOT NULL,
  `Empresa` INT NOT NULL,
  `Articulo` INT NOT NULL,
  PRIMARY KEY (`idProveedor`),
  INDEX `fk_Proveedor_Empresa1_idx` (`Empresa` ASC),
  INDEX `fk_Proveedor_Articulo1_idx` (`Articulo` ASC),
  CONSTRAINT `fk_Proveedor_Empresa1`
    FOREIGN KEY (`Empresa`)
    REFERENCES `test1`.`Empresa` (`idEmpresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Proveedor_Articulo1`
    FOREIGN KEY (`Articulo`)
    REFERENCES `test1`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Articulo_has_Servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Articulo_has_Servicio` (
  `Articulo_idArticulo` INT NOT NULL,
  `Servicio_idCliente` INT NOT NULL,
  PRIMARY KEY (`Articulo_idArticulo`, `Servicio_idCliente`),
  INDEX `fk_Articulo_has_Servicio_Servicio1_idx` (`Servicio_idCliente` ASC),
  INDEX `fk_Articulo_has_Servicio_Articulo1_idx` (`Articulo_idArticulo` ASC),
  CONSTRAINT `fk_Articulo_has_Servicio_Articulo1`
    FOREIGN KEY (`Articulo_idArticulo`)
    REFERENCES `test1`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Articulo_has_Servicio_Servicio1`
    FOREIGN KEY (`Servicio_idCliente`)
    REFERENCES `test1`.`Servicio` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Forma_de_Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Forma_de_Pago` (
  `idForma_de_Pago` INT NOT NULL,
  `Forma_de_Pago` VARCHAR(45) NULL,
  PRIMARY KEY (`idForma_de_Pago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Proveedor_has_Forma_de_Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Proveedor_has_Forma_de_Pago` (
  `Proveedor_idProveedor` INT NOT NULL,
  `Forma_de_Pago_idForma_de_Pago` INT NOT NULL,
  PRIMARY KEY (`Proveedor_idProveedor`, `Forma_de_Pago_idForma_de_Pago`),
  INDEX `fk_Proveedor_has_Forma_de_Pago_Forma_de_Pago1_idx` (`Forma_de_Pago_idForma_de_Pago` ASC),
  INDEX `fk_Proveedor_has_Forma_de_Pago_Proveedor1_idx` (`Proveedor_idProveedor` ASC),
  CONSTRAINT `fk_Proveedor_has_Forma_de_Pago_Proveedor1`
    FOREIGN KEY (`Proveedor_idProveedor`)
    REFERENCES `test1`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Proveedor_has_Forma_de_Pago_Forma_de_Pago1`
    FOREIGN KEY (`Forma_de_Pago_idForma_de_Pago`)
    REFERENCES `test1`.`Forma_de_Pago` (`idForma_de_Pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Forma_de_Pago_has_Trabajador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Forma_de_Pago_has_Trabajador` (
  `Forma_de_Pago_idForma_de_Pago` INT NOT NULL,
  `Trabajador_idTrabajador` INT NOT NULL,
  PRIMARY KEY (`Forma_de_Pago_idForma_de_Pago`, `Trabajador_idTrabajador`),
  INDEX `fk_Forma_de_Pago_has_Trabajador_Trabajador1_idx` (`Trabajador_idTrabajador` ASC),
  INDEX `fk_Forma_de_Pago_has_Trabajador_Forma_de_Pago1_idx` (`Forma_de_Pago_idForma_de_Pago` ASC),
  CONSTRAINT `fk_Forma_de_Pago_has_Trabajador_Forma_de_Pago1`
    FOREIGN KEY (`Forma_de_Pago_idForma_de_Pago`)
    REFERENCES `test1`.`Forma_de_Pago` (`idForma_de_Pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Forma_de_Pago_has_Trabajador_Trabajador1`
    FOREIGN KEY (`Trabajador_idTrabajador`)
    REFERENCES `test1`.`Trabajador` (`idTrabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Servicio_has_Forma_de_Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Servicio_has_Forma_de_Pago` (
  `Servicio_idCliente` INT NOT NULL,
  `Forma_de_Pago_idForma_de_Pago` INT NOT NULL,
  PRIMARY KEY (`Servicio_idCliente`, `Forma_de_Pago_idForma_de_Pago`),
  INDEX `fk_Servicio_has_Forma_de_Pago_Forma_de_Pago1_idx` (`Forma_de_Pago_idForma_de_Pago` ASC),
  INDEX `fk_Servicio_has_Forma_de_Pago_Servicio1_idx` (`Servicio_idCliente` ASC),
  CONSTRAINT `fk_Servicio_has_Forma_de_Pago_Servicio1`
    FOREIGN KEY (`Servicio_idCliente`)
    REFERENCES `test1`.`Servicio` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servicio_has_Forma_de_Pago_Forma_de_Pago1`
    FOREIGN KEY (`Forma_de_Pago_idForma_de_Pago`)
    REFERENCES `test1`.`Forma_de_Pago` (`idForma_de_Pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test1`.`Apellido_has_Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test1`.`Apellido_has_Persona` (
  `Apellido_idApellido` INT NOT NULL,
  `Persona_idPersona` INT NOT NULL,
  PRIMARY KEY (`Apellido_idApellido`, `Persona_idPersona`),
  INDEX `fk_Apellido_has_Persona_Persona1_idx` (`Persona_idPersona` ASC),
  INDEX `fk_Apellido_has_Persona_Apellido1_idx` (`Apellido_idApellido` ASC),
  CONSTRAINT `fk_Apellido_has_Persona_Apellido1`
    FOREIGN KEY (`Apellido_idApellido`)
    REFERENCES `test1`.`Apellido` (`idApellido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Apellido_has_Persona_Persona1`
    FOREIGN KEY (`Persona_idPersona`)
    REFERENCES `test1`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
