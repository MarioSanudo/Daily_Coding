-- Voy a crear tambien la simulación a modo de base de datos


-- Creación tabla
create table Users(
	id		Integer			not null			primary key		auto_increment,
	nombre	Char(64)		not null
);

create table Orders(
	id		Integer			not null		primary key		auto_increment,
	total	Numeric(10,2)	not null		check (total>=0),
	user_id	Integer			not null,	
	foreign key (user_id)	references Users(id)
);


-- Insercción de valores y consulta

insert into Users(nombre)
values("Mario"),
		("Sofía"),
		("Álvaro"),
		("Julian"),
		("Combo")
;


insert into orders(user_id,
				  total)
values(1, 120.50),
  	    (1,  39.99),
  		(2,  10.00),
  		(2, 250.00),
  		(4,  0.00),
  		(4,  75.25);



select nombre, o.id, sum(total) as Total_Pedidos from users u 
left join orders o on o.user_id=u.id
group by nombre, o.id
order by total_pedidos   desc;


-- Sumado
select u.id, sum(total) as total_pedidos from users u 
left join orders o on o.user_id=u.id
group by u.id
order by total_pedidos desc;


-- 2ª Forma
select u.nombre, o.id, sum(o.total) as Total_Pedidos from users u, orders o
where o.user_id=u.id
group by u.nombre, o.id;


-- Lo que se pide

select u.nombre , count(o.user_id) as Num_pedidos, sum(o.total) as gasto_total from users u
left join orders o on u.id=o.user_id
group by u.nombre order by gasto_total desc;
