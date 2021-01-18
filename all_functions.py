import numpy as np
import subprocess
from pathlib import Path
from zipfile import ZipFile
import shutil
import pandas
import sys
import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write2file(filename, url):
	with open(filename,"a") as f:
		f.write(url + '\n')
		
def ls_list(path):
	step_one = subprocess.check_output([ "ls", path ])
	step = str(step_one) # change object step_one to string step
	step_two = step.split("'") # split string to list
	step_three = step_two[1].split("\\n") #create list with folders/files names
	step_three.remove('') #remove from list empty elements
	return step_three

def find_list(path, find_string):
	step_one = subprocess.check_output([ "find", path, "-name", find_string + "*"])
	step = str(step_one) # change object step_one to string step
	step_two = step.split("'") # split string to list
	step_three = step_two[1].split("\\n") #create list with files names
	step_three.remove('') #remove from list empty elements
	return step_three
		
def remove_file(file_path):
	try:
		file_path.unlink()
	except OSError as e:
		print("Error: %s : %s" % (file_path, e.strerror))
		
def remove_folder(dir_path):
	try:
		shutil.rmtree(dir_path)
	except OSError as e:
		print("Error: %s : %s" % (dir_path, e.strerror))
		
def extract_zipfiles(range_years,data_group_in,data_type_in):
	unzip_path = Path("dane/unzip/") # path where extract zip files
	if int(range_years) == 2:
		path = "dane/dane.imgw.pl/"
	else:
		if int(data_group_in) == 1:
			path = "dane/dane.imgw.pl/klimat/"
		elif int(data_group_in) == 2:
			path = "dane/dane.imgw.pl/synop/"
		elif int(data_group_in) == 3:
			path = "dane/dane.imgw.pl/opad/"
			
	folders_names = ls_list(Path(path))
	for i in folders_names:
		pwd = path  + str(i) + "/"
		files_names = ls_list(Path(pwd))
		for j in files_names:
			file_path = pwd + str(j)
			with ZipFile(file_path, 'r') as zip:
				zip.printdir()
				zip.extractall(unzip_path)
				
	dir_path = Path('dane/dane.imgw.pl')
	remove_folder(dir_path)

