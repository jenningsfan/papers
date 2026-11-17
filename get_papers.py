import requests

def download_and_save(url, subject, paper, name):
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"papers/{subject}/{paper}/{name}.pdf"
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Maths
for paper in range(1, 4):
    for year in range(2018, 2026):
        url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA/Paper-{paper}/QP/June%20{year}%20QP.pdf"
        download_and_save(url, "Maths", f"{paper}", f"June {year} QP")
        url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA/Paper-{paper}/MS/June%20{year}%20MS.pdf"
        download_and_save(url, "Maths", f"{paper}", f"June {year} MS")

    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA/Paper-{paper}/QP/Specimen QP.pdf"
    download_and_save(url, "Maths", f"{paper}", f"Specimen QP")
    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA/Paper-{paper}/MS/Specimen MS.pdf"
    download_and_save(url, "Maths", f"{paper}", f"Specimen MS")

# NOTE: 2020/2021/2022 need .PDF not .pdf
# Further Maths Pure
for paper in range(1, 3):
    for year in list(range(2019, 2020)) + list(range(2023, 2026)):
        url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/QP/June%20{year}%20QP.pdf"
        download_and_save(url, "Further Maths", f"{paper}", f"June {year} QP")
        url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/MS/June%20{year}%20MS.pdf"
        download_and_save(url, "Further Maths", f"{paper}", f"June {year} MS")
    for year in range(2020, 2023):
            url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/QP/June%20{year}%20QP.PDF"
            download_and_save(url, "Further Maths", f"{paper}", f"June {year} QP")
            url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/MS/June%20{year}%20MS.PDF"
            download_and_save(url, "Further Maths", f"{paper}", f"June {year} MS")

    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/QP/Specimen QP.pdf"
    download_and_save(url, "Further Maths", f"{paper}", f"Specimen QP")
    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-{paper}/MS/Specimen MS.pdf"
    download_and_save(url, "Further Maths", f"{paper}", f"Specimen MS")

# NOTE: 2020/2021/2022 need .PDF not .pdf
# Further Maths 3
for module in ["Mechanics", "Discrete"]:
    for year in list(range(2019, 2021)) + list(range(2023, 2026)):
            url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/QP/June%20{year}%20QP.pdf"
            download_and_save(url, "Further Maths", f"3 - {module}", f"June {year} QP")
            url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/MS/June%20{year}%20MS.pdf"
            download_and_save(url, "Further Maths", f"3 - {module}", f"June {year} MS")
    for year in range(2020, 2023):
                url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/QP/June%20{year}%20QP.PDF"
                download_and_save(url, "Further Maths", f"3 - {module}", f"June {year} QP")
                url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/MS/June%20{year}%20MS.PDF"
                download_and_save(url, "Further Maths", f"3 - {module}", f"June {year} MS")

    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/QP/Specimen QP.pdf"
    download_and_save(url, "Further Maths", f"3 - {module}", f"Specimen QP")
    url = f"https://pmt.physicsandmathstutor.com/download/Maths/A-level/Papers/AQA-Further/Paper-3-{module}/MS/Specimen MS.pdf"
    download_and_save(url, "Further Maths", f"3 - {module}", f"Specimen MS")

for paper in list(range(1, 3)) + ["3A", "3B-C"]:
    for year in range(2017, 2026):
        url = f"https://pmt.physicsandmathstutor.com/download/Physics/A-level/Past-Papers/AQA/Paper-{paper}/QP/June%20{year}%20QP.pdf"
        download_and_save(url, "Physics", f"{paper}", f"June {year} QP")
        url = f"https://pmt.physicsandmathstutor.com/download/Physics/A-level/Past-Papers/AQA/Paper-{paper}/MS/June%20{year}%20MS.pdf"
        download_and_save(url, "Physics", f"{paper}", f"June {year} MS")

    url = f"https://pmt.physicsandmathstutor.com/download/Physics/A-level/Past-Papers/AQA/Paper-{paper}/QP/Specimen QP.pdf"
    download_and_save(url, "Physics", f"{paper}", f"Specimen QP")
    url = f"https://pmt.physicsandmathstutor.com/download/Physics/A-level/Past-Papers/AQA/Paper-{paper}/MS/Specimen MS.pdf"
    download_and_save(url, "Physics", f"{paper}", f"Specimen MS")