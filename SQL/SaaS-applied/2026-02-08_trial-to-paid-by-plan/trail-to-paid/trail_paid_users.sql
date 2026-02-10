#Creamos la tabla de subscripciones, y la relación 1:1 pués solo puede tener un usuario una subscr.

create table subscriptions(
	id				integer		primary key		auto_increment,
	subscripcion		char(32)		not null			default "basic",
	paid_at			timestamp	null,
	trial_at			timestamp	not null,
	
	user_id			integer		not null 	unique,	#Unique es como use_list=False 1:1
	foreign key(user_id)		references Users(id)
);

#Basic=Gratis,	Pro=Pago

insert into subscriptions(user_id,
						 subscripcion,
						 trial_at,
						 paid_at)
values
(1, 'basic', '2026-01-10', '2026-01-12'), 	#Convertido a pago
(2, 'basic', '2026-01-11', NULL),         	#Gratis
(3, 'pro',   '2026-01-11', '2026-01-20'),  	#Converted
(4, 'pro',   '2026-01-12', NULL),          
(5, 'pro',   '2026-01-15', '2026-01-18');


#Consulta

select count(trial_at) as Usuarios_Prueba,
count(paid_at) as Us
,count(paid_at)/count(trial_at) as Ratio_Conversion 
from subscriptions s;

#Más compleja

select subscripcion, count(trial_at) as Usuario_gratis,
count(paid_at) as Usuario_pago, round(count(paid_at)/count(trial_at),2) as Ratio_Conversion
from subscriptions s group by s.subscripcion
order by ratio_conversion desc;

select * from subscriptions s;


#Este ejercicio no tiene sentido si nos damos cuenta porque se calcula, el ratio de conversión para usuarios
#de pago y solo debería en usuarios gratis que fueron de pago(existe paid_at previo), y hay uno de pago sin que haya pagado, un sin sentido