def download_zipfile(range_years,data_group_in,data_type_in,url):
	now = datetime.datetime.now()
	#variables necessary to flags in download
	synop_range_amount = 8
	klimat_range_amount = 10
	opad_range_amount = 10
	#END

	if int(range_years) == 2:
		if int(data_group_in) == 1:
			while True:
				range_from = input(bcolors.BOLD + '\nPodaj zakres "od":' + bcolors.ENDC + bcolors.OKBLUE + '\n(Maksymalnie 1951)\n' + bcolors.ENDC)
				if range_from not in [str(a) for a in list(np.arange(1951,now.year + 1))]:
					print(bcolors.FAIL + '\nPodaj rok między 1951 a obecnym.' + bcolors.ENDC)
				else:
					break
		elif int(data_group_in) == 2:
			while True:
				range_from = input(bcolors.BOLD + '\nPodaj zakres "od":' + bcolors.ENDC + bcolors.OKBLUE + '\n(Maksymalnie 1960)\n' + bcolors.ENDC)
				if range_from not in [str(a) for a in list(np.arange(1960,now.year + 1))]:
					print(bcolors.FAIL + '\nPodaj rok między 1960 a obecnym.' + bcolors.ENDC)
				else:
					break
		elif int(data_group_in) == 3:
			while True:
				range_from = input(bcolors.BOLD + '\nPodaj zakres "od":' + bcolors.ENDC + bcolors.OKBLUE + '\n(Maksymalnie 1950)\n' + bcolors.ENDC)
				if range_from not in [str(a) for a in list(np.arange(1950,now.year + 1))]:
					print(bcolors.FAIL + '\nPodaj rok między 1950 a obecnym.' + bcolors.ENDC)
				else:
					break
		while True:
			range_to = input(bcolors.BOLD + '\nPodaj zakres "do":\n' + bcolors.ENDC)
			if range_to not in [str(a) for a in list(np.arange(int(range_from),now.year + 1))]:
					print(bcolors.FAIL + '\nPodaj rok między 1960 a obecnym.' + bcolors.ENDC)
			else:
				break
		if int(data_type_in) == 1 or int(data_type_in) == 3:
			if int(data_group_in) == 1:
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1951 and i <= 1955:
						url_rok = url + '1951_1955/' + str(i) + '_k.zip'
					elif i >= 1956 and i <= 1960:
						url_rok = url + '1956_1960/' + str(i) + '_k.zip'
					elif i >= 1961 and i <= 1965:
						url_rok = url + '1961_1965/' + str(i) + '_k.zip'
					elif i >= 1966 and i <= 1970:
						url_rok = url + '1966_1970/' + str(i) + '_k.zip'
					elif i >= 1971 and i <= 1975:
						url_rok = url + '1971_1975/' + str(i) + '_k.zip'
					elif i >= 1976 and i <= 1980:
						url_rok = url + '1976_1980/' + str(i) + '_k.zip'
					elif i >= 1981 and i <= 1985:
						url_rok = url + '1981_1985/' + str(i) + '_k.zip'
					elif i >= 1986 and i <= 1990:
						url_rok = url + '1986_1990/' + str(i) + '_k.zip'
					elif i >= 1991 and i <= 1995:
						url_rok = url + '1991_1995/' + str(i) + '_k.zip'
					elif i >= 1996 and i <= 2000:
						url_rok = url + '1996_2000/' + str(i) + '_k.zip'
					elif i > 2000:
						url_rok = url + str(i) + '/'
					write2file("save_url.txt", url_rok)
			elif int(data_group_in) == 3:
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1950 and i <= 1955:
						url_rok = url + '1950_1955/' + str(i) + '_o.zip'
					elif i >= 1956 and i <= 1960:
						url_rok = url + '1956_1960/' + str(i) + '_o.zip'
					elif i >= 1961 and i <= 1965:
						url_rok = url + '1961_1965/' + str(i) + '_o.zip'
					elif i >= 1966 and i <= 1970:
						url_rok = url + '1966_1970/' + str(i) + '_o.zip'
					elif i >= 1971 and i <= 1975:
						url_rok = url + '1971_1975/' + str(i) + '_o.zip'
					elif i >= 1976 and i <= 1980:
						url_rok = url + '1976_1980/' + str(i) + '_o.zip'
					elif i >= 1981 and i <= 1985:
						url_rok = url + '1981_1985/' + str(i) + '_o.zip'
					elif i >= 1986 and i <= 1990:
						url_rok = url + '1986_1990/' + str(i) + '_o.zip'
					elif i >= 1991 and i <= 1995:
						url_rok = url + '1991_1995/' + str(i) + '_o.zip'
					elif i >= 1996 and i <= 2000:
						url_rok = url + '1996_2000/' + str(i) + '_o.zip'
					elif i > 2000:
						url_rok = url + str(i) + '/'
					write2file("save_url.txt", url_rok)
			elif int(data_group_in) == 2: #synop
				tab_used = synop_range_amount * [False]
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1960 and i <= 1965:
						if tab_used[0] == True:
							continue
						url_rok = url + '1960_1965/'
						tab_used[0] = True
					elif i >= 1966 and i <= 1970:
						if tab_used[1] == True:
							continue
						url_rok = url + '1966_1970/'
						tab_used[1] = True
					elif i >= 1971 and i <= 1975:
						if tab_used[2] == True:
							continue
						url_rok = url + '1971_1975/'
						tab_used[2] = True
					elif i >= 1976 and i <= 1980:
						if tab_used[3] == True:
							continue
						url_rok = url + '1976_1980/'
						tab_used[3] = True
					elif i >= 1981 and i <= 1985:
						if tab_used[4] == True:
							continue
						url_rok = url + '1981_1985/'
						tab_used[4] = True
					elif i >= 1986 and i <= 1990:
						if tab_used[5] == True:
							continue
						url_rok = url + '1986_1990/'
						tab_used[5] = True
					elif i >= 1991 and i <= 1995:
						if tab_used[6] == True:
							continue
						url_rok = url + '1991_1995/'
						tab_used[6] = True
					elif i >= 1996 and i <= 2000:
						if tab_used[7] == True:
							continue
						url_rok = url + '1996_2000/'
						tab_used[7] = True
					elif i > 2000:
						url_rok = url + str(i) + '/'
					write2file("save_url.txt", url_rok)
		elif int(data_type_in) == 2:
			if int(data_group_in) == 1:
				tab_used = klimat_range_amount * [False]
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1951 and i <= 1955:
						if tab_used[0] == True:
							continue
						url_rok = url + '1951_1955/1951_1955_m_k.zip'
						tab_used[0] = True
					elif i >= 1956 and i <= 1960:
						if tab_used[1] == True:
							continue
						url_rok = url + '1956_1960/1956_1960_m_k.zip'
						tab_used[1] = True
					elif i >= 1961 and i <= 1965:
						if tab_used[2] == True:
							continue
						url_rok = url + '1961_1965/1961_1965_m_k.zip'
						tab_used[2] = True
					elif i >= 1966 and i <= 1970:
						if tab_used[3] == True:
							continue
						url_rok = url + '1966_1970/1966_1970_m_k.zip'
						tab_used[3] = True
					elif i >= 1971 and i <= 1975:
						if tab_used[4] == True:
							continue
						url_rok = url + '1971_1975/1971_1975_m_k.zip'
						tab_used[4] = True
					elif i >= 1976 and i <= 1980:
						if tab_used[5] == True:
							continue
						url_rok = url + '1976_1980/1976_1980_m_k.zip'
						tab_used[5] = True
					elif i >= 1981 and i <= 1985:
						if tab_used[6] == True:
							continue
						url_rok = url + '1981_1985/1981_1985_m_k.zip'
						tab_used[6] = True
					elif i >= 1986 and i <= 1990:
						if tab_used[7] == True:
							continue
						url_rok = url + '1986_1990/1986_1990_m_k.zip'
						tab_used[7] = True
					elif i >= 1991 and i <= 1995:
						if tab_used[8] == True:
							continue
						url_rok = url + '1991_1995/1991_1995_m_k.zip'
						tab_used[8] = True
					elif i >= 1996 and i <= 2000:
						if tab_used[9] == True:
							continue
						url_rok = url + '1996_2000/1996_2000_m_k.zip'
						tab_used[9] = True
					elif i > 2000:
						url_rok = url + str(i) + '/' + str(i) + '_m_k.zip'
					write2file("save_url.txt", url_rok)
			elif int(data_group_in) == 3:
				tab_used = opad_range_amount * [False]
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1950 and i <= 1955:
						if tab_used[0] == True:
							continue
						url_rok = url + '1951_1955/1951_1955_m_o.zip'
						tab_used[0] = True
					elif i >= 1956 and i <= 1960:
						if tab_used[1] == True:
							continue
						url_rok = url + '1956_1960/1956_1960_m_o.zip'
						tab_used[1] = True
					elif i >= 1961 and i <= 1965:
						if tab_used[2] == True:
							continue
						url_rok = url + '1961_1965/1961_1965_m_o.zip'
						tab_used[2] = True
					elif i >= 1966 and i <= 1970:
						if tab_used[3] == True:
							continue
						url_rok = url + '1966_1970/1966_1970_m_o.zip'
						tab_used[3] = True
					elif i >= 1971 and i <= 1975:
						if tab_used[4] == True:
							continue
						url_rok = url + '1971_1975/1971_1975_m_o.zip'
						tab_used[4] = True
					elif i >= 1976 and i <= 1980:
						if tab_used[5] == True:
							continue
						url_rok = url + '1976_1980/1976_1980_m_o.zip'
						tab_used[5] = True
					elif i >= 1981 and i <= 1985:
						if tab_used[6] == True:
							continue
						url_rok = url + '1981_1985/1981_1985_m_o.zip'
						tab_used[6] = True
					elif i >= 1986 and i <= 1990:
						if tab_used[7] == True:
							continue
						url_rok = url + '1986_1990/1986_1990_m_o.zip'
						tab_used[7] = True
					elif i >= 1991 and i <= 1995:
						if tab_used[8] == True:
							continue
						url_rok = url + '1991_1995/1991_1995_m_o.zip'
						tab_used[8] = True
					elif i >= 1996 and i <= 2000:
						if tab_used[9] == True:
							continue
						url_rok = url + '1996_2000/1996_2000_m_o.zip'
						tab_used[9] = True
					elif i > 2000:
						url_rok = url + str(i) + '/' + str(i) + '_m_o.zip'
					write2file("save_url.txt", url_rok)
			elif int(data_group_in) == 2:
				tab_used = synop_range_amount * [False]
				for i in range(int(range_from),int(range_to)+1):
					if i >= 1960 and i <= 1965:
						if tab_used[0] == True:
							continue
						url_rok = url + '1960_1965/1960_1965_m_s.zip'
						tab_used[0] = True
					elif i >= 1966 and i <= 1970:
						if tab_used[1] == True:
							continue
						url_rok = url + '1966_1970/1966_1970_m_s.zip'
						tab_used[1] = True
					elif i >= 1971 and i <= 1975:
						if tab_used[2] == True:
							continue
						url_rok = url + '1971_1975/1971_1975_m_s.zip'
						tab_used[2] = True
					elif i >= 1976 and i <= 1980:
						if tab_used[3] == True:
							continue
						url_rok = url + '1976_1980/1976_1980_m_s.zip'
						tab_used[3] = True
					elif i >= 1981 and i <= 1985:
						if tab_used[4] == True:
							continue
						url_rok = url + '1981_1985/1981_1985_m_s.zip'
						tab_used[4] = True
					elif i >= 1986 and i <= 1990:
						if tab_used[5] == True:
							continue
						url_rok = url + '1986_1990/1986_1990_m_s.zip'
						tab_used[5] = True
					elif i >= 1991 and i <= 1995:
						if tab_used[6] == True:
							continue
						url_rok = url + '1991_1995/1991_1995_m_s.zip'
						tab_used[6] = True
					elif i >= 1996 and i <= 2000:
						if tab_used[7] == True:
							continue
						url_rok = url + '1996_2000/1996_2000_m_s.zip'
						tab_used[7] = True
					elif i > 2000:
						url_rok = url + str(i) + '/' + str(i) + '_m_s.zip'
					write2file("save_url.txt", url_rok)
		
		subprocess.run(["wget", "-r", "-np", "--cut-dirs=5", "--reject", "index.html*", "-P", Path("dane"), "-i", "save_url.txt" ])
		remove_file(Path('save_url.txt'))

	else:
		subprocess.run(["wget", "-r", "-np", "--cut-dirs=4", "--reject", "index.html*,*.txt", "-P", Path("dane"), url ])
		
