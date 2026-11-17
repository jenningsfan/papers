import os

subjects = ["Maths", "Further Maths", "Physics", "German"]
years = range(2019, 2026)
papers = range(1, 4)
subject_segments = []

single_template = open("template_paper_single.html", "r").read()
segment_template = open("template_paper_segment.html", "r").read()
page_template = open("template_page.html", "r").read()
subject_template = open("template_subject.html", "r").read()

for subject in subjects:
    paper_segments = []
    papers = [ f.name for f in os.scandir(f"papers/{subject}") if f.is_dir() ]
    print(papers)
    for paper in papers:
        years = sorted(list(set([ f.name.split(" ")[1] for f in os.scandir(f"papers/{subject}/{paper}") ])))

        print(years)

        gened_qp_segment = ""
        gened_ms_segment = ""
        for year in years:
            qp_url = f"papers/{subject}/{paper}/June {year} QP.pdf"
            ms_url = f"papers/{subject}/{paper}/June {year} MS.pdf"
            gened_qp_segment += single_template.replace("%NAME%", f"June {year} QP").replace("%URL%", qp_url)
            gened_ms_segment += single_template.replace("%NAME%", f"June {year} MS").replace("%URL%", ms_url)

        paper_segments.append(segment_template.replace("%QP%", gened_qp_segment).replace("%MS%", gened_ms_segment).replace("%PAPER%", f"Paper {paper}"))

    subject_segments.append(subject_template.replace("%NAME%", subject).replace("%PAPERS%", "\n".join(paper_segments)))

page = page_template.replace("%SUBJECTS%", "\n".join(subject_segments))
with open("index.html", "w") as f:
    f.write(page)