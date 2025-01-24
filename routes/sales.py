from flask import render_template, url_for, redirect, request


products = {
  "productos": [
    {
        "img": "https://www.pianosbogota.com/wp-content/uploads/2023/11/MICROFONO-SHURE-MV7X.png" ,
        "nombre": "Microfono Shure",
        "precio": 130000
    },
    {
        "img": "https://http2.mlstatic.com/D_NQ_NP_958184-MLU75193472291_032024-O.webp",
        "nombre": "Mouse Logitech G203",
        "precio": 135000
    },
    {
        "nombre": "Teclado Redragon Kumara", 
        "img": "https://www.mipcparquecentral.com/cdn/shop/files/kumara_Redragon.png?v=1734534979",
        "precio": 220000
    }
  ]
}


def sales():
    return render_template('sales.html',productos=products['productos'])