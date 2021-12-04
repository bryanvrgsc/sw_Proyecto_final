BEGIN TRANSACTION;
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (1,'q','q','q','q','q');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (2,'w','w','w','w','w');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (3,'b','b','b','b','b');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (4,'','','','','');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (5,'','','','','');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (6,'x','x','x','x','x');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (7,'x','x','x','x','x');
INSERT INTO "alveografo" ("id_alv","tenacidad","extensibilidad","fuerza_panadera","indice_elasticidad","configuracion_curva") VALUES (8,'jkjk','jkjkj','jkjkj','jkjk','jkjk');
INSERT INTO "certificado" ("ncertificado","cantidad_solicitada","cant_total","factura","fecha_envio","fecha_caducidad","idl","idi","norden") VALUES (1,42342.0,42345.0,234234,'2021-12-02 00:00:00.000000','2021-12-02 00:00:00.000000',1,6,1);
INSERT INTO "certificado" ("ncertificado","cantidad_solicitada","cant_total","factura","fecha_envio","fecha_caducidad","idl","idi","norden") VALUES (2,423423.0,7654.0,435543,'2021-12-02 00:00:00.000000','2021-12-02 00:00:00.000000',3,2,4);
INSERT INTO "certificado" ("ncertificado","cantidad_solicitada","cant_total","factura","fecha_envio","fecha_caducidad","idl","idi","norden") VALUES (3,4235.0,5433.0,45411,'2021-12-02 00:00:00.000000','2021-12-02 00:00:00.000000',4,3,6);
INSERT INTO "certificado" ("ncertificado","cantidad_solicitada","cant_total","factura","fecha_envio","fecha_caducidad","idl","idi","norden") VALUES (4,54231.0,75432.0,75432,'2021-12-02 00:00:00.000000','2021-12-02 00:00:00.000000',2,1,7);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (1,'1','2','1','1','1',1,1,NULL,NULL);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (2,'1','5','1','1','1',1,1,2,3);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (3,'s','s','s','s','s',0,1,NULL,4);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (4,'s','s','s','s','s',0,1,NULL,5);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (5,'lfqoit4kb3oqj4232','John','Doe','f;o324','12632784',0,1,NULL,6);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (6,'lfqoit4kb3oqj4232','John','Doe','f;o324','12632784',0,1,NULL,7);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (7,'y','y','yu','y','yu',0,0,NULL,NULL);
INSERT INTO "cliente" ("idc","rfc","nombre","apellido","domicilio","ncontacto","personalizado_far","personalizado_alv","id_far","id_alv") VALUES (8,'y','y','yu','y','yu',0,0,NULL,NULL);
INSERT INTO "equipo_lab" ("clave","marca","modelo","serie","proveedor","fecha_adquisicion","garantia","ubicacion","mantenimiento","descripcionc","descripcionl","idl","id_far","id_alv") VALUES (1,'hjh','hjhj','hjhjh','hjh','2021-12-01 00:00:00.000000','2021-12-01 00:00:00.000000','hjhjh','2021-12-01 00:00:00.000000','jkjk','jkjkjkjkj',NULL,NULL,8);
INSERT INTO "equipo_lab" ("clave","marca","modelo","serie","proveedor","fecha_adquisicion","garantia","ubicacion","mantenimiento","descripcionc","descripcionl","idl","id_far","id_alv") VALUES (2,'d','d','d','d','2021-12-02 00:00:00.000000','2021-12-02 00:00:00.000000','d','2021-12-02 00:00:00.000000','dd','wefohgrqbgjven',NULL,3,NULL);
INSERT INTO "farinografo" ("id_far","absorcion_agua","tolerancia_ub","elasticidad","viscodidad","act_enzimatica","trigo_germinado","tiempo_amasado","cantidad_gluten","calidad_gluten","indoneidad","dureza","reblandecimiento","estabilidad","tiempo_desarrollo","qnumber") VALUES (1,'h','h','h','h','h','h','h','h','h','h','h','h','h','h','h');
INSERT INTO "farinografo" ("id_far","absorcion_agua","tolerancia_ub","elasticidad","viscodidad","act_enzimatica","trigo_germinado","tiempo_amasado","cantidad_gluten","calidad_gluten","indoneidad","dureza","reblandecimiento","estabilidad","tiempo_desarrollo","qnumber") VALUES (2,'a','a','h','a','a','a','a','a','a','aa','a','a','a','a','a');
INSERT INTO "farinografo" ("id_far","absorcion_agua","tolerancia_ub","elasticidad","viscodidad","act_enzimatica","trigo_germinado","tiempo_amasado","cantidad_gluten","calidad_gluten","indoneidad","dureza","reblandecimiento","estabilidad","tiempo_desarrollo","qnumber") VALUES (3,'f','f','f','f','f','f','f','f','f','f','f','f','f','f','f');
INSERT INTO "laboratorista" ("idl","username","password","role","active") VALUES (1,'admin','$2b$12$aK8xQA8qi5AirybUgRUII.ENJDqztZcS3lJ96zpbYvFwIMYMyp.JG','admin',1);
INSERT INTO "laboratorista" ("idl","username","password","role","active") VALUES (2,'lab1','$2b$12$SLH6IPCHLASbtqn36XIoTeLPn8SuPLxgbqt9d06sOxaAEi75Oh8XK','user',1);
INSERT INTO "laboratorista" ("idl","username","password","role","active") VALUES (3,'lab2','$2b$12$7MQVjzLzG6p15qywLjHuRecqsMaZawM0ep5TJxexy8mum/gbQliXO','user',1);
INSERT INTO "laboratorista" ("idl","username","password","role","active") VALUES (4,'CesarRz','$2b$12$zElye.h3qyZSnYGv2zy/ne15/CUloUEvTOQO1V4nLS6qASion1BRm','admin',1);
INSERT INTO "lote" ("idlote","cantidad") VALUES (1,4554.0);
INSERT INTO "lote" ("idlote","cantidad") VALUES (2,45454.0);
INSERT INTO "lote" ("idlote","cantidad") VALUES (3,5234.0);
INSERT INTO "lote" ("idlote","cantidad") VALUES (4,54321.0);
INSERT INTO "lote" ("idlote","cantidad") VALUES (5,54323.0);
INSERT INTO "lote" ("idlote","cantidad") VALUES (6,5321.0);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (1,5326.0,'2021-12-02 00:00:00.000000',45.0,1);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (2,7434.0,'2021-12-02 00:00:00.000000',35.0,5);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (3,8537.0,'2021-12-02 00:00:00.000000',47.0,3);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (4,751.0,'2021-12-02 00:00:00.000000',39.0,6);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (5,6431.0,'2021-12-02 00:00:00.000000',40.0,2);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (6,5325.0,'2021-12-02 00:00:00.000000',40.0,8);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (7,7557.0,'2021-12-02 00:00:00.000000',41.0,1);
INSERT INTO "orden" ("norden","cantidad_solicitada","fecha_creada","precio","idc") VALUES (8,6754.0,'2021-12-02 00:00:00.000000',40.0,2);
COMMIT;