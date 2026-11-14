from avaliador_acuracia import AvalidadorAcuracia
from avaliador_matriz_confusao import AvaliadorMatrizConfusao

class RelatorioModelo(AvaliadorMatrizConfusao, AvalidadorAcuracia):
    def gerar_pdf(self):
        print("Gerando PDF do relatorio completo...")



rm = RelatorioModelo()
rm.avaliar()
print(RelatorioModelo.__mro__)