def download_txt_file(data_group_in,data_type_in,url): #txt file contains csv description
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			url_klimat_txt_1 = url + "k_d_format.txt"
			url_klimat_txt_2 = url + "k_d_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_klimat_txt_1 ])
			subprocess.run([ "wget", "-P", "dane/txt_files", url_klimat_txt_2 ])
		elif int(data_group_in) == 2:
			url_synop_txt_1 = url + "s_d_format.txt"
			url_synop_txt_2 = url + "s_d_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_synop_txt_1 ])
			subprocess.run([ "wget", "-P", "dane/txt_files", url_synop_txt_2 ])
		elif int(data_group_in) == 3:
			url_opad_txt = url + "o_d_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_opad_txt ])
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			url_klimat_txt_1 = url + "k_m_d_format.txt"
			url_klimat_txt_2 = url + "k_m_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_klimat_txt_1 ])
			subprocess.run([ "wget", "-P", "dane/txt_files", url_klimat_txt_2 ])
		elif int(data_group_in) == 2:
			url_synop_txt_1 = url + "s_m_d_format.txt"
			url_synop_txt_2 = url + "s_m_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_synop_txt_1 ])
			subprocess.run([ "wget", "-P", "dane/txt_files", url_synop_txt_2 ])
		elif int(data_group_in) == 3:
			url_opad_txt = url + "o_m_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_opad_txt ])
	elif int(data_type_in) == 3:
		if int(data_group_in) == 1:
			url_klimat_txt_1 = url + "k_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_klimat_txt_1 ])
		elif int(data_group_in) == 2:
			url_synop_txt_1 = url + "s_t_format.txt"
			subprocess.run([ "wget", "-P", "dane/txt_files", url_synop_txt_1 ])

