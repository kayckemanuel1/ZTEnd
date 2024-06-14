import os
import psutil
import platform
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

def descobrir_gateways():
    sistema = platform.system()
    
    if sistema == "Windows":
        comando = "route print 0.0.0.0"
    else:  # Supondo que seja um sistema Unix-like
        comando = "ip route show default"

    gateways = []

    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        if sistema == "Windows":
            for linha in resultado.split('\n'):
                if "0.0.0.0" in linha:
                    partes = linha.split()
                    gateway = partes[2]
                    interface = partes[3]
                    custo = int(partes[-1])
                    gateways.append((gateway, interface, custo))
        else:
            for linha in resultado.split('\n'):
                if "default" in linha:
                    partes = linha.split()
                    gateway = partes[2]
                    interface = partes[4]
                    custo = int(partes[-1])
                    gateways.append((gateway, interface, custo))
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

    return gateways

def verificar_conexao_ethernet(interface_name):
    interfaces = psutil.net_if_stats()
    
    if interface_name in interfaces:
        # Verificar se a interface está operando
        if interfaces[interface_name].isup:
            return True
        else:
            return False
    else:
        raise ValueError(f"A interface {interface_name} não foi encontrada. Por favor verifique se você inseriu corretamente o nome da interface de rede, lembre-se de respeitar as letras maiusculas e minusculas e os espaços.")

def download_chromedriver():
    try:
        chromedriver_path = ChromeDriverManager().install()
        messagebox.showinfo('Informação', f'O Chromedriver foi baixado e salvo em {chromedriver_path}. Você pode desconectar da internet agora.')
        return chromedriver_path
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao baixar o Chromedriver: {e}')
        return None

def algoritimo_upload(interface_rede, file_path, gateway, headless, chromedriver_path):
    try:
        if not verificar_conexao_ethernet(interface_name=interface_rede):
            messagebox.showerror('Erro', 'Rede desconectada, verifique as conexões e o status da rede.')
            return
        
        # Dados
        url = 'http://' + gateway
        user_pass = 'multipro'

        messagebox.showinfo('Informação', f'Rede conectada!\nGateway: {gateway}')
        
        # Configurações navegador
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")

        service = Service(chromedriver_path)
        navegador = webdriver.Chrome(service=service, options=chrome_options)
        
        # Acessa o roteador
        navegador.get(url)

        # Login
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Frm_Username"]'))).send_keys(user_pass)
        navegador.find_element(By.XPATH, '//*[@id="Frm_Password"]').send_keys(user_pass)
        navegador.find_element(By.XPATH, '//*[@id="LoginId"]').click()
        time.sleep(0.5)

        # Chegando à aba de upload
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Btn_Close"]'))).click()
        time.sleep(0.5)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mgrAndDiag"]'))).click()
        time.sleep(0.5)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="devMgr"]'))).click()
        time.sleep(0.5)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="defCfgMgr"]'))).click()
        time.sleep(0.5)

        # Localizar o campo de upload e enviar o arquivo
        upload_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="defConfigUpload"]')))
        upload_element.send_keys(file_path)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DefConfUploadBar"]'))).click()
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Btn_Upload"]'))).click()
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmOK"]'))).click()

        # Verificação resultado do upload
        confirm_msg = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirmMsg"]/p'))).text
        if "processing, please wait" in confirm_msg.lower() or "Are you sure to restore user configuration?" in confirm_msg.lower():
            messagebox.showinfo('Informação', "Fazendo upload do arquivo, por favor aguarde.")
            time.sleep(1.5)
            confirm_msg = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirmMsg"]/p'))).text
            if "integrity check failed" in confirm_msg.lower():
                messagebox.showerror('Erro', 'Erro de integridade, Verifique se você selecionou o arquivo correto e se o arquivo não está corrompido.')
            else:
                messagebox.showinfo('Sucesso no upload!', 'Upload feito com sucesso. Desligue e ligue o roteador manualmente pelo botão power.')
        else:
            messagebox.showerror('Erro', f"Erro ao realizar upload: {confirm_msg}")
                
    except Exception as e:
        messagebox.showerror('Erro', str(e))
    finally:
        navegador.quit()

def selecionar_arquivo():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

# Interface gráfica
root = tk.Tk()
root.title("ZTEnd, Agile Preset ZTE H198")

tk.Label(root, text="Nome da Interface de Rede:").grid(row=0, column=0, padx=10, pady=10)
interface_rede = tk.Entry(root)
interface_rede.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Caminho para o Arquivo de Configuração:").grid(row=1, column=0, padx=10, pady=10)
file_path_entry = tk.Entry(root)
file_path_entry.grid(row=1, column=1, padx=10, pady=10)

btn_selecionar_arquivo = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_selecionar_arquivo.grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Selecione a Rota:").grid(row=2, column=0, padx=10, pady=10)
rota_combobox = ttk.Combobox(root, state="readonly")
rota_combobox.grid(row=2, column=1, padx=10, pady=10)

def atualizar_rotas():
    gateways = descobrir_gateways()
    rotas = [f"{gateway[1]} - {gateway[0]} (Custo: {gateway[2]})" for gateway in gateways]
    rota_combobox['values'] = rotas
    if rotas:
        rota_combobox.current(0)

btn_atualizar_rotas = tk.Button(root, text="Atualizar Rotas", command=atualizar_rotas)
btn_atualizar_rotas.grid(row=2, column=2, padx=10, pady=10)

headless_var = tk.BooleanVar(value=True)  # Faz o script ser executado de forma oculta
check_headless = tk.Checkbutton(root, text="Modo Headless", variable=headless_var)
check_headless.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

chromedriver_path = None

def baixar_chromedriver():
    global chromedriver_path
    chromedriver_path = download_chromedriver()

btn_baixar_chromedriver = tk.Button(root, text="Baixar Chromedriver", command=baixar_chromedriver)
btn_baixar_chromedriver.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

def executar_algoritmo():
    try:
        if not chromedriver_path:
            messagebox.showerror('Erro', 'Por favor, baixe o Chromedriver antes de executar o algoritmo.')
            return

        rota_selecionada = rota_combobox.get()
        if not rota_selecionada:
            messagebox.showerror('Erro', 'Por favor, selecione uma rota.')
            return
        gateway = rota_selecionada.split(' - ')[1].split(' (')[0]
        algoritimo_upload(interface_rede.get(), file_path_entry.get(), gateway, headless_var.get(), chromedriver_path)
    except Exception as e:
        messagebox.showerror('Erro', str(e))

btn_executar = tk.Button(root, text="Executar", command=executar_algoritmo)
btn_executar.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
