# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:24:18 2018

@author: marcos.souto
"""

import pandas as pd
import os
import glob
import shutil
from log import logger
import Gera_Senhas_Consolidadas


# --- Seta o diretorio Energisa --- #
my_dir = str(r'\\GcRJ01T-SRV03\Privado\Gestão de Risco e Saúde\VALIDAÇÕES\CNU\Energisa_Senhas\Relatorio')

os.chdir(my_dir)
#-- Verifica se o diretorio esta vazio
tx = os.path.exists("*.xls")
if tx == False:
    logger.info("Não existe arquivos da Energisa para serem gravado")

for files in glob.glob('*.xls'):
    try:
        # -- le o arquivo .htm e carrega para um DataFrame
        tabela = pd.read_html(files)  
        frm = pd.DataFrame(tabela[0]) 
        frm.to_csv("./Corrigido/" + files + ".csv", sep=',', index=False)
        shutil.move(files, './Original')
        logger.info("Arquivo " + files + " gravado com sucesso")
    except:
        logger.error("Erro ao gravar o arquivo "+ files)
    
 
    
# --- Seta o diretorio Valid --- #
my_dir = str(r'\\GcRJ01T-SRV03\Privado\Gestão de Risco e Saúde\VALIDAÇÕES\CNU\Valid senhas\Relatorios')

os.chdir(my_dir)

os.chdir(my_dir)
#-- Verifica se o diretorio esta vazio
tx = os.path.exists("*.xls")
if tx == False:
    logger.info("Não existe arquivos da Valid para serem gravados")

for files in glob.glob('*.xls'):
    try:
        # -- le o arquivo .htm e carrega para um DataFrame
        tabela = pd.read_html(files)  
        frm = pd.DataFrame(tabela[0]) 
        frm.to_csv("./Corrigido/" + files + ".csv", sep=',', index=False)
        shutil.move(files, './Original')
        logger.info("Arquivo " + files + " gravado com sucesso")
        
        # verifica se existe senha para os beneficiarios flegados como alerta
        Gera_Senhas_Consolidadas() 
    except:
        logger.error("Erro ao gravar o arquivo "+ files)
        