def move_csv_file2folder(data_group_in,data_type_in):
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			find_string = ["k_d_t", "k_d"]
		elif int(data_group_in) == 2:
			find_string = ["s_d_t", "s_d"]
		elif int(data_group_in) == 3:
			find_string = ["o_d"]
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			find_string = ["k_m_t", "k_m_d"]
		elif int(data_group_in) == 2:
			find_string = ["s_m_t", "s_m_d"]
		elif int(data_group_in) == 3:
			find_string = ["o_m"]
	if int(data_type_in) == 3:
		if int(data_group_in) == 1:
			find_string = ["k_t"]
		elif int(data_group_in) == 2:
			find_string = ["s_t"]
		
	path = "dane/unzip"
	for k in find_string:
		list_with_csv_file = find_list(path, k)
		destination = path + "_" + str(k) + "/"
		subprocess.run(["mkdir", "-p", destination])
		for t in list_with_csv_file:
			subprocess.run([ "mv", str(t), destination])
	remove_folder(path)
	
def name_of_stations():
	subprocess.run([ "wget", "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv" ])
	df = pandas.read_csv('wykaz_stacji.csv',
						header = None,
						encoding = 'Windows-1250',
						index_col = 0,
						low_memory=False)
	df = df.sort_values(1)
	df.to_csv('wykaz_stacji.csv', header=False)
	print(bcolors.OKGREEN + 'Plik csv z listą wszystkich stacji został pobrany.' + bcolors.ENDC)

