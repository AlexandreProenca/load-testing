# coding: utf-8
import datetime

class Target(object):
    """
    Abstract object to be inherited with our pre-configurations,
    and few static methods to helps share and handle paths, string, endpoint, and stuff like that
    """

    content_type = 'application/json;charset=UTF-8'
    origin = 'https://xxx-domain.com'
    autorization = ''
    accept = 'application/json'
    user_agent = 'SocialBase/Android'
    referer = 'https://xxx-domain.com'
    url_login = 'https://xxx-domain.com/authentication'

    header = {
            "Origin": origin,
            "Content-Type": content_type,
            "Accept": content_type,
            "Authorization": autorization,
            "User-Agent": user_agent,
            "Referer": origin
    }



data = [{"body": """Mussum ipsum cacilds, vidis litro abertis. Consetis adipiscings elitis. Pra lá ,
                                depois divoltis porris, paradis. Paisis, filhis, espiritis santis. Mé faiz elementum
                                girarzis, nisi eros vermeio, in elementis mé pra quem é amistosis quis leo.
                                Manduma pindureta quium dia nois paga. Sapien in monti palavris qui num significa nadis
                                i pareci latim. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num
                                gostis.
                                Ass: Mussum
                                """},
        {"body": """Se hoje é o dia das crianças... Ontem eu disse: o dia da criança é o dia da mãe, dos
                                pais, das professoras, mas também é o dia dos animais, sempre que você olha uma criança,
                                há sempre uma
                                figura oculta, que é um cachorro atrás. O que é algo muito importante!
                                Primeiro eu queria cumprimentar os internautas. -Oi Internautas! Depois dizer que o meio
                                ambiente é sem dúvida nenhuma uma ameaça ao desenvolvimento sustentável. E isso
                                significa que é uma ameaça pro futuro do nosso planeta e dos nossos países. O desemprego
                                beira 20%, ou seja, 1 em cada 4 portugueses.
                                Ass: Dilma
                                """},
        {"body": """Eu não queria perguntar isso publicamente, ma vou perguntar.
                                Carla, você tem o ensino fundamentauam? Ma vale dérreaisam? Boca sujuam... sem
                                vergonhuamm. Ma você, topa ou não topamm. Eu não queria perguntar isso publicamente,
                                ma vou perguntar. Carla, você tem o ensino fundamentauam? Eu não queria perguntar isso
                                publicamente, ma vou perguntar. Carla, você tem o ensino fundamentauam? É fácil ou não
                                éam? Um, dois três, quatro, PIM, entendeuam? Ma vejam só, vejam só.
                                Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você vai gerar textuans ha
                                haae.
                                Ass: Silvio Santos
                                ."""},
        {"body": """Eiiitaaa Mainhaaa!! Esse Lorem ipsum é só na sacanageeem!! E que abundância meu irmão
                                viuu!! Assim você vai matar o papai. Só digo uma coisa, Domingo ela não vai! Danadaa!!
                                Vem minha odalisca, agora faz essa cobra coral subir!!! Pau que nasce torto,
                                Nunca se endireita. Tchannn!! Tchannn!! Tu du du pááá! Eu gostchu muitchu, heinn!
                                danadinha! Mainhaa! Agora use meu lorem ipsum ordinária!!! Olha o quibeee! rema, rema,
                                ordinária!.
                                Ass: Compadre Washington
                                """},

        ]

behavior_home = [
    '/v3/users/me',
    '/v3/chat',
    '/v3/users/me/groups?offset=0&limit=10',
    '/v3/birthdays?currentDate=' + str(datetime.date.today()),
    '/v3/activities?limit=10'
]

behavior_novidades = [
    '/v3/users/me/groups?offset=0&limit=10',
    '/v3/members?external=False&offset=0&limit=10',
    '/v3/birthdays?currentDate=' + str(datetime.date.today()),
    '/v3/activities?limit=10'
]

behavior_grupo = [
    '/v3/users/me/groups?offset=0&limit=10',
    '/v3/members?external=False&offset=0&limit=10',
    '/v3/birthdays?currentDate=' + str(datetime.date.today())
]

