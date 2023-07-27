import pyautogui
import time

# Aguarde alguns segundos antes de começar para dar tempo de preparar a máquina
time.sleep(5)

# Supondo que você precise abrir o "Painel de Controle" para realizar a ação
pyautogui.press('win')
pyautogui.typewrite('sistema')
pyautogui.press('enter')

# Aguarde alguns segundos para o Painel de Controle abrir
time.sleep(2)

# Encontre e clique na opção "Sistema"
system_option = pyautogui.locateOnScreen('config.png')  # Substitua 'system_option.png' pelo caminho da imagem correspondente
if system_option is not None:
    x, y = pyautogui.center(system_option)
    pyautogui.click(x, y)

# Aguarde alguns segundos para a janela "Propriedades do Sistema" abrir
time.sleep(2)

change_option = pyautogui.locateOnScreen('nome.png')  # Substitua 'change_option.png' pelo caminho da imagem correspondente
if change_option is not None:
    x, y = pyautogui.center(change_option)
    pyautogui.click(x, y)

# Aguarde alguns segundos para a janela "Membro do Domínio" abrir
time.sleep(2)fieb.org.br    Geuw82200535@12
# Encontre e clique na opção "Alterar"
change_option = pyautogui.locateOnScreen('alterar.png')  # Substitua 'change_option.png' pelo caminho da imagem correspondente
if change_option is not None:
    x, y = pyautogui.center(change_option)
    pyautogui.click(x, y)

# Aguarde alguns segundos para a janela "Membro do Domínio" abrir
time.sleep(2)

# Insira o nome do domínio na caixa de texto apropriada
pyautogui.typewrite('fieb.org.br')
pyautogui.press('tab')

# Insira as credenciais de administrador do domínio
pyautogui.typewrite('adm_jefferson.souza')
pyautogui.press('tab')
pyautogui.typewrite('Geuw82200535@12')

# Clique no botão "OK" para ingressar no domínio
join_button = pyautogui.locateOnScreen('join_button.png')  # Substitua 'join_button.png' pelo caminho da imagem correspondente
if join_button is not None:
    x, y = pyautogui.center(join_button)
    pyautogui.click(x, y)

# Aguarde alguns segundos para o processo ser concluído
time.sleep(5)

# Feche a janela do Painel de Controle
pyautogui.hotkey('alt', 'f4')
