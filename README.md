# ZTEnd, Agile Configuration Restoration

[Leia em Português](#-ztend-restauração-ágil-de-configurações)

ZTEnd is a solution for internet providers that pre-configure their routers before installation, increasing productivity and the speed of router installation. It is a simple automation algorithm to quickly access and restore pre-defined configurations for a ZTE H198A router.

![Logo](https://i.ibb.co/gzQ5KmS/ZTEnd.png)

## 🔧 Installation

* Dependencies: Python3, Selenium, psutil

Visit the official Python website to download the latest version of Python: https://www.python.org/

After downloading Python and the project, open the ZTEnd folder and run the file ```install_dependencies.bat```. If the dependencies are installed without errors, you can start using the program.

* ⚠️ Possible errors and solutions:
```'pip' is not recognized as an internal or external command```:
If you have installed Python and this error persists, it is because the path to Python is not in the Windows PATH variable. You can resolve this by adding the Python path to the PATH variable or simply reinstalling Python and selecting the option to add Python to the PATH during installation.

## 🎠 How to Use

* ⚠️ Manually reset the router using the reset button located near the power button. You can use a paper clip or a pin for this. Press the reset button until the power LED turns off.

Run the file ```ZTEnd_start.bat```. A graphical interface will be displayed, requiring the following information:
* Interface Name: This field should be filled with the name of the network interface you are using to connect to the router to be configured. For example, Ethernet, Ethernet 2. Check the name of your network interface in the control panel. Be mindful of uppercase and lowercase letters.

* Path to the configuration file: Fill in or select the ```.bin``` configuration file. This file can be obtained from a router that already has your preferred settings via the router menu: ```> Management & Diagnosis > System Management > User Configuration Management > Backup User Configuration```

* Select the route: Select the route (if there is more than one) where the router (gateway) you want to configure is located.

* Headless mode: This mode runs the program in the background.

## 🔙 Error Output

* A interface não foi encontrada/Interface not found: This means that you have misspelled the network interface name.

* Rede desconectada/Network disconnected: This means that your computer is not connected to the network. Check if your machine is in the same IP range as the gateway and if the cable connection (if any) is properly plugged in.

* integrity check failed: Error in the router configuration file integrity. Verify that you selected the correct file and that the file is not corrupted. If the problem persists, access a configured router and download the configurations again.

* Error related to ```id="Frm_ShowPrivacy```: This likely means the router has not been reset.

* Error related to ```GetHandleVerifier```: This means that the router's access username and/or password is not the default "multipro". Ensure the router has been reset and is not already configured.

* Other errors: Contact the developer.

## 📞 Author/Support
- Github: [kayckemauel1](https://github.com/kayckemanuel1)
- Instagram: [@8kayck](https://www.instagram.com/8kayck)
- Email: [kayck@tutamail.com](mailto:kayck@tutamail.com)

---

# 🚀 ZTEnd, Restauração ágil de configurações

ZTEnd é uma solução para provedores de internet que deixam seus roteadores pré-configurados antes de fazer a instalação, fazendo assim com que aumente a produtividade e a velocidade com que é instalado um roteador. Trata-se de um simples algoritmo de automação para rapidamente acessar e restaurar as configurações pré-definidas de um roteador ZTE H198A.

![Logo](https://i.ibb.co/gzQ5KmS/ZTEnd.png)

## 🔧 Instalação

* Dependencias: Python3, Selenium, psutil

Acesse o site oficial do Python e veja como baixar a versão mais recente do Python: https://www.python.org/

Após o download do Python e do projeto, abra a pasta do ZTEnd e execute o arquivo ```instalar_dependencias.bat```, se a instalação das dependencias acontecer sem erros, você ja pode usar o programa.

* ⚠️ Possiveis erros e problemas e suas correções:
```'pip' is not recognized as an internal or external command```:
Se você já instalou o Python e esse erro permanece, isso é porque o caminho para o Python não está na variavel path do Windows. Você pode resolver isso incluindo o caminho para o Python dentro da variavel path ou simplismente reinstalando o Python e durante a instalação selecionar a opção para incluir o Python dentro da variavel path.

## 🎠 Como usar

* ⚠️ Resete manualmente o roteador através do botão de reset que fica próximo ao botão power, você pode usar um grampo ou um palito para isso, pressione o botão de reset até que o LED de power se apague.

Execute o arquivo ```ZTEnd_start.bat```, após isso será exibido uma interfaxe gráfica que necessita das seguintes informações: 
* Nome da interface: Esse campo deve ser preenchido com o nome da interface de rede que você está usando para se conectar ao roteador que será configurado. Ex: Ethernet, Ethernet 2. Verifique o nome da sua interface de rede no painel de controle. Lembre-se de respeitar as letras maiúsculas e minúsculas.

* Caminho para o arquivo de configuração: Preencha ou selecione o arquivo de configuração ```.bin``` de configuração. Esse arquivo pode ser obtido através de um roteador que já tem as configurações da sua prefêrencia através do roteador em: ```> Management & Diagnosis > System Management > User Configuration Management > Backup User Configuration```

* Selecione a rota: Selecione a rota (caso haja mais de uma) em que está o roteador (gateway) que deseja configurar.

* Modo handless: Modo que faz o programa rodar de forma oculta.

## 🔙 Retorno/saida de erros que podem acontecer

* A interface não foi encontrada: Significa que você escreveu o nome da interface de rede de forma errada.

* Rede desconectada: Significa que seu computador não está conectado a rede, verifique se sua máquina está no mesmo range de ip do gateway e se a conexão via cabo (se for uma) está bem encaixada.

* integrity check failed: Erro na integridade do arquivo de configurações do roteador. Verifique se você selecionou o arquivo correto e se o arquivo não está corrompido. Em caso de persistencia do problema, acesse um roteador já configurado e faça um novo download das configurações.

* Erro relacionado ao ```id="Frm_ShowPrivacy```: Significa que provavelmente o roteador não foi resetado.

* Erro reladionado ao ```GetHandleVerifier```: Significaque o usuário e/ou senha de acesso ao roteador não é a padrão "multipro". Verifique se o roteador foi resetado e se ele não já está configurado.

* Outros erros: entre em contato com o desenvolvedor.

## 📞 Autor/Suporte
- Github: [kayckemauel1](https://github.com/kayckemanuel1)
- Instagram: [@8kayck](https://www.instagram.com/8kayck)
- Email: [kayck@tutamail.com](mailto:kayck@tutamail.com)
