from settings import URL

CATEGORIES_ADVANCED = {

    "apartments" : {
        "1 room" : URL + "/kupit?rooms=1",
        "2 rooms" : URL + "/kupit-kvartiru?rooms=2",
        "3 rooms" : URL + "/kupit-kvartiru?rooms=3",
        "4 rooms" : URL + "/kupit-kvartiru?rooms=5",
        "5 rooms" : URL + "/kupit-kvartiru?rooms=6",
        "6 rooms and more" : URL + "/kupit-kvartiru?rooms=7",
        "open plan" : URL + "/kupit-kvartiru?rooms=8"
        },

    "houses" : {
        "1 room" : URL + "/kupit-dom?rooms=1",
        "2 rooms" : URL + "/kupit-dom?rooms=2",
        "3 rooms" : URL + "/kupit-dom?rooms=3",
        "4 rooms" : URL + "/kupit-dom?rooms=5",
        "5 rooms" : URL + "/kupit-dom?rooms=6",
        "6 rooms and more" : URL + "/kupit-dom?rooms=7",
        "open plan" : URL + "/kupit-dom?rooms=8"
    },

    "country house" : {
        "1 room" : URL + "/kupit-dachu?rooms=1",
        "2 rooms" : URL + "/kupit-dachu?rooms=2",
        "3 rooms" : URL + "/kupit-dachu?rooms=3",
        "4 rooms" : URL + "/kupit-dachu?rooms=5",
        "5 rooms" : URL + "/kupit-dachu?rooms=6",
        "6 rooms and more" : URL + "/kupit-dachu?rooms=7",
        "open plan" : URL + "/kupit-dachu?rooms=8"
    }

}


CATEGORIES = {

    "commercial real estate": URL + "/kupit-kommercheskaia-nedvijimost",

    "plot": URL + "/kupit-uchastok",

    "garage": URL + "/kupit-garaj"
}