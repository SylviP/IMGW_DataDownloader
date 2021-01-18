from all_functions import *

while True:
	what_to_do = input(bcolors.BOLD + '\nCo chcesz zrobić?\n' + bcolors.ENDC + bcolors.OKBLUE + '\n1.Pobrać dane ze strony IMGW.\n2.Wyszukać dane z konkretnej stacji z pobranych wcześniej plików ze strony IMGW.\n3.Zakończyć program.\nWpisz cyfrę:\n' + bcolors.ENDC)
	if what_to_do not in ('1','2','3'):
		print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
	elif what_to_do == '3':
		sys.exit()
	else:
		break
list_of_path_csv = []
#### variables:
if int(what_to_do) == 1:
	while True:
		data_type_in = input(bcolors.BOLD + '\nDane Meteorologiczne z IMGW\n\nJaki przedział czasowy danych?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.dobowy 2.miesięczny 3.terminowy)\nWpisz cyfrę:\n' + bcolors.ENDC)
		if data_type_in not in ('1','2','3'):
			print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
		else:
			break
	
	if int(data_type_in) == 3:
		while True:
			data_group_in = input(bcolors.BOLD + '\nZ jakiego typu stacji?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.klimatologicznych 2.synoptycznych)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if data_group_in not in ('1','2'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
	else:
		while True:
			data_group_in = input(bcolors.BOLD + '\nZ jakiego typu stacji?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.klimatologicznych 2.synoptycznych 3.opadowych)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if data_group_in not in ('1','2','3'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
	
	if check_folder(data_type_in,data_group_in):
		print(bcolors.FAIL + '\nPobrano już takie dane.\n\nJeśli chcesz pobrać te dane ponownie:\nPrzenieś w inne miejsce wartościowe pliki i usuń folder "dane".\n\nJeśli chcesz zachować wszystkie dane - zmień nazwę folderu "dane"\n' + bcolors.ENDC)
		sys.exit()			
	
	while True:
		range_years = input(bcolors.BOLD + '\nJaki zakres danych?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.wszystkie dostępne lata 2.zakres lat)\nWpisz cyfrę:\n' + bcolors.ENDC)
		if range_years not in ('1','2'):
			print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
		else:
			break
			
	
	data_type = {
			"1" : "dobowe/",
			"2" : "miesieczne/",
			"3" : "terminowe/"
	}

	data_group = {
			"1" : "klimat/",
			"2" : "synop/",
			"3" : "opad/"
	}
		
	url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/" + data_type[data_type_in] + data_group[data_group_in]
	
if int(what_to_do) == 2:
	while True:
		data_type_in = input(bcolors.BOLD + '\nZ jakim przedziałem czasowym pobrano dane?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.dobowym 2.miesięcznym 3.terminowym)\nWpisz cyfrę:\n' + bcolors.ENDC)
		if data_type_in not in ('1','2','3'):
			print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
		else:
			break
	
	if int(data_type_in) == 3:
		while True:
			data_group_in = input(bcolors.BOLD + '\nZ jakiego typu stacji pobrano dane?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.klimatologicznych 2.synoptycznych)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if data_group_in not in ('1','2'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
	else:
		while True:
			data_group_in = input(bcolors.BOLD + '\nZ jakiego typu stacji pobrano dane?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.klimatologicznych 2.synoptycznych 3.opadowych)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if data_group_in not in ('1','2','3'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
	
	yes_or_not = check_file_exist("wykaz_stacji.csv")
	if int(yes_or_not) == False:
		name_of_stations()
		
	option = check_folder(data_type_in,data_group_in)
	if option == True:
		print(bcolors.HEADER + '\nProszę czekać...' + bcolors.ENDC)
		important_file = name_of_download_stations(data_group_in,data_type_in)
		stations_in = input(bcolors.BOLD + '\nPodaj nazwę stacji z polskimi znakami.' + bcolors.ENDC + bcolors.OKBLUE + '\n(Jeśli kilka nazw stacji - oddziel je przecinkiem)\nLista wszystkich stacji znajduje się w pliku "wykaz_stacji.csv".\nLista stacji z pobranych danych znajduje się w pliku ' + str(important_file) + '\nPliki znajdują się w tym samym folderze co program "run.py".\n' + bcolors.ENDC)
		stations_in = stations_in.upper()
		list_stations = [x.strip() for x in stations_in.split(',')]
		list_stations = list(filter(None, list_stations))
		list_stations = check_file_csv(data_type_in,data_group_in,list_stations)
	else:
		print(bcolors.FAIL + '\nNie ma takich pobranych danych.\n' + bcolors.ENDC)
		sys.exit()
		
#### END variables

if int(what_to_do) == 1:
	download_zipfile(range_years,data_group_in,data_type_in,url)
	extract_zipfiles(range_years,data_group_in,data_type_in)
	download_txt_file(data_group_in,data_type_in,url)
	move_csv_file2folder(data_group_in,data_type_in)
	yes_or_not = check_file_exist("wykaz_stacji.csv")
	if int(yes_or_not) == False:
		name_of_stations()
	check_after_download(data_group_in,data_type_in)
	while True:
		do_you_want = input(bcolors.BOLD + '\nCzy chcesz teraz wyszukać dane z konkretnej stacji?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.Tak 2.Nie)\nWpisz cyfrę:\n' + bcolors.ENDC)
		if do_you_want not in ('1','2'):
			print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
		else:
			break
	if int(do_you_want) == 1:
		print(bcolors.HEADER + '\nProszę czekać...' + bcolors.ENDC)
		important_file = name_of_download_stations(data_group_in,data_type_in)
		stations_in = input(bcolors.BOLD + '\nPodaj nazwę stacji z polskimi znakami.' + bcolors.ENDC + bcolors.OKBLUE + '\n(Jeśli kilka nazw stacji - oddziel je przecinkiem)\nLista wszystkich stacji znajduje się w pliku "wykaz_stacji.csv".\nLista stacji z pobranych danych znajduje się w pliku ' + str(important_file) + '\nPliki znajdują się w tym samym folderze co program "run.py".\n' + bcolors.ENDC)
		stations_in = stations_in.upper()
		list_stations = [x.strip() for x in stations_in.split(',')]
		list_stations = list(filter(None, list_stations))
		list_stations = check_file_csv(data_type_in,data_group_in,list_stations)
		if list_stations:
			read_and_save(data_group_in,data_type_in,list_stations,list_of_path_csv)
			
		
		
	elif int(do_you_want) == 2:
		if list_of_path_csv:
			print(bcolors.OKGREEN + '\nŚcieżki do plików:' + bcolors.ENDC)
			for p in list_of_path_csv:
				print(p)
		sys.exit()
	
	flag = True
	while flag:
		while True:
			do_you_want = input(bcolors.BOLD + '\nCzy chcesz wyszukać dane z innej stacji?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.Tak 2.Nie)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if do_you_want not in ('1','2'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
		
		if int(do_you_want) == 1:
			important_file = name_of_download_stations(data_group_in,data_type_in)
			stations_in = input(bcolors.BOLD + '\nPodaj nazwę stacji z polskimi znakami.' + bcolors.ENDC + bcolors.OKBLUE + '\n(Jeśli kilka nazw stacji - oddziel je przecinkiem)\nLista wszystkich stacji znajduje się w pliku "wykaz_stacji.csv".\nLista stacji z pobranych danych znajduje się w pliku ' + str(important_file) + '\nPliki znajdują się w tym samym folderze co program "run.py".\n' + bcolors.ENDC)
			stations_in = stations_in.upper()
			list_stations = [x.strip() for x in stations_in.split(',')]
			list_stations = list(filter(None, list_stations))
			list_stations = check_file_csv(data_type_in,data_group_in,list_stations)
			if list_stations:
				read_and_save(data_group_in,data_type_in,list_stations,list_of_path_csv)
		elif int(do_you_want) == 2:
			if list_of_path_csv:
				print(bcolors.OKGREEN + '\nŚcieżki do plików:' + bcolors.ENDC)
				for p in list_of_path_csv:
					print(p)
			flag = False
elif int(what_to_do) == 2:
	if list_stations:
		read_and_save(data_group_in,data_type_in,list_stations,list_of_path_csv)
	
	flag = True
	while flag:
		while True:
			do_you_want = input(bcolors.BOLD + '\nCzy chcesz wyszukać dane z innej stacji?' + bcolors.ENDC + bcolors.OKBLUE + '\n(1.Tak 2.Nie)\nWpisz cyfrę:\n' + bcolors.ENDC)
			if do_you_want not in ('1','2'):
				print(bcolors.FAIL + '\nNie ma takiej odpowiedzi.' + bcolors.ENDC)
			else:
				break
		if int(do_you_want) == 1:
			important_file = name_of_download_stations(data_group_in,data_type_in)
			stations_in = input(bcolors.BOLD + '\nPodaj nazwę stacji z polskimi znakami.' + bcolors.ENDC + bcolors.OKBLUE + '\n(Jeśli kilka nazw stacji - oddziel je przecinkiem)\nLista wszystkich stacji znajduje się w pliku "wykaz_stacji.csv".\nLista stacji z pobranych danych znajduje się w pliku ' + str(important_file) + '\nPliki znajdują się w tym samym folderze co program "run.py".\n' + bcolors.ENDC)
			stations_in = stations_in.upper()
			list_stations = [x.strip() for x in stations_in.split(',')]
			list_stations = list(filter(None, list_stations))
			list_stations = check_file_csv(data_type_in,data_group_in,list_stations)
			if list_stations:
				read_and_save(data_group_in,data_type_in,list_stations,list_of_path_csv)
		elif int(do_you_want) == 2:
			if list_of_path_csv:
				print(bcolors.OKGREEN + '\nŚcieżki do plików:' + bcolors.ENDC)
				for p in list_of_path_csv:
					print(p)
			flag = False
