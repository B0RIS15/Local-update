+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
Программа называется Local_Update.  
Администратор сети хранит у себя все файлы, кроме LU_client 
Админ закачивает к себе обновления, сортирует их по ОС и архивирует и закидывает в папку update 
Если ему необходимо просканировать сеть и узнать какие IP адреса в ней находятся, то он запускает Local_Update  
Для передачи файлов обновления он включает LU_server и ждет подключения клиента 
Когда передача закончится - соедиение автоматически разорвется  
Передача осуществляется по протоколу TCP, порт - 9090 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

!!!!!Для успешной работы в каталоге с программой нужно создать папку update  
!!!!!Сканирование сети использует модуль scapy, требующий Win ncap   
!!!!!Работает только для одного клиента,чтобы передать следующему сервер нужно запустить заново 

