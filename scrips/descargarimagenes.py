import requests
import os

def descargar_pokemon_images(pokemon_ids, output_dir="pokemon_images"):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"

    for pokemon, id_ in pokemon_ids.items():
        image_url = f"{base_url}{id_}.png"
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(os.path.join(output_dir, f"{pokemon}.png"), "wb") as f:
                f.write(response.content)
            print(f"Imagen de {pokemon} descargada correctamente.")
        else:
            print(f"No se pudo descargar la imagen de {pokemon}.")

pokemon_ids = {
    "Articuno": 144,
    "Zapdos": 145,
    "Moltres": 146,
    "Mewtwo": 150,
    "Mew": 151,
    "Raikou": 243,
    "Entei": 244,
    "Suicune": 245,
    "Lugia": 249,
    "Ho-Oh": 250,
    "Celebi": 251,
    "Regirock": 377,
    "Regice": 378,
    "Registeel": 379,
    "Latias": 380,
    "Latios": 381,
    "Kyogre": 382,
    "Groudon": 383,
    "Rayquaza": 384,
    "Jirachi": 385,
    "Deoxys": 386,
    "Heatran": 485,
    "Cresselia": 488,
    "Regigigas": 486,
    "Uxie": 480,
    "Mesprit": 481,
    "Azelf": 482,
    "Dialga": 483,
    "Palkia": 484,
    "Giratina": 487,
    "Phione": 489,
    "Manaphy": 490,
    "Darkrai": 491,
    "Shaymin": 492,
    "Arceus": 493,
    "Cobalion": 638,
    "Terrakion": 639,
    "Virizion": 640,
    "Tornadus": 641,
    "Thundurus": 642,
    "Landorus": 645,
    "Reshiram": 643,
    "Zekrom": 644,
    "Kyurem": 646,
    "Victini": 494,
    "Meloetta": 648,
    "Genesect": 649,
    "Keldeo": 647,
    "Xerneas": 716,
    "Yveltal": 717,
    "Zygarde": 718,
    "Diancie": 719,
    "Hoopa": 720,
    "Volcanion": 721,
    "Cosmog": 789,
    "Cosmoem": 790,
    "Solgaleo": 791,
    "Lunala": 792,
    "Necrozma": 800,
    "Magearna": 801,
    "Marshadow": 802,
    "Zeraora": 807,
    "Meltan": 808,
    "Melmetal": 809,
    "Shaymin (Forma Tierra)": 492,
    "Shaymin (Forma Cielo)": 492,
    "Meloetta (Forma Lírica)": 648,
    "Meloetta (Forma Danza)": 648,
    "Hoopa (Forma Desatada)": 720,
    "Código Cero": 772,
    "Silvally": 773,
    "Tapu Koko": 785,
    "Tapu Lele": 786,
    "Tapu Bulu": 787,
    "Tapu Fini": 788
}

# Descargar imágenes
descargar_pokemon_images(pokemon_ids)
