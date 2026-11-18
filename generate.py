import os

subjects = ["Maths", "Further Maths", "Physics"]
subject_segments = []

single_template = open("template_paper_single.html", "r").read()
segment_template = open("template_paper_segment.html", "r").read()
page_template = open("template_page.html", "r").read()
subject_template = open("template_subject.html", "r").read()
german_template = open("template_paper_segment_german.html", "r").read()

def do_german():
    genned_qp = ""
    genned_ms = ""
    genned_insert = ""
    genned_tracked = ""
    genned_untracked = ""
    genned_transcript = ""

    years = [ f.name for f in os.scandir(f"papers/German/1") if f.is_dir() if f.name.isdigit() ]
    years.insert(0, "Specimen")

    for year in years:
        path = f"papers/German/1/{year}/"
        genned_qp += single_template.replace("%NAME%", f"June {year} QP").replace("%URL%", path + "QP.pdf")
        genned_ms += single_template.replace("%NAME%", f"June {year} MS").replace("%URL%", path + "MS.pdf")
        genned_insert += single_template.replace("%NAME%", f"June {year} Insert").replace("%URL%", path + "Insert.pdf")
        if os.path.exists(path + "Tracked.zip"):
            genned_tracked += single_template.replace("%NAME%", f"June {year} Tracked").replace("%URL%", path + "Tracked.zip")
        else:
            genned_tracked += single_template.replace("%NAME%", f"").replace("%URL%", "")
        if os.path.exists(path + "Untracked.mp3"):
            genned_untracked += single_template.replace("%NAME%", f"June {year} Untracked").replace("%URL%", path + "Untracked.mp3")
        else:
            genned_untracked += single_template.replace("%NAME%", f"").replace("%URL%", "")
        genned_transcript += single_template.replace("%NAME%", f"June {year} Transcript").replace("%URL%", path + "Transcript.pdf")

    paper1 = german_template.replace("%QP%", genned_qp).replace("%MS%", genned_ms).replace("%INSERT%", genned_insert).replace("%TRACKED%", genned_tracked).replace("%UNTRACKED%", genned_untracked).replace("%TRANSCRIPT%", genned_transcript)
    paper1 = paper1.replace("June Specimen", "Specimen")
    paper2 = gen_paper("German", "2")

    paper_segments = [paper1, paper2]

    return subject_template.replace("%NAME%", "German").replace("%PAPERS%", "\n".join(paper_segments))

def gen_paper(subject, paper):
    years = sorted(list(set([ f.name.split(" ")[1] for f in os.scandir(f"papers/{subject}/{paper}") ])))
    years = [year for year in years if year.isdigit()]
    print(years)
    gened_qp_segment = ""
    gened_ms_segment = ""
    gened_qp_segment += single_template.replace("%NAME%", f"Specimen QP").replace("%URL%", f"papers/{subject}/{paper}/Specimen QP.pdf")
    gened_ms_segment += single_template.replace("%NAME%", f"Specimen MS").replace("%URL%", f"papers/{subject}/{paper}/Specimen MS.pdf")
    for year in years:
        qp_url = f"papers/{subject}/{paper}/June {year} QP.pdf"
        ms_url = f"papers/{subject}/{paper}/June {year} MS.pdf"
        gened_qp_segment += single_template.replace("%NAME%", f"June {year} QP").replace("%URL%", qp_url)
        gened_ms_segment += single_template.replace("%NAME%", f"June {year} MS").replace("%URL%", ms_url)

    return segment_template.replace("%QP%", gened_qp_segment).replace("%MS%", gened_ms_segment).replace("%PAPER%", f"Paper {paper}")

for subject in subjects:
    paper_segments = []
    papers = [ f.name for f in os.scandir(f"papers/{subject}") if f.is_dir() ]
    print(papers)
    for paper in papers:
        paper_segments.append(gen_paper(subject, paper))

    subject_segments.append(subject_template.replace("%NAME%", subject).replace("%PAPERS%", "\n".join(paper_segments)))

# GERMAN IS WEIRD BC LISTENINGS EXIST RAHH RAHH RAHH
subject_segments.append(do_german())

page = page_template.replace("%SUBJECTS%", "\n".join(subject_segments))
with open("index.html", "w") as f:
    f.write(page)