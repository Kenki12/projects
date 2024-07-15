def download_the_image(link, path):
    import requests
    from bs4 import BeautifulSoup
    from win11toast import toast

    image_number = 0
    # link = "https://coomer.su/onlyfans/user/sweetiefox_of/post/899384727"

    #response = requests.get(link).text
    #soup = BeautifulSoup(response, "lxml")
    #block = soup.find("div", class_="post__files")
    #all_image = block.find_all("div", class_="post__thumbnail")

    for i in link:
        response = requests.get(i).text
        soup = BeautifulSoup(response, "lxml")
        block = soup.find("div", class_="post__files")
        all_image = block.find_all("div", class_="post__thumbnail")

        for image in all_image:
            image_link = image.find("a").get("href")
            print(image_link)
            image_bytes = requests.get(image_link).content

            with open(f"{path}/{image_number}.jpg", "wb") as file:
                file.write(image_bytes)
                image_number += 1
                print(f'Image {image_number}.jpg download successful!')

    toast("COOMER.SU DOWNLOADER", "Download complete!, click to open!", on_click=fr"{path}")
