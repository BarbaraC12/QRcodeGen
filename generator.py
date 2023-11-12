import qrcode

def generate_qr_code(url, output_path):
    '''
    Créer un objet QRCode a partir d'une adresse
    '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    # PNG : img = qr.make_image(fill_color="black", back_color="white", image_factory=PyPNGImage)


    img.save(output_path)

if __name__ == "__main__":
    url = input("Entrez l'adresse HTTPS : ")

    output_path = input("Entrez le chemin de sortie du fichier : ")

    generate_qr_code(url, output_path)

    print(f"QRCode généré avec succès et sauvegardé à {output_path}")
