import os 

def limpaRecord():
    ## Validação
    if os.path.exists("records.txt"): ## Verifica a existência do arquivo 
        os.remove("records.txt") ## Remove o arquivo 
        mensagem = "O ranque foi excluído"
        #print(mensagem)
    else:
        mensagem = "O ranque está vazio"
        #print(mensagem)
    return mensagem    
   

#print(limpaRecord()) ## Apaga o txt dos ranques 