DROP DATABASE IF EXISTS exampledb;

CREATE DATABASE exampledb
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `exampledb`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `exampledb`.`teacher` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `exampledb`.`course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `teacher_id` INT NOT NULL,
  PRIMARY KEY (`id`, `teacher_id`),
  UNIQUE INDEX `title_UNIQUE` (`title` ASC),
  INDEX `fk_course_teacher1_idx` (`teacher_id` ASC),
  CONSTRAINT `fk_course_teacher1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `exampledb`.`teacher` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `exampledb`.`student_has_course` (
  `student_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`student_id`, `course_id`),
  INDEX `fk_student_has_course_course1_idx` (`course_id` ASC),
  INDEX `fk_student_has_course_student_idx` (`student_id` ASC),
  CONSTRAINT `fk_student_has_course_student`
    FOREIGN KEY (`student_id`)
    REFERENCES `exampledb`.`student` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_has_course_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `exampledb`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `exampledb`.`student` (`name`) VALUES ('Роман Нордштрем');
INSERT INTO `exampledb`.`student` (`name`) VALUES ('Елена Соловьева');
INSERT INTO `exampledb`.`student` (`name`) VALUES ('Яна Петрова');
INSERT INTO `exampledb`.`student` (`name`) VALUES ('Михаил Волынов');
INSERT INTO `exampledb`.`student` (`name`) VALUES ('Дмитрий Комбаров');
INSERT INTO `exampledb`.`student` (`name`) VALUES ('Кирилл Комбаров');

INSERT INTO `exampledb`.`teacher` (`name`) VALUES ('Александр Емелин');
INSERT INTO `exampledb`.`teacher` (`name`) VALUES ('Александр Жебрак');

INSERT INTO `exampledb`.`course` (`title`, `teacher_id`) VALUES ('Python', 1);
INSERT INTO `exampledb`.`course` (`title`, `teacher_id`) VALUES ('Mobile Development', 2);
INSERT INTO `exampledb`.`course` (`title`, `teacher_id`) VALUES ('Machine Learning', 2);

INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (1, 1);
INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (2, 1);
INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (3, 1);
INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (4, 1);
INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (2, 2);
INSERT INTO `exampledb`.`student_has_course` (`student_id`, `course_id`) VALUES (2, 3);

# Показываем SELECT
# Показываем ORDER_BY
# Показываем WHERE
# JOIN student+student_has_course
# LEFT JOIN student+student_has_course
# JOIN course+teacher
# Показываем студентов, не участвующих ни в одном курсе 2мя способами (LEFT JOIN с условием или NOT IN)
# Выбираем преподов и кол-во курсов, которые они преподают (SELECT name, COUNT(teacher_id) FROM teacher LEFT JOIN course on teacher.id=course.teacher_id GROUP BY course.teacher_id;)
