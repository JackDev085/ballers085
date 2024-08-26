from ballers085.models import Treinos, Exercicios  # Importe seus modelos

"""treinos_data = {
  "title": "Treinos",
  "values": [
    ["Treino de drible - 1", "Treine seu drible na quadra.", "30 min", "2024-07-08 16:17:27.004098+00", "drible", "treino_drible_1","-Tk5_a83rjg"],
    ["Arremesso - média distância", "Melhore seu arremesso no perímetro", "40 min", "2024-07-08 16:19:00.777722+00", "arremesso", "media_distancia_1", "PqSasSwtGR4"],
    ["Treino de inferiores", "Carga: moderada", "~1 hora e 20 minutos", "2024-07-15 02:48:54.184296+00", "academia", "treino_academia_inferiores", "W-jkyAlyAdc"],
    ["Treino de superiores", "Carga: Moderada", "~1 hora e 20 minutos", "2024-07-15 02:46:59.811043+00", "academia", "treino_academia_superiores", "vT-QcEQC1M4"],
    ["Rotina de condicionamento", "Melhore seu físico.", "30 min", "2024-07-08 16:15:48.805059+00", "fisico", "rotina_condicionamento", "QJx_5rRR8_w"]
  ],
  "fields": ["nome", "descricao", "duracao", "data_criacao", "categoria", "caminho_treino_url", "id", "criador_id", "link_video_treino"],
  "types": [1043, 25, 1043, 1184, 1043, 1043, 23, 20, 1043]
}"""
exercicios_data = {
    "title": "Exercicios",
    "values": [
        ["Alongamento | Mobilidade","10 - 15 minuto","O8UkFIBhSi0",4],
        [
            "Bíceps triáde",
            "1x3 min (Ouça a explicação)",
            "T_pVdfzngyw",
            4
        ],
        [
            "Supino com halteres",
            "4x8 repetições",
            "ZV6GAB__vkE",
            4
        ],
        [
            "Remada unilateral",
            "3x8 repetições",
            "JLgkueCanew",
            4

        ],
        [
            "Elevação lateral",
            "3x12 repetiçoes",
            "Zpc8YpHtikQ",
            4
        ],
        [
            "Tríceps na polia",
            "2x1 minuto",
            "4xk3Ri1uroM",
            4
        ],
        [
            "Supino inclinado com halteres",
            "3x10 repetiçoes",
            "y35m-0gcJOI",
            4
        ],
        [
            "Desenvolvimento de ombros",
            "3x10 repetiçoes",
            "JgTsQF3XllI",
            4
        ],
        [
            "Puxada no cabo",
            "3x8 repetições",
            "SkB7rea_rqE",
            4
        ],
        [
            "Flexão de braço",
            "50 repetições ( x séries )",
            "a6sOSx69A5E",
            4
        ],
        [
            "Isometria em flexão",
            "2 séries indo até a falha",
            "uV2XOCfgRoc",
            4
        ],
        [
            "Flexão de braço",
            "50 repetições ( x séries )",
            "kV4gIXCFgL4",
            5
        ],
        [
            "Agachamento",
            "50 repetições ( x séries )",
            "GXe89NaE9Ss",
           5
        ],
        [
            "Abdominal",
            "50 repetições ( x séries )",
            "-xZ8j6UzMo8",
            5
        ],
        [
            "Prancha",
            "2x1 minuto",
            "A0mh0MMuzV0",
            5
        ],
        [
            "Molde com 1 mão",
            "2x10 acertos ( cada mão )",
            "fdyMXCpIu0o",
            2
        ],
        [
            "Flow de arremesso",
            "2x10 acertos ( mão dominante )",
            "wCSFkDgrexI",
           2
        ],
        [
            "Stiff unilateral e arremesso",
            "2x5 acertos ( cada perna )",
            "Y13L26prd6g",
            2
        ],
        [
            "Lance livre",
            "2x10 acertos ( mão dominante )",
            "rZS4MmTqhOE",
            2
        ],
        [
            "Cardio + arremesso 1",
            "2 séries de 60 segundos",
            "wWU5AWjNoC0",
            2
        ],
        [
            "Cardio + arremesso 2",
            "2 séries de 60 segundos",
            "omf6E9-5vgU",
            2
        ],
        [
            "Drible alto, médio e baixo",
            "2x40 segundos",
            "UYrIc2L055I",
            1
        ],
        [
            "Drible em V",
            "2x30 segundos",
            "nrdSioRWwDg",
            1
        ],
        [
            "Entre as pernas",
            "2x30 segundos",
            "IgxolYZ1qEI",
            1
        ],
        [
            "Drible e raquetada",
            "2x30 segundos",
            "uGA9PLsRQ_Y",
            1
        ],
        [
            "Crossover e parada",
            "2x30 segundos",
            "dl25vgAKfiw",
            1
        ],
        [
            "Drible e troca",
            "2x30 segundos",
            "eu7rFgdTSDk",
            1
        ],
        [
            "Pernada e troca",
            "2x30 segundos",
            "TUN1hokc0dk",
            1
        ],
        [
            "Mecânica de pernada",
            "meia quadra ( ida e volta )",
            "DZg3hXABQFY",
            1
        ],
        [
            "Mecânica de raquetada",
            "meia quadra ( ida e volta )",
            "6hbt4DWoX10",
            1
        ],
        [
            "Mecânica de pernada invertida",
            "meia quadra ( ida e volta )",
            "cQ0_U__FwGk",
            1
        ],
        [
            "Alongamento | Mobilidade",
            "10 - 15 minutos",
            "N8zjV5Ux6hs",
            3
        ],
        [
            "Stiff",
            "3x12 repetições",
            "pxjMPUX-6eQ",
            3
        ],
        [
            "Agachamento búlgaro",
            "3x12 repetições",
            "4SwnIjFCP7U",
            3
        ],
        [
            "Subida na caixa",
            "3x10 repetiçoes",
            "_funBh9tz-s",
            3
        ],
        [
            "Panturilha no step",
            "3x12 repetições",
            "4Xv0KRc7r7c",
            3
        ],
        [
            "Agachamento explosivo",
            "3x8 repetições",
            "I2IJH_aZ5o4",
            3
        ],
        [
            "Avanço com halteres",
            "3x10 repetiçoes",
            "j3plo0PDxgs",
           3
        ]
    ]
}



from django.core.management.base import BaseCommand
from ballers085.models import Exercicios, Treinos  # Substitua 'your_app' pelo nome da sua aplicação

class Command(BaseCommand):
    help = 'Insere dados massivamente no banco de dados'

    def handle(self, *args, **kwargs):
        # Exemplo de lista de objetos para Treinos
        """treinos_objs = [
            Treinos(nome=treino[0], descricao=treino[1], duracao=treino[2],data_criacao=treino[3],categoria=treino[4] , caminho_treino_url=treino[5],link_video_treino=treino[6])
            for treino in treinos_data["values"]
        ]"""
        exercicios_objs=[]

        for exercicio in exercicios_data["values"]:
            treino_obj = Treinos.objects.get(id= exercicio[3])
            obj = Exercicios(nome=exercicio[0], repeticoes=exercicio[1], link=exercicio[2],treino=treino_obj)
            exercicios_objs.append(obj)
            

        

        # Executa o bulk_create para ambos os modelos

        #Treinos.objects.bulk_create(treinos_objs)
        Exercicios.objects.bulk_create(exercicios_objs)

        self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso!'))
