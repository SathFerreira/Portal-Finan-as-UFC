from django.db import models

# Para o "Dicionário de Finanças"
class TermoFinanceiro(models.Model):
    termo = models.CharField(max_length=100, unique=True)
    definicao = models.TextField()

    # ... seus campos ...
    class Meta:
        ordering = ['termo'] # para manter os 500 termos em ordem de A a Z
    def __str__(self):
        return self.termo
    

class Disciplina(models.Model):
    SEMESTRES = [
        (1, '1º Semestre'),
        (2, '2º Semestre'),
        (3, '3º Semestre'),
        (4, '4º Semestre'),
        (5, '5º Semestre'),
        (6, '6º Semestre'),
        (7, '7º Semestre'),
        (8, '8º Semestre'),
    ]

    nome = models.CharField(max_length=100)
    
    professores = models.CharField(
        max_length=200, 
        help_text="´Professores que lecionam a cadeira",
        verbose_name="Professor(es) comum(ns)"
    )
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)
    descricao = models.TextField()
    semestre = models.IntegerField(choices=SEMESTRES, default=1)
    dificuldade = models.IntegerField(default=3)

    def __str__(self):
        return self.nome
 # Para "drive"   
class MaterialApoio(models.Model):
    CATEGORIA_CHOICES = [
        ('1', '1º Semestre'), ('2', '2º Semestre'), ('3', '3º Semestre'), ('4', '4º Semestre'),
        ('5', '5º Semestre'), ('6', '6º Semestre'), ('7', '7º Semestre'), ('8', '8º Semestre'),
        ('OPT', 'Optativas'), ('EQUIV', 'Equivalentes'), ('EXTRA', 'Materiais Extras'),
    ]

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='materiais')
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES)
    link_drive = models.URLField()

    def __str__(self):
        return f"{self.disciplina.nome} - {self.titulo}"
# Para "Bolsas"
class BolsaUFC(models.Model):
    TIPOS = (
        ('MONITORIA', 'Monitoria'),
        ('PESQUISA', 'Iniciação Científica (PIBIC)'),
        ('EXTENSAO', 'Extensão'),
        ('APOIO', 'Auxílio Estudantil (PRAE)'),
    )
    titulo = models.CharField(max_length=200, verbose_name="Nome da Bolsa")
    orgao_emissor = models.CharField(max_length=100, verbose_name="Órgão (Ex: PROGRAD, PRAE, FEAAC)")
    descricao = models.TextField(verbose_name="Requisitos e Benefícios")
    link_edital = models.URLField(verbose_name="Link do Edital Oficial")
    tipo = models.CharField(max_length=20, choices=TIPOS)
    data_publicacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Bolsa UFC"
        verbose_name_plural = "Bolsas Acadêmicas UFC"

    def __str__(self):
        return self.titulo
    
class LinkEssencial(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Sistema/Site")
    descricao = models.CharField(max_length=200, verbose_name="Para que serve?")
    url = models.URLField(verbose_name="Link de Acesso")
    icone = models.CharField(
        max_length=50, 
        default="fas fa-external-link-alt", 
        help_text="Ícone FontAwesome (Ex: fas fa-laptop, fas fa-globe)"
    )

    class Meta:
        verbose_name = "Link Essencial"
        verbose_name_plural = "Links Essenciais"

    def __str__(self):
        return self.nome

class MaterialApoio(models.Model):
    TIPOS = (
        ('PROVA', 'Provas Antigas / Resoluções (Drive)'),
        ('PDF', 'Livro / Apostila / Resumo (PDF)'),
        ('VIDEO', 'Vídeo Aula (YouTube)'),
        ('PLANILHA', 'Planilha (Excel/Sheets)'),
        ('OUTRO', 'Outros Formatos'),
    )
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField(verbose_name="Resumo do Material")
    link_acesso = models.URLField(verbose_name="Link do Arquivo (Google Drive, OneDrive, etc)")

    class Meta:
        verbose_name = "Material de Apoio"
        verbose_name_plural = "Materiais de Apoio"

    def __str__(self):
        return self.titulo
