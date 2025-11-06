from faker import Faker
import random
import os
import glob
faker = Faker('pt_BR')
LISTA_CURSOS = [
    "Administração", "Direito", "Enfermagem", "Engenharia Civil", "Psicologia",
    "Medicina", "Pedagogia", "Ciências Contábeis", "Educação Física",
    "Arquitetura e Urbanismo", "Fisioterapia", "Nutrição", "Odontologia",
    "Engenharia de Produção", "Medicina Veterinária", "Ciência da Computação",
    "Jornalismo", "Publicidade e Propaganda", "Farmacia", "Letras", "História",
    "Geografia", "Matemática", "Física", "Química", "Biologia", "Economia", "Sistema de Informação"
]
class Estudante:
    def __init__(self, matricula, cpf, curso, nome, filiacao_mae, filiacao_pai, ano, coeficiente):
        self.CPF = cpf
        self.Curso = curso
        self.Nome = nome
        self.Filiacao_mae = filiacao_mae
        self.Filiacao_pai = filiacao_pai
        self.Ano_ingresso = ano
        self.Coeficiente = coeficiente
        self.Matricula = matricula
    @staticmethod
    def gerar_aluno():
        matricula = faker.random_number(digits=9)
        nome = faker.name()[:50]
        cpf = faker.random_number(digits=11)
        curso = random.choice(LISTA_CURSOS)[:30] 
        filiacao_mae = faker.name_female()[:30]
        filiacao_pai = faker.name_male()[:30]
        ano = faker.random_int(min=2015, max=2025)
        coeficiente = round(random.uniform(0, 10), 2)
        return Estudante(matricula, cpf, curso, nome, filiacao_mae, filiacao_pai, ano, coeficiente)
    
    def transformar_em_bytes_variavel(self) -> bytes:
        linha = f"{self.Matricula};{self.CPF};{self.Curso};{self.Nome};{self.Filiacao_mae};{self.Filiacao_pai};{self.Ano_ingresso};{self.Coeficiente}\n"
        return linha.encode("utf-8")
    
    def transformar_em_bytes_fixo(self) -> bytes:
        padding_char = b'#'
        sep = b';'
        nl = b'\n'
        mat = str(self.Matricula).encode('utf-8')[:9].ljust(9, padding_char)
        nome = self.Nome.replace(" ", "#").encode('utf-8')[:50].ljust(50, padding_char)
        cpf = str(self.CPF).encode('utf-8')[:11].ljust(11, padding_char)
        curso = self.Curso.replace(" ", "#").encode('utf-8')[:30].ljust(30, padding_char)
        mae = self.Filiacao_mae.replace(" ", "#").encode('utf-8')[:30].ljust(30, padding_char)
        pai = self.Filiacao_pai.replace(" ", "#").encode('utf-8')[:30].ljust(30, padding_char)
        ano = str(self.Ano_ingresso).encode('utf-8')[:4].ljust(4, padding_char)
        ca = str(self.Coeficiente).encode('utf-8')[:8].ljust(8, padding_char)
        resumo_bytes = (mat + sep + nome + sep + cpf + sep + curso + sep + mae + sep + pai + sep + ano + sep + ca + nl)
        return resumo_bytes
class Bloco:
    def __init__(self, tamanho_maximo, indice):
      self.Tamanho_maximo = tamanho_maximo
      self.ocupado = 0
      self.indice_bloco = indice
      self.bloco = []

    def testar_se_cabe(self,tamanho_registro):
        return self.ocupado + tamanho_registro <= self.Tamanho_maximo
    
    def adicionar_registro(self, registro_embytes):
        tamanho = len(registro_embytes)
        self.bloco.append(registro_embytes)
        self.ocupado += tamanho

    def gravar_em_arquivos(self):
        nome_arquivo = f"bloco_{self.indice_bloco}.dat"
        with open(nome_arquivo, "ab") as arquivo:
            for registro in self.bloco:
                arquivo.write(registro)

    def registro_contiguo(self, registro_embytes)-> bool:
        tamanho_registro = len(registro_embytes)
        if self.testar_se_cabe(tamanho_registro):
            self.bloco.append(registro_embytes)
            self.ocupado += tamanho_registro
            return True
        else:
            return False
    def gravar_arquivo_unico(self):
        nome_arquivo = f"Alunos.dat"
        with open(nome_arquivo, "ab") as arquivo:
            for registro in self.bloco:
                arquivo.write(registro)
    def registro_espalhado(self, registro_embytes)->bool:
        tamanho_registro = len(registro_embytes)
        espaco = self.Tamanho_maximo - self.ocupado
        if espaco == 0:
            return registro_embytes
        tamanho_pedaco = min(espaco, tamanho_registro)
        parte1 = registro_embytes[:tamanho_pedaco]
        parte2 = registro_embytes[tamanho_pedaco:]
        self.bloco.append(parte1)
        self.ocupado += tamanho_pedaco
        return parte2
    