group_data = {
    "description": "Meu Grupo, criado automaticamente com a ferramenta de load",
    "photo": "/images/data/group_picture.png",
    "photo_id": None,
    "privacy": False,
    "search": True,
    "title": "Grupo 1"
}

group_message = {
    "body": "Mensagem para todas as pessoas da rede ",
    "target": {
        id: 1,
        type: "group"}
    }



room_list = [
    {"email": "usersb9@socialbase.com.br", "room_id": "1c412938-a103-4817-8fdd-12b5b0610d8d"},
    {"email": "usersb97@socialbase.com.br", "room_id": "ef517b9d-64de-4a82-b38e-f066f394ffdb"},
    {"email": "usersb45@socialbase.com.br", "room_id": "d3c1aaf1-11d3-4d37-bbaf-25cb56e5b2b6"},
    {"email": "usersb61@socialbase.com.br", "room_id": "f712d39e-3d91-49ed-8da0-7c87c03eb3ce"},
    {"email": "usersb75@socialbase.com.br", "room_id": "2acb674b-15a4-474f-9214-26d3c44751c0"},
    {"email": "usersb25@socialbase.com.br", "room_id": "a378b18c-1c16-4329-b7c6-ae2542ab41e2"},
    {"email": "usersb27@socialbase.com.br", "room_id": "95b75dab-d81c-47d4-811c-d114f3552003"},
    {"email": "usersb74@socialbase.com.br", "room_id": "2f0bc1e0-112d-4a93-b136-1792134970d4"},
    {"email": "usersb16@socialbase.com.br", "room_id": "46696f1b-e9af-4cb0-91e4-5be730d2481a"},
    {"email": "usersb34@socialbase.com.br", "room_id": "5adb8d30-67e1-4963-ba95-9f2b2727549b"},
    {"email": "usersb39@socialbase.com.br", "room_id": "8b0c3459-82e6-4738-9818-05e7416e481a"},
    {"email": "usersb35@socialbase.com.br", "room_id": "0da4a5b4-4d13-4cb1-95fc-0760cc66bb70"},
    {"email": "usersb32@socialbase.com.br", "room_id": "6efbaac6-6ca7-44d0-963d-e4695362bd98"},
    {"email": "usersb71@socialbase.com.br", "room_id": "65dda5d0-a447-432e-921c-1da1c34754eb"},
    {"email": "usersb46@socialbase.com.br", "room_id": "ae69d550-990f-471d-a5d3-7bb7310e7e33"},
    {"email": "usersb54@socialbase.com.br", "room_id": "2a2829e9-76b6-4774-a2ff-a3030e5559e2"},
    {"email": "usersb48@socialbase.com.br", "room_id": "e80c4c07-35f0-4c6a-b087-e9098d2a612c"},
    {"email": "usersb23@socialbase.com.br", "room_id": "f9fb684a-5085-455a-b8c5-2314d7b5fc9c"},
    {"email": "usersb59@socialbase.com.br", "room_id": "f9ff2ed1-2981-4199-b50a-5c615deb6aac"},
    {"email": "usersb26@socialbase.com.br", "room_id": "c779982d-a37d-4d5a-897b-54d96438e86b"},
    {"email": "usersb4@socialbase.com.br", "room_id": "4fd665e2-ae05-4fd9-9014-aec355457d61"},
    {"email": "usersb57@socialbase.com.br", "room_id": "9e1273a8-8cda-4744-ae5b-0d323bce16d5"},
    {"email": "usersb53@socialbase.com.br", "room_id": "99c8e13f-2249-4562-91d5-a1fcf7e436a9"},
    {"email": "usersb84@socialbase.com.br", "room_id": "aeba835d-94c7-462f-86ab-d25d1751e632"},
    {"email": "usersb1@socialbase.com.br", "room_id": "162b741d-65e1-4fd8-aa81-473187385a54"},
    {"email": "usersb47@socialbase.com.br", "room_id": "2a2d683f-872c-4569-a2e1-1356e18fb9dd"},
    {"email": "usersb90@socialbase.com.br", "room_id": "7038aa14-270c-4334-9eae-c0f38308cc45"},
    {"email": "usersb19@socialbase.com.br", "room_id": "8ed014f1-6bca-488e-92eb-ae7610c1e266"},
    {"email": "usersb31@socialbase.com.br", "room_id": "79d3c445-fe9d-46cf-bb66-5382ea77d1ca"},
    {"email": "usersb96@socialbase.com.br", "room_id": "33f841a0-4010-42d6-8fe3-9d3f67b9e162"},
    {"email": "usersb73@socialbase.com.br", "room_id": "5977ffe5-8920-4563-bdf0-fc145afb28c1"},
    {"email": "usersb87@socialbase.com.br", "room_id": "b260bf23-a058-4316-8b13-33d67fefb7e8"},
    {"email": "usersb89@socialbase.com.br", "room_id": "fad3f3e8-e6b3-4303-b98e-b02af43c4b91"},
    {"email": "usersb40@socialbase.com.br", "room_id": "f602e8bb-9c81-4012-8bb0-294717e5dafd"},
    {"email": "usersb49@socialbase.com.br", "room_id": "e726fba7-9ec5-41ed-b0aa-ba86fb9ac7d3"},
    {"email": "usersb68@socialbase.com.br", "room_id": "a73ddedd-ff98-4eb4-9de8-915c3ecaca33"},
    {"email": "usersb51@socialbase.com.br", "room_id": "17e48eb0-3243-4c90-ad08-f8f5aec98f2b"},
    {"email": "usersb66@socialbase.com.br", "room_id": "658bb82b-b698-4316-a325-e8a2eb43e196"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "c2c8c379-3987-4ddf-b989-9c2caafb8dfa"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "b9f100fe-d8a3-44aa-9978-52e7f34cb389"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "2893a29b-a3a8-40bd-ba5d-b1a8d0e410ed"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "59d9531a-b1c4-4974-9204-92f6d9eebe0a"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "e459a5f6-7d4f-4a59-8942-1112b58bd627"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "7bdcfd09-0888-4531-8fb1-a6143fa17fb1"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "32d3645b-06fe-40e2-b55b-ec06d033d187"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "4f552d32-c1c9-4b1c-b003-2bd49ed39fee"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "a3e9634b-60f1-49a5-a8f3-cf48f7228272"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "bf0c3ade-75c6-427a-a099-26a948a7d363"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "3c2f0582-303f-4826-86e6-28479dbead37"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "569fe400-ad2b-44e8-88df-de29897e010c"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "641cfe91-e70c-4035-8ad3-e58d3fcba619"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "3c57c6cc-7134-4159-9cb9-857da7907382"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "a7d79c1f-6897-46fc-a33c-74ee5a93335f"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "751134e0-80f0-454d-9b7a-41218b1397fe"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "e36ccb62-8e34-4b92-bebd-dd2970cef956"},
    {"email": "admin@socialbase.com.br1", "room_id": "aa195925-d6e4-43c6-ac8e-1889abeca2e1"},
    {"email": "admin@socialbase.com.br1", "room_id": "9e7c10dd-1f3a-4259-8008-1477fd077f77"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "0b4db968-7caf-4c9d-b9e4-4d60511883d5"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "4996eef9-ae6a-4b1c-a30e-98bebe65f9c0"},
    {"email": "sbsuporte@socialbase.com.br1", "room_id": "1aeb3cfa-90fa-46b3-bc48-3bc5758cf7f4"}
]

ws_server = "wss://l-websocket.socialbase.com.br/ws"

cor = {
    'ROXO': '\033[95m',
    'AZUL': '\033[94m',
    'VERDE': '\033[92m',
    'AMARELO': '\033[93m',
    'VERMELHO': '\033[91m',
    'BRANCO': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}


def output(color, message):
    char = 'HH'
    print(str(cor[color] + 20 * char + message + 20 * char + cor['BRANCO']))