def sort_all(path_file):
	df = pandas.read_csv(path_file,
						header = None,
						encoding = 'UTF-8',
						index_col = 0,
						low_memory=False)
	df = df.sort_values([2,3,4])
	df.to_csv(path_file, header=False)
	
def read_and_save(data_group_in,data_type_in,list_stations,list_of_path_csv):
	print(bcolors.HEADER + "\nProszę czekać - szukanie i zapisywanie danych..." + bcolors.ENDC)
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			find_string = ["k_d_t", "k_d"]
			print_string_1 = ["klimatologiczne średnie dobowe","klimatologiczne dobowe"]
			print_string_2 = ["klimatologicznych średnich dobowych","klimatologicznych dobowych"]
		elif int(data_group_in) == 2:
			find_string = ["s_d_t", "s_d"]
			print_string_1 = ["synoptyczne średnie dobowe", "synoptyczne dobowe"]
			print_string_2 = ["synoptycznych średnich dobowych","synoptycznych dobowych"]
		elif int(data_group_in) == 3:
			find_string = ["o_d"]
			print_string_1 = ["opadowe dobowe"]
			print_string_2 = ["opadowych dobowych"]
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			find_string = ["k_m_t", "k_m_d"]
			print_string_1 = ["klimatologiczne średnie miesięczne","klimatologiczne miesięczne"]
			print_string_2 = ["klimatologicznych średnich miesięcznych","klimatologicznych miesięcznych"]
		elif int(data_group_in) == 2:
			find_string = ["s_m_t", "s_m_d"]
			print_string_1 = ["synoptyczne średnie miesięczne","synoptyczne miesięczne"]
			print_string_2 = ["synoptycznych średnich miesięcznych","synoptycznych miesięcznych"]
		elif int(data_group_in) == 3:
			find_string = ["o_m"]
			print_string_1 = ["opadowe miesięczne"]
			print_string_2 = ["opadowych miesięcznych"]
	elif int(data_type_in) == 3:
		if int(data_group_in) == 1:
			find_string = ["k_t"]
			print_string_1 = ["klimatologiczne terminowe"]
			print_string_2= ["klimatologicznych terminowych"]
		elif int(data_group_in) == 2:
			find_string = ["s_t"]
			print_string_1 = ["synoptyczne terminowe"]
			print_string_2= ["synoptycznych terminowych"]
	count = 0
	for string_to_name_file_csv in find_string:
		path2folder = 'dane/unzip_' + str(string_to_name_file_csv) + '/'
		list_csv = ls_list(Path(path2folder))
		for j in list_stations: 
			flag = 0
			for i in list_csv:
				file_path = Path(path2folder + '/' + str(i))
				data_frame = pandas.read_csv(file_path,
										header = None,
										encoding = "Windows-1250",
										index_col = 0,
										low_memory=False)
				data_frame = data_frame.loc[data_frame[1] == str(j)]
				if not data_frame.empty:
					csv_name = str(j) +'_'+ string_to_name_file_csv + '_file.csv'
					csv_path = 'dane/' + csv_name
					data_frame.to_csv(Path(csv_path), mode='a', header=False)
					if flag == 0:
						list_of_path_csv.append(Path(csv_path)) # list with paths to csv plik with data
						print(bcolors.OKGREEN + '\nŚcieżka do pliku csv zawierającego dane ' + str(print_string_1[count]) + ' ze stacji ' + str(j) + ':\n' + bcolors.ENDC + str(Path(csv_path)))
						flag = 1
			if flag == 0:
				print(bcolors.FAIL + '\nNie znaleziono danych ' + str(print_string_2[count]) + ' ze stacji ' + str(j) + bcolors.ENDC)
			else:
				sort_all(Path(csv_path))
		count += 1

