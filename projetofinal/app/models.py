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

class Temes(models.Model):

    temm = models.CharField(max_length=50, null=False, blank=True, verbose_name="Tema")

    class Meta:
        db_table = "Temess"
        verbose_name = "Tema"

    def __str__(self):
        return self.temm

class Oficios(models.Model):
    OFICIO_CHOICES = [
        ("ANVISA", "ANVISA"),
        ("IBAMA", "IBAMA"),
        ("CONAMA", "CONAMA"),
        ("ANM", "ANM"),
        ("MAPA", "MAPA"),
        ("MTE", "MTE"),
        ("CBM", "CBM"),
    ]

    OFICIO_STATUS = [
        ("Aguardando Retorno", "Aguardando Retorno"),
        ("Retorno Recebido", "Retorno Recebido"),
    ]

    #LISTA_TEMAS = [
       # ("Emissões Atmosféricas", "Emissões Atmosféricas"),
        #("Resíduos Solidos", "Resíduos Sólidos"),
        #("Efluentes Líquidos", "Efluentes Líquidos"),
        #("Fertilizantes", "Fertilizantes"),
        #("Programa de Gerenciamento de Riscos - PGR", "Programa de Gerenciamento de Riscos - PGR"),
    #]

    responsavel_envio = models.CharField(max_length=50, null=False, verbose_name="Responsável pelo Envio")
    status_oficio = models.CharField(max_length=50, null=False, choices=OFICIO_STATUS, verbose_name="Status do Ofício")
    oficios = models.CharField(max_length=50, null=False, blank=True, verbose_name="Número do Ofício")
    titulo_oficio = models.CharField(max_length=50, null=False, verbose_name="Título do Ofício")
    orgao = models.CharField(max_length=50, null=False, choices=OFICIO_CHOICES, verbose_name="Órgão")
    #temaofi = models.CharField(max_length=50, null=False, choices=LISTA_TEMAS, verbose_name="Tema do Ofício")
    temm = models.ManyToManyField(Temes, verbose_name = "Tema")
    envio = models.DateField(null=False, verbose_name="Data do Envio")
    questionamento = models.TextField(verbose_name="Questionamento")
    conteudo = models.TextField(null=False, blank=True, verbose_name="Resposta do Ofício")
    anexs = models.FileField(null=False, blank=True, verbose_name="Anexo", upload_to='anexooficio/')
    recebimento = models.DateField(null=True, blank=True, verbose_name="Data do Recebimento")
    icon_name = "file-alt"

    def get_temm(self):
        return ",".join([str (p) for p in self.temm.all()])

    def __unicode__(self):
        return "{0}".format(self.oficios)

    class Meta:
        db_table = 'oficios'
        verbose_name = 'Ofício'

    def __str__(self):
        return self.oficios


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
    verbose_name = "Veículos"
    icon_name = "markunread"

    def __str__(self):
        return self.modelo
