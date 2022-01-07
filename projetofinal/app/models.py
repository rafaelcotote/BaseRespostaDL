from django.db import models

# Create your models here.

class Proprietario(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=20, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome

class Acessorio(models.Model):
    ESTADO_CHOICES = (
        ("ótimo", "Ótimo"),
        ("bom", "Bom"),
        ("ruim", "Ruim"),
    )
    descricao = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, null=False)

    def __str__(self):
        return self.descricao

class Oficios(models.Model):

    oficios = models.CharField(max_length=50, null=False, verbose_name="Número do Ofício")
    orgao = models.CharField(max_length=50, null=False, verbose_name="Órgão")
    envio = models.DateField(null=False, verbose_name="Data do Envio")
    temaofi = models.CharField(max_length=50, null=False, verbose_name="Tema do Ofício")
    anexs = models.FileField(null=True, upload_to='anexooficio/')
    questionamento = models.TextField(blank=True)
    recebimento = models.DateField(null=False, verbose_name="Data do Recebimento")
    conteudo = models.TextField(blank=True)
    icon_name = 'description'

    def __str__(self):
        return self.temaofi

class Consulta(models.Model):

    numticket = models.CharField(max_length=50, null=False, verbose_name="Número do Ticket")
    assunt = models.CharField(max_length=50, null=False, verbose_name="Tema")
    client = models.CharField(max_length=50, null=False, verbose_name="CLiente")
    agent = models.CharField(max_length=50, null=False, verbose_name="Agente responsável")
    dataresp = models.DateField(null=False, verbose_name="Data da Resposta")
    conteudo = models.TextField(blank=True)

    def __str__(self):
        return self.assunt


class Veiculo(models.Model):
    CORES_CHOICES = (
        ("preto", "Preto"),
        ("azul", "Azul"),
        ("amarelo", "Amarelo"),
        ("branco", "Branco"),
        ("prata", "Prata"),
        ("vermelho", "Vermelho"),
    )

    TIPO_CHOICES = (
        ("moto", "Moto"),
        ("carro", "Carro"),
    )

    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    placa = models.CharField(max_length=8, null=False)
    cor = models.CharField(max_length=20, null=False, choices=CORES_CHOICES)
    ano = models.IntegerField(null=False)
    preco = models.FloatField(null=False)
    foto_capa = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return self.modelo