def check_folder(data_type_in,data_group_in):
	name_path = 'dane/unzip_'
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			find_string = ["k_d_t", "k_d"]
		elif int(data_group_in) == 2:
			find_string = ["s_d_t", "s_d"]
		elif int(data_group_in) == 3:
			find_string = ["o_d"]
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			find_string = ["k_m_t", "k_m_d"]
		elif int(data_group_in) == 2:
			find_string = ["s_m_t", "s_m_d"]
		elif int(data_group_in) == 3:
			find_string = ["o_m"]
	elif int(data_type_in) == 3:
		if int(data_group_in) == 1:
			find_string = ["k_t"]
		elif int(data_group_in) == 2:
			find_string = ["s_t"]
	full_name_path = [ name_path + str(k) for k in find_string]
	folder_path = [Path(k) for k in full_name_path] 
	check_exist = [x.exists() for x in folder_path]
	return check_exist[0]

def check_file_exist(path):
	check_file_path = Path(path)
	return check_file_path.exists()

def name_of_download_stations(data_group_in,data_type_in):
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			find_string = ["k_d_t", "k_d"]
			path_with_name = 'stacje_k_d.csv'
			print_string_1 = "klimatologicznych dobowych"
		elif int(data_group_in) == 2:
			find_string = ["s_d_t", "s_d"]
			path_with_name = 'stacje_s_d.csv'
			print_string_1 = "synoptycznych dobowych"
		elif int(data_group_in) == 3:
			find_string = ["o_d"]
			path_with_name = 'stacje_o_d.csv'
			print_string_1 = "opadowych dobowych"
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			find_string = ["k_m_t", "k_m_d"]
			path_with_name = 'stacje_k_m.csv'
			print_string_1 = "klimatologicznych miesięcznych"
		elif int(data_group_in) == 2:
			find_string = ["s_m_t", "s_m_d"]
			path_with_name = 'stacje_s_m.csv'
			print_string_1 = "synoptycznych miesięcznych"
		elif int(data_group_in) == 3:
			find_string = ["o_m"]
			path_with_name = 'stacje_o_m.csv'
			print_string_1 = "opadowych miesięcznych"
	if int(data_type_in) == 3:
		if int(data_group_in) == 1:
			find_string = ["k_t"]
			path_with_name = 'stacje_k_t.csv'
			print_string_1 = "klimatologicznych terminowych"
		elif int(data_group_in) == 2:
			find_string = ["s_t"]
			path_with_name = 'stacje_s_t.csv'
			print_string_1 = "synoptycznych terminowych"
			
	if not check_file_exist(path_with_name):	
		path_list = ["dane/unzip_" + str(x) for x in find_string]
		list_path_file = []
		for i in path_list:
			for x in ls_list(Path(i)):
				list_path_file = str(i) + '/' + str(x)
				df = pandas.read_csv(Path(list_path_file),
									header = None,
									encoding = "Windows-1250",
									index_col = 0,
									low_memory = False)
				df = df.drop_duplicates(subset=1)
				df.to_csv(Path(path_with_name), mode = 'a', header=False)

		df = pandas.read_csv(Path(path_with_name),
							header = None,
							encoding = "UTF-8",
							usecols = [0,1],
							index_col = 0,
							low_memory = False)
		df = df.drop_duplicates(subset=1)
		df = df.sort_values(1)
		df.to_csv(Path(path_with_name), header=False)
	return path_with_name
	
