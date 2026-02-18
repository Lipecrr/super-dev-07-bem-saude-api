-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bem_saude_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bem_saude_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bem_saude_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `bem_saude_db` ;

-- -----------------------------------------------------
-- Table `bem_saude_db`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bem_saude_db`.`pacientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(15) NOT NULL,
  `cpf` VARCHAR(14) NOT NULL,
  `data_nascimento` DATE NOT NULL,
  `email` VARCHAR(60) NULL,
  `endereco` VARCHAR(45) NULL,
  `observacoes` TEXT NULL,
  `status` BIT NOT NULL,
  `tipo_sanguineo` ENUM('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-') NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bem_saude_db`.`profissionais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bem_saude_db`.`profissionais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `especialidade` ENUM('Clínico Geral', 'Cardiologia', 'Ortopedia', 'Dermatologia', 'Pediatria') NOT NULL,
  `registro` VARCHAR(9) NOT NULL,
  `duracao` TIME NOT NULL,
  `valor` DOUBLE NOT NULL,
  `atendimento_segunda` BIT NULL,
  `atendimento_terca` BIT NULL,
  `atendimento_quarta` BIT NULL,
  `atendimento_quinta` BIT NULL,
  `atendimento_sexta` BIT NULL,
  `atendimento_sabado` BIT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bem_saude_db`.`recepcionistas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bem_saude_db`.`recepcionistas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bem_saude_db`.`consultas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bem_saude_db`.`consultas` (
  `id` INT NOT NULL,
  `id_paciente` INT NOT NULL,
  `id_profissional` INT NOT NULL,
  `id_recepcionista` INT NOT NULL,
  `status` ENUM('Agendada', 'Atrasada', 'Confirmada', 'Cancelada', 'Em Andamento', 'Finalizada') NOT NULL,
  `data` DATE NOT NULL,
  `horario_previsto` TIME NOT NULL,
  `observacao` TEXT NULL,
  `horario_inicio` TIME NULL,
  `horario_final` TIME NULL,
  `anotacoes_consulta` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_consulta_paciente_idx` (`id_paciente` ASC) VISIBLE,
  INDEX `fk_consulta_recepcionista_idx` (`id_recepcionista` ASC) VISIBLE,
  INDEX `fk_consulta_profissional_idx` (`id_profissional` ASC) VISIBLE,
  CONSTRAINT `fk_consulta_paciente`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `bem_saude_db`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_consulta_recepcionista`
    FOREIGN KEY (`id_recepcionista`)
    REFERENCES `bem_saude_db`.`recepcionistas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_consulta_profissional`
    FOREIGN KEY (`id_profissional`)
    REFERENCES `bem_saude_db`.`profissionais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