class Estatisticas:
    def __init__(self, blocos):
        self.Blocos = blocos
    def calcular(self, tamanho_max):
        quantos_blocos = len(self.Blocos)
        total_bytes = sum(b.ocupado for b in self.Blocos)
        blocos_parciais = sum(1 for b in self.Blocos if b.ocupado < tamanho_max)
        eficiencia = (total_bytes / (quantos_blocos * tamanho_max)) * 100
        for b in self.Blocos:
            percentual = (b.ocupado / tamanho_max) * 100
            print(f"Bloco {b.indice_bloco}: {b.ocupado} bytes ({percentual:.1f}%)")
        print(f"\nTotal de blocos: {quantos_blocos}")
        print(f"Blocos parcialmente usados: {blocos_parciais}")
        print(f"Eficiência total: {eficiencia:.1f}%")

def main():
    for arquivo in glob.glob("bloco_*.dat"):
        os.remove(arquivo)
    if os.path.exists("Alunos.dat"):
        os.remove("Alunos.dat")
    print("Arquivos antigos removidos.\n")

    tamanho_bloco = int(input("Digite o tamanho máximo do bloco (em bytes): "))
    num_registros = int(input("Quantos alunos gerar: "))

    
    while True:
        modo = int(input("1 - Tamanho fixo 2 - Tamanho variável: "))
        if modo not in (1, 2):
            print("Opção inválida! Tente novamente.\n")
        else:
            break
    
    modo_variavel = 1
    if modo == 2:
        while True:
            modo_variavel = int(input("1- Registro contíguo e 2 - Registro espalhado: "))
            if modo_variavel not in (1, 2):
                print("Opção inválida! Tente novamente.\n")
            else:
                break
    blocos_usados = []
    bloco_indice = 0
    bloco_atual = Bloco(tamanho_bloco, bloco_indice)
    
    bloco_unico = Bloco(tamanho_bloco, "Alunos")
    for _ in range(num_registros):
        aluno = Estudante.gerar_aluno()
        registro_embytes = aluno.transformar_em_bytes_variavel() if modo == 2 else aluno.transformar_em_bytes_fixo()
        
        bloco_unico.bloco.append(registro_embytes)

        if modo == 1 or (modo == 2 and modo_variavel == 1):
            if not bloco_atual.registro_contiguo(registro_embytes):
                bloco_atual.gravar_em_arquivos()
                blocos_usados.append(bloco_atual)
                bloco_indice += 1
                bloco_atual = Bloco(tamanho_bloco, bloco_indice)
                bloco_atual.registro_contiguo(registro_embytes)

        elif modo == 2 and modo_variavel == 2:
            restante = registro_embytes
            while len(restante) > 0:
                restante = bloco_atual.registro_espalhado(restante)
                if len(restante) > 0:
                    bloco_atual.gravar_em_arquivos()
                    blocos_usados.append(bloco_atual)
                    bloco_indice += 1
                    bloco_atual = Bloco(tamanho_bloco, bloco_indice)

    if bloco_atual.ocupado > 0:
        bloco_atual.gravar_em_arquivos()
        blocos_usados.append(bloco_atual)

   
    bloco_unico.gravar_arquivo_unico()
    
    estat = Estatisticas(blocos_usados)
    estat.calcular(tamanho_bloco)

if __name__ == "__main__":
    main()