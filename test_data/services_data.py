BASE_SERVICES = [
    "билайн тв",
    "облако",
    "книги"
]

REGION_DOP_SERVICES = {
    "krasnodar": ["игры"],
    "moskva": ["игры"] #использовал тот же, но допустим они бы отличались, хз у красннодара мог бы быть роуминг
}

def get_dop_services(region: str):
    #  буду возвращать сервисы доступные региону
    services = BASE_SERVICES.copy()
    services += REGION_DOP_SERVICES.get(region, [])

    return services
