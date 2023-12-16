
USE Personal;

create table Empleados(
IdEmpleado int not null auto_increment,
nombre varchar (50) not  null,
apellido varchar(50) not null,
fecha_nacimiento date not null,
Dirección varchar(100) not null,
Primary key (PRIMARYidEmpleado)
)engine=InnoDB;

create table Supervisores(
IdSupervisor int not null auto_increment,
nombre varchar (50) not null,
apellido varchar(50) not null, 
fecha_nacimiento date not null,
Dirección varchar(50) not null,
primary key (IdSupervisor),
constraint IdEmpleado foreign key (idEmpleado)
references Empleados (IdEmpleado)
) engine=InnoDB;