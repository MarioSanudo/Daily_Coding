-- Creación tablas del esquema de la base de datos

create table users(
id				int				primary key		auto_increment, 	
email 			varchar(255)		unique													not null,
subscription		varchar(32)		check(subscription in ("free", "pro", "enterprise"))		default "free",
created_at		timestamp 		default CURRENT_TIMESTAMP(),
is_active		bool				default true);


create table bike_analyses(
id 					int			primary key		auto_increment,
analysis_type		char(32)		check (analysis_type in ("posture", "aerodynamics", "power"))		not null,
result_score			decimal(5,2)		check (result_score between 0 and 100)	not null,
created_at			timestamp	default Current_Timestamp(),

user_id				int			not null,	#No pongo unique por ser relacion 1:N
foreign key(user_id)				references users(id)
);


create table subscription_history(
id					int			primary key		auto_increment,
old_subscription		char(32)		check(old_subscription in ("free", "pro", "enterprise"))		not null,
new_subscription		char(32)		check(new_subscription in ("free", "pro", "enterprise"))		not null,
changed_at			timestamp 	default CURRENT_TIMESTAMP()		not null,

user_id				int			not null	,
foreign key(user_id)	references users(id)
);

create index idx_user_id on bike_analyses(user_id);


select u.id, ba.analysis_type  from users u
left join bike_analyses ba on u.id=ba.user_id;




-- Insercción Valores
insert into users(email, subscription)
values 
		("kartingcroc@gmail.com","free"),
		("mario@email.com","pro"),
		("msc799@alumnos.unican.es","pro"),
		("marito123@hotmail.es", "pro"),
		("pinochet@email.com", "enterprise"),
		("lococo8@gmail.com2", "free");


insert into bike_analyses(user_id,
						 analysis_type,
						 result_score)
values
    (1, "posture", 54),
    (1, "posture", 75.4),
    (2, "aerodynamics", 32.8),
    (3, "power", 68.5),
    (3, "posture", 82.1),
    (4, "aerodynamics", 91.3),
    (5, "power", 45.7),
    (5, "posture", 59.2),
    (6, "aerodynamics", 77.9),
    (2, "power", 88.4);


INSERT INTO subscription_history(user_id, old_subscription, new_subscription)
VALUES
    (1, 'free', 'pro'),
    (2, 'pro', 'free'),
    (3, 'pro', 'enterprise'),
    (6, 'free', 'enterprise');


insert into users(email, subscription)
values(
"abascal@gmail.com", "PRO");




-- Consultas SQL
-- Consulta general, suele ayudarme a ubicarme
select * from users u;
select * from bike_analyses ba;

-- Query 1

select count(*) as Usuarios_activos from users
where is_active=true;

-- Query 2
select result_score from bike_analyses
inner join users u on u.id = user_id
where u.email="msc799@alumnos.unican.es"
order by bike_analyses.created_at desc;

-- Query 3
select round(avg(result_score),2) as Total_selecto
from bike_analyses ba
inner join users u on ba.user_id = u.id 
where u.subscription = "enterprise" or u.subscription = "pro";


-- Query 4
select u.id, ba.analysis_type
from users u 
left join bike_analyses ba on u.id=ba.user_id
where ba.analysis_type is null;

select u.id, ba.analysis_type
from bike_analyses ba		-- Igualmente válido a la derecha va la tabla que se importa después
right join users u on u.id=ba.user_id
where ba.analysis_type is null;


-- Query 5

select u.email, u.subscription, sh.new_subscription , sh.old_subscription 
from users u
inner join subscription_history sh on sh.user_id = u.id
where u.id=1;
-- Debería estar actualizado pero la cuestión en este ejercicio es sacar la consulta


-- Query 6
select u.email, u.subscription, count(ba.analysis_type) as num_analis from users u
inner join bike_analyses ba on ba.user_id=u.id
group by u.email, u.subscription
order by num_analis desc
limit 3;