def check_file_csv(data_type_in,data_group_in,list_stations):
	new_list_stations = []
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			find_string = ["k_d_t", "k_d"]
			print_string_1 = ["klimatologiczne średnie dobowe","klimatologiczne dobowe"]
		elif int(data_group_in) == 2:
			find_string = ["s_d_t", "s_d"]
			print_string_1 = ["synoptyczne średnie dobowe", "synoptyczne dobowe"]
		elif int(data_group_in) == 3:
			find_string = ["o_d"]
			print_string_1 = ["opadowe dobowe"]
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			find_string = ["k_m_t", "k_m_d"]
			print_string_1 = ["klimatologiczne średnie miesięczne","klimatologiczne miesięczne"]
		elif int(data_group_in) == 2:
			find_string = ["s_m_t", "s_m_d"]
			print_string_1 = ["synoptyczne średnie miesięczne","synoptyczne miesięczne"]
		elif int(data_group_in) == 3:
			find_string = ["o_m"]
			print_string_1 = ["opadowe miesięczne"]
	elif int(data_type_in) == 3:
		if int(data_group_in) == 1:
			find_string = ["k_t"]
			print_string_1 = ["klimatologiczne terminowe"]
		elif int(data_group_in) == 2:
			find_string = ["s_t"]
			print_string_1 = ["synoptyczne terminowe"]
	for x in list_stations:
		count = 0
		flag = 0
		for k in find_string:
			path = 'dane/' + str(x) + '_' + str(k) + '_file.csv'
			option = check_file_exist(path)
			if option == True:
				print(bcolors.FAIL + '\nIstnieje już plik zawierający dane ' + str(print_string_1[count]) + ' ze stacji ' + str(x) + bcolors.ENDC)
			else:
				if flag == 0:
					new_list_stations.append(x)
					flag = 1
			count += 1
	return new_list_stations
	
def check_after_download(data_group_in,data_type_in):
	if int(data_type_in) == 1:
		if int(data_group_in) == 1:
			path_with_name = 'stacje_k_d.csv'
		elif int(data_group_in) == 2:
			path_with_name = 'stacje_s_d.csv'
		elif int(data_group_in) == 3:
			path_with_name = 'stacje_o_d.csv'
	elif int(data_type_in) == 2:
		if int(data_group_in) == 1:
			path_with_name = 'stacje_k_m.csv'
		elif int(data_group_in) == 2:
			path_with_name = 'stacje_s_m.csv'
		elif int(data_group_in) == 3:
			path_with_name = 'stacje_o_m.csv'
	if int(data_type_in) == 3:
		if int(data_group_in) == 1:
			path_with_name = 'stacje_k_t.csv'
		elif int(data_group_in) == 2:
			path_with_name = 'stacje_s_t.csv'
	yes_or_not = check_file_exist(path_with_name)
	if yes_or_not:
		remove_file(Path(path_with_name))
