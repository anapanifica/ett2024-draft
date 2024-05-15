from pathlib import Path
import csv

def generate_talk(line):
    id = line[0]
    authors = line[1].split(",")
    title = line[2]
    bottom = [
        "categories:\n",
        "  - Presentation\n",
        "hide: false\n",
        "---"
    ]
    with open(Path(__file__).resolve().parent / "_talks" / f"talk_{authors[0].strip().split(" ", 1)[1].lower().replace(" ", "")}.md", "w") as fout:
        fout.write("---\n")
        fout.write(f'name: "{title}"\n')
        fout.write("speakers:\n")
        for author in authors:
            fout.write(f"  - {author.strip()}\n")
        fout.write("links:\n")
        fout.write("  - name: Abstract\n")
        fout.write(f"    relative_url: /abstracts/{authors[0].strip().split(" ", 1)[1].lower().replace(" ", "")}.pdf\n")
        fout.write("    icon: file\n")
        fout.writelines(bottom)

    for author in authors:
        fname, lname = author.strip().split(" ", 1)
        with open(Path(__file__).resolve().parent / "_speakers" / f"{lname.strip().lower().replace(" ", "")}.md", "w") as fout:
            fout.write("---\n")
            fout.write(f'name: {author}\n')
            fout.write(f'first_name: {fname}\n')
            fout.write(f'last_name: {lname}\n')
            fout.write("hide: true\n")
            fout.write("---")

def generate_talks(filename):
    with open(Path(__file__).resolve().parent / filename, "r") as fin:
        fin_reader = csv.reader(fin, delimiter=";")
        for line in fin_reader:
            generate_talk(line)

if __name__ == "__main__":
    generate_talks("accepted_talks.csv")