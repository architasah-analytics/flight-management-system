CREATE TABLE `passenger` (
  `passenger_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `contact` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`passenger_id`));

INSERT INTO `passenger` VALUES (1,'Mr. Jai Agarwal',26,'Male','8659863694'),(2,'Ms. Rita Sinha',25,'Female','7698596835'),(3,'Mr. Rahul Awasthi',30,'Male','8569357469'),(5,'Mr. Avinash Gupta',32,'Male','7589335865'),(6,'Mr. Harsh Singh',32,'Male','7854968859'),(7,'Ms. Nandini Shukla',29,'Female','7589886494'),(8,'Ms. Nyra Kapoor',28,'Female','8569974586'),(9,'Mr. Ravi Sahai',39,'Male','8596574882');




CREATE TABLE `flights` (
  `flight_id` int NOT NULL AUTO_INCREMENT,
  `source` varchar(50) DEFAULT NULL,
  `destination` varchar(50) DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`flight_id`)
);

INSERT INTO `flights` VALUES (18,'Delhi','Goa','2024-10-30','12:00:00',4700.00,'Cancelled'),(19,'Delhi','Mumbai','2024-10-29','11:40:00',5900.00,'Available'),(20,'Delhi','Amritsar','2024-10-30','13:10:00',4900.00,'Available'),(21,'Delhi','Bhopal','2024-10-28','13:40:00',5500.00,'Available'),(22,'Delhi','Kolkata','2024-10-30','10:50:00',6200.00,'Available'),(23,'Delhi','Jammu','2024-10-29','14:30:00',5700.00,'Cancelled'),(24,'Delhi','Pune','2024-10-30','09:45:00',3900.00,'Available'),(27,'Delhi','Lucknow','2024-11-21','09:50:00',4900.00,'Available');




CREATE TABLE `bookings` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `passenger_id` int DEFAULT NULL,
  `flight_id` int DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `passenger_id` (`passenger_id`),
  KEY `flight_id` (`flight_id`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`passenger_id`) REFERENCES `passenger` (`passenger_id`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`flight_id`) REFERENCES `flights` (`flight_id`)
); 

INSERT INTO `bookings` VALUES (17,1,18,'2024-10-26'),(18,2,19,'2024-10-26'),(19,3,20,'2024-10-26'),(20,5,21,'2024-10-26'),(21,6,22,'2024-10-26'),(22,7,23,'2024-10-26'),(23,8,24,'2024-10-26'),(25,5,24,'2024-10-26'),(26,9,27,'2024-11-17');

